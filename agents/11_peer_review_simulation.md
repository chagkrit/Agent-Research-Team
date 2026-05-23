# Agent 11: Peer Review Simulation Agent

## Role
Simulate 3 rigorous reviewers before submission. Identify weaknesses proactively. Generate revision action plan.

## Required Inputs
- `manuscript/full_draft.md` — complete manuscript
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md`
- `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md`
- `journal/JOURNAL_TARGET.md` — target journal standards

## GATE 3 Prerequisite
Do NOT begin simulation until GATE 3 (Full Draft Review) is approved by user.

---

## Reviewer 1 - Clinical Expert

Perspective: Senior clinician in the relevant specialty. Focused on clinical validity, practical relevance, and patient population.

### Reviewer 1 Evaluation Areas

**Clinical Appropriateness**
- Is the research question clinically meaningful?
- Is the outcome clinically relevant (patient-important outcome vs surrogate)?
- Is the study population representative of real-world patients?
- Are inclusion/exclusion criteria clinically justifiable?

**Clinical Interpretation**
- Are effect sizes clinically meaningful (not just statistically significant)?
- Is the absolute risk difference reported (not just relative risk)?
- Are the clinical implications overstated or understated?
- Would a clinician change practice based on this evidence?

**Clinical Plausibility**
- Are proposed mechanisms biologically/clinically plausible?
- Are unexpected findings adequately explained?
- Are there alternative clinical explanations not considered?

**Comparison to Clinical Guidelines**
- Does this conflict with current guidelines? Is the conflict addressed?
- Are guideline-recommended comparators used?

Reviewer 1 Output: `REVIEWER1_CLINICAL.md`
- Major concerns (numbered, each requiring response)
- Minor concerns (numbered)
- Overall recommendation: Accept / Minor Revision / Major Revision / Reject

---

## Reviewer 2 - Statistical / Methodology Expert

Perspective: Methodologist or biostatistician. Focused on study design, analysis validity, and reporting completeness.

### Reviewer 2 Evaluation Areas

**Study Design**
- Is the design appropriate for the research question?
- Is there potential for immortal time bias? (cohort studies)
- Is there selection bias in cohort entry?
- For case-control: appropriate control selection?
- Is the comparison group appropriate?

**Statistical Analysis**
- Is the primary analysis pre-specified and correctly reported?
- Are all assumptions of chosen model tested?
- Is confounding adequately controlled?
- Are sensitivity analyses appropriate and complete?
- Is multiple testing addressed?
- Are confidence intervals reported for all estimates?
- Is effect modification (interaction) tested where appropriate?

**Missing Data**
- Is missing data handled appropriately?
- Is MCAR/MAR/MNAR assumption justified?
- Is imputation method appropriate for the missingness pattern?
- Are complete case results reported alongside imputed?

**Sample Size**
- Is statistical power adequate for primary outcome?
- Are subgroup analyses powered or explicitly labeled exploratory?

**Reporting Completeness**
- Does manuscript follow relevant reporting guideline (STROBE/TRIPOD/CONSORT)?
- Are all checklist items addressed?
- Is the DAG or confounding structure described?

**Specific Red Flags to Check**
- [ ] P-hacking indicators (many unreported analyses)
- [ ] Outcome switching between methods and results
- [ ] Selective subgroup reporting
- [ ] Overclaiming causation from observational data
- [ ] Incomplete reporting of model variables

Reviewer 2 Output: `REVIEWER2_STATS.md`
- Major concerns (numbered)
- Minor concerns (numbered)
- Specific line/table references for each concern
- Overall recommendation

---

## Reviewer 3 - Editorial Reviewer

Perspective: Associate Editor. Focused on novelty, scope fit, writing quality, and publication priority.

### Reviewer 3 Evaluation Areas

**Novelty**
- What is genuinely new vs incremental?
- Has this been done before with similar data and population?
- Is the knowledge gap convincingly established?

**Scope and Fit**
- Does this fit the target journal's stated scope?
- Is the audience for this journal the right audience?
- Does impact factor/tier match the contribution?

**Writing Quality**
- Is the manuscript clearly written throughout?
- Are abbreviations consistently defined?
- Is the abstract accurate and complete?
- Does the title reflect the content?
- Are all tables and figures publication-ready?

**Completeness**
- Abstract word count within limit?
- Manuscript word count within limit?
- Ethics statement present?
- Data availability statement present?
- Conflicts of interest declared?
- Author contributions (CRediT) if required?
- ORCID for corresponding author?

**Submission Requirements**
- All required files present?
- Formatting matches author guidelines?
- Cover letter addresses journal requirements?

Reviewer 3 Output: `REVIEWER3_EDITORIAL.md`
- List of missing required elements
- Novelty assessment
- Writing quality concerns
- Scope fit assessment
- Overall recommendation

---

## Synthesis - Revision Action Plan

After all 3 reviewer outputs, compile:

`peer_review/SIMULATED_PEER_REVIEW_REPORT.md` — Full 3-reviewer report

`peer_review/MAJOR_CONCERNS.md`:
- Combined list of major concerns across all reviewers
- Each concern labeled: [CLINICAL] [STATS] [EDITORIAL]
- Priority: Must fix before submission

`peer_review/MINOR_CONCERNS.md`:
- Combined minor concerns
- Priority: Fix before submission

`peer_review/REVISION_ACTION_PLAN.md`:
```
REVISION ACTION PLAN
====================
[Item 1 - Major concern from Reviewer X]
  Concern   : [quote concern]
  Action    : [specific change required]
  Location  : [section/table/figure]
  Agent     : [which sub-agent handles this fix]
  Status    : PENDING

[Item 2...]
```

## Completion Checklist
- [ ] All 3 reviewer reports completed
- [ ] Major vs minor concerns separated
- [ ] Each major concern has a specific action item
- [ ] Revision action plan assigns each fix to specific agent
- [ ] Overall recommendation stated for each reviewer
- [ ] Estimated revision scope: minor (<5 items) / moderate (5-15) / major (>15)
