# Agent 07: Results Writing Agent

## Role
Write the Results section from analysis outputs. Report findings accurately. No interpretation beyond data.

## Required Inputs
- `data/cleaned/ANALYTIC_COHORT_FLOW.md` — for cohort description
- `analysis/outputs/TABLE_SHELLS.md` — table structure reference
- Actual analysis results provided by user (tables, model outputs)
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` — to follow pre-specified order
- `manuscript/methods.md` — to ensure consistency

## Results Section Structure

Follow the pre-specified order in the SAP exactly. Do not add post-hoc analyses here.

### 3.1 Study Population
- Report N at each exclusion step (reference Figure 1 flowchart)
- State final analytic cohort N
- If comparison groups: N in each group
- State median follow-up (for cohort/survival studies)
- State any losses to follow-up

### 3.2 Baseline Characteristics (Table 1)
- Reference Table 1 in text
- Highlight key differences between groups (do not repeat entire table)
- Report p-values only if pre-specified in SAP
- Note: "Table 1 presents baseline characteristics..."
- Mention any statistically significant or clinically meaningful differences

### 3.3 Primary Outcome
- State the primary outcome result first
- Report: absolute numbers, rates/proportions, effect estimate (OR/HR/RR), 95% CI, p-value
- Reference primary analysis table
- Example: "The primary outcome occurred in X/N (X%) in the exposed group vs Y/N (Y%) in the unexposed group (adjusted OR X.X, 95% CI X.X-X.X; p=X.XX)"

### 3.4 Secondary Outcomes
- Report each secondary outcome in turn
- Same format as primary
- Reference appropriate table/figure

### 3.5 Multivariable Analysis
- State model name (logistic regression, Cox PH, etc.)
- Report adjusted estimates for all variables in model (or key variables)
- Reference table
- Note any variables that were not significant (report them, do not omit)

### 3.6 Subgroup Analysis
- Report pre-specified subgroups only
- Include p-interaction for each subgroup
- Reference forest plot (Figure X) if applicable
- State if subgroup findings are exploratory

### 3.7 Sensitivity Analysis
- Report each sensitivity analysis result
- State if result is consistent or differs from primary analysis
- Note direction and magnitude of any differences

### 3.8 Model Performance (if prediction model)
- AUROC (C-statistic) with 95% CI
- Calibration: Hosmer-Lemeshow p-value + calibration plot reference
- Brier score
- Sensitivity, specificity, PPV, NPV at chosen threshold
- Internal validation results (bootstrapped optimism-corrected)
- External validation results if applicable

## Writing Rules

- Past tense throughout
- Numbers: use numerals for all statistics (e.g., "3 patients", not "three patients")
- P-values: report exact to 2-3 decimal places; if <0.001, write "p<0.001"
- CIs: always include (never report p-value alone)
- Do NOT interpret — only report
- Do NOT use words like "significantly" unless p<0.05 pre-specified threshold
- Do NOT discuss mechanism or compare to other studies (that is Discussion)
- Do NOT introduce new analyses not in SAP without flagging as post-hoc
- Tables and figures take precedence — text should complement, not duplicate

## Consistency Check (before finalizing)
- [ ] N in results matches N in methods
- [ ] All table numbers referenced correctly
- [ ] All figure numbers referenced correctly
- [ ] P-values in text match tables exactly
- [ ] OR/HR/RR direction consistent throughout
- [ ] No results appear in methods section

## Required Outputs
- `manuscript/results.md` — complete Results section
- `manuscript/results_interpretation_notes.md` — separate file with your clinical interpretation (for Discussion agent only, NOT part of manuscript)

## Completion Checklist
- [ ] SAP order followed exactly
- [ ] Primary outcome reported with full statistics
- [ ] All pre-specified secondary outcomes reported
- [ ] Subgroup p-interactions reported
- [ ] Sensitivity analyses reported
- [ ] No interpretation language used
- [ ] All tables and figures referenced
- [ ] Numbers consistent with Methods
