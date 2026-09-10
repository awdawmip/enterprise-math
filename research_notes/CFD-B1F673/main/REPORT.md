# CFD main task: full trajectories and pressure-safe sparse interface

Progress-Event-ID: `CFD-B1F673-FULL-TRAJECTORY-01`
Researcher-ID: `EM-CFD-B1F673`
Research-Activity-ID: `RA-CFD-B1F673-20260910`
Task: `RS-CFD-SPECTRAL-HYBRID-20260910`
Publication: `TP2-C3B717C14153D5AC45BF`
Claim: `CFD-B1F673-20260910-MAIN`, actual raw-JSON Issue240 comment `5616124261`.
Status: **BOUNDED AUTHOR IMPLEMENTATION CHECKPOINT; NOT INDEPENDENT REVIEW, INDUSTRIAL SPEEDUP, OR PDE CERTIFICATE.**

## Authority and preserved frontier

All eight CFD taskbooks and immutable V2 publications reached main in PR1469, merge `668c3412ac81576df424e0bbfd520a7131851bf6`. Other tasks were published unclaimed, not launched as background workers. Main execution uses `research/cfd-b1f673-main-20260910` and the exact taskbook blob `a678a1769cf04df52520fe21b4404c0e59267689`.

The canonical runtime guard actually authorized this claim with the existing fault-isolation bootstrap against main `2f2dcd390f6c2c50610f043f56b6bd7fa6c53ba4`, 786 actual server comments, at `2026-09-10T09:13:06.539860+00:00`. Two failed control attempts are preserved: the first omitted canonical fault isolation; the second encountered no parsed claim because the earlier fenced-JSON comment was not a raw JSON event. No foreign task head was selected and no guard was weakened.

Original 3D probe is reused unchanged at `../prior_3d/probe.py`, SHA256 `1d10429616026f13643f0ba1641acd8c23f3aecd1dc7c03b429f5e0c4381eb09`. The distinct CFD9R2K7 2D negative trajectory result is context, not our 3D code or proof. Existing completed single-RHS tests were not replayed as a new research result.

## Implementation

`hybrid.py` adds unprojected rotational pair aggregation, a support-aware sparse/FFT choice with sticky dense fallback, matched projection and viscosity, and a no-pruning RK4 integrator. The sparse kernel includes all newly generated retained output frequencies. Exact `!=0` support chooses the method; the 1e-12 support diagnostic never deletes coefficients. Once dense, remaining stages use FFT without repeated scans. This does not assert that support can never shrink.

All runs use classical periodic incompressible velocity equations on a 2pi cube, double precision, n>3K with K=n//3-1, and an identical finite retained cube. This is an external effective model; it neither derives nor changes native P000 semantics.

## Applied BRC observer boundary: velocity alone is insufficient

The public spectralDNS NS source, blob `6a11909d1e2c1d529d382952c4c9d77e7073645c`, computes a pressure readout from the unprojected nonlinear term before subtracting its gradient. For each nonzero k, define g_k=F[u x curl u]_k and pi_k=(k dot g_k)/|k|^2. Then g_k=P_k g_k+k pi_k. Keeping P_k g_k alone discards pi_k; adding k*c leaves the velocity projection unchanged while changing the pressure input by c.

Actual applied interface: branch pair (p,q), output k=p+q, complex vector amplitude, and the joint observer (P_k g_k, pi_k). Alternative contributions add as complex vectors at the same output; serial RK4 and the host pressure stage remain allowed future operations. Grouping (p,q) and (q,p) preserves g itself. No absolute-value/positive-mass replacement is used. This is `EXTEND_EXISTING_TOOL` for the existing finite kernel and `COMPOSE_APPLIED` for observer-safe grouping, not a new top-level BRC family or novelty claim.

A regression witness u=(sin y,0,0) has projected nonlinear velocity RHS exactly zero, but maximum host pressure proxy 0.125. Feeding the already-projected RHS to the host changes that proxy to zero. This proxy is the rotational-form pressure input/modified-pressure convention, NOT a claim that the physical static pressure of this shear flow is nonconstant. The adapter returns unprojected g and leaves pressure recovery to the host.

