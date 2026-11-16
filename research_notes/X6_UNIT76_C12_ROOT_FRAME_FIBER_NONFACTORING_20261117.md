# X6 Unit76 — All-20 triadic C12 root readout loses source-frame information

Date: 2026-11-17, 06:xx Asia/Hong_Kong. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Own on-hour Research provenance: `EM-X6-FB6990` / `MCP-082892eb480e45dea6d4b9fcc0491034`, conversation `chatgpt-research-onhour-enterprise-math-20260923`. This is author mathematics and bounded live-consumer audit: **AUTHOR-PROVED / EXACT FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## 1. Exact source and input scope

Frozen scientific input is signed P000 V5 native Cell `Z^6`, pinned at `59538f585d037d09ef687b28715c4bc1a3f9fe03`. The separately current downstream executable source at `awdawmip/enterprise-math@76570a3b4dd3416bd5c2a90ec4edd0d955be3175` was actually read:

- `experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py`, Git blob `c446d0327f9bf643d5796348ba46cafe96d2915d`, especially `q_triad` / `act` / `power` and the six-phase orbit.
- `experiments/viete_x6_all20_triadic_root_c24_20260906/check_viete_x6_all20_triadic_root_c24.py`, blob `aa84515187c4319a6f8a65e65d12d6edbaae67fb`, especially lines 64–113: all 20 selected triples, two chirality branches, C12 outer microtrace root at index 3 and native two-step BRC checks.
- `experiments/viete_x6_outer_law_selection_20260906/check_viete_x6_outer_law_selection.py`, blob `2afe9637de17735707aaa5298b7a6d241f9fe696`, lines 64–106: INNER/OUTER branch horizon, a different provenance component.
- `experiments/viete_x6_fixed_radius_c12_20260905/check_viete_x6_fixed_radius_c12.py`, blob `a9be9405c199ccfc6c90abebec416ab40745cd5f`, lines 16–92 and 137–190: fixed FCC STAR signed carrier images versus six-axis native steps.
- `experiments/viete_x6_prostate_memory_obstruction_20260905/check_prostate_memory_obstruction.py`, blob `ea3273e1b1b05b9ea16efadc6351630fedfb22dd`, lines 22–64 and 68–111: periodic successor/memory and within-frame macro branch loss.

These exact named file observations extend the existing 28-LP consumer matrix; the original tests/benchmarks were **read, not rerun** in this unit. This audit does not overwrite their original source or infer a new P000 identity.

## 2. New exact source-frame fiber theorem

Work in the original six named signed native axes, with `e_i` the native positive primitive vector. Let `1 <= i < j < k <= 6`. Define the signed permutation `q=q_(i,j,k)` by

`q(e_i)=-e_j, q(e_j)=-e_k, q(e_k)=-e_i`, fixing all other basis axes.

This is the actual `q_triad` convention. It has `q^6=id`; starting from `e_i`, the positive-chirality macro orbit is exactly

`(e_i,-e_j,e_k,-e_i,e_j,-e_k)`.

The reverse chirality is obtained with `q^-1). The live `outer_cycle` emits `a_r, a_r+a_(r+1)` and its root readout is its zero-based index 3. Therefore the two native signed C12 root cells are precisely

`R_+(i,j,k)=e_k-e_j,  R_-(i,j,k)=e_j-e_k.`                                  **(1)**

Each has exactly two nonzero named native coordinates, `G=2`, shortest step count `T=2` and positive natural shortest BRC multiplicity `N_BRC=2`. Crucially, both roots forget **which smaller third axis i formed their original oriented triad**.

For each `j,k` with `2<=j<k<=6`, there are exactly `j-1` possible values of `i`. Hence the root-only observer from 20 triads x 2 orientations produces **40 labeled source observations but only 20 distinct signed native root cells**. Exact root-fiber sizes are:

| Number of source triad/orientation labels per root | Distinct signed roots | Source readouts |
|---|---:|---:|
| 1 | 8 | 8 |
| 2 | 6 | 12 |
| 3 | 4 | 12 |
| 4 | 2 | 8 |
| **Total** | **20** | **40** |

This is a complete all-20 finite classification, not a statement about all FCC carrier chart roots. The chosen 20 triples are all `C(6,3)` signed-native three-axis selections, while the FCC four STAR sectors and C6/C12 branch bits are typed separately.

## 3. The lost frame is operationally observable at the next phase

The next frame-labeled signed native updates of the same root obey

`q_(i,j,k)(R_+(i,j,k)) = e_k-e_i`,

`q_(i,j,k)^(-1)(R_-(i,j,k)) = e_j-e_i.`                         **(2)**

For any fixed `j,k` and two distinct possible smaller indices `i != i'`, (1) gives the **same** native root, its shortest BRC words and its exact `N_BRC=2`, whereas (2) gives two **different next native states**. Thus a frame-blind deterministic successor on root-only states cannot reproduce all the named triadic transitions. It is sufficient to preserve the source triad/frame index `i` (or a lossless equivalent) alongside the signed root and orientation.

