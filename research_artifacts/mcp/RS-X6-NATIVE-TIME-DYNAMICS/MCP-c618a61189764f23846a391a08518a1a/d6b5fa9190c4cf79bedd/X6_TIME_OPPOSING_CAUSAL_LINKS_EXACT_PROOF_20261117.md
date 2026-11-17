# X6 native-time: opposing two-chain causal-link theorem (author-side exact result)

2026-11-17 | Task RS-X6-NATIVE-TIME-DYNAMICS | Publication TP2-91D4A7C2F63805BE21A3 | Researcher EM-EMF6D046-5A2844 | CLAIM MCP-b7d9928b0aa18bb44389243e | RUN RUN-54541083d3b5df3dcf44a8f4, generation 1.

Status: **Exact conditional event-poset theorem**, independent mathematical review pending. This does not authorize a physical multi-Cell X6 event. P000 six-native-axis spatial typing, separate time dimension, triadic closure, signed port/branch provenance and frozen previous authorship are preserved.

## Input and new research scope
The previous authored theorem (2026-11-12) treats disjoint V1R C12 local chains and **one** hypothetical causal link. Reuse it unchanged:
- @f115d6abf67f4dd41fe8a4d89367a0b1d1caa55f research_notes/portable_direct/2026-11-12_x6_time_cut_lattice_and_C12_winding_residual_r2.md
- @c8a44eeb585f83be41a161f1492caae07f8066f6 research_notes/portable_direct/2026-11-12_x6_time_one_causal_crosslink_cut_polynomial_r2.md

Here take labeled chains A_1<...<A_a and B_1<...<B_b of event occurrences (a,b>=1). Add **opposing** hypothetical precedence links A_r<B_s and B_t<A_u with 1<=r,u<=a; 1<=s,t<=b. These are event relation symbols, not signed X6 axes, primitive force quanta or an actual native Cell/Link/Port admission.

## Theorem I: executable dependency guard
The combined directed event relation is acyclic **iff** r<u OR t<s.
Proof: A directed cycle must cross between chains using both crosslinks. It can close precisely when there is a directed chain segment B_s<=B_t (s<=t) and A_u<=A_r (u<=r). Their concatenation with A_r<B_s and B_t<A_u gives a cycle; conversely no other cross-chain route exists. A cyclic graph has no complete linear extension. QED.

## Theorem II: exact k-cut generating polynomial
Assume acyclicity. A prefix ideal is uniquely specified by the local completed counts (i,j), 0<=i<=a and 0<=j<=b, and is legal iff
(j<s OR i>=r) AND (i<u OR j>=t).

Let G_{p:q}(x)=sum_{k=p}^q x^k, with G=0 for an empty range. Then the exact reachable-cut polynomial is

C(x)=G_{0:a}(x)G_{0:b}(x)-G_{0:r-1}(x)G_{s:b}(x)-G_{u:a}(x)G_{0:t-1}(x).

In particular C(1)=(a+1)(b+1)-r(b-s+1)-(a-u+1)t.

Proof: The first edge forbids the prefix rectangle {i<r, j>=s}; the opposing edge forbids {i>=u,j<t}. If the two illegal rectangles intersect, then u<r and s<t, violating acyclicity, so the two subtractions are disjoint for the stated domain. Every legal ideal of a finite acyclic poset can be extended to a topological serialization; therefore every counted prefix is reachable. QED.

When a,b<=11, exact period 12 of each full decorated V1R local orbit makes the pair of local states injective on (i,j). Consequently [x^k]C(x) is the exact number of distinct *conditional-product-model* full decorated k-cut states. Distinguishing an unknown choice among N>0 such cuts costs ceil(log2 N) fixed-length selector bits (conditional on that declared cut observer).

## Theorem III: linear-extension DP
Set F(0,0)=1 and F(i,j)=0 for illegal or out-of-range prefixes; at any other legal prefix (i,j), F(i,j)=F(i-1,j)+F(i,j-1). Then F(a,b) is the exact number of legal complete serializations. Proof by the last event occurrence, which is A_i or B_j. QED.

## Exact verification
Separate standard-library Python checker uploaded with this report exhaustively verifies a,b in {1,2,3,4}, every r,u in 1..a, every s,t in 1..b: **900 models**. 500 acyclic models agree in (i) independently enumerated full serializations and their prefix sets, (ii) closed cut polynomial, (iii) dynamic-programming extension count. All 400 cyclic models have zero legal complete serializations. Arithmetic uses only exact integers. Illustrations (a,b;r,s;t,u):
- 2,2;1,2;1,2: cut histogram [1,2,1,2,1], 7 ideals, 4 serializations.
- 3,3;2,2;3,3: [1,2,2,1,1,1,1], 9 ideals, 3 serializations.
- 4,4;1,3;2,4: [1,2,3,3,3,3,3,2,1], 21 ideals, 60 serializations.
Exact finite tests cover only the stated parameter box; the mathematical proofs cover arbitrary finite positive chain lengths in the given assumptions.

## Live native-time frontier
Acyclicity of a *hypothetical event poset* is not a native-event permission certificate. The next source-based step is to find an actual admitted two-Cell event with declared source/target, three nonzero primitive force terms and TRIADIC_CLOSURE_E, resource/port read-write guard, signed BRC branch provenance, and temporal causal order; then test its actual dependency edges, cut polynomial and calibration. An opposed-cycle result is an obstruction to that particular serial execution hypothesis, not a P000 no-go. Other owner research and original Reviewer authority remain unchanged.
