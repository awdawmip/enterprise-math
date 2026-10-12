# Current Driver review of the frozen RSA exponent-collision Result

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Session: MCP-cd5eefdde49843898b2a70c1af94d8dd
Authority: DA-A1DB35C00ED2F8C2A9FA; actual server authorization comment 6115340052.
Prepared 2026-10-12. This current review does not reactivate any quarantined historical review or publication.

## Exact object and judgment

Task RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE, publication TP2-301CA54924787090237D, Result RR-2D43CCB30B906AFB6E20.
Current continuation300 reports FROZEN_RETURN/AWAITING_REVIEW, no live claim, no operational review and no legacy intake requirement. Own complete artifact302 verifies all 2037 Result bytes, SHA256 b69dd5e3107caf2e214e2e37df47e41d22d8a88d2e12a3cc165afa2bc7b6b9aa and blob48e59507afa688c544a584a84b35566f0bac362c at Source5591703654d7496a9ce6f3d9a8575e47158b2ae7. The full taskbook, return and execution record have also been read and their SHA256/blob digests independently recomputed against that packet. Return SHA2568fd60e5fd5be25c7fc17a8d142ed75616a0ceec73a89f7d2088f0221aef265b8; taskbook8f35f12e2d09e944915d28d6ffc033e913a69615e7f285832a70ab60f41c5220; ER eea6b712f9b772b248aa7d15a8c3260d18c032187e995e5bbd76819309ae5ee4. Original bytes and author's EM-RSACOL-C76042 identity are retained.

Judgment: ACCEPTED at this exact extraction-and-barrier Task scope; FOLLOWUP_TASK for the unchanged bounded external prior-art audit. The exposed-collision premise is essential. This is neither an efficient collision-generation procedure nor an improvement in factoring complexity. The larger research portfolio remains OPEN.

## Independent mathematical assessment

Let n=pq for distinct odd primes, x a unit, and a valid transcript provide Delta>0 with x^Delta=1. In proof-side CRT coordinates the orders are 2^a m_p and 2^b m_q, with odd m_p,m_q. If Delta=2^s u, then both odd parts divide u and u/m_p,u/m_q are odd. Thus the coordinates of x^u have exact orders 2^a,2^b, even if Delta contains redundant factors. The first global 1 in successive squaring occurs at t=max(a,b). When a<b its predecessor has signs (1,-1); when b<a the signs reverse; when a=b>0 the predecessor is (-1,-1), and when both are zero the initial value is already1. Hence the nontrivial-square-root mechanism succeeds iff a differs from b. Only the public transcript, modular arithmetic and gcd enter the extractor. This iff concerns the stated mechanism and grants no lower bound against other factoring methods.

For a uniform unit, independent local Sylow-2 components are uniform in C_(2^A),C_(2^B). Depth0 has probability2^-A and depth t>=1 has probability2^(t-1-A). Summing equal-depth pairs gives [1+sum_(t=1)^m 4^(t-1)]/2^(A+B)=(4^m+2)/(3*2^(A+B)). For fixed m the largest value occurs at A=B=m; it equals 1/3+2/(3*4^m), decreasing to1/3 and attaining1/2 exactly at m=1. Therefore success>=1/2 is sharp. Uniform-unit sampling is not interchangeable with conditioning on even order or sampling all residues.

The simultaneous exponent kernel is the lcm of the supplied element orders, equal to the exponent of their generated subgroup. The exponent of the complete unit group is lambda(n), proving the global power-map equality criterion. One nonzero globally annihilating Delta therefore supplies the classical randomized known-annihilator factor reduction; generating that Delta remains outside scope.

L=lcm(Delta_i) is a safe annihilator of the generated subgroup. The witness n65, x57,x47, each Delta4, has both displayed units square to-1 and their product14 square to1 with gcd(14-1,65)=13. This verifies strict amplification of the supplied transcript by combinations without repeating a semiprime census. Gcd of arbitrary local Delta_i does not generally annihilate either unit.

