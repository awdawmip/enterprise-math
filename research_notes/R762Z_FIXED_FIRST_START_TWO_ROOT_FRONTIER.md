# R762Z — Exact ordered-start preemption frontier for two named source roots

Date: 2026-11-14 (Asia/Shanghai). Evidence: **AUTHOR-SIDE CONDITIONAL THEOREM / EXACT FINITE VERIFICATION / NOT_REVIEWED**.

Mother Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\` / immutable publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen scientific source: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Author Researcher-ID: \`EM-X6-9568A5\`; Activity-ID: \`RA-0E6BF03532B050ED802ED0A4\`. An independent researcher held the active maternal-task CLAIM at the 2026-11-14T01:27:03Z native snapshot, so this is a separately preserved mathematical contribution, not an owner-claimed Result.

## 1. Question and execution language

Continue R762Y (PR #2358, immutable commit \`82a5112d19c9f24c9b5fba140820a8f25dce69aa\`). Let \`q>=2\` and take a directed simple cycle of q distinct, named ports \`v_0,...,v_(q-1)\`, with edges \`e_i:v_i -> v_(i+1 mod q)\`. A *labeled macro* \`C_r\` fires the q edges \`e_r,e_(r+1),...,e_(r+q-1)\` in that order, returning one conserved nonnegative integer token to its named root. Individual macro steps can interleave with those of others, but their own order cannot change. A switch away from an unfinished macro to a different macro counts as one interruption; a switch after completion is free. Choose the initial port token stocks with sum K. No replenishment after time zero.

**New restriction:** macros must be first started in a specified chronological list order \`w\`. Specialize to at most two distinct named roots A and B, with first root A. The two roots may be any two distinct vertices of the q-cycle. Denote by \`b(w)\` the number of maximal nonempty contiguous B-blocks (B-runs) in the sequence of first-start roots, with \`b(w)=0\` when B does not occur. All labeled macros must be completed exactly once.

The P000-relevant case is q=3, three named signed X6 source ports and a conditional R762W/R762Y ordered V29 PASS cycle per macro. The q-cycle combinatorics is auxiliary and retains the six-axis Cell substrate and separately typed time.

## 2. Theorem Z1 — exact chronological cost

For any finite nonempty two-root word w beginning at A and any integer q>=2:

\[
h_{\min}(K;w)=
\begin{cases}
b(w),&K=1,\\
0,&K\ge2.
\end{cases}
\]

If only A occurs, K=1 and h=0 suffice. If both roots occur, the dual resource frontier is \`K_min(h;w)=1\` for \`h>=b(w)\` and \`K_min(h;w)=2\` for \`0<=h<b(w)\`.

**Upper bound, one token.** The first macro can only start with its sole token at A. Partition w into successive A- and B-blocks. For each A-block followed by a B-block, finish all A macros except the last. Advance the last A macro (the carrier) until the unique passage through B; pause this incomplete carrier exactly once, execute the entire adjacent B-block of macros to completion, then resume the carrier to finish at A. It is possible because each complete B macro returns the same token to B. Finish any final A-block normally. The first starts obey their prescribed order; each macro's internal edges remain ordered. Exactly one interruption is made for each B-block, so \`h<=b(w)\`.

**Lower bound, one token.** The token initially must be at A. Consider the first start of the first B macro in each maximal B-block. An A-root macro started earlier, since an A first start precedes every B-block. Hence the token must have returned to B *after* that intervening A start. Immediately before this new B macro starts, one of the following must have happened:

(i) The token arrives at B in an unfinished A-root macro. Switching away from that incomplete A macro to the new B macro costs one interruption *at B*. Charge it to this B-block.

(ii) The token is at B because a previously started B-root macro has just finished. That finishing B macro must have started *before* the intervening A first start, because no new B macro was first started in the present B-block yet. Consequently this B macro stayed incomplete across an A first start and must have been interrupted earlier; charge one of its interruptions to this B-block.

These possibilities exhaust the ways to enable the first new B macro: a completed A macro ends at A, and a partially executed B macro cannot have its token at its own root B, since the directed simple cycle returns to the root only on completion. The charges are **injective**: type (i) is an interruption of an A-root macro *at B*, whereas type (ii) is of a B-root macro *away from B*; they cannot coincide. Two distinct type-(i) charges occur at distinct B first starts. Two type-(ii) charges belong to distinct B macros because a completed labeled macro is completed exactly once and cannot enable two different B-block first starts. Thus \`h>=b(w)\`, completing equality for K=1.

**Two or more tokens.** Put one initial token at each of A and B; run each labeled macro to completion in prescribed first-start order. Every macro returns its token to its own root. There are no interruptions, achieving the trivial nonnegative lower bound.

## 3. Corollary Z2 — unbounded chronology-dependent BRC residual

For arbitrary integer m>=1, let \`w_m=(A,B)^m\`, the alternating list of 2m individually labeled macros. There are precisely m B-blocks, so

\[
h_{\min}(1;w_m)=m.
\]

Under R762Y's **unrestricted** first-start order for the same macro multiset, d=2 and \`h_min(1)=d-1=1\`. Therefore enforcing chronology creates an exactly \`m-1\` excess interruption cost, unbounded as the number of macros grows.

A stronger same-input-summary comparison uses \`u_m=A^mB^m\`. Both \`u_m\` and \`w_m\` have exactly m A macros and m B macros, the same root histogram, the same nonnegative terminal directed PASS matrix \`M=2m M_cycle\` and the same terminal port imbalance. Their ordered-start one-token minima are respectively **1** and **m**. For q=3, m=2 this is the exact AABB versus ABAB witness: \`h_min(1)=1\` versus \`2\`; both admit \`h_min(2)=0\`.

For this specific two-root chronological preemption observer, the one-integer coordinate \`b(w)\` together with the seed budget K is a sufficient compressed observable. Terminal V29 PASS counts and the unordered named-root multiset are not sufficient. This is a time/source-order residual, not a claim that all future P000 and V39 observers factor through \`b(w)\`.

## 4. Independent exact verification

The reproducible standard-library checker \`research_notes/R762Z_CHRONOLOGY_FRONTIER_VERIFY.py\` enumerates every legal next edge of every labeled macro and uses a progress vector, fixed first-start index, exact port inventory and previous active macro. Memoized dynamic programming computes the **true optimum without calling the B-run formula**. It exhausts every two-root word of length 1..7 beginning at A, every second-root offset, and q=2..5 (K=1): **127, 254, 381 and 508** cases per q, respectively, or **1270** assertions in all, with no mismatches. The q=3 AABB/ABAB K=1,2 witness and alternating m=1..5 are checked separately. The deterministic JSON output is \`research_notes/R762Z_CHRONOLOGY_FRONTIER_EVIDENCE.json\`. The proof above establishes arbitrary finite q and k; the exhaustive computation crosschecks its declared finite scope.

## 5. Science provenance, exact boundary and next problem

Reused mathematical inputs: R762W PR #2354, R762X PR #2355, R762Y PR #2358, immutable Source publication TP2-8B7E13C5904A2D6F1142 and frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389. Current controls were read through \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, GLOBAL_KNOWLEDGE_V1, P000 startup and ACTIVE worldview. Source is held fixed.

The theorem is about an explicitly declared **auxiliary V29 token scheduler**, not an established native \`TRIADIC_CLOSURE_E\` event-admission or update law. It preserves six-dimensional X6 Cell/Link/Port provenance, event time ordering and individual source identities. No V17 frame or V39 holonomy claim is made. Formal Result and independent Driver review remain pending.

**Next discriminating unit:** derive actual native triadic Cell/Link/Port event admission and update; test whether chronological first starts and internal PASS interleaving are permitted, then compute source/frame-faithful V29 and V39 observers. Independently generalize the exact ordered-start frontier to three distinct macro roots, where the two-root run statistic no longer suffices.
