# EC49FTO — Log-concave prior stability for native BRC16943 optimal-price stochastic order

Date: 2026-11-19. Mode: independent portable mathematical postprocessing. Scientific status: AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / PARENT_DEPENDENT / NOT_REVIEWED.

## Provenance and typed model

Frozen original science: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (310 original configurations; 141 named response states; 228 original physical observers). This paper does **not** rerun Bellman or change any native source, P000, observer representation, or scientific pin.

Inherited native affine Bellman theorem: EC49FTH PR #2774@999bf1069403306b3813e0e390dae4435d7b4b8c.
Inherited optimal price and conditional mixed law: EC49FTK PR #2776, EC49FTL PR #2779, EC49FTM PR #2783; exponential-prior stability and smooth counterexample: EC49FTN PR #2786@e49c6abeb3921c95aec1aa96d95f14c187697dd4.

External (NOT native-state) price parameters lie in
A=[3/4,49/64], B=[7/16,57/128], z in [11/16,3/4].
The inherited optimized q140 discount and swap-cost gap are

Z(a,b)=min(3/4,(105a-6b-5)/96),

M(a,b)=max_z(D-S)= (525a-462b-9)/8 if a<a_c(b), and 47-54b otherwise,

a_c(b)=(77+6b)/105.

Choose a and b independently, with *arbitrary strictly positive continuous log-concave probability densities* f on A and g on B. Log-concave means log f, log g concave (no twice differentiability is required). The marginal density normalization may be absorbed in f,g. The randomness concerns chosen external prices, not original 141 native BRC response profiles.

The m support is [m0,m3] with m0=11457/512, m1=1461/64, m2=1469/64, m3=187/8. Define
L1(m)=(4m+2647)/3696,
L2(m)=(8m+173)/480,
U1(m)=(64m+1411)/3840.

For almost every m, continuous support in z is
(m0,m1): [L1(m),U1(m)];
(m1,m2): [L2(m),U1(m)];
(m2,m3): [L2(m),3/4].
All lower and upper endpoints are nondecreasing; they join continuously at m1,m2. For m>m2 there is in addition a point mass at z=3/4. Breakpoint conditional laws are understood through one-sided versions; regular conditional laws are unique only almost everywhere.

## Theorem — every positive product log-concave prior preserves conditional stochastic order

For any m<m' in the interior support, taking the one-sided conditional versions at breakpoints,

  Z | M=m  <=_st  Z | M=m'.

