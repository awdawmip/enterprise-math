# EC49FTR Supplement — C-infinity correlated prior: strict continuous TP2 yet reversed mixed stochastic order

**2026-11-19 | AUTHOR_PROVED / EXACT_RATIONAL_BOUND_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**

## Complete setup

This supplement solves the remaining counterexample question posed in the EC49FTR main theorem. It uses the same frozen BRC16943 scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, inherited author-proved native parent PR #2774, and the high-gap external price-prior transform from EC49FTQ PR #2793. It is strictly about external price prior conditioning, not native BRC/heartbeat evolution.

Let `p=23 < q=93/4`, `b_p=4/9`, `b_q=95/216`, `d_p=139/20160`, and `a_c(b)=(77+6b)/105`. Let `Phi(s)=0` for `s<=0` and `Phi(s)=exp(-1/s^2)` for `s>0`. For all prices in `a∈[3/4,49/64], b∈[7/16,57/128]`, define the **strictly positive, globally C-infinity, correlated** density up to normalization

```text
h_C(a,b) = 1+a+b
          +1000*((b-b_q)/(b_p-b_q))^2 * Phi((a-a_c(b))/d_p).
```

This is genuinely nonproduct because the additional term vanishes identically along b=b_q while the section there varies affinely in a; sections at other b cannot all be proportional to that same affine function.

## Why the nonclipped kernel remains strictly TP2

The bump is supported on the *clipped* wedge `a>a_c(b)` and vanishes identically on `a<=a_c(b)`. Thus the nonclipped conditional kernel for the optimizer is **exactly** the nonconstant EC49FTR kernel

```text
K(m,z)=(16/945)*(2054-37m+3948z)/1890
```

for all m,z in the inherited nonclipped high-gap wedge. In particular,

```text
partial_m partial_z log K = 146076/(2054-37m+3948z)^2 >0.
```

This is *strict* TP2, stronger than the flat TP2-equality counterexample in EC49FTQ.

## Exact clipping-atom reversal

The continuous kernel is unchanged for every C. For `b=b_q` the bump vanishes identically even on the clipped fiber, hence the conditional law at `m=q` remains the unperturbed `h_0=1+a+b` law.

At `m=p` the clipped atom increases by `(1000/54)d_p J`, where `J=∫_0^1 exp(-1/s^2)ds`. On `[1/2,1]`, `exp(-1/s^2)>=exp(-4)>1/81` since `e<3`; therefore **J>1/162**. Write `A_0,B_0` for the explicit rational nonclipped and clipped masses given in the main theorem. Then

```text
r_C(p)>[B_0(p)+(1000/162)d_p/54]/A_0(p),
r_C(q)=B_0(q)/A_0(q),
r_C(p)-r_C(q)>158980872564325/190572643785024>0.
```

The atom ratio **decreases** between p<q despite strict continuous TP2. By EC49FTR Theorem B this already disproves conditional stochastic increase. To give a direct CDF certificate, take threshold `t=3071/4096`, satisfying `L(q)<t<3/4`. Exact integration of the common nonclipped affine kernel gives

```text
F_C(t|m=q) = 4802228009/25942353984,
F_C(t|m=p) < 141169363569/823185364544,
F_C(t|q)-F_C(t|p) > 284041223446367875/20854849727977080804 >0.
```

Since p<q yet the later conditional CDF is larger at t, first-order stochastic increase fails. This proof uses only analytic flatness of Phi, a rational lower bound on its integral, and exact rational integration for the rest; no numerical approximation of Phi or Monte Carlo is required.

A second positive C^3 but not C-infinity polynomial witness replaces `Phi(s)` with `(max(s,0))^4` and uses coefficient `C=100`. It has the same strictly TP2 nonclipped kernel, and a fully rational clipped increment `(100/5)d_p/54`. At the same threshold its earlier CDF is exactly `5228494947/71818503872`, strictly smaller than `F_q(t)`.

## Significance, verification, and boundary

**Strictly positive smooth joint prior + strictly TP2 nonconstant continuous kernel does not guarantee conditional first-order stochastic order.** For nested-support mixed laws, the increasing top-atom-to-continuous ratio is a distinct indispensable condition, and under TP2 it is the precise missing *if and only if* condition established in the main theorem.

The standalone `EC49FTR_STRICT_TP2_REVERSAL_VERIFY.py` recalculates the rational bounds, strict CDF reversal and independent C^3 witness with standard-library Fraction; `EC49FTR_STRICT_TP2_REVERSAL_CERT.json` captures the exact result. The smooth integral is bounded analytically, not numerically integrated. All native BRC Bellman claims remain inherited and NOT_REVIEWED, no new physical model authority is implied.

**Next:** classify structural conditions on the joint prior guaranteeing or violating clipped atom ratio monotonicity; investigate sharp dependence and curvature requirements beyond this counterexample. The independent native BRC new optimal tree region below z=11/16 remains open.
