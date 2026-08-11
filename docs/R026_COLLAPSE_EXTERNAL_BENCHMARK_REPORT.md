# R026 Collapse External Benchmark Validation Report

Status: `COLLAPSE_EXTERNAL_CALIBRATION_COMPLETE / NOT CANONICAL`

Researcher-ID: `EM-R026-D19F1B`  
Task: `RS-R026-COLLAPSE-EXTERNAL-BENCHMARK-VALIDATION`  
Taskbook source: `752689001cd8ac541841a498486093385eeebdde`  
Execution: `REMOTE_SILENT research -> semantic checkpoint / CI_NOT_REQUIRED_FOR_RESEARCH`

## 1. Wind-tunnel verdict

The solved-problem benchmarks reject a universal collapse direction. `DOWN`/`UP` survive for one-sided bounds and enclosures; `NEAREST` for metric/MSE objectives; distance-weighted stochastic rounding for expectation-preserving objectives with variance/pathwise cost; `RESIDUAL_COLLAPSE` survives conditionally when the future factors through residual plus fixed context and residual precision is adequate; `ANCHOR_PLUS_RESIDUAL` is exact bookkeeping but shows no resource win without compression; `FIELD_COORDINATE` is useful only when the future genuinely factors through local coordinates; `BRC_SUPPORT` remains exact only for Boolean/result-support semantics; `FAR_PROJECTION` is an adversarial control.

No capability cell is `DOMINATES_REFERENCE_ON_DECLARED_RESOURCE_AXIS`. R026 therefore does **not** claim a new numerical algorithm that beats the solved reference methods. The Enterprise residue is a semantic/tooling layer: collapse typing, residual-sufficiency/factorization checking, anchor-necessity witnesses, and honest state/reconstruction accounting.

## 2. Execution coverage

- 245 deterministic machine rows across 9 benchmark families x all 10 collapse families, including precision sweeps and hostile subcases.
- 12/12 focused contract/kill tests PASS.
- Packaged split-source replay reproduces the pre-split raw JSON exactly: SHA-256 `a7b69a96d31316b6ff78f03b31577e2ef27ae1f7f04a49ad486ab2db53b4d00b`.
- Capability matrix SHA-256: `5544b9b2d88ddc55192182ecdb6083a85ffd5fa857688425914ee93690ed4505`.

## 3. Quantitative discriminator results

| Benchmark | Result | Meaning |
|---|---|---|
| GCD Fibonacci hostile | down depth `24`, up `23`, balanced/nearest `13` | balanced signed remainder can shorten descent, but all are Euclidean-domain prior art |
| Quantization `x=0.37` | DOWN bias `-0.0575`; UP/NEAREST `+0.005`; 50/50 `-0.026621933`; distance-weighted `-1.251221e-05` | 50/50 is not generally unbiased; distance weighting preserves expectation statistically |
| Summation `1000 x 0.01` | DOWN error `10`; NEAREST `5.625`; stochastic-unbiased `0.00170898438`; residual reconstruction `1.687539e-13` | error carry arrests accumulated drift, at extra state/work |
| Ill-conditioned refinement | exact-residual error `0`; quantized-residual error `0.00141662446` | residual state is only as useful as its precision |
| Multigrid Poisson `n=63` | residual correction rel-L2 `7.309253e-08`; state-only coarse overwrite `0.0427306612` | coarsening state is not equivalent to solving the residual equation |
| Convex projection | nearest objective gap `0`; far gap `1.28` | feasibility alone cannot substitute for the declared metric objective |
| Oscillator, 4000 steps | DOWN combined error `2.99806348`; NEAREST `0.331802127`; unbiased stochastic `0.263640293`; residual feedback `0.0172923356` | correction channel helps drift but is rooted and costs state/work; no universal monotone bit law |
| Elastic collision | stochastic mean coordinate bias/error `0.0038031006`; mean pathwise momentum+energy violation `0.133578491` | unbiased coordinates do not imply pathwise nonlinear conservation |
| Raster slope `13/29` | integer residual accumulator mismatch `0` vs nearest raster | exact residual/phase implementation, but Bresenham-family prior art |

## 4. Capability matrix

Legend: `EQ` known method; `PAR` Pareto alternative; `COORD` useful coordinate only; `EXACT0` exact/no resource gain; `APPROX` approximate; `1SIDE` one-sided useful bias; `FAIL` convergence/invariant failure; `TYPE` type mismatch.

| benchmark | C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|---|
| A_GCD | EQ | EQ | EQ | TYPE | TYPE | TYPE | EQ | EXACT0 | COORD | TYPE |
| B_QUANT | 1SIDE | 1SIDE | EQ | FAIL | APPROX | EQ | EQ | EXACT0 | COORD | TYPE |
| C_SUM | 1SIDE | 1SIDE | EQ | FAIL | APPROX | EQ | EQ | EXACT0 | COORD | TYPE |
| D_LINSYS | APPROX | APPROX | PAR | FAIL | APPROX | PAR | EQ | EXACT0 | COORD | TYPE |
| E_MULTIGRID | FAIL | TYPE | TYPE | TYPE | TYPE | TYPE | EQ | EXACT0 | COORD | TYPE |
| F_PROJ | 1SIDE | 1SIDE | EQ | FAIL | TYPE | TYPE | EQ | EXACT0 | COORD | EXACT0 |
| G_OSC | FAIL | FAIL | APPROX | FAIL | APPROX | PAR | EQ | EXACT0 | COORD | TYPE |
| H_COLLISION | FAIL | FAIL | APPROX | FAIL | APPROX | APPROX | FAIL | EXACT0 | EQ | TYPE |
| I_RASTER | 1SIDE | 1SIDE | EQ | FAIL | APPROX | APPROX | EQ | EXACT0 | EQ | EXACT0 |

