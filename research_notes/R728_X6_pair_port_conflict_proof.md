# R728 — X6 candidate port-conflict triads: sharp feasibility and BRC future-safe observation

Date: 2026-11-12. Role: author-side TASK_RESEARCH mathematical derivation. Parent task RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including native P000 and definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md. Continuation source: R727 Draft PR #2107, commit f0e617a61af11ab9e2861c1b19747ab1f05f6249.

## Exact conditional model

At one chosen X6 native Cell, source quanta have distinct source IDs, one of six original positive-axis families 0,...,5, a retained sign, and retained port/branch provenance. We count partitions of 3m distinguishable sources into m unordered triples. The R727 incidence layer permits triples of three pairwise distinct axis families; actual primitive stability additionally requires the typed native TRIADIC_CLOSURE_E certificate.

For a candidate port-exclusion hypothesis H, assume axis families 0 and 1 share one exclusive port block and no eligible candidate triple contains both. Other distinct-axis triples remain eligible. Write B_0={0,1}, B_1={2}, B_2={3}, B_3={4}, B_4={5}; the candidate hypergraph E_H consists of 16 of the 20 distinct-axis triples, excluding precisely 012,013,014,015. This is an explicit hypothesis to test against actual native Cell/Link/Port, V29 or V39 rules, not a recovered P000 force law. The six original axes are unchanged; a block is an auxiliary incidence constraint.

## Theorem 1: sharp feasibility for arbitrary conflict blocks

Let B_1,...,B_r be a disjoint partition of n original axis families, r>=3. Each legal candidate triple has three different blocks, and there are a_i distinct source IDs on family i, sum a_i=3m, m>=1. Put b_s=sum_(i in B_s) a_i. Then a partition into m unordered admissible triples exists if and only if max_s b_s<=m.

Proof. Necessity follows because a triple uses a block at most once. For sufficiency, regard each original source as a distinguishable element of its aggregate block. Initially the r block counts sum to 3m and are <=m. For k remaining triples, choose one source from each of the three largest positive blocks. At least three blocks are positive: if at most two were positive, their total would be <=2k, but it equals 3k. Every block of count k must belong to these three: four blocks of size k exceed the total 3k. After the decrements, every remaining block has size <=k-1 and the total is 3(k-1). Induction produces all m triples without deleting original source/axis labels. QED.

For the six-axis hypothesis H the criterion is a_0+a_1<=m and a_i<=m for i=2,3,4,5, together with sum a_i=3m.

## Theorem 2: exact source-ID BRC branch partition function

Let E be any finite hypergraph of allowed three-distinct-axis triples. Set P_E(x)=sum_(T in E) prod_(i in T)x_i. Denote by L_E(a) the number of unordered partitions of the distinguishable source IDs into allowed triples. Then

L_E(a) = (prod_i a_i! / m!) [x_0^a_0 ... x_(n-1)^a_(n-1)] P_E(x)^m.

Proof. Expanding P_E^m selects m ordered axis-triple slots. The indicated coefficient counts their ordered axis types at the required occupations. There are exactly prod_i a_i! bijective assignments of individual source IDs to the slots of each family. Each resulting unordered partition appears m! times, one for each permutation of its m distinct source-ID triple slots. Dividing by m! proves the identity. QED.

For conflict blocks let Q_B(y)=sum_(s<t<u) y_s y_t y_u. The candidate polynomial is P_B(x)=Q_B(sum_(i in B_1)x_i,...,sum_(i in B_r)x_i). For the *numeric count observer*, without discarding actual source-ID branch history,

L_B(a) = (prod_s b_s! / m!) [y^b] Q_B(y)^m.

This follows by applying the same labeled-source slot argument to block memberships while still treating every source ID as a separate individual. Thus the current count factors through b, but recovering the original family labels or predicting another port rule is a different observer.

## Theorem 3: exact future-fiber collision and repair

For m=2 consider a=(1,1,1,1,1,1) and a'=(2,0,1,1,1,1). Both have the same conflict-block totals b=(2,1,1,1,1), and L_H(a)=L_H(a')=6. If the candidate port-exclusion rule is hypothetically removed while leaving source IDs unchanged, the complete distinct-axis hypergraph has L_full(a)=10 whereas L_full(a')=6.

Proof. For a, there are 10 unordered partitions of six different-axis source IDs into two triples. Exactly four forbidden partitions contain both axes 0 and 1: the third axis in their triple may be any of 2,3,4,5 and the other triple is then forced. Hence six admissible H partitions remain. In a', axis family 1 has zero source IDs, so no complete partition is excluded by the pair rule; the full count equals the restricted count six. QED.

Therefore the block count observer b (even supplemented by the present exact count L_H) is not sufficient for the future operation H->full. The original axis split within B_0 is a future-relevant structural BRC residual. On this explicit two-state fiber, one extra binary distinction is necessary and sufficient; no global codec optimality is asserted.

A second exact witness is a''=(2,1,1,1,1,0), m=2. It satisfies R727's unrestricted criterion and has L_full(a'')=6, but the conflict block has population three >m, so L_H(a'')=0. The port condition changes existence, not only multiplicity.

## Theorem 4: typed axis-label covariance

For any axis permutation tau in S6, transport together all source-axis labels, original native chart labels and the port-rule hypergraph E. Then tau induces a bijection on the sets of source-ID partitions, so L_(tau E)(tau a)=L_E(a). Keeping the excluded pair fixed restricts symmetry to permutations preserving {0,1}; full S6 covariance requires transporting the port-rule state. This is candidate combinatorics, not a native rotation/heartbeat law.

## Exhaustive exact finite check

An independently written pivot-source-ID recursion and an ordered polynomial coefficient dynamic program agree, including all zero cases, on every six-family count vector of total 3m for m=1,2,3,4: 56+462+2002+6188=8708 vectors. Both sharp feasibility criteria were checked on the entire finite domain. Restricted feasible vectors: 16,99,378,1088; unrestricted: 20,141,580,1751. Maximum restricted source-partition counts: 1,6,96,2448; unrestricted: 1,10,124,4960. A distinct-axis S6 pair-label transport test covers 720 permutations. The machine marker is R728_PORT_CONFLICT_EXACT_PASS; the companion Python and JSON contain exact reproducible evidence.

These are finite typed, nonnegative integer BRC branch counts with preserved source identities. No numerical physical trajectory, pi, trigonometry, classical matrix exponential, V29 PASS/TRANSFER or V39 flow j has been computed.

## Next decisive native unit

Extract a single exact, legal, pinned Cell/Link/Port update and its permitted TRIADIC_CLOSURE_E decisions, with signed axes, individual sources, branch/port identity, native event order and V29 or V39 witness. Define its actual allowed triad hypergraph E(c,t), check whether the port-block hypothesis holds, then test the source-count observer before and after the real update. Retain any disconfirming event as a precise discriminator. Formal CLAIM, semantic checkpoint, independent Driver review and Foundation/Working Truth adoption retain separate Source authority.