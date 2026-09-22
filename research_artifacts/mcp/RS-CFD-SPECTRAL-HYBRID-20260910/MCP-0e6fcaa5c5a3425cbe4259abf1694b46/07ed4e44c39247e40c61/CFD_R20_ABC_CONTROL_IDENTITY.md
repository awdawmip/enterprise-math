# CFD continuation R20: A/B/C forced-fallback control identity and attribution residual

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`
Publication: `TP2-C3B717C14153D5AC45BF`
Researcher: `EM-DIRECT-263462`
State: `EXACT CONTROL-CERTIFICATE THEOREM / NO NATIVE SPEEDUP CLAIM`

## Consumed frontier

This unit consumes R19 at `043e0a563c60dabc141a51387865feb364a4cc6a` without replay. R19 already proved the full-trajectory sparse-attributable ceiling `S <= 1/(1-alpha_bar*f_bar*k*rho/(k*rho+n-k)+h_floor)` and its exact target-speed inversion. The pinned spectralDNS/shenfun/MPI/FFTW A/B/C experiment remains unexecuted in this dialogue.

## BRC / observer typing

`REUSE_APPLIED` for the BRC carrier/observer/provenance discipline. Population: nonlinear RHS calls of one frozen held-out RK4 trajectory, indexed by seed, step, stage and call position. Branch/route labels: guarded sparse route versus dense fallback, plus forced-fallback control. Scientific state retains integer wavevectors and signed/complex amplitudes; it is not replaced by positive mass. Cost carrier retains labeled signed timing differences, not absolute-value savings. Observer: total trajectory elapsed time, paired per-call evaluator time, route labels, and the unattributed residual below. Positive Weighted-BRC recurrence/cancellation theorems are `NOT_APPLICABLE`: timing deltas and Fourier amplitudes are signed/complex observables, and positive mass cannot represent cancellation or causal attribution.

## New theorem: A/B/C matched-control identity

For a fixed held-out case let `T_A>0` be dense baseline total trajectory time, `T_C` the forced-fallback control total time running through the same hybrid wrapper/guard path as B but forcing the final evaluator choice to dense, and `T_B` the guarded hybrid total time. Pair nonlinear calls by frozen call identity. For each call `i`, let `c_i` be forced-fallback evaluator time in C and `b_i` guarded-hybrid evaluator time in B. Let `E` be calls where B takes the sparse route and `F` calls where B falls back dense. Define signed paired gains

`G_E = sum_{i in E}(c_i-b_i)`,
`G_F = sum_{i in F}(c_i-b_i)`,

and retain the non-call attribution residual

`epsilon = (T_C-T_B) - (G_E+G_F)`.

Finally define measured wrapper/control delta `H=T_C-T_A`. Then the exact identity is

`T_B = T_A + H - G_E - G_F - epsilon`.

Proof: by definition of `epsilon`, `T_C-T_B=G_E+G_F+epsilon`; substitute `T_C=T_A+H` and rearrange. No sign assumption is used.

Writing `G_ctrl=G_E+G_F+epsilon=T_C-T_B` gives: (1) B beats A iff `G_ctrl>H`; (2) for target `q>1`, `T_A/T_B>=q` iff `G_ctrl-H >= T_A(1-1/q)`; (3) the target margin has the exact dual evaluation `M_q=G_ctrl-H-T_A(1-1/q)=T_A/q-T_B`, so disagreement is an accounting/call-pairing error; (4) sparse-route causality is stronger than total speedup, so `G_F` and `epsilon` must remain explicit. If fallback calls are claimed to use the identical dense route, nonzero `G_F` is a trajectory/timing/implementation witness. If B and C are claimed to differ only inside the paired evaluator timer, nonzero `epsilon` witnesses omitted route-dependent work. Neither residual may be silently renamed noise; (5) allocation, compilation, cache, guard, setup and fallback effects may be inside or outside the paired timer, but the partition must be declared once.

Thus C is not only a fallback safety test. Under a matched wrapper it directly identifies the wrapper tax `H` and the controlled B-vs-C gain without estimating them from route counts.

## Exact bridge back to R19

Under the additional identification conditions that the forced-fallback paired costs `c_i` are exactly the dense-reference call costs used in R19, `G_F=0`, `epsilon=0`, eligible-call savings obey `c_i-b_i <= alpha_bar*c_i`, and `D=sum_i c_i`, `f=D/T_A`, `w=sum_{i in E}c_i/D`, one has `G_ctrl/T_A <= alpha_bar*f*w`. Hence target speedup `q` requires

`alpha_bar*f*w - H/T_A >= 1-1/q`,

or equivalently

`w >= (1-1/q + H/T_A)/(alpha_bar*f)`

when `alpha_bar*f>0`. Combining this with R18/R19 `w <= k*rho/(k*rho+n-k)` recovers the R19 heterogeneity threshold. The A/B/C identity is therefore a measurable control decomposition, while R19 remains the information-theoretic ceiling when only bounded heterogeneity is known.

## Exact rational consistency certificate

Using only R19's explicitly illustrative, non-native values `q=11/10`, `H/T_A=1/50`, `alpha_bar*f=14/25`: required controlled gain fraction is `g=61/550`; required eligible weighted share is `w=61/308`; normalizing `T_A=1`, the threshold control run has `T_C=51/50`, `T_B=T_C-g=10/11=T_A/q`; inserting `w=61/308` into `w=k*rho/(k*rho+20-k)` gives exactly `rho=549/247` for `k=2` and `rho=61/13` for `k=1`, exactly reproducing R19. A `fractions.Fraction` checker verifies all identities exactly. This is an algebraic certificate, not native timing evidence.

## Native experiment instrumentation consequence

For each A/B/C held-out seed, persist the same frozen seed and RK4 step/stage call IDs; numerical-tolerance comparison; A/B/C total times; B route label for every call; paired B/C evaluator times under one fixed timer scope; `G_E`, `G_F`, `epsilon`, `H`, `M_q`; state/support fingerprints sufficient to detect schedule or trajectory drift; and R19's `T0`, `D`, actual weighted sparse share, paired sparse savings and hybrid-only costs. The forced-fallback override should occur after the shared guard/detection path if C is intended to isolate evaluator routing. Otherwise preserve the difference in `epsilon` rather than declaring it zero.

## Boundary

This theorem does not execute or replace the required pinned spectralDNS/shenfun/MPI/FFTW experiment. It gives an exact fail-closed attribution certificate for that experiment. There is no native speedup/slowdown claim, no theorem about Navier-Stokes stability, and no independent review claim.

## One next unresolved question

On the pinned native host, do the A/B/C held-out RK4 traces satisfy the matched-control contract strongly enough that `G_F` and `epsilon` are negligible/bounded at the declared timing precision, and if so does the measured `M_q` certify any whole-trajectory speedup after wrapper tax?
