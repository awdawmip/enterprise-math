# R7 source/state guard contract: canonical RK4 step-boundary certification

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Claim: `CLM-CFD-A13C72-20260921-1708-R7`  
Pinned spectralDNS commit: `6f6335b7ee3ed8a7e49211c82ddf4bacbe4c220a`

## New source-level result

R6 left Source-once-per-step disabled pending two facts: an exact no-midstep-Source-mutation contract and an exact RK4 step-boundary hook. The pinned host source supplies both **for the canonical synchronous path**, with explicit exclusions below.

At the pinned `spectralDNS.solve` loop, `integrate()` returns before `solver.update(context)` is called. The pinned fixed `RK4` implementation performs four consecutive `solver.ComputeRHS(...)` evaluations inside that single `integrate()` call and does not invoke the user `additional_callback`. In the pinned NS solver, `Source` is allocated as a distinct `Function(VT)` and `ComputeRHS` only consumes it through `rhs += Source`.

Therefore, for the exact pinned `NS + fixed RK4 + generic solve` path:

1. scan exact `support(Source)` immediately **before** `integrate()`;
2. if the scan is contained in certified carrier `C`, all four RK4 stages see the same Source support, provided no asynchronous mutation or monkey-patched/custom mid-stage code exists;
3. `solver.update(context)` occurs only after the full RK4 step and may change Source for the next step;
4. the next pre-`integrate()` scan catches any such between-step Source change before the next RHS evaluation.

This discharges the two R6 source-level preconditions **for this exact host path**. It does not activate the optimization on an unverified runtime and does not establish a native speedup.

## Correct integration point

The existing nonlinear / RHS callback is not an adequate place to infer “first stage of the step”: `ComputeRHS` is called four times but receives no explicit RK stage or step token. A correct Source-once-per-step optimization should therefore wrap the exact call boundary immediately before `integrate()` (or use an audited equivalent step token). If the adapter cannot hook that boundary, retain R6 Source-each-stage scanning. If host-state mutation assumptions are also unavailable, retain the R5 state-plus-Source-each-stage guard.

## Explicit exclusions

The once-per-step result is invalid without re-audit if any of these are present:

- a custom integrator or monkey-patched `ComputeRHS`;
- a callback inserted between RK4 stages;
- asynchronous mutation of `context.Source` from another thread/process/signal path;
- an application that bypasses the canonical generic `solve` loop and invokes the integrator through a different lifecycle;
- aliasing or external mutation not represented by the pinned source contract.

## Validation

`guard_reference_test.py` mirrors only the relevant control-flow invariant, not spectralDNS numerics. It passes four checks:

- canonical pre-step scans stay clear when Source remains in carrier;
- carrier-preserving state remains inside carrier;
- a post-step update injecting Source escape is caught before the next integrate call;
- a deliberately noncanonical mid-stage Source mutation defeats once-per-step certification, proving the exclusion is substantive.

`py_compile`: PASS.  
Runtime: PASS.  
SHA-256: `69d50f8d933a2560eaac4ddabd603cee1fab74bddbd94f75c641d462a2e22e1f`.

## Remaining hard gate

The original spectralDNS/shenfun/FFTW host was **not** run in this environment. The next decisive unit is still native-host execution: install/instantiate the pinned serial host, implement the guard at the actual pre-`integrate()` boundary, compare R5/R6/R7 guard tiers on identical nonlinear-active held-out trajectories, preserve raw total-cost timings, and then route the original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910`.