C0..C9 respectively: DOWN, UP, NEAREST, FAR, UNIFORM_ENDPOINT_RANDOM, UNBIASED_DISTANCE_RANDOM, RESIDUAL_COLLAPSE, ANCHOR_PLUS_RESIDUAL, FIELD_COORDINATE, BRC_SUPPORT.

## 5. Residual-State Principle

Verdict: `SURVIVES_WITH_FACTORISATION_CONDITION`.

Residual is a sufficient primary iteration coordinate only when every permitted future transition/observable factors through `(residual, fixed solver/operator context)` and residual precision is adequate. Positive lanes: GCD, quantization error feedback, compensated summation, exact-residual iterative refinement, multigrid residual correction, projection displacement, raster error accumulation. Kill lanes: quantized residual in an ill-conditioned solve, nonlinear equal-residual/different-anchor futures, and collision conservation without anchor/mass context.

This is a cross-domain **sufficiency contract**, not a claim that the component algorithms are new.

## 6. Anchor Necessity Boundary

Verdict: `CONFIRMED_BY_MINIMAL_COUNTEREXAMPLE_AND_CONSERVATION_CASE`.

If `rho(x)=rho(y)` but a permitted future observable has `F(x) != F(y)`, residual-only collapse is incomplete. Minimal witness: residual `1/4`, anchors `0` and `10`, states `1/4` and `41/4`, future `F(x)=x^2`; futures are `1/16` and `1681/16`. Collision/projection supply domain-level variants.

The reusable Enterprise residue is a quotient-factorization guard/witness generator, not a new abstract theorem claim.

## 7. Prior-art boundary

The successful component patterns root broadly to Euclidean remainder descent, stochastic rounding, compensated summation, iterative refinement, multigrid residual correction, convex projection, classical oscillator diagnostics/structure-preserving integration, center-of-mass/relative collision coordinates, and Bresenham-style integer error accumulation. See `docs/R026_PRIOR_ART_ROOTING.md`.

Therefore the specialization that remains is a **Collapse Contract Compiler**:

`(full state, proposed collapse map, declared future language/observable, precision schedule)`

-> `{EXACT_QUOTIENT, RESIDUAL_SUFFICIENT, ANCHOR_REQUIRED, SUPPORT_ONLY, APPROXIMATE, INVALID}`

plus state/work/reconstruction accounting and hostile witness generation.

## 8. Driver decision

Continue investment: conditional `RESIDUAL_COLLAPSE` as sufficiency/factorization tooling; selective `FIELD_COORDINATE`; Anchor Necessity as a semantic guard.

Keep specialized only: DOWN/UP for certified lower/upper goals; NEAREST as standard metric baseline; distance-weighted stochastic for expectation objectives; ANCHOR_PLUS_RESIDUAL as exact fallback; BRC_SUPPORT for exact Boolean/result support.

Deprioritize/retire as general principles: FAR except hostile controls; uniform 50/50 as generic “unbiased” collapse; unconditional residual-only state; universal DOWN or universal UP.

## 9. Artifacts and gates

The exact researched runner is published through `experiments/r026_collapse_external_benchmarks.py` plus deterministic gzip+base64 text chunks under `experiments/r026_payload/`. The loader reconstructs the frozen source bytes automatically; 12/12 tests and output hashes match the pre-packaging implementation.

Full 245-row machine outputs use the same connector-safe transport: deterministic `.json.gz` / `.csv.gz` bytes are split as ordered base64 text parts and mechanically reconstructed by `experiments/data/r026/reconstruct_frozen_results.py`. See `experiments/data/r026/README.md`.

Other frozen artifacts: `R026_CAPABILITY_MATRIX.json`, `R026_GROUND_TRUTH_CONTRACTS.json`, `R026_COUNTEREXAMPLES.json`, human ground-truth/hostile/law/prior-art docs, and focused tests.

Shared-surface delta: `N/A`. This is a Draft owner research calibration artifact; no canonical theorem/tool promotion is performed here.

## 10. Return class

`COLLAPSE_EXTERNAL_CALIBRATION_COMPLETE / RESIDUAL_STATE_REGIME_CLASSIFIED / POLICY_SPECIALIZATIONS_FROZEN / PRIOR_ART_ROOTED / NEW_TOOL_RESIDUE_ISOLATED / NOT_CANONICAL`

Secondary characterization:

`ROOTING_SUCCESS / MOST_COLLAPSE_MODES_MAP_TO_KNOWN_NUMERICAL_OR_ENGINEERING_PATTERNS / LIMITED_ENTERPRISE_RESIDUE / NOT_CANONICAL`

Not returned: `RESOURCE_ADVANTAGE_DEMONSTRATED`.
