# E001 Material Engineering Checkpoint — Real Data, Precision Tiers, and Runtime State

Status: `ACTIVE RESEARCH CHECKPOINT / NOT FOUNDATION`

Owner: `agent/e001-multires-collision` / Draft PR #70

## 1. Purpose

E001 material work is no longer evaluated by internal curve aesthetics. The active gate is engineering usefulness under public data and established baselines:

`real material observations -> finite integer fit -> external constitutive comparison -> compiled runtime state -> target-hardware test`.

Negative results are promotion-blocking evidence, not something to hide.

## 2. First real-material benchmark

The benchmark uses 25 uniaxial loading points from the classical Treloar vulcanized-rubber experiments [SRC-TRELOAR-1944-RUBBER], consumed from the machine-readable Steinmann-lineage transcription in the public thermalCANN repository [SRC-THERMALCANN-2023-TRELOAR-DATA]. Classical hyperelastic modeling remains prior engineering mechanics [SRC-STEINMANN-2012-HYPERELASTIC].

The E001 candidate loading family is integer-only after the observations have been represented on their declared finite scales:

1. finite interval projection to `0..A`;
2. integer root transform `G_r`;
3. root-basin quarter-circle complement / finite versine basis;
4. integer hardening `H_p`;
5. one non-negative integer output scale.

`A` is representation precision, not an additional fitted material-shape parameter.

### Current independently reconstructed loading results

| Model | Fitted/shape parameters | RMSE |
|---|---:|---:|
| Neo-Hooke baseline | 1 | ~0.7868 |
| Mooney-Rivlin baseline | 2 | ~0.6216 |
| Yeoh-2 baseline | 2 | ~0.2978 |
| Yeoh-3 baseline | 3 | ~0.1029 |
| E001 integer, A=8192, G8/H3 + output scale | 3 | ~0.1423 |

The E001 family is nontrivially competitive with the lower-order baselines on this one curve, but **does not beat Yeoh-3**. No constitutive-accuracy superiority is claimed.

## 3. Precision tiers select different represented curve structures

The best tested bounded discrete shape changes with `A`:

| A | Best tested shape | RMSE |
|---:|---|---:|
| 64 | G1/H1 | ~0.2760 |
| 128 | G4/H2 | ~0.1942 |
| 512 | G4/H2 | ~0.1667 |
| 1024 | G4/H2 | ~0.1594 |
| 2048 | G8/H3 | ~0.1485 |
| 8192 | G8/H3 | ~0.1423 |

This is an E001 engineering observation, not a universal complexity theorem. General statements about which operation distinctions survive coarse precision belong to P018/P023/A2.

## 4. Runtime compilation frontier

`material_runtime.py` compiles a fitted curve into `A+1` finite integer outputs. Runtime evaluation of an already normalized deformation state is direct lookup; physical-interval normalization can remain an integer operation in the host world engine.

Dense two-byte state sizes for the current Treloar output range:

- A=64: 130 B;
- A=128: 258 B;
- A=512: 1026 B;
- A=1024: 2050 B;
- A=2048: 4098 B;
- A=8192: 16386 B.

`material_runtime_compressed.py` uses standard lossless run-end compression over equal-output plateaus:

- A=64: 39 runs / 117 B;
- A=128: 47 runs / 141 B;
- A=512: 180 runs / 720 B;
- A=1024: 292 runs / 1168 B;
- A=2048: 309 runs / 1236 B;
- A=4096: 410 runs / 1640 B;
- A=8192: 498 runs / 1992 B.

The compression adds no curve approximation beyond the finite curve already declared. LUT and run compression are established implementation techniques; they are not claimed as project inventions.

## 5. Embedded boundary

`material_runtime_codegen.py` emits a no-floating-point C header for the run-compressed state. An independently generated A=128 header compiled successfully with C99 warning-fatal flags, and all 129 finite cell outputs matched independent checksums.

A provisional x86 `-O3` microbenchmark over 30 million pseudo-random normalized cell queries found, on that one container:

- dense A=128 table: about 0.064–0.072 s;
- 47-run binary-search table: about 0.89–0.94 s;
- 3-parameter Yeoh expression including cell-to-stretch mapping: about 0.129–0.142 s.

This is **not** a portable performance claim. It establishes only a next engineering decision: dense lookup can trade a small memory budget for latency, whereas naive run compression saves memory but needs a better access strategy on latency-sensitive targets.

## 6. Hard scientific/engineering boundaries

The current result is a **one-dimensional monotone loading curve**, not a full material theory. It does not yet establish:

- a 3D objective strain-energy function;
- thermodynamic consistency;
- multiaxial prediction from one shared material state;
- unloading or cyclic response;
- Mullins effect;
- rate dependence or viscoelasticity;
- damage, plasticity, fracture, or temperature dependence.

Separate fits to different deformation modes would not by themselves solve this boundary.

## 7. Next gate: NIST elastomeric impact foam

The next preferred dataset is the NIST elastomeric impact-mitigating foam repository. It contains quasi-static, intermediate-rate, DMA and drop-tower data; the public `foam_db` example code fits a six-parameter `N=2` Hyperfoam model to a VN01 quasi-static stress/strain sample.

That dataset directly pressure-tests the E001 claims that are not visible in monotone Treloar loading:

- compression and return branches;
- finite loss / hysteresis history;
- rate-dependent state;
- impact mitigation;
- deployment state versus a richer classical constitutive fit.

The current execution environment has not successfully ingested the large VN01 HDF5/ZIP file. No NIST fit result exists yet and none may be inferred from plots.

## 8. Resume assets

Primary code/tests:

- `src/enterprise_math/material_fit.py`;
- `tests/test_material_fit.py`;
- `experiments/e001_treloar_material_benchmark.py`;
- `src/enterprise_math/material_runtime.py`;
- `src/enterprise_math/material_runtime_compressed.py`;
- `src/enterprise_math/material_runtime_codegen.py`;
- corresponding runtime/codegen tests;
- `experiments/e001_material_runtime_frontier.py`;
- `experiments/e001_emit_treloar_c_header.py`.

Provenance:

- `sources_e001_material.json`;
- `lineage_e001_material.json`;
- `docs/PRIOR_ART_E001_MATERIAL.*`.

Coordination:

- PR #70 checkpoint comment `5229980513`;
- runtime follow-up comment `5229993767`;
- Research Relay #82 comment `5229981383`.

Full repository CI is not claimed while the source PR remains Draft/concurrent and the current execution environment cannot obtain a local GitHub checkout.
