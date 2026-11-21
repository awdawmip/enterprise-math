# CBRC F7 Driver r465 — B13 extension of the frozen r464 witness requires changing old scalar coordinates

Date: 2026-11-22 (Asia/Taipei). Original F7 mathematical researcher: `EM-CBRCF7-83A1D4`. Frozen finite certificate constructor and this bounded audit: `EM-DVR-DEBB5E`. Scientific scope: the unchanged auxiliary two-coordinate F7 model, `A=I+uv^T` with `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, evenness `q(-x,y)=q(x,y)`, axis and two-mark conditions. No native-X6 lift is asserted.

## Exact statement and definition

Let `q_*` be the r464 globally defined admissible rational function proving `E*_{12}=1/2`. The complete 2,813-row, 62,463-byte witness `F7_R464_B12_Exact_Half_Witness_20261122.json` has SHA256 `340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`, integer denominator `M=30000000000000`. In the current run this exact artifact was recovered from the retained r464 certificate ZIP, hash-checked, and independently checked over all `25^4=390625` B12 inputs.

For `z=(a,b,c,d)`, `k=a-2b-c+2d` and
`D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.
Define the r464 B12 scalar-coordinate footprint
`F12 = { (|x|,y) : (x,y) occurs as one of the four q-arguments of some z in [-12,12]^4 }`.
Exact enumeration gives `|F12|=3073`.

**r465 scoped lemma.** Every even-in-first-coordinate function `q'` that satisfies `|D_{q'}(z)|<=1/2` for every `z in [-13,13]^4` differs from the particular frozen r464 witness `q_*` at **at least 53 distinct keys in `F12`**. Consequently, assigning only the scalar values at new, previously unused keys cannot extend the frozen r464 assignment to B13.

## Proof and explicit local witness

For r464's `q_*`, full integer enumeration of `27^4=531441` B13 inputs finds 16,432 violations of `|D|<=1/2`. Exactly 7,916 violating inputs have all four scalar argument keys inside `F12`. Greedily order these inputs by ascending sum of their support-key frequencies (then support cardinality, then lexicographic z). Select a violated input if its old-footprint support is disjoint from all previously selected supports. The exact computation selects 53 violated inputs, whose disjoint supports cover 210 distinct old-footprint keys. This is a finite combinatorial certificate: any B13-feasible `q'` must change at least one old-key value in each of the 53 disjoint supports, therefore at least 53 old-key values overall.

One self-contained witness is `z=(0,-13,0,1)`, with `k=28` and q-arguments `(28,15),(-28,-27),(0,-13),(0,1)`; all their even-coordinate keys belong to `F12`. At the frozen r464 rational assignment, the four numerators `M q_*(x,y)` are respectively `31079902636242, 23114601831999, 37715903596569, 35017662532569`, giving

`M D_{q_*}(z)=-18539061660897 < -M/2=-15000000000000`.

The largest B13 residual under this same frozen q is `48016153472784/M` in magnitude. The full 53-witness audit uses integers only and is reproducible via `research_checks/CBRC_F7_R465_B13_FROZEN_WITNESS_CHANGE_BOUND_20261122.py` on the above exact-hash r464 table.

## Interpretation, provenance, and status

This establishes a **correction lower bound for the particular r464 finite witness**, not an impossibility theorem for `E*_{13}=1/2`. A new B13 candidate may change old scalar-coordinate values while still satisfying every B12 constraint. The next useful test is an exact B13 feasibility or infeasibility certificate allowing those old values to vary.

Current code pin: `f1a8db61f1aa16f377c9d405814740d5267e5123:research_checks/CBRC_F7_R465_B13_FROZEN_WITNESS_CHANGE_BOUND_20261122.py`, readback verified against submitted bytes. Original r464 proof: `9f02cc6d638a62b36d504755d5b5c51afd11d806:research_notes/driver/2026-11-22_f7_r464_exact_B12_half_certificate.md`; original checker: `ae6fb6aef0ab4581ebf3cb094b4334755b4ec9a2:research_checks/CBRC_F7_R464_BOX12_EXACT_HALF_CERT_20261122.py`.

The full r464 62,463-byte table remains in the retained local ZIP, not yet on GitHub. Its exact hash must be preserved when publishing the data; the r465 code alone cannot substitute for those 2,813 frozen rows. Native Driver Review/Result acceptance and Source/Activity association remain separate and pending; the evidence here is a scoped new mathematical/finite combinatorial audit, not a formal native disposition.

## Source-publication addendum — 2026-11-22

The original 2,813-row frozen witness has now been **published and exact-content read back** from canonical GitHub Source. Immutable pin: `awdawmip/enterprise-math@43165a915ab1db44a6194fcda670443cd3bc5720:research_artifacts/F7_R464_B12_Exact_Half_Witness_20261122.json`; Git blob SHA1 `6d20fccdb175dd156d0e89a1a39553876ed8da0b`; 62,463 UTF-8 bytes; SHA256 `340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`. The original local-only status described the earlier historical state and is superseded for this artifact. Formal Native Review/Result/Activity admission is still a separate control operation.
