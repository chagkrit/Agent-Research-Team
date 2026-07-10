#!/usr/bin/env python3
"""citation_audit.py — ตรวจ citation ในร่างเทียบกับ synthesis-matrix.csv

Heuristic ชั้นแรก ไม่ใช่คำตัดสินสุดท้าย: จับรูปแบบ author-year (ไทย/อังกฤษ,
พ.ศ./ค.ศ.) แล้วเทียบกับรายการในคลัง รองรับ draft เป็น .md/.txt/.docx และ
library เป็น .csv (synthesis-matrix.csv จาก lr-builder, คอลัมน์ paper_id/authors/
year/title), .bib (BibTeX), .json (CSL-JSON) — ถ้ามีไฟล์ export จาก reference
manager ภายนอกอยู่แล้วก็ยังใช้ได้เหมือนเดิม

ข้อจำกัดที่ผู้ใช้ต้องรู้:
- ใช้ไม่ได้กับระบบอ้างอิงแบบตัวเลข (Vancouver) — ต้องตรวจมือ
- จับ "(ชื่อ, ปี)" และ "ชื่อ (ปี)" เป็นหลัก รูปแบบนอกเหนือจากนี้อาจหลุด
- ผล MATCHED ยังควรสุ่มตรวจด้วยตาเพิ่มเสมอ

Usage:
    python citation_audit.py --draft draft.md --library export.csv --out audit-report.md
"""
import argparse
import csv
import json
import re
import sys
import zipfile
from pathlib import Path

YEAR_RE = r"(?:19\d{2}|20\d{2}|24\d{2}|25\d{2})"
# (Name, 2019) | (Name et al., 2019; Other, 2020) | (สมชาย ใจดี, 2560)
PAREN_CITE_RE = re.compile(r"\(([^()]{2,120}?,\s*" + YEAR_RE + r"[^()]*)\)")
# Name (2019) | สมชาย ใจดี (2560) | Smith et al. (2019)
NARRATIVE_CITE_RE = re.compile(
    r"([A-Z][A-Za-z\-']+(?:\s+et\s+al\.?)?|[\u0E00-\u0E7F][\u0E00-\u0E7F\s\.]{1,60}?)"
    r"\s*\(\s*(" + YEAR_RE + r")[a-z]?\s*\)"
)
INNER_RE = re.compile(r"([^;]{2,120}?),\s*(" + YEAR_RE + r")[a-z]?")
STOPWORDS = {"et", "al", "and", "the", "of", "in", "และ", "คณะ", "และคณะ"}


def read_draft(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return path.read_text(encoding="utf-8", errors="ignore")


def name_tokens(text: str) -> set:
    toks = re.findall(r"[A-Za-z\-']{2,}|[\u0E00-\u0E7F]{2,}", text)
    return {t.lower() for t in toks if t.lower() not in STOPWORDS}


def load_library(path: Path):
    """คืน list ของ dict: {key, authors(set ของ token), years(set ของปีทั้ง พ.ศ./ค.ศ.), label}"""
    items = []

    def add(key, author_text, year_text, label):
        years = set(re.findall(YEAR_RE, str(year_text or "")))
        both = set()
        for y in years:
            yi = int(y)
            both.add(str(yi))
            both.add(str(yi + 543) if yi < 2200 else str(yi - 543))
        items.append({
            "key": key or "?",
            "authors": name_tokens(author_text or ""),
            "years": both,
            "label": (label or "").strip()[:90],
        })

    suffix = path.suffix.lower()
    if suffix == ".csv":
        with open(path, newline="", encoding="utf-8-sig", errors="ignore") as f:
            for row in csv.DictReader(f):
                low = {k.lower().strip(): (v or "") for k, v in row.items() if k}
                add(low.get("key") or low.get("paper_id") or low.get("zotero_key"),
                    low.get("author") or low.get("authors"),
                    low.get("publication year") or low.get("date") or low.get("year"),
                    low.get("title"))
    elif suffix == ".bib":
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"@\w+\s*\{([^,]+),(.*?)(?=\n@|\Z)", text, re.S):
            key, body = m.group(1).strip(), m.group(2)

            def field(name):
                fm = re.search(name + r"\s*=\s*[{\"]([^}\"]*)", body, re.I)
                return fm.group(1) if fm else ""
            add(key, field("author"), field("year") or field("date"), field("title"))
    elif suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        rows = data if isinstance(data, list) else data.get("items", [])
        for it in rows:
            creators = it.get("author") or it.get("creators") or []
            author_text = " ".join(
                " ".join(str(c.get(k, "")) for k in ("family", "lastName", "given", "firstName", "literal", "name"))
                for c in creators if isinstance(c, dict)
            )
            issued = it.get("issued", {})
            year = ""
            if isinstance(issued, dict):
                dp = issued.get("date-parts", [[]])
                year = str(dp[0][0]) if dp and dp[0] else issued.get("raw", "")
            year = year or str(it.get("date", "")) or str(it.get("year", ""))
            add(it.get("id") or it.get("key"), author_text, year, it.get("title", ""))
    else:
        sys.exit(f"ไม่รองรับนามสกุล library: {suffix} (รองรับ .csv .bib .json)")

    if not items:
        sys.exit("อ่าน library ได้ 0 รายการ — ตรวจไฟล์ export อีกครั้ง")
    return items


