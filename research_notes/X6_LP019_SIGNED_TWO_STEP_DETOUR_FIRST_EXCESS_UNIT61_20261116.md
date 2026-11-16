# X6 / LP019 — first two-step detour of positive signed-native BRC (unit 61)

Date: 2026-11-16 14:01–14:xx Asia/Hong_Kong. Parent Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Research lane identifier `chatgpt-research-onhour-enterprise-math-20260923`. Source historical researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, RUN `RUN-3356cbe3c2b4916d79399941`. GitHub author-side math/evidence; privileged Source publication separately requires current authenticated owner/lease. Scientific status: **AUTHOR-PROVED + EXACT EXECUTED, UNREVIEWED / NOT_ADMITTED**.

## Frozen object and exact prior inputs

P000 V5 `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json`, blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`. Signed native Cell displacements `z in Z^6` with twelve signed unit coordinate steps and `G(z)=sum z_i^2`. The time/event step count `T(z)=sum |z_i|` is separate from `G`. P000's Enterprise right-angle convention remains unchanged.

Frozen scientific producer `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at the same pin, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`: `shortest_path_multiplicity` and `endpoint_multiplicity`. Current typed consumer source `src/enterprise_math/p022_geodesic_multiplicity.py`, blob `46373050168d2430b6cb3952aa763f3081284632`: `sc_geodesic_path_count` counts *shortest* paths and `sc_shell_total_geodesic_paths` sums only the fixed L1-graph-radius shell. This report checked their source definitions by authenticated GitHub reads; it **did not execute either imported project module**. The actual new checker computes the stated mathematics independently.

Previously saved unit 58: `G=25` six-axis shell has 7,812 signed endpoints and sum of **shortest** natural BRC multiplicities 2,538,954,612. Unit 59/60 establish support-loss theorems; their original semantic Source authorization remains separate.

## New all-endpoint exact identity: first positive detour

Write `a_i=|z_i|`, `T=sum_i a_i` and `B_T(z)=T!/prod_i a_i!`. For any `z in Z^6`,

```
B_{T+2}(z) = B_T(z) (T+1)(T+2) sum_{i=1}^6 1/(a_i+1).
```

Here `B_m(z)` means the number of *all ordered signed primitive-axis words of exact length m reaching z*, not the number of geodesic paths. This is an **exact integer identity** even though the displayed summands are rational.

Proof: Every path of length `T+2` uses the required `a_i` signed moves plus exactly one opposite-sign pair on some uniquely determined axis `i`. For each choice `i`, the required move multiplicities are `a_i+1` in the demanded direction and 1 in the reverse direction on axis `i`, plus `a_j` on every other axis. Multiset permutation count is `(T+2)!/[(a_i+1)! prod_{j != i} a_j!]`. Sum over the six disjoint choices of extra backtracking axis. Factoring out `B_T(z)` yields the identity. As a consequence `B_{T+1}(z)=0` by parity, so **first** possible non-geodesic length is `T+2`; no positive natural paths are subtracted or cancelled.

Witnesses: `z=0` has `B_0=1, B_2=12`; `z=(1,0,0,0,0,0)` gives `B_1=1, B_3=33`; `z=(1,1,0,0,0,0)` gives `B_2=2, B_4=120`; `z=(3,0,0,-4,0,0)` has `G=25, T=7, B_7=35, B_9=11,214`. These retain named signed-axis and length provenance.

## New complete native G=25 first-excess certificate

For each of the 7,812 native signed endpoints in `G=25`, sum `B_{T(z)+2}(z)`. This is a **variable exact path-length per endpoint** observer (first excess over its own geodesic length); it must not be represented as a single common-time shell.

| T(z) | support | endpoints | sum B_T | sum B_(T+2) |
|---:|---:|---:|---:|---:|
| 5 | 1 | 12 | 12 | 2,604 |
| 7 | 2 | 120 | 4,200 | 1,345,680 |
| 9 | 4 | 2,880 | 10,886,400 | 4,031,596,800 |
| 11 | 5 | 960 | 399,168,000 | 160,864,704,000 |
| 11 | 6 | 3,840 | 2,128,896,000 | 774,918,144,000 |
| **all** | | **7,812** | **2,538,954,612** | **939,815,793,084** |

The P022 graph radius `T=5` all-endpoint geodesic mass remains `106,452` in six dimensions. Its type is neither the fixed `G=25` shortest mass nor this endpoint-adaptive first-excess mass.

## Execution and independent checks

An actually executed pure-Python exact checker exhaustively enumerates the 7,812 signed `G=25` endpoints, while a separate orbit/partition algorithm reconstructs all five `(T,support)` rows from positive-square magnitude multisets, signed embeddings and exact multinomials. A direct factorial one-backtrack calculation is checked against independently rearranged common-denominator arithmetic. A third signed-walk recursive predecessor count checks six small cases. All checks use explicit exceptions and run identically under regular Python and `python -O` (exit code 0). No float approximations. No original R063 / Helly benchmark was rerun.

Saved source `research_checks/X6_LP019_SIGNED_TWO_STEP_DETOUR_UNIT61_20261116.py`, commit `0b4b97dd2bcd01e75291985b54a51c583c78f66c`, blob `60c5cac2beb15b507c81e95f41d35f2f595d3a9e`, local SHA256 `547a3c1d214844db08112d6500e3e3380802b0dcbd234857fb41cde8423a7e50`.

Saved complete JSON `research_checks/X6_LP019_SIGNED_TWO_STEP_DETOUR_UNIT61_RESULTS_20261116.json`, commit `caa9fda6daf89a4de2548004db22c2df0aa06d29`, blob `d5efa20c9514110ea3345b47264b5c3d1f6efe10`, local SHA256 `643c6b1d917f0b4b6235ec21fd681331a4f27d4f25b4fa47e0de1ee710cac58b`. Both blobs have been fetched from the immutable commits and matched to the local exact files.

## Precise consumer disposition

P022 geodesic endpoint count is correctly typed for `B_T(z)`; frozen signed BRC `endpoint_multiplicity` covers non-geodesic `B_m(z)`. A caller asking for length `T+2` cannot reuse P022's *geodesic* aggregate without an explicit change of object, and a caller asking for `G` cannot silently use an `L1` shell. This is a provable **type boundary**, not an allegation of a found historic bad caller. LP011 singleton argmax and LP019 positive-natural-count signed-cancellation wrong callsites remain `UNRESOLVED_PROVENANCE` until exact source lines are established.

Next: fresh own-run status and original request receipt; legally publish Source semantic progress for saved units 59–61 if authority is current. Continue *actual* downstream consumer/callsite localization or producer-side independent module execution under pinned source. Independent Driver controls `REQUEST_REVISION`; this report does not grant Result admission.