The serial adapter explicitly requires its Fourier coefficient scale, wavevector layout, communicator size, domain and cutoff. Unsupported configurations fail instead of silently changing the problem. Contract tests cover forward-normalized and backward-normalized coefficient arrays and sparse/dense callback paths. The original spectralDNS/shenfun/MPI distribution was NOT executed; a synthetic matching callback was used. This is not a claim of production integration or host performance.

## Frozen full-trajectory results

Eight cases, five interleaved runs per method, ten RK4 steps with dt=0.001 and viscosity=0.01. Both methods include engine setup, input validation, allocation, support detection, kernels, projection, diffusion, RK4 algebra and finite checks. Shared initial input generation, first JIT/cache warmup and report-only diagnostics are excluded. Raw timings are retained in results JSON.

| n | input | initial full modes | FFT median ms | hybrid median ms | FFT/hybrid |
|---:|---|---:|---:|---:|---:|
| 32 | shear | 2 | 175.489 | 49.049 | 3.578 |
| 32 | random | 32 | 185.849 | 176.743 | 1.052 |
| 32 | random | 128 | 182.558 | 174.267 | 1.048 |
| 32 | random | 512 | 181.889 | 180.702 | 1.007 |
| 32 | random | 4096 | 180.252 | 181.630 | 0.992 |
| 64 | shear | 2 | 1509.674 | 406.702 | 3.712 |
| 64 | random | 128 | 1480.475 | 1460.831 | 1.013 |
| 64 | random | 8192 | 1611.827 | 1512.231 | 1.066 |

Maximum relative trajectory difference across these cases is 6.250e-17. Solenoidality, Hermitian zero-plane symmetry, viscous energy decay and the analytic shear decay checks passed their declared tolerances. Time refinement on the same finite spatial operator gave successive error ratios 16.35 and 16.23; this is not a continuous-PDE convergence certificate.

Persistent shear uses 40 sparse evaluations and shows roughly 3.6-3.7x complete prototype speedup. This is a special zero-nonlinear-velocity flow with an analytic solution, not evidence for general turbulence acceleration. Random 32-mode data grows 32 -> 231 -> 4537 exact stage modes; random 128-mode data switches after one sparse evaluation. Random/dense ratios near one are not a statistically established optimization. In particular the n=64 dense case uses the SAME FFT kernel on all 40 stages, so its apparent 1.066 ratio is timing variability, not algebraic acceleration.

The first contract test failed on a NumPy axis-indexing error and was repaired before benchmark execution. A local execution timeout interrupted the 64-cubed batch after two complete cases; those printed raw rows were recovered without rerun. The pre-checkpoint driver is preserved, and only per-case checkpoint/resume plumbing changed. See `implementation_corrections.md`.

## Scope and next unit

The no-pruning prototype, pressure-safe restricted interface and frozen finite-trajectory author tests are delivered. `propose_pruning` produces a conjugacy-aware proposal and an explicit UNVERIFIED status; no proposal is used by the integrator, and it provides no rounding, tail, timestep or trajectory error certificate.

The smallest remaining engineering unit is to run the restricted adapter inside an actual pinned serial spectralDNS/shenfun installation and compare host velocity AND pressure outputs, including all integration cost. Independent review is separately published as RS-CFD-TRAJECTORY-VERIFY-20260910. Approximate sparsification requires the separately published rounding/cancellation work. Do not repeat the completed eight-case baseline merely to claim a new result. Do not generalize the special shear speedup or promote author tests to independent acceptance.

## Reproduction

From this directory, with numpy/scipy/numba installed:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiment.py --suite contracts
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiment.py --suite 32
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python experiment.py --suite 64
```

The scripts save each completed case. The historical `--resume` option reads completed case JSON lines from stdout_64.jsonl; those rows are retained verbatim in results_64.json for this checkpoint. A new verification run should normally omit --resume and retain its own raw results.
