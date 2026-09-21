# CFD continuation R12: pinned-host instantiation obstruction checkpoint

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-4A8C2D`  
Claim: `CLM-CFD-4A8C2D-20260921-1931-R12`  
Activity: `RA-4A8C2D91F3E74B10`  
State: `CONTINUATION_REQUIRED / ORIGINAL HOST NOT RUN / CAPABILITY OBSTRUCTION VERIFIED / NO SPEEDUP CLAIM`

## Frontier consumed

R11 is consumed without replay. It proved that generation/dirty metadata cannot replace exact support scanning while raw state/Source writes remain unmediated, and that any metadata fast path must first establish a complete write barrier. R12 therefore attempts the next mandated unit: instantiate the pinned serial spectralDNS/shenfun/FFTW host before making any further performance claim.

BRC resolution is `COMPOSE_APPLIED_AT_BOUNDARY`: exact source identity, mutation provenance, signed/complex state and observer distinctions are preserved. No Boolean support quotient is used to infer host availability or numerical correctness.

## Frozen source verification

The task pins `spectralDNS/solvers/NS.py` blob `6a11909d1e2c1d529d382952c4c9d77e7073645c`. Connector readback of public `spectralDNS/spectralDNS` master shows commit `835b01b1e820b5c56559b9a028293e57526bfbf9` still carries exactly that blob, so the task's frozen NS source is not stale relative to public master for this file.

At that same public commit, `setup.py` declares runtime/build dependencies `numpy`, `shenfun>=4.0.2`, `cython`, `mpi4py-fft`, and `mpi4py`, and builds Cython/C++ extensions. Thus an exact host checkpoint needs more than the standalone `NS.py` file.

## Executable host-capability probe

`pinned_host_execution_probe.py` is network-free and fail-closed. It checks the required Python modules plus MPI/FFTW build/runtime surfaces and emits machine-readable JSON. On this execution host it reports:

- Python 3.13.5; GCC/G++ available.
- `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, and `pyfftw`: absent.
- `mpicc`/`mpicxx`: absent.
- `mpi.h` and `fftw3.h`: absent from standard include roots.
- FFTW shared libraries are present, but an MPI shared library is not detected.
- `runtime_ready = false`, `offline_source_build_prereqs = false`, exit code 3.

Script SHA-256: `1ab3ed03b7bc09b56cf1991aba6d2e72225bcf94c4492d77f5dfb0ef2d50b565`.

## Dependency acquisition attempt

A bounded package-install attempt for `spectralDNS shenfun pyfftw mpi4py` was made. It failed before installation because package-index DNS resolution repeatedly returned `[Errno -3] Temporary failure in name resolution`. Direct DNS probes for both `pypi.org` and `files.pythonhosted.org` returned the same error. No package was installed.

This is an execution-environment capability obstruction, not evidence that spectralDNS or its dependencies are unavailable generally.

## Result

The exact pinned native host could not be instantiated in this execution environment. Consequently R12 does **not** run a native RK4 trajectory and makes **no native-host speedup, total-cost, industrial-acceleration, continuous-PDE, or mathematical-acceptance claim**.

The useful result is narrower but verified: the current host cannot satisfy the task's original-host gate from either its present runtime or an offline source build, and the missing prerequisites are captured by a deterministic rerunnable probe. This prevents another continuation from mistaking surrogate execution for native-host evidence.

## Durable outputs

- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_4A8C2D_R12/host_capability_probe.json`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_4A8C2D_R12/pinned_host_execution_probe.py`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_4A8C2D_R12/results.json`

## Smallest unresolved unit

Run `pinned_host_execution_probe.py` in a host where the pinned spectralDNS/shenfun/MPI/FFTW stack is already provisioned. Only after it reports native readiness should the continuation execute identical nonlinear-active held-out RK4 trajectories for unmodified dense and guarded-hybrid paths, preserving Nyquist treatment, pressure/diffusion, Source ordering, fallback events and raw setup/allocation/compilation/guard/trajectory timings. Route that native-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.

Do not mark this task `DONE` before original-host evidence and independent review.
