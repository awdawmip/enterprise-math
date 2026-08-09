# E001 Material Validation Gate — Measurement Scale, Fixed Domain, and Held-Out Error

Status: `ACTIVE ENGINEERING GATE / NOT FOUNDATION`

Owner: `agent/e001-material-foundation`

## 1. Why this gate exists

An all-points material fit measures representation capacity. It does **not** by itself establish predictive usefulness. The material benchmark therefore separates experimental representation, material-model precision, calibration, and evaluation.

Required pipeline:

`declared measurement scale -> fixed benchmark domain -> train-only calibration -> held-out evaluation`.

A result that reports only the best in-sample curve is incomplete engineering evidence.

## 2. Three scales that must remain distinct

Keep these objects separate:

1. **measurement scale** — how an experimental quantity was recorded, e.g. integer count `v` at scale factor `100` represents exact rational `v/100` in a declared unit;
2. **benchmark domain** — the physical/count interval over which the model is intended to operate;
3. **model precision `A`** — the finite material-state resolution available to the integer curve.

No rule identifies `A` with the experimental scale factor. Equality between them is permitted but has no special semantics.

`material_measurement.py` records this separation explicitly. Unit strings are opaque metadata here; this line does not pretend to provide dimensional algebra.

## 3. Fixed-domain anti-leakage rule

Train/test splitting must not redefine the material coordinate system. The deformation interval is declared before a split. Removing a held-out endpoint or interior point must not change the map from deformation counts to finite cells.

Only training **responses** may influence the discrete input-root power, output-hardening power, and integer output scale. Held-out targets are evaluation-only. A regression test changes a held-out target drastically and requires the fitted training model to remain unchanged.

## 4. Deterministic Treloar validation checkpoint

The same 25-point Treloar uniaxial benchmark [SRC-TRELOAR-1944-RUBBER] / [SRC-THERMALCANN-2023-TRELOAR-DATA] is evaluated with deterministic interleaved five-fold splitting:

`test_fold(i) = {index : index mod 5 = i}`.

The count domain remains fixed at `[100,761]` for every fold.

Independent reconstruction of the benchmark gives these held-out RMSE values:

| Model | Five-fold RMSE |
|---|---:|
| Neo-Hooke | ~0.7999 |
| Mooney-Rivlin | ~0.6351 |
| Yeoh-2 | ~0.3142 |
| Yeoh-3 | ~0.1244 |
| E001 integer, `A=128` | ~0.2145 |
| E001 integer, `A=2048` | ~0.1842 |
| E001 integer, `A=8192` | ~0.1804 |

This strengthens the negative boundary: the finite integer family is nontrivial, but it does **not** currently beat Yeoh-3 on held-out Treloar uniaxial data.

## 5. Precision is also a capacity control

In-sample error improves as more finite states are made available, but held-out improvement is smaller and selected shape can become less stable.

At `A=128`, all five current folds select `G4/H2` with slightly different output scales. At higher precision, four folds favor `G8/H3` while one high-deformation-containing fold can select a more complex `G12/H4` in the tested search box.

Engineering interpretation:

> higher precision opens additional material distinctions and therefore additional fitting freedom; that freedom must earn its cost on held-out data.

This is an E001 observation, not a universal statistical theorem.

## 6. Mandatory reporting contract for real-material claims

Until superseded by a stricter protocol, report at least:

1. source/provenance of observations;
2. exact measurement scales and unit tags;
3. fixed operating/benchmark domain;
4. model precision `A` separately from fitted material parameters;
5. training/all-points error;
6. deterministic held-out or external-test error;
7. fitting/search box and tie rule;
8. comparable established baselines;
9. negative results and known scientific boundaries.

A higher-precision fit may not be promoted merely because training SSE is smaller.

## 7. Source assets

- `src/enterprise_math/material_response.py`;
- `src/enterprise_math/material_fit.py`;
- `src/enterprise_math/material_measurement.py`;
- `src/enterprise_math/material_validation.py`;
- corresponding tests;
- `experiments/e001_treloar_material_benchmark.py`;
- `experiments/e001_treloar_validation_benchmark.py`.

## 8. Next gate

NIST VN01 foam should inherit this protocol before adding loading/return history or rate state. Raw acquisition scale, deformation domain, finite-state precision, branch/history state, and evaluation split must be separately declared.
