# R057 Stage F — Dimensionless STAR-basis transfer and within-arm drift test

Researcher-ID: `EM-R057-6A31F2`

Status: `STAGE_F_DIMENSIONLESS_STAR_TRANSFER_FROZEN / AWAITING_DRIVER_REVIEW / NOT_THEOREM`

## F0 unit gate

- PASS 393/393; hash `d902d2f46161318168bc10ffd96546b15201172fdd2a49090f78ffc3515a7909`.
- Exact A units: `ell_edge_A=1/sqrt(3)`, `L_chord=sqrt(Q/3)`, `signed_area=(sqrt(3)/12)A2`.
- All 65 frozen packet classes satisfy corrected-physical == scale-cancelled-internal STAR values exactly.

## Global zero-refit results

| basis | coefficients | MSE | MAE | phase spread |
|---|---|---:|---:|---:|
| D1 | `0.012238021074562497, -0.0038566365799604305` | `3.2313017005482164e-06` | `0.0012689554543402852` | `0.011689849764731974` |
| D2 | `0.012567725670299635, -0.01878347013038947` | `3.4275552444926749e-06` | `0.001308226848974115` | `0.012153239042087982` |
| D3 | `0.010738231159592106, -0.023434694173124094, -0.005257373412722947, 0.10374665311865718` | `2.7499748702756741e-06` | `0.0011441529914078387` | `0.01193412900673696` |

Legacy combined TD000+TD001 MSE: `3.2313017005482164e-06`. D1 reproduces it exactly under the independently refit STAR coordinates.

## Drift result

- `STAR_DRIFT_NOT_REDUCED`.
- `STAR_NORMALIZATION_INSUFFICIENT`.
- `STAR_ROLE_REFACTORIZATION_FOUND`.

Nested-window drift summary:

| basis | median relative span | mean successive normalized variation | sign flips |
|---|---:|---:|---|
| legacy | `0.19272570596223013` | `0.091223559455211531` | `[0, 0]` |
| D1 | `0.22063643721201917` | `0.12434267101652746` | `[0, 0]` |
| D2 | `0.22185151540171272` | `0.11719045715021004` | `[0, 0]` |
| D3 | `4.0463763925088845` | `2.350639227394665` | `[0, 2, 2, 2]` |

Normalization control: at K7, legacy `(a,b)` maps exactly to D1 STAR `(4a/7, sqrt(3)b/7)`. Static nonzero coordinate scaling preserves within-basis relative spans; positive scaling preserves sign flips. Hence normalization alone explains **0%** of normalized drift reduction.

## D1 vs D2 role

- Definition-level legacy role: **D1 topology-only run**.
- D2 has slightly lower MSE than D1 in every nested window `R>=56,96,160,224,320`.
- D1 has lower all-data global MSE and slightly smaller median relative span; D2 has slightly smoother successive-window trajectory.
- Therefore D1/D2 are a metric-split near tie for stability; D3 is decisively less stable.

## Ablation

Global MSE:

- AREA_STAR_ONLY: `4.4986422047864829e-05`
- RUN_SWITCH_STAR_ONLY: `2.6608461705483887e-05`
- RUN_DEFECT_STAR_ONLY: `2.8567497670119653e-05`
- D1: `3.2313017005482164e-06`
- D2: `3.4275552444926749e-06`
- D3: `2.7499748702756741e-06`

Both D1 and D2 beat every single-generator model by more than 8x global MSE. `RUN_SWITCH_STAR_ONLY` is the best single globally; `RUN_DEFECT_STAR` becomes useful mainly as a paired large-scale refinement.

## Validation

- Independent checker: `47/47 PASS`, SHA256 `a054ef4e37244e8a774dacb14b645e98c1eb0d73dae2c2d1dc6721a9849b4195`.
- Independent parser: 8-state min-plus cyclic tiling automaton.

## Frozen checkpoint

`R057_STAGE_F_STAR_TRANSFER_CHECKPOINT_SHA256 = e8ad43b87b4a64f8b7b1d888bab1bcb96711c36faba592caac724c35edfb848e`
