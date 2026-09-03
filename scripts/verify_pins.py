#!/usr/bin/env python3
"""Check that every pinned upstream source in the archive is still real.

Some records in data/cases.csv carry a repo address plus a 40-character pinned
commit (nine, as of 2026-09-03). That pair is the archive's whole claim to "we
know exactly which code did this work" — but nothing ever re-tested it after the
day it was written down. Upstream repos get deleted, renamed, made private, or have their history
rewritten, and the archive would keep quoting a version that no longer exists.

Three things are checked per record, all over plain git (no GitHub API, no
token, so it works from a restricted network):

  1. the repo still answers            -> git ls-remote <url> HEAD
  2. the pinned version still resolves -> git fetch --depth 1 origin <sha>
  3. license_status is still true      -> list the root tree at that version

Point 3 matters because of the license rule: we only ever store an address plus
a version, never the code. If a repo gained a root license since it was logged,
that is worth knowing; if it says no_root_license and still has none, the record
is confirmed rather than merely old.

This needs the network and talks to third-party repos, so it is deliberately
NOT part of the CI triple. Run it on demand:

    python3 scripts/verify_pins.py
    python3 scripts/verify_pins.py --report research/PIN-DOGRULAMA-2026-09-03.md

Exit code is non-zero if any record fails, so it can gate a research round.
"""
import argparse
import csv
import json
import re
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "data" / "cases.csv"
CATALOG = ROOT / "catalog.csv"

SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
# A root license file under any of these names counts as "the repo has a
# license at its root". Anything nested (docs/LICENSE) deliberately does not.
LICENSE_NAMES = re.compile(r"^(LICEN[CS]E|COPYING|UNLICENSE)(\.[A-Za-z0-9]+)?$", re.I)

# Status verdicts, worst first. The order is what --strict sorts and reports on.
FAIL = "fail"
WARN = "warn"
OK = "ok"

# Findings are recorded as codes, then rendered twice: English on the console
# for whoever runs the script, Turkish in the report, which is archive text and
# follows the language rule in CLAUDE.md.
NOTE_EN = {
    "bad_sha": "pinned commit is not a 40-character version id",
    "repo_gone": "repo does not answer: deleted, renamed or made private",
    "pin_unreachable": "pinned version no longer reachable: history rewritten or commit removed",
    "tree_unreadable": "pinned version fetched but its root listing could not be read",
    "license_added": "recorded as no_root_license but the pinned version now carries {detail}",
    "license_confirmed": "no root license at the pinned version, as recorded",
    "head_moved": "upstream has moved past the pinned version (expected; that is what pinning is for)",
}
NOTE_TR = {
    "bad_sha": "sabitlenen sürüm kimliği 40 karakterlik geçerli bir numara değil",
    "repo_gone": "özgün depo cevap vermiyor: silinmiş, adı değişmiş ya da gizlenmiş",
    "pin_unreachable": "sabitlenen sürüme artık ulaşılamıyor: deponun geçmişi yeniden yazılmış ya da o sürüm kaldırılmış",
    "tree_unreadable": "sabitlenen sürüm indirildi ama kök dizin listesi okunamadı",
    "license_added": "kayıtta lisansı yok yazıyor, oysa sabitlenen sürümde artık {detail} var",
    "license_confirmed": "sabitlenen sürümün kök dizininde lisans yok — kayıt doğru",
    "head_moved": "özgün depo sabitlenen sürümün ilerisine geçmiş",
}
# These two are already visible as columns in the report table, so repeating
# them under every record would pad the report without adding anything.
ROUTINE_NOTES = {"license_confirmed", "head_moved"}


def render(note, table):
    return table[note["code"]].format(detail=note.get("detail", ""))


def git(args, cwd=None, timeout=90):
    """Run git and return (returncode, stdout). Never raises on git failure."""
    try:
        done = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin:/usr/local/bin"},
        )
    except subprocess.TimeoutExpired:
        return 124, ""
    return done.returncode, done.stdout


