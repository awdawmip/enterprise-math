# R284Z — Exact cyclic two-terminal path pairing and planar rigidity for stable nonnegative Port observers

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**.
Research lineage: Researcher EM-DIRECT-E6B1DD, registered SID MCP-8487128c846440d1952bfc6fa44aeb86. Original frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34, unchanged. This is an auxiliary finite-rational BRC Port observer result, not a native Heartbeat World/X6 dynamics result, Task CLAIM, Result or independent Review.

## Source and scientific question

Immediate predecessor: R284Y, exact partial-matching coefficient certificate and two-terminal Schur reduction, at source commit eb197ee78efb59a38657c0f9ae4fbf7ed0a8950c (research_notes/portable_direct/R284Y_MATCHING_MINOR_ENUMERATION_AND_PORT_SCHUR_CERTIFICATE_20261119.md). Related: R284V Hall deficiency, R284W/X common-kernel and aligned-pencil results.

R284Y leaves open whether the strictly nonnegative stable Port-sign domain admits a matching-present, identically singular, independently unit-edited complementary pencil without a fixed common kernel. Here we prove a necessary topological condition for such cancellation, and give an exact polynomial-time graph certificate in the planar disk regime even with internal cycles.

## Definitions

Let P=(p1,p2), Q=(q1,q2), and S be three pairwise disjoint vertex sets, with S ordered. Let W be a nonnegative transition matrix with spectral radius rho(W_SS)<1. Strictly substochastic W is a sufficient condition. The relevant subnetwork uses only edges from P to S or Q, and from S to S or Q; all other edges are irrelevant to this complementary minor. Preserve all vertex, edge and edit names.

Use ordered rows (S,P) and columns (S,Q), and set

\[
G=I_S-W_{SS},\quad
T=W_{PQ}+W_{PS}G^{-1}W_{SQ},\qquad
A=\begin{pmatrix}G&-W_{SQ}\\-W_{PS}&-W_{PQ}\end{pmatrix}.
\]

The Schur complement gives \(\det A=\det G\det T\), and \(\det G>0\).
For i,j in {1,2}, let Gamma_ij be the simple directed paths from p_i to q_j with interior vertices only in S (a direct edge is allowed). A routing for bijection pi consists of two vertex-disjoint such paths gamma_1 from p1 to q_pi(1), gamma_2 from p2 to q_pi(2). Denote their total internal vertex set U, their edge-weight product w(gamma_1)w(gamma_2), and the residual principal determinant \(\det(I-W_{S\setminus U,S\setminus U})\), equal to 1 for the empty set.

A *support perfect matching* refers to the bipartite nonzero pattern of A, not a formal research-task matching.

## Theorem Z1 (cycle-exact path-pairing formula and sign rigidity)

For every such W (arbitrary finite internal feedback cycles allowed),

\[
\begin{aligned}
\det A
={}&\sum_{\substack{\gamma_1:p_1\to q_1,\ \gamma_2:p_2\to q_2\\
\gamma_1,\gamma_2\text{ vertex-disjoint}}}
w(\gamma_1)w(\gamma_2)\det(I-W_{S\setminus U,S\setminus U})\\
&-\sum_{\substack{\gamma_1:p_1\to q_2,\ \gamma_2:p_2\to q_1\\
\gamma_1,\gamma_2\text{ vertex-disjoint}}}
w(\gamma_1)w(\gamma_2)\det(I-W_{S\setminus U,S\setminus U}).
\end{aligned}
\]

Every existing positive-edge routing contributes a **strictly positive** value to its pairing sum. Hence if at most one of the two terminal bijections has a positive routing, det A has a fixed sign and is nonzero exactly when that pairing has a routing. If a matching exists but det A=0, there must be positive-weight disjoint routings for **both** bijections and their two weighted sums must agree.

**Proof.** Expand det A using its rows S,P and columns S,Q. Since no P column and no Q row appears, every permutation term decomposes uniquely into two directed P-to-Q paths, vertex-disjoint cycles supported on their unused internal vertices, and fixed internal vertices. The paths define a bijection pi of the two terminal pairs. Each nontrivial edge contributes -W_uv; choosing a fixed internal vertex contributes 1, while using its -W_uu part is a one-vertex cycle. In the determinant sign bookkeeping, the path family contributes sign(pi), and the remaining signed cycles and fixed vertices sum to the principal determinant det(I-W_{S\setminus U,S\setminus U}). This fixes the displayed signs, also visible for S empty where det A=det W_PQ.

Any principal submatrix W_J of nonnegative W_SS has rho(W_J)<1. On the continuous interval 0<=t<=1, det(I-tW_J) never vanishes and starts at 1; hence det(I-W_J)>0. Positive edge products make every nonempty routing summand positive. All conclusions follow. QED.

## Theorem Z2 (exact matching/routing equivalence)

The bipartite support of A admits a perfect matching **if and only if** the positive-edge directed subnetwork contains two vertex-disjoint paths connecting P to Q for at least one bijection.

