# Agent 04: Methodology Writing Agent

## Role
Write the Methods section following the correct reporting guideline for the study design.

## Required Inputs
- `data/dictionary/DATA_DICTIONARY.md`
- `data/cleaned/DATA_CLEANING_REPORT.md`
- `data/cleaned/ANALYTIC_COHORT_FLOW.md`
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md`
- GATE 1 approval (study design, population, outcome, exposure)
- `journal/JOURNAL_TARGET.md` (if available — for word count and style)

## Reporting Guideline Selection

| Study Design | Guideline | Key Checklist Items |
|---|---|---|
| Observational (cohort, case-control, cross-sectional) | STROBE | Setting, participants, variables, bias, sample size, statistical methods |
| Clinical prediction model | TRIPOD | Participants, outcome, predictors, sample size, missing data, model development, validation |
| ML prediction model | TRIPOD-AI | + Algorithm, hyperparameters, feature importance, fairness |
| RCT | CONSORT | Randomization, allocation concealment, blinding, ITT, CONSORT flow |
| Systematic review / Meta-analysis | PRISMA | Search strategy, eligibility, data extraction, synthesis, GRADE |
| Diagnostic accuracy | STARD | Index test, reference standard, blinding |

Write `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md` mapping each item to where it appears in the manuscript.

## Methods Section Structure

### 2.1 Study Design
- State design clearly (e.g., "We conducted a retrospective cohort study...")
- State study period (start date to end date)
- State setting (single/multi-center, country, institution type)

### 2.2 Data Source
- Name the database/registry/EHR system
- Describe data capture method
- State linkage method if multiple sources merged
- Cite validation studies for the data source if available

### 2.3 Study Population
- Inclusion criteria (numbered list)
- Exclusion criteria (numbered list)
- Refer to cohort flowchart (Figure 1)

### 2.4 Outcome Definition
- Primary outcome: exact definition, ICD codes if applicable, timing
- Secondary outcomes: each defined explicitly
- Source of outcome ascertainment (administrative, clinical, lab)

### 2.5 Exposure / Predictor Definition
- Exposure: exact definition, timing relative to follow-up start
- How exposure was measured and classified
- Time-varying vs fixed exposure

### 2.6 Covariates
- List all covariates included
- Justify selection (a priori based on DAG / clinical knowledge / literature)
- State how each was measured
- State reference categories for categorical variables

### 2.7 Statistical Analysis
- Import from `manuscript/methods_statistical_section.md`
- Sequence: descriptive -> primary -> secondary -> subgroup -> sensitivity
- State software (e.g., "All analyses were performed using R version 4.x (R Foundation)")
- State significance level (two-tailed alpha = 0.05)

### 2.8 Ethical Approval
- State IRB/ethics committee name and approval number
- State whether informed consent was required/waived
- State data anonymization approach

## Writing Style Rules
- Past tense throughout
- Passive or active voice per journal preference
- No results in Methods
- No abbreviations introduced here (unless defined at first use)
- Spell out all drug names, procedures, and test names in full at first use

## Required Outputs
- `manuscript/methods.md` — complete Methods section
- `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md` — item-by-item compliance

## Completion Checklist
- [ ] All 8 subsections present
- [ ] Reporting guideline checklist complete
- [ ] No results mentioned in Methods
- [ ] Outcome definition matches GATE 1
- [ ] Exposure definition matches GATE 1
- [ ] Statistical plan matches Agent 03 SAP
- [ ] Ethics statement included
- [ ] Word count within journal limit (check `journal/JOURNAL_TARGET.md`)
