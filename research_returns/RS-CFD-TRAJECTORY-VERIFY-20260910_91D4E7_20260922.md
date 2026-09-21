# RS-CFD-TRAJECTORY-VERIFY-20260910 — successor 23-cycle native manifest freeze 91D4E7

Status: `CONTINUATION_REQUIRED`
Researcher: `EM-CFD-VFY-MANIFEST-91D4E7`
Claim: `CLM-CFDVFY-91D4E7-20260922-0158`

## Scope

This unit consumes immutable 4C2F19 and historical 6D3A91 without replay and freezes the next confirmatory native benchmark before observing any new native timing data. It does not alter 6D3A91 and does not run or accept unavailable spectralDNS/shenfun/MPI/FFTW evidence.

## Frozen successor design

`research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_91D4E7/cycle_block_manifest.json` fixes 23 complete six-order A/B/C cycles = 138 triplets = 414 arm executions. Every cycle contains `ABC,BCA,CAB,ACB,CBA,BAC` once, ordered by a predeclared SHA256 permutation. There is no adaptive reordering, replacement or optional stopping. Across the full design, each arm occupies each execution position 46 times and each directed pair precedence occurs 69 times. Raw triplet magnitudes, orders and timestamps are retained.

The historical physical/correctness contract is preserved: 32^3 Taylor-Green, spectralDNS `835b01b1e820b5c56559b9a028293e57526bfbf9`, shenfun 4.3, A=dense FFT, B=guarded hybrid, C=guarded forced fallback, same input identity, Nyquist/pressure-diffusion/Source/RK4 ordering, route constraints, endpoint/Hermitian/divergence/Source/energy/fallback diagnostics, and full setup/allocation/compilation/RK4 cost accounting. The charged horizon is now all 138 triplets.

## Exact block inference

A triplet is positive only when its contrast is strictly >0; zero/negative are non-successes. A cycle block is positive iff at least 4/6 triplet contrasts are positive. Ties are never deleted, replaced or resampled.

For the strictly conjunctive target `AB directional advantage AND CB directional advantage`, the primary analysis is an intersection-union test with each component at one-sided alpha .05 and both required to pass. With 23 independent cycle blocks, the exact minimal critical value is 16/23:

`P[Binomial(23,1/2)>=16] = 763/16384 ≈ 0.0465698`,

whereas the 15/23 tail is `440485/4194304 ≈ 0.105020`.

At planning `p_block=.8`, the exact marginal power is `11068512973881344/11920928955078125 ≈ 0.928494`; without assuming AB/CB dependence, the Frechet lower bound for both passing is `10216096992684563/11920928955078125 ≈ 0.856988`.

If AB and CB must instead be separately reportable simultaneous claims, the non-primary Bonferroni `.025` rule is 17/23 with exact tail `145499/8388608 ≈ 0.0173448`.

The AC negative-control veto is also block-calibrated: >=16/23 AC-positive cycles veto sparse-speed attribution pending explanation.

## Independence boundary

A fresh solver worker is required for every cycle; solver arrays, route state, sparse caches, RNG state and mutable application context cannot carry across cycles. Immutable binaries/JIT artifacts may be reused only symmetrically across A/B/C and logged.

This operational reset does **not** prove statistical independence. The manifest therefore records `REQUIRED_ASSUMPTION_NOT_CERTIFIED_BY_MANIFEST`. Exact binomial confirmation is permitted only if the native run supplies a defensible cross-cycle-independence justification under the null, or an alternative dependence law/calibration was separately predeclared. Otherwise block-sign p-values are `DESCRIPTIVE_ONLY` and confirmatory performance acceptance is fail-closed.

Within-cycle arbitrary dependence remains allowed under the previously derived sufficient null condition of central sign symmetry of the six-dimensional gate-difference vector.

## Machine verification

`research_checks/RS_CFD_TRAJECTORY_VERIFY_91D4E7.py` and `py_compile` passed. The checker verifies all 729 six-sign patterns, the deterministic 23-cycle SHA256 schedule, 138/414 run counts, exact 46/69 balance, the exact 16/23 and alternate 17/23 tails, exact `.8` power and Frechet bound, plus fail-closed synthetic cases for missing independence, insufficient AB wins, AC veto and all ties. It explicitly reports `cross_cycle_independence_certified=false` and `native_host_run=false`.

## Boundary and next action

This is an experimental-contract freeze only: no native spectralDNS/shenfun/MPI/FFTW run, no cross-cycle independence proof, no speedup/material-speedup/PDE/generic-industrial claim, and no Working Truth/Foundation/final acceptance.

Next, on a provisioned pinned native host, execute the immutable 23-cycle manifest exactly as frozen, preserving raw triplets, all physical diagnostics, route/support/guard/sparse/fallback traces, cycle-reset logs and fully charged 138-triplet costs. Before confirmatory interpretation, supply cross-cycle independence justification or the predeclared replacement calibration, then return the immutable checkpoint for independent verifier review.
