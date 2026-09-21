# Source-support guard and atomic dense replay contract

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`
Research unit: `EM-CFD-E6911D / CLM-CFD-E6911D-20260921-1300`
Scope: implementation-ready contract only; not a replacement for the pinned spectralDNS host and not a native-host timing result.

## 1. Authority and defect boundary

The task-pinned native adapter (`1436c730189ba1b4f8d84359ff24a39f3ddc2f82`) constructs its fixed carrier only from `validate_initial(u_hat)`: it calls the exact support extractor on the initial spectral field and closes that seed under retained negation/pair sums. Its constructor retains `K`, `Tp`, and `VTp`, but has no `Source` field or Source-support validation. Therefore its certificate is sound for the frozen `Source == 0` case but is not a general Source-safe trajectory certificate.

The host operator order established by the prior source-backed checkpoint is nonlinear callback -> optional Nyquist mask -> pressure/diffusion -> `rhs += Source`. Masking deletes modes and pressure/diffusion are modewise; Source can add a new label after those operations.

## 2. Static support contract

A static Source contract means a **declared support envelope**, not frozen Source coefficients.

Let `S0 = support(U_hat(t0))` and let `Ssrc` be a set of retained Fourier labels such that at every certified RK stage `support(Source_stage) subseteq Ssrc`. Seed the existing carrier closure with `S0 union Ssrc`.

The coefficients on `Ssrc` may vary arbitrarily with stage and time. The support certificate is label-based and never depends on amplitude, phase, conjugacy assumptions, or a coefficient threshold.

### Exactness rule

In exact-equivalence mode, a coefficient belongs to support iff it is exactly nonzero. Any tolerance-based detector is an explicit approximation parameter and cannot be described as an exact-equivalence certificate without a separate error bound.

## 3. Dynamic escape contract

For a general host-compatible adapter, inspect the current stage Source before the current stage RHS is committed:

1. Compute `S = exact_support(Source_stage)`.
2. Compute `escape = S - C`, where `C` is the certified fixed carrier.
3. If `escape` is empty, the stage may use the certified sparse route.
4. If `escape` is nonempty:
   - do not drop/project the escaped Source modes;
   - discard any speculative sparse RHS for that stage;
   - replay the **same stage input** through the unchanged dense host RHS;
   - ensure Source is added exactly once by the host path;
   - set dense mode sticky for the remainder of the RK step/trajectory unless a separate formally validated reclosure/restart protocol exists.

Detection after the stage result has already been committed is too late because the Source-injected mode may already have entered the next RK stage state.

## 4. RK4 atomicity

If the first escape occurs at RK4 stage `k2`, the valid route sequence is `SPARSE, DENSE, DENSE, DENSE`. The dense `k2` evaluation uses the same `k2` stage state that the sparse evaluation would have used; no partial sparse result is retained. This makes the guarded integrator equal to the all-dense reference whenever all earlier sparse stages satisfy the certified carrier hypotheses.

The same rule applies when the first escape occurs at `k1`, `k3`, or `k4`: the escaping stage itself is replayed densely before commit, and later stages remain dense.

## 5. Support-preservation lemma

Let `C` contain the current stage state support and current stage Source support. Assume:

- the validated retained Vortex pair closure maps every retained pair sum generated from labels in `C` back into `C`;
- Nyquist masking only deletes labels;
- pressure projection and diffusion act modewise;
- RK stage construction is by linear combinations of already-supported stage states/RHS values.

Then the complete native stage RHS is supported in `C`, and the next stage state remains supported in `C`. Induction over RK stages yields full-step support preservation.

If `Source_stage` has a nonzero coefficient at `q notin C`, the premise fails. The previous exact witness with `p=(1,0,0)`, `q=(0,1,0)`, `u_p=(0,-1,-1)`, `u_q=(-1,0,-1)` produces a nonzero Vortex contribution at `p+q=(1,1,0)` that pressure projection does not remove. Therefore silently discarding Source escape is not generally sound.

## 6. Reference validation

`source_guard_reference.py` implements the contract without host dependencies. `test_source_guard_reference.py` checks:

1. zero Source remains sparse;
2. changing complex coefficients inside a declared support envelope remain valid;
3. a label outside the declared envelope is rejected;
4. dynamic escape triggers dense replay and preserves the escaped coefficient;
5. an escape first appearing at RK4 stage 2 yields `SPARSE,DENSE,DENSE,DENSE` and exactly matches the all-dense witness step;
6. an arbitrarily small nonzero coefficient belongs to exact support, while tolerance mode is explicitly marked approximate.

Local result for this research unit: `6 passed`.

## 7. Integration note

The existing adapter currently owns only the nonlinear callback and has no Source handle. Therefore the dynamic guard cannot be made complete merely by adding a condition inside its existing `__call__` signature. Integration must either:

- pass a Source inspector/handle into a wrapper that controls stage commit, or
- place the guard at the host RK/RHS orchestration layer where the stage Source and pre-stage state are both visible.

This is an integration requirement, not a claim that the pinned host has already been modified or executed.
