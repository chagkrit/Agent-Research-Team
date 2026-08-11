# Agent 08: Figure & Graph Creation Agent

## Role
Plan appropriate figures, write publication-quality captions, and generate reproducible figure code.

## Required inputs

- `data/cleaned/analytic_cohort.dta`
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md`
- `analysis/results-ledger.csv`
- Source `analysis/scripts/*.do` and successful `analysis/logs/*.log`
- `manuscript/results.md`
- `journal/JOURNAL_TARGET.md`

## Live-state and provenance gate

Before starting, run `ls -la -t` on the data, analysis, manuscript, figure, and supplementary directories; record the current inputs in `PIPELINE_STATE.md`.

Generate every data-derived plot in STATA 18 from the declared analytic `.dta`. Each figure must have a numbered `.do` file and successful matching `.log`. Do not use R or Python to calculate, transform, or plot statistical results. A non-statistical flowchart, DAG, or graphical abstract may use a design tool only if every displayed number is copied from the verified results ledger and no calculation occurs outside STATA.

## Figure selection by study design

| Study Design | Recommended Figures |
|---|---|
| Cohort / Case-control | Flowchart, forest plot, bar/KM curve |
| Survival | Kaplan-Meier curve with risk table, cumulative incidence |
| Prediction model | ROC curve, calibration plot, decision curve |
| Meta-analysis | Forest plot, funnel plot, PRISMA flow |
| Any | DAG, graphical abstract |

## Standard figures

### Figure 1 — Study flowchart

- Use CONSORT/STROBE structure and ledger-verified counts.
- Prefer STATA 18 `twoway` text/shape annotations. If a design tool is used for layout only, retain a plain-text source table and independently verify every count.

### Figure 2 — Kaplan-Meier curve

```stata
version 18
use "data/cleaned/analytic_cohort.dta", clear
stset time_days, failure(event == 1) id(patient_id)
sts graph, by(group) risktable ci ///
    xtitle("Time (days)") ytitle("Survival probability") ///
    graphregion(color(white)) name(fig2_km, replace)
graph export "figures/outputs/figure2_km.png", width(2400) replace
```

### Figure 3 — Forest plot

Use estimates generated in the same STATA `.do` file. Record the installed version of any user-written command such as `coefplot`; if the required command is unavailable, stop and report the missing capability rather than switching software.

### Figure 4 — ROC curve

```stata
version 18
use "data/cleaned/analytic_cohort.dta", clear
logistic outcome predictor1 predictor2
lroc, name(fig4_roc, replace)
graph export "figures/outputs/figure4_roc.png", width(2400) replace
```

### Figure 5 — Calibration plot

Use a pre-specified, validated STATA 18 calibration workflow. Record every command and any user-written ado version in the figure log. Do not substitute a different engine.

### Figure 6 — Decision curve analysis

Use a validated STATA decision-curve command only if installed and recorded. Otherwise stop and report the missing capability.

### Figure 7 — DAG

A DAG is a conceptual diagram, not a statistical calculation. A design tool may be used, but save the variable/edge specification as plain text and independently review it. Do not embed unverified numeric results.

### Figure 8 — Graphical abstract

Create after the manuscript numbers are verified. Use simple shapes and minimal text. Copy every displayed number from `analysis/results-ledger.csv`.

## Code execution

For each data-derived figure:

1. Write complete STATA 18 code to `figures/scripts/figureN_name.do`.
2. Open and save `analysis/logs/figureN_name.log`.
3. Load the declared analytic `.dta`; do not use a manually edited derivative.
4. Export `figures/outputs/figureN_name.png` at 300 DPI or the target journal's required format.
5. If execution fails, record the error in `figures/FIGURE_ERRORS.md`; do not create a substitute figure in another statistical package.
6. Copy displayed numbers from the results ledger and run the whole-project numeric sweep.
7. Leave corrected values `corrected_pending_independent_recheck` until Agent 11 or a later fresh-context pass verifies them.

## Caption writing rules

Use sentence case and concise NEJM/Lancet clinical-journal discipline. Define abbreviations and state the population, time frame, analysis, and uncertainty needed to interpret the figure. Do not repeat the full Results paragraph or use AI-style filler.

```text
Figure N. [Sentence-case title]. [What is shown and in whom].
[Analysis/uncertainty]. [Abbreviations].
```

## Required outputs

- `figures/FIGURE_PLAN.md`
- `figures/FIGURE_CAPTIONS.md`
- `figures/scripts/figureN_name.do`
- `analysis/logs/figureN_name.log`
- `figures/outputs/`

## Completion checklist

- [ ] All referenced figures exist and match the journal limit/format.
- [ ] STATA 18 was the sole engine for every data-derived figure.
- [ ] Each data-derived figure has a current `.do`, successful `.log`, and declared `.dta`.
- [ ] Every displayed number traces to `analysis/results-ledger.csv`.
- [ ] Whole-project numeric sweep passed after the latest change.
- [ ] Latest corrections passed a later independent re-check.
- [ ] Captions are concise, nonredundant, and free of AI-style filler.
- [ ] Color and line styles are accessible and remain interpretable in grayscale.
