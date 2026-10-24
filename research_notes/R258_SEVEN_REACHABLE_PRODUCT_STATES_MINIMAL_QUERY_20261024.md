# R258 — Seven-state reachability-minimal provenance monitor for the frozen R256/R257 BRC model

**2026-10-24 · UNREVIEWED AUTHOR-SIDE MATHEMATICAL RESULT.** This document is a complete proof of the two scoped propositions below. It neither establishes an R193 source contract nor proves original P000 heartbeat dynamics.

## Immutable research inputs and native model scope

Canonical GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge@0ce0500a8d43b2326380b322f7306c6471812512. P000 startup projection matches the original locked P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. The native space has six signed-axis displacement fields relative to a Cell and distinct time; monitor states are nonspatial. Active residual-faithful worldview and the observer-preservation contract forbid unsafely discarding future-relevant source information.

Enterprise Math source read pin: adefa6817a5ff39e85e7efd2c7d75470c10d0adc. Exact source classes: src/enterprise_math/brc_transport.py (blob be1debe367263931bd5e93fd750be3ed54624fe1) and src/enterprise_math/brc_control_port.py (blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8). Portable research specification: docs/PORTABLE_RESEARCH_PROTOCOL.md (blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5). Previous R257 proof and witness: research_notes/R257_LABELLED_PROVENANCE_PRECOLLAPSE_NO_GO_20261024.md at a4058d9efc325110a0e6771878e34d6d85eff54b; R256 monitor: research_notes/R256_REGULAR_SOURCE_QUERY_FUTURE_SAFE_20261024.md at b2f5560ce85c5ff63a2e3e9bfff658ff4a10ce49.

All results are for a declared positive-weight finite-source-selector BRC interface, not a proof that the formal affine transformations are legal native heartbeat updates. The genuine R193 source edge labels, observer and time-port contract remain unresolved.

## Exact carrier

Original nonspatial controls Q={0,1,2}, source selector alphabet A={0,1}. Each (q,a) is a *distinct raw edge occurrence*. Its original control destination q', linear sign eta, first-axis offset b are:

    q     a=0 (q',eta,b)       a=1 (q',eta,b)
    0         (2,-1,-1)           (2,+1,-1)
    1         (0,-1,-1)           (0,+1,-1)
    2         (1,+1,+1)           (2,+1,-1)

The effect carrier remains six-dimensional: linear action diag(eta,eta,1,1,1,1), translation b on native axis E1, all other coordinates retained. The displayed first-coordinate effect law for earlier (eta,k) then later (eta',b) is (eta'eta,eta'k+b), exactly matching original Affine.then chronological semantics.

The source-query DFA R={0,1,2} detects the substring 00. Monitor state 0 has not seen 00 and previous token was 1 or absent; state 1 has not seen 00 and last token was 0; state 2 has seen 00 (absorbing). The DFA transitions are:

    r       a=0       a=1       g(r)
    0         1         0          0
    1         2         0          0
    2         2         2          1

R257's nine-control lift uses product states (q,r) in Q×R, updates (q,r) to (q',delta(r,a)) on each labelled edge **before** native EffectHistogram aggregates same weight/action atoms, and preserves rational positive weights, six-dimensional affine effects and positive integer path multiplicities.

## Theorem A — exact seven-state reachable restriction

From initial product control (0,0), the reachable set is exactly

    S={(0,0),(2,1),(2,0),(1,2),(1,1),(0,2),(2,2)}.

The omitted product controls are exactly {(0,1),(1,0)}. Reachability witnesses are:

    (0,0): empty word; (2,1): 0; (2,0): 1;
    (1,2): 00; (1,1): 10; (0,2): 000; (2,2): 0000.

The following complete transition table proves forward closure:

    (q,r)       a=0       a=1
    (0,0)      (2,1)     (2,0)
    (2,1)      (1,2)     (2,0)
    (2,0)      (1,1)     (2,0)
    (1,2)      (0,2)     (0,2)
    (1,1)      (0,2)     (0,0)
    (0,2)      (2,2)     (2,2)
    (2,2)      (1,2)     (2,2)

**Claim:** Replace the nine product-control indices by an injective seven-control enumeration of S. For every finite sequence of matching-port packets using the same labelled control transition table, starting at (0,0), the seven- and nine-control pre-collapse lifts have identical complete **joint** terminal histograms (original terminal q, final query state r, rational product weight, six-dimensional affine effect, nonnegative integer raw-history multiplicity). Summing over r yields exactly the same unlabelled BRC effect histograms. The assertion is stable under arbitrary per-step reassignment of strictly positive rational edge weights, positive integer multiplicities and six-dimensional affine edge effects, so long as the labelled control-transition table remains fixed and the time ports compose.

