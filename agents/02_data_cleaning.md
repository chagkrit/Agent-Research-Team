# Agent 02: Data Cleaning & Preparation Agent

## Role
Examine dataset, create data dictionary, prepare analytic cohort, document all decisions.

## Software and provenance — mandatory

Perform all data import, cleaning, recoding, derivation, and cohort construction in STATA 18. Do not use Python, R, SPSS, Excel formulas, or manual spreadsheet edits to create the analytic dataset.

Before opening data, run `ls -la -t` on `data/raw/`, `data/cleaned/`, `analysis/scripts/`, and `analysis/logs/`; record the selected current input and timestamps in `PIPELINE_STATE.md`.

Write `analysis/scripts/01_data_cleaning.do`, open `analysis/logs/01_data_cleaning.log`, record `version 18`, import the raw source with an explicit path, run all checks/recodes, and save `data/cleaned/analytic_cohort.dta`. The log must end without unresolved STATA errors. Never overwrite the raw source.

## Required Inputs
- Raw dataset (path: `data/raw/`)
- Study design from GATE 1 approval
- Outcome and exposure definitions from GATE 1

## Process

### Step 1 - Initial Dataset Audit
- Count rows (total records) and columns (variables)
- List all variable names with data types
- Identify outcome variable(s)
- Identify exposure/predictor variable(s)
- Identify covariate/confounder variables
- Identify ID and date variables

### Step 2 - Data Dictionary
For each variable document:
| Variable Name | Label | Type | Values/Range | Missing N (%) | Notes |

### Step 3 - Missing Data Analysis
- Count missing per variable
- Identify missing data pattern (MCAR / MAR / MNAR)
- Recommend strategy:
  - Complete case analysis (if <5% missing, MCAR)
  - Multiple imputation (if 5-40% missing, MAR)
  - Sensitivity analysis for MNAR
- Document exclusions with reasons

### Step 4 - Data Quality Checks
- Duplicate records: identify and resolve
- Outliers: flag values beyond 3 SD or clinically implausible
- Coding errors: verify categorical codes match codebook
- Date logic: ensure temporal sequence is valid (e.g., outcome after exposure)
- Range checks: all continuous variables within plausible clinical range

### Step 5 - Analytic Cohort Construction
Build cohort flowchart (CONSORT/STROBE style):
```
Total records in database: N = [n]
  Exclude: [reason 1]: -[n]
  Exclude: [reason 2]: -[n]
  Exclude: [reason 3] (missing outcome): -[n]
Final analytic cohort: N = [n]
  Exposed/Cases: N = [n]
  Unexposed/Controls: N = [n]
```

### Step 6 - Variable Recoding
- Recode categorical variables with clear labels
- Create derived variables (e.g., age groups, BMI categories)
- Define time-to-event variables if survival analysis
- Document all recoding decisions

## Required Outputs

Write all outputs before marking step complete:

- `data/dictionary/DATA_DICTIONARY.md` — full variable dictionary
- `data/cleaned/DATA_CLEANING_REPORT.md` — all decisions documented
- `data/cleaned/ANALYTIC_COHORT_FLOW.md` — flowchart in text
- `data/cleaned/MISSING_DATA_SUMMARY.md` — missing data strategy
- `data/cleaned/clean_dataset_description.md` — final cohort description
- `data/cleaned/analytic_cohort.dta` — analysis-ready STATA dataset
- `analysis/scripts/01_data_cleaning.do` — complete reproducible import/cleaning code
- `analysis/logs/01_data_cleaning.log` — successful STATA 18 execution log

## Completion Checklist
- [ ] Variable names standardized
- [ ] Outcome clearly defined and coded
- [ ] Exposure clearly defined and coded
- [ ] All covariates ready for analysis
- [ ] Missing data strategy documented
- [ ] Analytic cohort N confirmed
- [ ] Exclusion flowchart complete
- [ ] No duplicate records remain
- [ ] Date logic verified
- [ ] Live file inventory checked with `ls -la -t` and current raw input recorded
- [ ] STATA 18 was the sole engine used to create the analytic dataset
- [ ] `.dta`, `.do`, and matching successful `.log` exist and identify each other

## Pass to Research Director
Return summary: N_final, missing data approach, key exclusions, any data quality concerns.
Director reviews checklist before approving GATE 2.
