---
name: systematic-review-meta-analysis
description: Guides the full design, conduct, and publication of a systematic review and/or meta-analysis in medical research, following the peer-reviewed 24-step methodology (Muka et al. 2020, Eur J Epidemiol). Use this whenever the user is starting, planning, or working through any stage of a systematic review or meta-analysis — defining a research question with PICO(S)/PECO, writing or registering a protocol (PROSPERO/Cochrane), building a multi-database search strategy (MEDLINE, Embase, Web of Science, Google Scholar, Cochrane), deduplication, title/abstract or full-text screening, drawing a PRISMA flow diagram, designing a data extraction form, assessing risk of bias (RoB 2, Newcastle-Ottawa, QUADAS-2, QUIPS, PROBAST), deciding whether to pool data, choosing fixed- vs random-effects models, exploring heterogeneity or running subgroup/meta-regression analyses, checking publication bias (funnel plot, Egger's/Begg's test), grading evidence quality with GRADE, or preparing the manuscript/PRISMA checklist for submission. Trigger even when the user doesn't name a specific step — phrases like "meta-analysis", "systematic review", "SR/MA", "PRISMA", "PROSPERO", "forest plot", "pool the studies", "risk of bias", "heterogeneity", "I2", "publication bias", "search strategy for a review", or "ทำ systematic review", "ทำ meta-analysis", "ทบทวนวรรณกรรมเชิงระบบ" are all strong signals to use this skill.
---

# Systematic Review & Meta-Analysis (24-Step Guide)

## Why this exists

Not all systematic reviews are truly systematic — quality varies wildly, and most guidance
(PRISMA, MOOSE) tells you how to *report* a review, not how to actually *run* one end to end.
This skill operationalizes the 24-step process from Muka T, Glisic M, Milic J, et al.
"A 24-step guide on how to design, conduct, and successfully publish a systematic review and
meta-analysis in medical research." *Eur J Epidemiol.* 2020;35:49–60.
(Source PDF: `/Users/chagkrit/Downloads/Step_to_MA.pdf` — keep as the canonical reference if the
user wants to re-check exact wording.)

Use the 24 steps as the skeleton for the whole project, not a rigid script. Figure out which
step the user is actually on, do that step properly, produce the concrete deliverable it calls
for, and keep the rest of the roadmap visible so nothing gets skipped later (screening without
a written protocol, or pooling without a heterogeneity check, are the errors that get caught at
peer review and cost months).

## Division of labor: this skill vs. the Stata pipeline

**This skill owns steps 1–17 and 22–24** (the design, search, screening, extraction, and
reporting machinery). **Steps 18–21 (database prep, descriptive synthesis, pooling, and
heterogeneity exploration) are statistical analysis** — hand those off to
`medical-research-pipeline:medical-stats` and run them in **Stata 18**, never Python or R.
[[feedback_stata18_medical_stats]] This is a standing rule for this user's medical research
work, not a per-project choice — do not improvise with `metafor` in R or `statsmodels` in
Python even if it would be faster to prototype.

If the user is deep in a project already tracked in memory (e.g. the ICG SLNB meta-analysis,
[[project_icg_slnb_metaanalysis]]), check that memory first — don't restart steps that are
already done.

## The 24 steps

### Phase 1 — Design (Steps 1–6)

1. **Define the research question.** Use PICO(S) for intervention questions, PECO for
   exposure/etiology questions (most relevant for observational epidemiology), PEO/SPICE for
   qualitative questions, SPIDER for mixed-methods. Write out population, exposure/intervention,
   comparator, outcome, and (if relevant) study designs explicitly — this drives the search
   strategy and inclusion criteria downstream. Check PROSPERO and recent reviews on the same
   topic first: an existing review isn't a blocker if this one adds new studies, closes a gap,
   or takes a quantitative angle a prior narrative review lacked.
2. **Establish the team.** At minimum: someone to build/run the search (ideally a librarian or
   information specialist), two independent screeners, someone who can run the statistics. A
   third, senior reviewer resolves disagreements. Flag to the user if their team is
   all-clinical-expert with no methods/stats coverage — reviews skew toward lower quality when
   over-dominated by one type of expertise.
