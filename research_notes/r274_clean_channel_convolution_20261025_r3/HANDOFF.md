# R274 — exact clean-channel convolution: research handoff

**Scope:** the fixed R268–R273 positive-weight ordered affine BRC auxiliary six-channel automaton; not P000 native physics.

**Author-side result:** For every n≥1 and every full effect g, the clean q=1 histogram is exactly
`Q_n=P_n+P_(n-2)+P_(n-3)⋆δ_(-1,-1)`, where P is clean q=0 reset and right convolution preserves order and positive original path multiplicity. Proof is an exhaustive three-class word bijection based on final `10`: q2 with prefix ending 1 ↔ reset word final `01`; q0 prefix + `10`; q0 prefix + `010`. Thus **Q_n(g)≥P_n(g)** at all effects and all n≥1, and q=1 clean can be removed from the minimization defining six-channel B_n with no finite-length loss.

The other clean histogram satisfies the exact effect-level recurrence
`R_n=R_(n-1)⋆δ_(+1,-1)+P_(n-1)⋆δ_(-1,-1)+P_(n-1)⋆δ_(+1,-1)`. Its unrolled right-convolution is in the proof; unlike total-mass estimates it retains the full affine effect.

**Executed evidence:** standalone Python-standard-library checker reconstructs raw transitions; depths 0..400, 8191 independent enumerated raw words at depths 0..12, 400 exact q1 histogram decompositions, 400 q2 recurrences, 157212 individual comparisons establishing Q≥P in the covered finite run. `EXACT_EVIDENCE.json` includes recorded anchors and precise coverage. The universal theorem is from word-class bijections, not finite checking. On 0..400, R<P occurs only at n=0,3,4,6,7,10,11, one effect at each; this **does not** establish the all-n conjecture for n≥12.

**Next exact mathematical question:** prove `∀n≥12,∀g:R_n(g)≥P_n(g)` from the right-convolution, or produce a counterexample, then analyze the dirty q0/q1/q2 channels to determine R273's effective equality threshold N. Separate unresolved tasks: D(6) aggregation and native R193/P000 port transfer.

**Read provenance:** GLOBAL_KNOWLEDGE_V1 main@d232a89119d9e4be10657da018198f4fd3ab8d98, P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; initial EM main@0463187e6425367d643415366869423e35013e7e; R272 paper 39c4801a51850d58f75ef71c9d4721e9ed8c6316; R273 author-side local-limit branch@25762051437bf05dc4810ebc41beba28a7fcf28f. R272 typed BRC / exact integer histogram semantics `REUSE_EXECUTED`; full six-slot physical transfer is not claimed.

**Authorization:** connected GitHub principal awdawmip; `em_control_tasks=CONTROL_QUOTA`, `em_session_start=STATIC_READONLY_SCOPE_DENIED` / `operation_sent=false`. Research activity is local-client identified, not a native session or formal task CLAIM. No Result, Driver review or Foundation promotion. Branch persistence does not make author-side mathematics canonically admitted.
