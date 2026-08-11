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
- `analysis/results-ledger.csv` plus source `.do`/`.log` for every number repeated in Discussion
- `references/search-log.md` plus PMID/DOI and Q1/Q2 verification for every literature comparator

Before drafting, run `ls -la -t` on analysis, references, manuscript, and journal directories and record the current files in `PIPELINE_STATE.md`. Copy study numbers only from the ledger. Use literature only when it was retrieved live through PubMed, Semantic Scholar, and Consensus, resolves to a real PMID/DOI record, and has verified Q1/Q2 journal status.

---

## Discussion Structure — select the variant matching GATE 1's study design

| GATE 1 Study Design | Use Variant |
|---|---|
| Clinical prediction model (TRIPOD/TRIPOD-AI), survival analysis building a model/score | **Variant A** |
| Cohort, case-control, cross-sectional (etiologic/descriptive) | **Variant B** |
| RCT | **Variant C** |
| Systematic review / meta-analysis | **Variant D** |

All variants share the **Writing Rules (R4 Standard)** near the bottom of this file.

---

## Variant A — Clinical Prediction Model / Survival Analysis (R4 Standard)

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

## Variant B — Cohort / Case-Control / Cross-Sectional (STROBE)

### B.1 Principal Findings (~150 words)
- Open: "This [cohort/case-control/cross-sectional] study examined the association between [exposure] and [outcome] in [N] [population] at [institution]."
- State the main finding with effect size: "[Exposure] was associated with [outcome] (adjusted OR/RR/HR [x.xx], 95% CI [x.xx]–[x.xx])."
- Do NOT repeat raw numbers already fully stated in Results

### B.2 Comparison with Previous Studies (~250–350 words)
- State what previous studies found on the same association; compare direction, magnitude, CI overlap
- Explain reasons for agreement or disagreement: population differences, exposure/outcome measurement, confounders adjusted, study design (this study vs prior cohort/case-control)
- Cite specific papers with their effect estimates

### B.3 Methodological Points (~150–200 words)
Address each key methodological decision, using language proportionate to actual severity:
- **Confounding**: which confounders were adjusted for and why residual confounding may remain (unmeasured variables)
- **Selection bias** (case-control): how controls were selected and whether this could bias the OR toward/away from the null
- **Information/recall bias**: how exposure/outcome were ascertained and susceptibility to misclassification
- **Reverse causation** (cross-sectional/case-control): whether temporality between exposure and outcome can be established
- **Missing data**: CCA vs imputation, and whether MAR is plausible

### B.4 Clinical/Public Health Implications (~120 words)
- State who benefits from this finding and what decision it could inform
- Use hedging appropriate to observational design: "associated with", "may contribute to" — never "causes" unless causal inference methods were explicitly used and justified
- Do NOT overclaim causation from an observational design

### B.5 Strengths (~80 words)
- List 3–4 genuine strengths: sample size, prospective design (if applicable), validated exposure/outcome measurement, adjustment for key confounders, generalisability of the source population

### B.6 Limitations (~150–200 words)
Address, as applicable to the design:
1. **Residual/unmeasured confounding** — name specific plausible unmeasured confounders
2. **Selection bias** — direction and likely magnitude if estimable
3. **Information bias** — exposure/outcome misclassification and likely direction (toward/away from null)
4. **Temporality** (cross-sectional/case-control) — cannot establish which came first
5. **Generalisability** — single-centre/registry-specific limitations
6. **Missing data** — proportion excluded and assumption required

Do NOT soften with "however, our study has several strengths." Limitations stand alone.

### B.7 Future Research (~60 words)
- State 2–3 specific directions: replication in another population, prospective design to address temporality, additional confounder measurement

### B.8 Conclusion (~80 words, also written to `manuscript/conclusion.md`)
- Restate the main association finding with hedged causal language
- Match exactly to study objective from GATE 1

---

## Variant C — RCT (CONSORT)

