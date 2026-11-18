# R5: sharp exponential growth exponent for radius-two repair advice

2026-11-15. Follows `BLIND_RECOURSE_AND_LIBRARY_COMPLEXITY_THEOREM.md` in the same directory and frozen source `435e77af0d180eac32bd1f9c4c464bc4010b7551`. AUTHOR_PROVED / EXACT_CORE_CHECKED / NOT_REVIEWED.

For `m>=1`, define `kappa_a(m,2)` and `kappa_ab(m,2)` as the least number of precommitted old optimal center configurations such that every a-only or jointly closed new optimal center configuration can be repaired within two replacements using a configuration in the library.

## Corollary: exact exponential rate (without asserting an exact finite-m cardinality)

For each `t in {a,ab}` and `l=m-1`,

```
ceil(2^l / (1+l+l(l-1)/2)) <= kappa_t(m,2) <= 2^(l+1).
```

The right-hand side improves the trivial full-old-family bound `5*2^l`.

Consequently both limits exist and are **exactly** one:

```
lim_{m->infinity} log_2(kappa_a(m,2))/(m-1) = 1,
lim_{m->infinity} log_2(kappa_ab(m,2))/(m-1) = 1.
```

Equivalently, the size needed to preserve the constant adaptive repair radius 2 is `2^(m-o(m))`.

**Proof.** The lower bound is the Hamming ball covering argument in Theorem B of the preceding file; the radius-two ball on the l-dimensional binary suffix cube has size `1+l+l(l-1)/2` (the formula also works at l=0,1). For the upper bound, direct complete seven-event core enumeration gives `max_{C in G_t} min_{D in {0125,0135}} |C\D| <=2` for both t=a and ab. For each suffix word H choose the two old configurations `0125 union H` and `0135 union H`. Every new `C union H` is within two swaps of one of them, so the total library size is at most `2*2^l`. Take binary logarithms, divide by l, and apply the squeeze theorem as l increases. QED.

This identifies a precise information bottleneck: the **nearest-repair function** can be represented by a fixed seven-event core, while a precomputed library supporting that same radius for arbitrary future suffix observations has an unavoidable exponential count. This is a change in the declared observer/quantifier order, not a contradiction.

Checks: core pair coverage was independently evaluated against all 12 a-only and all 17 jointly closed seven-event optimal sets using exact integer center-index swap distances; the finite minimum library sizes for m=1..3 are recorded in `RESULTS_SUMMARY.json`. The all-m theorem uses the earlier all-m optimizer-family product lemma, rather than relying on finite sample extrapolation.

Remaining problem: determine exact finite-m `kappa_a(m,2)` and `kappa_ab(m,2)`, and whether a shared optimal suffix code construction approaches the Hamming-ball lower bound polynomial factor.
