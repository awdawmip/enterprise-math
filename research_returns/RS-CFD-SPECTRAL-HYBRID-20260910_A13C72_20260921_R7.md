# CFD continuation R7: canonical solve discharges the Source-once-per-step control-flow precondition

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-TASK-AUTO-A13C72`  
Claim: `CLM-CFD-A13C72-20260921-1708-R7`  
Activity: `RA-TASK-AUTO-A13C72-20260921T170700P0800`  
State: `CONTINUATION_REQUIRED / SOURCE_ONCE_PER_STEP_SOURCE_CONTRACT_PROVED_FOR_CANONICAL_PATH / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Frontier consumed

R6 proved that RK4 stage state support is inductive inside the exact pinned RK4 contract and reduced the conservative R5 guard candidate from `state + Source` each stage to `Source` each stage. R6 intentionally left `Source` once per step disabled until both a no-midstep-Source-mutation contract and an exact step-boundary hook were established.

## New result

Auditing the exact pinned upstream `spectralDNS/__init__.py`, `spectralDNS/maths/integrators.py`, and `spectralDNS/solvers/NS.py` at commit `6f6335b7ee3ed8a7e49211c82ddf4bacbe4c220a` establishes a stronger host-control-flow fact for the canonical synchronous path:

- generic `solve()` calls `integrate()` first and calls application `solver.update(context)` only after the integrator returns;
- fixed RK4 executes four consecutive `ComputeRHS` calls inside that `integrate()` call and has no `additional_callback` hook;
- NS creates `Source` independently and `ComputeRHS` only reads it at `rhs += Source`.

Hence, if the exact pinned `NS + fixed RK4 + generic solve` path is used, and no asynchronous Source mutation or monkey-patched/custom mid-stage code exists, an exact Source-support scan immediately before `integrate()` certifies Source support for all four stages. A Source mutation performed by the ordinary application `update` callback happens after the step and is caught by the next pre-integrate scan.

This identifies the exact implementation boundary: **R7 belongs at the solve/integrate wrapper, not inside the nonlinear callback.** If that boundary cannot be hooked or fingerprinted, retain R6 Source-each-stage. If host-state mutation assumptions are not verified, retain R5 state+Source-each-stage.

## Validation

A task-local executable reference test was compiled and run successfully. It verifies the canonical two-step control flow, catches a Source escape injected by a post-step update before the next integrate, and includes a negative control where a synthetic mid-stage callback injects an escape and defeats once-per-step scanning.

- `guard_reference_test.py` SHA-256: `69d50f8d933a2560eaac4ddabd603cee1fab74bddbd94f75c641d462a2e22e1f`
- `py_compile`: PASS
- runtime assertions: PASS

This is a control-flow/certification result only. It is not native spectralDNS trajectory evidence, speedup evidence, or a continuous-PDE theorem.

## Durable artifacts

- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_A13C72_R7/host_contract_probe.json`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_A13C72_R7/source_state_guard_contract.md`
- `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_A13C72_R7/guard_reference_test.py`

## Next unresolved unit

Instantiate the pinned serial spectralDNS/shenfun/FFTW host on an authorized environment; place the R7 scan at the real pre-`integrate()` boundary; run R5, R6 and R7 guard tiers against the unchanged dense host on identical nonlinear-active held-out RK4 trajectories; retain setup/allocation/guard/trajectory total timings and fallback events; keep the most conservative tier if any activation assumption is not directly verified; then submit the original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910`.

No DONE, native speedup, industrial acceleration, canonical promotion or mathematical acceptance is asserted.
