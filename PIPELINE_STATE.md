# Pipeline State Tracker

Update this file after completing each step.
Format: `[DONE]` / `[IN PROGRESS]` / `[PENDING]` / `[SKIPPED]`

---

## Project Info

- **Project Title**: [fill in]
- **Study Design**: [fill in]
- **Target Journal**: [fill in]
- **Target Prose Standard**: [NEJM / Lancet / shared concise clinical-journal default]
- **Last Updated**: [fill in]
- **Live File Inventory (`ls -la -t`) Checked**: [date/time, directories, selected current paths]

---

## Gates

| Gate | Status | Date | Notes |
|---|---|---|---|
| GATE 1 - Study Design Approval | PENDING | | |
| GATE 2 - Analytic Plan Approval | PENDING | | |
| GATE 3 - Full Draft Review | PENDING | | |

---

## Agent Steps

| Step | Agent | Status | Output Files | Notes |
|---|---|---|---|---|
| 1 | Research Director - Initial Assessment | PENDING | | |
| 2 | Data Cleaning & Preparation | PENDING | analytic_cohort.dta, 01_data_cleaning.do/.log, DATA_DICTIONARY.md, DATA_CLEANING_REPORT.md, ANALYTIC_COHORT_FLOW.md | |
| 3 | Statistical Analysis Planning & Execution | PENDING | numbered .do/.log files, results-ledger.csv, STATISTICAL_ANALYSIS_PLAN.md, TABLE_SHELLS.md | |
| 4 | Methodology Writing | PENDING | manuscript/methods.md, REPORTING_GUIDELINE_CHECKLIST.md | |
| 5 | Literature Review | PENDING | KEY_REFERENCES.md, KNOWLEDGE_GAP.md | |
| 6 | Introduction Writing | PENDING | manuscript/introduction.md | |
| 7 | Results Writing | PENDING | manuscript/results.md | |
| 8 | Figure & Graph Planning | PENDING | FIGURE_PLAN.md, FIGURE_CAPTIONS.md, figure scripts | |
| 9 | Discussion Writing | PENDING | manuscript/discussion.md | |
| 10 | Journal Selection | PENDING | JOURNAL_TARGET.md, COVER_LETTER_DRAFT.md | |
| 11 | Peer Review Simulation | PENDING | SIMULATED_PEER_REVIEW_REPORT.md, REVISION_ACTION_PLAN.md | |
| 12 | Final Integration | PENDING | manuscript/full_draft.md, FINAL_SUBMISSION_CHECKLIST.md | |

---

## QC Log

Use only `generated`, `corrected_pending_independent_recheck`, or `verified` for numeric/statistical corrections. The same pass that edits an item cannot verify it.

| Date | Step | Issue Found | Resolution | Source do/log/ledger ID | Independent Reviewer/Date | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## Final hard gates

- [ ] Current paths and timestamps were checked with `ls -la -t` this session.
- [ ] STATA 18 was the sole data-cleaning/statistical engine.
- [ ] Current analytic `.dta`, executable `.do`, and successful `.log` files exist.
- [ ] Every important manuscript number is mapped in `analysis/results-ledger.csv`.
- [ ] Whole-project sweep passed after the latest numeric change, including Word tables and every supplementary Excel worksheet.
- [ ] No item remains `corrected_pending_independent_recheck`.
- [ ] Introduction/Discussion citations have live connector retrieval evidence, PMID/DOI, and verified Q1/Q2 status.
- [ ] NEJM/Lancet editorial pass removed redundant, repetitive, and AI-style prose.
