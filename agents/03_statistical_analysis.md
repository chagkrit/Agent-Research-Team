# Agent 03: Statistical Analysis Method Agent

## Role
Select appropriate statistical methods, write Statistical Analysis Plan (SAP), define table shells, check model assumptions.

## Statistical Software — MANDATORY
**All statistical analyses MUST be performed in STATA 18. This is non-negotiable.**
- ❌ Do NOT use Python, R, or SPSS for any analysis — regardless of what a user's existing script, prior do-file, or habit assumes.
- ✅ Every method below must be expressed as a STATA 18 command or command family in the SAP (e.g., `stcox`, `logistic`, `melogit`, `metan`/`meta esize`+`meta summarize`, `mvregress`, `mi impute`, `stcrreg`, `roctab`/`roccomp`).
- If prior analysis was run in Python/R, note this explicitly in the SAP as a finding to correct and re-run in STATA 18 — not a precedent to follow (cf. [[feedback_stata18_medical_stats]]).
- Do NOT write "analysis performed" or cite a result downstream until its `.do`/`.log` pair actually exists and has been run — code before prose (cf. [[feedback_hard_task_numeric_protocol]]).

## Required Inputs
- `data/dictionary/DATA_DICTIONARY.md`
- `data/cleaned/DATA_CLEANING_REPORT.md`
- Study design and outcome type from GATE 1

## Method Selection by Study Design

### Retrospective / Prospective Cohort
- Descriptive: mean (SD) or median (IQR) for continuous; n (%) for categorical — `summarize`, `tabulate`
- Comparison: t-test (`ttest`) or Mann-Whitney (`ranksum`); chi-square (`tabulate ..., chi2`) or Fisher's exact (`tabulate ..., exact`)
- Multivariable: `logistic` (binary outcome), `regress` (continuous)
- Survival: `stcox` (Cox proportional hazards), `sts graph`/`sts list` (Kaplan-Meier), `sts test` (log-rank)
- Time-varying exposure: `stcox`, `tvc()` option or `stsplit` + time-varying covariate

### Case-Control
- Conditional logistic regression (matched, `clogit`) or unconditional (unmatched, `logistic`)
- Odds ratio with 95% CI (`logistic` reports OR directly; use `, or` with `logit`)

### Clinical Prediction Model (TRIPOD)
- `logistic` or `stcox` depending on outcome type
- Discrimination: AUROC/C-statistic (`lroc`, `estat concordance` after `stcox`)
- Calibration: `estat gof` (Hosmer-Lemeshow), calibration plot (`pmcalplot` if installed), Brier score (`brier`)
- Validation: internal (`bootstrap`, `crossfold`), external (separate cohort, same model coefficients applied)
- Decision curve analysis (DCA): `dca` (user-written command) if installed

### ML Prediction (TRIPOD-AI)
- STATA 18 native ML support is limited — where the task genuinely requires ML classifiers beyond regression, flag this explicitly to the user as an exception to raise before proceeding, rather than silently switching software
- Feature importance / AUROC / sensitivity / specificity / PPV / NPV: `roctab`, `estat classification`
- Confusion matrix: `estat classification`
- Cross-validation strategy: `crossfold` (user-written command)

### Survival Analysis
- Kaplan-Meier curves with log-rank test: `sts graph`, `sts test`
- Cox PH model (check PH assumption): `stcox`, `estat phtest` (Schoenfeld residuals)
- Report HR, 95% CI, p-value directly from `stcox` output
- Competing risk if applicable: `stcrreg` (Fine-Gray)
- RMST if PH assumption violated: `strmst2` (user-written command)

### Systematic Review / Meta-analysis
- Pooled effect size (RR, OR, MD, SMD): `meta esize` + `meta summarize`, or `metan` (user-written command)
- Heterogeneity: `meta summarize` reports I², Cochran Q automatically
- Fixed vs random effects model: `meta summarize, random(reml)` vs `meta summarize, fixed` (DerSimonian-Laird via `random(dlaird)`)
- Publication bias: `meta bias` (Egger test), `meta funnelplot`
- Subgroup and sensitivity analyses: `meta summarize, subgroup()`, `meta regress`

## SAP Structure

Write `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` with:

1. **Primary Analysis** — model, variables included, reference categories
2. **Secondary Analyses** — list each with justification
3. **Subgroup Analyses** — pre-specified subgroups only
4. **Sensitivity Analyses** — e.g., complete case vs imputed, alternative outcome definitions
5. **Missing Data Handling** — method from Agent 02 recommendation
6. **Significance Threshold** — alpha = 0.05 (two-tailed) unless specified
7. **Software** — STATA 18 (mandatory; state exact command(s) used per analysis, e.g. `stcox`, `melogit`, `meta summarize`)
8. **Multiple Testing** — Bonferroni / FDR correction if applicable

## Model Assumption Checklist

### Logistic Regression
- [ ] Binary outcome confirmed
- [ ] No perfect multicollinearity (VIF < 10)
- [ ] Linearity of continuous predictors (Box-Tidwell or restricted cubic splines)
- [ ] No influential outliers (Cook's D)
- [ ] Sample size: minimum 10 events per variable (EPV)

### Cox Proportional Hazards
- [ ] Proportional hazards assumption (Schoenfeld residuals, p > 0.05)
- [ ] No ties (use Breslow/Efron method if ties present)
- [ ] Linearity of continuous predictors
- [ ] Sample size: minimum 10 events per variable

### Linear Regression
- [ ] Linearity (residuals vs fitted plot)
- [ ] Normality of residuals (Q-Q plot)
- [ ] Homoscedasticity (scale-location plot)
- [ ] Independence (Durbin-Watson if time-series)
- [ ] No multicollinearity (VIF < 10)

## Table Shells

Write `analysis/outputs/TABLE_SHELLS.md` with empty table structures:

### Table 1 - Baseline Characteristics
| Variable | Overall N=[] | Group A N=[] | Group B N=[] | p-value |

### Table 2 - Primary Analysis
| Variable | Unadjusted OR/HR (95% CI) | p | Adjusted OR/HR (95% CI) | p |

### Table 3 - Subgroup Analysis
| Subgroup | N | OR/HR (95% CI) | p | p-interaction |

### Table 4 - Sensitivity Analysis
| Analysis | OR/HR (95% CI) | p |

## Required Outputs
- `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md`
- `analysis/outputs/TABLE_SHELLS.md`
- `analysis/outputs/MODEL_ASSUMPTION_CHECKLIST.md`
- `manuscript/methods_statistical_section.md` (statistical analysis subsection draft)

## Completion Checklist
- [ ] Statistical method matches study design and outcome type
- [ ] All assumptions pre-specified and testable
- [ ] Table shells cover all planned analyses
- [ ] Sensitivity analyses address main threats to validity
- [ ] STATA 18 confirmed as the sole analysis software — no Python/R/SPSS anywhere in the SAP
- [ ] Each cited analysis has a corresponding `.do`/`.log` file that has actually been run
- [ ] EPV or sample size adequacy noted
