#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.csv"
REQUIRED = {
    "id", "title", "evidence_grade", "status", "work_model", "client_type",
    "reported_result", "source_url", "repo_url", "pinned_commit",
    "license_status", "difficulty", "tr_sellability", "notes"
}
GRADES = {"A", "B", "C", "X"}
SELLABILITY = {"high", "medium", "low"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if not CATALOG.exists():
        fail("catalog.csv not found")

    with CATALOG.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED - fields
        if missing:
            fail(f"missing columns: {sorted(missing)}")

        seen = set()
        count = 0
        for line_no, row in enumerate(reader, start=2):
            count += 1
            item_id = row["id"].strip()
            if not item_id:
                fail(f"line {line_no}: empty id")
            if item_id in seen:
                fail(f"line {line_no}: duplicate id {item_id}")
            seen.add(item_id)

            grade = row["evidence_grade"].strip()
            if grade not in GRADES:
                fail(f"line {line_no}: invalid grade {grade!r}")

            sellability = row["tr_sellability"].strip()
            if sellability not in SELLABILITY:
                fail(f"line {line_no}: invalid tr_sellability {sellability!r}")

            source = row["source_url"].strip()
            if not source.startswith(("https://", "http://")):
                fail(f"line {line_no}: invalid source_url")

            repo = row["repo_url"].strip()
            commit = row["pinned_commit"].strip()
            if grade in {"A", "B", "X"}:
                if not repo.startswith("https://github.com/"):
                    fail(f"line {line_no}: grade {grade} requires GitHub repo")
                if len(commit) != 40 or any(c not in "0123456789abcdefABCDEF" for c in commit):
                    fail(f"line {line_no}: invalid pinned commit SHA")

            if grade == "A" and row["status"].strip() != "verified_exact_repo":
                fail(f"line {line_no}: grade A must use status=verified_exact_repo")

    print(f"catalog OK: {count} records")


if __name__ == "__main__":
    main()