Equivalently, for every real t, Pr(Z>t | M=m) <= Pr(Z>t | M=m'). This includes the clipping atom at z=3/4 and strictly extends the exponential-tilt family of PR #2786.

### Proof, part 1: continuous conditional likelihood-ratio order

In the non-clipped region, invert the affine map:

a(m,z)=(47-m)/945+(44/45)z,
b(m,z)=1/27-m/54+(10/9)z.

Set alpha=44/45, beta=10/9. The absolute inverse Jacobian equals 16/945. Therefore on the appropriate moving z-fiber the unnormalized continuous joint density is

  K(m,z)=(16/945) f(a(m,z)) g(b(m,z)).

For a positive log-concave univariate function h and any s>0, x -> h(x+s)/h(x) is nonincreasing on its domain (finite-difference slopes of log h decrease). For m'>m and z'>z in the common feasible z-fiber, because a(m',z)<a(m,z) and b(m',z)<b(m,z), while a,b increase with z, we obtain

  K(m',z') K(m,z) >= K(m',z) K(m,z').

Thus K is TP2 / monotone-likelihood-ratio ordered in (m,z) on every overlapping feasible pair of fibers. Under C2 log densities this is directly

  d_m d_z log K = - (44/(45*945)) (log f)''(a)
                  - (10/(9*54)) (log g)''(b) >= 0,

with the preceding finite-difference argument covering nonsmooth positive log-concave densities.

On each continuous strip, both fiber endpoints move right (or remain fixed). Truncating from below and/or adding right-tail mass moves a conditional law upward in first-order stochastic order; on the common interval, the TP2 ratio also moves it upward. Hence the *continuous* conditional component is stochastically nondecreasing in m across all three strips. Their common limit intervals match at m1 and m2.

### Proof, part 2: the clipping atom is increasing

For m in (m2,m3) define

x=a_c(m)=(740-m)/945, y=b_*(m)=(47-m)/54,
d=49/64-x, T=3/4-L2(m), alpha=44/45, beta=10/9.

Since z=3/4-t implies a=x-alpha*t and b=y-beta*t, the non-clipped density mass along the m-fiber and the clipping line mass are respectively

I(m)=(16/945) integral_0^T f(x-alpha*t) g(y-beta*t) dt,

B(m)=(1/54) g(y) integral_x^(49/64) f(a) da.

The clipping weight is p(m)=B/(B+I). After dividing by positive f(x)g(y),

B/I = (945/864)
 * [ integral_0^d f(x+s)/f(x) ds ]
 / [ integral_0^T [f(x-alpha*t)/f(x)] [g(y-beta*t)/g(y)] dt ].

As m increases, x and y strictly decrease, d strictly increases, and T strictly decreases.
For log-concave f the forward ratio f(x+s)/f(x) is nonincreasing in x, hence its integral in the numerator increases as x moves left and d grows.
For log-concave f and g, the backward ratios f(x-alpha*t)/f(x) and g(y-beta*t)/g(y) are nondecreasing in their base points x,y, hence they each decrease as x,y move left; the integration interval [0,T] also shrinks. Thus the positive denominator strictly decreases, the numerator strictly increases, and p(m) strictly increases on (m2,m3).

At m2 the continuous interval reaches z=3/4; the new clipping atom is at the maximum feasible z, so its addition is a rightward stochastic shift. Above m2, both the continuous component and the atom weight move the law right. Across the two lower strips no atom is present. Combining with part 1 proves the claim for all ordered interior m,m' (transitivity across breakpoints).

## Corollary — cross-price positive dependence

For all bounded nondecreasing measurable functions u and v,

  Cov(u(M),v(Z)) >= 0.

In particular Cov(M,Z)>=0 (both are bounded). Indeed, H(m)=E[v(Z)|M=m] is nondecreasing by the theorem, and Cov(u(M),H(M))>=0 by the elementary covariance identity with two independent copies of M. This yields positive quadrant dependence of (M,Z) as an additional consequence. No claim of complete multivariate total positivity is made.

## Exact non-exponential example and finite reproduction

Take f(a) proportional to a and g(b) proportional to b, strictly positive and log-concave on their positive price intervals. This is not an exponential tilt in either coordinate.

A direct exact Fraction polynomial integration over the clipping region a>=a_c(b) gives

  Pr(Z=3/4) = 109942873 / 241690050.

For verification, the unnormalized clipping numerator is
integral_(b=7/16)^(57/128) (b/2) [ (49/64)^2 - ((77+6b)/105)^2 ] db,
and the unnormalized total weight is
[(49/64)^2-(3/4)^2]/2 * [(57/128)^2-(7/16)^2]/2.

An independent standard-library exact rational verifier checks: the price-box inversion at interior rational points, support breakpoints, the exact clipping ratio, and 13,485 pairwise conditional-CDF inequalities for 30 rational m-values and 31 rational z-thresholds. That test is regression only; the universal theorem follows from the preceding analytic proof.

Scientific status and limitations: AUTHOR_PROVED / EXACT_FRACTION_EXAMPLE_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. The native original-index optimality is inherited and remains unreviewed. This is price-prior postprocessing, not new native Bellman optimization. No formal task publication, authenticated CLAIM, Result, Review or Activity is represented by this note.

Next scientific directions: (1) find a sharp condition weaker than product log-concavity using an inequality coupling the continuous fiber's TP2 cross-ratio and its clipping atom, and supply explicit non-log-concave stable examples; (2) continue the original-index native Bellman fan below z=11/16, preserving frozen input and native observer types.