3. **Define the search strategy.** Minimum four databases: Embase, MEDLINE, Web of Science, and
   Google Scholar (cap at ~200–1000 refs from Google Scholar — it doesn't support exhaustive
   retrieval). Add Cochrane CENTRAL for intervention/RCT questions, and PsycINFO/CINAHL for
   psychiatry, psychology, nursing, or qualitative-research components (CINAHL indexes
   qualitative work better than PubMed). Draft the actual boolean search string per database —
   don't just describe the concept.
4. **Define selection criteria (inclusion/exclusion).** Derive from the PICO(S)/PECO: study
   design, publication date/language, population characteristics, exposure/outcome definitions,
   and methodological requirements (e.g., adjustment for confounders). Turn this into a written
   screening checklist so both reviewers apply the same rule.
5. **Design the data collection form.** Fields should cover: study identification (authors,
   year, funding/COI), population (age, sex, ethnicity, setting), exposure/intervention
   (definition, measurement, dose), outcomes, methods (analysis type, adjustment set), and
   results (effect measure + precision, stratified estimates, agreement with other studies).
   Pilot it on ~5 studies before finalizing — this always surfaces fields that are ambiguous or
   missing.
6. **Write the protocol and register it.** Protocol = research question, aims, design,
   inclusion/exclusion, search strategy, and analysis plan, circulated to co-authors/experts for
   feedback before locking it. Register on PROSPERO (health/social care) or via Cochrane
   (intervention reviews) before starting the search — this is what lets a peer reviewer trust
   the review wasn't outcome-switched after the fact.

### Phase 2 — Search & screening (Steps 7–12)

7. **Run the search strategy in every database** identified in step 3. Each database needs its
   own syntax — a PubMed string does not transfer directly to Embase or Web of Science.
8. **Collect all references and abstracts into a single file** using EndNote, Covidence,
   DistillerSR, or Rayyan. EndNote is preferred if step 9's deduplication method will be used.
9. **Eliminate duplicates.** De-duplication is genuinely error-prone by hand across
   heterogeneous export formats — use a structured method (e.g. the EndNote-based approach in
   Bramer et al. 2016, *J Med Libr Assoc*), not a naive title-match.
10. **Two independent reviewers screen title/abstract.** Screen title+abstract together (not
    title-then-abstract sequentially); if a record has only a title with no abstract, include it
    forward rather than excluding on missing information. Rayyan/Covidence/DistillerSR all
    support this; avoid doing it in a spreadsheet for anything beyond a trivial reference count.
11. **Collect, compare, and select for retrieval.** Where the two reviewers agree, the
    reference moves to full-text retrieval. Where they disagree, resolve by discussion or a
    third senior reviewer — don't silently let one reviewer's screen win.
12. **Retrieve full text and apply selection criteria**, again independently by both reviewers,
    with the third reviewer resolving disagreement. Missing full texts: try Google Scholar,
    ResearchGate, direct author contact, or interlibrary loan — don't drop a study just because
    the PDF wasn't immediately available.

### Phase 3 — Assembly (Steps 13–17)

13. **Contact experts** (authors of included studies) for unpublished data, missing-outcome
    recalculation, or a standardized covariate set for pooling. Screen anything they suggest
    through steps 9–13 like any other candidate reference.
14. **Search for additional references** via forward citation search (who cited the included
    studies — Scopus works well) and backward search (reference lists of included studies and
    prior reviews on the topic).
15. **Make the final selection list and draw the PRISMA flow chart** — number of records
    identified per source, number excluded at each stage with reasons and counts, and the final
    included count. This diagram is a mandatory attachment at submission.
16. **Apply the data collection form, in pairs.** Two independent reviewers extract into the
    step-5 form. Keep abbreviations, units, and definitions consistent across extractors — this
    is where silent errors creep into a meta-analysis (mismatched units are a common one).
17. **Evaluate study quality and risk of bias**, independently, by two reviewers. Match the tool
    to study design — see `references/risk-of-bias-tools.md` for RoB 2 (RCTs), Newcastle-Ottawa
    (cohort/case-control), ROBINS-I (nonrandomized interventions), QUADAS-2 (diagnostic
    accuracy), QUIPS (prognostic factor studies), and PROBAST (prediction models).

### Phase 4 — Synthesis & analysis (Steps 18–21) — hand off to Stata

18. **Prepare the database for analysis** — collate the extraction forms into one dataset.
19. **Conduct descriptive synthesis** regardless of whether pooling happens: report the
    PRISMA-style screening funnel, then study characteristics, populations, exposures/outcomes,
    and quality, in text and a summary table.
