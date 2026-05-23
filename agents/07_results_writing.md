# Agent 07: Results Writing Agent

## Role
Write the Results section from analysis outputs. Report findings accurately. No interpretation beyond data.

## Required Inputs
- `data/cleaned/ANALYTIC_COHORT_FLOW.md` — for cohort description
- `analysis/outputs/TABLE_SHELLS.md` — table structure reference
- Actual analysis results provided by user (tables, model outputs, JSON summary)
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` — to follow pre-specified order
- `manuscript/methods.md` — to ensure consistency

---

## Results Section Structure (R4 Standard)

### 3.1 Cohort Characteristics
- Report N at each exclusion step (reference Figure [flowchart])
- State final analytic cohort N with surgery subgroups: "The analytic cohort comprised [N] patients: [n] ([%]%) treated with BCT and [n] ([%]%) with mastectomy (Figure [X])."
- State diagnosis year range
- Report median age with IQR
- Report key baseline variables with n and % (referencing Table 1)
- State complete-case N: "The complete-case dataset for multivariable analysis contained [n] patients ([n] OS events, [n] DFS events, [n] LRFS events)."
- State EPV for each outcome: "EPV were [x] for OS, [x] for DFS, and [x] for LRFS; the low LRFS EPV of [x] indicates that LRFS estimates should be interpreted cautiously."

### 3.2 Survival Estimates
- State median follow-up (years) with IQR
- State event counts: "[n] deaths, [n] DFS events, and [n] local recurrence events were recorded."
- Report KM estimates in table format:
  - "Five-year OS was [x]% (95% CI [x]–[x]%); 10-year OS was [x]% (95% CI [x]–[x]%)"
  - Same for DFS and LRFS
- Reference Figure 1 (overall KM curves with number-at-risk tables)
- Reference Figure 2 (KM by stage, if applicable — note omitted groups)
- Reference Table 2 for full KM summary

### 3.3 Univariable Cox Regression
- Reference Table 3
- Highlight 2–3 strongest univariable associations with HR (95% CI, p-value)
- Format: "Each additional TNM stage unit was associated with a [x]-fold increase in the OS hazard (HR [x.xx], 95% CI [x.xx]–[x.xx]; p[value])."
- Note any variables not reaching significance

### 3.4 Multivariable Cox Regression and Model Performance
- State model: "Multivariable Cox proportional hazards regression with ridge penalization (λ=0.1) was applied."
- Report primary outcome (OS) results first, then DFS, then LRFS
- Format for each predictor: "HR [x.xx], 95% CI [x.xx]–[x.xx]; p[value]"
- Reference Table 4
- Flag any small subgroups with wide CIs: "The Luminal B HER2− subgroup (n=[x]) generated an OS HR of [x.xx] (95% CI [x.xx]–[x.xx]); the wide CI reflects the small subgroup size and this estimate should be considered exploratory."
- **Discrimination**: "Apparent Harrell C-statistics were [x.xxx] for OS, [x.xxx] for DFS, and [x.xxx] for LRFS."
- **Internal validation (bootstrap optimism correction)**: "Bootstrap optimism-corrected C-statistics ([n] resamples) were [x.xxx] (OS; 95% CI [x.xxx]–[x.xxx]), [x.xxx] (DFS; 95% CI [x.xxx]–[x.xxx]), and [x.xxx] (LRFS; 95% CI [x.xxx]–[x.xxx])."

### 3.5 Missing Data Sensitivity Analysis (MICE)
- "MICE with [n] imputations was performed as a pre-specified sensitivity analysis."
- Report pooled C-statistics: "Pooled C-statistics across [n] imputed datasets were [x.xxx] (SD [x.xxx]) for OS, [x.xxx] (SD [x.xxx]) for DFS, and [x.xxx] (SD [x.xxx]) for LRFS, consistent with the CCA estimates."
- Reference supplementary MICE table

### 3.6 Proportional Hazards Diagnostics
- "Schoenfeld residual tests indicated statistically significant deviations from proportional hazards for [list variables] in OS (p=[values]) and DFS (p=[values])."
- "These violations indicate that hazard ratios for these predictors change over follow-up time."
- "Supplementary Figure S1 shows the Schoenfeld residual plots."
- Report stratified Cox sensitivity: "A stage-stratified Cox model yielded a C-statistic of [x.xxx], confirming that stage is a primary driver of discrimination."
- Report λ=0 sensitivity: "An unpenalised (λ=0) OS model yielded C=[x.xxx], confirming that ridge penalization had minimal effect on discrimination."

### 3.7 Risk Stratification and Calibration
- "Risk groups defined by tertiles of the OS model linear predictor are presented in Table 5 and Figure 4."
- Report 5-year and 10-year OS for each tertile with 95% CI
- Reference Figure 4 (with number-at-risk tables)
- **Clinical Score Chart**: "An integer clinical score chart was derived from OS Cox coefficients (score points = round(coefficient × unit × 10)) (Figure 5). Approximate weights: [list key weights from analysis]."
- **Calibration E:O**: "E:O ratios for OS were [x.xxx] at 5 years and [x.xxx] at 10 years; for DFS, [x.xxx] at 5 years and [x.xxx] at 10 years. Values within 1% of unity indicate excellent calibration." Reference Figure 6.

### 3.8 Local Recurrence and Competing Risk Analysis
- "The KM LRFS estimate may overestimate LR-free survival given the substantial competing mortality in this cohort ([n]/[N], [x]% of patients died during follow-up)."
- "Aalen–Johansen CIF for LR (with death as competing event) was [x.xx]% at 5 years and [x.xx]% at 10 years, lower than the KM-based estimate."
- Reference Supplementary Table S2 for full CIF data

---

## Writing Rules (R4 Standard)

- Past tense throughout
- Numerals for all statistics (e.g., "3 patients", not "three patients")
- Format: N=2,757; HR 1.75 (not 1.750); 95% CI with en-dash (1.53–2.01); p<0.001 or exact p to 3 decimal places
- Do NOT interpret — only report
- Do NOT use "significantly" unless p<0.05 pre-specified threshold met AND it is the pre-specified primary outcome
- Do NOT discuss mechanism or compare to other studies (that is Discussion)
- Do NOT introduce new analyses not in SAP without flagging as post-hoc
- Tables and figures take precedence — text complements, not duplicates
- Flag small subgroup estimates as exploratory inline (not only in Discussion)

---

## Consistency Check (before finalizing)
- [ ] N in Results matches N in Methods
- [ ] Complete-case N matches SAP
- [ ] EPV reported for all three outcomes
- [ ] Bootstrap CI format correct (apparent / optimism / corrected)
- [ ] MICE pooled C matches supplementary table
- [ ] Schoenfeld p-values match analysis output
- [ ] E:O ratios correctly attributed to Breslow baseline hazard
- [ ] All table numbers referenced correctly
- [ ] All figure numbers referenced correctly
- [ ] P-values in text match tables exactly
- [ ] No results appear in Methods section

---

## Required Outputs
- `manuscript/results.md` — complete Results section
- `manuscript/results_interpretation_notes.md` — separate file with clinical interpretation (for Discussion agent only, NOT part of manuscript)

## Completion Checklist
- [ ] SAP order followed: Cohort → KM → Univariable → Multivariable+Performance → MICE → PH Diagnostics → Risk Groups+Calibration → Competing Risk
- [ ] EPV statement included with cautionary note for EPV <10
- [ ] Apparent AND optimism-corrected C-statistics both reported with bootstrap CI
- [ ] MICE sensitivity reported as consistency check vs CCA
- [ ] PH violations named with p-values; stratified Cox sensitivity reported
- [ ] Integer score chart weights stated in text
- [ ] E:O calibration ratios stated with calibration plot reference
- [ ] Aalen–Johansen CIF stated with competing mortality context
- [ ] Small subgroup wide-CI estimates flagged as exploratory
- [ ] All tables and figures referenced
- [ ] Numbers consistent with Methods
