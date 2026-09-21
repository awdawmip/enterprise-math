# CFD continuation R16: native-host gate recheck and route-saturation cost ceiling

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-BCC918`  
Claim: `CLM-CFD-6F3A9C-20260921-R16`  
Activity: `RA-S0011-6F3A9C-20260921`  
State: `CONTINUATION_REQUIRED / NATIVE HOST UNAVAILABLE / NEW ANALYTICAL COST-OBSTRUCTION CHECKPOINT / NO NATIVE SPEEDUP CLAIM`

## Canonical control entry consumed

The exact startup packet `EMREQ-AUTO-20260921T172303Z-S0011-6F3A9C` returned `CLAIM_NEW_OWNER` for this task with `HANDOFF_READY + NEEDS_DISPATCH`, publication `TP2-C3B717C14153D5AC45BF`, and the native-host next action. The activity record was registered before research. The task-level claim was then published to Issue 240 as comment `5764791191`; its server readback is unedited, authored by the authorized repository owner, and the bounded post-packet comment window contains no competing control event before that claim.

The first dependency was read at its declared immutable ref, `aa054a7ac72a3f78ab7f590291017cbd453ed29f:research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_A11R10_20260921_R10.md`, rather than replaying the old work. R10 supplied the frozen held-out route counts used below: `(2 sparse, 18 fallback)`, `(2,18)`, `(1,19)` over 20 nonlinear calls, with exact support saturating the 729-mode retained cube by the end of the first RK4 step.

## Native-host gate recheck

A fresh fail-closed probe was run in the current execution environment. The required Python modules `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, and `pyfftw` are all absent. `mpicc`, `mpicxx`, `mpi.h`, and `fftw3.h` are absent; `libfftw3.so.3` is visible, but no MPI library is resolved. Therefore `native_ready=false`.

No install attempt was made and no surrogate was relabelled as native. This run does **not** claim that the pinned spectralDNS/shenfun/MPI/FFTW host was instantiated, that the original spectralDNS RK4 trajectory ran, or that any native speedup was observed.

## New bounded result: route-saturation speedup envelope

The R10 support-growth observation can be turned into a simple cost obstruction that is useful for the still-required native A/B/C run.

For one matched trajectory, let the dense-reference nonlinear costs be `D_i`. Let `E` be the nonlinear calls on which sparse routing is permitted and `F` the fallback calls. Write

`D_total = sum_i D_i`, `D_E = sum_{i in E} D_i`, `D_F = sum_{i in F} D_i`, and `w_sparse = D_E / D_total`.

In the most optimistic possible hybrid, set every sparse computation and every guard to zero cost and make every fallback cost exactly its paired dense-reference cost. Then

`H_ideal = D_F`,

so the nonlinear-evaluator speedup is bounded by

`S_kernel <= D_total / D_F = 1 / (1 - w_sparse)`.

If the dense trajectory spends fraction `alpha` of its full elapsed cost inside the nonlinear evaluator and every other trajectory component is unchanged, the full-trajectory bound is

`S_total <= 1 / (1 - alpha * w_sparse)`.

These are ceilings: nonzero guard cost, nonzero sparse compute, allocation/setup cost, or fallback overhead can only reduce the speedup.

A useful break-even form follows from the same decomposition. If fallback compute is paired to the dense reference, actual nonlinear hybrid cost is `D_F + S_E + G`, where `S_E` is sparse compute and `G` is all guard/routing overhead. Hybrid improvement requires

`D_E > S_E + G`.

If fallback itself carries extra overhead `Delta_F`, the condition tightens to

`D_E > S_E + G + Delta_F`.

Therefore a native benchmark should not report only total A-vs-B time. It should retain enough paired per-call information to compute `D_E`, `D_F`, `S_E`, `G`, and `Delta_F`, or at minimum the exact weighted `w_sparse` plus the dense nonlinear fraction `alpha`.

### Equal-dense-call-cost specialization of the frozen R10 routes

When dense-reference nonlinear calls are idealized as equal cost, `w_sparse = m/N`, where `m` is the sparse-eligible call count and `N` is the total nonlinear call count. The ideal kernel ceiling becomes `N/(N-m)`.

- Seed `91001`: `m/N = 2/20 = 0.10`; ideal kernel ceiling `10/9 = 1.111111...`.
- Seed `91003`: same `2/20`; ideal kernel ceiling `10/9 = 1.111111...`.
- Seed `91007`: `m/N = 1/20 = 0.05`; ideal kernel ceiling `20/19 = 1.052631...`.

For illustration, if `alpha=0.7`, the corresponding full-trajectory ceilings are about `1.07527`, `1.07527`, and `1.03627`. These are not empirical speedups; they are optimistic ceilings under the stated equal-call-cost specialization. The exact native replacement is the weighted formula above.

This converts the qualitative statement “support fills rapidly” into a quantitative kill criterion: when sparse-eligible dense-reference work is only a small share of total dense work, even a free sparse kernel cannot produce a large end-to-end gain, and guard/fallback overhead can erase the remaining envelope.

## Verification and artifacts

The probe was executed with Python `3.13.5`; `python -m py_compile` passed. The machine-readable result asserts all frozen route-count identities (`N = sparse + fallback`) and computes the exact rational ceilings with `fractions.Fraction`.

Durable branch artifacts:

- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_BCC918_R16/native_host_probe.py` — local SHA-256 `4a0adc7936e556cb116e07d6622b6cf6cfb6873b5a4aa615e80f14a98bd6a330`.
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_BCC918_R16/host_readiness_probe.json` — local SHA-256 `c7549d42840d435c39f59c4988958c9d0880db120efea3d990178da50ac6b73c`.

## Boundary

This checkpoint is a cost-obstruction analysis over frozen R10 route counts plus a fresh host-capability observation. It is not native spectralDNS evidence, not MPI execution, not a production benchmark, not an industrial acceleration claim, not a continuous-PDE certificate, and not independent review. The equal-call-cost numerical ceilings are deliberately labelled as idealized; the weighted identities are the quantities the native run must evaluate.

## Smallest unresolved unit

On a host already provisioned with the pinned spectralDNS/shenfun/MPI/FFTW stack, run the frozen native dense / guarded-hybrid / forced-fallback A/B/C experiment on the same held-out RK4 trajectories. Preserve normalization, retained cube/dealiasing, viscosity, precision, integrator, Nyquist handling, pressure/diffusion ordering, and Source ordering. Record exact support and route on every nonlinear call, plus paired dense-reference per-call cost, sparse compute, guard/routing cost, fallback cost, setup/allocation/compilation cost and full trajectory elapsed cost. Compute the weighted `w_sparse`, `alpha`, the ideal ceiling `1/(1-alpha*w_sparse)`, and the actual break-even margin `D_E-(S_E+G+Delta_F)`. Then route the immutable native checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.

Do not mark this task `DONE` before native-host evidence and independent review.