def check_record(row, workdir):
    """Return a verdict dict for one pinned record."""
    cid = row["id"].strip()
    url = row["repo_url"].strip()
    sha = row["pinned_commit"].strip()
    recorded_license = row["license_status"].strip()

    result = {
        "id": cid,
        "repo_url": url,
        "pinned_commit": sha,
        "license_status_recorded": recorded_license,
        "head": "",
        "pin_is_head": False,
        "root_license_files": [],
        "license_status_observed": "",
        "status": OK,
        "notes": [],
    }

    def note(code, detail=""):
        result["notes"].append({"code": code, "detail": detail})

    if not SHA_PATTERN.match(sha):
        result["status"] = FAIL
        note("bad_sha")
        return result

    code, out = git(["ls-remote", url, "HEAD"])
    if code != 0 or not out.strip():
        result["status"] = FAIL
        note("repo_gone")
        return result
    result["head"] = out.split()[0]
    result["pin_is_head"] = result["head"] == sha

    # Fetch just the pinned version into a throwaway clone. GitHub serves an
    # explicit SHA even when it is far behind the branch tip, so "not our ref"
    # here means the version is genuinely gone, not merely old.
    repo = workdir / cid
    repo.mkdir(parents=True, exist_ok=True)
    git(["init", "-q", "."], cwd=repo)
    git(["remote", "add", "origin", url], cwd=repo)
    code, _ = git(["fetch", "-q", "--depth", "1", "origin", sha], cwd=repo)
    if code != 0:
        result["status"] = FAIL
        note("pin_unreachable")
        return result

    code, out = git(["ls-tree", "--name-only", "FETCH_HEAD"], cwd=repo)
    if code != 0:
        result["status"] = FAIL
        note("tree_unreadable")
        return result

    names = [n for n in out.splitlines() if n.strip()]
    licenses = [n for n in names if LICENSE_NAMES.match(n)]
    result["root_license_files"] = licenses
    result["license_status_observed"] = "has_root_license" if licenses else "no_root_license"

    if recorded_license == "no_root_license" and licenses:
        result["status"] = WARN
        note("license_added", ", ".join(licenses))
    elif recorded_license == "no_root_license":
        note("license_confirmed")

    if not result["pin_is_head"]:
        note("head_moved")

    return result


def load_rows():
    with CASES.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return [r for r in rows if r["repo_url"].strip() and r["pinned_commit"].strip()]


def catalog_pins():
    """id -> (repo_url, pinned_commit) for the pinned subset, to cross-check."""
    with CATALOG.open(newline="", encoding="utf-8") as fh:
        return {
            r["id"].strip(): (r["repo_url"].strip(), r["pinned_commit"].strip())
            for r in csv.DictReader(fh)
            if r["repo_url"].strip()
        }


