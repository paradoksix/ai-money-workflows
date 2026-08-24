#!/usr/bin/env python3
"""Catalog Doctor MVP.

Audits and cleans product CSV files without overwriting the source.
Optional Ollama enrichment keeps the AI step local/free when Ollama is available.
Standard-library only.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

TITLE_CANDIDATES = ("title", "name", "product_name", "product", "urun_adi", "ürün_adı", "urun")
DESC_CANDIDATES = ("description", "desc", "product_description", "aciklama", "açıklama")
CATEGORY_CANDIDATES = ("category", "product_category", "kategori")
SKU_CANDIDATES = ("sku", "stock_code", "product_code", "stok_kodu", "urun_kodu", "ürün_kodu")


def norm_key(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").strip().casefold()
    value = re.sub(r"\s+", " ", value)
    return value


def clean_cell(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("\u00a0", " ")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\s*\n\s*", "\n", value)
    return value.strip()


def choose_column(fieldnames: list[str], candidates: tuple[str, ...]) -> str | None:
    normalized = {norm_key(name).replace(" ", "_"): name for name in fieldnames}
    for candidate in candidates:
        key = norm_key(candidate).replace(" ", "_")
        if key in normalized:
            return normalized[key]
    return None


def ollama_json(model: str, prompt: str, base_url: str, timeout: int) -> dict[str, Any]:
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1},
    }).encode("utf-8")
    request = urllib.request.Request(
        base_url.rstrip("/") + "/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        outer = json.loads(response.read().decode("utf-8"))
    raw = outer.get("response", "{}")
    parsed = json.loads(raw)
    return parsed if isinstance(parsed, dict) else {}


def ai_suggestion(
    row: dict[str, str],
    title_col: str | None,
    desc_col: str | None,
    category_col: str | None,
    model: str,
    base_url: str,
    timeout: int,
) -> dict[str, str]:
    title = row.get(title_col, "") if title_col else ""
    description = row.get(desc_col, "") if desc_col else ""
    category = row.get(category_col, "") if category_col else ""
    prompt = f"""You clean e-commerce product catalog data.
Return ONLY a JSON object with these string keys:
clean_title, suggested_category, reason, confidence.
Do not invent specs, brands, dimensions, compatibility, certifications or facts not present in the input.
Keep clean_title concise and preserve factual product identity.
If there is not enough evidence for a category, suggested_category must be an empty string.
confidence must be one of: high, medium, low.

