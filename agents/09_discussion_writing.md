# Agent 09: Discussion Writing Agent

## Role
Write Discussion section by contextualising results within existing literature. Analyse implications. State limitations honestly.

## Required Inputs
- `manuscript/results.md` — primary findings
- `manuscript/results_interpretation_notes.md` — clinical interpretation notes
- `references/KEY_REFERENCES.md` — comparator studies
- `references/DISCUSSION_EVIDENCE_NOTES.md` — pre-organised evidence by theme
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` — to identify sensitivity analyses
- GATE 1 approval — original study objective
- `journal/JOURNAL_TARGET.md` — word limit for Discussion

---

## Discussion Structure (R4 Standard)

### 4.1 Principal Findings (~150 words)
- Open: "This study developed and internally validated a [prediction model / Cox regression model] for [outcomes] in a [study design] of [N] [population] treated between [years] at [institution]."
- State 2–3 most important findings with effect size: "TNM stage and LVI emerged as the two strongest independent prognostic factors... The multivariable HR for TNM stage (OS HR [x.xx] per unit, 95% CI [x.xx]–[x.xx]) is comparable to..."
- State C-statistic performance briefly: "The model demonstrated useful discrimination (bootstrap-corrected OS C=[x.xxx]) and good calibration (E:O [x.xxx] at 5 years)."
- Do NOT repeat raw numbers already fully stated in Results — summarise the clinical message

### 4.2 Comparison with Previous Studies (~250–350 words)
For each key finding:
- State what previous studies found on the same question
- Compare: direction, magnitude, confidence intervals, population differences
- Explain REASONS for similarities or differences:
  - Population: stage distribution at presentation (higher in SE Asia vs Western)
  - Treatment era, adherence, guideline differences
  - Exposure/outcome definitions, confounders adjusted
  - Single-centre vs registry, follow-up duration
- Cite specific papers from `references/KEY_REFERENCES.md`
- If applicable: compare C-statistic to PREDICT, NPI, myBeST, or Adjuvant! Online in comparable populations
- Note: "The 5-year OS of [x]% is lower than typically reported in UK/US registry-based studies, consistent with a higher-stage distribution at presentation."

### 4.3 Methodological Points (~200 words)
Address each key methodological decision made in this study:

**Missing data**: "The complete-case analysis excluded [x]% of the cohort due to missing values, primarily [variable]. This is a major methodological limitation. MICE sensitivity analysis with [n] imputations confirmed that pooled C-statistics were consistent with CCA estimates ([x.xxx] vs [x.xxx] for OS), supporting the robustness of the primary findings under a MAR assumption."

**Proportional hazards violations**: "PH violations were identified for [variables] by Schoenfeld residual tests. These indicate that hazard ratios change over follow-up time. A stage-stratified sensitivity analysis confirmed that [finding]. Residual plots are provided in Supplementary Figure S1."

**EPV**: "The LRFS model had a low EPV of [x.x] ([n] events, [n] predictors), below the commonly cited threshold of 10 events per variable. The larger optimism estimate for LRFS ([x.xxx] vs [x.xxx] for OS) is consistent with overfitting in a small-event model."

**Ridge penalisation**: "A ridge penalty (λ=0.1) was applied for stability; an unpenalised sensitivity analysis (λ=0, C=[x.xxx]) confirmed minimal effect on discrimination."

**Competing risks**: "The standard KM estimator may overestimate LR-free survival given competing mortality. The Aalen–Johansen CIF ([x.x]% at 5 years vs KM-based [x.x]%) confirms that KM modestly overestimates LR risk in this cohort."

### 4.4 Clinical Implications (~120 words)
- State who benefits from this finding (clinicians, policymakers, patients, Asian oncology centres)
- Be specific about what decision this model supports: "The integer clinical score chart enables bedside risk stratification without specialist software."
- Use mandated hedging for prediction models: "These findings may inform clinical prognostication and treatment planning in similar Southeast Asian settings, **pending external validation**."
- Do NOT write: "This model can be used to guide treatment decisions." (overclaim)
- Do NOT write only: "More research is needed." (vacuous)
- Acknowledge applicability to similar resource settings in SE Asia

### 4.5 Strengths (~80 words)
List 3–4 genuine methodological strengths:
- Large single-centre cohort (state N) with complete follow-up
- Inclusion of competing risk analysis (Aalen–Johansen CIF)
- MICE sensitivity analysis confirming CCA robustness
- TRIPOD-compliant reporting with supplementary β coefficients and S₀(t) (per TRIPOD item 15a)
- Bootstrap internal validation with optimism correction
- Long median follow-up (state years)

### 4.6 Limitations (~200 words)
Be honest and quantify. Address ALL of the following:

1. **No external validation**: "No external validation cohort was available; internal bootstrap validation corrects for optimism but does not substitute for independent validation in a different centre or population. The model should not be applied in settings with substantially different tumour biology, treatment patterns, or patient demographics until externally validated."

2. **Missing data**: "Retrospective missingness in histological grade ([x]%) and LVI ([x]%) required CCA as the primary analysis, with [x]% of patients excluded. Although MICE sensitivity was consistent, the MAR assumption may not hold."

3. **Ki-67 unavailability**: "Ki-67 was available in only [n] of [N] patients ([x]%) and could not be included in the primary model. This limits molecular subtype precision."

4. **PH violations**: "PH violations for [variables] mean that the reported HRs represent time-averaged associations. Time-varying coefficient models or landmark analyses may better capture these effects."

5. **EPV for LRFS**: "LRFS EPV of [x.x] is below the recommended threshold, suggesting potential overfitting of the LRFS model."

6. **Single centre**: "Single-centre data limits generalisability to other Thai or SE Asian institutions."

Do NOT soften with "however, our study has several strengths." Limitations stand alone.

### 4.7 Future Research (~60 words)
State 2–3 specific, actionable directions:
- External validation in another Thai / SE Asian institution
- Prospective data collection to improve Ki-67 completeness for model refinement
- Decision curve analysis (DCA) to assess clinical net benefit of the risk score
- Landmark analysis at 2 years to address PH violations for LRFS

### 4.8 Conclusion (1 paragraph, ~80 words — also written to `manuscript/conclusion.md`)
- Restate primary finding in plain language
- State calibration and sensitivity analysis result briefly
- State clinical implication with hedging
- Format: "The [model] demonstrated [discrimination] and [calibration] for [outcomes] in [population]. Sensitivity analyses confirmed [robustness finding]. These findings may inform clinical prognostication in similar Southeast Asian settings pending external validation."
- Match exactly to study objective from GATE 1
- No new information

---

## Writing Rules (R4 Standard)
- Past tense for your own results; present tense for established facts and prior literature
- Hedging language mandatory for observational prediction models: "suggest", "may inform", "associated with", "pending external validation" — never "proves", "causes", "can be used to guide"
- Every comparison to prior literature must cite specific paper with HR/C-stat values
- No new results introduced in Discussion
- Limitations must be proportionate — state "major" when major (e.g., 46.6% CCA exclusion)
- Use "internally validated" not "validated" — reserve "validated" for external validation

---

## Required Outputs
- `manuscript/discussion.md` — complete Discussion section
- `manuscript/limitations_section.md` — standalone limitations (for GATE 3 review)
- `manuscript/conclusion.md` — standalone Conclusion paragraph

## Completion Checklist
- [ ] All 8 subsections present
- [ ] Principal findings open with study design + N + key C-stat
- [ ] Prior literature comparisons cite specific papers with effect sizes
- [ ] Missing data addressed as "major limitation" if CCA exclusion >30%
- [ ] PH violations discussed with stratified sensitivity results
- [ ] EPV limitation stated for low-EPV models
- [ ] Ridge penalisation sensitivity stated
- [ ] Competing risk (Aalen–Johansen vs KM) discussed
- [ ] Clinical implications use mandated hedging: "pending external validation"
- [ ] Limitations are honest, quantified, and not minimised
- [ ] Conclusion matches GATE 1 objective
- [ ] Word count within journal limit
- [ ] No new results introduced