Smallest explicitly source-typed witness:

- Triads `S=(1,3,5)` and `S'=(2,3,5)`, both forward chirality, give the **same** C12 root `e_5-e_3=(0,0,-1,0,1,0)`.
- Their next original `q`-updates are `e_5-e_1=(-1,0,0,0,1,0)` and `e_5-e_2=(0,-1,0,0,1,0)`.
- Both source roots have shortest native BRC mass 2; even keeping the two ordered shortest step witnesses loses the omitted frame index, because the native endpoint/displacement is identical.

Exactly **12 of the 20 root states** have at least two distinct possible next updates; the other eight are singly sourced. This gives a concrete LP023/LP028 operation-safe provenance obstruction at actual executable source boundaries. The current all-20 checker properly counts 40 *oriented source arcs* and does not itself assert the 40 root Cell positions are distinct; no code correction to that owner is inferred. An adapter or consumer that must evolve a root through a named `q` needs the frame index.

## 4. Independently executed exact finite certificate

An independent, executable Python checker reconstructed the original six-axis signed-permutation definitions and enumerated **all 20 triples x both orientations**, the six macro orbit states and 12 outer microstates. It checked the exact formulas (1)–(2), `q^6=id`, orbit closure, native `G=T=N_BRC=2`, the full fiber size histogram `{1:8,2:6,3:4,4:2}`, and that the number of distinct next states in each root fiber is exactly its number of source frames. Explicit `require(...)` guards remain active in Python normal, `-O` and `-OO`; output was byte-for-byte identical in all three modes.

- Executed checker Git blob: `92f4fe7699b45f1f5fdbceaf95cae573b781483b`; local SHA256 `a6bdf8d88828f0f13f8f980be4f9e9e1bbe7e545d6b51b4786c57422ce3eaa0d`.
- Exact result Git blob: `c406c865c4df2d0396f9fd5fafb484af1507ef95`; local SHA256 `0287ea1043f4c83050e58f9e6c0d54890e3001e61d2deb0f162e934ed5d231b6`.
- GitHub checker: `research_checks/X6_UNIT76_TRIADIC_ROOT_FRAME_FIBERS_20261117.py`, committed `f53bdbc0c8c2a67b869dd2cc45f71e04638a40a4`.
- GitHub certificate: `research_checks/X6_UNIT76_TRIADIC_ROOT_FRAME_FIBERS_RESULTS_20261117.json`, committed `2e95a2deb5e9bd2e6ffc084fc9ee3f8e7884bfe8`.

The matching source blobs were read back from those immutable commits. This check is independent of the original frozen R063/Helly benchmarks and of live all-20 script execution.

## 5. Actual consumer classification and parent continuation

For the five actual executable sources named above, the current `q_triad`, outer root, native signed step and INNER/OUTER operations remain correctly typed in their own domains. New dependency recorded: **frame-qualified C12 root evolution must not factor through root Cell alone for the 12 ambiguous root states**; `root + orientation + frame-index` restores the original named transition. This is independent of the previously established BRC-positive versus signed-Gaussian cancellation distinction.

The frozen LP011 *historical wrong native argmax caller* and LP019 *historical subtraction of positive N_BRC* remain `UNRESOLVED_PROVENANCE`; this unit did not attribute them to the five correct Viète programs. The full 28-LP actual consumer closure and independent Driver `REQUEST_REVISION` remain open. The author should check any actual downstream file that consumes these root states as a source-free successor; do not patch proven-correct owners just because a projection can lose information.

Own Native Unit75 original same-SID resume `onhour-20261117-0536-x6-own-run-resume-unit75-v1` was independently read as `SUCCEEDED/RUN_READY` generation 4. The Unit75 semantic publication request `onhour-20261117-0630-x6-unit75-native-semantic-progress-v1` is an original pending request to reconcile, not to resubmit. A read-only exact continuation request `onhour-20261117-0629-x6-exact-continuation-read` is also pending; neither changes the frozen science. Native Unit76 semantic publication requires fresh own-run authorized execution and separate terminal Source readback. GitHub author research and Activity are separate from native PROGRESS/Result/review.

No scheduler, notification settings, maintenance identity, frozen input, accepted R063 result or other owner code was changed.
