# BRC-X6: exact minimum supports of barycenters of 180 eight-dimensional faces

**AUTHOR_PROVED / EXACT_FINITE_ENUMERATION / UNREVIEWED / NOT_ADMITTED**, dated 2026-11-09. Task-research portable author evidence; no native CLAIM, Result or independent Driver review is claimed.

Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Original kernel SHA-256 d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0. Retain all 96 native ports, six labeled actions (576 labeled transitions), nine frozen roots and full signed one-step (next-port,R1,...,R6,K) observations. Original signed source ports (6,7,28,29), signs (+,-,-,+). The legal first-step policy polytope P is the convex hull of the 38 previously classified deterministic 24-coordinate 0/1 policies; affine dimension 12.

## New exact finite theorem

For an 8-dimensional face F with n vertices, take its canonical vertex barycenter b_F=(sum_{v in V(F)} v)/n, in relint(F). minSupport(b_F) is the minimum number of distinct legal deterministic policies in an exact strictly positive convex representation of b_F, retaining all original action/port labels.

The complete classification for all 8-dimensional faces with n in {11,12,13} is:

| Dimension | Face vertices n | Number of faces | minSupport(b_F) |
| --- | ---: | ---: | ---: |
| 8 | 11 | 24 | 9 |
| 8 | 12 | 56 | 8 |
| 8 | 13 | 48 | 7 |
| 8 | 13 | 52 | 9 |

Exactly 180 faces are covered. Relative-interior barycenters at the *same face dimension 8* have minimum supports 7, 8 and 9. Even fixing the number of vertices at 13 gives both 7 and 9. These are original native 24-coordinate convex supports, not a quotient-state or different-observer model. Previously classified nine-vertex 8-simplex faces are unchanged; face sizes above 13 are not part of this theorem.

## Explicit rational witnesses

All tuples are original action labels at source ports (6,7,28,29). The face mask is the 38-bit mask of allowed deterministic vertices.

13-vertex face with minimum 7: mask 000016bf0b. Its exact barycenter has common denominator 13 and original four-by-six row numerator matrix

    (3,4,3,3,0,0)
    (4,1,3,3,1,1)
    (3,3,0,4,3,0)
    (4,4,1,1,3,0)

A seven-point decomposition uses (0,0,0,0), (1,0,3,2), (1,1,3,3), (1,4,3,0), (1,5,3,1), (2,2,1,1), (3,3,4,4) with weights (3,1,1,1,1,3,3)/13. All one- through six-point supports drawn from this face are exactly excluded.

12-vertex face with minimum 8: mask 0000000fff. Policies (0,0,0,0), (0,0,1,1), (0,0,2,2), (0,0,4,4), (0,0,5,5), (0,1,2,3), (1,4,3,0), (1,5,3,1) with weights (1,1,2,1,1,2,2,2)/12.

11-vertex face with minimum 9: mask 000001fee0. Policies (0,1,2,3), (0,4,2,0), (1,1,3,3), (1,5,3,1), (2,2,0,0), (2,2,1,1), (2,2,2,2), (2,2,4,4), (2,2,5,5) with weights (1,2,1,2,1,1,1,1,1)/11.

13-vertex face with minimum 9: mask 000001f0ff. Policies (0,0,0,0), (0,0,1,1), (0,0,2,2), (0,1,2,3), (0,4,2,0), (0,5,2,1), (2,2,0,0), (2,2,4,4), (2,2,5,5) with weights (1,2,2,1,1,1,1,2,2)/13.

## Proof and exact certificate method

First, all 24 original coordinate-zero masks are computed from the 38 native policies. Their intersection closure reproduces exactly 46,204 faces, including the empty face and P, and agrees with the prior full-lattice ledger SHA-256 2a4fa0cbebd8828b3f05cae6cbd3804be5bd8b74b808ca96e87a6aa1f4433786. The 180 selected faces all have exact augmented rational/finite-field rank 9, hence affine dimension 8.

Face locality: for b_F, every coordinate zero throughout F is zero. Since all mixture coefficients are nonnegative, every vertex in any representation of b_F must also be zero on those coordinates. As P is of the form {x>=0:Ax=b}, each face is defined by coordinate equalities, so every possible support vertex belongs to V(F).

A minimum-support positive convex representation has affinely independent vertices: an affine dependence permits a positive-coefficient elimination. Each 0/1 policy has four original row sums equal to 1, so affine and ordinary linear dependencies coincide. Therefore, for any candidate size m, enumerate all independent m-subsets of V(F); a dependent subset cannot be a minimum support.

Exact modular screening is valid because each nonzero k-by-k 0/1 integer minor with k<=13 has absolute value at most k^(k/2) <= 13^(13/2) < 1,000,000,007. In particular, a Q-independent candidate remains independent modulo p=1,000,000,007. With integer target t=n*b_F, rational inclusion in its span would then imply consistency mod p, so an augmented-rank increase is a rigorous infeasibility witness. For modularly undecided supports, solve exact rational coefficients, require strict positivity and total weight 1, and verify all 24 coordinates. Enumerate every smaller candidate support to prove optimality.

Main author-side computation: 832,225 candidate subsets were examined up to the first positive exact witness for each of the 180 faces. 654,179 were directly excluded by modular inconsistency and 644 required exact Fraction solves after modular ambiguity; the remainder were linearly dependent. A separately implemented row-echelon verifier with independent prime p=1,000,000,009 re-enumerated all nine-root native policies, verified 8D ranks, checked all 180 exact positive witnesses and excluded 798,032 subsets smaller than the certified minima. These are two same-author algorithms, not independent Driver reviews.

The author-turn portable ZIP includes frozen original kernel, face ledger, full 180-case JSON with original integer numerators and exact fractional decomposition weights, the general face-local exact rational support solver, the classification verifier and the alternative-prime verifier. The general solver is finite and exact for x in this fixed polytope; full-dimensional worst-case subset enumeration is combinatorial, not a claimed polynomial-time algorithm.

## Provenance and continuation

Reuses prior 38-vertex classification: https://github.com/awdawmip/enterprise-math/blob/7886a552ff372fee6d68dada88d1219d9916016e/research_notes/portable_direct/2026-11-09_prefix577_r6_signed_first_step_integral_flow_complete_38_vertices_author_portable.md

Reuses prior complete face lattice: https://github.com/awdawmip/enterprise-math/blob/77acfe64d0535d4f80094ba0f00bb3ea9c313e64/research_notes/portable_direct/2026-11-09_prefix577_r6_signed_policy_complete_face_lattice_author_portable.md

Original Source D25 continuation request h40-r11-d25-exact-continuation-20261109t0137-read-v1 is historically SUCCEEDED as a read receipt; execution_authorized=false and no current own winning CLAIM/private execution capability is established. D25 H0/B0 divided-power, native Frobenius, kappa and CM experiments remain unfinished. UR V2 original four-file bundle remains a separate provenance target (94,687 bytes, SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76). This note is GitHub author evidence, not predecessor Source completed_units.

Next scientific unit: use exact face locality and algebraic lower bounds to prune generic strict-positive policy support searches, with separate compact infeasibility certificates for targets <=m; retain known full-support minSupport 9..13 cases as regression inputs.
