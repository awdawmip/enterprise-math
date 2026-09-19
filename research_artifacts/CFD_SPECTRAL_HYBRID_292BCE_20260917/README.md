# CFD static-carrier integration checkpoint — EM-DIRECT-292BCE

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Claim: `CLM-CFD-292BCE-20260917T1407Z`  
Status: `LOCAL_INTEGRATION_AND_FINITE_SURROGATE_PASS / ORIGINAL_HOST_NOT_RUN / CONTINUATION_REQUIRED`

## What this checkpoint adds

This checkpoint integrates the exact least retained additive-support carrier detector into a spectralDNS-compatible serial Vortex callback prototype. The route is decided once in `validate_initial` before time integration. A certified carrier is gathered by fixed rFFT label maps and passed with all complex coefficients to the pre-existing unprojected rotational pair kernel. If the carrier construction proves more than the configured support limit, every trajectory call goes immediately to the unchanged dense callback. No amplitude thresholding or pruning is used.

The adapter preserves the host pressure/diffusion ordering: it returns the unprojected rotational quantity, leaving pressure and viscosity downstream. The separate `propose_pruning` interface is explicitly marked unverified and is never called by the checked trajectory route.

## BRC / information discipline

BRC reuse is restricted to the routing layer. The carrier is exact Boolean signed-wavevector support; branch identity is the integer wavevector label. Complex vector amplitudes, phase, conjugacy and pair multiplicity are not compressed to positive mass. Future operations covered by the carrier argument are retained convolution, diagonal pressure/viscosity multipliers and RK linear combinations. Resolution: `REUSE_APPLIED`.

## Local validation actually executed

The local environment does not contain `spectralDNS`, `shenfun` or `mpi4py`; no GitHub-hosted computation was used. Therefore this run did **not** execute the original pinned spectralDNS/shenfun/FFTW host. Instead, it ran an independent serial finite 3/2-padded Fourier-Galerkin surrogate with the native host cutoff convention `K=n/2-1`, `n=16`, dealiased physical grid `24^3`, complex128, viscosity `0.01`, `dt=0.002`, 12 RK4 steps, seven interleaved timing repeats, and full signed sparse limit 384.

The spectralDNS-compatible callback itself was separately exercised with a fake host context implementing the same call/normalization/wavevector interface: a 15-label certified line matched the independent 3/2-padded unprojected reference to relative max error `6.26e-16`, and a random-48 case proved lower bound 385 and routed to the unchanged dense callback with exact zero difference.

Held-out trajectory results (all new seeds/families relative to the preceding detector checkpoint):

| case | decision | carrier / lower bound | FFT median total | static median total | FFT/static ratio | final max abs diff |
|---|---|---:|---:|---:|---:|---:|
| oblique line | certified | 15 | 0.060612 s | 0.004644 s | 13.052 | 9.73e-21 |
| even-axis line | certified | 7 | 0.060068 s | 0.004193 s | 14.327 | 2.63e-21 |
| xy-plane generators | certified | 225 | 0.065966 s | 0.062525 s | 1.055 | 1.52e-20 |
| random 48, seed 926211 | dense fallback | >384 | 0.064775 s | 0.067383 s | 0.961 | 0 |
| random 96, seed 926212 | dense fallback | >384 | 0.059857 s | 0.060250 s | 0.993 | 0 |

The line cases show that fixed-carrier gathering removes repeated support scans and can be dramatically cheaper in this local finite surrogate. The 225-label plane is close to break-even once the one-time detector cost is charged. Random inputs are rejected before trajectory sparsity assumptions are made; the remaining cost is the detector overhead plus the unchanged dense path. These ratios are **not** spectralDNS host speedups and must not be combined with the earlier native-host timing matrix.

For the 225-label plane, the median static breakdown was approximately: detector `18.23 ms`, fixed gather over all 48 RK RHS calls `0.59 ms`, sparse-output allocation `0.13 ms`, pair-kernel nonlinear work `14.06 ms`, projection/diffusion `3.04 ms`; median total including setup and trajectory was `62.52 ms`. For random-48 fallback, detector median was about `0.58 ms`; all 48 nonlinear calls used the dense evaluator.

## Reproduction

Run:

`python research_checks/CFD_SPECTRAL_HYBRID_292BCE_20260917.py`

Files:
- `static_carrier_native_adapter.py` — integrated serial callback prototype.
- `summary.json` — compact held-out results and interface tests.
- `raw_trials.csv` — all interleaved trial timings.
- `verification.txt` — run status and SHA-256 pins.

## Exact remaining unit

Run this integrated adapter, unchanged in logic, inside the already pinned actual spectralDNS/shenfun/FFTW host environment on the same five held-out cases (or an equivalently new frozen held-out set), retaining the original dense callback and native pressure/diffusion/RK4. Record detector/setup/allocation ownership, nonlinear evaluation and total elapsed host cost. Only same-run matched host data may support a host-level speed claim. Independent `RS-CFD-TRAJECTORY-VERIFY-20260910` review remains separate and must not be self-accepted here.
