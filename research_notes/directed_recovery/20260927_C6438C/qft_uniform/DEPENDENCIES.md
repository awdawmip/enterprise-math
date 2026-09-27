# Dependencies and restoration

This publication contains the complete new uniform-certificate stage selected by its final publication manifest: sources, proofs, reviews, checks and original bounded evidence. It is not a dependency-free runtime bundle. Earlier implementations and phase-bank evidence remain external and pinned below. Current-stage final hashes and actual source commit belong to the publication receipts. No previous runtime is silently replaced.

All EM references mean `awdawmip/enterprise-math`. Paths are relative to the stated immutable commit/prefix. SHA-256 values identify complete file bytes, including compressed bytes for `.gz` files. The selected files are entry points and provenance, not a substitute for restoring their transitive source trees.

## Immediate adaptive parent

EM commit `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_adaptive/`, restored under `sep27-qft-adaptive/`.

| File | SHA-256 |
|---|---|
| `adaptive_execution/adaptive_feedback.py` | `86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45` |
| `adaptive_execution/check_adaptive_feedback.py` | `cd77bc2ff17a6b2938665a622a74c332e7e24cbe362ba359225fc071716510d3` |
| `adaptive_execution/ADAPTIVE_FEEDBACK_RESULTS.json.gz` | `36a6460fbda4d081d1416bbfa48fa0fd641f96d0df235d2d168a7ac06aa5a9c0` |
| `adaptive_execution/ADAPTIVE_FEEDBACK_SUMMARY.json` | `81808acea7086ffe64da61410aba8fdbeefdc49301d9bc075a6242f289b16153` |
| `DEPENDENCIES.md` | `6bb7707a8296a24a43a1f7f439a5e6ca9a7ccef2a581d7771c1be1ccd846e8d9` |
| `PUBLICATION_MANIFEST.json` | `ce47909737e87360d9510fb098f560daf9f41de3d2924ece2d92edbfe8dd1582` |

The uniform policy imports frozen `adaptive_feedback.py`; its checker imports prior fixture helpers and reads the actual adaptive result as comparator. The result archive has 4,807,682 bytes. The source/hash pin in the new policy binds this superclass. There is no asserted adaptive `DEPENDENCY_MANIFEST.json`: the actual parent has `DEPENDENCIES.md` and `PUBLICATION_MANIFEST.json`.

The parent publication includes readable chunks/restoration metadata. Its verified backup is Drive file `1K4jGwDnQp31Fx4uPJZ3YS9X1nfIaCp9g`, `QFT_Adaptive_20260927_C6438C.zip`, 16,746,556 bytes, SHA-256 `015208237e9b15aea784e9a866e249e10850cf441112141fec62e9f0b4ffdf8a`. EM remains source authority; Drive is backup.

## Carry dependency

