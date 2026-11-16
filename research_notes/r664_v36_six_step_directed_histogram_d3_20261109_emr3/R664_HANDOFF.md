# R664 handoff — six-step shortest directed-histogram collision with different V17 D3

**Date:** 2026-11-09 (Asia/Shanghai)  
**Researcher-ID:** EM-X6-B4E7F1 · **Research-Activity-ID:** RA-F8B77ECD77EB4C6809BA008A  
**Task:** RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW · publication TP2-47D65B35A7D48082EFBB  
**Original frozen science:** R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; historic V17/V20/V36 unchanged.  
**Prior author frontier:** R663@ba21fd9dee43a703af8641fa95b9955645c06171; V36 source blob b104e09cdb7479d0d981492ddfb20b713cc817d9.  
**Native identity status:** Source activity registered, author-side research; formal Claim/Result/Driver not asserted here.

## Scientific increment

For based closed words in the 20-vertex Johnson graph J(6,3), the complete **directed triad-transition histogram** loses V17 slot holonomy for the first time at **word length 6** (within the stated all-words domain).

Direct exact counting:
- n=2: 9 closed, 9 directed-edge histograms, 0 ambiguous.
- n=3: 36 closed, 36 histograms, 0 ambiguous.
- n=4: 369 closed, 333 histograms, 0 ambiguous.
- n=5: 2952 closed, 2628 histograms, 0 ambiguous.
- n=6: 26937 closed, 22647 histograms, **108 ambiguous histograms / 288 ordered word pairs with unequal h**.

Explicit witness:
- A = (012,013,023,012), h(A)=(0,2,1).
- B = (012,013,123,012), h(B)=(2,1,0).
- AB vs BA have identical directed-edge histogram but h(AB)=(1,2,0) and h(BA)=(2,0,1).
- Relative Δ=h(BA)h(AB)^{-1}=(1,2,0), a nontrivial 3-cycle.

A native X6 6-Cell unit-step directed ring (six positions listed in the proof) realizes AB or BA under V36's deterministic V20 neighbor-copy rule; after six layers active triads return and Cell0 differs by h. Same physical 6-Cell ring and histogram; different **initial label distribution**. This refines R663's four-step all-S3-image result into a shortest verified **same-histogram** obstruction.

## Evidence and reuse

`R664_PROOF.zh-CN.md` contains the full statement, proof and X6 chart; `R664_VERIFY.py` exhaustive enumeration, independent position-permutation crosscheck and six-cell realization; `R664_EVIDENCE.json` exact counts and witnesses. Local CPython standard library verification passed marker `R664_MINIMAL_SIX_STEP_HISTOGRAM_D3_COLLISION_EXACT_PASS`. No external packages or real-number approximation.

**BRC reuse resolution:** `COMPOSE_APPLIED` for the exact V17 group residual and signed-histogram information-fidelity principle; V39 based-loop `(j,h)` retained as the already-proposed operation-safe observer for its declared packet language. No new native PF10 arithmetic was introduced; no result admission or global dynamics theorem is claimed.

## Next independent research unit

Take the current V29 permitted port graph `H` and the actual synchronous/asynchronous scheduler (V35–V39), then construct a two-loop finite Cell graph sharing a vertex. Test: (1) whether the R664 pair can occur as allowed event schedules with the same typed V29 totals; (2) whether `(j,h)` together with local triads, slots and margins is future-sufficient; (3) exact minimal memory if the scheduler observes source pairing; (4) locality, continuity, rotation covariance. Avoid replacing a frozen scientific pin with latest control rule.

**Control scope:** Current Source task read 2026-11-09T06:23:06Z: HANDOFF_READY / NEEDS_DISPATCH, owner taskbook/unassigned, publication TP2-47D65B35A7D48082EFBB. Formal-task CLAIM requires a separate positive writer receipt; repository author-side branch publication is not it.
