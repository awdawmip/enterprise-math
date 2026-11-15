# R762BB — Unordered visible-pair holonomy and exact BRC return residual

Status: AUTHOR-PROVED / EXACTLY ENUMERATED / NOT_REVIEWED
Date: 2026-11-15 (Asia/Shanghai)
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Scientific input pin: frozen task and publication at \`d5eb171f15801f54c0659a2bbf4e42844ba2d527\`, source P000 and native signed X6 torsor (original task source pin); predecessor candidate R762BA at \`fee3948cca65d81b89ad698be5d07a6b9fe391c5\`.
Author context: current research lane EM-X6-44BACF, original SID MCP-8b844b9054c94d40aaed0131426d3935 (historical attribution only; this file itself is not a protected CLAIM/Result).
Proof type: finite group action, exact positive named-source BRC enumeration.

## Model and question

Let A={1,2,3,4,5,6}, G=S6, C the P000 affine X6 Cell torsor. Fix an atomic *candidate relational* event with equal positive force quantum q and three pairwise distinct positive native axes: T(c;i,j,k;q,t,id). The three primitive force legs are incident at c and recorded with named Ports and ordered source occurrence (i,j,k); the center Cell does not move. This is the same clearly typed candidate as R762BA, not an assertion that P000 has admitted this triadic event as its actual TRIADIC_CLOSURE_E law. P000 fixes the triadic balance arity and 120° Enterprise orthogonality as starting axioms.

The new observer retains the UNORDERED set {i,j} of the first two legs, along with the Cell, q and declared t, but omits their order and the third leg k. It forgets an event identifier by explicit choice; all comparisons below fix the same non-source metadata. For an unordered pair U={i,j}, the candidate source fiber is
E_U = {(i,j,k),(j,i,k): k in A\U},
of size 8. K=Stab_G(U) is S2 x S4 (order 48), acting on all three labels. A based visible-pair frame loop means g in K; do not assume that every such g is physically realizable in the unfinished native V17/V39 dynamics.

## Theorem BB1 — eight-sheet equivariant completion and minimal future source residual

K acts transitively on E_U. Every nonempty G-invariant relational completion of all unordered two-leg observations contains the full eight-sheet fiber. There is no G-equivariant deterministic choice of a single fully ordered candidate triad over each U.

For any nonempty K-equivariant auxiliary-state fiber V_U with an equivariant readout f:V_U→E_U, every K-orbit in V_U has size divisible by 8. Eight is attainable with V_U=E_U. If future permitted tests can query both the first-leg order and the named third Port, exactly eight observer-equivalence classes are required; three bits are sufficient only after local labelling, not as a canonical S6-equivariant selector.

*Proof.* The subgroup K=S2×S4 acts transitively on its two possible first-leg orders and its four possible third axes. An individual full tuple has stabilizer {id on visible pair}×S3, of order 6; its K orbit has size 48/6=8. A G-equivariant section would require a K-fixed tuple in E_U, impossible. If f(v)=e, equivariance gives Stab_K(v)⊆Stab_K(e), hence |K·v|=8[Stab_K(e):Stab_K(v)], a positive multiple of 8. The named future tests separate any two distinct tuples, while retaining the tuple is sufficient. QED.

Note: If future operations never test first-leg order and genuinely factor only through unordered {i,j} and k, a four-class residual can be sufficient. This is a different declared observer interface.

## Theorem BB2 — full-source fixed return spectrum

For g=(τ,π) in S2×S4, let F_r(g) be the number of source records in E_U fixed after r repetitions of the based visible-pair loop g. Then, for every positive integer r,

F_r(g) = (2 if τ^r=id else 0) · Fix(π^r on the four hidden axes).

In particular F_1 is in {0,2,4,8}. Among the 48 elements of K, its exact distribution is 0:33, 2:8, 4:6, 8:1. Over the 15 unordered visible pairs this is 0:495, 2:120, 4:90, 8:15.

*Proof.* A tuple (a,b,k) is fixed precisely when the first ordered pair (a,b) returns and k returns. If τ^r is the identity both visible orders are fixed; if τ^r swaps, neither is fixed. The four hidden labels are independently permuted by π^r, giving the product. For τ=id, the S4 cycle types have counts (identity 1, single transposition 6, double transposition 3, 3-cycle 8, 4-cycle 6) and hidden fixed points (4,2,0,1,0). Thus the first-return counts among these 24 are (8:1,4:6,2:8,0:9). For τ=swap all 24 give zero, yielding 33 zero-return elements. Each unordered pair has a conjugate K. QED.

## Theorem BB3 — two-loop scalar signature is sufficient for *counts*, but not for named transport

The complete sequence (F_r(g))_(r≥1) has **exactly six** possible values as g ranges over K. Its equivalence classes are already determined by the first two values (F_1,F_2), and no one-loop observation suffices to separate all six classes. At each U, the six signatures and their exact multiplicities among K are:

| (F_1,F_2) | Multiplicity | Source class |
|---|---:|---|
| (8,8) | 1 | τ=id, π=id |
| (4,8) | 6 | τ=id, π=single transposition |
| (2,2) | 8 | τ=id, π=3-cycle |
| (0,8) | 13 | τ=id, π=double transposition; OR τ=swap with π of order 1 or 2 |
| (0,0) | 12 | π=4-cycle with either τ |
| (0,2) | 8 | τ=swap, π=3-cycle |

*Proof.* Each element of S4 has exactly one of the five displayed cycle types. Compute Fix(π^r) from that cycle type: for identity always 4; single transposition 2 at odd r,4 at even r; double transposition 0 at odd r,4 at even r; 3-cycle 1 unless 3 divides r (then 4); 4-cycle 0 unless 4 divides r (then 4). Multiply by the visible-order return factor of BB2. This yields precisely the six all-r sequences and the per-class counts in the table. Their (F_1,F_2) pairs are distinct; their F_1 values are not, so horizon 2 is both sufficient and sharp. QED.

A concrete provenance collision: visible identity plus hidden double transposition, and visible transposition plus hidden identity, have the same F_r sequence (0 for odd r, 8 for even r) while acting differently on each named source record. Therefore the six-class quotient is exact for the future family of scalar fixed-return counts, but it is not a source-preserving quotient for named-Port queries, nor for composition with arbitrary additional noncommuting frame actions.

## Relevance to the mother problem

R762BA's ordered visible-pair four-sheet model becomes an eight-sheet full-source model when first-leg order is hidden. Its S4 based-loop return spectrum changes to S2×S4 and admits distinguishable full-source behavior invisible in the unordered pair observation. This gives precise tests for a future actual native V39 loop observer: determine whether it preserves first-leg order, tests the hidden third Port, and which subgroup of K is genuinely realized by the admitted V17 frame-to-Port transport beta. V29 PASS/TRANSFER legality and a true signed TRIADIC_CLOSURE_E Cell/Link/Port incidence law remain the next substantive input. P000 and its frozen pins are unchanged.

## Reproducibility and source discipline

Companion JavaScript verifier uses only exact integer combinatorial enumeration, no floating-point or classical-π computation: 720 S6 permutations, 15 unordered base pairs, 48 stabilizer elements per pair, eight named source tuples per fiber, and powers r=1..12. The \`r<=12\` finite check is a cross-check; the all-r theorem follows symbolically from finite cycle-type classification (orders divide lcm(2,3,4)=12). Evidence JSON includes the six full period signatures, exact histogram and a concrete nonfaithfulness witness. The computation is positive provenance-labelled BRC counting, not signed-amplitude cancellation.

Status: author-side mathematical proof and computational cross-check; NOT_REVIEWED, no formal Result or independent Driver judgment. This independent research-note publication must not be mistaken for a Source PROGRESS or winning CLAIM.
