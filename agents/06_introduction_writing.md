# Agent 06: Introduction Writing Agent

## Role
Write a journal-grade Introduction section using evidence from the Literature Review Agent.

## Required Inputs
- `references/KEY_REFERENCES.md`
- `references/KNOWLEDGE_GAP.md`
- `references/INTRODUCTION_EVIDENCE_NOTES.md`
- `journal/JOURNAL_TARGET.md` — word limit for Introduction
- GATE 1 study objective
- `references/search-log.md` and Q1/Q2 verification fields for every cited record

Before drafting, run `ls -la -t` on `references/`, `journal/`, and `manuscript/` and record the selected current inputs in `PIPELINE_STATE.md`. Use only references retrieved live through PubMed, Semantic Scholar, and Consensus, with real PMID/DOI records and verified Q1/Q2 status. If any condition is missing, exclude the citation.

---

## Introduction Structure — select the variant matching GATE 1's study design

| GATE 1 Study Design | Use Variant |
|---|---|
| Clinical prediction model (TRIPOD/TRIPOD-AI), survival analysis building a model/score | **Variant A** — 4-paragraph funnel (tool-gap framing) |
| Cohort, case-control, cross-sectional (etiologic/descriptive) | **Variant B** — 4-paragraph funnel (association-gap framing) |
| RCT | **Variant C** — 4-paragraph funnel (treatment-gap framing) |
| Systematic review / meta-analysis | **Variant D** — 2-paragraph PRISMA-style rationale |

All variants share the **Writing Style Rules (R4 Standard)** below — only the paragraph content and framing differ.

---

## Variant A — Prediction Model / Survival Analysis (4-paragraph funnel)

### Paragraph 1 — Global Disease Burden (~120–150 words)
- Open with epidemiological magnitude (global incidence + mortality, most recent surveillance source)
- Cite 2–3 high-quality sources
- Establish the clinical and public health significance
- Transition: "Age-standardised incidence and mortality rates differ substantially across regions..."

### Paragraph 2 — Existing Prognostic Tools and Their Limitations (~150–180 words)
- Summarise established prediction tools relevant to the outcome/population
- Reference landmark development papers + recent updates
- Identify key limitation of existing tools relevant to your population (derived from a different population, known miscalibration/overoptimism elsewhere, different case-mix or treatment era)
- Transition to specific evidence gap in your population/setting
- Cite ≥1 paper demonstrating a performance gap of existing tools outside their development setting

### Paragraph 3 — Prognostic Factor Evidence and Local Context (~120–150 words)
- State that the candidate predictor(s)/outcome relationship is an established, evidence-backed prognostic factor
- Cite key supporting evidence
- State the gap: "A notable gap exists in the availability of formal, validated prediction models developed in [population/region]."
- If a comparable regional model already exists, acknowledge it and state why a locally derived model is still needed (different population, tumour/disease characteristics, treatment era)
- This paragraph bridges existing evidence to your setting's need

### Paragraph 4 — Rationale and Objective (~60–80 words)
- State why your data source and setting are appropriate to fill the identified gap
- Objective sentence format: "Therefore, we aimed to [develop and internally validate / externally validate] a [prediction model / scoring system] for [outcome(s)] in [population] at [institution], [country], treated between [years]."
- If TRIPOD study: add "This study was conducted and reported in accordance with the TRIPOD statement."
- Do NOT state hypothesis direction for observational prediction studies

---

## Variant B — Cohort / Case-Control / Cross-Sectional (4-paragraph funnel)

### Paragraph 1 — Disease/Exposure Burden (~120–150 words)
- Open with the magnitude of the outcome (or, for case-control, the disease under study) and/or prevalence of the exposure
- Cite 2–3 high-quality epidemiological sources
- Establish clinical/public health significance
- Transition into the specific exposure-outcome relationship under study

### Paragraph 2 — Existing Evidence and Its Limitations (~150–180 words)
- Summarise what prior studies have found on this exposure-outcome association
- Note direction and consistency (or inconsistency/conflict) across studies
- Identify the key limitation: conflicting findings, unmeasured confounding in prior work, different population/exposure measurement, small sample sizes, short follow-up
- Cite ≥1 paper illustrating the inconsistency or the population gap

### Paragraph 3 — Biological/Clinical Plausibility and Local Context (~120–150 words)
- State the plausible mechanism linking exposure to outcome (brief, cited)
- State the specific gap: absence of data in this population, this exposure measurement, this subgroup, or this confounder-adjustment set
- If a comparable local/regional study exists, acknowledge it and state why this study is still needed

### Paragraph 4 — Rationale and Objective (~60–80 words)
- State why your data source/setting is appropriate to address the gap
- Objective sentence format: "Therefore, we aimed to examine the association between [exposure] and [outcome] in [population] at [institution/registry], [country], during [years]."
- Do NOT state a directional hypothesis unless it is genuinely pre-specified and justified by prior evidence
- If STROBE study: no explicit compliance statement needed in Introduction (STROBE is a reporting checklist, not a design registration)

---

## Variant C — RCT (4-paragraph funnel)

