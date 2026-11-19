# EC49FTP — Curvature-compensation stochastic order beyond product log-concavity

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. **Route:** independent portable research, no native Task CLAIM.

## Sources, model and preserved scientific scope

Frozen BRC16943 science: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (310 original configurations, 141 separate named profiles, 228 physical observations). No native Bellman recomputation or P000 change.

Inherited original-index Bellman optimum: EC49FTH [PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) @ `999bf1069403306b3813e0e390dae4435d7b4b8c`. Probability/optimization parents: EC49FTK #2776, EC49FTL #2779, EC49FTM #2783, EC49FTN #2786 and EC49FTO [#2788](https://github.com/awdawmip/enterprise-math/pull/2788) @ `d790653d2e61b3d4db0a8fe066e746d0ad6196d7`.

Independent *external price parameters* a in A=[3/4,49/64], b in B=[7/16,57/128], q140 discount z in [11/16,3/4]. These parameters are not asserted to be original native X6 spatial coordinates or 141 equiprobable BRC states.

Inherited formulas:
- Z(a,b) = min(3/4, (105a-6b-5)/96).
- M(a,b)=max_z(D-S)=(525a-462b-9)/8 for a<a_c(b)=(77+6b)/105, and M=47-54b otherwise.
- Support m in [m0,m3], where m0=11457/512, m1=1461/64, m2=1469/64, m3=187/8. Define α=44/45, β=10/9.
- Nonclipped inverse map: a(m,z)=(47-m)/945+αz, b(m,z)=1/27-m/54+βz, Jacobian 16/945.
- Conditional continuous z fiber: [L1,U1] for m in (m0,m1), [L2,U1] for (m1,m2), [L2,3/4] for (m2,m3), where L1=(4m+2647)/3696, L2=(8m+173)/480, U1=(64m+1411)/3840. Both endpoints are nondecreasing. A top atom at z=3/4 is additionally present for m>m2.

## Theorem: positive C² product curvature compensation

Let a,b be independent and have positive C² densities f on A and g on B; let ℓ_f=log f, ℓ_g=log g. Assume f is nondecreasing, and there are numbers H,G≥0 such that on the *entire respective domains*

`ℓ_f''≤H;   ℓ_g''≤-G;   G≥(44/875)H;   (H/2)(7/960)^2<1.`

Then for all m<m' in the interior of the M support, with one-sided conditional versions at m1,m2,

`Z | M=m ≤_st Z | M=m'.`

This includes the atom at z=3/4, not merely the absolutely continuous component. Consequently Cov(u(M),v(Z))≥0 for any bounded nondecreasing measurable u and v. In particular, product log-concavity of both marginals is **not necessary**.

### Proof: TP2 of the continuous fiber

On a nonclipped feasible fiber the joint density is K(m,z)=(16/945) f(a(m,z))g(b(m,z)). Differentiate:

`∂_m∂_z log K=-(α/945)ℓ_f''(a)-(β/54)ℓ_g''(b)≥-(α/945)H+(β/54)G≥0,`

because (α/945)/(β/54)=44/875. Thus K is TP2 on feasible cross rectangles, equivalently the density ratio at a larger m is nondecreasing in z. The moving endpoints L1,L2,U1 also move right. On overlapping intervals the monotone likelihood ratio order, combined with deletion of the left tail/addition of the right tail, implies first-order stochastic order of the *continuous normalized* laws, with one-sided transitions at m1,m2.

### Proof: clipping-atom compatibility

For m in (m2,m3), put x=(740-m)/945, y=(47-m)/54, d=49/64-x and T=3/4-L2(m). Then x'=-1/945, y'=-1/54, d'=1/945, T'=-1/60 and 0<d≤7/960. The joint-M density contributions from the clipped stratum and continuous fiber are

`B(m)=g(y)/54 ∫_x^(49/64) f(a)da;`
`I(m)=(16/945)∫_0^T f(x-αt)g(y-βt)dt.`

Normalize by f(x)g(y), writing B/I=(945/864)N/Q, where

`N=∫_0^d exp[ℓ_f(x+s)-ℓ_f(x)]ds`,
`Q=∫_0^T exp[ℓ_f(x-αt)-ℓ_f(x)+ℓ_g(y-βt)-ℓ_g(y)]dt`.

Writing E(s)=exp[ℓ_f(x+s)-ℓ_f(x)] and using Leibniz,

`945N'=E(d)-∫_0^d E(s)[ℓ_f'(x+s)-ℓ_f'(x)]ds.`

Since f is nondecreasing, E(s)≤E(d); ℓ_f''≤H implies ℓ_f'(x+s)-ℓ_f'(x)≤Hs. Hence

`945N'≥E(d)[1-Hd²/2]>0.`

The m-derivative of log Q's *integrand* at fixed t is

`[ℓ_f'(x)-ℓ_f'(x-αt)]/945+[ℓ_g'(y)-ℓ_g'(y-βt)]/54 ≤ t(αH/945-βG/54)≤0.`

As T decreases strictly, Q strictly decreases. Therefore B/I strictly increases and so does the top-atom probability p(m)=B/(B+I). At the threshold m2 the newly added atom is located at the maximal feasible z; combining with the continuous TP2 order proves the mixed conditional order across all m. The covariance corollary follows from E[v(Z)|M=m] being nondecreasing and the two-copy monotone covariance identity. QED.

## Strictly log-convex polynomial marginal: exact example

Take independently normalized densities proportional to

`f(a)=1+(a-3/4)^2,     g(b)=b.`

For u=a-3/4 in [0,1/64],

`(log f)''=2(1-u²)/(1+u²)^2>0,   (log f)''≤2,`

while `(log g)''=-1/b²≤-16384/3249`. Therefore H=2, G=16384/3249 work. The exact TP2 margin is

`βG/54-αH/945=14050088/138163725>0`.

The maximum d is 7/960 and Hd²/2=49/921600<1. This density f is **strictly log-convex everywhere**, so the preceding theorem is a genuine extension, not a restatement of product log-concavity.

Exact clipping probability:

`P(Z=3/4)=3636023540431/8037720298125 ≈ 0.452370001140646.`

To reproduce, let F(a)=a+(a-3/4)^3/3 and a_c(b)=(77+6b)/105. The unnormalized clipping numerator is

`∫_(7/16)^(57/128) b[F(49/64)-F(a_c(b))] db=3636023540431/149158845480960000`.

The total unnormalized mass is

`[F(49/64)-F(3/4)]·[(57/128)^2-(7/16)^2]/2=1388657/25769803776`.

Division gives the stated rational probability. These are exact polynomial integrals, with a second independent symbolic integration check.

## Computation, reproducibility and unfinished questions

Run `python EC49FTP_CURVATURE_COMPENSATION_VERIFY.py` with Python standard library. Actual author run: 36 rational m values, 37 z thresholds, 23,310 exact Fraction stochastic-order comparisons; 468 exact inverse-map points; exact TP2-margin and rational clipping mass checks passed. The checker is a finite regression; the continuum theorem is the analytic argument above.

**Evidence boundary:** parent native BRC optimality and M,Z mapping are inherited author proofs, not independent review. No native 228-observer Bellman run, Lean formalization, canonical Result/Review/CLAIM, or Activity publication is claimed here. Draft PR is a durable source, not Foundation acceptance.

**Next:** determine necessary/sharp TP2 and top-atom compatibility for dependent price priors; separately compute the next original-index BRC Bellman phase below z=11/16 under frozen input, without projecting away named states.
