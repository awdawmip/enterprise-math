# CFD continuation R9: exact guard lower bound and memory-layout benchmark

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-TASK-AUTO-C4D219`  
Claim: `CLM-CFD-C4D219-20260921-1749-R9`  
Activity: `RA-TASK-AUTO-C4D219-20260921T174838P0800`  
State: `CONTINUATION_REQUIRED / R9_GUARD_LOWER_BOUND_PROVED / LOCAL_LAYOUT_BENCHMARK_ONLY / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Frontier consumed

R8 proved that on the exact pinned synchronous `NS + fixed RK4 + generic solve` path, state and Source may both be certified once immediately before each `integrate()` call, tolerating arbitrary ordinary between-step mutation while excluding external mid-stage mutation. Its reference checker implements the exact outside-carrier test with boolean complement indexing.

## New result 1 — exact information lower bound

For an independently mutable coefficient array `x`, exact certification of `support(x) subseteq C` requires checking every coefficient in `C^c` in the worst case unless the host supplies additional trusted mutation metadata. Proof is adversarial: if any outside coordinate is unqueried, the all-zero outside state and a one-spike escape at that coordinate are indistinguishable on every queried value but require opposite route decisions.

Hence under R8's robustness model, independently mutable state and Source require at least `2|C^c|` outside-coefficient value queries per step boundary. R8 is therefore minimal in the number of independently mutable objects certified. R7 can use one object only because it assumes state preservation; a sound further reduction requires a write barrier/dirty bit/mutation log or an equally strong host contract, not another purely black-box guard trick.

This is a finite-array routing theorem only. It grants no PDE result, host trajectory equivalence or speedup.

## New result 2 — query-optimal is not memory-layout-optimal

The deterministic reference program used `N=405,504` complex coefficients, matching the prior n=64 three-component r2c storage count, seed `20260921`, 200 exactness/mutation cases, and 60 warm repetitions per benchmark point. All correctness cases and adversarial missed-index witnesses passed; `py_compile` passed.

At the task-relevant sparse threshold of 384 retained carrier coefficients (`|C|/N ~= 9.47e-4`), median two-object state+Source boundary costs were:

- R8-style NumPy boolean complement gather: **1.3986 ms**;
- full contiguous masked predicate: **0.7946 ms**;
- integer outside-index gather: **1.5233 ms**;
- compiled complement loop (Numba, warm): **0.7317 ms**.

Thus in this local layout, the contiguous predicate was about **1.76x faster** than boolean complement gather even though it examines inside-carrier values, while the compiled complement loop was about **1.91x faster** than the boolean gather and about **8.6% faster** than the contiguous predicate. At larger carrier fractions the ordering changes; integer outside-index gather becomes advantageous only when the complement is substantially smaller. Therefore logical coefficient-query count is not a valid proxy for actual guard time.

These are local guard microbenchmarks, not spectralDNS native trajectory timings. Compilation/setup costs are excluded from warm medians and must be charged according to the declared reuse horizon in the native host.

## BRC resolution

`COMPOSE_APPLIED`. The exact Boolean carrier remains sufficient only for routing. Complex amplitudes/phases, pressure, diffusion, Hermitian structure and RK state are preserved by the numerical path; the guard does not replace them.

## Durable outputs

- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_C4D219_R9/complement_guard_contract.md`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_C4D219_R9/complement_guard_reference.py`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_C4D219_R9/results.json`

Script SHA-256: `d74ebfe0bfa8dcbbc43edb453af678306b2ecdba6c16b50b3e748cb4f7ec14b4`  
Results SHA-256: `38438be8986452b9f33d35ff0a6bfb8787b5777b3961195501dedc6c0711291b`

## Next unresolved unit

On the exact pinned serial spectralDNS/shenfun/FFTW host, compare the exact R8 boolean-complement guard with an allocation-conscious contiguous or compiled exact guard on identical nonlinear-active held-out trajectories. Charge compilation/setup/allocation according to the declared reuse horizon and preserve unchanged dense callback, Nyquist, pressure/diffusion, RK4 and fallback events. This implementation comparison can be folded into the already-required R5/R6/R7/R8 native matrix; route the resulting original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910`.

No original-host speedup, trajectory-equivalence acceptance, industrial acceleration, continuous-PDE theorem, canonical promotion or mathematical acceptance is asserted.