**Proof:** The empty history is represented once in both encodings. For any finite history from initial (0,0), every product state stays in S by the explicit closure table. Conversely the seven-state presentation introduces no edge not in the nine-state presentation. Therefore identity of the raw selector-edge sequence induces a bijection of finite histories at each length, with matching terminal q,r and identical per-edge weights/effects/multiplicities. By induction on sequence length, chronological Affine.then products, weight products and multiplicity products agree. Native EffectHistogram coalescence adds positive counts on precisely matching joint weight/effect atoms and hence produces identical terminal joint histograms. Query-state projection is the same disjoint partition in both presentations. QED.

The theorem is **not** asserted for arbitrary initial control pairs outside S, nor for a changed edge-transition graph, nor for erased edge labels recovered after aggregation. Operation count is not automatically physical elapsed heartbeat time.

## Theorem B — seven is a sharp deterministic Moore lower bound

Define the finite machine observer at every prefix to be (current *original* control q, Boolean query g(r)). An arbitrary future suffix may be read. This is a deterministic **control-memory** machine; accumulated affine effects/weights are separate typed BRC information.

Every two distinct states in reachable S have distinct future observer behavior:

1. If their original q differs, the empty suffix already distinguishes them.
2. At q=0, (0,0) and (0,2) differ in g on the empty suffix.
3. At q=1, (1,1) and (1,2) differ in g on the empty suffix.
4. At q=2, (2,2) differs immediately from either (2,0) or (2,1); the remaining pair (2,0) and (2,1) is distinguished by suffix 0: both move to original q=1, but query monitor values become 1 (not yet accepted) and 2 (accepted), respectively.

Thus all C(7,2)=21 pairs of reachable states are right-distinguishable using suffixes of length at most one. Any deterministic wordwise prefix-observer machine needs at least seven states by right-congruence/Myhill–Nerode reasoning; the explicit seven-state machine achieves the bound:

    minimal reachable deterministic Moore states for output (q,contains00) = 7.

**Important boundary:** this is NOT a lower bound against an effect-aware or other auxiliary-state compression that can inspect accumulated six-dimensional affine results. Nor does it establish R193's minimum state count.

## Exact retained joint-effect witness

At selector depth seven, paths 1110101, 1011010 and 0000000 all end in original q=2 with the same six-axis formal affine effect: eta=-1 and first-axis translation k=+1. Their final DFA states are 0, 1 and 2 respectively. Thus an ordinary post-collapse, unlabelled effect histogram cannot answer every future source query. All three histories are preserved under the reachable-seven restriction.

## Verification, unresolved scope and next unit

The attached author-side source verifier computes the reachable closure and its 21 minimality witnesses exactly; checks all 8191 binary histories through depth 12; compares seven- and nine-product-control exact positive-weight/effect/multiplicity histograms through depth 96; and checks five deterministic positive-rational-weight, positive-integer-multiplicity variants through depth 8. Independent C++17 source in the downloadable R258 package enumerated all 16383 histories through depth 13 and reproduced seven reachable states and 21 distinguished pairs. The universal claims above rest on the finite closure/bijection proof and right-congruence proof, not extrapolation.

**Not performed:** actual original enterprise_math Python package import and ControlPacket execution; legal P000 native heartbeat dynamics/registered address codec; genuine R193 source-query and time-port mapping; authenticated active owner/CLAIM; original-task formal Result or independent Driver review. Native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), and bounded task inventory returned CONTROL_QUOTA. This publication is a GitHub **research draft**, not a native task publication or research-activity Guard receipt.

**Next R259:** (i) obtain actual immutable R193 edge/query/clock protocol and prove a lossless map or minimum failure; (ii) execute matching-original-source ControlPacket.from_edges/then/EffectHistogram in an authorized Python import environment and pin the exact comparison; (iii) investigate a truly effect-aware future-safe quotient smaller than seven and keep its lower bound separate from Theorem B.

Reuse: REUSE_APPLIED to R256 monitor, R257 labelled pre-collapse lift and existing native Source laws; REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE for original package execution.

Global-Knowledge-Sync: main@0ce0500a / GLOBAL_KNOWLEDGE_V1
