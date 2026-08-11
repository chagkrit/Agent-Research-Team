# Research Manuscript Agent System

**12-agent pipeline สำหรับเขียน manuscript วิจัยคุณภาพ publication-ready ใน Claude Code**

---

## ระบบนี้คืออะไร

Research Manuscript Agent System คือ multi-agent orchestration system ที่ทำงานใน Claude Code โดยมี Research Director Agent เป็น orchestrator ควบคุม sub-agent ทั้ง 12 ตัวตลอด pipeline การเขียนงานวิจัย ตั้งแต่ data cleaning จนถึง submission package

**รองรับ study design:**
- Retrospective / Prospective Cohort
- Case-Control
- Cross-Sectional
- Clinical Prediction Model (TRIPOD / TRIPOD-AI)
- Survival Analysis
- Systematic Review / Meta-analysis (PRISMA)
- RCT (CONSORT)

---

## Pipeline

```
User Input
    |
[GATE 1] Human approves: Study Design
    |
Data Cleaning --> Statistical Analysis --> Methods Writing
    |
[GATE 2] Human approves: Analytic Plan
    |
Literature Review --> Introduction --> Results --> Figures  (parallel)
    |
Discussion --> Journal Selection
    |
[GATE 3] Human reviews full draft
    |
Peer Review Simulation (3 reviewers)
    |
Final Integration --> Submission Package
```

**3 Human-in-the-Loop Gates** ป้องกัน pipeline วิ่งผิดทิศ

---

## 12 Sub-agents

| # | Agent | หน้าที่ | Output |
|---|---|---|---|
| 01 | Research Director | Orchestrator, routing, QC | PIPELINE_STATE.md |
| 02 | Data Cleaning | Dataset audit, cohort flow, missing data | DATA_DICTIONARY.md, clean dataset |
| 03 | Statistical Analysis | SAP, model selection, table shells | STATISTICAL_ANALYSIS_PLAN.md |
| 04 | Methodology Writing | Methods section (STROBE/TRIPOD/CONSORT) | manuscript/methods.md |
| 05 | Literature Review | Live PubMed/Semantic Scholar/Consensus search, PMID/DOI + Q1/Q2 verification, gap analysis | KEY_REFERENCES.md |
| 06 | Introduction Writing | 5-paragraph funnel intro | manuscript/introduction.md |
| 07 | Results Writing | Results section from tables | manuscript/results.md |
| 08 | Figure & Graph | STATA 18 plot plans, `.do`/`.log` provenance, captions | figures/scripts/ |
| 09 | Discussion Writing | Compare literature, implications, limits | manuscript/discussion.md |
| 10 | Journal Selection | Q1/Q2 matching, formatting, cover letter | JOURNAL_TARGET.md |
| 11 | Peer Review Simulation | 3-reviewer mock review (clinical/stats/editorial) | SIMULATED_PEER_REVIEW_REPORT.md |
| 12 | Final Integration | Consistency check, submission package | manuscript/full_draft.md |

---

## วิธีติดตั้งและใช้งาน

### วิธีที่ 1 — Claude Marketplace (แนะนำ)

ติดตั้งครั้งเดียว ใช้ได้ทุก project:

```
# เปิด Claude Code แล้วพิมพ์:
/plugin marketplace add chagkrit/Agent-Research-Team
```

```
/plugin install research-manuscript@agent-research-team
```

จากนั้นใน research project folder ใดก็ได้:

```bash
cd my-research-project
claude
```

แล้วพิมพ์:
```
I want to write a research paper about [หัวข้อ]
```

---

### วิธีที่ 2 — Git Clone (Project Template)

Clone repo นี้เป็น project folder:

```bash
git clone https://github.com/chagkrit/Agent-Research-Team.git my-research-project
cd my-research-project
claude
```

`CLAUDE.md` จะโหลดอัตโนมัติเมื่อเปิด Claude Code ใน folder นี้

---

## ขั้นตอนการใช้งาน (Step-by-Step)

### Step 1 — บอก research goal
```
ฉันต้องการเขียนงานวิจัย retrospective cohort study เกี่ยวกับผลของ metformin ต่อการเกิด MACE ในผู้ป่วย T2DM
```

### Step 2 — ยืนยัน GATE 1 (Study Design)
ระบบจะถามให้ยืนยัน:
- Research question
- Study design
- Population / Exposure / Outcome
- Target journal

### Step 3 — ระบุ data location
```
ข้อมูลอยู่ที่ data/raw/cohort_data.csv
```
Agent 02 จะ clean data, สร้าง data dictionary, และ analytic cohort flow

### Step 4 — ยืนยัน GATE 2 (Analytic Plan)
ระบบจะ present SAP ให้ยืนยันก่อนเริ่มเขียน

### Step 5 — เขียน manuscript อัตโนมัติ
ระบบจะเรียก agents 04-10 ตามลำดับและ parallel

### Step 6 — ยืนยัน GATE 3 (Full Draft Review)
อ่าน `manuscript/full_draft.md` แล้วยืนยัน

### Step 7 — Peer Review Simulation
Agent 11 จำลอง reviewer 3 คน (clinical / stats / editorial) วิจารณ์อย่างเข้มก่อน submit

### Step 8 — Final Integration
Agent 12 รวม manuscript, ตรวจ consistency ทุก N/table/figure, เตรียม submission package

---

## Requirements

### ต้องมี
- [Claude Code](https://claude.ai/code) (latest version)
- Git

### Literature connectors (บังคับสำหรับ Introduction/Discussion evidence)

ระบบต้องเรียก live PubMed, Semantic Scholar/Scholar Gateway และ Consensus ครบทั้งสามฐาน พร้อม log exact tool/query/timestamp ทุกครั้ง Cite ได้เฉพาะ record ที่ PMID/DOI resolve จริงและวารสารถูกตรวจเป็น Q1/Q2 จากฐานจัดอันดับที่ระบุ source/category/year/date ห้ามใช้ WebSearch แทนหลักฐานการมีอยู่ของบทความหรือเดา quartile

### Reproducible analysis (บังคับ)

Data cleaning และ statistical analysis ใช้ STATA 18 เท่านั้น ทุก project ต้องมี analytic `.dta`, source `.do`, successful `.log`, `analysis/results-ledger.csv`, whole-project numeric sweep และ independent re-check หลังการแก้ตัวเลข

---

## Project Structure

```
Agent-Research-Team/
├── CLAUDE.md                    # Main orchestrator (auto-loads in Claude Code)
├── PIPELINE_STATE.md            # Checkpoint tracker
├── agents/                      # 12 sub-agent instruction files
│   ├── 01_research_director.md
│   ├── 02_data_cleaning.md
│   ├── 03_statistical_analysis.md
│   ├── 04_methodology_writing.md
│   ├── 05_literature_review.md
│   ├── 06_introduction_writing.md
│   ├── 07_results_writing.md
│   ├── 08_figure_graph.md
│   ├── 09_discussion_writing.md
│   ├── 10_journal_selection.md
│   ├── 11_peer_review_simulation.md
│   └── 12_final_integration.md
├── data/                        # Put your dataset here (gitignored)
├── analysis/                    # Statistical scripts and outputs
├── manuscript/                  # All manuscript sections
├── figures/                     # Figure scripts and outputs
├── references/                  # Literature review outputs
├── journal/                     # Journal selection and cover letter
├── peer_review/                 # Simulated peer review reports
└── submission/                  # Final submission package
```

---

## License

MIT

---

## Author

[@chagkrit](https://github.com/chagkrit)