### C.1 Principal Findings (~150 words)
- Open: "This randomised controlled trial evaluated [intervention] versus [comparator] for [primary outcome] in [N] [population] at [site(s)]."
- State the primary outcome result with effect estimate and whether the pre-specified hypothesis (superiority/non-inferiority) was met

### C.2 Comparison with Previous Trials (~250–350 words)
- Compare with existing trial evidence/meta-analyses on the same question: direction, magnitude, consistency
- Explain differences in population, dose/regimen, comparator, follow-up duration, or outcome definition

### C.3 Internal Validity (~150–200 words)
- Assess whether randomisation achieved balance (reference baseline table)
- Assess adequacy of blinding and any potential for detection/performance bias
- Assess adherence/protocol deviations and their likely impact on the ITT estimate
- Assess completeness of follow-up and handling of missing outcome data

### C.4 Clinical Implications (~120 words)
- State the practical treatment decision this finding supports, and for which patient population specifically
- Do NOT overstate: a single trial rarely changes practice alone unless pre-specified as definitive/pivotal

### C.5 Strengths (~80 words)
- Randomisation and allocation concealment, blinding achieved, pre-registration, low loss to follow-up, adequately powered

### C.6 Limitations (~150–200 words)
1. **External validity** — how representative the trial population is of the broader treatment-eligible population (eligibility criteria restrictiveness)
2. **Blinding limitations** — if open-label or blinding imperfect, state impact
3. **Duration of follow-up** — whether long-term outcomes/harms are captured
4. **Protocol deviations/non-adherence** — magnitude and likely direction of bias
5. **Generalisability** — single-site vs multi-site, healthcare-system specific factors

### C.7 Future Research (~60 words)
- Longer-term follow-up, replication in a broader/different population, head-to-head trial against another active comparator

### C.8 Conclusion (~80 words, also written to `manuscript/conclusion.md`)
- Restate the primary result and whether it supports a change in practice
- Match exactly to the pre-specified hypothesis from GATE 1

---

## Variant D — Systematic Review / Meta-analysis (PRISMA)

### D.1 Summary of Main Findings (~150 words)
- Open: "This systematic review and meta-analysis of [n] studies ([N] participants) examined [PICO question]."
- State the pooled effect estimate, 95% CI, and direction of effect

### D.2 Comparison with Previous Reviews (~200–300 words)
- Compare with prior systematic reviews on the same question: consistency of pooled estimate, additional studies now included, methodological differences (search date, eligibility, RoB tool)
- If this review updates a prior one, state what changed and why (new trials, corrected data, refined eligibility)

### D.3 Interpretation of Heterogeneity and Risk of Bias (~150–200 words)
- Interpret the I² value in context: what it implies about consistency of effect across studies
- Discuss whether subgroup/meta-regression explained heterogeneity, or whether it remains unexplained
- Discuss how risk-of-bias distribution across included studies affects confidence in the pooled estimate (e.g., "sensitivity analysis restricted to low-risk-of-bias studies yielded a consistent/attenuated estimate of [x.xx]")

### D.4 Certainty of Evidence (~100 words)
- State the GRADE certainty rating per outcome and the primary reasons for downgrading (risk of bias, inconsistency, indirectness, imprecision, publication bias)
- State what this certainty level means for confidence in the estimate

### D.5 Clinical/Policy Implications (~120 words)
- State what decision-makers (clinicians, guideline panels) can reasonably conclude given the certainty level
- Do NOT recommend a practice change from low/very-low certainty evidence without explicit qualification

### D.6 Strengths (~80 words)
- Comprehensive search strategy, pre-registered protocol, dual independent screening/extraction, formal risk-of-bias and GRADE assessment

### D.7 Limitations (~150–200 words)
1. **Heterogeneity** — clinical/methodological heterogeneity across included studies limiting pooled interpretation
2. **Risk of bias in included studies** — specific domains most commonly at high/unclear risk
3. **Publication bias** — possibility of unpublished null/negative studies, especially if funnel plot asymmetric or <10 studies precluded formal testing
4. **Language/database restrictions** — studies potentially missed
5. **Indirectness** — if included populations/interventions vary from the review question

