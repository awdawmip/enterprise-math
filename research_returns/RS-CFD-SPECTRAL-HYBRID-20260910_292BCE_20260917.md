# Research return — static-carrier adapter integration and held-out local trajectory check

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-292BCE`  
Claim: `CLM-CFD-292BCE-20260917T1407Z`  
State: `CONTINUATION_REQUIRED / ORIGINAL_HOST_EXECUTION_BLOCKED_LOCALLY`

## Completed in this claim

1. Reused the exact finite least-additive-carrier detector from the preceding frontier and wired it into the pinned native serial Vortex callback interface as a one-time pre-trajectory route.
2. Preserved the unchanged dense callback, unprojected rotational quantity, full complex coefficients, conjugate labels, downstream pressure/diffusion, and no-pruning behavior. The optional pruning interface is exposed separately and remains explicitly unverified/unused.
3. Added fixed-carrier rFFT gathering so certified trajectories no longer need repeated full support scans; the gather includes every carrier label, including currently zero coefficients, so newly generated retained outputs are not silently discarded.
4. Executed deterministic local validation with native cutoff `K=n/2-1` and an independent 3/2-padded finite-Galerkin reference. Five new held-out cases were run for 12 RK4 steps with seven interleaved timing repeats.
5. Exercised the spectralDNS-compatible callback signature against a fake serial host context to verify both the certified sparse route and exact early dense fallback.

## Validation result

All single-RHS and full-trajectory comparisons passed the declared finite floating tolerances. Certified carrier sizes were 15 (oblique line), 7 (even-axis line), and 225 (xy-plane generated support). Random 48 and random 96 inputs both proved carrier lower bound 385 and routed to dense fallback before the trajectory.

Local surrogate median FFT/static total ratios were 13.052, 14.327, 1.055, 0.961, and 0.993 respectively. These are local finite-surrogate results only. They are not spectralDNS host speedups and are not a continuous-PDE, industrial, or universal performance claim.

BRC resolution is `REUSE_APPLIED`: exact Boolean signed-wavevector support is used only as a cost-routing carrier. Complex amplitudes, phase and multiplicity remain in the nonlinear evaluator; no positive-mass reduction is used.

## Capability boundary and blocker

The execution environment used for this claim has NumPy/SciPy/Numba but not `spectralDNS`, `shenfun`, or `mpi4py`. No hosted computation was started. Therefore the original pinned spectralDNS/shenfun/FFTW host was **not** executed in this claim. This prevents promoting the local timing evidence to the task's host-cost checkpoint.

## Durable outputs

- `research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/static_carrier_native_adapter.py`
- `research_checks/CFD_SPECTRAL_HYBRID_292BCE_20260917.py`
- `research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/summary.json`
- `research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/raw_trials.csv`
- `research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/verification.txt`
- `research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/README.md`

## Smallest next action

Execute the integrated adapter in the exact pinned actual spectralDNS/shenfun/FFTW serial host on the new held-out matrix, with the original dense callback and pressure/diffusion/RK4 unchanged. Record same-run detection, setup/allocation ownership, nonlinear and total cost, then submit the resulting host checkpoint for independent `RS-CFD-TRAJECTORY-VERIFY-20260910` review. Do not mark final acceptance from this researcher return.
