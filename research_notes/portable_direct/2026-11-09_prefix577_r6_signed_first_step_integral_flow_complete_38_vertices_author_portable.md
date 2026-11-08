# BRC-X6 signed first-step policy polytope: exact network-flow integrality and all 38 vertices

Date: 2026-11-09 Asia/Hong_Kong. Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`; unchanged 96 native ports, six original labeled actions, complete seven-output observation `(R1,...,R6,K)` and native target port, all nine roots `0,±e1,±e2,±e3,±e4`. **Research status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**. No native CM experiment, Source CLAIM or Result is asserted.

## New theorem: complete vertex classification

Let four initial source ports `(6,7,28,29)` have signed coefficients `s=(+1,-1,-1,+1)`. Allow a separate six-action first-step probability distribution `x[p,a]` at each port, with `x[p,a]≥0` and `Σ_a x[p,a]=1`. Write `A_r(p,a)=(native target port, complete seven-output reward W)`. Define the exact signed target/output balance `C_r(x)(o)=Σ_{(p,a):A_r(p,a)=o}s_p x[p,a]` at each outcome atom `o`.

The predecessor portable author result at commit `7df4937038f4a1a4106d53970f9e1d64da40a204` identified exactly nine nontrivial target/output balance equations, a 12-dimensional solution polytope in 24 coordinates, and 38 feasible deterministic action tuples. **This note completes the stronger, previously unresolved classification: all vertices are integral, and precisely those 38 pure policies comprise the entire vertex set.** Every feasible stochastic policy is a convex combination of at most **13** of the 38 deterministic preserving controllers. In particular there are **no fractional extreme policies**.

## Exact proof: signed incidence, total unimodularity

Construct a bipartite graph with four source-port nodes `S_6,S_7,S_28,S_29` and nine distinct output-atom nodes `O_o`, one edge `(p,a)` for every original action `a` at every source `p`: 13 nodes, 24 edges. Its defining linear system consists of the four source-normalization equations and the nine signed atom-balance equations. The graph is connected for all nine frozen roots.

The matrix column for edge `(p,a)` originally has `+1` at source row `S_p` and `s_p` at outcome row `O_{A_r(p,a)}`. Multiply source row `S_p` by `s_p`, and all outcome rows by `−1`. The column becomes `(+s_p at S_p, −s_p at O_o)`, exactly a directed graph incidence column. Thus the transformed matrix, and therefore the original matrix, is totally unimodular. The demands at the transformed source nodes are the integers `s_p`, and all outcome demands are zero. Every vertex of the nonnegative feasible flow system is hence an integer vector. The normalization `Σ_a x[p,a]=1` forces each source to select exactly one action with probability 1; all others vanish. Conversely each feasible pure controller is already a vertex of the ambient product of four probability simplices, hence is a vertex of this subpolytope.

The connected incidence rank is `13−1=12`, and the all-positive `x[p,a]=1/6` is feasible. Therefore the relative affine dimension remains exactly `24−12=12`. Carathéodory's theorem supplies a mixture of at most `12+1=13` vertices. A constructive exact rational decomposition follows from support-graph cycle perturbations: if support contains a cycle, shift flow along it in positive and negative directions to expose a zero edge in each branch while keeping node demands; if support is a forest, peel leaves with integer demands and inductively obtain an integral pure controller. Repeat until all pieces are vertices.

The complete pure-policy count has a concise integer certificate. The signed balance for four sources amounts to equality of the two positive outcome multisets and two negative outcome multisets. Two pairings cover all possibilities:
`(6↔7,29↔28)` has `5×5=25` native action tuples; `(6↔28,29↔7)` has `4×4=16`; their intersection has exactly `3`. Hence **`38=25+16−3`** and there are exactly 38 vertices, for each of the nine roots. Exhaustive independent verification checks all `9×6^4=11,664` pure controllers; the connected graph, nine atoms, 24 action-edges and pairing numbers are extracted from the original frozen native action kernel. Rerun in independently extracted ZIP reproduces the exact certificate.

A nontrivial fractional feasible example is the 1/2–1/2 mixture of pure tuples `(a0,a0,a0,a0)` and `(a1,a1,a3,a3)`; every deterministic realization individually preserves the complete signed target/output atom cancellation, unlike a mere numerical equality after averaging.

The new mathematical result is a **BRC observer-safe convex-coupling certificate**: signed port provenance, all six spatial reward coordinates, target, gate and future operations are retained under the exact one-step operator. Neither action labels nor gate are treated as additional spatial axes. The output identity persists under arbitrary shared continuation on observed state/history, but is not asserted under operations that separately retain unreported hidden original-port identity.

## Exact reusable artifacts and provenance

Self-contained eight-file original-kernel/certificate/verifier/proof package: `PREFIX577_R6_INTEGRAL_FLOW_COMPLETE_38_VERTICES_AUTHOR_PORTABLE_20261109.zip`, size **16,518 bytes**, SHA-256 `5e2c511f4c2c1ec60e7beee71414266636ac876bf3d232a419bf8fa493805d96`. Machine certificate `INTEGRAL_FLOW_VERTEX_CERTIFICATE.json` SHA-256 `30bf8deb9dd844fc99370d62e7550859049542d52031cef2cdde5c71b87ad67b`. Verifier `verify_integral_flow_polytope.py` and manifest preserve the exact original BRC native kernel hash and full nine-root counts. Both original and independently extracted runs PASS. The integrality theorem is structural; the finite enumeration only certifies the native graph/pairing counts.

Previous signed identities, predictive ranks and the 12D policy equations keep attribution to original author commits `f20a2c42e0c8db2435215b3cf1a212e7e507644e` and `7df4937038f4a1a4106d53970f9e1d64da40a204`; only complete extreme-point classification, integral flow proof, and ≤13-mixture theorem are newly added here.

## Source-bound continuation boundary

The canonical D25 original-class divided-power module H0/B0, `[X]U mod p²`, Frobenius direction/eta, native κ / `Delta_p−R_p` and real CM experiment remain unresolved; D24 native Result and Driver Review remain terminal. The original UR four-file V2 bundle remains missing (94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). This is **not** its replacement.

Source exact-current continuation request `h40-r11-d25-exact-continuation-20261109t0137-read-v1` returned `FAILED/GITHUB_HTTP_403`; current private Source own-session capability and winning claim remain unverified. The attempted client checkpoint revision18 failed before sending (`BACKEND_IDENTITY_CHECK_UNAVAILABLE,operation_sent=false`). Native Source checkpoint and independent review have not been performed. A detailed authorized author-only continuation handoff including the original old/new request IDs and checkpoints is at GitHub commit `911a3f74f614ea74d778bedb0f4ac15cf963e5c6`, `research_notes/portable_direct/2026-11-09_h40_r11_task_research_portable_handoff_author_only.md`; it also predates this theorem.

Next legitimate research target, if nonduplicative: minimal facets or a more efficient exact coupling/unranking algorithm for the full 38-vertex policy polytope. Formal Source progress and reviewer admission need current authorized own Source session, exact claim and writer/provenance readback.
