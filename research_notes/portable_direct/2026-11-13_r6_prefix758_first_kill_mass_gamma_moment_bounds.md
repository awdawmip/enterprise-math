# PREFIX-758-R6 — First-kill mass improves quantitative Gamma(max) ordering bounds

Date: 2026-11-13 (Asia/Shanghai). Continuation of PREFIX-757; parent PREFIX-675.
Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scope: the external two-Gamma-clock auxiliary model, not the native X6 time evolution.
Evidence: AUTHOR_EXACT_ANALYTIC_DERIVATION_AND_RATIONAL_CONSTANT_CHECK / UNREVIEWED / NOT_ADMITTED.

## Theorem 758.1 (exact earliest-death mass and optimal uniform bound)

Reuse the 350 exact frozen mask checks of PREFIX-757: all Bernoulli paths survive rows 1..24, and at row 25 only the two extreme paths k=0,25 are killed. Let `T_z` be the positive integer stopping layer for `z in [0,1/2]`. Then

`Pr(T_z=25)=g(z):=z^25+(1-z)^25 >= 2^(-24)`.

Proof: for n<=24 all masks accept, hence the probability of stopping at n=25 is exactly that of 25 Bernoulli outcomes all equal, either zero successes or 25 successes. The function g is symmetric and strictly convex on (0,1), with `g'(z)=25[z^24-(1-z)^24]<=0` on [0,1/2], so its minimum there is `g(1/2)=2*(1/2)^25=2^(-24)`. This constant is **optimal as a uniform lower bound for the earliest-death mass** over this parameter interval, attained at z=1/2. QED.

If `G_m` denotes the Gamma(m,1) waiting time, the conditional clock CDF obeys, for all t>0,

`F_z(t):=Pr(G_{T_z}<=t) >= g(z)*Pr(G_25<=t) >= g(z)*exp(-t)*t^25/25!`.

The second inequality uses the exact integer-shape Gamma CDF
`Pr(G_25<=t)=exp(-t)*sum_{j=25}^{infinity}t^j/j!`.

## Theorem 758.2 (improved strict survival and moment gaps)

For any real `0<=p1<p2<=1/2`, put `D=S_25(p2)-S_25(p1)>0`.
The all-row stochastic order in PREFIX-756 gives

`H_{p2}(t)-H_{p1}(t) >= D exp(-t)t^25/25!`,

where `H_p(t)=Pr(G_{T_p}>t)`. Let `Y(p,z)` be the maximum of two independent conditional clocks. Its survival tail satisfies

`Pr(Y(p2,z)>t)-Pr(Y(p1,z)>t)`
`=(H_{p2}(t)-H_{p1}(t))*F_z(t)`
`>=D*g(z)*exp(-2t)*t^50/(25!)^2`
`>=D*exp(-2t)*t^50/[2^24*(25!)^2]>0`

for every t>0, z in [0,1/2]. This is independent of the slower row-189 tail bound of PREFIX-757.

For every real r>0, direct tail integration yields

`E[Y(p2,z)^r]-E[Y(p1,z)^r]`
`>= r*D*g(z)*Gamma(r+50)/[(25!)^2*2^(r+50)]`
`>= r*D*Gamma(r+50)/[(25!)^2*2^(r+74)]>0`.

In particular, **without any floating-point approximation**, the first raw-moment gap obeys

`E[Y(p2,z)]-E[Y(p1,z)] >= D*C(50,25)/2^75`,

and the second raw-moment gap obeys

`E[Y(p2,z)^2]-E[Y(p1,z)^2] >= 51*D*C(50,25)/2^75`.

The exact coefficient is

`C(50,25)/2^75 = 15801325804719/4722366482869645213696`,

approximately `3.346060891724141e-9`. The second-moment coefficient is exactly 51 times this value. For the exact test p1=0,p2=1/4 from PREFIX-757,

`D=281263154558295/281474976710656`,

so the mean gap is at least

`4444330742038655213871594105/1329227995784915872903807060280344576`.

This quantitative certificate improves the earlier first- and second-moment bounds obtained by using only termination at layer 189. For arbitrary large r both certificates remain valid; which is numerically stronger may depend on r. Neither bound implies monotonicity of variance `Var(Y)`, so Gamma extreme-value cells still require their actual comparison functional certificates.

## Verification, provenance and next action

Exact Fraction calculation of `C(50,25)/2^75`, the second-moment factor, and the stated sample mean gap was executed in a local Python-stdlib process. The separately published PREFIX-757 checker supplies the 350 frozen integer-width membership checks. The proofs above are analytic statements; no sampling approximation or new 189-row run is claimed.

Sources:
- `research_notes/portable_direct/2026-11-13_r6_prefix757_soft_centered_masks_strict_gamma_order.md` (project main, published in this research continuation).
- `research_notes/portable_direct/2026-11-13_r6_prefix756_centered_killed_pascal_monotonicity.md` at `0f8b4c3b13b5976ec442631e820fee7fa1a1c10c`.
- Frozen BRC scientific source commit `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Next: investigate whether the exact earliest-kill mass can tighten a certified comparator bound or identify a concrete uncovered fine cell. Keep the variance term separate from ordered raw moments. Formal independent review remains open. No shared CLAIM, Result or Review is asserted by this unshared proof.
