# BRC N=4 S23: a certified finite-contrast Chernoff crossover

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF + EXACT_INTEGER_INTERVAL_EXECUTED; independent review and native admission pending.

## Precise scientific scope

This is the inherited two-state statistical experiment (scheme (3,31), removed source label 0, E-observation repair), not a theorem about all nine-parameter recovery designs or the ten-label decoder minimax. Keep the scientific source pinned at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`; current governance rules are read separately. Set `h=1/42`, `s=(1-beta_E)^2`, `0<s<1`, `beta_N=0`, with equal prior hypotheses and independently sampled observations. These are legal boundary states in the prior S23 construction.

Full-source observation `T` has laws `(s(1/2+h), 1-s, s(1/2-h))` and `(s(1/2-h), 1-s, s(1/2+h))`, and price `c_T=2-s`. Repaired Bernoulli observation `B` has success rates `s(1/2+h)` and `s(1/2-h)`, price `c_B=1`. Write `C_T` and `C_B` for their Chernoff information, and `F(s,h)=C_T/(2-s)-C_B`. `F>0` means T has higher Chernoff information per stipulated cost; `F<0` means B does.

## Theorem: a unique certified crossing inside an explicit interval

At the lawful finite contrast `h=1/42`, the equation `F(s,h)=0` has **exactly one** root in the rational interval

`10243902443/100000000000 < s < 10243902445/100000000000`.

The sign is negative at the left endpoint and positive at the right endpoint, and throughout the closed interval

`36499888 / 10^15 < (d/ds) F(s,1/42) < 36933068 / 10^15`.

Thus the crossover is resolved to absolute width `2/10^11 = 0.00000000002`. The sixth-order predecessor gave only a small-h local asymptotic shift from `s_*=(20-2 sqrt(91))/9`; this theorem certifies an actual finite lawful h with a truly optimized Chernoff coefficient. Other roots outside this interval remain the next independent question.

## Exact formulas and proof

Let `u=s/2`, `v=1-u`, `d=sh`, and define positive quantities

`X=s sqrt(1/4-h^2)`, `Y=sqrt(v^2-d^2)`, `alpha=atanh(2h)`, `gamma=atanh(d/v)`.

Use `delta=2t-1`, where `t` is the Chernoff exponent. The Bernoulli Chernoff coefficient is

`G(s,delta)=X exp(alpha delta) + Y exp(-gamma delta)`, `-1<=delta<=1`.

`G_delta_delta = X alpha^2 exp(alpha delta)+Y gamma^2 exp(-gamma delta)>0`; its stationary exponent is

`delta_*(s) = log(Y gamma/(X alpha))/(alpha+gamma)`.

The exact full-source Chernoff coefficient is `T(s)=1-s+s sqrt(1-4h^2)` (optimized at exponent 1/2), and

`F(s,h)=log(G(s,delta_*(s)))-log(T(s))/(2-s)`.

Consequently, for rational endpoints, the sign of F is determined by comparing `G(s,delta_*)` with `E(s)=exp(log(T(s))/(2-s))`.

For the **left endpoint**, the executable certificate evaluates `G` at the rational trial delta `0.00751349463555` and proves `G<E`. Since `min G <= G(trial)`, this establishes `F<0`. For the **right endpoint**, the trial delta is `0.00751349463546`. The program proves `G_delta(delta0-r)<0<G_delta(delta0+r)` with `r=0.00000000003`, so the unique minimizing delta lies in this small rational enclosure. Convexity bounds `|G'|` inside that interval by the larger absolute endpoint derivative. Therefore `min G >= G(delta0)-r max(|G'(delta0-r)|,|G'(delta0+r)|)>E`, proving `F>0`.

For uniqueness on the entire rational s-interval, use the envelope theorem at the interior minimizer. Put `k=sqrt(1/4-h^2)`, `v=1-s/2`, and write

`Y_s=(-v/2-s*h^2)/Y`, `gamma_s=4h/((2-s)^2-4s^2 h^2)`, `T_s=sqrt(1-4h^2)-1`.

At `delta=delta_*(s)`,

`G_s=k exp(alpha delta)+(Y_s-Y delta gamma_s)exp(-gamma delta)`

and exactly

`F_s=G_s/G - T_s/(T(2-s)) - log(T)/(2-s)^2`.

The verifier encloses `s` over the full rational interval; obtains a rigorous enclosure of `delta_*(s)` from the exact log-ratio formula; checks it lies in `(0,1)`; and interval-evaluates `F_s` with **positive lower bound** `36499888/10^15`. Hence F is strictly increasing over this interval. Together with endpoint signs and continuity, the intermediate value theorem proves exactly one root there. QED.

## Certificate semantics

`VERIFY.py` performs only rational and integer arithmetic, `isqrt`, and fixed-point outward rounding with unit `10^-70`. The identities used for transcendental bounds are elementary convergent series:

`atanh(x) = sum_{k=0}^{N-1} x^(2k+1)/(2k+1) + R`, for `0<=x<1/2`, with `0<=R<=x^(2N+1)/((2N+1)(1-x^2))`; use `N=32`.

For `0<=x<1/8`, `exp(x)` is bounded below by its first 36 Taylor terms and above by the same partial sum plus the first omitted term divided by `1-x/(N+2)` (`N=35`); negative arguments use `exp(-x)=1/exp(x)`. `log(z)=-2 atanh((1-z)/(1+z))` for `0<z<=1`, and positive log ratios are evaluated by the corresponding positive atanh formula. Square roots are enclosed by integer `isqrt` at the fixed-point scale. Each operation rounds lower endpoints down and upper endpoints up. These inequalities and the arithmetic code are sufficient for an independently executable certificate without relying on floating-point root finding.

The script proves both endpoint signs, the optimizer localization, and positivity of the full-interval derivative. It is a finite exact computer-assisted certificate of a real-variable theorem, subject to review of the displayed analytic identities and verifier implementation. It does not prove global uniqueness over `0<s<1`. The project P000, provenance and observer/source distinctions are unchanged.

## Next

Investigate the complement `(0,s_L] union [s_R,1)` for further zeros. A potentially tractable target is to certify the sign of a properly normalized F on bands bounded away from `s=0,1`, with separate endpoint expansions and interval subdivisions; retain actual Chernoff optimization. Then examine finite-budget allocation changes near the certified finite-h crossover and compare costs under the original observation pipeline.
