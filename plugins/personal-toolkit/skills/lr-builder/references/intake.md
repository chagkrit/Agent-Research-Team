# เฟส 1 — Intake & Contract

เป้าหมายของเฟสนี้: รู้จักผู้ใช้และโจทย์ของเขาดีพอที่จะทำงานแทนทีม postdoc ได้ และจบด้วย `project-config.md` ที่ผู้ใช้ยืนยันแล้ว

## 0. ตรวจ live files และเลือกโหมดงาน

รัน `ls -la -t` ที่ project root และโฟลเดอร์ references/drafts/manuscript ก่อนอ่าน note หรือ config บันทึก path/timestamp ของไฟล์ปัจจุบันใน config ห้ามเชื่อ memory, note, หรือชื่อไฟล์ `final` อย่างเดียว

ถามผู้ใช้ตรง ๆ ว่างานนี้คือ:

- **โหมด A — Introduction + Discussion evidence ของ original article (IMRAD)**: ร่าง Introduction และเตรียม evidence matrix/comparator notes สำหรับ Discussion ที่จะเขียนหลังผลวิเคราะห์ เนื้อหาต้องสั้น กระชับ ตาม word limit ของ target journal
- **โหมด B — Standalone review manuscript**: manuscript ทั้งฉบับที่ตัวมันเองคือทบทวนวรรณกรรม (narrative/scoping review) มี Discussion/Conclusion ของตัวเอง

ถ้าผู้ใช้บอกว่าต้องการทำ **systematic review/meta-analysis อย่างเป็นทางการ** (มี PRISMA flow, risk of bias assessment, pooled effect size) นั่นไม่ใช่โหมด B — แจ้งว่าอยู่นอกขอบเขตของ skill นี้ และชี้ไปที่ skill `systematic-review-meta-analysis` แทน

บันทึกโหมดที่เลือกไว้ใน `project-config.md` ตั้งแต่ต้น เพราะกำหนดโครงสร้างของเฟส 5 ทั้งหมด

## 1. Contract — ข้อมูลขั้นต่ำที่ต้องมีก่อนเดินหน้า

| รายการ | ทำไมขาดไม่ได้ | ถ้าไม่มี |
|---|---|---|
| PubMed, Semantic Scholar/Scholar Gateway, และ Consensus เชื่อมต่อและเรียก live query ได้ครบทั้งสามฐาน | เป็นแหล่งค้น/ตรวจข้ามกันและเป็นหลักฐานว่ารายการมีอยู่จริง | **หยุด** ถ้าขาดฐานใดฐานหนึ่ง — ขอให้ผู้ใช้เชื่อม/เปิด connector ก่อน ห้ามลด coverage เงียบ ๆ |
| ช่องทางตรวจ quartile จากฐานจริง (JCR preferred; SCImago/SJR fallback) | cite ได้เฉพาะวารสาร Q1/Q2 และต้องบันทึก source/category/year | **หยุด** ถ้าตรวจไม่ได้ — ห้ามเดา quartile จาก impact factor หรือชื่อเสียง |
| คำถามวิจัย / study objective (จาก protocol, proposal หรือ draft ที่มีอยู่แล้ว) | ทั้งส่วนคือข้อโต้แย้งที่ต้องจบลงตรงคำถามวิจัย/objective ไม่มีเป้า = สังเคราะห์ไม่ได้ | **หยุด** — ขอเอกสารหรือให้ผู้ใช้พิมพ์คำถามวิจัย/objective มาตรง ๆ |
| กฎ format: author guidelines ของ target journal หรือตัวอย่าง manuscript ที่ตีพิมพ์แล้วในวารสารเดียวกัน | โครงส่วน, word limit, จำนวน reference สูงสุด, และรูปแบบอ้างอิง (ส่วนใหญ่ medical journal ใช้ Vancouver แบบตัวเลข) ต่างกันมากระหว่างวารสาร | **ไม่หยุด แต่เตือน** — ใช้โครง default (ดู references/drafting.md) ได้ โดยบันทึกใน config ว่าใช้ default และผู้ใช้รับความเสี่ยงเอง — แนะนำให้เลือก target journal ให้ได้ก่อนเฟส 5 เพราะ word/reference limit กระทบการร่างโดยตรง |

หลักการ: **fail loudly** — ขาดอะไรให้บอกชัด เสนอทางแก้ แล้วรอ ห้ามเดาแทน

## 2. บทสัมภาษณ์

ถามทีละข้อหรือเป็นชุดสั้น ๆ อย่าโยนทุกคำถามพร้อมกัน ปรับภาษาตามผู้ใช้:

1. สาขาวิชาและหัวข้อของ manuscript คืออะไร
2. คำถามวิจัย / study objective (ขอจาก protocol/proposal ถ้ามี — ถ้าโหมด A ให้ถามด้วยว่า study design ที่จะรายงานใน Methods คืออะไร เพราะ Introduction ต้องปูทางไปหามันโดยตรง)
3. target journal — ชื่อวารสาร, มี author guidelines/template ไหม (ขอไฟล์หรือลิงก์), word limit ของ Introduction/ทั้งฉบับ, จำนวน reference สูงสุด
4. ระบบอ้างอิงที่ target journal ใช้ (Vancouver ตัวเลข / AMA / APA / อื่น ๆ) และภาษาของ manuscript (ไทย/อังกฤษ)
5. ขอบเขตการค้น — ช่วงปีที่ต้องการ, ภาษาที่รับ, ประเภทงาน (RCT/cohort/review ฯลฯ) ที่จะให้น้ำหนัก, และมีคำค้น/MeSH term ที่อยากให้ใช้อยู่แล้วไหม (ถ้าไม่มี skill จะช่วยร่างในเฟส 2)
6. มีกรอบทฤษฎีหรือ conceptual model หลักที่กำหนดไว้แล้วหรือยังเปิดอยู่
7. timeline — deadline submission (มีผลต่อการจัดลำดับงาน)
8. (เฉพาะโหมด A) จะให้ `medical-research-pipeline:manuscript-writer` ทำ Methods/Results/Discussion ต่อไหม — ถ้าใช่ บันทึกไว้ใน config เพื่อเตรียม hand-off

