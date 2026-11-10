# R5: the first-contact 14-edge sheet contains a four-dimensional transport face

Date: 2026-11-10 (Asia/Shanghai). Research status: author-side exact derivation and independent local rational reconstruction; mathematical review pending.

Frozen scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Direct predecessor: Draft PR #1954 at `6f01b6424cc5563db7976fa8131ef687c15091ca`; underlying center `z_c`, affine physical model, 21-row Blackwell system and ten forced arcs remain unchanged. This note uses BRC branch arcs as distinct positive transport channels, with the complete seven-statistic observer and original physical constraints. It does not introduce an additional native spatial axis or modify P000.

## Result: a four-dimensional 12-vertex transport face

At the exact legal physical contact `z_c=R*(-1,1,1,-1,-1,-1,-1,1)` with `R=49948501046391/3920403670319950000`, let `C` be the pinned rank-15 reduced Blackwell transfer matrix, `b(z_c)` its pinned right hand side, and let `P(z_c)={E>=0:C*E=b(z_c)}` in the 30 allowed transport arcs.

Let the ten forced arcs be

`F=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))`.

Set the common additional arc `a=(1,5)` and mutually exclusive optional groups

`G1=((2,1),(3,1),(4,1))`,
`G2=((3,2),(4,2))`,
`G3=((0,3),(2,3))`.

Let `U=F union {a} union G1 union G2 union G3` (18 arcs). The coordinate-support face `Q={E in P(z_c): E_e=0 for e outside U}` is four-dimensional and has exactly 12 vertices. Every vertex has precisely 14 positive arcs: all eleven common arcs `F union {a}`, and one arc chosen independently from each of `G1,G2,G3`. Every one of the `3*2*2=12` choices occurs as an exact positive rational solution.

Its seven facets correspond exactly to the seven optional-arc nonnegativity inequalities. Its vertex–facet incidence structure is that of the **combinatorial product**

`Delta_2 x [0,1] x [0,1]`.

The one-skeleton is `K3 Cartesian-product K2 Cartesian-product K2`, with 12 vertices, 24 edges, and degree four at every vertex. Thus the earlier twelve positive 14-arc supports form a single connected pivot family, with one-arc exchanges in three independent support-choice groups.

**BRC observer consequence:** the same seven-dimensional Blackwell marginal observation and the same legal physical strategy correspond to a four-dimensional family of distinct branch-preserving exact transfers. The choice-group *combinatorics* factor, but the underlying arc *masses* remain coupled: for instance the total mass in G1 takes three different exact rational values among the twelve vertices. This is a concrete nontrivial transport/observer fiber, rather than a new physical coordinate.

## Proof and finite evidence

The predecessor's full exact support enumeration covers all `binom(20,4)=4845` ten-forced-plus-four candidate supports: exactly 28 linear spans contain the contact; 12 admit strictly positive fourteen-arc solutions, the other 16 have a negative coefficient. All `binom(20,3)=1140` thirteen-arc candidates are excluded. Our reconstruction rechecks this and classifies the 12 positive supports.

For the 18 selected columns, exact rational linear algebra gives `rank C_U=14`. A strictly positive mixture of the twelve solutions has all 18 chosen arcs positive, so `dim Q=18-14=4`. The 12 positive 14-arc supports are the complete vertex list of `Q`: no missing fewer-than-14 support is possible by the predecessor's exact forced-arc and exclusion certificates, and all 14-arc possible supports were classified. The eleven common arcs are strictly positive at every vertex, so no facet comes from their zero inequalities. Each of the seven optional-arc zero sets has affine span dimension three, giving seven genuine facets; their incidences are exactly those of `Delta_2 x I x I`. Single-option swaps are polytope edges.

A complementary stability statement follows: there is a relatively open neighborhood of `z_c` in the predecessor's seven-dimensional hyperplane `H` where the same 12 support choices remain strictly positive, the other finitely many candidate supports remain excluded, and the 18-arc face retains this combinatorial type. The existence follows from finite support exclusion, strict rational margins, and fixed matrix rank; **no explicit numerical radius is claimed**.

## Reproducibility / verification scope

The accompanying `VERIFY_FACE.py` invokes the predecessor's `VERIFY_SHEET.py` and checks the 18-column rank, all twelve actual positive solution vectors, 4D vertex affine span, seven 3D facet spans and 24 candidate exchange edges. Independent reconstruction in the local Python/SymPy environment executed these arithmetic checks using the frozen formulas and produced `RECONSTRUCTION_OUTPUT.txt`. The independent reconstruction, rather than a byte-identical run of the newly composed wrapper against the source checkout, is the directly executed local evidence. The predecessor's native repository verifier is available at the linked pinned PR.

Evidence applies to this exact seven-statistic model and contact family. It is a finite exact algebraic classification; mathematical acceptance and formal Result require independent review.

## Next scientific unit

Parameterize the four-dimensional face by four free positive branch variables and compute its exact vertex/facet transition inequalities on the seven-dimensional wall H. Locate the first parameter where a common eleven-arc mass reaches zero or an excluded 14-arc support becomes feasible, then test the corresponding contact for a lawful 13-arc realization. Preserve all 30 arc identities, physical constraints and the complete observer during that continuation.
