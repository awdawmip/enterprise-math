# BRC causal future peak quotient — author-side handoff (2026-10-24)

Scientific question: Is full historical peak M essential in the previously proved causal state (action counts c, residual R, historical max M), or is there a smaller exact sufficient state for every future suffix?

**New author-side answers:** (1) Given a fixed (c,R), the precise future-residual equivalence class of M is min(M,U(c)), where U(c)=sup_{c'≥c} δ(c'). (2) The conservative computable statistic H_B=min(M,B(c)) is an exact causal observer, with B(c) the sum of four good-edge containment probabilities. (3) Reachable word prefixes 0223 and 2203 have exactly the same c and R, different maxima, and **identical residual under every possible common future suffix**, certified by B(c)=29981759/62500000 being below both historical peaks. (4) Under positive rational actions U(c) is exactly finite-computable via 4*(998/1000)^n tail bound, although no optimized full-grid computation was done.

Author-side proof: CAUSAL_PEAK_FUTURE_EQUIVALENCE_AUTHOR_PROOF.zh-CN.md
Compact exact program: verify_causal_peak_quotient.py
Evidence and declared bounds: EXACT_EVIDENCE.json

Pinned global rule snapshot: awdawmip/chatgpt-global-knowledge main@779a23bbf80a705993a4be5ca3cabfa9bdb3a2fe.
Pinned project source: awdawmip/enterprise-math main@e7dd4d6ed0ec737aa7bbe31b837fe05ec3708edc.
Predecessor: awdawmip/enterprise-math@e6bccc31d7431f075b463a4de5a91373f1e8c86b.

BRC reuse: REUSE_APPLIED — the four-label positive-mass occupancy, countwise inclusion-exclusion and residual variation readout are reused exactly. Retained information: counts, current residual, future-relevant capped peak. Discarded information: historical maximum margin that no future permitted occupation can recover. This is an auxiliary model, not a native P000 six-dimensional Cell proof.

Real control boundary: authenticated static MCP identity can read but em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); em_control_tasks reported CONTROL_QUOTA. Canonical live Owner was not resolved. No own formal researcher session, CLAIM, checkpoint, frozen Result, independent Driver review or Foundation admission has been asserted. Unreviewed GitHub branch is only source-backed author evidence. No Google Drive fallback was needed for successful GitHub delivery.

Next mathematical unit: derive cheap tighter exact bounds to U(c) and a representation-theoretic cross-count future-equivalence condition, with explicit preservation of branch provenance. Preserve the P000 native X6 bridge as a separate unproved obligation.
