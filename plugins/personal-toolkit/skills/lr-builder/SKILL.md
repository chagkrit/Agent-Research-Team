---
name: lr-builder
description: Build verified literature evidence and prose for manuscript Introductions, Discussions, and narrative/scoping reviews. Use for literature review, LR, ทบทวนวรรณกรรม, synthesis matrix, research gap, Introduction/Background, Discussion comparisons, review manuscripts, paper discovery, PubMed searches, or evidence synthesis. Requires live PubMed, Semantic Scholar/Scholar Gateway, and Consensus retrieval; real PMID/DOI records; verified Q1/Q2 journal status; reproducible search logs; thematic synthesis; gap testing; concise NEJM/Lancet-style drafting; and citation audit. Never cite from model memory.
---

# LR Builder — สร้างส่วนทบทวนวรรณกรรมของ manuscript

Skill นี้พาผู้ใช้สร้างส่วนทบทวนวรรณกรรมของ manuscript ตั้งแต่ศูนย์จนถึงร่างที่ตรวจสอบแล้ว โดยค้นวรรณกรรมสดผ่านสามฐาน — **PubMed**, **Consensus**, และ **Scholar Gateway (Semantic Scholar)** — เป็นแหล่งอ้างอิงเดียวของทั้งระบบ ไม่มีคลังส่วนตัวที่ต้องเตรียมมาก่อน รองรับสองโหมด (เลือกในเฟส 1):

- **โหมด A — Introduction section ของ original article (IMRAD)**: ส่วน Introduction/Background ของ manuscript ที่จะมี Methods/Results/Discussion ตามมา เนื้อหาสั้น กระชับ ปิดท้ายด้วย study objective/hypothesis ที่ชัดเจน ไม่ใช่ conceptual framework แบบยาว
- **โหมด B — Standalone review manuscript**: manuscript ทั้งฉบับที่ตัวมันเองคือทบทวนวรรณกรรม (narrative/scoping review) มีโครงยาวกว่า มี Discussion/Conclusion ของตัวเอง — ถ้าผู้ใช้ต้องการทำ **systematic review/meta-analysis อย่างเป็นทางการ** (PRISMA, risk of bias, pooled effect) ให้แจ้งว่านั่นอยู่นอกขอบเขตของ skill นี้ และชี้ไปที่ skill `systematic-review-meta-analysis` แทน

## กฎเหล็ก (บังคับทุกเฟส ไม่มีข้อยกเว้น)

1. **Citation integrity = ต้องมาจากการค้นจริง ไม่ใช่ความจำ** — ห้ามเขียนอ้างอิงที่ยังไม่ได้ถูกดึงจาก PubMed, Semantic Scholar/Scholar Gateway, หรือ Consensus จริงและบันทึกไว้ใน `synthesis-matrix.csv` ทุกแถวต้องมี `paper_id` (PMID หรือ DOI), exact connector/tool, และ `search_query` ถ้านึกถึงงานใดจากความจำ ให้ค้นยืนยันก่อนเสมอ ห้ามใส่ลง matrix จากความจำ
2. **Fail loudly** — ถ้าข้อมูลขั้นต่ำไม่ครบ (ดู contract ใน references/intake.md) ให้หยุดและบอกว่าขาดอะไร ห้ามเดาเงียบ ๆ แล้วเดินหน้าต่อ
3. **Synthesis, not summary** — หน่วยของการเขียนคือ "ประเด็น" ไม่ใช่ "เปเปอร์" ห้ามเขียนแบบไล่เล่างานทีละชิ้น (annotated bibliography) กฎเชิงปฏิบัติอยู่ใน references/synthesis.md
4. **ทำงานทีละธีม** — ห้ามพยายามร่างทั้งส่วนในรอบเดียว ทำทีละ section/ธีม แล้วเซฟลงไฟล์ทุกครั้ง
5. **ยืนยันก่อนใช้** — กฎ format ที่สกัดจาก author guidelines ของ target journal ต้องให้ผู้ใช้ยืนยันก่อนนำไปใช้เสมอ
6. **Reproducibility ของการค้น** — ทุก query ที่ยิงไปยัง PubMed/Consensus/Scholar Gateway ต้อง log ลง search-log.md ทันที (ฐานข้อมูล, query ตรงตัว, วันที่, จำนวนผลลัพธ์, จำนวนที่คัดเข้า) เพราะผลค้นสดเปลี่ยนได้ตามเวลา — ถ้าไม่ log ไว้ session ถัดไปจะ reproduce ไม่ได้
7. **Q1/Q2 only** — cite เฉพาะบทความในวารสารที่ตรวจ quartile เป็น Q1 หรือ Q2 จากฐานจัดอันดับที่ระบุชื่อ, category, ranking year, และวันที่ตรวจได้จริง ห้ามอนุมาน quartile จาก impact factor/ชื่อเสียง/ความจำ งานที่ตรวจไม่ได้หรือเป็น Q3/Q4/unranked ต้องคัดออก
8. **Real database record only** — PMID/DOI ต้อง resolve และ metadata (title, journal, year) ต้องตรงกับฐานจริง ถ้าขัดแย้งแก้ไม่ได้ ให้คัดออก ห้ามแต่งหรือเติม metadata
9. **NEJM/Lancet prose discipline** — สำหรับ Introduction/Discussion ให้เขียนกระชับ evidence-led, ตัด redundant/repetitive/AI-style filler และไม่ลอกถ้อยคำจากบทความตีพิมพ์

