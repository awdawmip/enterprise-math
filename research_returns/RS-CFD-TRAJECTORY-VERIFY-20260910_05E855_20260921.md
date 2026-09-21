# RS-CFD-TRAJECTORY-VERIFY-20260910 — trajectory diagnostic continuation

Researcher: `EM-CFD-VFY-05E855`  
Claim: `CLM-CFDVFY-05E855-20260921-1340`  
Status: `CONTINUATION_REQUIRED`

## Result

This continuation advances two missing verifier obligations without pretending that the unavailable native spectralDNS/shenfun/FFTW host was rerun.

The pinned host stores velocity Fourier data as `U_hat.shape == (3,n,n,n//2+1)` for even `n`. In this r2c layout, the only stored `kz` planes whose negative-`kz` partner is also stored are `kz=0` and `kz=n/2`. A correct in-storage Hermitian certificate must therefore check

`U(-kx,-ky,kz) = conj(U(kx,ky,kz))`

on **both** boundary planes. Interior `0<kz<n/2` modes do not have their negative-`kz` partner stored; inventing a same-array interior pair test is incorrect. The previous native harness only exposed an initial zero-plane check, so the verifier-owned contract now makes the full stored-plane requirement explicit at the initial state, every completed RK step, and the final state.

For kinetic energy, the verifier contract records the host real velocity after `s.get_velocity(**c)` and computes `E = 0.5 * mean(sum_i U_i^2)`. This avoids silently assuming a shenfun Fourier normalization. Zero-Source trajectories may additionally be checked for numerically nonincreasing energy under a declared tolerance. Static or dynamic Source cases are **not** generically monotonic-gated because forcing may inject energy; their energy series is recorded instead.

Timestep refinement is also frozen more narrowly: compare identical initial/source data at the same final time for `dt=0.002` and `dt=0.001`, recording endpoint velocity and modified-pressure differences. With only two levels, no convergence order is claimed.

## Validation

A standalone NumPy checker was added and executed locally against deterministic seed `20260921`. Seven checks passed:

- real-field r2c boundary Hermitian symmetry;
- physical-vs-rfftn Parseval energy identity under NumPy's declared convention;
- injected `kz=0` violation detection;
- injected Nyquist-plane violation detection;
- no false stored-pair test on interior `kz`;
- zero-Source decay gate behavior;
- forced-energy series is recorded without an invalid monotonicity gate.

The synthetic reference energy matched exactly (`1.4793232958405569` physical and spectral under NumPy's convention). Injected boundary-plane residuals were approximately `1e-6` and were detected.

## Durable outputs

- `research_checks/RS_CFD_TRAJECTORY_DIAGNOSTICS_05E855.py`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_05E855/diagnostic_contract.json`

## Remaining native verification unit

On the exact pinned serial spectralDNS/shenfun/FFTW host, integrate these diagnostics into the verifier-owned trajectory matrix; run zero/static/dynamic Source cases; run same-final-time `dt=0.002` versus `dt=0.001` on one sparse-preserving and one densifying case; retain dense-vs-hybrid velocity/modified-pressure comparisons, per-step Hermitian/energy diagnostics, fallback state, and complete timing evidence.

This return grants no continuous-PDE certificate, universal speedup claim, or independent numerical acceptance of the native host results.