## 3. สกัดกฎ format จาก author guidelines

เมื่อได้ author guidelines หรือ manuscript ตัวอย่าง:

1. อ่านแล้วสกัดเป็นรายการกฎที่ชัดเจน: โครงหัวข้อที่บังคับ (โหมด A มักบังคับแค่ "Introduction" ไม่มีหัวข้อย่อย), word limit ของแต่ละส่วน, จำนวน reference สูงสุด, รูปแบบอ้างอิงในเนื้อหาและบรรณานุกรม, รูปแบบตาราง/ภาพถ้ามี
2. author guidelines บางวารสารเขียนหลวมหรือคลุมเครือ — จุดไหนกำกวม ให้ระบุว่ากำกวมและเสนอการตีความที่เลือก
3. **แสดงรายการกฎทั้งหมดให้ผู้ใช้ยืนยันก่อนบันทึกลง config** จุดที่ผู้ใช้ไม่แน่ใจ แนะนำให้เช็คกับ corresponding author คนอื่นหรือ journal's editorial office แล้วติดป้าย `[รอยืนยัน]` ใน config

## 4. Audit ช่องทางเข้าถึงฐานข้อมูล

ตรวจและรายงานต่อผู้ใช้ก่อนเริ่มเฟส 2:

- ฐานไหนใช้ได้จริงในเซสชันนี้ (PubMed / Consensus / Scholar Gateway) — โหลด tool schema ผ่าน ToolSearch แล้วลองเรียกแบบเบา ๆ เพื่อยืนยันว่าเชื่อมต่อจริง ไม่ใช่แค่ปรากฏชื่อในรายการ
- ถ้าขาดฐานใดฐานหนึ่ง ให้หยุดและแจ้งว่าต้องเชื่อม connector ใด ห้ามเริ่มคัด citation ด้วยฐานที่เหลือ
- แจ้งข้อจำกัดเฉพาะฐานที่ต้องระวังตั้งแต่ต้น: Consensus จำกัด batch การค้นพร้อมกันไม่เกิน 3 ครั้งต่อรอบและมี rate limit, PubMed ให้ full text ได้เฉพาะบางบทความ (ต้องเช็ค copyright status ก่อนดึงเต็ม), Scholar Gateway ใช้ semantic search เป็นหลักจึงเหมาะกับคำถามเชิงแนวคิดมากกว่า exact boolean
- ถ้าผู้ใช้ระบุช่วงปีหรือภาษาที่ต้องการมาแล้ว (จากข้อ 5 ของบทสัมภาษณ์) บันทึกไว้ใน config เพื่อใช้ตั้งค่า filter ตอนค้นจริงในเฟส 2
- ทดลองตรวจ quartile ของวารสารตัวอย่างอย่างน้อยหนึ่งรายการ บันทึก ranking database, exact journal identity/ISSN, category, quartile, ranking year และ verified_at เพื่อยืนยันว่า workflow ใช้งานได้จริง

## 5. สร้าง project-config.md

ใช้โครงนี้ (คงหัวข้อให้ครบ):

```markdown
# Project config — [ชื่อหัวข้อ]
อัปเดตล่าสุด: [วันที่]

## โหมดงาน
- โหมด: [A — Introduction + Discussion evidence ของ IMRAD | B — Standalone review manuscript]
- ส่งต่อให้ manuscript-writer ทำต่อไหม (เฉพาะโหมด A): [ใช่/ไม่ใช่]

## ผู้ใช้และโจทย์
- สาขา / หัวข้อ manuscript:
- คำถามวิจัย / study objective: (ลอกมาตรงตัว)
- (โหมด A) study design ที่จะรายงานใน Methods:
- กรอบทฤษฎี/conceptual model ที่กำหนดแล้ว (ถ้ามี):

## Target journal และกฎ format (ยืนยันโดยผู้ใช้เมื่อ [วันที่])
- Target journal:
- โครงหัวข้อที่บังคับ:
- word limit (Introduction / ทั้งฉบับ): / จำนวน reference สูงสุด:
- ระบบอ้างอิง: / ภาษา manuscript:
- กฎอื่น ๆ:
- จุดที่ [รอยืนยัน]:

## แหล่งค้นวรรณกรรม
- Connector live check: PubMed [tool/time/result] / Semantic Scholar [tool/time/result] / Consensus [tool/time/result]
- Quartile source: [JCR/SCImago/SJR, access date, ranking year/category policy]
- ขอบเขตการค้น: ช่วงปี / ภาษา / ประเภทงานที่เน้น
- คำค้น/MeSH term เริ่มต้น (ถ้ามี):

## เกณฑ์คัดเลือก (จากเฟส 2)
- คัดเข้า: / คัดออก:

## สถานะล่าสุด
- เฟสปัจจุบัน:
- งานล่าสุดที่เสร็จ:
- งานถัดไป:
- เฟสที่ถูกข้าม (ถ้ามี) และเหตุผล:
```

จบเฟส 1 เมื่อผู้ใช้ยืนยัน config แล้วเท่านั้น → ไปเฟส 2 (อ่าน references/synthesis.md)
