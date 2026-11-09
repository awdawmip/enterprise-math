# R662 Source alignment with frozen X6 V39 — static edge transport versus based-loop port

Date 2026-11-09 Asia/Shanghai. Exact historic source read: `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`, Git blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`; accompanying V37 source blob `daef41596f5eddf5f96862bc9614968459101358`. This read is source interpretation, **not a change of R462/V23/V27/V17/V29 frozen scientific pins**.

V39 has already established the coarsest exact **based-loop-packet** observer for its declared future language `L_JH`:
`Sigma_JH(gamma)=(j(gamma),h(gamma))`, with additive integer cycle current j and exact active-frame `h∈S3`; appending a permitted packet updates `j←j+j(packet)` and `h←h(packet)∘h`. V39 directly queries both j and h, so dropping either is unsafe within that language. V39's h is a **based packet/history holonomy readout**, not asserted to arise from a fixed per-geometric-edge S3 label.

R662's independent `U_edge` is an **alternative candidate realization** for histories whose h factors through static graph path transport. Its theorem that `U_{uv}=σ_vσ_u^{-1}` yields all-loop identity applies to a vertex-coboundary **edge field**; it does not make a nontrivial V39 packet h impossible. V39 need not store one U per edge; it can store h directly. R662's gauge class count `N_beta` does not replace V39's operation-safe quotient: R662 counts **static connections under all vertex gauge changes**, whereas V39 has a fixed based active frame and queries the specific group element h.

## Exact factorization criterion (graph path language)

Let G be a connected finite graph and b a base vertex. Consider a proposed packet-to-S3 map `h` on paths closed at b. If `h` respects word concatenation and is invariant under immediate edge/backtrack cancellation, and sends a reversed edge to the inverse transport wherever this reversal belongs to the declared path language, then it factors through `pi_1(G,b)`; equivalently it is a group homomorphism `pi_1(G,b)→S3` with path-order convention fixed.

**Sufficiency and constructive realization:** choose a spanning tree and `beta=m−n+1` fundamental loops. The graph fundamental group is free on those loop generators. Set all tree edge labels to the identity and each non-tree chord to its designated generator's h value (or inverse depending on orientation). Path multiplication reproduces h on every reduced based loop. Necessity follows from cancellation `U_e U_{e^{-1}}=e` and ordinary group multiplication along a fixed edge-labelled connection.

Thus V39 packet h is statically edge-realizable **if and only if** the above groupoid/backtrack conditions hold on its actual loop packet domain. V39's declared monoid composition by itself supplies the concatenation part, but does not specify reversibility/backtracking equivalence for all event packets. V29 TRANSFER counts are nonnegative and updates are irreversible in that sense, so no inverse packet is to be presumed.

**Next discriminating experiment:** read the exact V35/V36/V39 packet formation constraints and actual H, then exhibit either (a) a valid family satisfying cancellation, giving an explicit U-edge realization with β generators, or (b) a pair of allowed packet words with the same reduced geometric path but different resulting V17 transport, proving any fixed edge-only transporter insufficient for those histories. Either outcome narrows the mother objective's future-sufficient state question.

Review level: author-side source-alignment and algebraic derivation. No assertion that V39 is invalid or that the static edge field has been installed in the native model.
