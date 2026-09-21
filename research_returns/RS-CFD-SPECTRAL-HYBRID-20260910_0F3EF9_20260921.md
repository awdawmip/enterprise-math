# CFD continuation: pinned host capability and Source-support guard

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-E6911D`  
Claim: `CLM-CFD-0F3EF9-20260921-1200`  
Activity: `RA-20260921T1200-0F3EF9`  
State: `CONTINUATION_REQUIRED / NEW_SOURCE_GUARD_FOUND / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Claimed frontier and reuse

This run resumed the most recent continuation checkpoint at `0037b7b54ad0ac74b22607d29aca38e85b564522:research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_421478_20260921.md` rather than repeating its exact-axis certificate, `(0,3)` empty-support repair, held-out finite-Galerkin trajectories or reuse-horizon arithmetic. The task-pinned upstream host source remains `spectralDNS/solvers/NS.py` blob `6a11909d1e2c1d529d382952c4c9d77e7073645c`; the native adapter remains Enterprise Math blob `1436c730189ba1b4f8d84359ff24a39f3ddc2f82` at commit `3fb575716647b3f618bbd1483b7a4439ccca2601`.

BRC resolution is `EXTEND_EXISTING_TOOL / REUSE_EXECUTED`. The carrier remains exact signed wavevector support used only for route certification; amplitudes, phase, conjugacy, pair multiplicity, pressure/diffusion and dense fallback remain outside that quotient.

## Environment capability result

The current execution environment exposes Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Numba 0.65.1 and system FFTW shared libraries, but does not expose `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft` or `pyfftw`; `mpiexec`, `mpirun` and `fftw-wisdom` are absent. The original pinned serial spectralDNS/shenfun/FFTW host therefore cannot be instantiated in this environment.

The Project Library now positively lists `/进取数论/CFD_9CFD0F_research.bundle` at 34,316 bytes. A direct raw materialization attempt was made and was denied because this Project file has no authorized raw-byte materialization path. Therefore the previously reported bundle SHA-256 `7ff5b7369cb052f42820da987d0559e202834dd8d841784168c29810d73465bb` is preserved as prior evidence but was not re-certified in this run.

## New source-backed result: initial support alone is not a general Source-safe trajectory certificate

The pinned upstream `NS.py` constructs `Source = Function(VT)` with a comment that it is initially zero. Its `ComputeRHS` performs the nonlinear callback, optional Nyquist mask, pressure projection and diffusion, and only then executes `rhs += Source`.

The current native adapter computes a fixed carrier only from the initial `u_hat`. Its constructor retains `K`, `Tp` and `VTp`, but does not retain or validate the host `Source` object. Therefore the existing closure proof is sufficient for the frozen zero-Source experiment but is not sufficient for a general source-agnostic spectralDNS wrapper.

### Full-trajectory support lemma

Let `C` contain the initial support and be closed under negation and every retained pair sum. If `support(Source) subseteq C` at every RK stage, then the Vortex nonlinear term remains in `C`; Nyquist masking only deletes labels; pressure projection and diffusion are modewise; and RK linear combinations preserve support. By stage induction, all stage states stay in `C`.

Thus `Source == 0` is a sufficient pinned-host condition. A nonzero source must either be included in the closure or guarded dynamically.

### Exact silent-discard counterexample

Take `p=(1,0,0)` in the initial state and let Source later inject `q=(0,1,0)`. Choose divergence-free coefficients

- `u_p=(0,-1,-1)`;
- `u_q=(-1,0,-1)`.

Then

- `omega_p = i p x u_p = (0,i,-i)`;
- `omega_q = i q x u_q = (-i,0,i)`;
- at `r=p+q=(1,1,0)`, the Vortex pair sum is `(0,0,-2i)`.

This vector is perpendicular to `r`, so pressure projection does not remove it. After Source has inserted `q` into an RK stage, the next exact nonlinear evaluation can therefore contain a genuine nonzero `r` mode. A fixed gather built only from the initial x-axis carrier excludes both `q` and `r` and can silently miss that contribution.

The durable exact counterexample and environment probe are recorded in `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_0F3EF9/host_capability_probe.json`; the operator-order proof and repair contract are in `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_0F3EF9/spectraldns_host_contract.md`.

## Required adapter condition

Before actual host evaluation, the certified sparse route should use one of three explicit contracts:

1. assert and preserve `Source == 0` for the whole certified trajectory;
2. include a proven static Source support in the initial carrier closure;
3. detect Source support escape and permanently fall back to the unchanged dense host callback before the next sparse nonlinear call.

For the currently frozen default Source-zero experiment, condition 1 is sufficient. For a general spectralDNS-compatible adapter, condition 3 is the conservative choice.

## Status and smallest unresolved unit

This run completed a bounded research unit and found a new exact integration condition that prevents a real silent-discard class. It did **not** run the original host and does not mark the parent task DONE.

The smallest unresolved unit is now sharper: instantiate the pinned serial spectralDNS/shenfun/FFTW Python host (or execute on an authorized host where it already exists); enforce the Source contract above; integrate the existing exact-axis selector and `(0,3)` repair; run the unchanged dense callback, pressure/diffusion and RK4 on nonlinear-active held-out cases; retain setup/allocation/compilation/trajectory raw timings under the declared reuse horizon; then submit the host checkpoint to independent `RS-CFD-TRAJECTORY-VERIFY-20260910` review.

No universal speedup, industrial acceleration, continuous-PDE theorem, native-P000 fluid theorem, canonical promotion or mathematical acceptance is asserted.
