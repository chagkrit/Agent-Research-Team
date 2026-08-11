# Provenance, numeric consistency, and independent re-check protocol

Apply this protocol to every pipeline stage. It is a hard gate, not optional guidance.

## 1. Inspect the current filesystem state first

At the start of every work session, run `ls -la -t` on the project root and on every relevant source/output directory. Record the paths, timestamps, and selected current files in `PIPELINE_STATE.md`. Do not trust memory, notes, filenames such as `final`, or a prior status entry without this live inspection.

## 2. STATA-only analytic provenance

Use STATA 18 for data cleaning and every statistical analysis. Do not use Python, R, SPSS, Excel formulas, or another statistical engine to calculate manuscript results.

Maintain this minimum artifact chain:

- `data/cleaned/analytic_cohort.dta` — the analysis-ready dataset produced by a cleaning `.do` file.
- `analysis/scripts/01_data_cleaning.do` and `analysis/logs/01_data_cleaning.log`.
- One or more numbered analysis `.do` files under `analysis/scripts/` and matching `.log` files under `analysis/logs/`.
- `analysis/results-ledger.csv` — the single source for manuscript numbers.

Each `.do` file must open its own text log, record the STATA version and input dataset, use explicit relative paths, save derived `.dta` files deliberately, and close the log. A log with an error, an unclosed run, or an unknown input dataset is not valid provenance.

## 3. Code before prose

Do not write a Methods sentence claiming an analysis was performed and do not write any Results sentence until the corresponding `.do` file exists and a successful `.log` records the actual run. Planned analyses may appear only in a clearly labeled protocol/SAP, never as completed work.

## 4. Results ledger as the only numeric source

Store every important manuscript value as one row in `analysis/results-ledger.csv`. Required fields are:

`result_id,section,analysis_label,display_value,raw_value,unit,source_dta,source_do,source_log,source_locator,generated_at,verification_status,verified_by`

Use stable `result_id` values. `source_locator` must identify the STATA command, returned result, table name, or unmistakable log location. `verification_status` may be only `generated`, `corrected_pending_independent_recheck`, or `verified`.

When drafting or revising prose, tables, figures, abstracts, or supplements, copy `display_value` from the ledger. Never retype or mentally reconstruct a number. If a needed value is absent, return to STATA, update the `.do` file, run it, save the log, and then update the ledger before writing.

## 5. Whole-project numeric sweep after every change

After changing any number, run:

```bash
python3 analysis/scripts/numeric_sweep.py \
  --root . \
  --ledger analysis/results-ledger.csv \
  --changed 'OLD_VALUE=NEW_VALUE' \
  --out analysis/outputs/NUMERIC_SWEEP_REPORT.md
```

The sweep must cover every manuscript paragraph, every Word table object, all Markdown/CSV/JSON/TXT/TEX tables, every worksheet in every supplementary `.xlsx`, and figure captions. Do not check only the paragraph where the discrepancy was found. Resolve every stale occurrence before proceeding.

## 6. Correction status is always provisional

Treat `corrected` as temporary. A correction becomes `verified` only after a separate, independent re-check on a later pass by Agent 11 or another fresh-context reviewer who compares the ledger row with the source `.do`, `.log`, and `.dta`, and reruns the whole-project sweep. The same pass that makes a correction cannot verify it.

Record the correction and the independent reviewer/date in `PIPELINE_STATE.md`. Block final integration while any ledger row is `corrected_pending_independent_recheck`.

## 7. Mandatory NEJM/Lancet clinical-journal prose discipline

Apply the target journal's current author instructions when the target is known. Otherwise use the shared NEJM/Lancet discipline: concise, evidence-led, clinically precise, and restrained.

- Prefer short declarative sentences and concrete subjects and verbs.
- Remove redundant or repetitive claims, duplicated numbers, throat-clearing, generic transitions, and restatement of table contents.
- Prohibit AI-style filler and stock phrasing, including unsupported superlatives, vague intensifiers, symmetrical boilerplate, and meta-commentary about the writing process.
- Do not imitate copyrighted wording from published articles. Follow structural and editorial conventions, not sentences.
- Preserve design-appropriate causal language and uncertainty.
- Run a dedicated redundancy/AI-style edit, then an independent editorial re-check before finalization.
