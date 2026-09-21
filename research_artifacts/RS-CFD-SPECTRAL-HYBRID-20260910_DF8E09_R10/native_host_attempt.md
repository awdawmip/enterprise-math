# R10 native-host attempt and exact guard information bound

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-DF8E09`  
Claim: `CLM-CFD-DF8E09-20260921-1805-R10`

## Canonical frontier consumed

The canonical startup packet for this execution selected the R8 durable frontier at immutable commit `6b1589021a94d304e7e404ec5143047f2c6e8b6e`. R8 established a joint state+Source exact-support certificate immediately before each `integrate()` on the pinned synchronous `NS + fixed RK4 + generic solve` route, while explicitly leaving the original spectralDNS/shenfun/FFTW host unrun.

The pinned upstream `NS.py` blob is `6a11909d1e2c1d529d382952c4c9d77e7073645c`. Its `ComputeRHS` ordering is nonlinear convection, optional Nyquist masking, pressure/diffusion, then `rhs += Source`. This run preserves that ordering as the host target and does not replace it with the local benchmark.

## Original-host attempt

The current runtime has Python 3.13.5, NumPy 2.3.5, Numba 0.65.1 and a system `libfftw3.so.3`, but the Python modules `spectralDNS`, `shenfun`, `mpi4py` and `pyfftw` are absent. `mpiexec`, `mpirun` and `fftw-wisdom` are also absent. A bounded `python -m pip download spectralDNS --no-deps` attempt could not reach the configured package index because DNS/network resolution failed. Consequently the exact pinned serial host could not be instantiated and **was not run**. The network failure is not evidence that the package is unavailable upstream.

## New exact lower bound

Let `C` be the certified carrier and let a guard decide, with zero error, whether `supp(x) ⊆ C`. Assume coefficients outside `C` may be changed arbitrarily between steps and the guard has no trusted mutation metadata, dirty set, generation counter or write barrier.

**Claim.** On a passing worst-case input, every deterministic exact guard based on coefficient reads must inspect every coefficient outside `C`.

**Proof.** Consider the all-zero transcript. Suppose the guard accepts after reading only a strict subset of `C^c`. Choose an unqueried outside coordinate `j`. The all-zero input `x=0` and an input `x=e_j` with a nonzero coefficient at `j` return identical values on every coordinate the guard queried, yet the correct decisions differ: `supp(0) ⊆ C` is true and `supp(e_j) ⊆ C` is false. A deterministic guard therefore cannot accept before exhausting `C^c`. For independently mutable state and Source, the lower bounds add. With three complex velocity components per spectral mode, the state+Source bound is `2 * 3 * |C^c_modes|` complex coefficient reads.

A concrete adversarial certificate used `M=257`, `|C|=31`, `|C^c|=226`; a hypothetical guard reading 225 outside coordinates cannot distinguish all-zero from an impulse at the skipped coordinate 256, while the correct answers are opposite.

This is an information-acquisition bound, not a statement that an advanced-index gather is the fastest implementation. Trusted exact mutation metadata would change the information model and can invalidate the lower bound's premise.

## Exact local guard experiment

A deterministic local reference benchmark used a 64^3 rFFT storage geometry: 135,168 spectral storage modes, three complex components, and state+Source together containing 811,008 complex coefficients. Four exact guards were compared on passing cases at seven carrier fractions:

1. NumPy advanced-index complement gather;
2. NumPy full contiguous mode reduction;
3. a compiled Numba full contiguous scan that skips carrier modes;
4. a compiled Numba complement-index scan.

All methods use exact `!= 0`. A deliberately tiny outside-carrier coefficient `1e-300` at the last complement index was detected by every method at every nonempty-complement case, so the experiment does not introduce an amplitude threshold.

The main implementation result is a locality/query-count tradeoff. At carrier fraction 0 (the complement is the whole storage domain), median pair-guard times were 4.817 ms for NumPy gather, 1.467 ms for NumPy full reduction, 1.072 ms for compiled full-skip, and 1.297 ms for compiled complement-index. At carrier fraction 0.5, compiled complement-index was 0.666 ms versus 1.890 ms for compiled full-skip. At carrier fraction 0.99, compiled complement-index was 0.0216 ms versus 0.120 ms for compiled full-skip and 1.660 ms for NumPy full reduction.

Thus the logical optimum of querying only `C^c` is not automatically the physical-memory optimum when `C^c` is nearly the whole array. The native implementation should select among exact layouts based on actual carrier density and actual host/hardware timing, charging calibration/compilation/setup under the declared reuse horizon. No threshold inferred from this runtime is promoted to the pinned host.

The executed benchmark script compiled successfully. Its SHA-256 is `7dda81c5a6b1e3cdab6bbb6f4fe4e344cca0d5619a35483504610019956a0667`. Summary results and validation witnesses are preserved in `results.json`.

## BRC resolution

`COMPOSE_APPLIED`. Exact Boolean support remains the smallest sufficient observer for the sparse-versus-dense route decision. The numerical state retains signed/complex amplitudes, phases, wavevector labels, conjugacy, pressure/diffusion and RK4 state; none of those are replaced by the support observer. The new lower bound concerns the cost of obtaining the exact routing observer under arbitrary between-step mutation.

## Status and next unresolved unit

This run proves a new worst-case guard-information bound and supplies a local exact implementation comparison, but does not satisfy the parent task's original-host requirement. The smallest unresolved unit is still to instantiate the exact pinned serial spectralDNS/shenfun/FFTW host and run identical nonlinear-active held-out RK4 trajectories through the unchanged dense callback and the R5/R6/R7/R8 guard tiers, preserving Nyquist, pressure/diffusion, fallback events and raw setup/allocation/compilation/guard/total timings. The exact guard layout should be chosen or calibrated on that host, not from this local microbenchmark. The resulting original-host checkpoint must then go to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review before any DONE or speedup claim.

No native-host speedup, trajectory-equivalence acceptance, industrial acceleration, continuous-PDE theorem, P000 fluid derivation, canonical promotion or mathematical acceptance is asserted.
