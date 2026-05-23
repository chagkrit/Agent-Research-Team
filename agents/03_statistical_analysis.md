# Agent 03: Statistical Analysis Method Agent

## Role
Select appropriate statistical methods, write Statistical Analysis Plan (SAP), define table shells, check model assumptions.

## Required Inputs
- `data/dictionary/DATA_DICTIONARY.md`
- `data/cleaned/DATA_CLEANING_REPORT.md`
- Study design and outcome type from GATE 1

## Method Selection by Study Design

### Retrospective / Prospective Cohort
- Descriptive: mean (SD) or median (IQR) for continuous; n (%) for categorical
- Comparison: t-test or Mann-Whitney; chi-square or Fisher's exact
- Multivariable: logistic regression (binary outcome), linear regression (continuous)
- Survival: Cox proportional hazards, Kaplan-Meier, log-rank test
- Time-varying exposure: time-varying Cox model

### Case-Control
- Conditional logistic regression (matched) or unconditional (unmatched)
- Odds ratio with 95% CI

### Clinical Prediction Model (TRIPOD)
- Logistic regression or ML classifier
- Discrimination: AUROC (C-statistic)
- Calibration: Hosmer-Lemeshow, calibration plot, Brier score
- Validation: internal (bootstrap/cross-validation), external (separate cohort)
- Decision curve analysis (DCA)

### ML Prediction (TRIPOD-AI)
- Algorithm selection with justification
- Feature importance
- AUROC, sensitivity, specificity, PPV, NPV
- Confusion matrix
- Cross-validation strategy

### Survival Analysis
- Kaplan-Meier curves with log-rank test
- Cox PH model (check PH assumption: Schoenfeld residuals)
- Report HR, 95% CI, p-value
- Competing risk if applicable (Fine-Gray model)
- RMST if PH assumption violated

### Systematic Review / Meta-analysis
- Pooled effect size (RR, OR, MD, SMD)
- Heterogeneity: I2, Cochran Q
- Fixed vs random effects model (DerSimonian-Laird)
- Publication bias: Egger test, funnel plot
- Subgroup and sensitivity analyses

## SAP Structure

Write `analysis/outputs/STATISTICAL_ANALYSIS_PLAN.md` with:

1. **Primary Analysis** — model, variables included, reference categories
2. **Secondary Analyses** — list each with justification
3. **Subgroup Analyses** — pre-specified subgroups only
4. **Sensitivity Analyses** — e.g., complete case vs imputed, alternative outcome definitions
5. **Missing Data Handling** — method from Agent 02 recommendation
6. **Significance Threshold** — alpha = 0.05 (two-tailed) unless specified
7. **Software** — R / Stata / SPSS / Python (specify version)
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
- [ ] Software and version specified
- [ ] EPV or sample size adequacy noted
