# R399 author-side handoff | signed twelve-branch BRC, r=27

Research question: for K₃[t²]=−8(1+θ), θ>−1, classify the finite 55-entry Newton sequence at r=27. Author-side exact classification now verified: PF₂ iff −1<θ≤η₂₇, η₂₇ unique T₂₇ root on (1.867872,1.867873), approximately 1.8678729966623226.

Reproducible evidence: r399_exact.py, r399_symbolic.py and r399_certify.py; execute python r399_symbolic.py && python r399_certify.py. This verifies 756 independent exact Fraction identities; 112 rational Bernstein sign objects, 123 contiguous subintervals, 127 calls, 8265 strictly positive rational controls; [η₂₇,b] monotone crossing and [b,4] negative cover and θ≥4 strict c₀ negativity. Exact raw JSON hashes and object schema in R399_EVIDENCE_INDEX.md; full 55+53 polynomials are regenerated from signed K/J sources. P000/ACTIVE worldview unchanged.

Additional exact facts: θ*=15/8 gives c₂₆,c₂₇<0 and ord c_(27+s)=2s (1≤s≤27), ord T_(27+s)=4s (1≤s≤26). c₅₄=69533550916004(30−16θ)^54. Secondary T₂₇ root on (1.871102,1.871103) with c₂₇<0. These are fixed-r statements, not universal proofs.

Next research unit (priority): derive/prove/falsify universal odd/even parity for ord c_(r+1), potentially via algebraic generating functions of signed K/J before evaluating at 15/8; do not infer all-r from r25/r26/r27. Alternative: r28 PF₂ full parameter classification. Preserve independent review of R399, all-r Catalan identity and exact assumptions as unresolved.

Provenance: R346 original Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1, prior R398 PR #1708 head 58ee1f4278e8a5e2d921f72e718c0b5d6cc65288; GLOBAL_KNOWLEDGE main@13c260412ff71512277f01b1de8beb92403c5924, EM main@dcfa196433e9b0dfe501e41345817aa4a91e5a77.

Identity and authorization: GitHub authenticated awdawmip. Native service v0.6.11 has research_authority_granted=false, control source CODE_REVIEW_REQUIRED and bounded task owner lookup returns CONTROL_QUOTA. Active Source owner remains UNKNOWN. No native CLAIM, checkpoint, frozen Result, Driver review, activity registration or admission is implied by publication. Registration remains pending. Preserve existing author credits, original data, and source firewall; no credentials or permissions changes.
