# X6 Unit 65 — historical R063 Stage 3 source-level LP019 classification and verification guard

**Scope:** author-source-attested, actually executed scoped fault injection; UNREVIEWED, NOT_ADMITTED. Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION` under frozen X6/P000 `59538f585d037d09ef687b28715c4bc1a3f9fe03`; old corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. No modification to other authors' claims, original PR or frozen native benchmark.

## Exact checked immutable original sources

The original R063 Stage 3 [PR #574](https://github.com/awdawmip/enterprise-math/pull/574) was OPEN / DRAFT / unmerged when read, at branch HEAD `69b7a90328bdb72852d47b338dedd7b276740ac9`. Sources actually inspected under that immutable head:

| Path (prefix `research_results/R063_STAGE3/` unless specified) | Git blob SHA1 |
|---|---|
| `scripts/r063_stage3_validate_pairwise_interaction_process.py` | `4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636` |
| `R063_STAGE3_INTERACTION_COUNT_COLLAPSE_THEOREM.md` | `2650ffb8098e3d9cc0f64b720a8e3f323ba70de8` |
| `R063_STAGE3_CANCELLATION_CONFLUENCE_OR_NO_GO.md` | `5e4be3be6848ed2d88b24f9b773a351f6bea1788` |
| `R063_STAGE3_SEMANTIC_SCOPE_CLAIM_LEDGER.json` | `3fd60ed3de679879ceb43d8187374166112ad874` |

Also checked the Stage3 historical [Driver review](https://github.com/awdawmip/enterprise-math/blob/fd2bcff10ca6e147348b6c1236027fc0d2877df3/driver_reviews/R063_STAGE3_PAIRWISE_INTERACTION_SIGNED_CANCELLATION_DRIVER_REVIEW_20260822.md) blob `32ab69b84c479f34846ae9addf4a601f80645194`.

## LP019 exact consumer judgment

Original script lines 22, 26–28, 69 and 75–80 construct derived `C4`-labelled interaction rectangles, with source component counts `(a,b)` and `(c,d)`. Signed phase counts are

[
(n_0,n_1,n_2,n_3)=(ac,ad+bc,bd,0)
]

and their algebraic evaluation is ((n_0-n_2,n_1-n_3)=(ac-bd,ad+bc)). The *subtracted values* are signed phase labels of an N1 algebraic interaction, not counts of positive natural BRC paths. Line 81 separately computes `target_native_path_count` via a positive binomial, and line 120 explicitly records `R062_N_BRC` as another positive channel. The original typed ledger lines 63–85 and 115–139 classify the process/cancellation as **N1_DERIVED_OPERATIONAL**, not N0 global native operation.

**Classify this single branch:** `NO_WRONG_POSITIVE_N_BRC_CANCELLATION_FOUND / PRESERVE_N1_DERIVED_SIGNED_PROCESS`. This does not establish corpus-wide absence, and LP011 historical wrong native singleton argmax and LP019 purported wrong positive N_BRC subtraction callers remain `UNRESOLVED_PROVENANCE`.

## Separate executable source-guard defect

Original frozen source `scripts/r063_stage3_validate_pairwise_interaction_process.py:54–57` terminates `relation_weights` with:

```python
assert total and all(cnt(w)==target for w in total);return tuple(sorted(total.items()))
```

CPython strips `assert` in `python -O` and `python -OO`. A **scoped fault injection** compiled the literal four-line original function, with exact original guard/return intact and only its outside dependencies stubbed to supply `residual_sets(p,q)=[]`. As a result, `total=Counter()` is invalid; three independently invoked Python modes yielded:

| Executed mode | Process exit | Observed invalid-input outcome |
|---|---:|---|
| ordinary CPython | 0 | `AssertionError` raised and caught; rejected |
| `python -O` | 0 | silent `()` returned |
| `python -OO` | 0 | silent `()` returned |

The scripts specifically verify expected ordinary/optimized behavior and exit zero only when observed outcomes match. This confirms a **verification/implementation guard gap** in the original branch under an injected invalid dependency. It does **not** claim the normal full original benchmark failed, that Stage3 mathematics is invalid, or that the original 15,876 paired words were rerun. The original PR remains untouched.

GitHub artifacts: [scoped checker](../research_checks/X6_R063_S3_ASSERT_OPTIMIZATION_GUARD_UNIT65_20261116.py), [machine-readable executed outcomes](../research_checks/X6_R063_S3_SOURCE_GUARD_UNIT65_RESULTS_20261116.json). Independently executed local variant SHA256 `572e6cb0f6ef3af87617f8b52a7831923a5358ec5dd8675e690be8ab86a40b64` and local certificate SHA256 `b1b2e1d61d5e60b9e73f7600ccff669f5a5712e805d3fddac78891db032d7fc0`; the published files are compacted equivalent representations, not a claim of bit-identical SHA.

**Minimum owner-side correction:** use an explicit `if not total or not all(cnt(w)==target for w in total): raise AssertionError(...)`; run the original benchmark under ordinary / `-O` / `-OO`, and inject the empty external `residual_sets` to verify rejection in every mode. It is for the original PR owner or authorized Driver to modify that distinct branch.

## Continuation

Preserve Unit64 three-chart holonomy/three-mode optimization evidence, native R063 17 gate/512-radius original results, original Helly and previous BRC path proofs. Next research is exact source:line history of LP011/LP019 alleged wrong native callers *if one exists*, the outstanding 28-LP active-consumer closure, and independent Driver `REQUEST_REVISION`. This unit is not admitted, and no new native experiment performance is asserted.

## Additional original-checker acceptance-label limitation

The same original Stage3 script initializes every named `acceptance_gates` entry to `True` at **line 68**, then only assigns the `DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES` key at **line 121** before testing `all(gates.values())` at line123. Thus the other names are **static declared labels**, not individually evaluated Boolean gate implementations. Many specific checks do append mismatch rows elsewhere in the script; the factual scope is precisely that `all(gates.values())` is not independent proof that each labelled gate has a dedicated predicate. The frozen Stage3 Driver review already notes the similarly overstated `STAGE2_FROZEN_DEPENDENCY_REPLAY_INTACT` label: the checker encodes the dependency formula, **not** a literal load-and-run of original Stage2 code. A future repair should preserve real theorem certificates while driving each advertised executable gate by its actual evaluated evidence and reporting non-executed dependencies separately. This is an additional source audit, not a newly observed mathematical counterexample or an executed original benchmark failure.

## Exact original witness separating process histories from positive BRC

The original script **line 120** additionally records the already frozen `W2_5x5_iijxiij` fixture: `source_path_pair_count=9`, `interaction_cell_count=9`, `cancellation_matching_count=4`, `residual_process_object_count=4`, `generated_target_path_support=5`, `process_formal_witness_count=102`, `full_target_native_path_count=35`, `signed_gaussian_provenance_preimages=4`, `R062_N_BRC=35`, `Boolean_support=1`. The different values `102`, `35`, and `1` are source-typed process witnesses, natural shortest-path mass and Boolean endpoint support, respectively. They cannot be identified without specifying an information-discarding map. This is an **inspected existing original exact fixture**, not a new run of original Stage3. It provides a concrete typed distinction for LP019 and fixes the consumer's target/source observer interpretation.
