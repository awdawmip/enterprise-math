# R5: exact triangle–quadrilateral fibers, affine indecomposability, and four-dimensional volume

2026-11-09 (Asia/Shanghai). Status: AUTHOR_DERIVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Source and scope

This author-side derivation continues Enterprise Math Draft PR #1861, immutable research commit 54f4abcb13b7453a29e66ed3421cbafa017e9e27, based on its irredundant seven-inequality representation of **one fixed seven-LR-node Blackwell marginal pair**. Source: PR #1859 at f63a0250714f2445e8b406754b85f26d983ec3a6. Keep its original scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Read current normative rules separately.

For arbitrary **positive real** a,b,d, define an abstract polytope Q(a,b,d) in (s,t,u,v) by the seven inequalities

    s>=0; t>=0; 13s+18t<=23a;
    u>=0; v>=0;
    18u-13v<=23b+13s;
    10v-5u<=23d+5t.

The fixed Blackwell instance has

    a=3997/690000
    b=170189123/37621284000
    d=8294919533/677183112000.

Here s=q1,t=q2,u=q3,v=q4. The previous verified 17-edge equations and omitted-edge positivity identify Q at these fixed values with **all** feasible Blackwell couplings of that specific marginal pair. The arbitrary-positive-parameter theorem below is an abstract seven-facet extension, not a claim that arbitrary a,b,d correspond to physical marginal pairs.

## Theorem I: analytic fiber decomposition and exactly twelve vertices

Let L1=23a/13, L2=23a/18. The projection T to the first two coordinates is the closed triangle with vertices (0,0), (L1,0), (0,L2). For every (s,t) in T put B=23b+13s and D=23d+5t. Both are positive. The fiber in (u,v) is the convex quadrilateral with four ordered vertices

    F0=(0,0),
    F1=(B/18,0),
    F2=((10B+13D)/115,(5B+18D)/115),
    F3=(0,D/10).

**Proof.** The slanted boundary equations 18u−13v=B and 10v−5u=D have determinant 115>0 and meet at F2. Together with u,v>=0 they enclose exactly the displayed four distinct intersections. Each satisfies the other halfspaces; there is no feasible triple intersection of fiber boundaries for positive B,D. The decomposition and vertices are therefore valid for **every real** (s,t) in T.

Each 4D vertex needs four linearly independent active facet equations. At most two can come from a quadrilateral fiber. Consequently at least two base-triangle facets must be active, placing (s,t) at one of its three vertices, while (u,v) lies at one of the four fiber vertices. Conversely each of the 12 pairs has four independent active facets, proving exactly twelve full vertices for every a,b,d>0. This gives an analytic proof of the combinatorial triangle×quadrilateral result and reobtains the fixed-instance 13-positive-edge vertices of PR #1861.

## Theorem II: the product is combinatorial but never affine

The facet normals of the **four six-vertex facets** are, in the coordinates (s,t,u,v),

    (0,0,1,0)
    (0,0,0,1)
    (-13,0,18,-13)
    (0,-5,-5,10).

Their exact determinant is **65**, so they span R^4. For an affine image of a triangle×planar-quadrilateral product, the four facets that each contain six vertices arise from triangle×edge, and their normals must lie in a common 2D dual subspace. Invertible affine maps preserve the dimension of the span of facet normals. Therefore **Q(a,b,d) cannot be affinely equivalent to a Cartesian product of a triangle and any planar quadrilateral** for any a,b,d>0. The fiber family is an actual affine twist, rather than two separable coordinate polytopes.

## Theorem III: fiber area, exact coordinate volume, and sharp fixed area bounds

By the four-vertex shoelace formula, the fiber area is exactly

    A(B,D)=(25B^2+180BD+117D^2)/20700.

Set s=L1 x, t=L2 y on the standard triangle x,y>=0, x+y<=1, giving B=23b+23ax, D=23d+(115a/18)y. Integrate A over the base using the elementary exact moments

    integral_triangle x^m y^n dxdy = m!n!/(m+n+2)!.

This produces the **complete positive-parameter quartic formula** for 4D Lebesgue volume in the declared (s,t,u,v) mass coordinates:

    Vol_4 Q(a,b,d) =
      (12167 a^2/90979200) *
      (2125 a^2 + 7200 ab + 17640 ad + 5400 b^2
       + 38880 bd + 25272 d^2).

For the fixed marginal pair this is the exact rational number

    17113607962497316638837165221
    /503876396283588297216000000000000000
    ≈ 3.39639008469560 × 10^(-8).

Area A is separately increasing in B>0,D>0. In the frozen instance it has its unique minimum at base (s,t)=(0,0). Its maximum occurs on the base hypotenuse x+y=1: there A(x,1−x) is a concave quadratic whose derivative is still positive at x=1, and hence positive over [0,1], yielding the unique maximum at (s,t)=(L1,0). Exact extrema:

    A_min = 1428755703638704652497/1993812900773932800000000
    A_max = 95175648542901379463/86687517424953600000000.

This coordinate volume is a computable polyhedral invariant **relative to the specified q-parameterization**, not an intrinsic native X6 spatial volume or a probability distribution.

## Verification, status, and next scientific unit

The accompanying VERIFY.py is a self-contained Python standard-library Fraction verifier. It checks 12 analytic frozen-instance vertices and all seven facet slacks; four active facets at each; exact shoelace area at base vertices and an interior base point; the true 4×4 normal determinant; the polynomial volume identity against independent simplex-moment integration at four exact positive rational triples; the frozen rational volume; and the frozen area extrema. EXACT_OUTPUT.txt records actual execution.

**Next discriminating action.** Find a physically lawful perturbation of the source and target marginals transverse to the saturated Phi=0 support face in PR #1859, and determine whether the derived fiber chart persists with new nonzero edges. Use exact linear constraints/dual prices to build a new 13/14-edge support chart or a certified neighboring obstruction. The universal all-physical 14-vs-15 edge question remains unresolved. This result has no formal Owner/CLAIM, Result, independent mathematical review, or canonical theorem admission by this artifact alone.
