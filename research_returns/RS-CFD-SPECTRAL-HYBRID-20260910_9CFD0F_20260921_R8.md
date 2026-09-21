# CFD continuation R8: joint state+Source step-boundary certificate

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-9CFD0F`  
Claim: `CLM-CFD-9CFD0F-20260921-1721-R8`  
Activity: `RA-TASK-AUTO-9CFD0F-20260921T172123P0800`  
State: `CONTINUATION_REQUIRED / R8_STEP_BOUNDARY_CERTIFICATE_PROVED / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Frontier consumed

R6 proved pinned-RK4 state-support induction and reduced R5's conservative state+Source-each-stage scans to Source-each-stage under explicit host-state assumptions. R7 then audited the canonical generic solve boundary and proved that Source can be certified once immediately before `integrate()` because ordinary `solver.update(context)` occurs only after the four-stage fixed RK4 call. R7 still leaves a robustness distinction: application code after a step can in principle mutate state as well as Source.

## New result

A fourth guard tier is proved: on the exact pinned synchronous `NS + fixed RK4 + generic solve` path, scan **both state and Source exactly once immediately before each `integrate()`**. If both supports lie in the certified carrier and no external mutation occurs during the `integrate()` call, R6's closure induction keeps all four stage states inside the carrier and R7's control-flow audit keeps the certified Source unchanged throughout the stages.

This tier tolerates arbitrary ordinary post-step `solver.update(context)` mutation of either state or Source, because the next step boundary rescans both before any sparse evaluation. It does not tolerate asynchronous or custom mid-stage mutation; the negative control demonstrates that limitation.

For four-stage RK4 the exact full-array scan count is 2 arrays/step for R8, versus 8 for R5 and 4 for R6. R7 remains cheaper at 1 scan/step but requires the stronger state-preservation attestation. These are logical scan counts, not measured native speedups.

## BRC resolution

`COMPOSE_APPLIED`. Exact Boolean support is the smallest sufficient carrier for the route decision. The numerical evolution retains complex amplitudes/phases and the existing pressure, diffusion, conjugacy and RK state; no support summary is substituted for those quantities.

## Validation

A deterministic task-local reference checker was compiled and executed:

- 50 canonical synthetic RK4 steps: exact carrier preservation PASS;
- between-step state+Source escape: caught before the next integrate PASS;
- between-step state-only escape: caught before the next integrate PASS;
- noncanonical mid-stage state mutation: pre-step certificate is shown insufficient, so the exclusion is real PASS;
- `py_compile`: PASS;
- runtime assertions: PASS;
- script SHA-256: `4372cb16f57be33208165325f0f3899b3bdadf1fccc18825aac49c2565d2c51d`.

The checker is a control-flow/support certificate only. The original spectralDNS/shenfun/FFTW host was not available or run in this unit.

## Durable outputs

- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_9CFD0F_R8/step_boundary_guard_contract.md`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_9CFD0F_R8/step_guard_reference_test.py`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_9CFD0F_R8/results.json`

## Next unresolved unit

Run the pinned native host and compare R5/R6/R7/R8 on identical nonlinear-active held-out trajectories against the unchanged dense callback, preserving Nyquist, pressure/diffusion and RK4; record raw setup/allocation/guard/total costs and fallback events; retain the most conservative tier whose assumptions are directly verified; then submit the original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910`.

No native speedup, trajectory-equivalence acceptance, industrial acceleration, continuous-PDE theorem, canonical promotion or mathematical acceptance is asserted.
