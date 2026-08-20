# R061 Stage 1 — Native Line Trace Fiber / Origin-Affine Validation Proof

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`  
Taskbook source: `4183c1300994e61f5a4443aea8487438a7210cc6`  
Stage 0 frozen head: `e6657ce00382d52acda319f0108b787a03e9d5f2`  
Owner branch: `research/r061-stage1-native-line-trace-realization`  
Researcher-ID: `EM-R061S1-4183C1`

## Final status

`NATIVE_LINE_PATH_FIBER_IS_EXACTLY_TYPED_AND_ALGEBRAICALLY_GENERABLE = true`.

`NATIVE_LINE_PATH_FIBER_DERIVABLE_FROM_CURRENT_FOUNDATION = true`.

Selected candidate:

`C1_TRACE_LINEARIZATIONS_WITH_NATIVE_INCIDENCE`.

No Stage 2 is opened by this researcher result.

## 1. Frozen Stage 0 regression

Stage 1 does not re-prove the accepted Stage 0 theorems. It regression-checks them.

Independent Stage 1 regression reproduced the frozen invariants:

- coordinate census `N=0..100000`: mismatch `0`;
- coordinate SHA256: `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`;
- Euclid square-hypotenuse audit through `r=4096`: mismatch `0`;
- explicit shuffle through `a+b<=22`: `8,388,607` words, mismatch `0`;
- shuffle SHA256: `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`;
- compressed Pascal through `a+b<=512`: mismatch `0`;
- Pascal SHA256: `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`.

Therefore the Stage 1 change is entirely in native realization/typing.

## 2. Minimal native typing correction

The raw tuple ambiguity is resolved by two typed integer charts:

- vertex/component address `VADDR_ij(a,b)`;
- affine cell-center address `CADDR_ij(a,b)`.

The native line endpoint is the typed pair

`(V_ij(a,b), C_ij(a,b))`.

Native length belongs to the coordinate/vector component object; the terminal discrete state belongs to the circle cell.

This proves:

`NATIVE_OBJECT_TYPING_COMPLETE = true`.

## 3. Origin incidence and affine anchor

At radius `1/sqrt(3)`, exactly three mutually neighboring circle cells meet at `O_E`.

Because their centers occupy the three open 120-degree sectors, every fixed sector has a unique origin-anchor cell.

Hence

`Sigma_O^(ij): O_E -> C_ij(0,0)`

is exact and canonical for fixed `(ij)`.

The affine relation is

`ctr(C_ij(a,b))=V_ij(a,b)+s_ij`,

where `s_ij=ctr(C_ij(0,0))-O_E` is constant.

No numerical `+1/-1` is required.

This proves:

`ORIGIN_INCIDENCE_EXACT = true`.

`AFFINE_ADDRESS_ANCHOR_EXACT = true`.

## 4. Line identity and realization

The line identity is the native component trace

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`.

Its path representatives are all native realizations of its linearizations after `Sigma_O^(ij)`.

An adjacent `X_i X_j <-> X_j X_i` swap is realized by a valid local commuting carrier diamond and preserves the native component identity.

A reverse-third carrier chord does not preserve that native identity because the carrier relation is explicitly not a native vector relation.

Thus:

`LINE_IDENTITY_DEFINED_INDEPENDENTLY_OF_ENDPOINT_ONLY = true`.

`LINE_PATH_CLASS_FINITE_AND_CANONICAL = true`.

`LINE_PATHS_SINGLE_CELL_ADMISSIBLE = true`.

## 5. Same endpoint versus same line

The Stage 0 `(1,1)` third-direction counterexample is resolved, not erased.

`-X_k` remains a valid same-endpoint nearest-center carrier route, but it is classified

`CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`

relative to `T_{1,1}^{(ij)}`.

The decision follows from typed native component identity, not from jump count.

Therefore:

`SAME_ENDPOINT_VS_SAME_LINE_CLASSIFIED = true`.

