# X6 r426 — Cell-only future probes versus path/frame-orbit parity: exact bridge audit

Date: 2026-11-20. Status: **author-side mathematical synthesis and cross-model audit**. This preserves r423–r425 as finite signed-frame orbit theorems at their stated strength; it is not an independent Native Review or a physical realization of the candidate group actions.

## Source and provenance

This continues the original RESEARCH_DRIVER logical research line EM-DVR-DEBB5E, with original X6 authors and accepted Foundation material retaining their separate credit. Exact referenced scientific sources:

- X6 native Cell torsor: `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, §§2–3, 9–12 (signed Z^6 torsor, primitive translations, path/BRC and observer hierarchy).
- Finite-group r424: `enterprise-math@c83635cd2e7c57dd2e664fc5df940bc041f30d40:research_notes/portable_direct/2026-11-20_x6_r424_one_step_future_parity_probe.md`.
- Reset-versus-cumulative r425: `enterprise-math@47e61f09f53fe5709a785e2a3c7bf68392b0dbd2:research_notes/portable_direct/2026-11-20_x6_r425_separate_vs_cumulative_future_probes.md`.
- Active P000 and `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json` and the Joint Relation Observer Preservation contract govern interpretation. No new P000 premise or change to their immutable scientific status is introduced.

## Exact theorem: coordinate-only futures cannot detect a positive-history ordering

Let `X` be the affine torsor for `Z^6` with chosen anchor `z0`, and let `T_i^+(z)=z+e_i` denote precisely the existing primitive coordinate adjacency. Fix an occurrence vector `c∈N_0^6` of length `n=Σ_i c_i`. Let `W_c` be the set of all positive-axis words with that fixed vector.

For `u=(i_1,…,i_n)∈W_c`, put `E(u)=z0+Σ_{k=1}^n e_{i_k}`. For any *fixed labelled* legal positive future word `w=(j_1,…,j_m)`, define its **post-history Cell trace** as
`
C_w(u)=(E(u), E(u)+e_{j_1}, …, E(u)+Σ_{k=1}^m e_{j_k}).
`
A family of separate probes may also reset to `E(u)` between such experiments. Time stamps fixed by the known step positions can accompany these traces.

**Theorem 1 (exact future-cell fiber):** Every `C_w` and every joint tuple of such separate/cumulative future traces is constant across `W_c`. Therefore for an observer factoring only through these post-history coordinate traces, all `|W_c|=n!/∏_i c_i!` histories remain in one observation fiber; the extra information required *to predict these futures from their common exact endpoint* is precisely **0 bits**, for any finite or unbounded family of fixed future coordinate commands.

**Proof.** The defining commutative torsor translations give `E(u)=z0+c`, independent of the order of `u`. Every subsequent Cell after the history is `z0+c+Σ_{k≤t}e_{j_k}`; a reset changes no starting Cell coordinate. Both assertions hold for every future prefix, so for their entire family. The quotient by the occurrence vector therefore satisfies future-observer fiber constancy on this **coordinate-only** language. QED.

**Theorem 2 (full prior trace retains exact path):** The full ordered **history** Cell trace `H(u)=(z0,z0+e_{i_1},…,E(u))` uniquely determines `u`, since successive differences equal distinct basis vectors `e_{i_k}`. Thus the worst-case extra fixed-length tag to restore this full history trace from its common endpoint on `W_c` is precisely `ceil(log2(n!/∏_i c_i!))` bits. This is about an available *past trace readout*, not the future-coordinate language of Theorem 1.

## Exact comparison with r425: a typed observer mismatch, not a contradiction

Take `c=(1,1,1,1,0,0)`, baseline calibration `S=∅`, and the candidate signed-permutation group `G_+=ker(pq)` in r425. There are 24 labelled histories. r425's observer of **whole-word signed-frame orbits** has baseline/separate/cumulative fiber sizes `24/24/12` when the distinct future labels are `5,6`. It therefore demands 1 parity bit to predict its cumulative orbit observation.

The native Cell *coordinate-only* observer instead has, for the same 24 histories and future sequence `e5,e6`, the identical post-history trace
`
(z0+(1,1,1,1,0,0), z0+(1,1,1,1,1,0), z0+(1,1,1,1,1,1)).
`
Its fiber remains `24`, so no parity bit is revealed. Conversely, retaining the entire historical Cell trace distinguishes all 24 histories (5 bits given the endpoint).

| Declared observation | Restricted fiber | Additional fixed tag |
|---|---:|---:|
| Future Cell coordinate trace after same endpoint | 24 | 0 bits |
| Candidate r425 cumulative `G_+` whole-word orbit | 12 (two classes) | 1 bit |
| Full historical ordered Cell trace | 1 (24 classes) | 5 bits |

The simple exact enumeration of all 24 permutations of four distinct axes corroborates `24` distinct history traces and one common post-history `e5,e6` Cell trace. The general theorems are proved algebraically, not by this finite enumeration.

## Consequence for native transfer and next discriminating experiment

Primitive coordinate adjacency establishes that the commands `e_j` exist. It does **not by itself** establish that a whole-word signed-frame orbit is the actual P000/Cell/Port/triadic/time observer, nor that its parity is a physical future readout. Any claim that r424/r425's parity splits are seen natively must identify at least one typed path/branch/Port/internal-state/rotation relation that retains the distinction and an admissible operation/readout that exposes it.

Precisely, suppose a richer state space `Y` admits a Cell projection `q:Y→X` and declared future transition/readout maps. If every admissible future update descends through `q` and every declared future readout factors through `q`, equal Cell states remain indistinguishable under all future compositions. If a demonstrated native future readout distinguishes two such states, at least one of those two descent/factorization properties fails and the additional distinguishing state must be preserved or repaired. No claim that all full P000 packet states reduce to Cell coordinates is made.

The next useful bridge test is to select an actual legal triadic Cell/Port/branch/time event (not merely a candidate signed-letter orbit), compute both paths' complete typed pre/post-state and future observation, and check whether the two orderings can be separated. A positive native witness would identify a residual carrier; a negative result for a specific observer would give a scope-typed safe quotient. Existing X6 published/native researchers and claims remain authoritative.

**Status:** One author-side cross-model mathematical audit and exact counterexample to the *unqualified native Cell-coordinate reading* of the r425 orbit split; r425's formal theorem remains valid. Native independent review = pending, Native Result newly admitted = 0, formal Task closed = 0, parent objective closed = 0. Source/Activity association remains pending for this original Driver identity.
