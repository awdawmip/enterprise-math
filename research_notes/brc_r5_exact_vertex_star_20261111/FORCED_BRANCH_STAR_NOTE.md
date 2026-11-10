# R5 — Forced two-sided transport and exact corank-one vertex degree

Date: 2026-11-11 Asia/Shanghai. Mathematical status: PROVED (conditional on the exact frozen finite Blackwell model and the previously verified rational physical witness); exact SymPy verification executed. Scientific pins remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e, unchanged. Predecessors: PR #2017 (physical all-positive witness) and PR #2026 (exact 14-arc vertex).

## Frozen mathematical input

The ratios are r=(1/10,1/2,3/4,1,5/4,3/2,19/10). There are 30 allowed arcs (i,j): (0,0), (6,6), and all i=0,...,6 for j in {1,2,3,5}. C is the 21-by-30 rational observation matrix encoding seven target marginals, seven source marginals, and seven source first moments. The exact rank of C is 15. Let E0 be the all-strictly-positive rational 30-arc witness in PR #2017, q=C E0, and F={E in R_+^30: C E=q}. The fixed physical pair is the original lawful pinned witness, not an arbitrary right-hand side. All statements involving the original physical pair refer to F. The model is an auxiliary typed observer, not an additional P000/worldview axiom.

## Theorem A — three ports force two-sided non-diagonal branching

For each source j, set mu_j=q[7+j], nu_j=q[j], lower L_j=sum_{i:r_i<r_j}E_ij, upper U_j=sum_{i:r_i>r_j}E_ij, and M_j=L_j+U_j. Then for every E in F and j in {1,3,5}, both L_j and U_j are strictly positive, and these exact inequalities hold:

| j | delta_j=mu_j-nu_j | L_j lower bound | U_j lower bound |
|---|---|---|---|
| 1 | 3733899/135903376 | (5/13) delta_j = 1436115/135903376 | (2/9) delta_j = 1244633/203855064 |
| 3 | 2330939/8493961 | (5/23) delta_j = 11654695/195361103 | (5/23) delta_j = 11654695/195361103 |
| 5 | 3733899/135903376 | (2/9) delta_j = 1244633/203855064 | (5/13) delta_j = 1436115/135903376 |

Consequently each of these source ports has at least one positive non-diagonal arc to a smaller-ratio target and one to a larger-ratio target: at least six distinct non-diagonal positive arcs are mandatory throughout F.

**Proof.** The target marginal condition gives E_jj <= nu_j. Source conservation gives M_j=mu_j-E_jj >= mu_j-nu_j=delta_j>0. The source first-moment equality (row 14+j of C) gives

sum_{i:r_i<r_j}(r_j-r_i) E_ij = sum_{i:r_i>r_j}(r_i-r_j) E_ij.

Write a_min and a_max for min and max positive gaps r_j-r_i on the lower side, and b_min and b_max for the higher-side gaps r_i-r_j. With nonnegative E,

a_min L_j <= b_max U_j and b_min U_j <= a_max L_j.

Solving with M_j=L_j+U_j yields

L_j >= [b_min/(a_max+b_min)] M_j,
U_j >= [a_min/(a_min+b_max)] M_j.

Substitute M_j>=delta_j and the seven exact rational ratios to obtain the table. Each bound is strictly positive. QED.

This is an entire-fiber structural theorem and gives exact branch-and-bound pruning inequalities for searches for 13-or-fewer-arc feasible extreme points.

## Theorem B — closed-form vertex-star degree

Let C be the same 30-column matrix (rank 15), but allow any feasible fiber {E>=0:C E=q'}. Suppose X is a vertex with |supp(X)|=rank(C_supp(X))=14 and for exactly one selected variable source j in {1,2,3,5} the only positive arc leaving j is diagonal (j,j). Then

**deg(X)=10+j(6-j)**.

Specifically the degrees are 15, 18, 19 and 15 for j=1,2,3,5 respectively. Any vertex with 15 independent positive support columns has degree exactly 15.

**Proof.** The column span of the 14 support arcs has codimension one in im(C). The row functional phi_j = (source-j first-moment observation) - r_j (source-j mass observation) vanishes on all support columns, since the only occupied source-j arc is diagonal. It is nonzero on missing j arcs; hence it defines the unique quotient direction. Among the 16 absent arcs, ten have source different from j, quotient 0. The remaining six are the source-j arcs with quotient r_i-r_j: j negative and 6-j positive because ratios are strictly ordered.

The pointed tangent cone at X is described in the 16 missing-arc insertion coordinates by nonnegativity and the sole relation sum_k (r_i-r_j) d_k=0. Its extreme rays are exactly ten singleton zero-quotient insertions and j(6-j) positive-negative pairs, weighted to cancel quotient. Each ray uniquely determines the old-support change because C_supp(X) has independent columns. The fiber is bounded (all arc masses are bounded by source marginals), so each ray has a positive finite endpoint X+t d, giving an adjacent distinct vertex. These exhaust tangent rays. At a rank-15 vertex there are 15 absent arcs and every singleton insertion gives a unique edge ray. QED.

## Executed exact first-star test

The exact 14-arc vertex of PR #2026 has only (2,2) occupied from source j=2. Formula B gives 10+2*4=18, independently of the full inverse-rank enumeration. Rebuilding the entire first star from exact rational coefficients verifies ten neighboring 14-support vertices are also source-2-locked and each has degree 18; the other eight are 15-support vertices and each has degree 15.

Run from this directory: python VERIFY_STAR_DEGREES.py, then python VERIFY_BRANCH_STAR.py. The latter directly reconstructs E0 from the immutable rational WITNESS.txt values (embedded as data), verifies Cx=CE0 and all delta fractions, and prints the actual transcript saved in EXACT_BRANCH_STAR_OUTPUT.txt. All calculations use exact SymPy Rational, no floating-point optimization. The physical legality of E0 is inherited from PR #2017, not separately re-proved this run.

## Remaining discriminating problem

Determine whether **every** 14-support vertex of this fixed F is source-2-diagonal-locked, or construct one that is not. Search for 13-support or smaller vertices using the now-proved six-mandatory-branch bound. The previous complete radius-four BFS reported 1775 vertices but did not settle the global minimum, and this note does not claim a radius-five search was completed.

Evidence scope: author-side mathematical proof, exact local execution, published branch evidence after GitHub readback. Native authenticated registration and formal Source CLAIM/Result/review remain separate.
