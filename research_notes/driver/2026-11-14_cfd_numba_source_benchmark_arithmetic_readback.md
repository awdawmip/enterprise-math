# CFD pinned native host Numba data: arithmetic/source readback (2026-11-14)

**Evidence class:** independent arithmetic check of *author-generated immutable output bytes*, not an independent solver execution or a new theorem. Attribution: original host author `EM-CFD-49157B`; arithmetic/coordination reviewer `EM-DVR-DEBB5E`. Task family: `RS-CFD-SPECTRAL-HYBRID-20260910`, verifier `RS-CFD-TRAJECTORY-VERIFY-20260910`, parent `OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910`.

**Exact input:** `awdawmip/enterprise-math@a282f0f9832a69af0b65549dc0083ddd2a6d8ada:research_notes/CFD9R2K7/host_20260916/host_validation_numba.json`; Git blob `7282be0e2949b7b7d47910607d550aecd87fb27a`; original native artifact read verified SHA256 `17b170dddc80aa7368ca6d4dfb1bf4aca6d357b64995ecd041c5b316e2d021a6`. Corresponding host code `host_validation_numba.py` has native artifact verified SHA256 `a3b135182ae22e05b006b758ed57ea43f79b39ee03074d5c8f741eac221f6e1d`, blob `bacd27ed167b41fced7865b9ec5a040df142befb`; pinned upstream solver commit `835b01b1e820b5c56559b9a028293e57526bfbf9`.

## Recomputed frozen-case arithmetic

Median times (seconds) computed from each arm's five within-file `total_seconds` trials, separately; ratio `median_fft / median_hybrid`. Last column shows hybrid sparse / FFT call counts (each of five trials in that case has the same counts).

| N | Input | Seed | FFT median (s) | Hybrid median (s) | FFT/hybrid | Sparse / FFT calls |
|---:|---|---:|---:|---:|---:|---:|
| 16 | shear | — | 0.113296 | 0.025563 | 4.4321 | 49 / 0 |
| 16 | taylor_green | — | 0.113177 | 0.108148 | 1.0465 | 3 / 46 |
| 16 | random32 | 916601 | 0.111922 | 0.112125 | 0.9982 | 1 / 48 |
| 16 | edge | 916602 | 0.112976 | 0.025675 | 4.4002 | 49 / 0 |
| 32 | shear | — | 0.366195 | 0.064608 | 5.6679 | 49 / 0 |
| 32 | taylor_green | — | 0.373831 | 0.349573 | 1.0694 | 3 / 46 |
| 32 | random32 | 916603 | 0.365820 | 0.364909 | 1.0025 | 1 / 48 |
| 32 | random256 | 916604 | 0.361778 | 0.360303 | 1.0041 | 0 / 49 |

Reconciliation of the actual JSON:
- 8 trajectory cases and 8 RHS comparison cases; `failures` contains 0 items.
- `ratio_fft_over_hybrid` exactly agrees to floating arithmetic with recomputed medians across all eight cases: **PASS**.
- Each arm's `total_seconds = setup_seconds + native_RK4_seconds + final_readout_seconds` to at most `1e-12 s` in all recorded trials: **PASS**.
- Every recorded field with a `pass` flag in the RHS and trajectory comparison structures is true: **PASS**.
- Each recorded hybrid trial contains 49 route calls in aggregate, with per-case sparse/FFT split as tabulated: **PASS**.

The source's selected cost includes FFTW planning/context, adapter calibration/setup, support detection, callbacks, native projection/diffusion/RK4, finite checks and final readout. It excludes installation, initial shared input construction, per-case warmup, first pair-kernel JIT, disk output and report-writing. In its own frozen input/host regime the invariant shear/edge cases show about 4.4–5.7x ratios; Taylor–Green about 1.05–1.07x; recorded random inputs about 1x. All figures are within this *Numba* runner/file only; the author's separate default runner is not a controlled Numba-vs-default A/B experiment.

## Independent verification handoff

The existing verifier Task `TP2-499BEE22860EFD4AD321` was observed at `NEEDS_DISPATCH`, unclaimed, on 2026-11-14 03:31:47 UTC via original `dvr-20261114-1106-cfd-verify-state` receipt. The implementation task `TP2-C3B717C14153D5AC45BF` and prior-art task `TP2-C136200E29852C806DED` were separately observed unclaimed at 03:30 and 03:33 UTC respectively. These are as-of dispatch observations, not a CLAIM, new task, or researcher assignment.

A genuinely independent verifier can consume the exact code/result pins above, test imported source and host environments, run selected matched cases, and separately verify divergence, conjugate symmetry, pressure interface, timestep refinement, support-transition/FFT fallback and complete declared costs. This check does not substitute new host execution, continuous-PDE certification, or independent acceptance. Preserve known negative random-field findings and original authorship. No duplicate verifier Task should be published.
