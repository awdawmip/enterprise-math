# RS-CFD-TRAJECTORY-VERIFY-20260910 — independent verification return

Researcher: `EM-CFD-VFY-7C31A2`  
Claim: `CLM-CFDVFY-7C31A2-20260921-1240`  
Status: `CONTINUATION_REQUIRED`

## Result

I independently audited the published task contract, the pinned spectralDNS source, the native-host validation harness, adapter source, durable author report, and the stored Numba validation result. This is a verifier-owned source/result audit; it does **not** relabel the author run as an independent numerical rerun.

The published author evidence is internally coherent for the frozen **zero-Source finite-discrete matrix**. The harness uses the real spectralDNS context, preserves upstream pressure projection/diffusion and RK4, compares dense and hybrid velocity/RHS/pressure outputs, checks one-RHS projected divergence, records full per-trajectory timings, and preserves dense fallback. The durable result records the eight frozen cases with passing floating comparisons; random256 demonstrates genuine dense fallback rather than forced sparsity. Source identity pins are explicit and stable.

However, the Task cannot honestly be closed from the current evidence. Four required certificate obligations remain incomplete:

1. **Nonzero Source is unverified.** `host_validation.py` explicitly executes `c.Source.fill(0)`. The pinned upstream `ComputeRHS` adds `Source` after convection, masking, pressure projection and diffusion. Therefore the current native-host matrix is a zero-Source certificate only; it does not cover static or dynamic forcing.
2. **No timestep refinement.** The frozen trajectory uses only `dt=0.002`, 12 steps, final time 0.024. The taskbook explicitly requires timestep refinement, so floating agreement at one timestep cannot satisfy that requirement.
3. **Conjugacy is only partially checked.** The adapter validates initial zero-plane Hermitian symmetry, but the durable output does not emit an explicit all-step or final full-storage conjugacy certificate.
4. **Energy behavior is only partially checked.** The analytic viscous shear decay is useful, but there is no general kinetic-energy series/inequality audit for the other cases.

The environment available to this verifier does not contain spectralDNS, shenfun, mpi4py, mpi4py-fft or pyFFTW, so a native-host rerun here would be fabricated if claimed. I therefore froze the exact missing rerun unit instead of replaying author benchmarks or marking PASS/DONE.

## Smallest next verification unit

On the same pinned serial spectralDNS/shenfun/FFTW host:

- add verifier-owned zero/static/dynamic Source cases and compare dense vs hybrid full trajectories, velocity and modified pressure;
- repeat the same final time at `dt=0.002` and `dt=0.001` for one sparse-preserving and one densifying case;
- emit explicit Hermitian-conjugacy and kinetic-energy diagnostics at every step/final state;
- retain raw setup/allocation/planning/RK4/readout timings and all failures.

No universal CFD speedup, continuous-PDE certificate, industrial claim, or independent numerical acceptance is granted by this return.

## Durable verifier artifacts

- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_7C31A2/source_audit.json`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_7C31A2/validation_matrix.json`
