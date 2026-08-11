# เฟส 5 — Drafting + Audit

เฟสนี้ห้ามเริ่มถ้า gap-argument.md ยังไม่ถูกยืนยัน การเขียนคืองานที่ง่ายที่สุดในระบบ — ความแข็งของส่วนนี้ถูกตัดสินไปแล้วในเฟส 2–4

เช็คโหมดใน project-config.md ก่อนเริ่มเสมอ — โครงบทและกติกาความยาวต่างกันชัดเจนระหว่างโหมด A กับ B

ก่อนร่าง รัน `ls -la -t` ที่ references/drafts/manuscript และบันทึกไฟล์ปัจจุบัน ห้ามเชื่อ memory/note อย่างเดียว ตรวจว่า matrix ทุกแถวที่จะใช้มี live connector/tool + query, PMID/DOI ที่ resolve จริง, และ quartile Q1/Q2 พร้อม source/category/year/verified_at

## 5.1a โครง — โหมด A: Introduction section ของ IMRAD

ใช้โครงจาก config ถ้า author guidelines ระบุไว้ ถ้า config ระบุว่าใช้ default ให้ใช้โครงมาตรฐานนี้และแจ้งผู้ใช้อีกครั้ง:

```
Introduction
  ¶1  Broad context — ภาระโรค/ความสำคัญของปัญหาในภาพกว้าง (สั้น 2–4 ประโยค)
  ¶2–3  สิ่งที่สนามรู้แล้ว — สังเคราะห์ 2–4 ประเด็นจาก theme-map ไล่จากกว้างไปแคบ
        (ไม่ใช่ทุกประเด็นใน theme-map ต้องเข้า — เลือกเฉพาะที่ปูทางตรงไปหา gap)
  ¶4  Gap — ใช้ "ประโยค gap สุดท้าย" จาก gap-argument.md ตรง ๆ
  ¶สุดท้าย  Study objective/hypothesis — ประโยคที่ชัด ตรง วัดผลได้ ต้องสอดคล้องกับ
             study design ที่บันทึกไว้ใน config
```

**ไม่มี** conceptual framework section แบบยาวในโหมดนี้ — ถ้ามี conceptual model จริง มันอยู่ใน Methods ของ manuscript (นอกขอบเขต skill นี้) ไม่ใช่ท้าย Introduction

Word limit ของ Introduction (จาก config) คือข้อจำกัดจริง ไม่ใช่ตัวเลขอ้างอิงเฉย ๆ — ถ้าร่างเกิน ให้บีบเนื้อหาไม่ใช่ยืดขอบเขต journal

## 5.1b โครง — โหมด B: Standalone review manuscript

ใช้โครงจาก config (สกัดจาก author guidelines และผู้ใช้ยืนยันแล้ว) ถ้า config ระบุว่าใช้ default ให้ใช้โครงมาตรฐานนี้และแจ้งผู้ใช้อีกครั้ง:

```
Introduction                      ← ทำไม review เรื่องนี้จำเป็นตอนนี้ ปิดท้ายด้วยวัตถุประสงค์ของ review
Methods                           ← กลยุทธ์การค้นและเกณฑ์คัดเลือก (จาก search-log.md) — สั้นได้ถ้าไม่ใช่ systematic review
[ประเด็นที่ 1..N]                 ← เรียงตามประเด็นใน theme-map ไม่ใช่ตามปีหรือใน/ต่างประเทศ
Discussion / Research gaps        ← ต้องไหลมาจาก gap-argument.md โดยตรง
Conclusion
```

หมายเหตุ: ถ้าระหว่างทางพบว่าผู้ใช้ต้องการความเข้มระดับ systematic review (PRISMA flow, risk of bias, pooled estimate) ให้หยุดและชี้ไปที่ skill `systematic-review-meta-analysis` — โหมด B ของ skill นี้ทำได้แค่ narrative/scoping review

## 5.2 กติกาการร่าง (ทั้งสองโหมด)

