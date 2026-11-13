# R749SNK — Exact zero-calibration-penalty ray at Walsh moment 3/10

Date: 2026-11-14. Scientific source: R749SNJ at awdawmip/enterprise-math@c597b3214ffa827953ddb4b3fa40d98cc961b865. Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. This auxiliary Walsh observation model is not asserted to model native signed-Port/X6/V29/V39 events. P000 remains unchanged.

## Exact theorem

Let G=(F_2)^4 and chi_m(x)=(-1)^popcount(m&x). Retain the ten moments B={3,5,6,7,9,10,11,12,13,14}. Fix m_3=t and m_12=3/10, with the other eight retained moments zero. Let F_(t,3/10) denote the compatible probability fiber on the sixteen states. For total variation TV(mu,q)=sum_x |mu(x)-q(x)|/2 define:

    rho(t,s)     = min_{q probability} max_{mu in F_(t,s)} TV(mu,q),
    rho_cal(t,s) = min_{q in F_(t,s)} max_{mu in F_(t,s)} TV(mu,q).

For EVERY REAL t in [1/2,1],

    rho(t,3/10) = rho_cal(t,3/10) =
         27/80 + t/8       if 1/2 <= t <= 7/10,
         3/5 - t/4         if 7/10 <= t <= 1.

The pieces meet at t=7/10, radius 17/40. The radius rises from 2/5 at t=1/2 to 17/40 and falls to 7/20 at t=1. In particular the zero-calibration-penalty point of R749SNJ belongs to an exact closed segment of zero penalty.

## Walsh parameterization and symmetry

Set A=chi_3, D=chi_12, AD=chi_15, P=chi_1, AP=chi_2, Q=chi_4, DQ=chi_8. The unique inverse-Walsh parameterization of every compatible law is

    mu_(t,h,u,v,w,z)(x)
      = [1 + t A(x) + (3/10)D(x) + h AD(x)
           + u P(x) + v AP(x) + w Q(x) + z DQ(x)]/16,

with sixteen nonnegative masses. All other retained character coefficients are zero by definition.

Translations of x by masks 3 and 12 preserve both nonzero retained moments, preserve the zero retained moments, and independently flip the unretained coefficient pairs (P,AP) and (Q,DQ). Averaging any decoder over this order-four translation group cannot increase the maximum TV error on the invariant source fiber, by convexity and group invariance; it also preserves calibrated status. Therefore the unrestricted minimax problem has a symmetric optimal decoder of the form

    q_(tau,sigma,eta)(x)=[1+tau A(x)+sigma D(x)+eta AD(x)]/16.

Calibrated symmetric decoders satisfy tau=t and sigma=3/10.

## Constructive calibrated upper bounds

Use the following explicit probability laws:

    q_L(t,x)=[1+t A(x)+(3/10)D(x)]/16
             for 1/2 <= t <= 7/10;

    q_R(t,x)=[1+t A(x)+(3/10)D(x)+(t-7/10)AD(x)]/16
             for 7/10 <= t <= 1.

Every mass of each q is affine in t and nonnegative at its interval endpoints. Therefore the centers are nonnegative and normalized for every intervening real parameter and retain all prescribed moments.

For a rigorous upper certificate, consider the joint six-variable probability polytope in (t,h,u,v,w,z) with sixteen atom nonnegativity constraints and two parameter bounds. Each is bounded and full dimensional. Every vertex is a unique solution of six linearly independent active constraints. The attached checker enumerates all C(18,6)=18564 six-facet combinations per interval with integer Bareiss elimination and exact Fraction arithmetic, discards singular/infeasible solutions, and deduplicates rational vertices.

For either affine center and claimed affine radius, the function

    (t,h,u,v,w,z) -> TV(mu_(t,h,u,v,w,z),q(t)) - radius(t)

is convex. Its maximum over the joint compact polytope is achieved at a vertex. Every vertex was checked with exact rational comparisons:

