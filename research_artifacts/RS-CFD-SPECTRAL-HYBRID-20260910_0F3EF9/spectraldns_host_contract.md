# Pinned spectralDNS Vortex host contract: support closure and Source guard

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Claim: `CLM-CFD-0F3EF9-20260921-1200`  
Researcher: `EM-CFD-E6911D`

## Scope

This is a source-backed integration checkpoint for the already pinned serial spectralDNS route. It does not emulate spectralDNS and does not assert an original-host run. The upstream source authority used here is the task-pinned `spectralDNS/solvers/NS.py` Git blob `6a11909d1e2c1d529d382952c4c9d77e7073645c`. The native adapter authority is Enterprise Math commit `3fb575716647b3f618bbd1483b7a4439ccca2601`, blob `1436c730189ba1b4f8d84359ff24a39f3ddc2f82`.

## Exact host operator order

The pinned `NS.py` context constructs Fourier/TensorProduct spaces, `U_hat = Function(VT)`, and `Source = Function(VT)`, with the source comment stating that it is initialized to zero. For the Vortex route the host convection callback transforms the stage state, computes curl, and applies the cross-product convolution. `ComputeRHS` then applies the Nyquist mask when enabled, applies pressure projection and diffusion, and finally performs `rhs += Source`.

The current native adapter replaces only the nonlinear convection callback. Its `validate_initial` extracts support from the initial `u_hat`, closes that support under retained signed addition, and freezes a fixed gather. The constructor retains `K`, `Tp`, and `VTp`, but does not retain or validate the host `Source` object.

## Full-trajectory support lemma

Let `C` be a fixed signed wavevector carrier inside the retained cube. Assume:

1. the initial spectral state has support contained in `C`;
2. `C` is closed under negation and every retained pair sum;
3. at every RK stage, `support(Source) subseteq C`;
4. pressure projection, diffusion, masking, and other linear host operations are modewise and therefore create no new wavevector labels.

Then every RK stage state has support contained in `C`.

Proof is by stage induction. A Vortex convolution of two fields supported in `C` can only create retained pair sums, hence remains in `C`. Nyquist masking can only delete labels. Pressure projection and diffusion multiply existing coefficients by wavevector-dependent matrices/scalars, so they do not create labels. The Source addition remains in `C` by assumption. Every explicit RK stage is a linear combination of already-supported states and RHS vectors, so its support also remains in `C`.

Therefore the current initial-support certificate is a valid support certificate for the pinned zero-Source trajectory. It is **not** a general source-agnostic certificate.

## Exact Source-escape counterexample

Take retained cutoff `K >= 1`. Let the initial support contain `p=(1,0,0)` and its conjugate partner, so the initial exact carrier can be x-axis-only. Let the host Source inject `q=(0,1,0)` and its conjugate partner after the first nonlinear call.

Choose divergence-free Fourier coefficients

- `u_p = (0,-1,-1)`, so `p . u_p = 0`;
- `u_q = (-1,0,-1)`, so `q . u_q = 0`.

Their vorticity coefficients are

- `omega_p = i p x u_p = (0,i,-i)`;
- `omega_q = i q x u_q = (-i,0,i)`.

At `r=p+q=(1,1,0)`, the Vortex pair contribution is

`u_p x omega_q + u_q x omega_p = (0,0,-2i)`.

This vector is perpendicular to `r`, so pressure projection leaves it unchanged. Thus after Source has inserted `q` into an RK stage, the next exact nonlinear evaluation can contain a nonzero `r=(1,1,0)` contribution. A fixed gather certified only from the initial x-axis carrier excludes both `q` and `r` and would miss that contribution.

This is an exact support-level failure mode, not a floating-point threshold effect and not a claim that the pinned default zero-Source run fails.

## Required contract repair for a general host adapter

The certified sparse route must adopt one of the following machine-checkable conditions:

1. **Zero-Source contract:** assert `Source == 0` before integration and preserve/check that condition for the certified route.
2. **Static-Source closure:** include the exact static Source support in the seed before computing `C`, and guarantee that support does not change.
3. **Dynamic escape guard:** before any sparse nonlinear call whose preceding stage may have received new Source support, detect support outside `C` and permanently fall back to the unchanged dense host callback.

The third option is safest for a general spectralDNS-compatible wrapper, while the first is sufficient for the currently frozen default Source-zero experiment.

## Host capability result in this execution environment

The environment exposes Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Numba 0.65.1 and system FFTW shared libraries. It does not expose the Python modules `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, or `pyfftw`; neither `mpiexec`, `mpirun`, nor `fftw-wisdom` is present. The original pinned serial host therefore cannot be instantiated here.

The project Library does list `/进取数论/CFD_9CFD0F_research.bundle` at 34,316 bytes, but raw materialization is denied for this Project file in the current execution context. Its previously reported SHA-256 is preserved as prior evidence and is not re-certified in this run.

## Status

This checkpoint strengthens the integration contract and identifies a concrete silent-discard condition that the final host adapter must guard. It does not replace the outstanding actual pinned serial-host execution, raw native timing capture, or independent `RS-CFD-TRAJECTORY-VERIFY-20260910` review.
