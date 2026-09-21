# CFD trajectory verification checkpoint: frozen native-run manifest

Task: `RS-CFD-TRAJECTORY-VERIFY-20260910`  
Target research task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Researcher: `EM-CFD-VFY-6D3A91`  
Claim: `CLM-CFDVFY-6D3A91-20260921-2058`  
State: `CONTINUATION_REQUIRED / MANIFEST_FROZEN / ORIGINAL HOST NOT RERUN`

## Scope consumed

This unit consumes, without replaying prior research:

- R15 three-arm experimental design at `283a135c7a8b4cd7830cee4b13e05ca07531011f`;
- independent R15 design audit at `d152a77e9cf122d4c7df98ded4c9281e575027f2`.

The preceding verifier required the tie policy and order sequence to be frozen before any new native timing observation. This unit performs exactly that bounded step. No spectralDNS/shenfun/MPI/FFTW host execution is claimed.

## Frozen protocol

The next native run is fixed at 24 scheduled same-trajectory A/B/C triplets (72 timed arm executions), arranged as four complete six-order cycles. A is the unmodified dense FFT baseline, B is automatic guarded hybrid routing, and C is the same guarded wrapper forced to dense fallback with sparse execution disabled.

The order sequence is generated before data by a deterministic SHA256 ranking rule whose seed material is bound to the immutable R15 design, immutable verifier audit, task id and this claim. Each cycle contains every A/B/C permutation exactly once. The frozen cycle orders are:

1. `BAC, ACB, CAB, ABC, CBA, BCA`
2. `CBA, BCA, ABC, CAB, ACB, BAC`
3. `CAB, ABC, BAC, ACB, BCA, CBA`
4. `BAC, CBA, CAB, ACB, BCA, ABC`

This produces, over 24 triplets, exactly 8 appearances of each arm in each ordinal position and exactly 12 occurrences of each directed pairwise precedence relation. The order-sequence digest is `115093dc97d1c4360294696aba32e79061c74a170f8701599acb5d3d4e6bb328`.

The hash ordering is a **predeclaration mechanism**, not a claim that timing observations become statistically random merely because SHA256 is used. Sign-test interpretation still depends on the experiment's sampling/stability assumptions; raw order and timestamps remain mandatory.

## Tie and inference policy

The verifier-preferred fixed-n rule is now frozen:

- all 24 scheduled triplets remain in the analysis;
- success for a contrast means strictly `delta > 0 ms`;
- an exact tie (`delta == 0`) is a non-success;
- ties are not deleted, replaced, resampled or conditioned away;
- no adaptive repeat extension is allowed.

The confirmatory contrasts remain `A-B` (end-to-end) and `C-B` (effect of sparse-route permission inside the guarded wrapper). Bonferroni alpha is 0.025 per one-sided gate. Exact binomial arithmetic gives the fixed threshold `18/24` for each gate, with tail probability `190051/16777216 = 0.011327922344207764`.

The `A-C` all-fallback comparison remains a diagnostic veto. At n=24, the least one-sided alpha <= 0.05 positive count is `17/24`, with tail `536155/16777216 = 0.03195732831954956`; reaching this threshold blocks sparse-speed attribution until the unexplained wrapper/fallback advantage is diagnosed.

The directional margin is explicitly frozen at `epsilon = 0 ms`. Therefore even a passing sign result supports only a directional-frequency statement. It does not establish a minimum practically material speedup. No nonzero engineering epsilon is invented in this unit.

## Added fail-closed cost gate

R13 showed that per-repeat signs cannot silently discard guard/setup/compilation costs. The manifest therefore adds a non-inferential declared-horizon gate: any setup or compilation intentionally performed outside the timed triplets must still be measured per arm and charged to that arm's full 24-triplet horizon. Performance acceptance requires both fully charged inequalities `A_horizon > B_horizon` and `C_horizon > B_horizon` in addition to the two sign gates.

This does not replace the paired sign tests; it prevents a protocol in which steady-state signs pass while one-time costs erase the benefit over the declared reuse horizon.

## Correctness and attribution gates

The manifest fails closed unless every triplet uses identical deterministic state/Source and solver parameters across A/B/C, the pinned solver semantics and task numerical tolerances are resolved from immutable canonical evidence, and the required trajectory diagnostics pass. B must execute at least one sparse nonlinear call in every scheduled triplet used by the confirmatory design; C must execute exactly zero sparse calls. A longitudinal-Source negative control may be retained diagnostically but cannot be pooled into positive-control performance gates.

Required raw evidence includes order/timestamps, setup/allocation/compilation/RK4/total timings, per-call route/support, guard/sparse/fallback costs, velocity and modified-pressure comparisons, Hermitian/divergence/energy/fallback diagnostics, and shadow dense numerical counterfactuals kept outside the production timing path.

`C-B` is deliberately interpreted as the effect of **allowing the sparse route inside the guarded wrapper**. It is not promoted to a pure sparse-convolution arithmetic effect unless cache/allocation/control-state differences are separately excluded.

## Machine verification

A stdlib-only checker independently regenerates the hash-frozen schedule, verifies complete-cycle membership, per-cycle/global position balance and pairwise-precedence balance, recomputes the exact sign thresholds, verifies fixed-n tie handling, and exercises fail-closed synthetic acceptance cases.

Local validation completed successfully:

- manifest checker: PASS;
- synthetic fail-closed acceptance tests: PASS;
- Python `py_compile`: PASS;
- manifest and verification JSON parse: PASS.

Artifact SHA256 values at local validation time:

- `native_run_manifest.json`: `6d84eece01730a17f7374ca442601731e313e827515fd6f61544d6fb7ce914af`
- `manifest_verification.json`: `a1c399bcebbdb15ef111c8fad1a1fd5da18611f028eae13538e0859795bcd340`
- `RS_CFD_RUN_MANIFEST_6D3A91.py`: `055214b3a50e48540144d93ec02dc47d52ad3c738d000f167a1b00728dfe77b5`

## Boundary and next action

This is a protocol-freeze checkpoint only. It does not rerun the original host and does not establish native speedup, generic CFD/industrial acceleration, a continuous-PDE theorem, mathematical acceptance, Working Truth or canonical promotion.

Next: on an already provisioned pinned spectralDNS/shenfun/MPI/FFTW host, execute this manifest exactly, without adaptive reordering or tie replacement. Preserve the full correctness/cost record and fully charged horizon costs, then return the immutable native checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review. Neither CFD task should be marked DONE before that review.
