# EC49FTQ reproducibility

Run with standard Python 3: `python EC49FTQ_SMOOTH_TP2_ATOM_VERIFY.py`

Independent local rational witness calculation was executed successfully before GitHub publication. The exact identities checked are recorded below and in the verifier, and the certificate records their rational results. This is analytic *external price prior* postprocessing; no native BRC optimizer was re-executed.

```text
M_early=23; M_late=93/4; z0=719/960
K_nonclipped=16/945
F_late=288/2741
F_early_smooth < 38880/450451
F_late - upper_bound = 23159808/1234686191 > 0
F_early_polynomial=160/5057
F_late-F_early_polynomial=1017856/13861237 > 0
Result: PASS (exact rational identities; smooth bump integral bounded analytically)
```

Scope: `AUTHOR_PROVED / EXACT_RATIONAL_BOUND_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED`. Inherited Bellman science is unchanged; the smooth integral itself is not numerically approximated.