20. **Decide whether to meta-analyze.** Pooling requires comparable estimates, definitions, and
    coding across studies — not just the same broad topic. Note explicitly that combining
    conceptually different study designs (e.g. RCT mean-change outcomes vs. observational
    risk-ratio outcomes) is usually a "report both, don't force one pooled number" situation
    rather than a blocker to the review.
21. **Explore heterogeneity** via subgroup analysis (by study design, geography, population
    characteristics, publication date) and meta-regression (worthwhile once >10 studies are
    included). Choose fixed- vs. random-effects **based on clinical/methodological judgment
    about whether a single true effect is plausible, not based on the heterogeneity test result**
    — I²/Cochran's Q can look nonsignificant purely from low power with few or small studies.
    See `references/statistical-methods.md` for the FE-vs-RE decision table and heterogeneity
    metrics (I², tau², Cochran's Q).

**Do all of steps 18–21 with `medical-research-pipeline:medical-stats` in Stata 18** —
`metan` for standard pairwise meta-analysis, `metareg` for meta-regression, `network` for
network meta-analysis when comparing >2 interventions with no head-to-head trials.
[[feedback_metan_nointeger_rr_not_or]] applies if `metan ... nointeger` comes up — it produces a
log-RR, not a log-OR; for a true OR use generic inverse-variance with pre-computed log(OR)/SE.

### Phase 5 — Quality, bias, and publication (Steps 22–24)

22. **Check reporting/publication bias.** Funnel plot (visual asymmetry check) plus Egger's test
    (has power issues with cohort studies of very unequal group sizes) and/or Begg's/Kendall's
    test (fewer assumptions, but underpowered with few studies). None of the three tests is
    reliable when between-study heterogeneity is large — say so rather than reporting a single
    p-value as decisive. Publication bias must be reported and discussed if present, but it does
    not by itself block publication.
23. **Check the quality of the evidence with GRADE** — independently by two reviewers, third to
    resolve disagreement. RCTs start high quality, observational studies start low; both can be
    downgraded (risk of bias, inconsistency, indirectness, imprecision, publication bias) or, for
    observational studies, upgraded (large effect, dose-response gradient, plausible confounding
    would only move the estimate toward the null).
24. **Update, report, and submit.** If more than 6–12 months have passed since the search was
    run, rerun it before submission to catch newly published studies. Attach a PRISMA (most
    review types) or MOOSE (meta-analysis of observational studies) checklist and flow diagram —
    reviewers and editors expect this as a submission requirement, not an optional extra. Hand
    off to `medical-research-pipeline:submission-package` for the checklist file, cover letter,
    and other submission artifacts, and to `medical-research-pipeline:journal-strategy` for
    target-journal selection if that hasn't happened yet.

## Working with the user on this

- **Ask which step they're on** if it isn't obvious from context, rather than assuming step 1.
  A returning user picking up a stalled project is the common case, not a cold start.
- **Produce the actual artifact for the step**, not just a description of what the step
  involves: a filled PICO(S)/PECO table, a drafted protocol document, real boolean search
  strings per database, a populated risk-of-bias table, a PRISMA flow diagram (as a Mermaid
  diagram or numbered figure, ready to drop into the manuscript), a GRADE summary-of-findings
  table.
- **Surface skipped steps.** If someone asks to "just pool the studies" without a written
  protocol, registered PROSPERO entry, or documented risk-of-bias assessment, flag what's
  missing — those are exactly the gaps a Q1-journal reviewer will catch, and they're much
  cheaper to fix before the search than after.
- **Don't force a pooled estimate** when studies are too heterogeneous in design, exposure
  definition, or outcome scale — a well-justified "descriptive synthesis only" (step 19, skip
  step 20) is a legitimate, common outcome, not a failure.

## Reference files

- `references/risk-of-bias-tools.md` — which tool for which study design, and the
  domains/scoring each one evaluates (RoB 2, Newcastle-Ottawa, ROBINS-I, QUADAS-2, QUIPS,
  PROBAST).
- `references/statistical-methods.md` — FE vs. RE model decision table, heterogeneity metrics
  (I², tau², Cochran's Q) and their limitations, and when meta-regression/subgroup analysis is
  warranted. Read this before advising on step 20–21, then execute in Stata via
  `medical-research-pipeline:medical-stats`.
