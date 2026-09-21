# R8 step-boundary guard contract: state + Source once per RK4 step

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Claim: `CLM-CFD-9CFD0F-20260921-1721-R8`  
Consumes R6: `e0433bfb27986280333d5232eaff33f02ccbaeba`  
Consumes R7: `4f953b8545613f172ba98add4583bd4fe37d4a34`  
Pinned spectralDNS commit: `6f6335b7ee3ed8a7e49211c82ddf4bacbe4c220a`

## Exact statement

Let `C` be the linear coordinate subspace consisting of spectral states supported on the certified retained carrier. Assume, for one call of the pinned fixed-RK4 `integrate()`:

1. immediately before `integrate()`, exact scans establish `support(U_n) subseteq C` and `support(Source) subseteq C`;
2. whenever `U` and `Source` are supported in `C`, the certified sparse `ComputeRHS` path returns the complete RHS on `C`, while Nyquist deletion, pressure projection and diffusion are modewise, so `support(RHS(U,Source)) subseteq C`;
3. during that `integrate()` call there is no asynchronous, monkey-patched or custom callback mutation of either the RK state or `Source`;
4. the host is the audited pinned `NS + fixed RK4 + generic solve` control-flow, or an audited equivalent with the same step boundary.

Then every RK4 stage state and the final step state are supported in `C`. Therefore neither state nor Source requires a full support scan between the four RK stages: **one exact state scan plus one exact Source scan immediately before each `integrate()` is sufficient for the whole step.**

Proof: R6 established closure of `ComputeRHS` on `C`. The fixed RK4 stages are scalar linear combinations of the step-entry state and already-closed RHS values; a linear coordinate subspace is closed under these combinations. R7 established that the canonical fixed-RK4 call has no ordinary application callback between stages and that ordinary `solver.update(context)` occurs only after `integrate()` returns. Thus both step-entry certificates remain valid throughout the integration interval under assumption 3.

## Robustness gain over R7

R7's cheapest tier scans Source once per step while deriving state support inductively. That remains valid only if state cannot be externally moved outside `C` between certified steps, or if such state preservation is separately attested.

R8 deliberately spends one additional full-array scan at the next step boundary. Consequently ordinary post-step application code may mutate **either** state or Source arbitrarily: any outside-carrier coefficient is detected before the next sparse RK4 evaluation and the adapter can permanently route to dense.

- R5: state + Source each of four stages = 8 array scans/step.
- R6: Source each stage = 4 scans/step.
- R7: Source once per step = 1 scan/step, with stronger state-preservation attestation.
- **R8: state + Source once per step = 2 scans/step; ordinary between-step mutation of both is tolerated, but no mutation during `integrate()` is allowed.**

These are scan-count reductions only, not runtime speedup claims.

## Failure boundary

A pre-step certificate cannot see a mutation introduced after the scans but before a later RK stage. The executable negative control injects an outside-carrier state coefficient after stage 1; the pre-step guard has already passed and the outside coefficient survives, so the certificate is invalid. Any asynchronous mutation, custom mid-stage callback, monkey patch, custom integrator, or lifecycle bypass therefore forces fallback to R6/R5 or a re-audit.

## BRC use

`COMPOSE_APPLIED`. The Boolean support carrier is used only as the routing certificate. Complex amplitudes and phases, conjugacy, pair multiplicity, pressure/diffusion and RK state are retained by the actual evolution; no total-only or absolute-value quotient is used to justify trajectory equivalence. The observer is the exact outside-carrier nonzero predicate.

## Executed validation

`step_guard_reference_test.py`:

- `py_compile`: PASS;
- runtime assertions: PASS;
- 50 canonical synthetic RK4 steps remain exactly inside the carrier;
- post-step mutation of both state and Source is detected at the next boundary;
- state-only post-step mutation is detected at the next boundary;
- an explicit mid-stage mutation is missed by the pre-step certificate and remains outside the carrier, validating the exclusion;
- test SHA-256: `4372cb16f57be33208165325f0f3899b3bdadf1fccc18825aac49c2565d2c51d`.

This reference checker validates the control-flow/support argument only. It is not spectralDNS/shenfun/FFTW native-host trajectory evidence.

## Smallest unresolved unit

Instantiate the pinned serial spectralDNS/shenfun/FFTW host and implement the R8 guard immediately before the real `integrate()` call. On identical nonlinear-active held-out trajectories compare R5/R6/R7/R8 against the unchanged dense callback, preserving Nyquist, pressure projection, diffusion and RK4. Record raw guard/setup/allocation/total trajectory costs and all fallback events. If any activation assumption is not directly verified, retain the more conservative tier. Route the resulting original-host checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review. No DONE before that evidence and review.