- **ร่างทีละ section** เซฟลง `drafts/<หมายเลข-ชื่อ>.md` ทีละไฟล์ ให้ผู้ใช้ตรวจก่อนไป section ถัดไป
- **แหล่งอ้างอิงเดียวคือ synthesis-matrix.csv** — ก่อนเขียนแต่ละ section ให้ระบุก่อนว่าจะใช้แถวไหนบ้าง ถ้าระหว่างเขียนรู้สึกอยากอ้างงานที่ไม่อยู่ใน matrix นั่นคือสัญญาณ hallucination — หยุด กลับไปค้นจริง (PubMed/Consensus/Scholar Gateway) เพื่อยืนยันแล้วเพิ่มเข้า matrix พร้อม paper_id และ search_query ก่อนใช้อ้างอิง
- **Q1/Q2 hard gate** — ใช้ได้เฉพาะแถวที่ quartile เป็น Q1/Q2 และมี ranking database, category, year, verified_at ครบ ถ้าไม่มีให้คัดออก ไม่ใช่เดาเติม
- **บังคับใช้กฎต้าน annotated bibliography** จาก references/synthesis.md ข้อ 3.3 ทุกย่อหน้า
- โทนภาษา: วิชาการ ตามภาษาของ manuscript ใน config ไม่ใช้สำนวนแปลตรงจากอังกฤษถ้าเขียนไทย
- ส่วน "สิ่งที่สนามรู้แล้ว"/"ประเด็นที่ N" ของแต่ละประเด็น: เปิดด้วยข้อสรุปสังเคราะห์ → หลักฐานหนุน → จุดขัดแย้ง/ข้อจำกัด → ประโยคเชื่อมสู่ประเด็นถัดไป
- section สุดท้ายก่อน gap/study objective ต้องลงจอดที่ gap โดยใช้ "ประโยค gap สุดท้าย" จาก gap-argument.md
- รวมเป็น .docx เมื่อทุก section ผ่านผู้ใช้แล้ว (`introduction.docx` โหมด A, `review-manuscript.docx` โหมด B) — อ่าน docx skill ของระบบก่อนสร้างไฟล์ ใส่ paper_id (PMID/DOI) กำกับไว้ในตารางอ้างอิงท้ายไฟล์เสมอ เพื่อให้ผู้ใช้ import เข้า reference manager ของตัวเอง (Zotero, EndNote ฯลฯ) ได้ง่ายตอนเตรียม submission
- ระบบอ้างอิงตัวเลข (Vancouver/AMA) พบบ่อยใน medical journal — ถ้า config ระบุแบบนี้ ให้ใส่ใจลำดับการปรากฏของ reference ตั้งแต่ร่างแรก ไม่ใช่ไปเรียงเลขทีหลัง
- **NEJM/Lancet discipline** — ใช้ target-specific author instructions เมื่อเลือกวารสารแล้ว; มิฉะนั้นใช้ shared clinical-journal style: concise, evidence-led, concrete verbs, one main claim per sentence. ตัด redundant/repetitive claims, duplicated citations/numbers, stock transitions, vague intensifiers, generic AI-style synthesis, และ meta-commentary ห้ามลอกถ้อยคำจากบทความตีพิมพ์
- โหมด A ต้องสร้าง `references/DISCUSSION_EVIDENCE_NOTES.md` ด้วย โดย map anticipated/actual finding theme → Q1/Q2 comparator papers → direction/effect size → contextual differences; ยังห้ามเขียนผลของงานผู้ใช้ถ้ายังไม่มีผลวิเคราะห์จริง

## 5.3 Audit สามชั้น (ก่อนส่งมอบทุกครั้ง)

ผลทั้งหมดเขียนลง `audit-report.md`

**ชั้นที่ 1 — Citation integrity**
รัน `scripts/citation_audit.py`:

```bash
python scripts/citation_audit.py --draft <ไฟล์ร่าง .md หรือ .docx> --library synthesis-matrix.csv --out audit-report.md
```

- `UNMATCHED` (อ้างในร่างแต่หาในคลังไม่เจอ) ทุกตัวต้องถูกแก้ — ลบ, แก้ตัวสะกด, หรือค้นยืนยันแล้วเพิ่มเข้า synthesis-matrix.csv พร้อม paper_id จริง — ก่อนส่งมอบ **ห้ามส่งมอบทั้งที่มี UNMATCHED ค้าง**
- audit ต้อง fail หาก matrix row ที่ถูกใช้ไม่มี PMID/DOI, record URL, live connector/query provenance, หรือ verified Q1/Q2 fields ครบ
- สคริปต์เป็น heuristic: จับรูปแบบ author-year ได้ แต่อาจพลาดรูปแบบแปลก — ให้สุ่มไล่ตรวจด้วยตาเพิ่ม 10 รายการเสมอ และถ้า manuscript ใช้ระบบตัวเลข (Vancouver/AMA) สคริปต์ใช้ไม่ได้ ต้องตรวจมือทั้งหมด

**ชั้นที่ 2 — Coverage**
- ทุกแถวใน matrix ถูกใช้ในร่างหรือถูกบันทึกเหตุผลที่ไม่ใช้ (ใน audit-report)
- ทุกประเด็นใน theme-map ที่เลือกใช้ปรากฏในร่าง (โหมด A ไม่จำเป็นต้องใช้ทุกประเด็นจาก theme-map — แค่ต้องระบุเหตุผลว่าทำไมตัดประเด็นไหนออกเพราะ word limit)
- "จุดที่ขัดแย้ง" สำคัญ ๆ ไม่ถูกกลบหาย — ส่วนที่เล่าแต่ความเห็นพ้องคือส่วนที่ reviewer ไม่เชื่อ

**ชั้นที่ 3 — Coherence**
- เนื้อหาไหลจากกว้าง → แคบ → gap → (โหมด A: study objective / โหมด B: conclusion) โดยไม่มี section กำพร้า
- (โหมด A) study objective ตรงกับ study design ที่บันทึกไว้ใน config เป๊ะ ไม่มีตัวแปรที่ objective พูดถึงแต่ design ไม่ได้วัด
- (โหมด B) ทุกตัวแปรที่กล่าวถึงใน conclusion มีฐานจากวรรณกรรมที่สังเคราะห์มาก่อนหน้า
- ประโยคปิดเชื่อมไปส่วนถัดไปได้ (โหมด A: เชื่อมไป Methods, โหมด B: เชื่อมไป Conclusion)
- อยู่ใน word limit และ reference count limit ของ config

**ชั้นที่ 4 — Editorial integrity**
- sweep ทุกย่อหน้าหา redundant/repetitive ideas, duplicated evidence, canned transitions, vague intensifiers, และ AI-style prose
- ให้ independent later pass ยืนยันว่าการแก้ editorial ผ่านจริง; สถานะ `แก้แล้ว` ยังเป็น provisional จนกว่าจะ re-check

ส่งมอบ: ไฟล์ .docx + audit-report.md + synthesis-matrix.csv + journal-quartile-log.csv พร้อมกันเสมอ และอัปเดตสถานะใน project-config.md

**โหมด A เท่านั้น**: หลังส่งมอบ ให้เสนอ hand-off ไปยัง `medical-research-pipeline:manuscript-writer` ทันที (ดูรายละเอียดใน SKILL.md ส่วน "ส่งต่อให้ manuscript-writer") — ไม่ต้องรอให้ผู้ใช้ถาม
