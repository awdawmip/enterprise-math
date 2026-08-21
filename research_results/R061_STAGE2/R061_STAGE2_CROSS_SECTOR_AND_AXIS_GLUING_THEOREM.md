# R061 Stage 2 — Cross-Sector and Axis Gluing Theorem

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`CROSS_SECTOR_AXIS_GLUE_PASS = true`

## 1. Displacement chart, not endpoint origin chart

For arbitrary `P,Q`, the native line chart is selected by the translated displacement `D(P->Q)`, not by the origin-based sector containing `P` or `Q`.

This removes the apparent cross-sector ambiguity without subtracting native signed coordinates.

Example:

- start `P` has canonical origin address `(1,0,3)` and lies in origin sector `S31`;
- end `Q` has canonical origin address `(1,1,0)` and lies in origin sector `S12`;
- nevertheless `D(P->Q)=(3,4,0)`;
- the line is exactly the translated `S12(P)` trace `T_{P;3,4}^{(12)}` with native directed length `5`.

Origin-chart membership of endpoints is therefore not line-sector typing.

## 2. Axis double-chart gluing

If `D(P->Q)` is on translated positive axis `E_i(P)`, it has exactly two adjacent local sector presentations.

The global line identity is deduplicated as

`(P,E_i,n)`.

The two local realization trajectories remain distinct because their translated start anchors are different.

The checker replayed `273` translated global axis identities over seven start vertices and radial coordinates `0..12`, corresponding to `546` chart presentations. Every adjacent-chart trajectory pair remained physically distinct; mismatch count was zero.

## 3. Zero triple-chart gluing

At `P=Q`, all three sector-local zero traces have the same coordinate endpoint but three different incident anchor cells.

They are glued to one global zero trace identity `T_P^0` while retaining three separate incidence-only support branches.

## 4. Global rule

The exact gluing hierarchy is:

1. open translated sector: one line chart;
2. translated positive axis: two chart presentations -> one global line identity, both trajectories retained;
3. zero displacement: three zero presentations -> one global zero identity, three incidence support branches retained.

No cell trajectories are deduplicated merely because the coordinate endpoint is shared.