EM commit `8e2f54ce5581636b9169845a54f018c25d00b165`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_carry_execution/`, restored under `sep27-qft-carry-execution/`. `carry_executor.py` SHA-256 is `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`; it supplies the frozen source/phase snapshot used by the adaptive parent. Restore its complete source dependency tree through its published dependency note.

## Optimization

EM commit `0e6380ff74d31b842ba0b54802c1f0595a7dd60d`, prefix `research_notes/directed_recovery/20260926_C6438C/optimization/`, restored under `sep26-shor-general/optimization/`.

| File | SHA-256 |
|---|---|
| `collision_analysis/check_gram_sampler.py` | `7972b5863f674ae808c74322c3abd8cef8c156521918183e868b4965bf1d68be` |
| `collision_analysis/gram_sampler.py` | `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9` |
| `streaming/lazy_streaming.py` | `635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257` |
| `carrier_codec/carrier_codec.py` | `c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953` |
| `lazy_modular/lazy_modular.py` | `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4` |
| `lazy_modular/lazy_gcd.py` | `b704590f055da0785d03b6026d9fa749e75218acd2764d25e90288f32db0965e` |
| `lazy_modular/lazy_postprocess.py` | `c353b8dc429e3d60c8afd9685da4cf1624dbf36785d85eee4a12f636eea0af56` |

## Direct Word Bank

EM commit `9348fc6abdf45becbd12a8019d93f72d576b9fab`, prefix `research_notes/directed_recovery/20260926_C6438C/`, restored under `sep26-shor-general/`.

| File | SHA-256 |
|---|---|
| `direct_word_integration/check_direct_word_integration.py` | `c8dd1d00cbb66c540240877c3b45eecce154e86be265809768b4c60082eef7b7` |
| `direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz` | `ef981768a20a72a67bfd7d01284d1b946cfc95ded96552a07571c436964d1460` |
| `direct_word_compiler_general/construct_general_word.py` | `830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63` |
| `direct_word_compiler_general/M3_DELTA_EIGHTH.json.gz` | `297121c8c8cfdd529e5a0e95ea02bf8e54584caf1b645dbf27e025f221ed58ad` |
| `direct_word_compiler_general/M4_DELTA_QUARTER.json.gz` | `9f1a5b371bbf7de9783f2bed83b1934a872281f39a1bc7fd0244d806205d1db7` |

## Compiled Word

EM commit `8d4e9c12f7492316b825e96423bc0ee36ccdee22`, prefix `research_notes/directed_recovery/20260926_C6438C/new_word_compiler/`, restored under `sep26-shor-general/new_word_compiler/`.

| File | SHA-256 |
|---|---|
| `certified_word_compiler.py` | `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d` |
| `compiled_streaming.py` | `d0f980b7ff5fb41438e9e0ad40af65a190bcd6f83660c821f8362643190a558c` |
| `check_compiled_streaming.py` | `0cf231a238f6aa899f1cf7e86a8d7dc8dd3e1aeda33e3c1b6c371ef10804a9ce` |

## General Foundation

EM commit `1fb7ff99d205f9ca03772942be64f732553dcd86`, prefix `research_notes/directed_recovery/20260926_C6438C/`, restored under `sep26-shor-general/`.

| File | SHA-256 |
|---|---|
| `integration/general_streaming.py` | `fcf510292d0f30814c6f5fdc6ac49d06b2e5afdf063cccc23704df1d6c689b71` |
| `integration/general_driver.py` | `f326d8fe53275839eeb1d250433ca58bc1d647ff9fb4eb7028444a54f4162747` |
| `sparse/sparse_modular.py` | `fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46` |
| `completion/typed_integer_prechecks.py` | `0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb` |

## Terminal Foundation

EM commit `b6625778e869511d85a202a0839eb105a197659e`, prefix `research_notes/directed_recovery/20260926_0C08F0/`, restored under `sep26-shor-alternative/`.

| File | SHA-256 |
|---|---|
| `algorithm_intake/terminal_instrument.py` | `acc2fc3d5a0535c33f39b9a706400d68c980a4bea73ac3d5758cfb7a469af67e` |
| `adversarial/zero_endpoint_extension.py` | `cb2bdbdda5445b4cb76a7c6a26b3f2074b452c1b5e7d950295e71ff49ac5b8c5` |

The direct-integration decompressed payload SHA-256 is `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c`. Its t=4 bank uses exact m=2 and direct certified words m=3, delta=1/8 and m=4, delta=1/4. The current checker re-admits actual words. This is not the RP1 heartbeat underlying bundle. The complete carrier retains residual coordinates; exact compression is not truncation.

The word certificate uses `CompleteNativeWord`, full-column replay, the actual positive-path observer, exact carrier codec and lazy modular propagation. The optimization and terminal sources above close these imports. Unrelated row-query/character modules from historical packages are not thereby claimed as imports of this stage.

## Complete historical map and native source

The complete restoration map is EM commit `6370e937d3cea8b957ac2d66d0bd6a42f385f9ee`, path `research_notes/directed_recovery/20260927_C6438C/qft_coherence/DEPENDENCY_MANIFEST.json`, SHA-256 `247b58caf177a9b12117898e6966128bce04a56c62a2ae8343c44e0a05808016`. The selected groups above and the native group provide immutable paths, import edges and binary restoration instructions. Reuse this map rather than assuming the present ZIP includes every old runtime.

Stage87 is a separate frozen bundle snapshot `0852cad130c1d877174d235687cf60c19f318c58`, not an asserted EM commit. Restore the complete bundle tree under `sep26-local-takeover/intake_brc/stage87-source/`. Drive file `1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV`, 61,398,315 bytes, SHA-256 `a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c`. Its authority is EM `1fb7ff99d205f9ca03772942be64f732553dcd86`, `research_notes/directed_recovery/20260926_C6438C/HANDOFF.md`.

Selected native files:

| File | SHA-256 |
|---|---|
| `stage45/brc_loop_recheck.py` | `f5242c74b5f1f53b8f50caf87d0eace7f3588d76d0d05240d9d5eb56255ae022` |
| `stage45/vendor/brc_weighted_recurrent.py` | `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26` |
| `stage58/coupled_reader.py` | `35df78a3e3098fa8b8241d0ceb3a3f59faf7ea9460c0ec6761f209b5aaa23c58` |
| `stage78/shor_benchmark.py` | `e5cb9c4871da2662bbf831cc7721730593be478ebbe238a58d95ba2917dda47c` |
| `stage79/phase_compiler.py` | `00a2d1369bcafd70d469381e517ed9f2dd4e7a6f79a55144337cd085de49f15d` |
| `stage80/fixed_phase.py` | `d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254` |

The canonical core is EM `bc7babbb9e890f6d5a7094430a5fbdccf66c77ad`, `src/enterprise_math/brc_weighted_recurrent.py`, SHA-256 `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26`, git blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb`. The vendor copy above has the same bytes; `stage45.brc_loop_recheck.verify_vendor` checks that binding before admission.

## Restore layout and validation scope

Restore immutable source trees first, then original `.gz` evidence from each readable-evidence index or verified Drive original. Check compressed hashes and any separately pinned decompressed payload hash. Keep sibling directories under a common TEMP root as named above, plus `sep27-qft-uniform/`. The recorded interpreter is `D:/kimi-query-bridge/.venv/Scripts/python.exe -X utf8`. Runtime bindings use `BRC_STAGE87_SOURCE`, `BRC_ZERO_ENDPOINT_SOURCE` and `BRC_STREAMING_PREVIOUS` for the native tree, terminal zero-endpoint module and terminal source root. These paths document actual execution provenance; they are not capability restrictions on future conversations. Relocated execution must preserve pins and satisfy source bindings, or explicitly rebind and re-certify a new version. Proof and inspection can continue without running the old environment.

This closeout preparation inspected imports and hashed frozen local bytes against available historical manifests/readback records. It performed no scientific calculations and did not independently refetch every old remote file. Final new-stage source bindings and results are captured by this publication and its execution reports. Query and primary-reading reuse are recorded separately in `PRIOR_EVIDENCE_REUSE.md`.