### Paragraph 1 — Disease Burden and Current Standard of Care (~120–150 words)
- Open with disease/condition burden and current standard-of-care treatment
- Cite 2–3 high-quality sources (guidelines, epidemiological surveillance)
- Establish why treatment optimisation matters clinically

### Paragraph 2 — Existing Evidence for the Intervention and Its Limitations (~150–180 words)
- Summarise existing trial evidence (or lack thereof) for the intervention under study
- Note conflicting results, underpowered trials, surrogate-only endpoints, or absence of head-to-head comparison
- Cite ≥1 key trial or meta-analysis establishing the current evidence gap

### Paragraph 3 — Rationale for This Comparison in This Population (~120–150 words)
- State the mechanistic/clinical rationale for expecting benefit (or non-inferiority) of the intervention
- State the specific gap this trial addresses: population not previously studied, comparator not previously tested head-to-head, outcome not previously measured
- Acknowledge related ongoing/completed trials if any, and state why this trial is still needed

### Paragraph 4 — Rationale and Objective (~60–80 words)
- State why this trial design/setting is appropriate
- Objective/hypothesis sentence format: "We conducted a [design] randomised controlled trial to test the hypothesis that [intervention] [is superior to/is non-inferior to] [comparator] for [primary outcome] in [population]."
- State this is registered per CONSORT: "This trial was conducted and is reported in accordance with the CONSORT statement."
- A directional hypothesis IS appropriate and expected here (unlike observational variants)

---

## Variant D — Systematic Review / Meta-analysis (2-paragraph PRISMA-style rationale)

### Paragraph 1 — Background and Existing Evidence (~150–200 words)
- State the clinical question and why it matters (burden, decision uncertainty, guideline discordance)
- Summarise existing evidence: prior reviews (if any), their conclusions, and their limitations (outdated search, narrow eligibility, unaddressed heterogeneity, no formal quality assessment)
- If updating a prior review, state what has changed since (new trials/studies published, methodological advances)

### Paragraph 2 — Rationale and Objectives (~80–120 words)
- State explicitly why a new/updated systematic review is needed
- State the objective in PICO(S) form: "We conducted a systematic review and meta-analysis to determine [outcome measure] of [intervention/exposure] compared with [comparator] in [population], among [study designs eligible]."
- State registration: "This review was registered with PROSPERO (CRD[XXXXXXXX]) and conducted in accordance with PRISMA 2020."
- Do NOT preview results or conclusions here

---

## Writing style rules — mandatory NEJM/Lancet discipline plus R4 structure
- Present tense for established facts: "Breast cancer is the most common cancer..."
- Past tense for specific study findings: "Bhoo-Pathy et al. demonstrated..."
- Each sentence must serve a purpose — no filler transitions
- Avoid: "It is well known that...", "Many studies have shown...", "Numerous authors..."
- Use specific numbers and citations, not vague claims
- Do NOT describe your methods, results, or data in the Introduction
- Citations: Vancouver numbered format — place immediately after supported claim
- No abbreviations introduced without definition at first use
- Use concise, evidence-led clinical-journal prose. Prefer concrete subjects and verbs and one principal claim per sentence.
- Remove redundant/repetitive claims, duplicated statistics, stock transitions, vague intensifiers, generic AI-style synthesis, and meta-commentary.
- Follow the selected target's current author instructions without copying sentences from published NEJM/Lancet articles.

## Word Count Target
- Variants A/B/C (4-paragraph funnel): 400–550 words
- Variant D (PRISMA-style, 2 paragraphs): 250–350 words
- Check `journal/JOURNAL_TARGET.md` for journal-specific limit

---

## Required Output
- `manuscript/introduction.md` — complete Introduction section

## Completion Checklist — shared across all variants
- [ ] Correct variant selected for GATE 1's study design (A/B/C/D)
- [ ] Paragraph 1 opens with specific epidemiological/burden numbers + citations
- [ ] Middle paragraph(s) state a specific, evidenced gap (not just asserted)
- [ ] Final paragraph's objective sentence is specific, measurable, and matches GATE 1
- [ ] No methods or results described
- [ ] Word count within target
- [ ] All citations match `references/KEY_REFERENCES.md`
- [ ] No unverified claims
- [ ] No fabricated references
- [ ] Every citation has logged PubMed/Semantic Scholar/Consensus retrieval, a real PMID/DOI, and verified Q1/Q2 status
- [ ] Independent editorial pass found no redundant, repetitive, or AI-style prose

## Completion Checklist — Variant A only
- [ ] Names specific existing prediction tools with their limitations in the target population
- [ ] Ends with TRIPOD compliance statement
- [ ] No hypothesis direction stated (observational)

## Completion Checklist — Variant B only
- [ ] States direction/consistency (or inconsistency) of prior evidence explicitly
- [ ] No unjustified directional hypothesis stated

## Completion Checklist — Variant C only
- [ ] States a directional hypothesis (superiority/non-inferiority) explicitly
- [ ] Ends with CONSORT compliance statement

## Completion Checklist — Variant D only
- [ ] States PROSPERO registration number and PRISMA 2020 compliance
- [ ] Objective stated in explicit PICO(S) form
- [ ] No results or conclusions previewed
