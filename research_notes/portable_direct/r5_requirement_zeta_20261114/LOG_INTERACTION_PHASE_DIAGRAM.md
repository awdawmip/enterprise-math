# R5 — exact finite log-interaction phase diagram and Bernoulli optimizer abundance

Date: 2026-11-14. Status: **AUTHOR_DERIVED / EXACT_INTEGER_CHECKED / NOT_REVIEWED**.
Frozen science: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Observer: derived radius-2 one-dimensional integer-event model, indexed centers. This note extends the optimizer **count** observer, not the native X6 state.

## Exact two-cut count representation

Reuse the established principal-filter result and the five-mask exact count certificate at PR #2412, commit `69b0fa35b6c0f191190c66f8d857a175b289370c`. For every original 28-gap closure mask and budget `293 <= K <= 314`, the optimizer count depends only on indicators `X = 1_{15 closed}`, `Y = 1_{17 closed}`:

```
N_K(X,Y) = a + b X + c Y + d XY
N00 = a, N10 = a+b, N01 = a+c, N11 = a+b+c+d.
```

All four coefficients are nonnegative integers; all four counts are positive in this budget range. Exactly the same algebra works for any Boolean optimizer-family with four nonnegative prerequisite cohorts.

## Theorem A — additive complementarity does not determine multiplicative complementarity

The discrete mixed difference of `N` is `N11-N10-N01+N00=d >= 0`, so counts are supermodular (strictly for K=294..313).

For the log-cardinality observer, define the finite interaction
```
L_K = log N11 + log N00 - log N10 - log N01
    = log[ N11*N00 / (N10*N01) ].
```

Its sign is **exactly** the sign of the integer determinant
```
D_K = a*d - b*c.
```
Indeed, `N11*N00 - N10*N01 = a*d-b*c`. Positivity of all counts makes the logarithm strictly order preserving. No floating-point logarithms are needed to certify the sign.

Using the exact 24-row JSON at this path, `D_K` is:

- **Positive exactly at K = 299, 300, 301.**
- **Negative at K = 293..298 and K = 302..314.**
- **Zero at K = 292 and K = 315.** The previously proved optimizer-family invariance extends zero to all 315<=K<=954.

Therefore two simultaneously useful cut variables can have an additive positive interaction while their **relative** optimizer-cardinality interaction is negative, with a narrow three-budget positive window. The only signs claimed here are for the **frozen 954-event R5** and the given integer-center observer.

Exact integer crossover witnesses:
```
D_298 = -1076497326375075298857659506959110681944917740001621115404288000
D_299 =  6318107756242913535087549531738362202519376369239425089850572800
D_301 =  1031647069261457610452470419175449149063555367684265525290152755200
D_302 = -4583113930077162997476534526313635690686196046485536133081359974400
```

## Theorem B — exact random-closure moments for optimizer abundance

Let the two relevant cut closures be independent Bernoulli(p) variables X,Y, 0<=p<=1, and let `Z_K=N_K(X,Y)`. Other independent cut indicators can be present: for K>=292 they do not change this observer. Then

```
E[Z_K] = a+(b+c)p+d*p^2.
Var(Z_K) = p(1-p) [ (b+d*p)^2 + (c+d*p)^2 ]
           + d^2*p^2*(1-p)^2.
Cov(Z_K,X) = p(1-p)*(b+d*p).
Cov(Z_K,Y) = p(1-p)*(c+d*p).
```

Proof: with `U=X-p,V=Y-p`, the centered decomposition is
```
Z_K-E[Z_K] = (b+dp)U + (c+dp)V + dUV.
```
The three summands are pairwise orthogonal by independence and centering. Using `E[U^2]=E[V^2]=p(1-p)` gives the variance and covariances. This is an **exact polynomial identity** at every real p in [0,1], with exact integer coefficients; no stochastic simulation is required.

If an optimal indexed center set is chosen uniformly from the all-closed optimizer family and closure bits are sampled independently, its retention probability is exactly
```
P(retained) = [a+(b+c)p+dp^2]/[a+b+c+d].
```
This distinguishes the *number* of usable optimizers from the *binary existence* observer, which is already 1 throughout K>=292.

At K=292 and every K>=315, the earlier family-invariance theorem makes Z_K deterministic under closure, so its variance is zero.

## Verification / evidence

Input: `EXACT_R5_REQUIREMENT_ZETA.json` at pinned commit
`69b0fa35b6c0f191190c66f8d857a175b289370c`, containing integer strings for K=292..315 and `N_both_equals_N_all` certificates. The original R5 data derive from `VERIFY_R5_REQUIREMENT_ZETA.py` at that commit.

In the present continuation, the 24 rows were read from GitHub and evaluated with JavaScript `BigInt` products, not binary floating point. Exact D-sign classification: positive 3, negative 19, zero 2. All four displayed crossover determinants were obtained from that exact pass. `VERIFY_R5_LOG_INTERACTION.py` replays the same integer checks using only Python's standard library and the existing JSON; it contains the explicit expected sign sets and asserts them.

This is additional analysis of the previously saved finite spectrum, not an independent rederivation of its DP counts. Independent mathematical review remains **NOT_REVIEWED**.

## Next scientific question

For the same frozen data, compute the exact directed max-min replacement distance `R_15(K),R_17(K)` for K=293..314 using the four enabling-mask cohorts. Preserve `max_S min_T` quantifier order; do not substitute a typical or average distance. The log-count crossovers suggest that multiplicative optimizer abundance alone is insufficient to predict worst-case reconfiguration distance.

## Existing sources

- R5 optimizer prerequisite theorem, exact counts, original DP: [Draft PR #2412](https://github.com/awdawmip/enterprise-math/pull/2412), `research_notes/portable_direct/r5_requirement_zeta_20261114/`.
- Prior full-cost family compression: [Draft PR #2379](https://github.com/awdawmip/enterprise-math/pull/2379).
