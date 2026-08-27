#!/usr/bin/env python3
"""Validate data/cases.csv and keep it consistent with catalog.csv and the encyclopedia.

data/cases.csv is the full browsable index of every case (A/B/C/X). catalog.csv
stays the stricter subset that additionally carries a pinned upstream source.
Two cross-checks stop the two files from silently drifting apart:

  A. every id in catalog.csv also exists in cases.csv, and the fields they share
     (grade, status, source_url, repo_url, pinned_commit) are identical;
  B. every id in cases.csv really appears as a heading in the file its
     detail_file column points at.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "data" / "cases.csv"
CATALOG = ROOT / "catalog.csv"

REQUIRED = [
    "id", "title", "niche", "evidence_grade", "status", "revenue_type",
    "reported_amount", "reported_result", "work_model", "client_type", "stack",
    "difficulty", "tr_sellability", "source_url", "repo_url", "pinned_commit",
    "license_status", "detail_file", "summary",
]
SHARED_WITH_CATALOG = [
    "title", "evidence_grade", "status", "work_model", "reported_result",
    "source_url", "repo_url", "pinned_commit",
]

GRADES = {"A", "B", "C", "X"}
SELLABILITY = {"high", "medium", "low"}
REVENUE_TYPES = {"F", "R", "S", "V", ""}
ID_PATTERN = re.compile(r"^[ABCX]\d{3}$")

errors = []


def fail(message):
    errors.append(message)


def check_readme(rows, grade_counts, niches, catalog_count):
    """README.md quotes figures derived from cases.csv; make sure they stay true.

    Each entry is (label, the exact string README must contain). The string is
    built from the data, so editing cases.csv without refreshing README fails
    here instead of silently leaving the front page wrong.
    """
    readme = ROOT / "README.md"
    if not readme.exists():
        fail("README.md not found")
        return 0

    revenue = {}
    sellability = {}
    for row in rows:
        if row["revenue_type"]:
            revenue[row["revenue_type"]] = revenue.get(row["revenue_type"], 0) + 1
        sellability[row["tr_sellability"]] = sellability.get(row["tr_sellability"], 0) + 1

    superseded = sum(1 for r in rows if r["status"].startswith("superseded"))
    archived = len(rows) - grade_counts.get("X", 0) - superseded
    real_niches = len(set(niches) - {"tartismali"})

    expected = [
        ("archived count badge", f"badge/örnek-{archived}-"),
        ("niche count badge", f"badge/iş%20kolu-{real_niches}-"),
        ("verified-source badge", f"badge/kaynağı%20doğrulanmış-{grade_counts.get('A', 0)}-"),
        ("archived count", f"**{archived}** — ayrıca {grade_counts.get('X', 0)} şüpheli"),
        ("total rows", f"{len(rows)} kaydın tamamı"),
        ("grade split", "A: {A} · B: {B} · C: {C} · X: {X}".format(
            A=grade_counts.get("A", 0), B=grade_counts.get("B", 0),
            C=grade_counts.get("C", 0), X=grade_counts.get("X", 0))),
        ("niche count", f"| {real_niches} (+ şüpheliler eki) |"),
        ("pinned sources", f"{sum(1 for r in rows if r['repo_url'])} kayıt (depo adresi"),
        ("source links", f"{sum(1 for r in rows if r['source_url'])} kayıt |"),
        ("revenue split", "F: {F} · S: {S} · R: {R} · V: {V}".format(
            F=revenue.get("F", 0), S=revenue.get("S", 0),
            R=revenue.get("R", 0), V=revenue.get("V", 0))),
        ("sellability split", "Yüksek: {h} · Orta: {m} · Düşük: {l}".format(
            h=sellability.get("high", 0), m=sellability.get("medium", 0),
            l=sellability.get("low", 0))),
        ("catalog core size", f"çekirdek ({catalog_count} kayıt)"),
    ]

    text = readme.read_text(encoding="utf-8")
    for label, needle in expected:
        if needle not in text:
            fail(f"README.md: stale {label} — expected to find {needle!r}. "
                 "Refresh the figure after changing data/cases.csv.")

    # the six A-grade rows quote a short commit; it must match the dataset
    by_id = {r["id"]: r for r in rows}
    for cid, short in re.findall(r"\*\*(A\d{3})\*\*.*?\|\s*`([0-9a-f]{7})`\s*\|", text):
        real = by_id.get(cid, {}).get("pinned_commit", "")
        if not real.startswith(short):
            fail(f"README.md: {cid} quotes commit {short} but the data says {real[:7] or '(none)'}")

    return len(expected)


def main():
    if not CASES.exists():
        raise SystemExit("ERROR: data/cases.csv not found")

    with CASES.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if list(reader.fieldnames or []) != REQUIRED:
            raise SystemExit(
                f"ERROR: column mismatch\n  expected: {REQUIRED}\n  found:    {reader.fieldnames}"
            )
        rows = list(reader)

    seen = set()
    niches = {}
    for line_no, row in enumerate(rows, start=2):
        cid = row["id"].strip()
        where = f"line {line_no} ({cid or '?'})"

        if not ID_PATTERN.match(cid):
            fail(f"{where}: malformed id")
            continue
        if cid in seen:
            fail(f"{where}: duplicate id")
        seen.add(cid)

        if not row["title"].strip():
            fail(f"{where}: empty title")
        if not row["summary"].strip():
            fail(f"{where}: empty summary")

        grade = row["evidence_grade"].strip()
        if grade not in GRADES:
            fail(f"{where}: invalid evidence_grade {grade!r}")
        elif grade != cid[0]:
            fail(f"{where}: grade {grade!r} does not match id prefix")

        if row["revenue_type"].strip() not in REVENUE_TYPES:
            fail(f"{where}: invalid revenue_type {row['revenue_type']!r}")
        if row["tr_sellability"].strip() not in SELLABILITY:
            fail(f"{where}: invalid tr_sellability {row['tr_sellability']!r}")

        niche = row["niche"].strip()
        if not niche:
            fail(f"{where}: empty niche")
        niches.setdefault(niche, []).append(cid)

        source = row["source_url"].strip()
        if source and not source.startswith("https://"):
            fail(f"{where}: source_url must be https or empty")

        repo = row["repo_url"].strip()
        commit = row["pinned_commit"].strip()
        if repo and not repo.startswith("https://github.com/"):
            fail(f"{where}: repo_url must be a GitHub URL or empty")
        if repo and not commit:
            fail(f"{where}: repo_url without pinned_commit")
        if commit and (len(commit) != 40 or not all(ch in "0123456789abcdef" for ch in commit.lower())):
            fail(f"{where}: invalid pinned commit SHA")

    # ── cross-check A: catalog.csv agreement ────────────────────────────────
    by_id = {r["id"].strip(): r for r in rows}
    with CATALOG.open(newline="", encoding="utf-8") as fh:
        catalog_rows = list(csv.DictReader(fh))

    for line_no, cat in enumerate(catalog_rows, start=2):
        cid = cat["id"].strip()
        case = by_id.get(cid)
        if case is None:
            fail(f"catalog.csv line {line_no}: {cid} is missing from data/cases.csv")
            continue
        for field in SHARED_WITH_CATALOG:
            if cat[field].strip() != case[field].strip():
                fail(
                    f"{cid}: {field} differs between catalog.csv "
                    f"({cat[field].strip()!r}) and cases.csv ({case[field].strip()!r})"
                )

    # ── cross-check B: every case is written up where detail_file says ──────
    heading_cache = {}
    for row in rows:
        cid = row["id"].strip()
        rel = row["detail_file"].strip()
        if not rel:
            fail(f"{cid}: empty detail_file")
            continue
        path = ROOT / rel
        if rel not in heading_cache:
            if not path.exists():
                heading_cache[rel] = None
            else:
                text = path.read_text(encoding="utf-8")
                heading_cache[rel] = set(re.findall(r"^#{1,3}\s+([ABCX]\d{3})\b", text, re.M))
        headings = heading_cache[rel]
        if headings is None:
            fail(f"{cid}: detail_file {rel} does not exist")
        elif cid not in headings:
            fail(f"{cid}: no heading for it in {rel}")

    grade_counts = {}
    for row in rows:
        grade_counts[row["evidence_grade"]] = grade_counts.get(row["evidence_grade"], 0) + 1

    # ── cross-check C: the figures quoted in README.md still hold ──────────
    readme_checks = check_readme(rows, grade_counts, niches, len(catalog_rows))

    if errors:
        print(f"ERROR: {len(errors)} problem(s) found")
        for message in errors:
            print(f"  - {message}")
        raise SystemExit(1)

    summary = " ".join(f"{g}={grade_counts.get(g, 0)}" for g in "ABCX")
    print(f"cases OK: {len(rows)} records ({summary}) across {len(niches)} niches")
    print(f"catalog cross-check OK: {len(catalog_rows)} pinned-source records agree")
    print(f"README cross-check OK: {readme_checks} quoted figures match the data")


if __name__ == "__main__":
    main()
