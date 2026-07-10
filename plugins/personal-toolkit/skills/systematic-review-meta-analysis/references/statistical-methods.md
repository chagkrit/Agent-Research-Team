# Pooling, heterogeneity, and bias — statistical reference for Steps 18–21

Read this before advising on whether/how to pool. **Execute everything here in Stata 18 via
`medical-research-pipeline:medical-stats`** — this file is for judgment calls, not for hand-rolling
the computation in another language.

## Fixed-effect (FE) vs. random-effects (RE) model

| | Fixed-effect (FE) | Random-effects (RE) |
|---|---|---|
| **Assumption** | All studies share one true effect size; observed variation is sampling error/chance | True effect size varies genuinely study to study |
| **Weighting** | By inverse of within-study variance — bigger studies dominate | Within-study variance *plus* between-study variance (tau²) — smaller studies get more relative weight than under FE |
| **What it estimates** | The single common effect | The average of a distribution of true effects |
| **When to use** | Strong evidence all studies are functionally identical (e.g. identical protocol multi-site trial) and inference is limited to the population studied | Default choice whenever included studies differ in design, population, or setting — which is nearly always true in observational-epidemiology meta-analyses |

**Do not choose the model based on the heterogeneity test result.** Cochran's Q has low power
with few or small studies, so a nonsignificant Q does not rule out real heterogeneity — the
model choice should reflect a judgment about whether one true effect is plausible, made before
looking at Q/I².

## Heterogeneity metrics

- **Cochran's Q (Chi²)** — tests the null hypothesis that all studies estimate the same effect.
  Low power with few studies; a nonsignificant result is not proof of homogeneity.
- **Higgins' I²** — percentage of total variation across studies attributable to heterogeneity
  rather than sampling error. Rough bands: <25% low, 25–50% moderate, >75% high — but I² itself
  has uncertainty and can have wide 95% CIs with few studies; always report the CI (Stata's
  `heterogi` module gives a non-central χ²-based CI, generally preferable to the test-based CI).
- **tau² (between-study variance)** — Ruecker et al. argue tau² is often a more appropriate
  basis than I² for deciding whether to pool, since I² is a *relative* measure (proportion of
  variance) while tau² is on the same scale as the effect estimate itself.

## Subgroup analysis and meta-regression (Step 21)

- Subgroup/stratified analysis: split by design, geography, population characteristics
  (age/sex/ethnicity/disease presence), publication date, or other effect modifiers defined at
  Step 1 — compare pooled estimates and tau² across strata.
- Meta-regression: conceptually a regression with study-level covariates predicting the effect
  size; generally only well-powered once **more than 10 studies** are included in the
  meta-analysis. Below that, treat subgroup findings as exploratory/hypothesis-generating.
- In Stata: `metan` for the base pairwise meta-analysis, `metareg` for meta-regression.

## Reporting units, and network meta-analysis

- Standardize units/scales across studies before pooling (e.g. blood glucose mmol/L vs mg/dL;
  currencies/inflation-adjustment for health-economics outcomes) — this is a data-cleaning step
  that happens before Step 18's database prep, not during analysis.
- If comparing more than two interventions with no direct head-to-head evidence between some of
  them, consider network meta-analysis (NMA, Stata `network` suite) instead of forcing pairwise
  comparisons — but NMA assumes no study/individual characteristic modifies relative treatment
  effects differently across comparisons (the "transitivity" assumption); flag this assumption
  explicitly rather than treating NMA as a drop-in replacement for pairwise meta-analysis.

## Publication bias (Step 22)

- **Funnel plot**: exposure effect (x-axis) vs. a measure of precision, typically standard error
  (y-axis). Visual asymmetry suggests missing studies, but asymmetry can also come from genuine
  heterogeneity, selective outcome reporting, or chance — not only publication bias.
- **Egger's test**: standard small-study-effects test; a modified version (Harbord) exists for
  binary-endpoint trials with unbalanced group sizes. Underpowered with a low number of studies.
- **Begg's/Kendall's test**: fewer assumptions than Egger's, but a nonsignificant result cannot
  rule out bias when the study count is small — treat it as an exploratory/complementary check,
  not a formal decisive test on its own.
- None of the three methods performs reliably when between-study heterogeneity is large — say
  so in the write-up rather than reporting a single p-value as conclusive.

## GRADE (Step 23)

- RCTs start as high-quality evidence; observational studies start as low-quality.
- **Downgrade** for: risk of bias, inconsistency (unexplained heterogeneity), indirectness,
  imprecision, or evidence of publication bias.
- **Upgrade** (observational studies only) for: large magnitude of effect, dose-response
  gradient, or when plausible residual confounding would move the estimate *toward* the null
  (i.e., the true effect is probably at least as strong as observed).
- Full worked criteria: https://gdt.gradepro.org/app/handbook/handbook.html
