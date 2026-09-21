# CFD continuation R6: pinned-RK4 state-support induction and guard-cost reduction candidate

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-TASK-AUTO-B6F841`  
Claim: `CLM-CFD-B6F841-20260921-1646-R6`  
Activity: `RA-20260921-AUTO-B6F841`  
State: `CONTINUATION_REQUIRED / PINNED_RK4_GUARD_ELISION_CANDIDATE_DERIVED / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Frontier consumed

This run consumed the exact R5 continuation at `006f41e636d6980765709cb0cb4cdea1cc758ad6:research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_9CFD0F_20260921_R5.md`. R5 had already implemented the conservative correctness guard: before every certified sparse nonlinear call it scans both current RK stage state and current host `Source` for exact nonzero coefficients outside the certified carrier; any escape permanently routes dense before the sparse call.

The present run did not repeat the R5 finite-Galerkin trajectory result. It targets the next measurable bottleneck visible in R5: exact full-array guard scans can consume a material fraction of the sparse-path runtime.

BRC resolution: `COMPOSE_APPLIED / REUSE_EXECUTED`. The exact Boolean support carrier remains a route certificate only. Complex amplitudes, phases, conjugacy, pair multiplicity, pressure/diffusion and RK state remain unquotiented.

## Exact source pin recovered

The task-pinned `spectralDNS/solvers/NS.py` blob `6a11909d1e2c1d529d382952c4c9d77e7073645c` is exactly present at upstream commit `6f6335b7ee3ed8a7e49211c82ddf4bacbe4c220a`. At the same commit, `spectralDNS/maths/integrators.py` has blob `a08b242047a6d5d672f884925e9aa353fbc5ed44`.

The pinned `ComputeRHS` order is:

1. nonlinear convection callback;
2. optional Nyquist mask;
3. pressure projection plus diffusion;
4. `rhs += Source`.

The same pinned commit's RK4 is exactly four RHS evaluations. It initializes `u2[:] = u1[:] = u0`; after each of the first three RHS evaluations it sets `u0[:] = u1 + b[rk]*dt*rhs`; every stage accumulates `u2 += a[rk]*dt*rhs`; and finally sets `u0[:] = u2`. The fixed coefficients are `a=(1/6,1/3,1/3,1/6)` and `b=(1/2,1/2,1)`.

## New result: state support is an inductive invariant under the exact pinned RK4 contract

Let `C` be the exact certified retained carrier. Assume at the start of an RK4 step that `support(u0) subseteq C`. Assume the sparse nonlinear evaluator returns the complete retained nonlinear output on `C`; Nyquist masking only deletes coefficients; pressure projection and diffusion are modewise; and at each relevant RHS evaluation `support(Source) subseteq C`.

Then `support(ComputeRHS(u)) subseteq C` whenever `support(u) subseteq C`. The pinned RK4 stage assignments are only scalar linear combinations of the step-entry state and an RHS whose support is in `C`. Therefore every intermediate RK4 stage and the final step state remain in `C`. Induction over time steps preserves state support while those assumptions remain true.

Consequently, **inside the exact pinned RK4 execution contract**, an exact full-array *state* escape scan before every nonlinear call is logically redundant after initial state certification. A narrower candidate guard may scan `Source` before each stage while deriving stage-state support from the RK4 invariant. This removes one full rFFT-array exact scan per sparse stage without weakening the support theorem under that contract.

This is not a universal adapter rule. If external application code can mutate the stage state outside the pinned RK4/ComputeRHS path, the derivation no longer applies and the conservative R5 state-plus-Source guard remains required.

A stronger tier—scan `Source` only once per four-stage RK4 step—is valid only if the host additionally attests that `Source` cannot mutate during the step and the adapter has an exact step-boundary signal. It is not enabled by this run.

## Executed finite checks and negative controls

`native_host_preflight.py` was compiled successfully and executed with deterministic seed `20260921`. `preflight_results.json` records four passing local checks.

- 64 randomized support-preserving cases, each 8 synthetic RK4 steps, retained exact zero outside the carrier (`max_outside_abs = 0.0`). This is a finite regression witness for the algebra, not the proof itself.
- External-state mutation negative control: state-plus-Source scanning detects the injected outside-carrier coefficient; Source-only scanning does not. This confirms the required host-state-mutation attestation is substantive.
- Mid-step Source mutation negative control: a step-entry-only Source scan misses a later injected outside-carrier Source mode, while a per-stage Source scan detects it. This confirms that once-per-step scanning requires the stronger Source immutability contract.
- Current environment probe still fails the original-host readiness condition.

The local NumPy microbenchmark used an `n=64` last-axis rFFT-shaped field with 405,504 complex coefficients per state and 80 repetitions. Median exact complement-scan costs were:

- state + Source before one stage: `5.917124 ms`;
- Source only before one stage: `2.895589 ms`;
- measured saving: `3.021535 ms/stage`, ratio `2.0435x` for scan code only;
- four-stage group, state + Source every stage: `23.696433 ms`;
- Source every stage: `11.628978 ms`;
- Source once per step: `2.886115 ms` (stronger, not-enabled contract), giving `8.2105x` relative to conservative four-stage scan code.

These are local NumPy scan timings only. They are **not** spectralDNS trajectory timings or a native-host speedup claim.

Artifact SHA-256 values from the local validated files:

- `native_host_preflight.py`: `325c21730e7796c9c62d957df2715936d099141752387b224c340685a6ef7c7c`;
- `preflight_results.json`: `5e9b441fc6d92579132e954ac8ca90d1e854c65c7e28b9b0379cd4aa3c8a8898`;
- `host_probe.json`: `48411b2d056fd0c0521af4b05550993e9805fc4a3c303918ca07fe694338d3e4`.

## Original-host capability result

The current execution environment is Python 3.13.5 with NumPy/SciPy/Numba available. `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft` and `pyfftw` remain unavailable; `mpiexec`, `mpirun`, `fftw-wisdom` and `fftw-wisdom-to-conf` are absent. System `libfftw3.so.3` and `libfftw3_threads.so.3` exist, while `fftw3_mpi` is not found. Package-index attempts did not produce an install: the spectralDNS lookup hit DNS/name-resolution failure and the shenfun lookup timed out. No substitute environment is represented as the original host.

Therefore the candidate guard reduction is deliberately recorded as `NOT_ACTIVATED_NATIVE_HOST_PENDING`.

## Status and smallest unresolved unit

This run completed a new bounded research unit: the task-pinned NS blob was tied to its exact upstream commit, the same-commit RK4 source was audited, a state-support induction was derived, guard-elision preflight code and negative controls were executed, and the local scan-cost opportunity was quantified.

The parent task remains **CONTINUATION_REQUIRED**. The smallest unresolved unit is now:

1. instantiate the pinned serial spectralDNS/shenfun/FFTW host on an authorized environment;
2. run the existing conservative R5 state-plus-Source guard and the R6 **Source-each-stage candidate** on identical nonlinear-active held-out trajectories with unchanged dense callback, Nyquist policy, pressure/diffusion and RK4;
3. verify dense-vs-hybrid velocity/pressure equivalence, support/fallback events and all previously required diagnostics;
4. retain raw guard and total trajectory timings under the same reuse horizon;
5. keep the conservative guard if any host-state-mutation attestation is unavailable or if total-cost evidence loses;
6. only evaluate Source-once-per-step after an explicit no-midstep-Source-mutation contract and exact step-boundary hook are established;
7. submit the original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.

No universal speedup, industrial acceleration, continuous-PDE theorem, native-P000 fluid theorem, canonical promotion or mathematical acceptance is asserted.