## เริ่มทุกเซสชันแบบนี้

1. รัน `ls -la -t` ที่ project root และโฟลเดอร์ references/drafts/manuscript แล้วบันทึก path + timestamp ของไฟล์ปัจจุบันใน `project-config.md` ห้ามเชื่อ memory/note หรือชื่อไฟล์ `final` อย่างเดียว
2. มองหาไฟล์ `project-config.md` ใน working directory ของโปรเจกต์
   - **มี** → อ่านก่อนทำอะไรทั้งสิ้น แล้วถามผู้ใช้ว่าจะทำต่อจากเฟสไหน (config บันทึกโหมดงานและสถานะล่าสุดไว้)
   - **ไม่มี** → นี่คือผู้ใช้ใหม่ เริ่มเฟส 1 ทันที (อ่าน references/intake.md) — เฟส 1 จะถามก่อนว่าเป็นโหมด A หรือ B
3. Discover tools by capability and run a minimal live query against all three required connectors: PubMed, Semantic Scholar/Scholar Gateway, and Consensus. Tool names vary by host; record the exact callable names.
   - ถ้าฐานใดฐานหนึ่งไม่พร้อมใช้ → **หยุด** และขอให้ผู้ใช้เชื่อม/เปิด connector นั้น ห้ามลด coverage เงียบ ๆ
4. ตรวจว่ามีช่องทางยืนยัน Q1/Q2 จริง (JCR preferred; SCImago/SJR เป็น fallback) ถ้าไม่มี → **หยุด** ก่อนคัด citation

## Pipeline ห้าเฟส

ทุกเฟสมีไฟล์อ้างอิงของตัวเอง — **อ่านไฟล์ของเฟสนั้นก่อนเริ่มเฟสเสมอ**

| เฟส | งาน | อ่านไฟล์ | ผลลัพธ์ (เซฟเป็นไฟล์) |
|---|---|---|---|
| 1. Intake & contract | เลือกโหมด สัมภาษณ์ผู้ใช้ ตรวจ contract สกัดกฎ format จาก author guidelines | `references/intake.md` | `project-config.md` |
| 2. Search & Extraction | ออกแบบ query ต่อฐานข้อมูล ค้นจริง คัดกรอง สกัดที่เข้าเกณฑ์ลงตารางสังเคราะห์ | `references/synthesis.md` | `synthesis-matrix.csv` + `search-log.md` |
| 3. Thematic synthesis | จัดกลุ่มเป็นประเด็น ชี้จุดพ้อง/ขัดแย้ง/เงียบ | `references/synthesis.md` | `theme-map.md` |
| 4. Gap argumentation | ทดสอบ gap ด้วยวิธีสองสาย | `references/gap.md` | `gap-argument.md` |
| 5. Drafting + audit | ร่างทีละ section ตาม format แล้วตรวจสามชั้น | `references/drafting.md` | `drafts/` + `.docx` + `audit-report.md` |

ห้ามข้ามเฟส ห้ามเริ่มเฟส 5 ถ้า `gap-argument.md` ยังไม่ผ่านการยืนยันจากผู้ใช้ ถ้าผู้ใช้ขอข้ามเฟสโดยตรง ให้อธิบายความเสี่ยงหนึ่งครั้ง — ถ้ายืนยัน ให้ทำตามแต่บันทึกไว้ใน config ว่าเฟสใดถูกข้าม

## โครงไฟล์ของโปรเจกต์ (สร้างและดูแลตลอดอายุงาน)

