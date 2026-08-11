#!/usr/bin/env python3
"""Sweep manuscript artifacts after a numeric change and verify ledger provenance.

The standard-library-only scanner reads plain text files, all Word paragraph/table
text in DOCX XML, and every worksheet/shared string in XLSX files.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json", ".tex"}
SCAN_SUFFIXES = TEXT_SUFFIXES | {".docx", ".xlsx"}
REQUIRED_LEDGER_FIELDS = {
    "result_id",
    "display_value",
    "source_dta",
    "source_do",
    "source_log",
    "source_locator",
    "verification_status",
}
VALID_STATUSES = {
    "generated",
    "corrected_pending_independent_recheck",
    "verified",
}
TAG_RE = re.compile(r"<[^>]+>")


def xml_text(data: bytes) -> str:
    text = data.decode("utf-8", errors="ignore")
    text = re.sub(r"</(?:w:p|w:tr|row)>", "\n", text)
    text = TAG_RE.sub(" ", text)
    return html.unescape(re.sub(r"[ \t]+", " ", text))


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        parts = [name for name in archive.namelist() if name.startswith("word/") and name.endswith(".xml")]
        return "\n".join(xml_text(archive.read(name)) for name in sorted(parts))


def read_xlsx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        wanted = [name for name in names if name == "xl/sharedStrings.xml" or re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name)]
        return "\n".join(xml_text(archive.read(name)) for name in sorted(wanted))


def read_artifact(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return read_docx(path)
    if path.suffix.lower() == ".xlsx":
        return read_xlsx(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def load_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_LEDGER_FIELDS - fields)
        if missing:
            raise ValueError(f"ledger missing required columns: {', '.join(missing)}")
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    errors: list[str] = []
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        result_id = row["result_id"]
        if not result_id:
            errors.append(f"line {line}: blank result_id")
        elif result_id in seen:
            errors.append(f"line {line}: duplicate result_id {result_id}")
        seen.add(result_id)
        if not row["display_value"]:
            errors.append(f"line {line}: {result_id or '?'} has blank display_value")
        if row["verification_status"] not in VALID_STATUSES:
            errors.append(f"line {line}: {result_id or '?'} has invalid verification_status")
        for field in ("source_dta", "source_do", "source_log", "source_locator"):
            if not row[field]:
                errors.append(f"line {line}: {result_id or '?'} missing {field}")
    return rows, errors


def artifacts(root: Path, ledger: Path, report: Path) -> list[Path]:
    skip_dirs = {".git", ".venv", "node_modules", "__pycache__"}
    found: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.name.startswith("NUMERIC_SWEEP_REPORT") or path.name.startswith("NUMERIC_SWEEP_"):
            continue
        if path.resolve() in {ledger.resolve(), report.resolve()}:
            continue
        found.append(path)
    return sorted(found)


def locate(text: str, token: str) -> list[int]:
    return [text.count("\n", 0, match.start()) + 1 for match in re.finditer(re.escape(token), text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--ledger", default="analysis/results-ledger.csv")
    parser.add_argument("--changed", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--out", default="analysis/outputs/NUMERIC_SWEEP_REPORT.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ledger = (root / args.ledger).resolve() if not Path(args.ledger).is_absolute() else Path(args.ledger)
    report = (root / args.out).resolve() if not Path(args.out).is_absolute() else Path(args.out)
    rows, errors = load_ledger(ledger)
    for row in rows:
        for field in ("source_dta", "source_do", "source_log"):
            source = Path(row[field])
            source = source if source.is_absolute() else root / source
            if not source.is_file():
                errors.append(f"{row['result_id']}: {field} does not exist: {source}")
        log_path = Path(row["source_log"])
        log_path = log_path if log_path.is_absolute() else root / log_path
        if log_path.is_file():
            log_text = log_path.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"\br\([1-9]\d*\);", log_text):
                errors.append(f"{row['result_id']}: STATA error return code found in {log_path}")

    changes: list[tuple[str, str]] = []
    for item in args.changed:
        if "=" not in item:
            errors.append(f"invalid --changed value: {item!r}; expected OLD=NEW")
            continue
        old, new = item.split("=", 1)
        if not old or not new:
            errors.append(f"invalid --changed value: {item!r}; OLD and NEW are required")
        else:
            changes.append((old, new))

    corpus: dict[Path, str] = {}
    for path in artifacts(root, ledger, report):
        try:
            corpus[path] = read_artifact(path)
        except Exception as exc:  # fail closed and report unreadable artifacts
            errors.append(f"could not scan {path.relative_to(root)}: {exc}")

    lines = ["# Numeric sweep report", "", f"- Files scanned: {len(corpus)}", f"- Ledger rows: {len(rows)}", ""]
    lines.append("## Ledger value occurrences")
    for row in rows:
        token = row["display_value"]
        hits = []
        for path, text in corpus.items():
            positions = locate(text, token)
            if positions:
                hits.append(f"{path.relative_to(root)}:{','.join(map(str, positions))}")
        lines.append(f"- `{row['result_id']}` = `{token}` -> " + ("; ".join(hits) if hits else "not yet used"))

    lines.extend(["", "## Changed-value sweep"])
    for old, new in changes:
        stale = []
        fresh = []
        for path, text in corpus.items():
            if old in text:
                stale.append(str(path.relative_to(root)))
            if new in text:
                fresh.append(str(path.relative_to(root)))
        lines.append(f"- `{old}` -> `{new}`: old occurrences={len(stale)}, new occurrences={len(fresh)}")
        if stale:
            errors.append(f"stale value {old!r} remains in: {', '.join(stale)}")

    lines.extend(["", "## Gate result"])
    lines.extend([f"- FAIL: {error}" for error in errors] or ["- PASS: no stale changed values or ledger-schema/provenance errors detected."])
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"scanned {len(corpus)} files; report={report}; errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
