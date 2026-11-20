# Stage483-B — Twelve signed native X6 directions: sparse Euler–BRC exact equivalence/counting

Date: 2026-11-06. Research2 author proof, exact integer verification, UNREVIEWED.

## Provenance and model

Parent: Stage482-B commit 52950a9a9cc50e081df98e853ecd3aaebc283066, Research2 PR #1736. Immutable scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules are read separately via docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context.

Work in native six-axis signed relative X6 displacements. Let D={A,...,L} correspond in order to +E1,...,+E6,-E1,...,-E6; twelve directions are not twelve spatial axes. Study ordered primitive path words with k,u>=1, m=2k+2, P=A^m, Q=A^m W A H A, |W|=k, |H|=u. Each APPEND selects any of the twelve signed native directions. P has at most k POP and k APPEND; Q has at most h POP and one APPEND; operations may legally interleave. Do not POP the last remaining letter. Observation records both word lengths, their native six-coordinate signed endpoint displacements, complete directed adjacency counts in D×D, and positional equality count K.

Write E(X) for the 144-component directed adjacency multiset of word X and Θ=E(Q). Q always begins with A, so the number of occurrences of any v in Q is indeg_Θ(v)+[v=A]. Thus Θ determines the Q six-axis signed displacement and, with fixed P, determines the complete initial observation fiber. Path order beyond Θ remains a potentially future-visible residual.

## Theorem 483.1 — Exact future observation equivalence

Let r=min(h,u). Two histories in the same initial full-observation fiber yield identical observations for **every common legal future operation word** if and only if

\[
\boxed{(W_1,\operatorname{suffix}_{r}(H_1))=(W_2,\operatorname{suffix}_{r}(H_2)).}
\]

**Sufficiency.** The P word is identical under the same P operations, and its maximum possible length is m+k. When h<=u, Q retains its initial A^m W prefix throughout. All positional comparisons with P therefore depend only on W (and known appended actions); changes from Q APPEND occur beyond length m+k. Q future directed edges and six signed displacements are obtained from initial Θ and the known initial displacement by removing the edges/signed directions actually popped, and adding those actually appended. The removed original Q directions for up to h POP belong to the known final A and suffix_h(H); after an APPEND the new terminal direction is known. When h>u, the key contains all of H, and together with W determines all of the original Q, including any further POP across the fixed separators. This covers arbitrary legal interleavings, including APPEND followed by POP.

**Necessity.** If W differs, APPEND the k letters W_1 to P without changing Q. This makes all k new positions match Q_1, while at least one fails against Q_2, so K differs. If W is equal but the length-r suffixes of H differ, choose the rightmost differing letter at depth d<=r from the H tail. Apply d Q-POPs, leaving P unchanged. Earlier popped directed edges are identical; the d-th pop deletes edge x->z versus y->z with x!=y and identical right neighbor z, so the complete directed edge count differs. This proves exact separation in the stated operation language.

This direct proof is independent of the still-unreviewed general Stage474.1 arbitrary-budget theorem.

## Theorem 483.2 — Sparse directed Euler word populations

For a directed edge multiplicity vector e on the twelve-letter alphabet, let N(ell,s,t,e) count distinct length-ell vertex words with first s, last t and adjacency multiset e. For ell=1 the unique legal case is s=t and e empty. For ell>=2, impose nonnegative edges, sum e=ell-1 and out(v)-in(v)=[v=s]-[v=t].

Let V contain s,t and all vertices incident to positive edges. Exclude the root t and form the outgoing Laplacian minor L_t on V\{t}, whose diagonal is out(v)-e(v,v) and whose off-diagonal entries are -e(v,w). Let tau_t=det(L_t), the number of directed arborescences toward root t. When tau_t>0, and all nonroot active vertices have positive outdegree,

\[
\boxed{N(\ell,s,t,e)=
\frac{\tau_t\,\operatorname{out}(t)!\,
 \prod_{v\in V\setminus\{t\}}(\operatorname{out}(v)-1)!}
 {\prod_{x,y\in V}e(x,y)!}.}
\]

Otherwise N=0. By the directed matrix-tree theorem and open/closed BEST trail counting, temporarily label equal parallel edges; choose the last-exit directed tree toward t, permute other outgoing edges, and divide by every parallel-edge factorial to recover distinct vertex words. Loops participate in outgoing permutations but not in the arborescence minor. Isolated vertices and zero-edge words have the explicit rules above. The determinant uses at most |V|-1<=11 rows and may be computed exactly by Bareiss integer elimination; its algebraic signs are not signed/amplitude BRC masses.

