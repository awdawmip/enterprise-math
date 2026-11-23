# EC49FYF — Full S11 column symmetry and exact hard-state prefix pruning

Date: 2026-11-24 (Asia/Shanghai). Frozen science: **BRC16943**. Research lane: Research 4, informed independent portable continuation. Parent: [EC49FYE](https://github.com/awdawmip/enterprise-math/blob/7c760835aadb2a8de458dad54fa103c23bc4fe8f/research_notes/portable_direct/EC49FYE_ONE_HOLE_TWO_MULTICOVER_THEOREM.md) at immutable source commit \`7c760835aadb2a8de458dad54fa103c23bc4fe8f\`; prior hard-factor certificate theorem: [EC49FYD](https://github.com/awdawmip/enterprise-math/blob/7454e769679058baf19b5c922ae0543fa5407076/research_notes/portable_direct/EC49FYD_FULL_FACTOR_HITTING_CERTIFICATE_THEOREM.md).

Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**. This is a normalized P10/C11 auxiliary observer result; the exact realizability of all 600 states uses the frozen predecessor EC49FXU and is not a native X6 dynamical claim. This document does not establish new live CLAIM, Result or mathematical Review authority. Historical line: \`RA-0F8055ACDE0F5F6A97CA5D6D\` / \`EM-DIRECT-48E619\`; current execution ownership must be assessed separately.

## Exact model

Use precisely the 50 ten-bit masks in the BRC16943 P10 census, \(\mathcal F\subseteq 2^{\{0,\ldots,9\}}\). Let \(J=\{0,\ldots,10\}\) and let
\[
\mathcal S=\mathcal F\times(\{-1\}\cup J),\qquad
W_{U,z}(t,j)=\mathbf1_{t\in U}\mathbf1_{z\ne j}.
\]
There are \(50\cdot12=600\) states and 110 Boolean sites. Here \(z=-1\) is a complete factor and \(z=j\) deletes column \(j\). Queries are noiseless and indexed, and the objective is to identify the entire \((U,z)\) with minimum worst-case adaptive tree depth; no full reflection spectrum is supplied for free.

## Theorem 1 — exact full symmetric-group automorphism

**Claim.** Every permutation \(\pi\in S_{11}\) of the eleven physical column labels is an automorphism of the complete state/observer pair, acting by
\[
\pi(U,-1)=(U,-1),\qquad \pi(U,z)=(U,\pi(z))\quad(z\in J),
\]
and \(\pi(t,j)=(t,\pi(j))\). For every state and query,
\[
\boxed{W_{\pi(U,z)}(t,\pi(j))=W_{U,z}(t,j)}.
\]

**Proof.** Row membership \(t\in U\) is unchanged. For a hole label \(z\in J\), bijectivity gives \(\pi(z)\ne\pi(j)\iff z\ne j\); for \(z=-1\), neither observer has a deleted column. The family of all 600 states is invariant because for each \(U\) all eleven hole labels and the complete label occur. The observation identity follows, proving the full \(S_{11}\), not merely cyclic \(C_{11}\), symmetry. \(\square\)

**Scope.** This automorphism pertains to the full 600-state, column-indexed product observer. Introducing a height bound, anchoring an external physical-column geometry, or permitted future operations that are not column-equivariant may break this symmetry; their invariance must be checked anew. No such stronger symmetry is asserted for original Farey fractions or native X6 dynamics.

## Theorem 2 — exact pathwise canonicalization of new columns

Fix any partial query/answer transcript \(P\). Write \(J_P\subseteq J\) for the set of physical columns already mentioned, with \(k=|J_P|\). Its candidate-state set \(\mathcal S_P\) is invariant under every permutation fixing \(J_P\) pointwise, because all past query answers concern only these columns. That stabilizer permutes the other \(11-k\) columns transitively.

**Claim.** Any zero-error adaptive decision tree of depth \(d\) can be transformed into another with no larger depth in which, on every root-to-leaf path, the next previously unseen column is always the smallest unused label. At a node with \(k<11\) used columns, it is therefore sufficient to consider tests in \(k\) existing columns plus one canonical new column: at most \(10(k+1)\) row/column queries. For \(k=11\), at most 110 queries remain (minus already queried positions).

**Proof.** If a node proposes a query in an unseen column \(j\) other than the canonical new label \(j_0\), swap \(j,j_0\), fixing the columns in \(J_P\). The candidate set at the node is invariant under this swap. Relabel all query columns and all hole-label outputs in the downstream subtree by the same swap, applying the inverse relabeling to recover the original physical hole label at the output. The transformed subtree has the same answer partitions and exact depths. Induct down the tree, independently at each node (subtrees following distinct answer branches need not share renamings). Previously used columns never change. \(\square\)

At the root the **110 concrete physical queries reduce to 10 symmetry classes**: query \((t,0)\), \(t=0,\ldots,9\). After the first query there are **19 nonduplicate canonical second-query candidates**: \((u,0)\) except the already queried site and \((u,1)\), \(u=0,\ldots,9\). This reduction is a depth-preserving theorem, not a heuristic.

## Theorem 3 — hard-state certificate restrictions and exact depth-two pruning

Prior EC49FYD establishes that for a complete-factor target \((U,-1)\), its minimum certificate size is \(11+\tau(U)\), where \(\tau\) is the minimum number of negative support rows hitting every strict-supermask difference. Exactly three masks have cost 14:
\[
U\in\{101,788,833\}.
\]
Their complete sets of minimum negative-row transversals are:

- \(U=101\) (6): \(\{1,4,9\},\{1,7,9\},\{3,4,9\},\{3,7,9\},\{4,8,9\},\{7,8,9\}\).
- \(U=788\) (4): \(\{0,3,6\},\{0,3,7\},\{0,5,6\},\{0,5,7\}\).
- \(U=833\) (8): \(\{1,2,3\},\{1,2,4\},\{1,3,7\},\{1,4,7\},\{2,3,5\},\{2,4,5\},\{3,5,7\},\{4,5,7\}\).

**Necessary path constraints.** Suppose a depth-14 identification tree exists. On the path for each of these full-factor targets, all fourteen queries must constitute a minimum separating certificate. In particular:

1. Exactly eleven *positive* queries, in all eleven **distinct** columns, must occur to distinguish the eleven single-hole variants of that same mask.
2. Exactly three *negative* queries, in three **distinct** rows forming one of the listed minimum transversals, must occur. A negative query outside every minimum transversal, two negative queries in the same row, or two positive queries in the same column therefore makes depth 14 impossible on that state path.

These constraints follow from disjointness of the eleven positive-column obligations and the three negative transversal obligations; they are necessary, not sufficient for a complete decision tree.

For each first row \(t\), fix the root query \((t,0)\), and independently consider each answer branch \(b\in\{0,1\}\). Only the hard complete-factor targets giving answer \(b\) can obstruct a second query at that branch. Of the 19 canonical nonduplicate second probes, the following counts are *rigorously excluded* by the necessary path constraints above (empty hard-state branches have zero exclusions):

| Root row \(t\) | Forbidden if first answer \(0\) | Forbidden if first answer \(1\) |
|---:|---:|---:|
|0|3|5|
|1|19|0|
|2|3|8|
|3|9|0|
|4|5|5|
|5|5|3|
|6|5|5|
|7|9|0|
|8|5|7|
|9|1|7|

The row-1 root is thereby eliminated altogether: \((788,-1)\) has answer zero there, and its minimum transversals never contain row 1; no length-14 certificate on that target can contain a row-1 query. Thus only **nine** root-row symmetry classes remain potentially feasible for depth 14. For every other row, the table gives a sound branch-specific rejection list, not a claim that the surviving probes succeed.

## Exact reproducible evidence

Companion \`EC49FYF_S11_HARD_PREFIX_VERIFY.py\` (Python 3, standard library only) reconstructs the 72 primitive P10 directions and all 50 support masks from the pinned P10 predicate. It performs **660,000 integer/Boolean readout equalities**, i.e. every state (600) and every physical query (110) under each of the 10 adjacent column transpositions generating \(S_{11}\). It enumerates every row subset for each of the three hard-state transversal hypergraphs, confirms minimum sizes 3 and counts 6/4/8, and tests all 19 canonical second positions for each of the 10 root rows and each answer branch. Exact results are in \`EC49FYF_S11_HARD_PREFIX_OUTPUT.json\`.

This is a mathematical proof supported by finite crosschecks. The finite checks cover the stated 600-state frozen observer; they do not substitute for a proof of a global 14-depth tree or its impossibility.

## Next unresolved unit

The global optimum remains \(\boxed{14\le Q_{\rm adaptive}\le15}\). Use the pathwise \(S_{11}\) quotient and the exact branch-specific hard-state certificate filters to implement an exact minimax search on canonical candidate sets, with reusable subset lower bounds. A depth-14 constructive tree, or exhaustive depth-14 exclusion over the nine remaining root rows, is required to settle the dichotomy. Reuse the existing EC49FYA 15-depth construction and EC49FYB 37-site nonadaptive baseline without rederiving them.

## Research/authority handoff

Independent portable source publication is not a formal CLAIM, Result, Review, theorem promotion or Activity audit. Preserve the historical researcher and immutable parent proof pins; a current authenticated research identity/role must be established separately before any protected native association or shared-task write.