**Proof.** A support perfect matching defines an S/P-to-S/Q bijection. Decompose its chosen nonzero matrix entries into directed terminal paths and internal cycles (diagonal entries can be treated as fixed points); removing the cycles leaves two vertex-disjoint terminal paths. Conversely, select the -W edge entries along a given pair of disjoint terminal paths, then select the nonzero diagonal \(1-W_{ss}>0\) at every unused internal vertex s. This is a support perfect matching. QED.

The Hall obstruction from R284V thus decides the existence of *some* routing, while Z1 shows that determinant cancellation needs competition between two different terminal permutations.

## Theorem Z3 (planar disk rigidity)

Suppose all positive-support edges of the relevant subnetwork admit a noncrossing planar embedding inside a closed disk, each S vertex in the interior, with the four distinct terminals on the boundary in cyclic order

\[
p_1,\ p_2,\ q_1,\ q_2.
\]

Then disjoint routings p1->q1 and p2->q2 are impossible. Consequently,

\[
\det T\leq 0,\quad
\det T<0\ \Longleftrightarrow\ A\text{ has a support perfect matching},\quad
\det T=0\ \Longleftrightarrow\ A\text{ has no support perfect matching}.
\]

The signs and equivalences hold for **all strictly positive weights on declared support edges** satisfying rho(W_SS)<1, regardless of internal cycles. A different boundary order can interchange the allowed pairing and determinant sign. Named edit edges must remain within the same planar embedded support family for a parameter-uniform application.

**Proof.** The boundary pairs (p1,q1) and (p2,q2) alternate. Two vertex-disjoint arcs joining these alternating pairs would cross by planar Jordan separation, contradicting the embedding. Thus only swapped routings can occur. Their Z1 sum is negative if nonempty, while Z2 says the sum is nonempty exactly when a support perfect matching exists. Since det G>0, det T has the same sign. QED.

**Algorithmic cost.** With the disk embedding supplied, split every internal vertex into in/out vertices connected by a capacity-1 edge, give each directed graph edge unit capacity, connect a super-source to p1,p2 and q1,q2 to a super-sink at capacity 1. An integral flow of value 2 is equivalent to two vertex-disjoint terminal paths for some pairing. Planarity excludes the other pairing, so a single value-2 max-flow test decides det T=0 and its strict sign, with no rational inversion, cofactor expansion or variable grid. A unit-capacity augmenting-path implementation needs at most two augmentations, O(V+E) graph search work with a provided embedding. This is a graph-decision bound, not a bound for computing the exact rational determinant or verifying the embedding from scratch.

## Exact examples

**Cyclic, unique-pairing example.** P=(0,1), S={2}, Q=(3,4), and only the following W entries are nonzero:
0->4=1/8, 0->2=1/8, 1->3=1/8, 2->2=1/5, 2->4=1/8.
All row sums are below 1; the graph supports only swapped routings. The routing using direct 0->4 and 1->3 contributes -(1/8)(1/8)(1-1/5)=-1/80; the routing 0->2->4 and 1->3 contributes -(1/8)^3=-1/512. Thus

\[
\det A=-1/80-1/512=-37/2560.
\]

This checks that the closed loop 2->2 is correctly included by the residual determinant.

**Both-pairing cancellation.** Take S empty, P=(0,1), Q=(2,3), and W_{p_i,q_j}=1/8 for every i,j, all other entries zero. Both pairing sums are exactly 1/64; det T=0 despite a perfect support matching. Under two independent named updates z on 0->2 and t on 1->3,
\[
\det T(z,t)=(z+t)/8+zt.
\]
This is a strictly substochastic Port sign-pattern example where the single-pairing hypothesis matters. The baseline has a fixed kernel, so this is **not** a solution to R284Y's stronger no-common-kernel question.

## Exact verification scope and reproducibility

Executable: research_notes/portable_direct/R284Z_port_pairing_certificate.py.
Machine result: research_notes/portable_direct/R284Z_port_pairing_verification.json.
Python standard-library fractions.Fraction, exhaustive Leibniz determinants for each tested matrix, independent simple-path enumeration and support-permutation matching. Fixed seed 28426. Exactly 512 deterministic generated strictly substochastic graphs: 128 each with |S| in {0,1,2,3}. Every case checked Z1 (all routed cycles included), Z2, and the Z1 sign implication. Counts: 159 no pairing, 186 exactly one pairing, 167 both pairings; 353 support matchings. Both explicit witnesses were also checked, including the exact -37/2560. These finite calculations verify implementation and examples; the general claim rests on the proofs.

## Remaining scientific problem

To solve R284Y's stronger question, construct (or obstruct) a stable nonnegative complementary unit-edit pencil with a perfect support matching, identically vanishing determinant, and no common fixed left/right kernel. Z1 proves that such a candidate needs *both terminal pairing classes* and equality of their cycle-weighted sums as rational functions under all named edits; Z3 rules out the topologically single-pairing disk regime. Next test edit-incidence coefficients of the two signed routing sums, exploit bottleneck separators, and compare the exact cost to Y1 matching-minor and Y2 Schur certificates. Preserve P000 and the auxiliary/native correspondence boundary.
