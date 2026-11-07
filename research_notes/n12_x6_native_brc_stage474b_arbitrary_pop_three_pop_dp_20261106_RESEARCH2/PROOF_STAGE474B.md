# Stage474-B: arbitrary finite POP repair and three-POP exact BRC counts

Date: 2026-11-06. Author-side proof, exact-integer experimental verification, independent review pending.
Parent frontier: Stage473-B at commit a5cb7f2fb79d1f82e8e0476b5d59839fb93e33d7 in Draft PR #1736.
Frozen scientific pin: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current rules read independently.

## Observer, operations, and exact repair theorem

Let 2<=m<n. Original P and Q have lengths m,n and first direction A, with each step in Sigma={A=+E1,B=+E2,C=+E3}, embedded in the six-dimensional signed X6 native space. The complete initial Phi includes both full signed six-dimensional endpoints, both directed 12x12 adjacency matrices, both lengths, and K=sum_(i=1)^m [P_i=Q_i]. Ordered source histories are distinct raw BRC branches with positive unit mass.

A labeled future is any legal interleaving of POP_P<=k, APPEND_P<=k, POP_Q<=h, APPEND_Q<=1, where 1<=k<=m-1 and h>=0. POP never reduces length below 1. Every APPEND may use any of the twelve native signed X6 directions; appended steps can later be popped. Observe the same complete Phi after each action, and compare two histories under every identical labeled legal future.

Set t=max(1,n-h), and define
L_t=(Q_t, ((P_i,Q_i)) for t<i<=m, (Q_i) for max(t+1,m+1)<=i<=n).
Empty index intervals are empty. Define the repair key
R(k,h)=(L_t, (P_i) for m-k<=i<=m-1, (Q_j) for m-k+1<=j<=min(n,m+k)).
Repeated labels may be removed from a codec but are retained in this mathematical definition.

**Theorem 474.1.** On each fixed complete initial Phi fiber, the full labeled future-observation trees agree exactly if and only if R(k,h) agree, for **every finite** k,h in the declared ranges.

Necessity: From fixed first step and directed adjacency, out(a)-in(a)=[a=first]-[a=last], determining the last step. POP_P reveals P_(m-k)..P_m; POP_Q reveals Q_t..Q_n. For each t<i<=m, POP Q to i-1 and APPEND Q with every direction a; the resulting K increment is [P_i=a]. For each m-k+1<=j<=m, POP P to j-1, then APPEND P with direction a; the increment is [Q_j=a]. For m<j<=min(n,m+k), APPEND P to position j while varying the last appended direction; its K increment recovers Q_j. Thus each key letter is recoverable by legal futures.

Sufficiency: After any action word, the surviving original P and Q prefixes have lengths alpha>=m-k, beta>=t, followed by appended steps determined by the labeled word. Phi and the known deleted original suffixes reconstruct endpoints and adjacency exactly, including insertion edges and POP-of-APPEND cases. Reconstruct K from its initial value: an original-original comparison disappears only where i>alpha or i>beta. If i>beta>=t, P_i,Q_i are in L_t. If i>alpha>=m-k, P_i is in the P boundary and Q_i either lies in the Q boundary or Q suffix. A new Q letter compared with original P at i requires i>beta>=t, so P_i is in L_t. A new P letter compared with original Q at i belongs to m-k+1<=i<=m+k, so Q_i is in the Q boundary. Two new letters are both known from actions. Hence all intermediate K are fixed; induction in the labeled action word finishes the proof. The same argument works for any fixed finite original subset of the twelve signed directions.

For k=3, the three additional original labels relative to k=2 are P_(m-3), Q_(m-2), Q_(m+3) when the latter exists. Three strict examples with identical initial Phi and identical k=2 keys:

* P_(m-3): m=12,n=14, P1=AAABAAAACAAA, P2=AAACAAAABAAA, Q=A^14. Three POP_P leave different last directions and directed adjacency.
* Q_(m-2): m=7,n=13, P=A^7, Q1=AAAABAAAAACAA, Q2=AAAACAAAAABAA. POP_P three times then APPEND_P(B) gives K=5 versus K=4.
* Q_(m+3): m=7,n=15, P=A^7, Q1=AAAAAAAAABAACAA, Q2=AAAAAAAAACAABAA. APPEND_P(A,A,B) gives K=10 versus K=9.

These witnesses certify individual necessity in some fibers, not universal independence of tags.

## Theorem 474.2: exact positive-BRC support, population, and rank

For fixed original ternary alphabet, k=3, and 1<=t<=m-2, the growing-window key is equivalent, on a fixed Phi fiber, to the visible word
(Q_t, hidden P labels among P_(m-3),P_(m-2) with index<=t, ((P_i,Q_i)) for t<i<=m, (Q_i) for m<i<=n).
There are at most two hidden P labels. The positive-prefix BRC table to t stores last P/Q, previous P, two 3x3 directed-edge profiles, prefix K and exact nonnegative integer branch mass. Group its records by the declared head label. A deterministic suffix automaton emits visible P/Q pairs and Q-only tail letters, tracking suffix edges and matches. At each terminal, complementary edge counts, the boundary P_t->P_(t+1) edge and residual K select compatible prefix states; their masses sum to M(key). The Boolean contribution is [M(key)>0]. Recursion over distinct visible suffix words counts support, while positive branch masses preserve all raw multiplicity. Lexicographic rank adds Boolean support of earlier children; inverse rank descends by it. Sum M(key) equals the original raw population.

For fixed ternary directions and k=3 the edge counters (18), K, and position yield a conservative O(n^20) exact-integer arithmetic bound; masses have O(n) bits. This bound is not an end-to-end optimized runtime. For k growing with n, compressing the possible 3^k boundary assignments is an open additional algorithmic question.

## Actual computations and integrity scope

A separate independently executed local Python3 standard-library checker (the local execution file is supplied alongside this handoff) verified 10 small configurations, 465 selected full observer fibers, 3568 exact classes with population and rank/unrank checks, and three strict witnesses. Its bounded full 12-direction future-action comparison visited 33085 equal-key states without differences (all action words of length <=4) and found a differing pair at depth 1. In the Stage470 canonical big fiber m=35,n=56,P=A^35,K=18, Q directed edge multiplicities AA=3,AB=BA=14,AC=CA=12, the raw mass is 11154643500: support at t=8 is 4618757880, at t=32 is 675840, and at t=33 is 394240; the three deterministic suffix-state counts are 8221,4083,3756. All tests use exact integer arithmetic.

STAGE474B.py published here is a separately generated/rebased source derivative of the prior Stage471 implementation with the new hidden boundary-label repair; it was **not** the byte-identical file used by that independent local execution. The executed local source SHA256 and complete evidence summary are recorded in STAGE474B_EXECUTED.json. The proof establishes the arbitrary-k semantic statement; the deployed algorithm source here covers the t<=m-2 k=3 case. Both remain author-side and unreviewed.

Next: implement the t>=m-1 three-POP transfer, independently review the generalized repair proof and investigate growing-k head compression.