`THIRD_DIRECTION_COUNTEREXAMPLE_RESOLVED_BY_TYPING_NOT_BY_PATCH = true`.

## 6. Competing candidate falsification

- C0 free shuffle: rejected as origin-untyped.
- C1 trace + native incidence: selected.
- C2 all minimum-jump endpoint paths: retained as a different endpoint-realization object, rejected as line identity fiber.
- C3 all simple sector endpoint paths: rejected as infinite.
- C4 balanced digital subset: rejected as an unforced proper subset; no frozen native invariant selects it.
- C5 other incidence-forced class: no stronger class is forced after the exact affine typing.

The full machine-readable matrix is committed.

## 7. Exact native formula

For each sector:

`LINE_E^(ij)(N)`

`= disjoint_union_{a^2+b^2=N} Realize_E(T_{a,b}^{(ij)})`,

with

`Realize_E(T_{a,b}^{(ij)})={Sigma_O^(ij);w : w in Sh_{a,b}(X_i,X_j)}`

and typed terminal endpoint

`(V_ij(a,b),C_ij(a,b))`.

## 8. N=25 / 3-4-5

`D_25={(0,5),(3,4),(4,3),(5,0)}`.

The `(3,4)` branch has exactly `35` native line-path representatives, indexed by three-element `X_i` position subsets of seven positions.

The `(4,3)` branch also has `35`.

The two axis branches have one each in a fixed sector.

Thus fixed-sector total: `72`.

The omitted reverse-third/mixed same-endpoint routes are not in the same native component trace.

This proves:

`N25_3_4_5_NATIVE_PATH_FIBER_EXACT = true`.

## 9. Deterministic Stage 1 native replay

Explicit replay for every pair `a+b<=18`:

- pair count: `190`;
- formal linearizations: `524,287`;
- all three sectors: `1,572,861` sector-local native paths;
- bad neighbor transitions: `0`;
- bad endpoints: `0`;
- bad sector prefixes: `0`;
- bad single-cell states: `0`;
- duplicate trajectories within one trace pair: `0`;
- replay SHA256: `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`.

Compressed trace counting through `a+b<=256`:

- mismatch: `0`;
- SHA256: `aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`.

Axis gluing through radial coordinate `18` found zero duplicate physical trajectories after line-identity deduplication; the two adjacent sector-anchor trajectories are physically distinct and are retained.

Scaling/concatenation audit on the deterministic parameter grid through `8` had zero mismatch.

Therefore:

`DETERMINISTIC_VALIDATION_PASS = true`.

## 10. Acceptance gates

1. `NATIVE_OBJECT_TYPING_COMPLETE = true`
2. `ORIGIN_INCIDENCE_EXACT = true`
3. `AFFINE_ADDRESS_ANCHOR_EXACT = true`
4. `LINE_IDENTITY_DEFINED_INDEPENDENTLY_OF_ENDPOINT_ONLY = true`
5. `LINE_PATH_CLASS_FINITE_AND_CANONICAL = true`
6. `LINE_PATHS_SINGLE_CELL_ADMISSIBLE = true`
7. `SAME_ENDPOINT_VS_SAME_LINE_CLASSIFIED = true`
8. `THIRD_DIRECTION_COUNTEREXAMPLE_RESOLVED_BY_TYPING_NOT_BY_PATCH = true`
9. `THREE_SECTOR_COVARIANCE_PASS = true`
10. `SCALING_AND_CONCATENATION_AUDIT_PASS = true`
11. `N25_3_4_5_NATIVE_PATH_FIBER_EXACT = true`
12. `NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE = true`
13. `DETERMINISTIC_VALIDATION_PASS = true`

All Stage 1 acceptance gates pass.

## 11. Stop condition

Stage 1 package is complete for Driver review.

Do not freeze Stage 2 or alter the current foundation automatically from this researcher branch.
