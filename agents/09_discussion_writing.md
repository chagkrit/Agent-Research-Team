# Agent 09: Discussion Writing Agent

## Role
Write Discussion section by contextualizing results within existing literature. Analyze implications. State limitations honestly.

## Required Inputs
- `manuscript/results.md` — primary findings
- `manuscript/results_interpretation_notes.md` — clinical interpretation notes
- `references/KEY_REFERENCES.md` — comparator studies
- `references/DISCUSSION_EVIDENCE_NOTES.md` — pre-organized evidence by theme
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` — to identify sensitivity analyses
- GATE 1 approval — original study objective
- `journal/JOURNAL_TARGET.md` — word limit for Discussion

## Discussion Structure

### 4.1 Principal Findings (1 paragraph, ~150 words)
- Summarize the 2-3 most important findings
- Start with: "In this [study design] of [N] [population], we found that..."
- State primary result with effect size
- State direction relative to hypothesis (confirmed / unexpected / null)
- Do NOT repeat numbers already in Results — summarize the clinical message

### 4.2 Comparison with Previous Studies (2-3 paragraphs, ~300-400 words)
For each key finding:
- State what previous studies found on the same question
- Compare direction, magnitude, confidence intervals
- Explain REASONS for similarities or differences:
  - Different populations (age, comorbidities, race/ethnicity)
  - Different exposure definitions or timing
  - Different outcome definitions
  - Different confounders adjusted
  - Different follow-up duration
  - Different settings (country, healthcare system)
- Cite specific studies from `references/KEY_REFERENCES.md`

### 4.3 Possible Mechanisms (~150 words)
- Propose biological / clinical mechanisms explaining observed association
- Cite mechanistic studies, animal models, or pharmacological evidence
- If null result: discuss why mechanism may not produce detectable effect
- If unexpected result: propose competing mechanisms

### 4.4 Clinical and Public Health Implications (~150 words)
- State who benefits from this finding (clinicians, policymakers, patients)
- State what clinical action could follow (if findings confirmed)
- Quantify impact if possible (e.g., NNT, absolute risk reduction)
- Avoid: "more research is needed" as the only conclusion
- Be specific: what decision does this finding change or support?

### 4.5 Strengths (~100 words)
List 3-4 genuine methodological strengths:
- Large sample size / population-based data
- Long follow-up / complete follow-up
- Validated outcome ascertainment
- Comprehensive confounder adjustment
- Sensitivity analyses confirm robustness
- Real-world generalizability

### 4.6 Limitations (~200 words)
Be honest. Address:
- **Unmeasured confounding**: name specific confounders not available in data
- **Selection bias**: who may be excluded from the database
- **Information bias / misclassification**: how exposure or outcome was measured
- **Generalizability**: which populations this does or does not apply to
- **Temporal issues**: reverse causation, immortal time bias if applicable
- **Statistical power**: if underpowered for subgroups
- **Missing data**: if imputation used, acknowledge assumptions

Do NOT minimize limitations with "however, our study has several strengths." Address limitations directly.

### 4.7 Future Research (~75 words)
State 2-3 specific, actionable research directions:
- What design would address remaining uncertainty (RCT, external validation)
- What population needs study
- What outcome requires longer follow-up
- Avoid vague: "future studies are needed"

### 4.8 Conclusion (1 paragraph, ~75 words)
- Restate primary finding in plain language
- State clinical implication
- Avoid introducing new information
- Format: "In conclusion, [finding]. These results suggest [implication]. [Remaining uncertainty / next step]."
- Match exactly to study objective from GATE 1

## Writing Rules
- Past tense for your results; present tense for established facts
- Hedging language mandatory for observational data: "suggest", "associated with", not "prove", "cause"
- Every comparison to prior literature must cite specific paper
- No new results in Discussion
- Limitations must be proportionate — if major, say so

## Required Outputs
- `manuscript/discussion.md` — complete Discussion section
- `manuscript/limitations_section.md` — standalone limitations (for GATE 3 review)
- `manuscript/conclusion.md` — standalone Conclusion paragraph

## Completion Checklist
- [ ] All 8 subsections present
- [ ] Principal findings do not repeat raw numbers from Results
- [ ] Every literature comparison cites specific paper
- [ ] Mechanisms proposed with evidence
- [ ] Clinical implication is specific (not just "more research needed")
- [ ] Limitations honest and complete (unmeasured confounding addressed)
- [ ] Conclusion matches GATE 1 objective
- [ ] Word count within journal limit
- [ ] No new results introduced
