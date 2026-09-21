# CFD continuation R10: exact guard lower bound and native-host blocker

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-DF8E09`  
Claim: `CLM-CFD-DF8E09-20260921-1805-R10`  
Activity: `RA-A328104BCDDE90FA79D78F93`  
State: `CONTINUATION_REQUIRED / EXACT_GUARD_INFORMATION_BOUND_PROVED / LOCAL_LAYOUT_BENCH_EXECUTED / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Frontier consumed

This execution consumed the canonical R8 continuation at immutable commit `6b1589021a94d304e7e404ec5143047f2c6e8b6e` rather than replaying earlier support/Source work. R8 had already proved that on the pinned synchronous `NS + fixed RK4 + generic solve` path, exact state+Source support can be certified once immediately before each `integrate()` when no external mid-stage mutation occurs. The unresolved requirement remained an actual run on the pinned serial spectralDNS/shenfun/FFTW host.

BRC resolution remains `COMPOSE_APPLIED`: exact Boolean support is used only as the routing observer. Signed/complex amplitudes, phase, wavevector labels, conjugacy, pressure/diffusion and RK4 state remain intact outside that quotient.

## Native-host attempt

The current runtime exposes Python 3.13.5, NumPy 2.3.5, Numba 0.65.1 and system `libfftw3.so.3`, but does not contain `spectralDNS`, `shenfun`, `mpi4py` or `pyfftw`; `mpiexec`, `mpirun` and `fftw-wisdom` are absent. A bounded package-source attempt (`python -m pip download spectralDNS --no-deps`) failed because DNS/network resolution to the configured package index was unavailable. Therefore the original pinned host was **not run**, and no native timing or native trajectory-equivalence claim is made.

The exact environment evidence is preserved in `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_DF8E09_R10/native_host_probe.json`.

## New research result: exact R8 guard has a complement-size information lower bound

Under the R8 mutation model—state and Source may each change arbitrarily between steps, with no trusted dirty set, generation counter or write barrier—any zero-error exact certificate of `supp(x) ⊆ C` must inspect every outside-carrier coefficient on a passing worst-case input.

The proof is an indistinguishability adversary. If a deterministic guard accepts before reading all of `C^c`, choose an unqueried outside coordinate `j`. The all-zero input and an input with one nonzero coefficient at `j` give the same complete query transcript but require opposite decisions. Hence the guard cannot accept before exhausting `C^c`. For independently mutable state and Source the bounds add; with three complex velocity components this is `2 * 3 * |C^c_modes|` complex coefficient reads.

A concrete certificate with 257 coordinates, a 31-coordinate carrier and 226 outside coordinates verifies the witness: querying 225 outside coordinates leaves one skipped coordinate, and the zero input versus an impulse at that coordinate have identical observed transcripts but opposite correct support decisions.

This lower bound is conditional on the no-metadata mutation model. Exact trusted host mutation metadata would change the information model and can legitimately reduce scanning work.

## Local exact-layout experiment

A deterministic 64^3 rFFT local guard benchmark used 135,168 storage modes, three complex components and state+Source together containing 811,008 complex coefficients. Four exact guards were compared: NumPy advanced-index complement gather, NumPy full contiguous mode reduction, compiled full contiguous skip, and compiled complement-index scan. Every method caught an outside-carrier coefficient of magnitude `1e-300`, preserving exact nonzero support rather than threshold support.

The measured result separates logical query optimality from memory-layout efficiency. For carrier fraction 0, medians were 4.817 ms (NumPy gather), 1.467 ms (NumPy full reduction), 1.072 ms (compiled full-skip), and 1.297 ms (compiled complement-index). At carrier fraction 0.5, compiled complement-index fell to 0.666 ms versus 1.890 ms for compiled full-skip. At carrier fraction 0.99 it reached 0.0216 ms versus 0.120 ms for compiled full-skip and 1.660 ms for NumPy full reduction.

Therefore, although an exact guard cannot beat the complement-size information bound in coefficient-query count under arbitrary mutation, explicitly gathering the complement is not always the fastest physical implementation. When the carrier is sparse, contiguous traversal can win through locality; when the carrier is dense, compiled complement-index traversal wins decisively in this local runtime. The crossover must be re-measured on the actual pinned host/hardware, and any calibration/compilation cost must be charged to the task's declared reuse horizon.

Validation: the local checker compiled and ran; all exact escape controls passed. Benchmark script SHA-256 is `7dda81c5a6b1e3cdab6bbb6f4fe4e344cca0d5619a35483504610019956a0667`. Full summary data are preserved in `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_DF8E09_R10/results.json`.

## Smallest unresolved unit

Instantiate the exact pinned serial spectralDNS/shenfun/FFTW host. On identical nonlinear-active held-out RK4 trajectories, compare the unchanged dense callback against R5/R6/R7/R8 while preserving Nyquist handling, pressure/diffusion, Source ordering, fallback events and raw setup/allocation/compilation/guard/total costs. For the R8 exact guard, compare an exact contiguous/compiled scan against exact complement-index scanning on the native layout rather than assuming the local crossover transfers. Retain the most conservative guard tier whose assumptions are directly verified, keep dense fallback for losing configurations, then route the original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.

The parent task remains `CONTINUATION_REQUIRED`. No native speedup, industrial acceleration, continuous-PDE result, native-P000 fluid theorem, canonical promotion or mathematical acceptance is asserted.
