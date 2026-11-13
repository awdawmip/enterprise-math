# Stage426-B: Unequal-length Euler/J/K transfer and a sharp K frontier

Date: 2026-11-04. Parent Stage425-B (75b8be402011e28e8b23599b5ffacb1919f764f), Draft PR #1736.
Scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Status: author-side math and exact execution, UNREVIEWED / NOT_ADMITTED.

## Definitions
The alphabet D consists of the 12 original signed X6 directions (+E1,-E1,...,+E6,-E6). A path word W=w1...wm has six-component chart-relative endpoint sum_i v(w_i); directed adjacency count J_W(a,b)=#{i:(w_i,w_(i+1))=(a,b)}. For two unequal-length source words P,Q, their positional equality observer is K(P,Q)=sum_(i=1)^min(m,n) [p_i=q_i]. These are typed ordered native axis labels; the auxiliary empty word is permitted for combinatorial testing.

## Theorem 426.1: Exact remaining-Euler/J/K polynomial for unequal-length paths
Fix m,n, initial directions of each nonempty word, and nonnegative 12-by-12 J_P,J_Q edge inventories summing to m-1,n-1 respectively. The polynomial C(z)=sum_(all admitted ordered word pairs) z^K is exactly computed by dynamic programming with state (i,lastP,lastQ,remaining_JP,remaining_JQ), at the absolute index i. For the next position, a nonexhausted word chooses one positive-remaining outgoing *edge type*, decreases its count and emits the target direction; an exhausted word emits no direction. The contribution is z^[a=b] if both emitted symbols exist, else 1; the two initial symbols contribute z^[firstP=firstQ] if both nonempty. Terminal state has coefficient 1 precisely on complete exhaustion of both edge inventories.

Proof: For fixed first symbol, any path gives exactly one ordered sequence of its directed adjacent edge types; conversely, a complete legal Euler traversal of a typed edge multiset reconstructs exactly that path. Pairing two traversals by absolute index gives the precise aligned comparisons, including the unmatched suffix of the longer path. There is one choice per edge type, *not* multiplicity-many choices for equal copies of a repeated edge. The product of the local z factors is z^K. An induction on remaining inventories establishes the recurrence, exact integer coefficients and memoization. QED.

The X6 endpoint is fixed by input data: endpoint(W)=v(first)+sum_(a,b)J_W(a,b)v(b). This is an exact O(d^2) precheck, not a hidden DP coordinate. Each word's J is kept separately; K is a joint observer, not inferred from separate endpoints.

Let h=min(m,n), M=max(m,n), d<=12. A coarse DP bound is S=(M+1)(d+1)^2 product_(a,b)(J_P(a,b)+1)(J_Q(a,b)+1) states, at most d^2 transitions each, h+1 BigInt output coefficients. The count bit size is at most 1+ceil((m+n)log_2(max(2,d))); a straightforward implementation requires O(S d^2 h B) bit operations for coefficient additions, with separately accounted O(S d^2 log(M+1)) state-key formation and O(S [d^2 log(M+1)+h B]) stored bits. This is polynomial in numeric dimensions under fixed alphabet but may be exponential in binary input length. Reading encoded edge inventories, initializing, recovering requested outputs and emitting actual words incur their distinct costs. A full word-pair list costs Omega(m+n) symbols per pair.

## Theorem 426.2: Sharp forward alignment frontier (K-only observer)
Let P,P' be frozen words of the same length m>n and Q one common word of length n; assume K(P,Q)=K(P',Q). The *only* allowed future operation is independently appending a native letter to Q, at most b times. All K observations after every legal such operation agree if and only if the ordered length-r segments P[n+1..n+r] and P'[n+1..n+r] are equal, with r=min(b,m-n).

Proof: After t appends, K changes by exactly the matching indicators at the newly reached positions n+1 through min(n+t,m). Equal segments give equal increments. If the segments differ, let j be their earliest differing index. Append arbitrary j-1 letters (earlier increments agree by the choice of j), and then append precisely P[n+j]. That matches P and not P', producing a one-count K difference. QED.

Theorem 426.2 concerns the exact frozen-longer-source, forward-Q-append, K-only future language. The full (endpoint,J,K,executability) observer under two-sided POP/APPEND also requires legality suffixes and deleted/reexposed matching pairs; this is the Stage427-B question.

## Verification
An actual Node.js exact integer checker was executed, with output STAGE426B_UNEQUAL_EULER_FRONTIER_EXACT_PASS. It fully enumerates 121 words of lengths 0..4 on a 3-direction subset (14,641 pairs; 13,225 Euler-input fibers), and 157 words of lengths 0..2 over all 12 native directions (24,649 pairs). Every DP K histogram equals the independently generated word-pair histogram, and endpoint reconstruction agrees. It checks 1,773 same-observation P pairs under 33,687 future-Q-append comparisons at budgets b=1..3. It reproduces Stage425's K=2 vs 1 witness and a same-J four-letter distribution [0,0,2,0,2]. Only the finite ranges were computationally exhausted; the general cases are supported by the proofs above.

## Next
Stage427-B: include two-sided bounded independent POP/APPEND and full (endpoint,J,K,operation-legality) observations, prove a minimal sufficient carrier or find a shortest exact counterexample. Also derive/refute the Stage424 original implementation's 68n-463 memo states and 85n-628 transitions.
