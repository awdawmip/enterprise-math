# E001 Material Validation Gate — Measurement Scale, Fixed Domain, and Held-Out Error

Status: `ACTIVE ENGINEERING GATE / NOT FOUNDATION`

Owner: `agent/e001-multires-collision` / Draft PR #70

## 1. Why this gate exists

An all-points material fit measures representation capacity. It does **not** by itself establish predictive usefulness. E001 therefore separates experimental representation, material-model precision, calibration, and evaluation before the NIST foam stage.

The required pipeline is now:

`declared measurement scale -> fixed benchmark domain -> train-only calibration -> held-out evaluation -> runtime compilation`.

A result that reports only the best in-sample curve is incomplete engineering evidence.

## 2. Three scales that must remain distinct

For a material benchmark, keep these objects separate:

1. **measurement scale** — how an experimental quantity was recorded, e.g. a count `v` at scale factor `100` representing the exact rational `v/100` in a declared unit;
2. **benchmark domain** — the physical/count interval over which the model is intended to operate;
3. **model precision `A`** — the number of finite response/deformation cells available to the E001 material representation.

No rule identifies `A` with the experimental `scale_factor`. They may happen to be numerically equal without gaining any special meaning.

`material_measurement.py` records the first distinction explicitly. Unit strings are currently opaque metadata; E001 does not pretend to provide a dimensional-analysis algebra.

## 3. Fixed-domain anti-leakage rule

Train/test splitting must not redefine the material coordinate system.

The deformation interval is therefore declared before a split. A held-out endpoint or interior point may be removed from calibration without changing the map from deformation counts to finite cells.

Only training **responses** may influence:

- the discrete input-root power;
- the discrete output-hardening power;
- the integer output scale.

Held-out targets are used only for evaluation. `material_validation.py` contains a regression in which a held-out target is changed drastically and the fitted training model remains byte-for-byte identical.

## 4. Deterministic Treloar validation checkpoint

The same 25-point Treloar uniaxial benchmark [SRC-TRELOAR-1944-RUBBER] / [SRC-THERMALCANN-2023-TRELOAR-DATA] is evaluated with deterministic interleaved five-fold splitting:

`test_fold(i) = {index : index mod 5 = i}`.

The physical/count domain remains fixed at `[100,761]` for every fold.

Independent reconstruction of the current benchmark gives the following held-out RMSE values in the published response units:

| Model | Five-fold RMSE |
|---|---:|
| Neo-Hooke | ~0.7999 |
| Mooney-Rivlin | ~0.6351 |
| Yeoh-2 | ~0.3142 |
| Yeoh-3 | ~0.1244 |
| E001 integer, `A=128` | ~0.2145 |
| E001 integer, `A=2048` | ~0.1842 |
| E001 integer, `A=8192` | ~0.1804 |

This strengthens the existing negative boundary. E001 is a nontrivial finite representation, but it does **not** currently beat Yeoh-3 on held-out Treloar uniaxial data.

## 5. Precision is also a capacity control

In-sample error continues to improve as more finite states are made available, but held-out improvement is smaller and the selected shape can become less stable.

At `A=128`, all five current validation folds select `G4/H2` (with slightly different output scales). At higher precision, four folds favor `G8/H3` while one high-deformation-containing fold can select a more complex `G12/H4` shape in the tested search box.

The engineering interpretation is deliberately modest:

> higher precision opens additional material distinctions and therefore additional fitting freedom; that freedom must earn its cost on held-out data.

This is not a general statistical theorem about Enterprise Math. It is an E001 pressure-test observation.

## 6. Mandatory reporting contract for real-material claims

Until superseded by a stricter benchmark protocol, an E001 real-material result must report at least:

1. source/provenance of the observations;
2. exact measurement scales and unit tags;
3. fixed operating/benchmark domain;
4. model precision `A` separately from fitted material parameters;
5. training or all-points error;
6. a deterministic held-out or external-test error;
7. the fitting/search box and tie rule;
8. comparable established baselines;
9. runtime state size for deployment claims;
10. negative results and known scientific boundaries.

A higher-precision fit may not be promoted merely because its training SSE is smaller.

## 7. Source assets

- `src/enterprise_math/material_measurement.py`;
- `tests/test_material_measurement.py`;
- `src/enterprise_math/material_validation.py`;
- `tests/test_material_validation.py`;
- `experiments/e001_treloar_validation_benchmark.py`.

Repository-wide CI is not claimed while PR #70 remains Draft/concurrent. The fixed Treloar numbers above have been independently reconstructed from the same public 25-point data and formulas.

## 8. Next gate

NIST VN01 foam should inherit this protocol unchanged before adding loading/return history or rate state. In particular, the raw acquisition scale, deformation domain, E001 state precision, branch/history state, and evaluation split must be separately declared.