For the aggregate barrier, every element of H_2 has equal local depths iff both coordinate projections are injective. A nonzero projection kernel would have depth0 on one side and positive depth on the other; conversely injective projections identify H_2 with each image and preserve orders. The cyclic local factors therefore identify H_2 as the graph of an isomorphism between equal-order cyclic images. This is the exact subgroup mechanism barrier, not a claim of information-theoretic RSA security.

For t>=1 each local factor has a unique subgroup of order2^t, and there are phi(2^t) graphs. An ordered k-tuple generating a fixed graph has 2^(tk)-2^((t-1)k) choices. Distinct generated graphs do not double-count a tuple. Including the all-identity tuple yields exactly the return's aggregate failure law. All such tuples are a subset of separately failing tuples, so Fagg<=F1^k<=2^-k. Uniform exponent coefficient vectors modulo L push forward uniformly to H. This supplies an existential mechanism and finite randomized combination sampling; it does not establish a new collision-generation oracle.

## Evidence strength and no-repeat units

The author reported210 semiprimes,274904 units,18 aggregate formula cases and12 additional small aggregate parameter triples. I retain those as frozen regression evidence and do not relabel them as rerun by this Driver. The general claims above have elementary algebraic proofs; census output is corroboration. No new prime/semiprime campaign, KQB request, quota reset, or blanket Task redispatch occurred.

## Provenance judgment and necessary bounded successor

The already prepared primary-source audit is not a formal Result of the successor yet. It does materially inform interpretation:

- Miller1976 is read with its actual ERH-conditioned deterministic statements; HAC §8.2 Fact8.6 supplies the standard randomized ed-1 factor reduction.
- Shor quant-ph/9508027v2 §5 explicitly states the unequal local 2-depth criterion for order-based splitting. A supplied annihilator has the same odd-part terminal-sign chain as the exact order, so the local iff is an equivalent antecedent, not a new theorem claim.
- Abbassi–Bayle arXiv2505.00433v2 Prop4.1 together with Thm5.2 recovers the exact unconditional uniform-unit probability once the even-order conditioning is restored. Its all-residue factor phi(n)/n is a different sampling model.
- Goursat's graph-of-isomorphism core is classical. The collision packaging and exact aggregate ordered-tuple law have only a bounded partial-antecedent/no-exact-package-match judgment in the searched corpus; absence is not novelty proof.
- Monier strong-liar formulas have additional odd-part filtering and conditioning; they are adjacent and must not be substituted for the uniform-unit law.

Thus a bounded source-backed classification is worthwhile and already largely prepared. Reuse those bytes and recorded searches under the same audit Task's reviewed Gen2 publication; do not repeat literature retrieval or search merely because the previous publication was correctly isolated. Its mathematical scope, parent, five semantic sections and gates remain unchanged. The publication-scope code fix permits an independently authorized successor while preserving exact old quarantined bytes and authority isolation.

## Independence, typing and disposition boundary

This is a nonblind review of a historical author's frozen proof, not an identity-based claim of clean context. Root prior contribution IDs EM-DIRECT-E1F2B6, EM-DIRECT-FA0C27, EM-DIRECT-49ADE6, EM-DVR-C1A1D9, EM-DVR-4C90FB and current EM-DVR-FBF223 are disclosed. They do not overlap the original Result author. Delegated bounded source/probability preparations and shared Root context are disclosed; they are supporting papers rather than separately registered accepted Results.

These finite groups and probabilities are external classical arithmetic auxiliary readouts. The fixed P000 native Heartbeat X6 substrate and separately typed time remain unchanged; no full-X6 propagation or native-state collapse is claimed. Tool harvest is RESULT_ONLY at this Result's original strength; no new global tool family, L4, Working Truth, Foundation or canonical promotion is granted.

Required next step is the same bounded prior-art audit, after current Source publication/packet readback confirms its Gen2 operational state. The extraction Task may close at its satisfied hard target; that does not close the larger number-theory program.