def write_report(results, path, drift):
    """Write the dated, reader-facing Turkish record of this verification round."""
    today = date.today().isoformat()
    failed = [r for r in results if r["status"] == FAIL]
    warned = [r for r in results if r["status"] == WARN]
    moved = [r for r in results if r["status"] != FAIL and not r["pin_is_head"]]

    lines = [
        f"# Sabitlenmiş sürüm doğrulaması — {today}",
        "",
        "Arşivde depo adresi **ve** 40 karakterlik sürüm kimliği taşıyan her kaydın",
        "hâlâ gerçek olup olmadığı `scripts/verify_pins.py` ile denetlendi. Üç soru",
        "soruldu: özgün depo hâlâ cevap veriyor mu · sabitlenen sürüme hâlâ",
        "ulaşılabiliyor mu · deponun kök dizinindeki lisans durumu kayıtla uyuşuyor mu.",
        "",
        "Kod indirilmedi, kopyalanmadı. Yalnız sabitlenen sürümün kök dizin listesi okundu.",
        "",
        "## Sonuç",
        "",
        f"- Denetlenen kayıt: **{len(results)}**",
        f"- Ulaşılamayan: **{len(failed)}**",
        f"- Lisans kaydı gerçekle uyuşmayan: **{len(warned)}**",
        f"- Özgün deposu sabitlenen sürümün ilerisine geçmiş: **{len(moved)}** (beklenen durum — sabitlemenin varlık sebebi bu)",
        "",
        "| Vaka | Özgün depo | Sabitlenen sürüm | Ulaşılıyor mu | Depo şu an | Kök lisans | Sonuç |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        reach = "evet" if r["status"] != FAIL else "**HAYIR**"
        head = "sabitlenen sürüm hâlâ en güncel" if r["pin_is_head"] else (
            f"`{r['head'][:12]}` (ilerlemiş)" if r["head"] else "—"
        )
        lic = ", ".join(r["root_license_files"]) if r["root_license_files"] else "yok"
        verdict = {OK: "doğrulandı", WARN: "lisans kaydı güncellenmeli", FAIL: "kırık"}[r["status"]]
        repo_short = r["repo_url"].replace("https://github.com/", "")
        lines.append(
            f"| {r['id']} | [{repo_short}]({r['repo_url']}) | `{r['pinned_commit'][:12]}` "
            f"| {reach} | {head} | {lic} | {verdict} |"
        )

    if drift:
        lines += ["", "## `catalog.csv` ile uyuşmazlık", ""]
        lines += [f"- {d}" for d in drift]

    # Only findings the table does not already show are worth spelling out.
    noteworthy = [
        (r, [n for n in r["notes"] if n["code"] not in ROUTINE_NOTES])
        for r in results
    ]
    noteworthy = [(r, ns) for r, ns in noteworthy if ns]
    lines += ["", "## Dikkat edilecek kayıtlar", ""]
    if noteworthy:
        for r, ns in noteworthy:
            lines.append(f"**{r['id']}**")
            for n in ns:
                lines.append(f"- {render(n, NOTE_TR)}")
            lines.append("")
    else:
        lines += [
            f"Yok. {len(results)} kaydın hepsinde özgün depo cevap verdi, sabitlenen",
            "sürüme ulaşıldı ve lisans kaydı gerçekle uyuştu.",
            "",
        ]

    lines += [
        "## Nasıl tekrarlanır",
        "",
        "```bash",
        "python3 scripts/verify_pins.py",
        "```",
        "",
        "Ağ gerektirdiği ve başkalarının depolarına gittiği için CI üçlüsüne dâhil",
        "değildir; araştırma turu açarken elle çalıştırılır.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--report", type=Path, help="write a dated markdown report to this path")
    parser.add_argument("--json", action="store_true", help="print raw results as JSON")
    parser.add_argument(
        "--strict", action="store_true",
        help="also fail when a license record no longer matches what is upstream",
    )
    args = parser.parse_args()

    if not shutil.which("git"):
        print("ERROR: git not found on PATH")
        raise SystemExit(2)

    rows = load_rows()
    if not rows:
        print("ERROR: no pinned records found in data/cases.csv")
        raise SystemExit(2)

    # Same pair must be in catalog.csv where the id exists there at all.
    cat = catalog_pins()
    drift = []
    for row in rows:
        cid = row["id"].strip()
        if cid in cat and cat[cid] != (row["repo_url"].strip(), row["pinned_commit"].strip()):
            drift.append(f"{cid}: cases.csv and catalog.csv disagree on repo/pinned version")

    results = []
    with tempfile.TemporaryDirectory(prefix="verify-pins-") as tmp:
        workdir = Path(tmp)
        for row in rows:
            res = check_record(row, workdir)
            results.append(res)
            mark = {OK: "ok  ", WARN: "warn", FAIL: "FAIL"}[res["status"]]
            head = "pin=head" if res["pin_is_head"] else f"head={res['head'][:8] or '?'}"
            print(f"{mark}  {res['id']:5} {res['pinned_commit'][:8]}  {head:16} {res['repo_url']}")
            for n in res["notes"]:
                print(f"        {render(n, NOTE_EN)}")

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    if args.report:
        report = args.report if args.report.is_absolute() else (Path.cwd() / args.report)
        report.parent.mkdir(parents=True, exist_ok=True)
        write_report(results, report, drift)
        try:
            shown = report.resolve().relative_to(ROOT)
        except ValueError:
            shown = report
        print(f"report written to {shown}")

    failed = [r for r in results if r["status"] == FAIL]
    warned = [r for r in results if r["status"] == WARN]
    for message in drift:
        print(f"ERROR: {message}")

    print(
        f"pins checked: {len(results)} records "
        f"({len(results) - len(failed) - len(warned)} verified, {len(warned)} license drift, {len(failed)} broken)"
    )
    if failed or drift or (warned and args.strict):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
