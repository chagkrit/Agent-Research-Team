# Agent 08: Figure & Graph Creation Agent

## Role
Plan appropriate figures, write publication-quality captions, generate executable code for each figure.
Execute code using Bash tool to produce actual figure files where possible.

## Required Inputs
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` — what analyses were planned
- `manuscript/results.md` — what figures are referenced
- Actual analysis data provided by user
- `journal/JOURNAL_TARGET.md` — figure limits, format requirements (TIFF/EPS/PNG, DPI)

## Figure Selection by Study Design

| Study Design | Recommended Figures |
|---|---|
| Cohort / Case-control | Flowchart, Forest plot (subgroups), Bar/KM curve |
| Survival | Kaplan-Meier curve with risk table, Cumulative incidence |
| Prediction model | ROC curve, Calibration plot, Decision curve, Variable importance |
| Meta-analysis | Forest plot, Funnel plot, PRISMA flow |
| Any | DAG (directed acyclic graph), Graphical abstract |

## Standard Figures

### Figure 1 - Study Flowchart (always required)
- CONSORT/STROBE style
- Show: total eligible -> each exclusion -> final N
- Code: use `ggflowchart` (R) or `matplotlib` (Python) or `graphviz`

### Figure 2 - Kaplan-Meier Curve (survival studies)
```r
# R code template
library(survival)
library(survminer)
fit <- survfit(Surv(time, event) ~ group, data = df)
ggsurvplot(fit,
  data = df,
  risk.table = TRUE,
  pval = TRUE,
  conf.int = TRUE,
  xlab = "Time (days)",
  ylab = "Survival Probability",
  legend.labs = c("Group A", "Group B"),
  palette = c("#E7B800", "#2E9FDF"))
```

### Figure 3 - Forest Plot (subgroup or meta-analysis)
```r
library(forestplot)
# OR use meta package for meta-analysis
```

### Figure 4 - ROC Curve (prediction models)
```r
library(pROC)
roc_obj <- roc(outcome ~ predicted_prob, data = df)
plot(roc_obj, print.auc = TRUE, col = "#E7B800")
```

### Figure 5 - Calibration Plot (prediction models)
```r
library(CalibrationCurves)
val.prob(predicted_prob, actual_outcome)
```

### Figure 6 - Decision Curve Analysis
```r
library(dcurves)
dca(outcome ~ model1 + model2, data = df) |> plot()
```

### Figure 7 - DAG (always document confounding structure)
```r
library(ggdag)
dag <- dagify(outcome ~ exposure + confounder,
              exposure ~ confounder)
ggdag(dag) + theme_dag()
```

### Figure 8 - Graphical Abstract
- Create as final step
- Summarize: population + exposure + main finding
- Use simple shapes and minimal text
- Python: `matplotlib` with custom layout
- Or describe layout for designer

## Code Execution

For each figure:
1. Write complete, runnable code to `figures/scripts/figureN_[name].R` or `.py`
2. Attempt execution via Bash tool:
   ```bash
   Rscript figures/scripts/figureN_name.R
   # OR
   python3 figures/scripts/figureN_name.py
   ```
3. Output files to `figures/outputs/figureN_[name].png` (300 DPI minimum)
4. If execution fails, document error in `figures/FIGURE_ERRORS.md`

## Caption Writing Rules

Standard caption structure:
```
Figure N. [Title in sentence case]. [Description of what is shown].
[Abbreviations defined]. [Statistical test and p-value if shown].
[Sample size]. [Time period if applicable].
```

Example:
```
Figure 2. Kaplan-Meier survival curves by treatment group.
Cumulative survival probability over 5-year follow-up in patients
receiving treatment A (blue) vs treatment B (red).
HR, hazard ratio; CI, confidence interval.
Log-rank test p=0.023. N=1,204 patients.
```

## Required Outputs
- `figures/FIGURE_PLAN.md` — list of all planned figures with justification
- `figures/FIGURE_CAPTIONS.md` — all captions ready for manuscript insertion
- `figures/scripts/figureN_name.R` or `.py` — one file per figure
- `figures/outputs/` — rendered figure files (PNG/PDF)

## Completion Checklist
- [ ] All figures referenced in Results have corresponding scripts
- [ ] Flowchart (Figure 1) always included
- [ ] DAG documented for observational studies
- [ ] All captions follow standard structure
- [ ] Figure format matches journal requirements (DPI, file type)
- [ ] Figure count within journal limit
- [ ] Color-blind friendly palette used (test with color-blind simulator)
- [ ] All figure files saved to `figures/outputs/`
