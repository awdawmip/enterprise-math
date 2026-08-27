# Driver Review — P018 Ternary Carry Threshold-to-Cardinality

Status: `DRIVER_FINAL / ACCEPTED / P018_TERNARY_THRESHOLD_TO_CARDINALITY_CLOSED / L4_FORMAL_THEOREM / NO_FOUNDATION_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-FREE-C19420 / CONTROL_PLANE`

Task: `RS-P018-TERNARY-CARRY`

Publication: `TP2-674C46ECF01DD1D3E6F4`

Execution: `ER-21C68CC5C36A48DA17A9`

Researcher-ID: `EM-P018TC-E9AA2D`

Result: `RR-046FB92F6C42BB24A56C`

Source result PR: `#690`

Current-main integration PR: `#703`

Integration merge: `09aa0b9bc497e3375ef00857d5becd847736bba1`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = ACHIEVED`.

`P018_TERNARY_THRESHOLD_TO_CARDINALITY_EXACT_AND_LEAN_CHECKED_NO_SORRY = true`.

`RESULT_CLASS = L4_FORMAL_THEOREM / EXACT_FINSET_CARDINALITY / TERNARY_CARRY_CLOSURE`.

`UNRESOLVED_RESIDUE = NONE`.

`FOUNDATION_MUTATION = NONE`.

`SUCCESSOR_TASK = NONE`.

The Driver accepts the exact quotient-root atlas decomposition, binary cardinality theorem, and ternary threshold specialization. The old P018 threshold-to-cardinality frontier is closed. No successor is opened merely to extend finite scans.

## 2. Accepted exact theorem package

For positive `n`, let

`H = root (s+2) ((s+1)*n - 1)`

and

`D = n / (H+1)^(s+1)`.

The finite quotient-root atlas over denominators `1,...,n` is decomposed into:

1. a high-denominator image from `1,...,D`, with exactly `D` states by exact injectivity;
2. the forced positive low roots `1,...,H-1`;
3. the single optional horizon state `H`, present exactly when `(D+1)*H^(s+1) <= n`.

For `H>0` the high and low charts are disjoint. The formal theorem separately handles the `H=0` boundary rather than silently applying the positive-horizon description there.

Therefore:

`|quotientRootStates(s,n)| + 1 = D + H + kappa`

where `kappa` is the indicator of `(D+1)*H^(s+1) <= n`.

With

`q = H/(s+1)`,
`X = (H+1)^(s+1)`,
`Y = H^(s+1)`,
`A = max(q*X,(q+1)*Y)`,
`B = (q+1)*X`,

and ternary carry `tau` taking values `0,1,2` on the three threshold regions, the already-proved `ternary_count_from_binary_carry` theorem yields:

`|quotientRootStates(s,n)| + 1 = H + q + tau`.

The accepted Lean endpoints are:

- `EnterpriseMath.Precision.quotientRootStates_binary_cardinality`;
- `EnterpriseMath.Precision.quotientRootStates_ternary_cardinality`.

## 3. Formal proof gate

The theorem source blob is:

`EnterpriseMath/Precision/RootStateAtlasCardinality.lean`
`e46d6037257d4f330d6cd46459beb0bc1a11ba5d`.

Historical result certification:

- Lean workflow run `#888`;
- run id `33038025114`;
- job `98405044303`;
- compiled commit `5ab06db341bc4e579a8e86ca5d14f39c3a1f5e2a`;
- exact command `lake build --wfail -KCI EnterpriseMath`;
- conclusion `SUCCESS`.

Current-main semantic integration was independently revalidated:

- integration head `d12630848773c7bdf46733a6b74590edfb312b6f`;
- Lean workflow run `#898`;
- run id `33055614313`;
- job `98461593712`;
- warning-fatal compile step completed `SUCCESS`;
- full Lean workflow conclusion `SUCCESS`.

The theorem blob is unchanged between the original certificate and current-main integration. Direct source audit found no `sorry`, `admit`, or custom `axiom`.

## 4. Finite regression boundary

The frozen regression checks both exact formulas for:

- `s = 0,...,7`;
- `n = 1,...,2499`;
- `19,992` cases;
- `0` failures.

This remains `FINITE_REGRESSION_ONLY_NOT_A_PROOF`. General validity is supplied by the Lean theorem.

## 5. Method-harvest provenance

The historical branch

`research/p018-binary-root-atlas-lean@9fa0a84b4fff7f5140bc6cf96779a774c891ebcb`

is retained only as disclosed same-task method-harvest provenance. Its finite-atlas architecture was not promoted as canonical truth; the current closure was rebuilt on the stronger current P018 predecessor lemmas and warning-fatal checked.

## 6. Integration and CI boundary

The stale owner stack was integrated in lineage order:

`#690 -> #328 -> #226 -> #225`.

Top stale owner PR `#197` could not safely merge to current main because its base predated substantial parallel work. The Driver therefore performed a semantic replay onto current main, preserving all concurrent shared files and applying only P018-specific blobs. That replay was merged through PR `#703` as commit:

`09aa0b9bc497e3375ef00857d5becd847736bba1`.

Two non-P018 CI issues are explicitly not relabeled as successful:

1. `reference-integrity` fails on the pre-existing `RS-P022-OBSERVATION-HISTORY` dual-publication fork; both conflicting publication records are already present on the PR base.
2. the full Python `quality` workflow did not complete successfully. It logged pre-existing FoundationBackflow validation errors and later the hosted runner received a shutdown/cancellation signal. P018 tests that executed before shutdown were passing, but this review does not claim the whole quality workflow passed.

Neither issue changes the theorem-critical P018 Lean proof or introduces a P018-specific counterexample.

## 7. Final freeze

`RS-P018-TERNARY-CARRY = TERMINAL / ACCEPTED`.

`RR-046FB92F6C42BB24A56C = ACCEPTED`.

`DESTINATION = L4 / EnterpriseMath/Precision/RootStateAtlasCardinality.lean`.

`P018_THRESHOLD_TO_CARDINALITY_FRONTIER = CLOSED`.

`LEGACY_HANDOFF = SUPERSEDED_BY_CURRENT_IMMUTABLE_RESULT`.

`STALE_TOP_OWNER_PR_197 = SUPERSEDED_BY_CURRENT_MAIN_SEMANTIC_INTEGRATION`.

`FINITE_SCAN_SUCCESSOR = NONE`.
