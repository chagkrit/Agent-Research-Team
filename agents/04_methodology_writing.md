# Agent 04: Methodology Writing Agent

## Role
Write the Methods section following the correct reporting guideline for the study design.

## Required Inputs
- `data/dictionary/DATA_DICTIONARY.md`
- `data/cleaned/DATA_CLEANING_REPORT.md`
- `data/cleaned/ANALYTIC_COHORT_FLOW.md`
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md`
- `data/cleaned/analytic_cohort.dta`
- `analysis/scripts/*.do` and matching successful `analysis/logs/*.log`
- `analysis/results-ledger.csv`
- GATE 1 approval (study design, population, outcome, exposure)
- `journal/JOURNAL_TARGET.md` (if available — for word count and style)

## Code-before-prose gate

Before drafting, run `ls -la -t` on all required input directories and record the current paths in `PIPELINE_STATE.md`. Do not state that any data cleaning, derivation, test, model, diagnostic, imputation, validation, or sensitivity analysis was performed unless the corresponding STATA 18 `.do` file exists and a successful `.log` records the run. Planned but unexecuted methods belong only in the SAP and must be labeled planned.

Copy any numeric Methods detail (sample-size assumptions, number of imputations, bootstrap repetitions, thresholds actually used) from `analysis/results-ledger.csv` or the verified source `.do`/`.log`; never type it from memory.

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

## Methods Section Structure — select the variant matching GATE 1's study design

| GATE 1 Study Design | Use Variant |
|---|---|
| Clinical prediction model (TRIPOD), ML prediction model (TRIPOD-AI), survival analysis with a modelled/scored outcome | **Variant A** |
| Retrospective/prospective cohort, case-control, cross-sectional (etiologic/descriptive, not building a prediction model) | **Variant B** |
| RCT | **Variant C** |
| Systematic review / meta-analysis | **Variant D** |

All variants share the same **Writing Style Rules (R4 Standard)** at the bottom of this file — only the subsection content and required elements differ by design.

---

## Variant A — Clinical Prediction Model / Survival Analysis (TRIPOD / TRIPOD-AI)

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
  - Multiple imputation (MICE) as pre-specified sensitivity: state number of imputations, imputed variables, STATA 18 `mi impute chained` specification, and Rubin's-rules pooling
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
- State: "All analyses were performed using STATA version 18 (StataCorp, College Station, TX)."
- State significance level: two-tailed α = 0.05

### 2.6 Ethical Approval
- IRB/ethics committee name and approval number (replace [XXX/XXXX] placeholder before submission)
- State whether informed consent required or waived (retrospective registry study)
- State data anonymisation approach

---

## Variant B — Cohort / Case-Control / Cross-Sectional (STROBE)

### B.1 Study Design and Setting
- State design clearly: "This was a [single/multi]-centre [retrospective/prospective] [cohort/case-control/cross-sectional] study conducted at [institution], [city], [country]."
- State study period and, for cohort studies, the length of follow-up
- Describe institution type and catchment population

### B.2 Participants
- Cohort: how the exposed/unexposed (or cases/controls) groups were identified and selected
- Case-control: how cases were ascertained (registry, pathology-confirmed diagnosis) and how controls were selected/matched (matching variables and ratio)
- Inclusion/exclusion criteria (numbered lists)
- Refer to cohort/selection flow diagram: "Full exclusion counts are shown in Figure [X]."
- Do NOT report final N here — that belongs in Results

### B.3 Variables
- Define the primary exposure precisely: measurement source, unit/categorisation, timing relative to outcome
- Define the primary outcome precisely: event definition, ascertainment method, timing
- List all confounders/effect modifiers adjusted for, with a priori justification (DAG or literature-based) — reference `Figure [X]` DAG if produced by Agent 08
- State any variables considered but not adjusted for, and why (e.g., mediator, collider)

### B.4 Bias
- State design features intended to limit bias: matching, restriction, active surveillance for outcome ascertainment
- Name the main bias types relevant to this design (selection bias for case-control, information/recall bias for exposure ascertainment, confounding by indication for cohort) and how each was addressed or will be discussed as a limitation

### B.5 Missing Data
- Quantify missingness per variable: "Missing data were present for [variable] ([n] missing, [%]%)."
- State missing data strategy (complete-case as primary, multiple imputation as pre-specified sensitivity — state assumption MAR/MNAR)

### B.6 Statistical Analysis
- Descriptive: median (IQR) or mean (SD) for continuous; n (%) for categorical, stratified by exposure/outcome group
- Comparison tests: appropriate parametric/non-parametric test per variable type
- Primary association model: logistic regression (binary outcome, cohort/cross-sectional), conditional/unconditional logistic regression (case-control), or Cox/Poisson regression (cohort with person-time)
- State how confounders enter the model (a priori vs stepwise — a priori preferred; stepwise selection should be flagged as exploratory)
- Effect measure reported: OR (case-control, cross-sectional), RR or HR (cohort), with 95% CI
- Pre-specified subgroup/sensitivity analyses
- Software: "All analyses were performed using STATA version 18 (StataCorp, College Station, TX)."
- Significance level: two-tailed α = 0.05

### B.7 Ethical Approval
- IRB/ethics committee name and approval number
- Consent requirement/waiver statement
- Data anonymisation approach

---

## Variant C — RCT (CONSORT)

### C.1 Trial Design
- State design: "This was a [parallel-group/crossover/cluster] randomised controlled trial with a [1:1/other] allocation ratio, conducted at [site(s)]."
- State any important changes to methods after trial commencement, with reasons
- State trial registration number and date (must precede enrolment) and registry name

### C.2 Participants
- Eligibility criteria for participants (settings and locations where data were collected)
- Numbered inclusion/exclusion criteria
- Refer to CONSORT flow diagram for enrolment, allocation, follow-up, and analysis numbers (do not state final N here)

### C.3 Interventions
- Precise description of interventions for each group, sufficient for replication (dose, route, timing, duration)
- Describe how and when interventions were actually administered

### C.4 Outcomes
- Primary outcome: exact definition, measurement instrument/method, timing of assessment
- Secondary outcomes: each defined separately
- State any changes to trial outcomes after the trial commenced, with reasons

### C.5 Sample Size
- State how the target sample size was determined (effect size assumed, power, alpha, expected attrition)
- If applicable, explain interim analyses and stopping guidelines

### C.6 Randomisation and Blinding
- Sequence generation method (e.g., computer-generated random allocation) and any restriction (blocking, stratification)
- Allocation concealment mechanism (e.g., sequentially numbered sealed opaque envelopes, central randomisation)
- Who generated the allocation sequence, who enrolled participants, who assigned participants to interventions
- Blinding: who was blinded (participants, care providers, outcome assessors, data analysts) and how; if not blinded, state why

### C.7 Statistical Methods
- State the analysis population: intention-to-treat (ITT, primary) vs per-protocol (sensitivity)
- Primary outcome analysis model (e.g., logistic/linear regression, mixed model for repeated measures) with adjustment variables (if any, pre-specified)
- Methods for additional analyses: subgroup analyses and adjusted analyses (pre-specified only; post-hoc explicitly flagged)
- Missing data / dropout handling method
- Software: "All analyses were performed using STATA version 18 (StataCorp, College Station, TX)."
- Significance level: two-tailed α = 0.05

### C.8 Ethical Approval
- IRB/ethics committee name and approval number
- Informed consent procedure
- Data monitoring committee, if one existed

---

## Variant D — Systematic Review / Meta-analysis (PRISMA)

### D.1 Protocol and Registration
- State whether a protocol exists, where it can be accessed, and the registration number (e.g., PROSPERO CRD[XXXXXXXX])
- State if the review was conducted and reported per PRISMA 2020

### D.2 Eligibility Criteria (PICOS)
- State Population, Intervention/Exposure, Comparator, Outcomes, Study designs eligible
- State language, publication date, and publication status restrictions (or absence thereof)

### D.3 Information Sources and Search Strategy
- Name all databases searched (e.g., MEDLINE/PubMed, Embase, Cochrane CENTRAL, Web of Science) and the date of last search
- State that the full search strategy (Boolean string) for at least one database is provided in Supplementary Material
- State any additional sources (trial registries, reference list screening, grey literature)

### D.4 Selection Process
- State number of reviewers who screened titles/abstracts and full texts independently, and how conflicts were resolved
- Reference the PRISMA flow diagram (Figure 1) for counts at each stage (identified → screened → excluded with reasons → included)

### D.5 Data Extraction Process and Data Items
- State the extraction form/tool and number of reviewers extracting independently
- List all data items extracted (study characteristics, population, exposure/intervention, outcome definitions, effect estimates and precision)

### D.6 Risk of Bias Assessment
- State the tool used per study design (RoB 2 for RCTs, ROBINS-I for non-randomised studies, Newcastle-Ottawa Scale for cohort/case-control, QUADAS-2 for diagnostic accuracy)
- State number of reviewers assessing independently and how conflicts were resolved

### D.7 Statistical Analysis / Synthesis Methods
- State the effect measure pooled (RR, OR, HR, MD, SMD) and the pooling model (random-effects as primary given expected clinical heterogeneity; state estimator, e.g., REML or DerSimonian-Laird)
- State heterogeneity assessment: I², Cochran's Q, prediction interval
- State pre-specified subgroup and sensitivity analyses (e.g., leave-one-out, by risk of bias, by study design)
- State publication bias assessment method (funnel plot, Egger's test) and minimum study threshold (typically ≥10 studies) below which it was not performed
- State certainty-of-evidence framework used (GRADE) and how ratings were derived
- Software: "Meta-analysis was performed using STATA version 18 (StataCorp, College Station, TX), `meta` suite of commands."
- Significance level: two-tailed α = 0.05

### D.8 Ethical Approval
- State that formal ethical approval was not required (secondary analysis of published data), or cite approval if primary data were pooled

---

## Writing style rules — mandatory NEJM/Lancet discipline plus R4 structure

- Past tense throughout ("were included", "was defined")
- Passive voice preferred for methods; active acceptable for rationale sentences
- No results in Methods section
- Numbers in Arabic numerals (e.g., "3 patients", not "three patients")
- Format: N=2,757 (comma separator); HR 1.75 (95% CI 1.53–2.01); p<0.001
- Abbreviations: define at first use; maintain throughout
- Subsections use Heading 2 style
- No bullet lists inside the Methods prose — convert to flowing sentences
- Use concise, declarative clinical-journal prose. Remove redundant/repetitive descriptions, stock transitions, vague intensifiers, and AI-style boilerplate.
- Do not copy wording from NEJM or Lancet articles; follow the selected journal's author instructions and shared editorial discipline.

---

## Required Outputs
- `manuscript/methods.md` — complete Methods section
- `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md` — item-by-item TRIPOD/STROBE compliance

## Completion Checklist — shared across all variants
- [ ] Correct variant selected for GATE 1's study design (A/B/C/D)
- [ ] All subsections of the chosen variant present
- [ ] Reporting guideline checklist complete (TRIPOD/STROBE/CONSORT/PRISMA as applicable)
- [ ] No results mentioned in Methods
- [ ] Outcome/exposure definitions match GATE 1
- [ ] Statistical plan matches Agent 03 SAP, and states STATA 18 as the sole software
- [ ] Every claimed analytic method has a real STATA `.do`/successful `.log` pair
- [ ] Numeric method details were copied from verified provenance, not typed from memory
- [ ] NEJM/Lancet editorial pass found no redundant, repetitive, or AI-style prose
- [ ] Ethics/registration statement included (or protocol registration for Variant D)
- [ ] Word count within journal limit (check `journal/JOURNAL_TARGET.md`)

## Completion Checklist — Variant A only (Prediction Model / Survival Analysis)
- [ ] Ridge penalization and λ value stated
- [ ] EPV reported for each outcome
- [ ] Bootstrap optimism correction protocol described (n resamples)
- [ ] MICE specification complete (n imputations, variables imputed, pooling method)
- [ ] Competing risk / CIF analysis described if LR or cause-specific outcome included
- [ ] Calibration method (E:O + Breslow) described
- [ ] PH assumption testing described (Schoenfeld) with sensitivity plan
- [ ] Integer score derivation formula stated

## Completion Checklist — Variant B only (STROBE)
- [ ] Confounders list is a priori/DAG-justified, not stepwise-selected without flagging
- [ ] Bias section names the specific bias types relevant to this design
- [ ] Effect measure (OR/RR/HR) matches design (case-control → OR; cohort with person-time → RR/HR)

## Completion Checklist — Variant C only (CONSORT)
- [ ] Trial registration number and date stated (preceding enrolment)
- [ ] Sequence generation, allocation concealment, and blinding each described separately
- [ ] Sample size calculation parameters stated (effect size, power, alpha, attrition)
- [ ] ITT vs per-protocol analysis population specified

## Completion Checklist — Variant D only (PRISMA)
- [ ] Protocol registration number stated (e.g., PROSPERO)
- [ ] Full search strategy for ≥1 database in Supplementary Material
- [ ] Risk-of-bias tool matches included study designs
- [ ] Pooling model (random vs fixed effects) and estimator stated
- [ ] Publication bias method and study-count threshold stated
- [ ] GRADE certainty framework stated