| Parameter interval | Combinations | Nonsingular | Feasible bases | Distinct vertices | Tight | Violations |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [1/2,7/10] | 18564 | 9536 | 844 | 60 | 20 | 0 |
| [7/10,1] | 18564 | 9536 | 1108 | 16 | 6 | 0 |

This proves the displayed calibrated upper bounds for ALL real t on the stated intervals, not just rational samples.

## Explicit lower-bound witnesses (all decoders)

For the first segment take

    W_L(t)=(h,u,v,w,z)=(0,-7/10,-t,-3/10,-3/10),
    E_L={3,5,7,9,11,13,14,15}.

For the second segment take

    W_R(t)=(h,u,v,w,z)=(t-7/10,-7/10,-7/10,t-1,t-1),
    E_R={3,5,6,7,11,13,14,15}.

Substitute the W families into the inverse Walsh formula to obtain distributions. At both endpoints of each interval all sixteen probabilities are nonnegative; affine dependence then proves feasibility throughout each interval.

Each event E_L and E_R contains exactly eight of sixteen states and satisfies

    sum_{x in E} A(x) = sum_{x in E} D(x)
                     = sum_{x in E} AD(x) = 0.

Hence q_(tau,sigma,eta)(E)=1/2 for ANY symmetric decoder and the corresponding event. Direct exact substitution gives

    mu_WL(t)(E_L)-1/2 = 27/80 + t/8,
    mu_WR(t)(E_R)-1/2 = 3/5 - t/4.

Since TV(mu,q) >= mu(E)-q(E), these witnesses lower bound the maximum error of every symmetric decoder, including calibrated ones. Symmetry averaging reduces the original free-decoder problem to symmetric decoders without changing its optimum. Thus the lower bounds hold for the original unrestricted and calibrated problems. Matching the upper certificates completes the theorem.

## Verification and continuation

Reproduce with Python standard library only:

    python research_notes/portable_direct/R749SNK_CALIBRATION_RAY_EXACT_CHECK.py

Compare complete stdout JSON with research_notes/portable_direct/R749SNK_CALIBRATION_RAY_RESULTS.json. The script checks exact vertex completeness for both joint polytopes, event character-sum cancellations, source nonnegativity at endpoints, exact witness mass identities, and matching radius at the transition.

Together with R749SNJ, this establishes asymmetric behavior along two coordinate sections through (t,s)=(1/2,3/10): the earlier t=1/2 interval has positive calibration gap except at s=3/10; this new s=3/10 section has zero gap throughout t in [1/2,1]. Next: find the exact two-parameter zero-gap region and its boundary; investigate t<1/2 at s=3/10; separately search for a typed provenance-preserving native future-observer mapping. The exact theorem is an author-side mathematical certificate, not an independent review or a claim of native model correspondence.


## Exact sign-and-swap orbit (corollary)

The fixed set B consists exactly of all two-bit and three-bit masks on four bits. Hence B is invariant under all permutations of the four bit positions. Exchanging the first two bit positions with the last two sends masks 3 and 12 into each other; relabeling the sixteen states preserves TV and the fiber constraints with t,s exchanged. Moreover state translation by bit mask 1 changes the sign of chi_3 but not chi_12, while translation by bit mask 4 changes the sign of chi_12 but not chi_3. Translation preserves the zero values of all other retained moments.

Therefore both minimax values satisfy, on the complete nonempty domain,

    rho(t,s)=rho(|t|,|s|)=rho(s,t),
    rho_cal(t,s)=rho_cal(|t|,|s|)=rho_cal(s,t).

The theorem above consequently supplies the same exact piecewise zero-gap formula (with t replaced by |t|) on all signed horizontal segments

    |s|=3/10, 1/2<=|t|<=1,

and the swapped formula (with t replaced by |s|) on all signed vertical segments

    |t|=3/10, 1/2<=|s|<=1.

This is a group-isomorphism corollary of the original source model, not a new numerical extrapolation.
