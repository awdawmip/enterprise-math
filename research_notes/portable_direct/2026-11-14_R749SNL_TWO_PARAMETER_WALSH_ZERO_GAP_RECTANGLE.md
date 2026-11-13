# R749SNL — Two-dimensional exact zero-calibration-penalty rectangle

Date: 2026-11-14. Direct mathematical continuation of R749SNK and R749SNJ. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Scope: auxiliary 16-state Walsh observation model. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED; no native signed-Port/X6/V29/V39 correspondence asserted, no change to P000.

## Full all-real-parameters theorem

Let G=(F_2)^4, chi_m(x)=(-1)^popcount(m&x), and retain Walsh moments indexed by B={3,5,6,7,9,10,11,12,13,14}. Set m3=t and m12=s, with all eight other retained moments zero. Let F_(t,s) denote the compatible probability distributions and let TV(mu,q)=sum_x |mu(x)-q(x)|/2. Define the unrestricted and calibrated minimax prediction radii:

    rho(t,s)=min_{q probability} max_{mu in F_(t,s)} TV(mu,q);
    rho_cal(t,s)=min_{q in F_(t,s)} max_{mu in F_(t,s)} TV(mu,q).

**Theorem. For every pair of real numbers (t,s) in**

    3/5 <= t <= 13/20,       1/4 <= s <= 7/20,

**the exact radii coincide and equal**

    rho(t,s) = rho_cal(t,s) = (3+t-s)/8.

This is an exact two-dimensional region with nonempty interior, not merely a one-dimensional parameter ray or finite grid. It contains points on both sides of the former s=3/10 crossing and includes t+s=1 on its upper-right boundary. The optimal calibrated decoder is explicitly

    q_(t,s)(x)=[1+t*chi_3(x)+s*chi_12(x)]/16.

The rectangle has t+s<=1, so q is a nonnegative normalized law and satisfies every retained moment exactly.

## Symmetry reduction and universal lower bound

Use characters A=chi_3, D=chi_12, AD=chi_15, P=chi_1, AP=chi_2, Q=chi_4, DQ=chi_8. The exact fiber has unique parameterization

    mu_(t,s,h,u,v,w,z)(x)
       =[1+t A(x)+s D(x)+h AD(x)+u P(x)+v AP(x)+w Q(x)+z DQ(x)]/16

with all sixteen probabilities >=0. Translation of the state labels by masks 3 and 12 preserves the fiber. Averaging a candidate decoder over this four-element group does not increase its worst-case total-variation loss, by TV convexity and fiber invariance. Therefore an unrestricted optimal decoder may be taken in the three-coefficient form

    q_(tau,sigma,eta)(x)=[1+tau A(x)+sigma D(x)+eta AD(x)]/16.

Consider the affine source witness

    W_(t,s)=(h,u,v,w,z)=(0,s-1,-t,-s,-s)

and the event

    E={3,5,7,9,11,13,14,15}.

At the four corners of the parameter rectangle, every source atom produced by W is nonnegative. As every mass is affine in (t,s), W supplies a compatible source distribution throughout the rectangle (each point is a convex combination of four corners). The eight-element E has vanishing character sums for A,D,AD, so every invariant q has q(E)=1/2. Direct substitution gives

    mu_W(t,s)(E)-q(E)=(3+t-s)/8.

Because TV(mu,q)>=mu(E)-q(E), the right-hand expression is a lower bound for the unrestricted worst-case radius. The translation averaging argument makes this valid without requiring the original decoder to be invariant. It is automatically a lower bound for calibrated decoding as well.

## Constructive all-real upper bound via a complete exact vertex certificate

The explicit q_(t,s) from the statement is calibrated; to establish its worst-case TV <= (3+t-s)/8, introduce seven joint variables (t,s,h,u,v,w,z), and impose the sixteen source-atom nonnegativity inequalities together with four parameter-rectangle endpoint inequalities. The resulting feasible set is bounded, full-dimensional and polyhedral.

Every vertex is the unique solution of seven linearly independent active facets. The attached standard-library Python checker enumerates ALL C(20,7)=77520 seven-facet combinations. Each candidate is solved with exact integer Bareiss elimination, exact infeasibility checks and Fraction reconstruction, then duplicate feasible vertices are removed.

The function

    (t,s,h,u,v,w,z) ->
       TV(mu_(t,s,h,u,v,w,z),q_(t,s)) - (3+t-s)/8

is convex on this joint polytope, since both q and mu depend affinely on its seven variables and the subtracted radius is affine. A convex function achieves its maximum over a compact polytope at some vertex. The exhaustive exact output is:

| Certificate measurement | Exact output |
| --- | ---: |
| Potential 7-facet sets | 77,520 |
| Nonsingular sets | 30,208 |
| Feasible bases | 1,444 |
| Distinct joint vertices | 150 |
| Vertices attaining the radius | 40 |
| Violations of the upper bound | 0 |

Therefore the calibrated q is an exact upper witness for **all real (t,s) in the entire rectangle**. Combined with the preceding universal event lower witness, this proves both equalities.

## Reproducibility and relation to preceding work

From repository root run:

    python research_notes/portable_direct/R749SNL_TWO_PARAMETER_RECTANGLE_EXACT_CHECK.py

The result JSON at research_notes/portable_direct/R749SNL_TWO_PARAMETER_RECTANGLE_RESULTS.json records the entire exhaustive coverage counts and exact theorem. The source code uses only Python standard library, integer arithmetic and Fraction; it verifies all 7-facet combinations, rational atom positivity, four-corner witness feasibility, Walsh event cancellations and exact probability/radius equalities.

R749SNJ identified a single zero-penalty point on t=1/2. R749SNK established a one-dimensional zero-penalty ray at s=3/10, 1/2<=t<=1. R749SNL proves that this phenomenon extends into a genuinely two-dimensional open set with an explicit affine radius. The maximal connected two-parameter zero-penalty region, exact polygonal/curved boundary, and native provenance-preserving future-observer transfer remain open for later research and independent review.