## Theorem 483.3 — Sparse positive BRC support and population

For a fixed W, define B(W)=E(A^m W A) and R=Θ-B(W)=E(A H A), with |R|_1=u+1. Starting from state (A,R), read the last r hidden letters backwards. A transition along any positive remaining edge x->c is

\[
(c,e)\longmapsto(x,e-\mathbf{1}_{x\to c}).
\]

Let D_r(c,e) count different reverse-reading paths to that state. With L=u-r,

\[
q_R(r)=\sum_{c,e}D_r(c,e)\,[N(L+2,A,c,e)>0],
\qquad
M_R(r)=\sum_{c,e}D_r(c,e)N(L+2,A,c,e)=N(u+2,A,A,R).
\]

The first is the number of supported suffix **classes** (Boolean test at accepting states, but integer path multiplicities retained); the second is the number of original hidden words. Merging equivalent remaining-edge states must ADD their path counts rather than collapse to Boolean. This handles r=0 and r=u. Constraining a normal left prefix of the suffix gives exact lexicographic rank/unrank; for W, aggregate by its first/last symbols and internal edge vector e_W, weighted by N(k,s,t,e_W), then apply the same prefix-completion method.

Explicit full-fiber formula, summing over W directed types with nonnegative residual R:

\[
q_\Theta=\sum_{s,t,e_W}N(k,s,t,e_W)\,q_{R_{s,t,e_W}}(r),\quad
|F_\Theta|=\sum_{s,t,e_W}N(k,s,t,e_W)\,M_{R_{s,t,e_W}},
\]
\[
R_{s,t,e_W}=\Theta-\big[E(A^m)+\mathbf1_{A\to s}
 +e_W+\mathbf1_{t\to A}\big].
\]

For s_R positive edge types and a_R active symbols, after i backward steps at most
a_R * C(u+s_R-i,s_R-1) distinct residual states occur. Each has at most a_R possible transitions. The W-type search uses only edges from supp(Θ-E(A^m)), so at most a_Θ²*C(k+s_Θ-2,s_Θ-1) candidate types. Thus if the input directed-edge support is bounded by a small constant, the entire count has polynomial-size exact integer dynamic programming in k,u, even while the number of distinct history words/classes is exponential. Dense 144-edge instances can have very large state exponents; full cost includes type generation, tree determinant/factorial calculations, integer bit lengths and recovery.

## Actually executed evidence

The complete local exact verifier REPRO_STAGE483B.py ran twice and produced byte-identical REPRO_STAGE483B_EXECUTED.json. Coverage: 363 directly enumerated signed-alphabet sample words across lengths 1..5, 300 Euler endpoint-edge types, each of the 12 signed primitive directions individually; 1,230 complete initial-fiber/budget configurations from specified small k,u and signed letter subsets, 2,886 original-word occurrences, 2,660 class occurrences, 2,498 complete-key rank/unrank checks, and direct full 12-direction future operation trees (676 states for one same-key pair).

Large 12-symbol-domain sparse instance uses k=16,u=13, W=ABGAABGAABGAABGA, H=AGBAAGBAAGBAA, with signed direction G=-E1; Θ has seven positive edge types and three active directions. The exact fiber contains 333,915,624 raw histories, 1,154 positive W types, and 162 distinct residual R values. Results:

|Q POP r|Exact classes|Raw population|Sum of reverse transitions for distinct R|
|---:|---:|---:|---:|
|0|880,898|333,915,624|0|
|1|2,184,817|333,915,624|411|
|3|8,293,813|333,915,624|2,788|
|6|47,641,484|333,915,624|13,558|
|9|175,874,227|333,915,624|28,630|
|13|333,915,624|333,915,624|37,903|

Transition totals describe the automaton only, not wall-clock speed or the whole type-enumeration cost. The full original candidate word family has size 12^(16+13); no full enumeration was used for this instance. The published compact runnable reproducer independently computes this table and the 363-word Euler check; the complete local verifier additionally runs the smaller fiber, rank and future-tree checks.

Status: author mathematical argument + exact computer experiments / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_RESULT. Next Stage484-B: nonconstant shared P prefix, minimal 12-direction counterexamples or proof, and multi-Q-APPEND behavior under typed future operations.
