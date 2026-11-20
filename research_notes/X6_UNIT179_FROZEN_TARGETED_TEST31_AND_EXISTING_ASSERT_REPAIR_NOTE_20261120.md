# X6 Unit179 continuation — frozen targeted test callers and pre-existing assertion repair provenance

**Task:** RS-X6-LEGACY-PLANE-RECONCILIATION; **publication:** TP2-B4A441B23DA3159232C2; **frozen historical commit:** fd2bcff10ca6e147348b6c1236027fc0d2877df3; **science pin:** 59538f585d037d09ef687b28715c4bc1a3f9fe03. Status: AUTHOR_SOURCE_AUDIT / UNREVIEWED / NOT_ADMITTED.

Following the already-persisted Unit179 full 110-file experiment-Python inspection, this same run selected **31 of the 312** frozen `tests/*.py` files whose basenames matched the research-relevant terms `diagon|quotient|brc|signed|x6|coordinate|geodesic|path|native|residual`, read all 31 exact files by `mcp__GitHub__fetch_file` at the immutable historical commit and recorded their returned Git blobs. The 31-file test-bucket scan found **no direct textual named reference** to `diagonal_quotient`, `canonical_min_zero`, `same_diagonal_class`, `diagonal_chart`, `compose_canonical`, or `inverse_canonical`. This is a *filename-targeted* static read, not the full 312-test census or proof against indirect/equivalent computation.

Two positive source edges are confirmed: `tests/test_brc_weighted_foundation_tool.py:6–17` imports `enterprise_math.brc_weighted` and calls its `cwm_*` positive-weight APIs (e.g. lines 32–44); `tests/test_brc_weighted_recurrent.py:4` imports `enterprise_math.brc_weighted_recurrent`. These do not evidence LP011's alleged bad **native signed** argmax or LP019's alleged subtraction of **positive native N-BRC** multiplicity. The exact 31 file/blob inventory is below; no other test Python file is declared read.

## Existing optimization evidence: distinguish original discovery, historical persistence, and repair

The Unit179 frozen experiment evidence `assert` + unconditional `PASS` behavior is real; an independent representative CPython `compile(..., optimize=0/1/2)` probe confirms it. **However, the underlying optimized-assert vulnerability was already researched and repaired for a separate actual LP019 native-facing checker by Unit111**: `research_notes/X6_UNIT111_LP019_ALWAYS_ON_ORIGINAL_NATIVE_MUTATION_20261118.md@e43a95dff2a7501f43130a80891b7815e86f07dc`, with 18 remaining asserts replaced by always-on guards, real-native comparison and two mutation controls. The Unit179 report is only **historical-source assurance inventory for three other frozen checkers**; it does **not** claim discovery of the generic bug, new mutation result or that Unit111 is undone. It does not overwrite the original R063 benchmark or mark a rerun completed. The observed frozen checkers should not be used to infer optimized-mode mathematical PASS without their actual guards executing.

## Exact reviewed 31 test file/blob pairs

| Frozen path | Git blob SHA1 |
|---|---|
| `tests/test_brc_weighted_foundation_tool.py` | `69963f8a1089a87b6fb48e648f15ef19bff70e56` |
| `tests/test_brc_weighted_recurrent.py` | `bc32a22ae6596c73f4947ebb239671ad31e099bd` |
| `tests/test_exact_arithmetic_brc_runtime.py` | `6dedba31a1b1634afb59ca6862fc8823714df732` |
| `tests/test_p006_signed.py` | `e74d69aef5d853d587597770db4aecee8d5babc9` |
| `tests/test_euler_native_bisector.py` | `57eb499033b2432a3b5b325d711c50cf1719e4f0` |
| `tests/test_precision_signed_holonomy.py` | `cab5fd4e4d74303c06cb91dee8817ac520351efc` |
| `tests/test_p022_geodesic_multiplicity.py` | `ef3da1a789186867c538b604da1b642bf6039591` |
| `tests/test_p023_operation_quotient.py` | `89f93a312b4aaa40aac855de3691c445f7645019` |
| `tests/test_partial_operation_quotient.py` | `0a36a62a8676df260b6d1dec18923545603c4202` |
| `tests/test_predictive_quotient.py` | `7850a678a273f00580c15e543376d7a4c219c122` |
| `tests/test_quotient_basin.py` | `db0a9e174466ab70b9e894dee966dcba14db1eeb` |
| `tests/test_material_future_quotient.py` | `6cfb5f45977493cbd04cf05a582f05809505804f` |
| `tests/test_brc_critical_degeneracy_foundation.py` | `db33afe63a6fbe6ac3c8f86608ed0b65a8f7f1cc` |
| `tests/test_brc_critical_orbit_foundation.py` | `a262329f486ed83a20d3e0653e29d3463c576570` |
| `tests/test_brc_critical_ratio_jet_foundation.py` | `559ed5c2bbbd062f60a73632a8d93ca41ba5d4ec` |
| `tests/test_brc_logarithm_runtime.py` | `6131039b64437ea704e0183b63662b842201abec` |
| `tests/test_brc_newton_fiber_quotient_foundation.py` | `2fc8a1dcee7710d3f3f2654a1cd9e19d51ea9cc1` |
| `tests/test_brc_newton_handoff_resonance_foundation.py` | `d7f38f044659a0d94e43daaa42150ff80ea2270c` |
| `tests/test_brc_newton_observer_lattice_foundation.py` | `360d4c45715f4546d9303c492de141ddcde4d061` |
| `tests/test_brc_newton_quadratic_positive_selector_foundation.py` | `360a743800f2c66b17b39abd598b64532315852f` |
| `tests/test_brc_newton_quadratic_selector_foundation.py` | `95cc01034a483d0f436e28b0c3de7ba05e22a59b` |
| `tests/test_brc_newton_recursion_foundation.py` | `1b3599b82db86c62efa91edd4c659505baff7b` |
| `tests/test_brc_newton_schedule_strata_foundation.py` | `3c53c4b51844e71e9124726c10e3f53fd54ef270` |
| `tests/test_brc_newton_selector_chambers_foundation.py` | `70d39ca4cd97f45b012206350dfb860f2a9a3ffa` |
| `tests/test_brc_recurrent_interaction_foundation.py` | `9b978776facaa5013eb11e2024315d0f75ae94f8` |
| `tests/test_brc_recurrent_port_foundation.py` | `fb2a4fbf6b1bcf574411af7551b3c2f9b68c3540` |
| `tests/test_brc_reducible_critical_jet_foundation.py` | `e695b83d8c244f480862dd60d669f7abaf5f3afb` |
| `tests/test_brc_universal_histogram_foundation.py` | `a0fc2c27d009a3dfe36abdf38f46cef672785f91` |
| `tests/test_material_word_quotient.py` | `94589397826e42fa30c683656ea62b59b67d9e56` |
| `tests/test_native_trisector_coupled_closure.py` | `e0f4611115ce80979b362451435cd873a34a6c24` |
| `tests/test_prime_toolkit_native_trisector.py` | `17e8af9b723a261959237ee4b863b33d875ed34d` |

## Next

The remaining **281 frozen test Python files** have not been read in this sub-audit. Continue actual source/caller discovery, then reconcile exact LP011/LP019 historical `commit:path:line`; retain Units149–152 historical native association, Units175–179 current native PROGRESS pending, and Driver review as open. Unit179 evidence is preserved and never treated as an original R063 benchmark rerun.
