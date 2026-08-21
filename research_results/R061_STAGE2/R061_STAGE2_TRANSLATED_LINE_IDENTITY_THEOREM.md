# R061 Stage 2 — Translated Line Identity Theorem

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`TRANSLATED_LINE_IDENTITY_EXACT = true`

## 1. Interior translated trace

If `D(P->Q)` lies in translated open sector `S_ij(P)` with local nonnegative components `(a,b)`, define

`T_{P;a,b}^{(ij)} = (P, [X_i^a X_j^b])`

under the frozen relation generated only by

`X_i X_j ~ X_j X_i`.

Equivalently, the minimal typed fields are

`(start_vertex_id, displacement_sector, component_trace_class)`.

The endpoint `Q` is derivable from these fields, but endpoint coincidence alone is not the line identity.

## 2. Why the start vertex is mandatory

The origin trace `[X_i^a X_j^b]` identifies a component class, not a concrete translated placement. Two parallel translated segments with the same `(ij,a,b)` but different starts have different cell fibers and different physical placement.

Therefore the start vertex cannot be dropped.

`(ij,a,b)` alone is a translation-orbit trace type, not a concrete line segment identity.

## 3. Axis identity after gluing

For a directed displacement of `n` native ticks on translated positive axis `E_i(P)`, the two adjacent sector presentations are glued into one global identity

`T_{P;E_i,n}^{AXIS}`.

Its line identity is deduplicated by

`(start_vertex_id, axis_label, radial_component)`.

The two chart-local cell trajectories are **not** deduplicated; their start anchor cells differ and both remain realizations.

## 4. Zero identity

For `P=Q`, define one global zero trace

`T_P^0`.

It has zero native component content. Its discrete support consists of the three distinct sector-local incidence-only branches `Sigma_P^(12)`, `Sigma_P^(23)`, `Sigma_P^(31)`.

This is triple chart support of one zero trace identity, not a simultaneous three-cell state.

## 5. Same endpoint is still weaker than same line

The translated identity preserves the Stage 1 rule:

`SAME_CARRIER_ENDPOINT != SAME_NATIVE_LINE_IDENTITY`.

A carrier endpoint path using the reverse third direction may reach the same terminal cell, but it is not a linearization of `[X_i^a X_j^b]` and therefore does not belong to `T_{P;a,b}^{(ij)}`.

No jump-count criterion is used.

## 6. Translation covariance

For any coordinate-vertex translation `R`,

`T_{P;a,b}^{(ij)} -> T_{P+R;a,b}^{(ij)}`

preserves sector label and component trace class while changing only concrete placement.

The deterministic checker tested `12,005` translated point-pair cases under five independent lattice translations and found zero mismatch in decomposition or directed native line length.
