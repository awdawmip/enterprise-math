# EC49FTA — exact BRC16943 two-switch price fan beyond the earlier sharp a-boundary

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_PRIMARY_23_VERTICES / INDEPENDENT_2_ANCHORS / NOT_REVIEWED.
Continuity: EC49FSZ PR #2747 (head 8661779a1f85975c9fc79159aea310aee919516b). Scientific input remains frozen at enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. P000 and ACTIVE worldview unchanged. The three **price variables** below are not three native spatial dimensions.

## Theorem

The original BRC16943 identification problem has 310 configurations, 141 distinguishable **named joint-response profiles** with uniform prior, and 228 original physical observations. Let t>0 be the regular observation price. Physical q32, q34 and q140 have costs (1-a)t, (1-b)t and (1-z)t; all other observations have cost t. An admissible decision tree must correctly identify each of the 141 original named profiles by original physical observation indices and their response values. Write D(a,b,z)=141V(a,b,z)/t for the unrestricted optimal aggregate cost and S(a,b,z)=D(b,a,z) for swapped q32/q34 discounts.

For **every real** triple in the closed prism

    133/246 <= a <= 9/16,  7/16 <= b <= 57/128,  1/2 <= z <= 9/16,

the exact unrestricted minima are

    D(a,b,z) = min(D1,D3),
    D1=319-18a-75b-141z,
    D3=316-141a-43b-30z;

    S(a,b,z) = min(P,C),
    P=315-141a-10b-77z,
    C=323-89a-12b-141z.

The exact moving strategy switch surfaces are

    z_D(a,b)=(3+123a-32b)/111,  D1=D3;
    z_S(a,b)=(4+26a-b)/32,     P=C.

D3 is better for z<=z_D and D1 for z>=z_D; P is better for z<=z_S and C for z>=z_S. The comparison is restricted to the closed prism when a switch surface falls beyond a face. The sharp bounds are

    99683/15744 <= D-S <= 4973/444.

The lower endpoint occurs at (a,b,z)=(133/246,57/128,277277/503808), also at the corresponding top-face point z=9/16. The upper endpoint occurs at (9/16,7/16,931/1776). Therefore D-S is strictly positive at every point in this prism.

This fills a nonempty three-dimensional portion past the a=133/246 sharp limit of the *previous single-direct-plane formula*, by introducing a new direct-policy cell rather than extrapolating the old formula.

## Native policy witnesses and exact feasibility

Across all 141 original named-response rows, the complete physical observer-tree usage vectors (total observations, q32 uses, q34 uses, q140 uses) are:

    D1: (319,18,75,141)
    D3: (316,141,43,30)
    P:  (315,10,141,77)   [swapped price convention]
    C:  (323,12,89,141)  [swapped price convention]

D1, P and C retain the full original-index tree witnesses in the EC49FSZ frozen evidence archive. D3 was reconstructed in this round by unrestricted native Bellman at the exact point (9/16,7/16,931/1776), and its entire tree is in this round's self-contained evidence archive. All four trees have been replayed on 141/141 actual named profiles using the 228 original observer response vectors; every leaf equals its source row, every branch uses the real response, and no observer index repeats on a single path. These feasible trees produce the four displayed affine cost planes and yield the global **upper bounds**.

## Full continuous-domain optimality proof

For any fixed legal tree T, normalized total cost is the affine function U(T)-aN32(T)-bN34(T)-zN140(T), or the corresponding physical-index-swapped formula for S. The unrestricted optimum is the pointwise minimum over the finite collection of legal trees, and hence is a jointly concave, piecewise-affine function of (a,b,z).

Let L be a feasible tree's affine cost and K a convex polyhedron. If exact unrestricted Bellman agrees with L at every vertex of K, then at each x=Σλ_i v_i in K, concavity gives F(x)>=Σλ_iF(v_i)=Σλ_iL(v_i)=L(x). The feasible witness supplies F(x)<=L(x); hence equality at all real points in K.

Cut the stated price prism by the D equality plane 3+123a-32b-111z=0, producing the two convex D strategy cells. Enumerate the intersections of every triple among the six rectangular-face equations and the D plane, retaining feasible distinct intersections. The union of the D-cell vertices consists of **11** exact rational points. Unrestricted Bellman across **all 228** original observers matches min(D1,D3) at **every one of 11** points.

Perform the same construction with the S equality plane -8-52a+2b+64z=0. Its two convex S cells have **12** distinct exact vertices. The independently evaluated swapped-price unrestricted Bellman matches min(P,C) at **every one of 12** points. All 23 input triples, rational Bellman values, and formula expectations are in the accompanying certificate CSV. The preceding interpolation argument proves the theorem for every real parameter in the complete prism.

To certify the sharp D-S extrema, cut the prism by **both** D and S planes. The resulting arrangement has **15** distinct feasible rational vertices; D-S is affine on each closed chamber, so its global extrema occur in this finite set. Exact enumeration produces the quoted sharp rational bounds and attainment coordinates. Fractions, integer-scaled Bellman and determinant arithmetic are exact; no floating point fitting or parameter sampling is used in the proof.

A separate original-94-family decoder and independent Bellman implementation recalculated two load-bearing points: for direct pricing at (9/16,7/16,931/1776), value 14959/74; for swapped pricing at (133/246,57/128,277277/503808), value 96699527/503808. Both match the primary 228-physical-observer native solver and the formula. Independent coverage is **2 of 23** anchors; primary exact coverage is **23 of 23**.

## Reproduction, scope, and next frontier

The self-contained archive EC49FTA_NATIVE_TWO_SWITCH_3D_PRICE_FAN_EVIDENCE_20261118.tar.xz contains the 11MB pinned raw input pair, native 228-observer solver, separate raw-94 independent implementation, all four full named trees, 23-anchor result JSON, exact verifier, source-and-tree SHA256 manifest, primary logs and independent recomputation log. The verifier provides rational geometry, original tree replays, exact native Bellman reruns (in bounded batches), and independent 94-family checks. The single long 23-anchor process exceeded a tool execution limit after 13 calls; remaining 10 swapped anchors were completed in two smaller runs and checked against the same exact certificate.

No formal Result/Review admission or live CLAIM is asserted by this portable scientific artifact. The research result is a complete author proof with exact finite native certificates and partial independent implementation checks. Current canon/task-owner/activity bindings must be assessed separately.

**Next:** determine new native strategy planes for a>9/16 in the same z-neighborhood. Use exact counterexamples and original-index named decision-tree witnesses to locate the next transition; do not extrapolate this four-policy envelope beyond the stated prism.