TITLE: {title[:500]}
DESCRIPTION: {description[:1500]}
CURRENT_CATEGORY: {category[:300]}
"""
    result = ollama_json(model, prompt, base_url, timeout)
    return {
        "ai_clean_title": clean_cell(str(result.get("clean_title", ""))),
        "ai_suggested_category": clean_cell(str(result.get("suggested_category", ""))),
        "ai_reason": clean_cell(str(result.get("reason", ""))),
        "ai_confidence": clean_cell(str(result.get("confidence", ""))).lower(),
    }


def audit_csv(args: argparse.Namespace) -> int:
    src = Path(args.input)
    if not src.exists():
        print(f"ERROR: input not found: {src}", file=sys.stderr)
        return 2

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    with src.open("r", encoding=args.encoding, newline="") as fh:
        sample = fh.read(4096)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(fh, dialect=dialect)
        fieldnames = list(reader.fieldnames or [])
        if not fieldnames:
            print("ERROR: CSV header not found", file=sys.stderr)
            return 2
        rows = [{key: clean_cell(value or "") for key, value in row.items()} for row in reader]

    title_col = choose_column(fieldnames, TITLE_CANDIDATES)
    desc_col = choose_column(fieldnames, DESC_CANDIDATES)
    category_col = choose_column(fieldnames, CATEGORY_CANDIDATES)
    sku_col = choose_column(fieldnames, SKU_CANDIDATES)

    title_groups: dict[str, list[int]] = defaultdict(list)
    sku_groups: dict[str, list[int]] = defaultdict(list)
    if title_col:
        for idx, row in enumerate(rows, start=2):
            key = norm_key(row.get(title_col, ""))
            if key:
                title_groups[key].append(idx)
    if sku_col:
        for idx, row in enumerate(rows, start=2):
            key = norm_key(row.get(sku_col, ""))
            if key:
                sku_groups[key].append(idx)

    duplicate_title_rows = {n for group in title_groups.values() if len(group) > 1 for n in group}
    duplicate_sku_rows = {n for group in sku_groups.values() if len(group) > 1 for n in group}

    audit_rows: list[dict[str, str]] = []
    cleaned_rows: list[dict[str, str]] = []
    issue_counts: Counter[str] = Counter()
    ai_failures = 0
    ai_used = 0

    for csv_line, row in enumerate(rows, start=2):
        issues: list[str] = []
        empty_fields = [name for name in fieldnames if not row.get(name, "").strip()]
        if empty_fields:
            issues.append("missing_fields")
            issue_counts["missing_fields"] += 1
        if title_col and not row.get(title_col, ""):
            issues.append("missing_title")
            issue_counts["missing_title"] += 1
        if category_col and not row.get(category_col, ""):
            issues.append("missing_category")
            issue_counts["missing_category"] += 1
        if csv_line in duplicate_title_rows:
            issues.append("duplicate_title")
            issue_counts["duplicate_title"] += 1
        if csv_line in duplicate_sku_rows:
            issues.append("duplicate_sku")
            issue_counts["duplicate_sku"] += 1

        suggestion = {
            "ai_clean_title": "",
            "ai_suggested_category": "",
            "ai_reason": "",
            "ai_confidence": "",
        }
        should_use_ai = bool(args.ollama_model) and (args.ai_all or bool(issues))
        if should_use_ai:
            try:
                suggestion = ai_suggestion(
                    row, title_col, desc_col, category_col,
                    args.ollama_model, args.ollama_url, args.timeout,
                )
                ai_used += 1
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
                ai_failures += 1
                suggestion["ai_reason"] = f"AI unavailable: {type(exc).__name__}"
                suggestion["ai_confidence"] = "error"

        review_required = bool(issues)
        if suggestion["ai_confidence"] in {"low", "error"}:
            review_required = True

        audit_rows.append({
            "csv_line": str(csv_line),
            "sku": row.get(sku_col, "") if sku_col else "",
            "title": row.get(title_col, "") if title_col else "",
            "issues": ";".join(issues),
            "missing_fields": ";".join(empty_fields),
            "review_required": "yes" if review_required else "no",
            **suggestion,
        })
        cleaned_rows.append({**row, **suggestion, "review_required": "yes" if review_required else "no"})

    cleaned_fields = fieldnames + [
        "ai_clean_title", "ai_suggested_category", "ai_reason", "ai_confidence", "review_required"
    ]
    with (out_dir / "cleaned.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=cleaned_fields)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    audit_fields = [
        "csv_line", "sku", "title", "issues", "missing_fields", "review_required",
        "ai_clean_title", "ai_suggested_category", "ai_reason", "ai_confidence",
    ]
    with (out_dir / "audit.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=audit_fields)
        writer.writeheader()
        writer.writerows(audit_rows)

    summary = {
        "source": str(src),
        "rows": len(rows),
        "columns": len(fieldnames),
        "detected_columns": {
            "title": title_col,
            "description": desc_col,
            "category": category_col,
            "sku": sku_col,
        },
        "issue_counts": dict(issue_counts),
        "review_required_rows": sum(r["review_required"] == "yes" for r in audit_rows),
        "ai": {
            "enabled": bool(args.ollama_model),
            "model": args.ollama_model or None,
            "rows_processed": ai_used,
            "failures": ai_failures,
        },
        "outputs": {"audit": "audit.csv", "cleaned": "cleaned.csv"},
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit/clean a product catalog CSV without modifying the source.")
    parser.add_argument("input", help="Input CSV path")
    parser.add_argument("--out", default="catalog-doctor-output", help="Output directory")
    parser.add_argument("--encoding", default="utf-8-sig", help="Input encoding")
    parser.add_argument("--ollama-model", default="", help="Optional local Ollama model, e.g. qwen2.5:7b")
    parser.add_argument("--ollama-url", default="http://localhost:11434", help="Ollama base URL")
    parser.add_argument("--timeout", type=int, default=60, help="Ollama request timeout seconds")
    parser.add_argument("--ai-all", action="store_true", help="Run AI suggestion for every row instead of issue rows only")
    return parser


if __name__ == "__main__":
    raise SystemExit(audit_csv(build_parser().parse_args()))
