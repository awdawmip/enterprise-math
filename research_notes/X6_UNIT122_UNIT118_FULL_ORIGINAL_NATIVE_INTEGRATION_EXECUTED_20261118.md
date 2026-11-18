# X6 Unit122 — actual source-pinned Unit118 native integration, all three CPython modes

**Date:** 2026-11-18. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Author:** `EM-X6-FB6990` / own Research lane `chatgpt-research-onhour-enterprise-math-20260923`.

**Result:** The previously saved Unit118 strict runner is now **actually executed against the original source modules** in CPython normal, `-O`, `-OO`. All three exit 0, return byte-identical JSON (SHA256 `6ec8180c58e3943c8707c7f3a77281f10c163f32f98dfcc44b64e41718f5e127`), preserve 13 always-on converted mathematical guards, and reject a fault-injected native BRC return.

## Source integrity and experiment identity

The five original files were retrieved through the authorized connected GitHub source route and reconstructed in an isolated local checkout-like directory with **identical Git blob hashes**. The scientific source baseline is the frozen P000 `59538f585d037d09ef687b28715c4bc1a3f9fe03`; later program sources are pinned at their already saved exact Git blobs.

| Original source file | Verified Git blob SHA1 |
|---|---|
| R063 minima calculus `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py` | `643b2bac659a445891dcb5588b647972977104e0` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` | `ac32f6d82a91db99297e587cf63b0df95cece514` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` |
| Current LP028 signed PathSqrt consumer `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` | `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9` |
| Existing strict Unit118 runner `research_checks/X6_UNIT118_LP028_PINNED_ALWAYS_ON_NATIVE_REPLAY_20261118.py` | `61c33acc8ae2865f4c880673382ad630094ceee8` |

Each hash is computed from the *actual local source bytes* and matches the file's original GitHub blob. Full local SHA256 values are recorded in the adjacent machine certificate.

## Original-module three-mode integration result

Running `python research_checks/X6_UNIT118_LP028_PINNED_ALWAYS_ON_NATIVE_REPLAY_20261118.py`, `python -O ...` and `python -OO ...` (Python 3.13.5) under the reconstructed five-file repository:

| Property | normal | -O | -OO |
|---|---:|---:|---:|
| Exit code | 0 | 0 | 0 |
| Original assertions converted to always-on guards | 13 | 13 | 13 |
| `shortest_path_multiplicity` true calls | 24,600 | 24,600 | 24,600 |
| `endpoint_multiplicity` true calls | 24,600 | 24,600 | 24,600 |
| `full_distance_squared` true calls | 24,600 | 24,600 | 24,600 |
| `spatial_norm_squared` true calls | 24,600 | 24,600 | 24,600 |
| Wrong native BRC injection rejected | yes | yes | yes |

All outputs are byte-identical. The original source program emitted the exact `PASS_SIGNED_PATHSQRT_CURRENT_SOURCE_IMPORT` marker, radius 1..128, 24,600 labelled chart branches, 252 unique endpoints at r=50 and exact r=50 native union mass `6641732296455342852372`. Its captured stdout SHA256 is `1df473952c0d5d8a3221c1999a91b68f9a1505b0443e93b53230faef508fdb4f`.

The Unit118 strict wrapper obtains the module through the original imports; the AST-only conversion replaces bare assertion checks while preserving the signed embedding, native original R063/Spatial6/signed_brc functions and existing source pins. The wrapper tracks real function executions, not loop counters. Mutation changes the wrapped native shortest-path return by +1 inside the isolated unit namespace, and an actual integration assertion rejects it.

## Resolution and continuing mother task

**Unit118 original-module three-mode integration is now verified-complete.** Units117/118 previously reported a genuinely pending native run; this evidence resolves that specific gap. The original benchmark object (R063 six-blob 512/512 C3/C4 with its separate source/author evidence in Issue #2416) is untouched; independent review and admission of that benchmark remain an independent governance operation.

Read with Unit121's sharp named-step observer obstruction. The verified current LP028 source properly lifts its chart into full native signed deltas before using BRC, while the fixed strict tester now executes all validation guards even in optimized Python. Further audit should identify **actual** remaining LP023/LP028 or historical LP011/LP019 bad callsites by immutable `commit:path:line` before attempting any current-code patch. For the entire X6 mother objective, the 28-LP downstream ledger and Driver's `REQUEST_REVISION` remain active.

**Status:** `AUTHOR-SOURCE-INTEGRATED / ORIGINAL_NATIVE_EXECUTED / EXACT-INTEGER / UNREVIEWED / NOT_ADMITTED`. No P000 modification, frozen science pin change, new CLAIM, independent review, Result admission, scheduler or maintenance-lane identity change.