def extract_citations(text: str):
    """คืน set ของ (raw, frozenset(name_tokens), year)"""
    found = {}
    for m in PAREN_CITE_RE.finditer(text):
        for part in m.group(1).split(";"):
            im = INNER_RE.search(part)
            if im:
                toks = name_tokens(im.group(1))
                if toks:
                    found[(frozenset(toks), im.group(2))] = part.strip()
    for m in NARRATIVE_CITE_RE.finditer(text):
        toks = name_tokens(m.group(1))
        if toks:
            found.setdefault((frozenset(toks), m.group(2)),
                             f"{m.group(1).strip()} ({m.group(2)})")
    return found


def match(cite_toks, cite_year, items):
    hits = []
    for it in items:
        if cite_year in it["years"] and (cite_toks & it["authors"]):
            hits.append(it)
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--library", required=True)
    ap.add_argument("--out", default="audit-report.md")
    args = ap.parse_args()

    text = read_draft(Path(args.draft))
    items = load_library(Path(args.library))
    cites = extract_citations(text)

    matched, unmatched, used_keys = [], [], set()
    for (toks, year), raw in sorted(cites.items(), key=lambda x: x[1]):
        hits = match(set(toks), year, items)
        if hits:
            matched.append((raw, hits[0]["key"]))
            used_keys.update(h["key"] for h in hits)
        else:
            unmatched.append(raw)

    uncited = [it for it in items if it["key"] not in used_keys]

    lines = ["# Audit report — citation integrity", "",
             f"- citation ที่พบในร่าง: {len(cites)}",
             f"- MATCHED: {len(matched)} / UNMATCHED: {len(unmatched)}",
             f"- รายการในคลังที่ยังไม่ถูกอ้าง: {len(uncited)} / {len(items)}", ""]
    lines.append("## UNMATCHED — ต้องแก้ทุกตัวก่อนส่งมอบ (อาจเป็นอ้างอิงผีหรือสะกดคลาด)")
    lines += [f"- ⚠️ {u}" for u in unmatched] or ["- (ไม่มี)"]
    lines.append("")
    lines.append("## MATCHED (สุ่มตรวจด้วยตาเพิ่มอย่างน้อย 10 รายการ)")
    lines += [f"- {raw} → {key}" for raw, key in matched] or ["- (ไม่มี)"]
    lines.append("")
    lines.append("## ในคลังแต่ยังไม่ถูกอ้าง (ตรวจ coverage: ใช้หรือบันทึกเหตุผลที่ไม่ใช้)")
    lines += [f"- {it['key']}: {it['label']}" for it in uncited] or ["- (ไม่มี)"]
    lines.append("")
    lines.append("> หมายเหตุ: สคริปต์นี้เป็น heuristic — ใช้ไม่ได้กับระบบอ้างอิงแบบตัวเลข"
                 " และไม่ทดแทนการตรวจด้วยคน")

    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    print(f"เขียนรายงานที่ {args.out} | MATCHED {len(matched)} | UNMATCHED {len(unmatched)}")
    if unmatched:
        sys.exit(1)


if __name__ == "__main__":
    main()