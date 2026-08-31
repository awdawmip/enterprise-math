# R063 Stage 3 — Final Classification

Status: `COMPLETE / READY_FOR_DRIVER_REVIEW`
Researcher-ID: `EM-R063S3-F1CF9D`
Task-ID: `RS-R063-STAGE3-PAIRWISE-INTERACTION-SIGNED-CANCELLATION-MULTIPLICATIVE-PROCESS-LIFT`
Taskbook source: `f1cf9d88428c14ae56e228ed97eba9b657b1fb90`
Frozen Stage 2: `96fbcd431f4cbb8263347bffb5c8bf33b7639e98`; Driver acceptance `b31419774f6d7190a4ed51332a9f69f4c7359b31`.

## Final classification

`PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_LIFT_CLASSIFIED_WITH_EXACT_UNIT_EQUIVARIANT_ASSOCIATIVE_INTERACTION_TENSOR_CANONICAL_SOURCE_SENSITIVE_RELATION_AND_POSITIONAL_CANCELLATION_NONCONFLUENCE`

Hard target achieved:

`PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_LIFT_CLASSIFIED = true`.

## Tower of results

1. **Local interaction table — exact and unique.** Bilinearity plus the frozen Stage 2 raw law forces `ii->+i`, `ij/ji->+j`, `jj->-i`.
2. **Interaction rectangle — exact.** Its signed count collapse is `(ac-bd,ad+bc)` for every source word pair.
3. **Closed process carrier — exact.** Source position chains tensor by Cartesian product; `C4` labels add mod four. Evaluation is multiplicative, the unit action is equivariant, and process multiplication is associative/commutative up to canonical finite-poset isomorphism.
4. **Cancellation — two different levels.** Signed count cancellation is terminating and confluent. Position-retaining cancellation is nonconfluent, with minimal `3x2` witness `iij x ij`.
5. **Path-process advance — positive.** Taking all residual normal forms and their inherited-order linearizations yields a canonical source-sensitive relation. For W2 `(2,1)^2`, support sizes are `[[5,14,8],[14,11,14],[8,14,5]]`, all proper subsets of the 35-path target fiber.
6. **Source order is not erased.** The nine W2 relations differ; their union reaches only 31 of 35 target words.
7. **No canonical single path is forced.** Nontrivial source pairs generate multiple target words; selecting one adds a selector absent from the derived process.
8. **Associativity boundary is exact.** The uncancelled interaction tensor has a canonical associator. Destructive binary cancellation/path readout is not associative: `ij,ij,ji` gives left `{jiji,jjii}` and right `{iijj,ijij}`.
9. **Minimal new law.** `C4`-labelled Cartesian position tensor is sufficient and minimal relative to closure, unit-equivariance and source-order retention. Its semantic status is `N1_DERIVED_OPERATIONAL`, not N0.
10. **BRC remains downstream.** Stage 3 process weights/support project toward path/N/Boolean shadows only after the process is fixed; BRC chooses neither cancellation nor orientation nor target word.

## Deterministic evidence

- all nonempty binary source words of length `<=6`: `126`;
- all ordered source-path pairs: `15,876`;
- maximum interaction rectangle: `36` cells;
- full W2 nine-pair source-order census: PASS;
- unit-normalization witness `(1,2)^2`: PASS;
- full process associator: `512` selected triples, PASS;
- positional cancellation smallest counterexample preserved;
- binary collapsed relation associativity counterexample preserved;
- mismatch count: `0`;
- exhaustive row SHA-256: `8eb68b77c48a81b27ba764362db5aee20f512cd7f31010edb1bad51f975d47df`.

## Acceptance gates

1. `STAGE2_FROZEN_DEPENDENCY_REPLAY_INTACT = PASS`
2. `PAIRWISE_INTERACTION_TABLE_DERIVED_OR_NONUNIQUENESS_CLASSIFIED = DERIVED_UNIQUELY`
3. `INTERACTION_COUNT_COLLAPSE_EQUALS_RAW_ROOT_PRODUCT = PASS`
4. `SIGNED_CANCELLATION_TRACE_NORMAL_FORM_EXACT = PASS`
5. `REPRESENTATIVE_LEVEL_CANCELLATION_CONFLUENCE_OR_MINIMAL_COUNTEREXAMPLE = NONCONFLUENT / MINIMAL_3x2_PRESERVED`
6. `UNIT_EQUIVARIANT_PROCESS_LEVEL_CLASSIFIED = EXACT_N1_PROCESS`
7. `SOURCE_PATH_ORDER_RETENTION_OR_TOTAL_ERASURE_CLASSIFIED = RETENTION_PROVED`
8. `TRIVIAL_WHOLE_TARGET_FIBRE_RELATION_STRICTLY_IMPROVED_OR_PROVED_UNIMPROVABLE = STRICTLY_IMPROVED`
9. `PROCESS_ASSOCIATIVITY_COHERENCE_OR_NO_GO_CLASSIFIED = CANONICAL_ASSOCIATOR_BEFORE_DESTRUCTIVE_READOUT`
10. `MINIMAL_ADDITIONAL_PROCESS_STRUCTURE_CLASSIFIED = PASS`
11. `ALL_MULTIPLICITY_LAYERS_SEPARATED = PASS`
12. `SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE = PASS`
13. `DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES = PASS`

Semantic scope remains `FROZEN_R061_SECTOR_LOCAL_PYTHAGOREAN_TRACE_SEMANTICS`. No global full-plane native Gaussian/process multiplication is claimed.

`R063_STAGE4 = NOT_OPENED`.
