# R749SE — Strict finite-horizon and Chernoff-exponent loss from the 960-to-120 signed-source observer

Date: 2026-11-12. Independent TASK_RESEARCH scientific increment for scheduled Research2; native Source session registration request `research2-20261112-2115-R749SE-increment-session-v1`, SID `MCP-202aad4c7ff74091a0fbd489ef91c818` (session receipt/Researcher ID and activity to be read from Source separately). Author-side mathematical proof and rational checks, not independently reviewed.

**Scientific pins.** Source P000 at `awdawmip/enterprise-math@4e318b1a978a4c4e26817752354cdd3e63ebee87:p000_reality_foundation.json`. Predecessor frozen scientific input `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Use R749SA source at `ec7b7eec75e177e9d10c99b5cf943400189416d1:research_notes/portable_direct/2026-11-12_R749SA_UNSIGNED_SUPPORT_QUOTIENT_AND_RESIDUAL.md`, R749SD at `14af65b5285215cbd149d8db856be92bd5ea3c1d:research_notes/portable_direct/2026-11-12_R749SD_BINARY_DEGRADATION_AND_EXACT_TESTING.md`. Those are scientific premises, not updated behavioral rules.

## Exact question and model

Under the R749SA signed directed-edge carrier (960 states) and its 8:1 unsigned observer (120 states), a subsequent transition has 16 signed outgoing neighbors: exactly one full named-source C1 continuation S, one different signed lift with unsigned C1 continuation U, and fourteen others O. The R749N family mixes deterministic S with uniform resampling:

- `q(p)=(1+15p)/16`: probability of S.
- `r(p)=(1-p)/16`: probability of each of the 15 other signed continuations.
- `a(p)=q+r=(1+7p)/8`: probability of an unsigned C1 continuation.
- `p∈[0,1]`. In an n-vertex path, write `m=n-2` subsequent innovations.

For inference on p (not recovery of individual named signed-port trajectories), observing the entire signed path has the same parameter experiment as m iid `X_i~Bernoulli(q(p))`; observing its unsigned projection is equivalent to m iid `Y_i~Bernoulli(a(p))`. This R749SD equivalence assumes the fixed homogeneous 1:1:14 transition law and p-independent labeling of the nonforced choices. The parameter-independent observer channel is
`B(Y=1|X=1)=1`, `B(Y=1|X=0)=1/15`; apply it independently each step.

Consider testing `H_0:p=p_0` against `H_1:p=p_1`, equal prior weights, `0≤p_0<p_1≤1`. Denote the optimal Bayes errors `E_s(m)` and `E_u(m)`.

## Theorem 1 — Strict information loss at *every* finite positive horizon

For every integer `m≥1` and `0≤p_0<p_1≤1`,

`E_s(m)<E_u(m)`.

More sharply, writing `q_j=q(p_j)`,

`E_u(m)-E_s(m) ≥ 1/2 min{q_1^m-q_0^m, [(1-q_0)^m-(1-q_1)^m]/15^m} > 0.    (1)`

**Proof.** Let `P_j` be the product Bernoulli(q_j) laws on `X^m`. Let `Q_j=B^⊗m P_j` be the corresponding unsigned laws. The total-variation difference is a sum, over observed y, of the cancellation between the positive and negative parts of the signed difference `P_1-P_0` inside the fiber over y. Pick the single observed output `y=(1,...,1)`. In this fiber, the signed input `x=(1,...,1)` has positive difference `q_1^m-q_0^m>0` and maps to y with probability 1. The input `x=(0,...,0)` has negative difference `(1-q_1)^m-(1-q_0)^m<0` and maps to y with probability `15^{-m}`. Hence the cancellation in this fiber is at least the minimum of their two positive magnitudes. TV satisfies `E=(1-TV)/2`, proving (1) and strictness. This proof also covers `p_1=1`, where the second negative difference remains nonzero. There is no reliance on an unproved asymptotic extrapolation.

## Theorem 2 — Exact asymptotic sample discrimination exponent

For a Bernoulli observation channel `c(p)`, where `c` is either q or a, define `c_j=c(p_j)`. If `p_1<1`, set

`t_c = log((1-c_0)/(1-c_1)) / log(c_1(1-c_0)/(c_0(1-c_1)))`,
`D(t||c)=t log(t/c)+(1-t)log((1-t)/(1-c))`.

Then `c_0<t_c<c_1` and

`lim_{m→∞} -(1/m)log E_c(m)=C_c=D(t_c||c_0)=D(t_c||c_1)>0.    (2)`

Equivalently,
`C_c=-log min_{0≤s≤1}[c_0^{1-s}c_1^s+(1-c_0)^{1-s}(1-c_1)^s]`.

**Proof.** The log likelihood ratio at count k is
`k log(c_1/c_0)+(m-k)log((1-c_1)/(1-c_0))`; it crosses zero at `k/m=t_c`. The two Bayes error tails are binomial tails across this threshold. Stirling's formula (or elementary binomial large deviations) gives exponents `D(t_c||c_0)` and `D(t_c||c_1)`. Algebra using the zero log-likelihood condition makes these two divergences equal. The sum of the tails has this exponent. The variational expression follows by optimizing the Chernoff coefficient; the minimizing tilted Bernoulli law has mean `t_c`.

If `p_1=1`, the optimal rule chooses H1 exactly on the all-successes word, and
`E_c(m)=c_0^m/2`, `C_c=-log c_0`. This is the correct boundary formula, replacing (2)'s interior threshold expression.

## Theorem 3 — Signed-source precision yields a strictly larger asymptotic error exponent

For all `0≤p_0<p_1≤1`,
`C_s>C_u>0`.   (3)

**Proof for p1<1.** For `0<s<1`, applying the fixed B channel strictly increases the Hellinger/Chernoff affinity `A_s(P_0,P_1)=Σ_x P_0(x)^{1-s}P_1(x)^s`. This follows from the weighted Hölder inequality in each output fiber. Equality in a fiber requires a constant likelihood ratio there. Output Y=1 receives input X=1 with probability 1 and X=0 with probability 1/15. The hypotheses have unequal likelihood ratios `q_1/q_0>1` and `(1-q_1)/(1-q_0)<1`, and all those input masses are positive. Hence the inequality is strict for every interior s. Since `A_s` has an interior minimum for distinct Bernoulli laws, its post-channel minimum is strictly larger. Taking negative logarithms gives (3). For p1=1, use the boundary formula: `0<q_0<a_0<1`, so `-log q_0>-log a_0`.

## Theorem 4 — Exact local testing-efficiency ratio

For any fixed `0≤p<1` and a small admissible positive difference `δ`,

`C_s(p,p+δ)=δ² I_s(p)/8+O(δ³)`,
`C_u(p,p+δ)=δ² I_u(p)/8+O(δ³)`,

where (from exact Bernoulli derivatives)

`I_s(p)=15/[(1+15p)(1-p)]`,
`I_u(p)=7/[(1+7p)(1-p)]`.

Thus the local ratio of required observation counts at the same leading exponential error is

`I_s/I_u=15(1+7p)/[7(1+15p)]`.

This ratio is strictly decreasing in `p∈[0,1)`; it starts at `15/7` and tends to `15/14` as `p↑1`. Differentiate the rational ratio: its numerator derivative after cancellation is `-8`, times the positive prefactor. The statements are local-in-p and do not identify observation count with physical time or heartbeat steps.

## Exact worked example and checker

For `p_0=0,p_1=1/2`, signed `(q_0,q_1)=(1/16,17/32)` and unsigned `(a_0,a_1)=(1/8,9/16)`. The exact optimal errors at m=2 are `349/2048` and `109/512` respectively, with unsigned excess `87/2048`, recovering R749SD. At m=1 the excess is `1/64`, exactly attaining lower bound (1). At m=4 the excess is `29471/2097152`.

A 65-digit Decimal log readout (not a certified interval):
- `t_s≈0.244650542118226030`, `C_s≈0.170682985118309964`.
- `t_u≈0.315464876785728719`, `C_u≈0.123994067370048728`.
- `C_s/C_u≈1.376541545402511205`: the unsigned observer needs about 37.65% more steps in the *fixed-pair, small-error exponential regime* to reach the same leading error exponent.

`R749SE_CHERNOFF_OBSERVER_EXACT_CHECK.py` verifies rational Bayes error, positive finite observer penalty and the explicit bound at m=1,2,4,8,16,32,64, the exact m=2 historical values, 48 additional strict-error pairs across four p-pairs and m=1..12, four rational Fisher identities and the p1=1 endpoint. The checker uses integer and `fractions.Fraction` arithmetic for finite claims; numeric exponent values use `decimal.Decimal`, with exact symbolic theorem proof above. The bounded checker assumes the previously proven 1:1:14 fiber law, rather than re-running the 960-edge construction.

## Research consequence / next useful question

R749SD's loss of source evidence is present for every finite sample size, not merely m=2, and its best asymptotic discrimination rate can now be quantified exactly. This creates an observer-sensitive BRC-style provenance budget: choosing an unsigned carrier is justified for unsigned-support forecasting (R749SA), while any future source-parameter decision should account for (1)-(3) or retain the signed C1 statistic. A promising next unit is an **arbitrary nonuniform initial eight-lift distribution**: derive a finite-rational hidden-sign filtering transport under observed unsigned paths and determine what minimal source residual must be retained. Native V29/V39 Cell/Link/Port closure and event permission remain separate input checks before transferring these laws to physical events.
