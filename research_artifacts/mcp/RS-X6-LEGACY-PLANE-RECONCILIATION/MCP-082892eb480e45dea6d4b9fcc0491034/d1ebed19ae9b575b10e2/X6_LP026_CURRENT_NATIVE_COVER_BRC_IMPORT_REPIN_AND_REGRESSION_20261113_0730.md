# LP026 exact current native cover/BRC consumer — pin repair and executable regression

Date: **2026-11-13**. Mother objective `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research lane: `EM-X6-FB6990`, same registered session `MCP-082892eb480e45dea6d4b9fcc0491034`. NONBLIND author-side Source audit; not independent review or formal Result.

## Actual downstream failure, repaired at current main

Existing executable `research_checks/X6_LP026_CURRENT_COVER_FAST_G_NATIVE_BRC_IMPORT_20261112_ONHOUR.py` (original Git blob `4c0ffed845a94eb81f9d7c04eae1c54ea3d08e39`) pinned two code dependencies to pre-repair versions. Execution against actual current imported modules failed at the **first SHA assert**, before entering any scientific test:

```text
AssertionError: ('.../x6_coordinate.py',
 'dd6dd7e74b83be09bb7545ee92357eda445c6ca3',
 'ef66285d8ae81569cbbd3195b3e38daae37944ef')
```

This was an **actual source-consumer compatibility break after legitimate native/relative typing repairs**, not a mathematical counterexample or proof failure. Both stale PINS were updated to the verified current main Git blobs, with no change to the mathematical assertions, formulas, algorithm, imports or other two pins. Historical commits retain the prior experiment and its exact original pins.

| Imported module | Previous checker pin | Current executed and new checker pin |
|---|---|---|
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `ef66285d8ae81569cbbd3195b3e38daae37944ef` | `dd6dd7e74b83be09bb7545ee92357eda445c6ca3` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` | `3f7d9e62a4dd66e7888a69ff87276b283c891aac` | `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` | unchanged |
| `research_checks/X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR.py` | `496764aa8ebdb19bb03b7d40b82128a82be0ed84` | unchanged |

The repaired checker was executed **unmodified except those two pin literals** from its original relative repo path using the five actual GitHub source bodies. Their Git blob SHA-1 hashes exactly matched the local executed bytes. Python 3.13.5, process exit code 0, elapsed 5.40 seconds (local timing, not a benchmark), RSS 110480 KiB. Patched checker blob: `346be279c42a1a44a7ecfae01256cb92e3109f00`, SHA-256 `6cef52c97fb755e370bff446ef4121c6e7b4b7710112e6b20f89467a50c0acab`.

## Complete actual stdout

```text
PASS_X6_LP026_CURRENT_COVER_FAST_G_NATIVE_BRC_IMPORT
pinned_git_blobs {'experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py': 'dd6dd7e74b83be09bb7545ee92357eda445c6ca3', 'experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py': '171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd', 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py': '300a96e3dc24bf6fff73743037a0347a8bc83176', 'research_checks/X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR.py': '496764aa8ebdb19bb03b7d40b82128a82be0ed84'}
n0_to_n6_native_brc_checks 10364
n0_to_n6_cover_state_checks 59267
n0_to_n5_source_step_transition_checks 281472
n0_to_n6_fast_native_norm_import_checks 59267 ambiguous 2355
section_norm_not_native_when_unambiguous_cases 49834
reverse_axis_section_and_native_norm 5 1
n9_equal_native_norm_distinct_BRC 21 10080 7560
```

## Verified mathematical meaning and scope

The original integration independently builds signed native endpoint distributions over exact lengths `N=0..6` via 12 primitive native directions and checks the actual imported signed-BRC endpoint multiplicity, all selected finite cover quotients `m=0..5`, source `CoverState.step` transitions, and the sharp native squared-norm recovery classification from the imported fast interval algorithm. The test checks **10,364** original signed endpoint multiplicities, **59,267** cover states, **281,472** primitive source transitions and **59,267** exact norm-recovery classifications; **2,355** classes have non-unique native norms and **49,834** classes have a unique native norm different from the min-zero section norm. These are statistics of the declared finite domain, not unbounded frequency claims.

Concrete provenance-preserving test: signed endpoint `(-1,0,0,0,0,0)` has relative min-zero section norm 5 but native squared norm 1. At `N=9,m=3`, signed displacements `(-3,-3,0,-1,-1,-1)` and `(0,0,3,2,2,2)` have the **same cyclic cover observer and native squared norm 21**, yet their original imported signed-BRC multiplicities differ, 10,080 vs 7,560. Thus even exact recovery of native norm does not by itself recover BRC branch/path multiplicity; preserving the full signed lift or appropriate BRC fibre is necessary for that subsequent observable.

## Exact persistence and continuation

- Current source checker CAS GitHub commit `4544c86adea3f3f368a012cbec8f05768d72a3ae`; new blob `346be279c42a1a44a7ecfae01256cb92e3109f00`; immutable readback matched.
- Previous original `check_x6_cover.py` complete 516,299-assertion PASS is separately documented in `research_notes/X6_LP003_LP005_LP026_COVER_ORIGINAL_REGRESSION_EXECUTED_20261113_0700.md` at `028bad3040fa43039d82cc5bef4d78f582d32df3`.
- Do not rerun previous original `check_x6_coordinate.py` 58,989 PASS or previously certified LP028/LP019 tests without a changed need.
- Next unresolved mother objective: finish actual LP28 downstream dependency closure and historical LP011/LP019 wrong-caller attribution, obtain independent Driver `REQUEST_REVISION` disposition.
- Source-native session/claim/run are ownership provenance until fresh resume: session `MCP-082892eb480e45dea6d4b9fcc0491034`, claim `MCP-9ce362c91287345702dd387d`, run `RUN-1e81bbcb1938961eb41db249`. Native Source PROGRESS remains a separate publish/readback obligation, not implied by this GitHub commit.
