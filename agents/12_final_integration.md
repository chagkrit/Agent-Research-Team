# Agent 12: Final Manuscript Integration Agent

## Role
Compile all sections into a complete, consistent manuscript. Run final consistency checks. Prepare submission package.

## Required Inputs
- `manuscript/introduction.md`
- `manuscript/methods.md`
- `manuscript/results.md`
- `manuscript/discussion.md`
- `manuscript/conclusion.md`
- `figures/FIGURE_CAPTIONS.md`
- `references/KEY_REFERENCES.md`
- `journal/JOURNAL_TARGET.md`
- `peer_review/REVISION_ACTION_PLAN.md` (if peer review simulation done)
- `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md`

## Step 1 - Compile Full Draft

Assemble in order:
1. Title page
2. Abstract
3. Keywords
4. Introduction
5. Methods
6. Results
7. Discussion (including Conclusion)
8. Acknowledgements placeholder
9. Conflicts of Interest statement
10. Funding statement
11. Data Availability statement
12. Author Contributions (CRediT taxonomy)
13. References
14. Table legends
15. Figure legends

Output: `manuscript/full_draft.md`

## Step 2 - Consistency Audit

### Number Consistency Check
Extract all N values and verify identical across:
- [ ] Abstract: N = ___
- [ ] Methods (cohort size): N = ___
- [ ] Results (Table 1): N = ___
- [ ] Results (primary analysis table): N = ___
- [ ] Figure 1 (flowchart final N): N = ___
All must match.

### Effect Estimate Consistency
For primary outcome, verify identical:
- [ ] Abstract results: OR/HR = ___ (95% CI ___-___)
- [ ] Results text: OR/HR = ___ (95% CI ___-___)
- [ ] Results table: OR/HR = ___ (95% CI ___-___)

### Table Reference Check
For each table mentioned in text:
- [ ] Table 1 referenced? Text location: ___
- [ ] Table 2 referenced? Text location: ___
- [ ] All referenced tables exist as actual tables?
- [ ] No table exists without a text reference?

### Figure Reference Check
- [ ] Figure 1 (flowchart) referenced in Methods?
- [ ] All figures referenced in Results or Methods?
- [ ] Figure count within journal limit?
- [ ] All figure files exist in `figures/outputs/`?

### Abstract Accuracy Check
- [ ] Background matches Introduction gap statement
- [ ] Methods matches actual methods (design, N, statistical approach)
- [ ] Results: primary outcome numbers match Results section exactly
- [ ] Conclusion matches Discussion conclusion

### Reference Integrity Check
- [ ] All in-text citations have corresponding reference list entry
- [ ] No reference list entry is uncited in text
- [ ] All PMIDs verified (spot check 5 random references)
- [ ] Reference format matches target journal

## Step 3 - Reporting Guideline Final Check

Open `analysis/outputs/REPORTING_GUIDELINE_CHECKLIST.md`
Verify each item: marked complete with manuscript location.
Flag any incomplete items.

## Step 4 - Word Count Final

Count each section:
| Section | Words | Journal Limit | Status |
|---|---|---|---|
| Abstract | | | |
| Introduction | | | |
| Methods | | | |
| Results | | | |
| Discussion | | | |
| Total | | | |

If over limit: identify lowest-priority paragraphs to trim.

## Step 5 - Submission Package Assembly

Create `submission/` folder with:
- `submission/MANUSCRIPT_MAIN.md` — main text (no figures embedded)
- `submission/TITLE_PAGE.md` — title, authors, affiliations, corresponding author
- `submission/ABSTRACT.md` — structured abstract standalone
- `submission/COVER_LETTER.md` — copy from `journal/COVER_LETTER_DRAFT.md`
- `submission/TABLES/` — each table as separate file
- `submission/FIGURES/` — copies of all figure files from `figures/outputs/`
- `submission/SUPPLEMENTARY/` — supplementary tables/figures if any
- `submission/REPORTING_CHECKLIST.pdf` — completed guideline checklist
- `submission/FINAL_CHECKLIST.md` — checklist below

## Final Submission Checklist

```
FINAL SUBMISSION CHECKLIST
============================

Manuscript
- [ ] Title within character limit
- [ ] Abstract within word limit and correct format
- [ ] Keywords: 3-6 MeSH terms
- [ ] Main text within word limit
- [ ] All sections present: Intro/Methods/Results/Discussion
- [ ] Ethics statement included
- [ ] Acknowledgements complete

Data & Statistics
- [ ] All N consistent throughout
- [ ] All effect estimates consistent
- [ ] CIs reported for all main estimates
- [ ] P-values reported correctly
- [ ] Reporting guideline checklist complete

Tables
- [ ] Table count within journal limit
- [ ] All tables titled and numbered
- [ ] All tables referenced in text
- [ ] Table footnotes define all abbreviations

Figures
- [ ] Figure count within journal limit
- [ ] All figures titled and numbered
- [ ] All figures referenced in text
- [ ] Figure resolution >= 300 DPI
- [ ] Figure format correct (TIFF/EPS/PNG per journal)
- [ ] Figure 1 = cohort flowchart

References
- [ ] Format matches journal style
- [ ] Count within journal limit
- [ ] All in-text citations have list entry
- [ ] All list entries cited in text

Administrative
- [ ] Cover letter complete
- [ ] Conflicts of interest declared
- [ ] Funding declared
- [ ] Data availability statement
- [ ] Author contributions (CRediT)
- [ ] ORCID for corresponding author
- [ ] All authors approved submission
```

## Required Outputs
- `manuscript/full_draft.md`
- `manuscript/ABSTRACT_FINAL.md`
- `manuscript/TITLE_KEYWORDS.md`
- `submission/` — complete submission package
- `submission/FINAL_CHECKLIST.md`

## Completion Checklist
- [ ] All sections compiled without gaps
- [ ] All consistency checks passed
- [ ] Reporting guideline 100% complete
- [ ] Submission package organized per journal requirements
- [ ] Final checklist signed off
- [ ] PIPELINE_STATE.md updated: all steps DONE
