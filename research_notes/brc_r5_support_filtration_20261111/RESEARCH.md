# R5: exact support filtration, source-3 five-mask census and connectivity threshold

Date: 2026-11-11 (Asia/Shanghai). Author-side result: Researcher-ID `EM-DIRECT-2CB28A / TASK_RESEARCH`; Research-Activity-ID `RA-8A53F787F030D7F32FF5EAA5`.
Source session registration: `a34388855bee7ed2873033f15b679aa69874caea`; no formal R5 CLAIM, Result or independent review.
Scientific lineage is unchanged from R5 PR #2063: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.
Foundational witness: R5 PR #2017. Prerequisite four-mask exact theorem: PR #2063, commit `9001105df972b214e8a52571aa4b175fc34cfcca`. The original `VERIFY_FOUR_MASKS.py` from that commit is reproduced verbatim here as `r5_prior_four.py`; its original blob SHA is `c316620c817b1abff6658b7f2d673f146141b28b`.

## Definitions and exact domain

Work in the **one frozen auxiliary seven-ratio P/Q–BRC Blackwell observer fiber**, with integer ratios
[
R=(2,10,15,20,25,30,38).
]
There are 30 labeled arcs: 28 dynamic arcs ((i,j)), (i=0,ldots,6), (jin{1,2,3,5}), and two fixed positive singleton arcs ((0,0),(6,6)). Let (E^0) be the positive exact rational witness from R5 PR #2017, reproduced by `r5_prior_four.py`. Define
[
F={Einmathbb R_{geq0}^{30}: CE=CE^0},
]
where (C) records seven target marginal masses, seven source marginal masses, and seven source first moments. Its rank is 15; the two singleton arcs are fixed. Equivalently dynamic masses (xinmathbb R_{ge0}^{28}) satisfy (Ax=b) with (Ainmathbb Z^{15	imes28}), (mathrm{rank}A=13). All marginal and first-moment right-hand sides are frozen at (E^0).

For (Ksubseteq{0,ldots,6}), define the face
[
F_K={Ein F:E_{i,3}=0quad(i
otin K)}.
]
Let (S_m={Ein F:|{i:E_{i,3}>0}|leq m}). Here support means **positive labeled branch mass**, retaining full source-target provenance. (F_K) is the zero-set face of a nonnegative linear functional. A mask is called *strictly realized* when a point of (F_K) is positive on every arc allowed by (K).

## Theorem: exact filtration of source-3 branch support

For the above fixed rational fiber, all realized (m)-target support masks, their exposed-face dimensions, and the number of connected components of the **support-at-most-(m) locus** are:

| m | Number of strictly realized masks of size m | Dimension of each corresponding face | Number of components of S_m |
|---|---:|---:|---:|
| 1,2,3 | 0 | — | empty |
| 4 | 3 | 12 | 3 |
| 5 | 9 | 13 | 3 |
| 6 | 6 | 14 | 1 |
| 7 | 1 | 15 | 1 |

The three four-target masks are exactly ({1,3,4,6}), ({2,3,4,5}), ({2,3,4,6}), as certified by PR #2063. **All nine** strictly realizable five-target masks, sorted, are

[
egin{aligned}
&01346,;02345,;02346,;02356,;12345,\
&12346,;12356,;13456,;23456.
end{aligned}
]

The other twelve five-target masks are exactly
[
01234,;01235,;01236,;01245,;01246,;01256,;01345,;01356,;01456,;02456,;03456,;12456.
]
Each has an explicit exact rational Farkas separator (yinmathbb Q^{15}), satisfying (y^	op a_kge0) for every column allowed by the mask but (y^	op b<0). All vectors are specified in `VERIFY_SUPPORT_FILTRATION.py` and checked against *every* allowed column.

Exactly six six-target masks are strictly realizable: all size-six subsets **containing target 3**. The remaining mask (012456) has a rational Farkas certificate inherited from the excluded five-mask (12456). The extra target-0 column has strictly positive dual pairing (18/35), so adding it does not invalidate the separation.

For (S_5), the nine five-face components have sizes **7,1,1** in the five-face incidence graph. The two singleton components are exactly (F_{02356}) and (F_{12356}), both 13-dimensional. Every member of the other seven five-faces contains an existing feasible four-target subface. No (S_5)-continuous path connects either exceptional five-face to the other seven or to the other exceptional face.

For (S_6), all six 14-dimensional six-faces are connected through nonempty intersections equal to feasible five-faces. Their union contains every point of (S_6), and (S_6) is connected.

**Optimal support peak between four-support components.** Any continuous path in (F) from one of the three disjoint four-face components to another has a point with at least five positive source-3 branches. This bound is attained **for each pair**: the path via the four-support witnesses on (A={1,3,4,6}), (C={2,3,4,6}), and (B={2,3,4,5}), interpolating (A	o C	o B), has at most five positive branches throughout. In particular, a direct (A	o B) convex interpolation would use six, while the two-segment route reduces the peak to five.

## Exact proof and certificate strategy

