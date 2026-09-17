# A3 Shell Partial-Move Scale Coherence Revision — Research Return

Task-ID: `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`  
Publication-ID: `TP2-D2D715EB36415B0CA0C5`  
Researcher-ID: `EM-A3SCR-7A41D2`  
Claim-ID: `claim-A3SCR-autoA-20260917-064030-7a41d2`  
Execution-record: `ER-61A4EAB6F40E0298D44B`  
Result-ID: `RR-9FF7F84F01C577774649`

Verdict: `PASS_AT_RESEARCHER_STRENGTH / EXACT_STATE_LEVEL_CLASSIFICATION / PENDING_INDEPENDENT_DRIVER_REVIEW`.

## Exact result

For adjacent scales `n+1 -> n`, prefix depth `d`, lower aligner `g_-`, upper aligner `g_+`, and `q=n-d+1`, the two actual carrier maps on `B_n` are

- upper-then-restrict: `g_+` on shells `r>=q+1`, identity on `r<=q`;
- restrict-then-lower: `g_-` on shells `r>=q`, identity on `r<=q-1`.

Their exact state-level radial defect `K=L U^{-1}` is shell-labeled by

- `e` for `r<q`;
- `g_-` for `r=q`;
- `g_- g_+^{-1}` for `q<r<=n`.

This separates the support-transition defect from the overlap frame phase. The parent single double coset `H g_- g_+^{-1} H` retains only overlap phase and cannot classify the scale square.

For legal aligner cosets `A_n=H g_-`, `A_{n+1}=H g_+`, the exact representative-free defect is the finite relation of all such shellwise operators under `h_-,h_+ in H`. A shellwise double-coset profile is a valid projection, but it is weaker than the exact relation because it can erase the requirement that one global residual `H` element act coherently across the restricted state.

Raw universal path equality holds iff the radial defect is identity: for depth 1 iff `g_-=e`; for depth at least 2 iff `g_-=g_+=e`.

For the global residual-`H` quotient on rigid states, exhaustive exact checking through `n<=4` verifies the closed criterion: at `n=1,d=1`, iff `g_- in H`; for `q>=2,d=1`, iff `g_-=e`; for `q>=2,d>=2`, iff both aligners are identity; for `q=1,n>=2`, iff `g_- in H` and `g_+=e`.

## Frozen regression and no-go

For the required `n=2,d=2,g_-=g_+=(23)` counterexample and `p=(1,-1,0,0)`:

- upper-then-restrict leaves `p` fixed;
- restrict-then-lower sends it to `(-1,0,1,0)`;
- the two are not residual-`H` equivalent;
- the exact radial double-coset profile is `S1:C2, S2:C0` while the old frame-only defect is only `C0`.

The identity-aligner positive control also has old frame-only defect `C0` and does commute. Therefore no invariant depending only on the old adjacent frame double coset can classify the actual state-level square.

## Structural repair

More generally, if a radial action at scale `n` is a shell-label function `alpha_n(r)`, exact restriction naturality holds iff `alpha_{n+1}(r)=alpha_n(r)` for every retained shell. Fixed absolute radial cutoffs are natural; fixed depth from the moving boundary shifts support and is generally non-natural. Support/domain data is therefore part of the morphism and must remain in the BRC carrier.

## Dependent-observable audit

The fixed-`H` algebra `C2*C2={C0,C2}` survives only at frame-phase strength. `DEFECT_BIRTH_RADIUS`, `STABILIZATION_RADIUS`, and boundary-to-bulk signatures must use `K`, the representative-free radial relation, or a separately proven operation-safe projection. The A2 orientation-leakage conclusion remains valid: orientation-sensitive observations cannot silently quotient by `H`.

## Reproducibility

Exact checker: `research_checks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917.py`  
Result package: `research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md`  
Certificate: `research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/certificate.json`

Local checker result: `PASS`; it evaluated 5,760 exact raw state-map cases and 5,760 exact global residual-`H` quotient cases for all `G x G`, all `1<=d<=n<=4`, replayed the frozen counterexample, checked the frame-only no-go, verified the alternating depth-2 profiles through transition `n=6`, and checked absolute-cutoff naturality. The general support-mask theorem is proved directly, not inferred from the finite census.

Checker SHA-256: `d9b9f6002aca78157a3548d7a2b78a44a05a0952e69ab4ff0abfdbdec8ab4a9c`  
Result SHA-256: `2d68fb4c8b9b3edc61a23fdf0065688ed99ec387f479fccb8fdb0cf1a7089a7a`  
Certificate SHA-256: `6d9efb0cc1435cd5528c2c0ab38ddb7206df20783adc8c0c37cc604a25663788`

## Boundary and next control action

Hard-target disposition: `A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED` at researcher strength.

No Working Truth, Foundation, ontology, or independent-review authority is asserted. The next control-plane action is independent Driver review of this revision result. The result should not be marked final task completion until that review accepts the replacement theorem at the claimed strength.