```
<โฟลเดอร์โปรเจกต์ของผู้ใช้>/
├── project-config.md      ← โปรไฟล์ผู้ใช้ + โหมดงาน + กฎ format + สถานะล่าสุด
├── search-log.md          ← query ทุกตัวที่ยิงไปแต่ละฐาน + เกณฑ์คัดเข้า/ออก + บันทึกการคัดเลือก
├── synthesis-matrix.csv   ← construct × study + connector/query + PMID/DOI + Q1/Q2 provenance
├── journal-quartile-log.csv ← journal/category/quartile/source/year/verified_at
├── theme-map.md           ← ประเด็น + จุดพ้อง/ขัดแย้ง/เงียบ
├── gap-argument.md        ← gap ที่ผ่านการทดสอบสองสาย
├── drafts/                ← ร่างทีละ section
├── introduction.docx      ← โหมด A: ร่าง Introduction section (ใช้ docx skill ของระบบในการสร้าง)
│   หรือ review-manuscript.docx ← โหมด B: ร่าง manuscript ทบทวนวรรณกรรมฉบับเต็ม
└── audit-report.md        ← ผลตรวจ citation/coverage/coherence
```

อัปเดต `project-config.md` ส่วน "สถานะล่าสุด" ทุกครั้งที่จบงานหนึ่งชิ้น เพื่อให้เซสชันถัดไปทำต่อได้โดยไม่ต้องถามซ้ำ

## เครื่องมือ

- `scripts/citation_audit.py` — ตรวจ citation ในร่างเทียบกับ `synthesis-matrix.csv` (แหล่งอ้างอิงที่สร้างเองจากการค้น ไม่ใช่ไฟล์ export ภายนอกแล้ว) รันในเฟส 5 (ดูวิธีใช้ใน references/drafting.md) สคริปต์นี้เป็น heuristic ชั้นแรก — ผลตรวจต้องให้คนยืนยันซ้ำเสมอ ไม่ใช่คำตัดสินสุดท้าย
- การสร้างไฟล์ .docx ให้ใช้ docx skill ของระบบ (ถ้ามี) — อ่าน SKILL.md ของมันก่อนสร้างไฟล์
- Connectors สำหรับค้นวรรณกรรม: PubMed, Consensus, และ Semantic Scholar/Scholar Gateway ต้องพร้อมใช้ทั้งสามฐาน Tool names แตกต่างตาม host ให้ discover by capability และ log ชื่อจริงทุกครั้ง รายละเอียดอยู่ใน `references/synthesis.md`

## ส่งต่อให้ manuscript-writer (โหมด A)

เมื่อ audit สามชั้นในเฟส 5 ผ่านแล้ว งานของ skill นี้จบแค่ส่วน Introduction — งานที่เหลือของ manuscript (Methods/Results/Discussion, deep-review เชิงลึก, consistency check, submission package) อยู่นอกขอบเขต ให้บอกผู้ใช้ชัดเจนว่าพร้อมส่งต่อ และแนะนำให้เรียก skill `medical-research-pipeline:manuscript-writer` (และ `medical-research-pipeline:peer-review` สำหรับ deep-review ก่อนส่ง) โดยส่งมอบไฟล์เหล่านี้ไปด้วย:

- `introduction.docx` (หรือ draft ล่าสุดใน `drafts/`)
- `synthesis-matrix.csv` — เพื่อให้ manuscript-writer อ้างอิงงานเดียวกันตอนเขียน Discussion โดยไม่ต้องค้นวรรณกรรมซ้ำ (ทุกแถวมี paper_id จริงพร้อมใช้)
- `gap-argument.md` — ประโยค gap สุดท้ายมักถูกนำไปย้อนพูดซ้ำใน Discussion ตอนเทียบกับ literature

ไม่ต้องรอให้ผู้ใช้ถาม — เสนอ hand-off นี้ทันทีที่ audit ผ่าน

## ขอบเขตที่ skill นี้ไม่ทำ

- ไม่คิด contribution หรือคำถามวิจัยแทนผู้ใช้ — ช่วยวิพากษ์ได้ แต่การตัดสินใจเป็นของผู้ใช้
- ไม่อ้างอิงงานจากความจำของโมเดลโดยไม่ยืนยันด้วยการค้นจริง — งานทุกชิ้นในบทต้องผ่านการค้นที่ log ไว้ใน search-log.md เท่านั้น (ดูกฎเหล็กข้อ 1)
- ไม่เขียน Methods/Results/Discussion ของ original article (โหมด A) — จบงานที่ Introduction แล้ว hand off ให้ `medical-research-pipeline:manuscript-writer`
- ไม่ทำ systematic review/meta-analysis อย่างเป็นทางการ (PRISMA, risk of bias, pooled effect) — ถ้าผู้ใช้ต้องการแบบนั้น ชี้ไปที่ skill `systematic-review-meta-analysis`
