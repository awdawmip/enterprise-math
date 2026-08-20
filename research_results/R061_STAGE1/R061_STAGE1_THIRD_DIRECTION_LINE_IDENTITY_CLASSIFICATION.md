# R061 Stage 1 — Third-Direction Line-Identity Classification

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`  
Researcher-ID: `EM-R061S1-4183C1`

## Status

`SAME_ENDPOINT_VS_SAME_LINE_CLASSIFIED = true`.

`THIRD_DIRECTION_COUNTEREXAMPLE_RESOLVED_BY_TYPING_NOT_BY_PATCH = true`.

## 1. Smallest witness

Fix `S_ij` and let `k` be the third carrier direction family.

For branch `(a,b)=(1,1)`, the line trace is

`T_{1,1}^{(ij)}`.

Its two linearizations are

`X_i X_j`, `X_j X_i`.

After the sector origin anchor both are valid two-transition cell trajectories and terminate at `C_ij(1,1)`.

At the carrier level the one-edge route `-X_k` reaches the same center because

`-t_k=t_i+t_j`.

## 2. Exact classification

The reverse-third one-edge route is classified as

`CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`

relative to the native line identity `T_{1,1}^{(ij)}`.

It is:

- a valid nearest-center **endpoint path**;
- a minimum-jump carrier endpoint path;
- a path to the same terminal circle cell;
- **not** a linearization of `T_{1,1}^{(ij)}`;
- therefore not a representative of the same native `ij` line identity.

## 3. Why this is a typing result, not a jump-count patch

The exclusion has nothing to do with one jump being shorter than two jumps.

The reason is the frozen distinction

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`.

`T_{1,1}^{(ij)}` records one native `i` component and one native `j` component.

Replacing those two labels by a reverse `k` carrier edge would assert the forbidden native identity

`-E_k = E_i+E_j`.

Stage 1 never asserts that identity.

Therefore same carrier endpoint does not imply same native line trace.

## 4. General theorem

For arbitrary `a,b>=0`, define

`Realize_E(T_{a,b}^{(ij)})`

by the trace-linearization rule.

A trajectory belongs to this native line fiber iff, after the typed start incidence, its transition-label word contains exactly:

- `a` labels `X_i`;
- `b` labels `X_j`;
- no third-family labels;

up to reordering by component-preserving commutations.

Hence any path containing a third-family carrier transition is not in the same `T_{a,b}^{(ij)}` fiber, even if carrier relations make its final center coincide.

This does not say such paths are invalid geometry. They remain typed as endpoint paths and, where appropriate, minimum-jump endpoint paths.

## 5. Relation to the old reverse-geodesic realization layer

The retained older theorem that all minimum-jump paths to a fixed endpoint are kept is not contradicted.

Stage 1 separates two realization fibers:

`LINE_PATH_FIBER(T_{a,b}^{(ij)})`

versus

`GEO_REV_E(endpoint)`.

The first preserves native line identity. The second preserves all endpoint graph minimizers after the endpoint is fixed.

They answer different questions and need not coincide.

## 6. N=2 consequence

For the `(1,1)` branch:

- native length squared: `2`;
- line identity: `T_{1,1}^{(ij)}`;
- native line-path representatives: exactly `2`;
- minimum-jump same-endpoint carrier routes include the direct reverse-third route;
- the direct reverse-third route is not counted among the two line-path representatives.

No graph jump count is used to define the native length.

## 7. Verdict

Freeze for Stage 1:

`SAME_CARRIER_ENDPOINT != SAME_NATIVE_LINE_IDENTITY`.

`THIRD_FAMILY_ENDPOINT_PATHS_MAY_EXIST`.

`THIRD_FAMILY_PATH_IN_SAME_IJ_TRACE = false`.

`THIRD_DIRECTION_CLASSIFICATION = CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.
