# R749SNM — Exact zero-calibration-penalty Walsh polygon

Date 2026-11-14. Scope: 16-state auxiliary Walsh source model. Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. This is a continuation of R749SNL, not an assertion of native X6, signed-Port, V29 or V39 correspondence or a change of P000.

## Statement and precise scope

Let G=F_2^4, chi_m(x)=(-1)^popcount(m&x), and let the retained set of Walsh moment indices be B={3,5,6,7,9,10,11,12,13,14}. Set m_3=t, m_12=s and all eight other retained moments to zero. Let F(t,s) be the corresponding nonempty probability fiber; TV(mu,q)=sum_x |mu(x)-q(x)|/2, and define

    rho(t,s)     = min_{q probability} max_{mu in F(t,s)} TV(mu,q)
    rho_cal(t,s) = min_{q in F(t,s)} max_{mu in F(t,s)} TV(mu,q).

**Theorem.** For every real (t,s) in the closed convex polygon

    P={(t,s): t>=3/5, s<=7/20, t+s<=1, t+4s>=8/5}

the two exact minimax radii agree:

    rho(t,s)=rho_cal(t,s)=(3+t-s)/8.

Its cyclic vertices are (3/5,1/4), (4/5,1/5), (13/20,7/20), (3/5,7/20). The entire R749SNL rectangle [3/5,13/20] x [1/4,7/20] is contained in P. The old area is 1/200 and the new area is 11/800, i.e. 11/4 times the old area. Maximality of P among all zero-penalty chambers is not asserted.

## Exact parameterization and calibrated upper witness

Use characters A=chi_3, D=chi_12, AD=chi_15, U=chi_1, AU=chi_2, V=chi_4, DV=chi_8. Every compatible law is uniquely

    mu_(t,s,h,u,v,w,z)(x)
      =[1+t A(x)+s D(x)+h AD(x)+u U(x)+v AU(x)+w V(x)+z DV(x)]/16,

with its 16 atom masses nonnegative. On P, t>=0, s>=0 and t+s<=1. Therefore

    q_(t,s)(x)=[1+t A(x)+s D(x)]/16

is a probability distribution preserving all ten retained moments.

## Lower certificate valid for unrestricted prediction

State-label translations by xor masks 3 and 12 preserve the fiber: A, D, AD are invariant, whereas the other four unconstrained characters change signs and average out. Averaging any candidate decoder over this order-four group cannot raise its worst-case TV distance by convexity and fiber invariance. Therefore an unrestricted optimal decoder may be assumed of form

    q(x)=[1+tau A(x)+sigma D(x)+eta AD(x)]/16.

Set h=0, u=s-1, v=-t, w=-s, z=-s and denote the resulting source by W(t,s). Its 16 atom probabilities are nonnegative at all four vertices of P (checked with exact fractions). They are affine in (t,s), so W(t,s) remains feasible over their entire convex hull. For the eight-element event E={3,5,7,9,11,13,14,15}, the A,D,AD character sums over E are all zero, implying q(E)=1/2 for every invariant q. Direct substitution yields

    W(t,s)(E)-q(E)=(3+t-s)/8.

The variational event inequality TV(mu,q)>=mu(E)-q(E) then proves rho(t,s)>=(3+t-s)/8; it is also a lower bound for rho_cal.

## Upper certificate: complete all-real joint-polytope check

Let y=20(t,s,h,u,v,w,z). The joint source/parameter polytope in seven variables is cut out by 20 integer halfspaces M*y>=b: 16 character rows (A,D,AD,U,AU,V,DV) with right sides -20, plus the four polygon rows

    row ( 1, 0,0,0,0,0,0) >=  12
    row ( 0,-1,0,0,0,0,0) >=  -7
    row (-1,-1,0,0,0,0,0) >= -20
    row ( 1, 4,0,0,0,0,0) >=  32.

The joint polytope is bounded, full-dimensional and nonempty, so every vertex is an intersection of seven independent facets. The attached standard-library Python checker enumerates exactly C(20,7)=77,520 active-facet subsets; solves every nonsingular integer linear system by Bareiss elimination with Fraction reconstruction; tests all inequalities exactly; and deduplicates exact rational vertices.

The certificate output reports: 39,520 nonsingular bases, 1,668 feasible bases, 126 distinct joint vertices, 32 vertices attaining equality, and **0 vertices violating** TV(mu,q_(t,s))<=(3+t-s)/8. The maximum exact vertex excess is 0.

The function

    (t,s,h,u,v,w,z) ->
       TV(mu_(t,s,h,u,v,w,z),q_(t,s)) - (3+t-s)/8

is convex, because both laws depend affinely on the seven variables and the radius term is affine. A convex function on a compact polytope is bounded above by its maximum over the vertices. Consequently this finite exhaustive *exact* certificate proves the upper inequality for every real parameter in P and every source in its fiber. Together with the lower event witness this proves the theorem.

## Reproduction, verification boundary, next question

Run: python research_notes/portable_direct/R749SNM_WALSH_POLYGON_EXACT_CHECK.py

The accompanying R749SNM_WALSH_POLYGON_RESULTS.json contains the raw exact-enumeration counts and statement. Both verification and the explicit lower witness use exact integers/Fraction, not floating-point samples. Independent scientific review remains open; formal Lean verification is not claimed.

Next: identify the maximal connected region or a polyhedral subdivision on which calibrated q remains minimax, distinguish a genuine optimal-radius phase boundary from the limits of this particular q certificate, and separately test native provenance-preserving future-observer transfer under the actual X6 type system.