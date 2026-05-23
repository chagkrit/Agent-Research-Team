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

---

## Methods Section Structure

### 2.1 Study Design and Setting
- State design clearly: "This was a [single/multi]-centre retrospective cohort study conducted at [institution], [city], [country]."
- State study period (calendar years of diagnosis/enrolment)
- Describe institution type (tertiary academic, community, regional referral)
- State population catchment area if relevant

### 2.2 Participants
- Inclusion criteria (numbered list, clear and measurable)
- Exclusion criteria (numbered list)
- Index date definition (e.g., operation date, with fallback to diagnosis date)
- Refer to cohort flow diagram: "Full exclusion counts are shown in Figure [X]."
- Do NOT report final N here — that belongs in Results

### 2.3 Outcome Definitions
- Primary outcome: exact event definition, timing from index date, censoring rules
- Secondary outcomes: each defined separately with event + censoring rules
- State competing events if applicable (e.g., "Death without local recurrence was treated as a competing event for LRFS.")
- Source of outcome ascertainment (registry, medical record audit, linkage)

### 2.4 Predictor Variables and Missing Data
- List candidate predictors selected a priori; state selection rationale (clinical relevance, prior literature, prior model structure)
- For each predictor: measurement source, unit/categorization, reference category
- Quantify missingness: "Missing data were present for [variable] ([n] missing, [%]%)."
- State missing data strategy:
  - Complete-case analysis (CCA) as primary: state assumption (MAR)
  - Multiple imputation (MICE) as pre-specified sensitivity: state number of imputations, imputed variables, algorithm (e.g., IterativeImputer / mice package), pooling method (Rubin's rules)
  - Do NOT use Ki-67 or high-missingness variables in the primary model without justification

### 2.5 Statistical Analysis

#### Descriptive Statistics
- Continuous: median (IQR); categorical: frequency (%)
- Kaplan–Meier survival curves with number-at-risk tables below each panel

#### Survival Models
- State model family: Cox proportional hazards (or Fine–Gray for competing risks)
- State penalization: "A ridge penalty (λ=0.1) was applied to stabilise estimates for small predictor subgroups; a sensitivity analysis with λ=0 (unpenalised) was performed."
- State EPV: "Events per variable (EPV) were [x] for OS, [x] for DFS, and [x] for LR. Models with EPV <10 should be interpreted cautiously."
- For competing risks (e.g., local recurrence with death as competing event): report Aalen–Johansen cumulative incidence function (CIF) separately from Kaplan–Meier

#### Discrimination and Internal Validation
- "Discrimination was quantified using Harrell's concordance statistic (C-statistic)."
- Bootstrap optimism correction: "Internal validation used bootstrap optimism correction with [n] resamples. In each resample, a new model was fitted and C-statistics computed in-sample (apparent) and out-of-sample (test); the mean optimism was subtracted from the apparent C-statistic to obtain the optimism-corrected estimate."
- Report: apparent C, optimism, optimism-corrected C, 95% bootstrap CI

#### Calibration
- "Calibration was assessed using expected:observed (E:O) ratio at 5 and 10 years, computed using the Breslow baseline hazard estimator."
- "E:O = 1.00 indicates perfect calibration. Values within ±5% indicate excellent agreement."
- Calibration plot: mean predicted survival vs Kaplan–Meier observed survival within risk quintiles (diagonal = perfect)

#### Proportional Hazards Assessment
- "Scaled Schoenfeld residual tests were used to assess the proportional hazards (PH) assumption for each predictor."
- For predictors with significant violations: report stratified Cox sensitivity analysis
- Report in supplementary (Schoenfeld residual plots as Figure S1)

#### Clinical Score Chart (if prediction model)
- "An integer clinical risk score was derived from OS Cox coefficients using: score points = round(coefficient × unit × 10)."
- This facilitates bedside application without software.

#### Sensitivity Analyses
List all pre-specified sensitivity analyses:
1. MICE multiple imputation (pooled C-statistics vs CCA)
2. Unpenalised Cox (λ=0) vs ridge Cox
3. Stage-stratified Cox (for PH violations)
4. Fine–Gray / Aalen–Johansen CIF for competing risks

#### Software
- State: "All analyses were performed using Python [version] with the lifelines [version] and scikit-learn [version] packages." or R equivalent.
- State significance level: two-tailed α = 0.05

### 2.6 Ethical Approval
- IRB/ethics committee name and approval number (replace [XXX/XXXX] placeholder before submission)
- State whether informed consent required or waived (retrospective registry study)
- State data anonymisation approach

---

## Writing Style Rules (R4 Standard)

- Past tense throughout ("were included", "was defined")
- Passive voice preferred for methods; active acceptable for rationale sentences
- No results in Methods section
- Numbers in Arabic numerals (e.g., "3 patients", not "three patients")
- Format: N=2,757 (comma separator); HR 1.75 (95% CI 1.53–2.01); p<0.001
- Abbreviations: define at first use; maintain throughout
- Subsections use Heading 2 style
- No bullet lists inside the Methods prose — convert to flowing sentences

---

## Required Outputs
- `manuscript/methods.md` — complete Methods section
- `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md` — item-by-item TRIPOD/STROBE compliance

## Completion Checklist
- [ ] All 6 subsections present (Study Design / Participants / Outcomes / Predictors+Missing / Statistical Analysis / Ethics)
- [ ] Ridge penalization and λ value stated
- [ ] EPV reported for each outcome
- [ ] Bootstrap optimism correction protocol described (n resamples)
- [ ] MICE specification complete (n imputations, variables imputed, pooling method)
- [ ] Competing risk / CIF analysis described if LR or cause-specific outcome included
- [ ] Calibration method (E:O + Breslow) described
- [ ] PH assumption testing described (Schoenfeld) with sensitivity plan
- [ ] Integer score derivation formula stated
- [ ] Reporting guideline checklist complete
- [ ] No results mentioned in Methods
- [ ] Outcome definitions match GATE 1
- [ ] Statistical plan matches Agent 03 SAP
- [ ] Ethics statement included
- [ ] Word count within journal limit (check `journal/JOURNAL_TARGET.md`)
