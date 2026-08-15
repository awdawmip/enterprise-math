# R057 Stage E — TD001 Large-Radius Extrapolation

Researcher-ID: `EM-R057-6A31F2`

Status: `STAGE_E_TD001_LARGE_RADIUS_FROZEN / AWAITING_DRIVER_REVIEW / NOT_THEOREM`

## Ordering discipline

- TD001 registry bytes were frozen first: `803fc5ea249a69af9b4b2597205fc32019a8f41a73bba108868e831fe15d49c7`. The two required registry filename variants are byte-identical aliases.
- Only after registry freeze were 36 circles at R=320,448,640 generated with the original 12 phases.
- E0 was persisted before any TD001 refit: `3f9df458e2cc612fd3fdcd8a9f8bd0c975a309b78741ff31f758198a440644b4`.

## E0 true out-of-window evaluation

| candidate | TD001 MSE | bias |
|---|---:|---:|
| STAGE_C_G002 | `2.6154602047384745e-06` | `-0.0015620532162110567` |
| STAGE_D_TD000_GLOBAL_REFIT | `2.6640423155806052e-06` | `-0.0015772546840468779` |
| STAGE_D_R_GE_160_PAIR | `1.7780896234891746e-07` | `-0.00026616085882617363` |
| FROZEN_G004 | `2.0918258714424032e-05` | `-0.0045425646626318589` |

The frozen Stage-D R>=160 pair transfers best, with ~14.71x lower MSE than frozen Stage-C G002 on the same 36 new circles. Frozen G004 deteriorates strongly.

## E1 per-radius refit

| R | a_R | b_R | MSE |
|---:|---:|---:|---:|
| 320 | `0.02006781098023825` | `-0.015436497464578078` | `1.1290500399620531e-07` |
| 448 | `0.0036695085617418359` | `-0.020693861394707389` | `5.980033254409563e-08` |
| 640 | `0.041418493357882641` | `-0.0027611619013266616` | `1.814572421459778e-08` |

Signs remain a>0,b<0 at all three new radii, but magnitudes are non-smooth; no coefficient limit is established.

## E2 pooled refit

| pool | a | b | MSE |
|---|---:|---:|---:|
| TD001_ONLY | `0.014549566406005385` | `-0.017463869148703223` | `9.5919476570760929e-08` |
| R_GE_224 | `0.012328284521238783` | `-0.018448134576757959` | `1.4185088179939715e-07` |
| R_GE_320 | `0.014549566406005385` | `-0.017463869148703223` | `9.5919476570760929e-08` |
| TD000_PLUS_TD001_ALL | `0.021416536880484373` | `-0.015586411173246977` | `3.2313017005482164e-06` |

## E3 generator ablation

- TD001 pooled bulge+run MSE: `9.5919476570760929e-08`.
- Pair beats best single by `4.5879669149122506x` and beats both singles independently at R=320,448,640.
- Full four improves over the pair by `1.8179246345472995x`, so extra generators remain useful but the pair remains the low-complexity backbone.

## E4 scale-law synthesis

- Constant / a0+a1/R / a0+a1/R^2 were re-tested on the combined TD000+TD001 per-radius coefficient trajectory.
- No large-radius domain shows a robust low-order drift law that passes the convergence gate; rational/algebraic reconstruction was not attempted.

## Disposition

- `GENERATOR_PAIR_SCALE_ROBUST_THROUGH_R640`
- `FROZEN_STAGE_C_COEFFICIENT_PAIR_NOT_SCALE_LIMIT_STABLE`
- `COEFFICIENT_LIMIT_NOT_ESTABLISHED`
- `EXPAND_RADIUS_BEFORE_K_STILL_SUPPORTED`
- `NO_EVIDENCE_REQUIRING_K_EXPANSION`

## Frozen checkpoint

`R057_STAGE_E_LARGE_RADIUS_CHECKPOINT_SHA256 = 0bd03d1b48d5b17e315595cbd4b3818b425ddb2f465e3d35bd75f8e40f39f99c`

## Artifact hashes

- `R057_TD001_TEACHER_REGISTRY_SHA256 = 803fc5ea249a69af9b4b2597205fc32019a8f41a73bba108868e831fe15d49c7`
- `R057_TEACHER_CORPUS_TD001_INCREMENT_SHA256 = 584f11f26b1833fa71f53771ca7e8808fff01ef926d2fb1bdf4f6348f5e32283`
- `R057_TD001_E0_FROZEN_EXTRAPOLATION_SHA256 = 3f9df458e2cc612fd3fdcd8a9f8bd0c975a309b78741ff31f758198a440644b4`
- `R057_TD001_EXTRAPOLATION_RESULTS_SHA256 = 33729380e5b26c4c30d18d26c9dc632bd353cf2495e71fdf4031bc4f7e3e0288`
- `R057_OP001_EXTENDED_SCALE_ATLAS_SHA256 = 3df21e8a7ed644da6aecbd6efd120a5d11cd7e63132df9409eb7d1e778b1ba4f`
- `R057_OP001_EXTENDED_COEFFICIENT_TRAJECTORY_SHA256 = b2dc363375b04bff8654938bf5b38acaf9a3a030f4e41934c99c9fd74cc5f1f4`
- `R057_STAGE_E_EXACT_CHECK_RESULTS_SHA256 = c2452c8cdc7731406f0d11ff912ed7b0d73dbc7a5c8ce2c703eb697d0d2a26e2`

Independent checker: `73/73 PASS`.

`CI_NOT_REQUIRED_FOR_RESEARCH`
