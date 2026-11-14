# R749SOE — Exact positive Walsh calibration-gap transverse segment

**Status:** author-side exact theorem and exhaustive rational polytope certificate (`NOT_REVIEWED`), 2026-11-14.

**Immutable scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessors:** R749SNG (PR #2309, diagonal minimax), R749SOD (PR #2367, positive-gap diamond). The source/observer model is auxiliary: no native X6/V29/V39 correspondence is asserted. Project P000, the ACTIVE X6 worldview, and the source-pinning rules remain unchanged.

## Statement

Let `G=F_2^4`, `chi_m(k)=(-1)^(popcount(m & k))`. Put `A=chi_3`, `B=chi_12`, `C=chi_15=A B`, and `P=chi_1`, `AP=chi_2`, `Q=chi_4`, `BQ=chi_8`. For real `(t,s)` let `F_{t,s}` be all nonnegative laws

`mu_{t,s,h,u,v,w,z}(k)=[1+t A(k)+s B(k)+h C(k)+u P(k)+v AP(k)+w Q(k)+z BQ(k)]/16`.

These are *all* compatible sources, since the other retained Walsh coefficients are fixed to zero. Define

`rho(t,s)=min_{q in Delta(G)} max_{mu in F_{t,s}} TV(q,mu)`,
`rho_cal(t,s)=min_{q in F_{t,s}} max_{mu in F_{t,s}} TV(q,mu)`.

**Theorem (all real parameters):** for `s=1/2`, `x=t-1/2` and `0<=x<=1/16`,

```
rho(1/2+x,1/2)     = 2/5 - x/2
rho_cal(1/2+x,1/2) = 9/22 - 6x/11
g(1/2+x,1/2)       = 1/110 - x/22 >= 1/160 > 0.
```

An optimal free law is `q_free=[1+A+(B+C)/5]/16`. An optimal calibrated law is `q_cal=[1+t A+(1/2)B+((2+x)/11)C]/16`. Both are nonnegative on the full segment; the calibrated law lies in the source fiber (its non-retained coefficients vanish). At `t=9/16`, the exact gap is `1/160`. This reaches transverse displacement `1/16`, 6.25 times the radius `1/100` of the earlier *two-dimensional sufficient diamond*, without claiming a larger two-dimensional region.

## Symmetry and analytic lower bounds

The source fiber is preserved by translation by `3` and by `12` in `G`: these operations flip the pair `(P,AP)` and `(Q,BQ)` respectively, while fixing `A,B,C`. By convexity, group-averaging cannot worsen either minimax risk. Thus it suffices to lower-bound symmetric predictors

`q_{a,b,c}=[1+a A+b B+c C]/16`,

with `a,b,c` chosen to give a law, and `a=t,b=1/2` for calibrated prediction.

For each `x in [0,1/16]`, define two compatible sources by the five free coefficients `(h,u,v,w,z)`:

```
mu_A=(1-x, -x, -x, 0, 0)
mu_G=(x, -1/2, -1/2, x-1/2, x-1/2).
```

Their sixteen atom probabilities are affine in `x`; substitution at both interval endpoints shows every atom is nonnegative, so these sources are valid for the full real segment. Use the three events

```
E_A   ={1,2,4,7,8,11,13,14}
E_GI  ={0,1,2,3,4,8,12}
E_GII ={0,1,2,3,4,5,6,8,9,10,12}.
```

Writing `L_A=q(E_A)-mu_A(E_A)` and `L_GI,L_GII` similarly with `mu_G`, direct character sums give **for every real `a,b,c`**

```
L_A   = (1-x-c)/2
L_GI  = (3a+3b-c)/16 - x/2 + 3/16
L_GII = (-a-b+3c)/16 - x/2 + 7/16.
```

For each event, `TV(q,mu)>=q(E)-mu(E)`. Positive convex combinations eliminate *all* free center parameters:

`(L_A+L_GI+3 L_GII)/5 = 2/5-x/2`.

For calibrated centers `a=1/2+x,b=1/2`, an additional combination eliminates `c`:

`(3 L_A+8 L_GII)/11 = 9/22-6x/11`.

These yield global lower bounds on both minimax values.

## Complete rational upper certificate

Set `y=(16t,16h,16u,16v,16w,16z)` with `s=1/2`. The joint source/parameter polytope has sixteen nonnegative-atom facets and two parameter endpoint facets `t>=1/2` and `t<=9/16`, all with **integer** coefficient matrices and right sides. It is compact and six-dimensional; every vertex admits six independent active facets. Exhaustive enumeration checks all `C(18,6)=18,564` candidate bases, solves with integer Bareiss elimination, discards singular or infeasible bases, then deduplicates rational vertices.

For either displayed predictor, `TV(mu,q)-r(t)` is convex in the six joint variables: the probabilities and proposed radius are affine, and total variation is a sum of absolute values. Its maximum therefore occurs at a vertex. The exact checker establishes:

| Item | Result |
|---|---:|
| All six-facet subsets | 18,564 |
| Nonsingular bases | 9,536 |
| Feasible bases | 812 |
| Distinct rational vertices | 37 |
| Free-predictor tight vertices | 13 |
| Calibrated-predictor tight vertices | 13 |
| Maximal upper-bound excess for each predictor | 0 |
| Violations | 0 |

Thus the upper bounds hold for **all real** source coefficients and parameters in the whole segment, and together with the analytic lower bounds prove the theorem. All computational operations use exact integers and `fractions.Fraction`, without numerical tolerances. The complete program is `R749SOE_TRANSVERSE_WALSH_EXACT_CHECK.py`, with deterministic stdout `R749SOE_TRANSVERSE_WALSH_RESULTS.json`.

## Interpretation, preservation and next question

This identifies a strictly positive gap throughout a previously uncertified off-diagonal line up to displacement `1/16`, and provides explicit free/calibrated centers plus three universal event dual certificates. It neither enlarges the earlier full-dimensional positive diamond nor changes the pinned source model.

**Next:** locate the exact first change of calibrated-optimal center as `t` increases past `9/16` with `s=1/2`; test whether a second affine phase permits a longer exact positive-gap interval. In parallel, construct a parameterized two-dimensional neighborhood of this line with a joint-vertex certificate; keep native observer correspondence as a separate task. Independent mathematical review remains pending.