### D.8 Future Research (~60 words)
- State specific evidence gaps: populations/subgroups needing dedicated trials, outcomes not yet measured consistently, need for standardised outcome reporting

### D.9 Conclusion (~80 words, also written to `manuscript/conclusion.md`)
- Restate the pooled estimate and certainty level
- State the practical implication proportionate to that certainty level
- Match exactly to the review's PICO(S) objective from GATE 1

---

## Writing rules — mandatory NEJM/Lancet discipline plus R4 structure
- Past tense for your own results; present tense for established facts and prior literature
- Hedging language calibrated to design: observational designs (A/B) mandate "suggest", "may inform", "associated with", "pending external validation" — never "proves", "causes", "can be used to guide"; RCTs (C) may state a causal effect directly since randomisation supports causal inference for the ITT estimate; SR/MA (D) hedges by GRADE certainty level, not by design alone
- Every comparison to prior literature must cite a specific paper with its effect size
- No new results introduced in Discussion
- Limitations must be proportionate — state "major" when major (e.g., large CCA exclusion, high heterogeneity, high risk of bias in most included studies)
- Variant A: use "internally validated" not "validated" — reserve "validated" for external validation
- Use concise, evidence-led clinical-journal prose with concrete subjects and calibrated interpretation.
- Remove redundant/repetitive summaries of Results, duplicated effect estimates, stock transitions, vague intensifiers, generic AI-style balancing phrases, and meta-commentary.
- Do not copy wording from published NEJM/Lancet articles; follow target-specific editorial conventions only.

---

## Required Outputs
- `manuscript/discussion.md` — complete Discussion section
- `manuscript/limitations_section.md` — standalone limitations (for GATE 3 review)
- `manuscript/conclusion.md` — standalone Conclusion paragraph

## Completion Checklist — shared across all variants
- [ ] Correct variant selected for GATE 1's study design (A/B/C/D)
- [ ] All subsections of the chosen variant present
- [ ] Principal findings open with study design + N + key effect estimate
- [ ] Prior literature comparisons cite specific papers with effect sizes
- [ ] Limitations are honest, quantified, and not minimised
- [ ] Conclusion matches GATE 1 objective
- [ ] Word count within journal limit
- [ ] No new results introduced
- [ ] Every study number was copied from the results ledger and matches source `.do`/`.log`
- [ ] Every literature comparison has live connector evidence, a real PMID/DOI, and verified Q1/Q2 status
- [ ] NEJM/Lancet editorial pass found no redundant, repetitive, or AI-style prose

## Completion Checklist — Variant A only
- [ ] Missing data addressed as "major limitation" if CCA exclusion >30%
- [ ] PH violations discussed with stratified sensitivity results
- [ ] EPV limitation stated for low-EPV models
- [ ] Ridge penalisation sensitivity stated
- [ ] Competing risk (Aalen–Johansen vs KM) discussed
- [ ] Clinical implications use mandated hedging: "pending external validation"

## Completion Checklist — Variant B only
- [ ] Confounding, selection bias, and information bias each explicitly addressed
- [ ] No causal language used without explicit justification
- [ ] Temporality limitation stated for cross-sectional/case-control designs

## Completion Checklist — Variant C only
- [ ] Internal validity (randomisation balance, blinding, adherence) explicitly assessed
- [ ] External validity/generalisability of trial population addressed
- [ ] Conclusion states whether the pre-specified hypothesis was met

## Completion Checklist — Variant D only
- [ ] GRADE certainty rating and downgrading reasons stated per outcome
- [ ] Heterogeneity (I²) interpreted, not just reported
- [ ] Publication bias discussed (or explicitly noted as untestable with <10 studies)
- [ ] Clinical/policy implications proportionate to certainty level
