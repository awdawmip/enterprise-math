# R057 Stage D — OP001 coefficient / generator scale-stability analysis

Researcher-ID: `EM-R057-6A31F2`

Status: `STAGE_D_SCALE_STABILITY_FROZEN / AWAITING_DRIVER_REVIEW / NOT_THEOREM`

## Main result

**Generator stability is stronger than coefficient stability.** The A-native `SIGNED_BULGE_DENSITY + RUN_SWITCH_DENSITY` pair remains the dominant low-dimensional core, but the best coefficients drift with radius/window and do not support a unique asymptotic rational pair on TD000.

### Frozen G002 scale profile

| R | MSE | bias | phase spread |
|---:|---:|---:|---:|
| 24 | 1.5009564672429295e-05 | -0.002076459052831455 | 0.011432383794828915 |
| 32 | 6.6827552594431763e-06 | 0.0011504691940542229 | 0.009189210640036638 |
| 40 | 5.0739711316643309e-06 | 0.0019257491862369285 | 0.0040920463748235214 |
| 56 | 2.4395631385896703e-06 | 0.00082750350332091072 | 0.0047494076433234333 |
| 72 | 8.4420907295432225e-07 | -0.00030686350546405006 | 0.0027467545773642854 |
| 96 | 1.0984207684199942e-06 | 5.5147073121745533e-06 | 0.0039742629091126247 |
| 128 | 8.8543331906110875e-07 | -0.00019324165262857296 | 0.0032958851091087205 |
| 160 | 8.4018255670002821e-07 | -0.00047599953256808697 | 0.00266213878200805 |
| 224 | 1.1449509116735891e-06 | -0.00091184569812678229 | 0.0017570403160269699 |

### G002 per-radius coefficient refits

| R | a_R | b_R | MSE |
|---:|---:|---:|---:|
| 24 | 0.032821433758093606 | -0.017842430195226022 | 8.8095458922557982e-06 |
| 32 | 0.034045025662795665 | -0.020459013550575864 | 3.5699776922122674e-06 |
| 40 | 0.022223710429046053 | -0.018602220280431587 | 1.3175961287110361e-06 |
| 56 | 0.011698574127365646 | -0.017021028961867336 | 1.515585276343018e-06 |
| 72 | 0.014252974668114491 | -0.017087663057757017 | 1.590180596367354e-07 |
| 96 | 0.016930539249837333 | -0.017532998255227659 | 9.149333219527203e-07 |
| 128 | 0.011153912577940513 | -0.018952348428782812 | 4.7679214189475601e-07 |
| 160 | 0.012527378635955386 | -0.018999039706130146 | 4.3290160549786052e-07 |
| 224 | 0.016265822506879139 | -0.01729220770778199 | 2.3254301199244858e-07 |

### Nested large-scale windows

| cut | a_cut | b_cut | MSE |
|---:|---:|---:|---:|
| >= 56 | 0.016351608671014362 | -0.017531667333381813 | 7.5787802128979642e-07 |
| >= 72 | 0.016284598570810556 | -0.017553830947550191 | 5.8136185706366339e-07 |
| >= 96 | 0.016282473316814719 | -0.017684099218269477 | 6.1882995276093483e-07 |
| >= 128 | 0.011673430706886173 | -0.018950097285335563 | 4.0184948224949693e-07 |
| >= 160 | 0.01194957199878908 | -0.018929826506221756 | 3.5894402614213986e-07 |

### Generator ablation (global TD000 refit)

| family | MSE | coefficients |
|---|---:|---|
| BULGE_ONLY | 3.2452135534624275e-05 | `0.061314601589259284` |
| RUN_SWITCH_ONLY | 2.7984010769934879e-05 | `-0.012791802574432094` |
| BULGE_RUN | 3.7796612357531551e-06 | `0.022785781250013105, -0.015865262127600279` |
| BULGE_RUN_PLUS_TURN_QUADRATIC | 3.5633278456482944e-06 | `0.028943542912519184, -0.015122084218265089, -0.040727929262670041` |
| FULL_FOUR | 3.4489886814529973e-06 | `0.029517070635872118, -0.03367097233158426, -0.053828336363203694, 0.015071034088516823` |

- Bulge+run beats the best single generator by a factor of `7.40384` globally, and beats both single-generator models in every nested large-radius window.
- Adding turn quadratic moment improves global MSE by about `5.724%`; full four generators improve by about `8.749%` relative to the two-generator pair.
- Stage-C `(1/44,-1/63)` is an excellent **global TD000 compression**: unconstrained global refit changes it only to `(0.022785781250013105,-0.015865262127600279)` and improves MSE by only `0.00617216%`.
- This does **not** make those rational values scale-limit constants: nested-window coefficients shift around `R>=128`.
- Primary D3 1/R and 1/R² trajectory fits do not robustly beat constant models across large-radius domains; no rational/algebraic reconstruction is attempted.

## Next-step evidence

`EXPAND_TEACHER_RADIUS_BEFORE_K_SUPPORTED` — keep K<=8 and OP001 fixed in the next approved generation and add larger radii first. The unresolved variable is scale/regime behavior of coefficients, not current generator expressiveness.

## Frozen hashes

- `R057_OP001_SCALE_STABILITY_ATLAS_SHA256 = 555dab3a917f978cf64b28af82e2b091e83a7316f378ba25cee921eb359c239b`
- `R057_OP001_COEFFICIENT_TRAJECTORY_SHA256 = 89eef3f0191c8ceecaf8f813c2d900c01a0ab9046a36b87791aa1bd5e3226eaa`
- `R057_OP001_GENERATOR_ABLATION_SHA256 = 7f10ad5e3a03e00e35959d1a9b0f6974af9c0378959da17e18894efbe0888ba4`
- `R057_STAGE_D_EXACT_CHECK_RESULTS_SHA256 = a642988e108ea50fceacaacf2c4c621e44ed075524a407e0a596f721b77abe20`
- `R057_STAGE_D_SCALE_STABILITY_CHECKPOINT_SHA256 = 3e730ccb9fd67506a1bdbb7929fc6479ddcf3d51c5236e4d93dd799404e8ff7b`

Independent checker: `63/63 PASS`, failures `0`.

`CI_NOT_REQUIRED_FOR_RESEARCH`
