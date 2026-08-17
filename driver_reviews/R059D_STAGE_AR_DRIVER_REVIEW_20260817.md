# R059D Stage AR — Driver Review

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Stage: `RS-R059D-STAGE-AR-STATEFUL-LINE-SEGMENT-MULTIPATH-ESCAPE-TURN-CLOSURE`

Owner branch: `research/r059d-stage-ar-stateful-line-segment-multipath-escape-turn-closure`

Taskbook source: `69719bbc84842386f1a3005420da3bff284b3c84`

Frozen owner head: `745e23bcfea34514fe4a01de5c7bfbf00401cf67`

Researcher-ID: `EM-R059D-AR-5B8D24`

## Driver disposition

`DRIVER_ACCEPTED__ONE_STEP_STATEFUL_SEGMENT_INCIDENCE_TURN_CLOSURE_PROVED__GENERAL_RADIUS_LIFT_OPEN`

Accepted primary theorem, with strict scope:

`STATEFUL_ALL_PATH_SEGMENT_ESCAPE_DERIVES_NATIVE_TURN_CLOSURE__NO_SINGLE_PATH_SELECTOR_NEEDED`

Scope qualifier:

`ONE_STEP_SIGNED_ORIGIN_SEGMENT_CLASS_ONLY__GENERAL_RADIUS_STATE_LIFT_OPEN`

## What is accepted

1. In the one-step signed-origin class, the minimal justified pre-circle line-segment state is

   `S=(e,C)`

   with fixed global `O_E`, primitive radial edge `e=[O_E,p]`, and `C` one of the two elementary origin-star triangles incident to `e`.

2. The two side triangles are both retained. They are not a hidden single-path selector: they are the two legitimate local sweep-side lifts of the same visible radial edge, and reversal exchanges them.

3. There are exactly twelve legitimate lifted states: six one-step radial edges times two side choices.

4. For `(e,C)`, native incidence alone leaves one forward continuation after excluding immediate reversal across `e` and the triangle edge not incident to the fixed endpoint. The successor uses the unique other `O_E`-incident edge of `C`, then carries the side state into the triangle across that edge.

5. The resulting transition law is

   `T(k,d)=(k+d,d)`, `k mod 6`, `d in {+1,-1}`.

   Hence the state graph is exactly two directed six-cycles exchanged by reversal.

6. Both side lifts close. No equally admissible nonclosing branch remains in this one-step state model. The projected free-endpoint orbit is exactly the six signed-origin one-step anchors in opposite cyclic orders.

7. AQ's cell-only strict-shell law does not survive this state lift: every AR primary side cell lies in `STAR(O_E)`, so every transition has `Delta SHELL=0`. Therefore `CELL_ONLY_ESCAPE_DAG` is not a theorem about a stateful one-step segment.

8. A pre-circle one-step length meaning is independently available here: `L_pre(e)=1` iff `e` is a primitive lattice edge incident to `O_E`. This is preserved without AK `SEG_E(1)` membership.

9. The AL support cap is inactive on this one-step state space and therefore is not responsible for the closure theorem.

## Important Driver typing restriction

Do **not** overstate Stage AR as a general escape-to-circle theorem.

At `r=1`, the stateful candidate relation collapses to a singleton once the side triangle is part of the state. Consequently `FAR_STATE` is vacuous as a selector: the closure theorem is primarily a **native incidence-turn theorem for one primitive radial segment**, not evidence that the same shell-maximizing escape mechanism automatically determines all radii.

Freeze:

`AR_R1_CLOSURE_IS_INCIDENCE_DERIVED`

but not:

`AR_ESCAPE_RULE_SOLVES_GENERAL_ENTERPRISE_CIRCLE`.

The general-radius object has not yet been defined pre-circle. In particular, AR does not establish what replaces the primitive edge `e` when a segment has more than one primitive unit, nor what the correct native footprint/side state is during a turn.

## Verification

Checker:

- `5075 / 5075 PASS`
- digest `ba4155ec2ad19084ff536086939fa091d4d9227ca21abe26d7dafdb39b8b6047`
- BFS/DFS equality for required `J=0..64`
- larger checkpoints through `J=4096`
- SCC count `2`
- minimal state/endpoint period `6`
- D6/reversal covariance
- no native zero
- no AK `tau` / `SEG_E`, AL A8, or source-circle leakage in primary transitions

External history compare from `db226bb787620e6518f9be3c375c82ff3ffdd4ac` to the AR owner branch shows only the AR taskbook/result files were added; no prior-stage result was modified or deleted.

## Next research boundary

The next hard problem is not another one-step refinement. It is:

`DEFINE_OR_REFUTE_A_PRE_CIRCLE_GENERAL_RADIUS_LINE_SEGMENT_STATE_THAT_EXTENDS_AR_R1`.

A valid general-radius state must be derived from native incidence and the signed-origin axis anchor meaning, must reduce exactly to AR at `r=1`, must retain every legitimate lift/path, and may not use AK orbit membership, AL A8, source geometry, or the old circle as its definition.

The primary diagnostic should include local triangle-flip / strip-sweep possibilities because, for a multi-unit segment, crossing a triangular cell can change a primitive edge-chain footprint by `1 <-> 2` edges. Whether this is the native form of the user's earlier "up/down length drift" intuition is open and must be tested rather than assumed.

Stage AR is accepted and frozen at the owner head above.