1. **Carry forward the complete lower layer.** Run the byte-identical prerequisite file `r5_prior_four.py`. Its standard-library `Fraction` checker proves no 1-,2-,3-support masks are feasible; exactly the three four-support masks above admit strictly positive rational full transfers with 27 positive arcs; four locally feasible alternatives have exact dual exclusions. The rank of the full dynamic constraints is 13.

2. **Nine strictly positive five-support primal certificates.** Seven feasible five-masks contain at least one of the three four-masks. For each such four-mask the prerequisite provides a full-rank set of 13 pivot columns and an exact rational interior point of its 12-dimensional face. Add the unique fifth source-3 target with a sufficiently small positive rational mass and correct the same 13 pivot columns by exact Gauss–Jordan elimination. The original pivot masses remain strictly positive by continuity, and the checker finds an explicit dyadic rational step by finite search and verifies all 15 original dynamic equations exactly. For the two exceptional masks, which contain no feasible four-mask, the checker supplies entirely new rational points with nonpivot mass (t=1/1000) and pivot sets:
[
egin{array}{c|l}
02356 & (1,16,17,19,0,8,25,27,20,4,11,14,2)\
12356 & (16,1,17,0,19,8,27,25,4,20,15,11,2).
end{array}
]
The column indices use the 28 dynamic arcs ordered by source (1,2,3,5), then target (0,dots,6). Exact solving yields all 26 permitted dynamic arc masses positive. The restricted observer rank remains 13 (equivalently the original 21×28 full observer rank 15 after adding fixed singleton arcs), so all nine five-faces have dimension (26-13=13).

3. **Twelve exact dual exclusions.** The checker contains 12 explicit 15-component rational vectors `DUALS`. It enumerates all 21 five-masks, proves nonnegativity of each dual against every allowed dynamic arc, and confirms strict negative pairing with the **frozen** right-hand side. Consequently precisely nine are feasible, with no floating-point feasibility inference.

4. **Six-support completeness.** For each size-six mask containing 3, select a previously verified feasible five-mask within it, add the sixth source-3 edge using that five-face's full-rank 13-pivot basis, and check all 27 permitted dynamic coordinates positive. Thus each of these 14-dimensional exposed faces exists. The sole other six-mask (012456) is excluded by the five-mask (12456)'s exact vector; the newly enabled source-3 target-0 column pairs to (18/35>0). All seven size-six masks are thereby classified.

5. **Component count by exact face intersections.** Nonnegative support constraints give (F_Kcap F_L=F_{Kcap L}). In the five-face incidence graph, two distinct size-five faces meet only if their intersection is a valid ≤4 support mask; for the three four-masks this gives one component of seven faces, and the remaining exceptional faces have no such lower mask, hence are isolated. Each five-face is compact convex and nonempty. A connected component of the finite union of such compact faces is exactly a graph component because distinct graph components are disjoint compact subsets with positive separation. In the six-face graph, any two size-six masks intersect on a size-five mask; those intersections are nonempty exactly when the corresponding five-mask is feasible. The exact graph has one connected component, and every five-face is included in a six-face, so (S_6) is connected.

6. **Minimax support bridge.** The earlier theorem establishes the lower bound (5) because (S_4) has three disconnected components. The explicit positive rational four-face witnesses of (A,C,B) establish the upper bound: convex interpolation preserves (CE=CE^0), and both unions (Acup C), (Ccup B) have size five. This proves the sharp minimax value.

All claims concern the fixed auxiliary P/Q–BRC observation fiber. The full 30-branch representation and the unobserved source-target correlation directions are retained; in particular the (S_5) component structure is not inferred from marginal-only reductions. The result supplies a branch-support transition certificate; it makes no statement about native six-axis rotation dynamics or physical time evolution.

## Verification and provenance

Run under Python 3 standard library:
```
python3 VERIFY_SUPPORT_FILTRATION.py
```
in the same folder as the reproduced preceding verifier `r5_prior_four.py`. The expected final marker is
`PASS_EXACT_R5_SUPPORT_FILTRATION_4_TO_7_AND_NINE_FIVE_MASKS`.
The program checks the four-mask inherited proof, each rational primal, exact (Ax=b), strict positivity and ranks, 12 dual inequalities, the excluded six-mask, face incidence and support-peak construction. The research derivation and corresponding checker logic were executed locally with exact `Fraction` arithmetic. The prior remote verifier is byte-identical to the earlier checked version; the new remote script was content-readback verified at publication. The new remote script's execution in its remote file form is a reproducibility task and is not separately claimed as completed.

Status: author-side theorem and exact finite verification, formal Source scientific Result and independent review pending. No shared R5 task owner was claimed.

## Next concrete research questions

Compute the minimum (K_{2,3})-six-edge circuit word length of an actual **five-support** bridge direction between the faces (A,C,B), using the 15-dimensional repair coordinates from PR #2021; check whether a one- or two-atom step can realize the optimum peak with nonnegative intermediate transfers. Separately classify adjacency inside the 11-dimensional smallest common face of the 49 four-residual extreme edges from PR #2059 and determine which non-sharp extreme edges connect its nine tree components. For the exceptional 13-dimensional faces (F_{02356}) and (F_{12356}), compute explicit first admissible 14D incidences and their exact circuit decomposition.
