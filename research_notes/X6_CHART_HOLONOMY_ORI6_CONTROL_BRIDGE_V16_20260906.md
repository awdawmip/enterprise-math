# X6 rotation V16: chart-holonomy parity as the unique compositional Ori6 control bridge

Status: `FREE_RESEARCH / EXACT CONDITIONAL BRIDGE + UNIQUENESS / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_20_SLICE_FRAME_CONNECTION_HOLONOMY_V2_20260906.md`;
- `X6_ORI6_TRIADIC_PHASE_REVERSAL_V13_20260906.md`;
- `X6_PHASE_CHIRALITY_D12_DYNAMICS_V14_20260906.md`;
- `X6_ORI6_CONTROL_LEDGER_V15_20260906.md`.
Checker: `experiments/x6_chart_holonomy_ori6_bridge_v16_20260906/check_chart_holonomy_ori6_bridge.py`.

## 1. The candidate source of the V15 control bit

V15 isolates a binary event-control input

`u_t in C2`

for local ADVANCE versus PHASE_REVERSAL, and proves local symmetry alone does not determine it.

Separately, the all-20 three-axis chart atlas has a canonical Johnson-graph connection with holonomy group

`Hol = S3`.

The simplest chart triangles split exactly into:

- 60 flat loops with identity holonomy;
- 60 four-axis loops with transposition holonomy.

This suggests a sharply typed question:

> if a declared multi-chart/event context is allowed to feed one **compositional binary control** into the local Ori6 dynamics, is there a canonical map from chart holonomy to that control?

The answer is yes and unique, conditionally on making such a bridge at all.

## 2. Unique nontrivial group homomorphism S3 -> C2

Let

`c:S3 -> C2`

be required to respect loop concatenation:

`c(h2 h1)=c(h2)+c(h1) mod2`.

Any 3-cycle has order three, while C2 has no nonidentity element of order three, so every 3-cycle must map to zero.

A nontrivial homomorphism must therefore send each transposition to one. Since 3-cycles and transpositions generate S3, the map is unique:

`c(h)=sgn(h) mod2`.

Equivalently

`S3^ab ~= C2`.

Hence the only nontrivial compositional binary charge carried by chart holonomy is permutation parity.

This is a theorem about the declared atlas connection. It does not yet assert that the charge is a physical event trigger.

## 3. Exact match to local Ori6 charge

V13/V14 give the local signed phase group

`D12=<Q,O | Q^6=1, O^2=1, OQO=Q^-1>`.

Projection to unsigned three-axis labels gives

`pi:D12 -> S3`

with

`pi(Q)=rho`, a 3-cycle,

`pi(O)=tau`, a transposition.

The local V14/V15 reversal charge is

`chi_loc:D12 -> C2`

with

`chi_loc(Q)=0`,

`chi_loc(O)=1`.

Therefore on generators, and hence on all of D12,

`chi_loc = sgn o pi`.

So the following diagram commutes:

`D12 --pi--> S3`

` |           |`

`chi_loc      sgn`

` |           |`

` v           v`

`C2  ==      C2`.

Under the V13 frame embedding this is also the restriction of the global V8 `Ori6` charge.

Thus chart-holonomy parity and local odd-event parity are not merely two unrelated binary labels: they are the same quotient after the signed local lift is supplied.

## 4. Flat versus curved Johnson triangles

For the canonical `J(6,3)` replacement connection:

- common-pair triangular loops have `h=1`, so `sgn(h)=0`;
- four-axis triangular loops have `h` equal to one transposition of the base chart, so `sgn(h)=1`.

Therefore a bridge law

`u(loop):=sgn(Hol(loop))`

would assign

- `u=0` to all 60 flat chart triangles;
- `u=1` to all 60 curved chart triangles.

Because sign is conjugacy invariant, this bit is independent of the arbitrary slot labeling chosen on the base triangular template.

Because sign is a homomorphism, concatenating chart loops adds the control bits mod two.

## 5. A transposition holonomy has exactly two local signed lifts

Fix one local signed C6 generator Q on the base three-axis chart and one unsigned transposition

`tau=(ij) in S3`.

The projection

`pi:D12 -> S3`

has kernel

`{1,Q^3} ~= C2`.

Hence the fiber over tau has exactly two signed involutions.

In the canonical gauge they are:

1. the pair-only swap `P_ij`, which leaves the third selected axis unflipped;
2. the V13 triadic phase reversal

`O_ij|k = Q^3 P_ij`,

which flips the third selected axis as well.

They have the same unsigned chart transposition and the same Ori6 charge, but different triadic/path semantics.

## 6. P000 triadic common-node condition selects the lift uniquely

For the pair-only lift, the two swapped shell tokens each have INNER/OUTER shortest paths while the third token is fixed. It is not a synchronous three-token shell-to-shell atomic scatter.

For the V13 lift, all three tokens move by two primitive steps. The third token has unique pivot midpoint, and the joint common-node criterion uniquely selects the common-pivot triadic path.

Therefore, once an **odd chart holonomy is declared to be realized as a P000 triadic atomic event**, the signed lift is no longer two-valued:

`TRANSPOSTION HOLONOMY + TRIADIC COMMON-NODE EVENT`

`-> UNIQUE V13 PHASE-REVERSAL LIFT`.

In the four-twist gauge-covariant version, the edge sign beta is fixed by the current twist coordinate exactly as in V13.

## 7. Conditional chart-loop control law

The complete conditional bridge is therefore:

1. a declared chart/event loop produces holonomy `h in S3`;
2. binary control is forced to

`u=sgn(h)`

if a nontrivial compositional binary bridge is wanted;
3. for `u=0`, no Ori6 change is requested by the bridge;
4. for `u=1`, `h` is in the odd S3 coset; on a simple curved triangle it is a specific transposition identifying a pointed pair;
5. the triadic common-node rule selects the unique V13 signed phase-reversal lift of that transposition.

Thus a multi-chart loop context can supply both:

- **whether** reversal charge is one;
- **which local pair** the odd transposition acts on.

No arbitrary standalone binary switch or unordered-pair selector is then required at that event.

## 8. Critical type boundary: observer holonomy is not automatically physical dynamics

The Johnson connection was derived as a chart/frame **observer transport**. Its nontrivial holonomy does not by itself move a native Cell or enact a physical frame event.

Therefore the statement

`CHART LOOP HOLONOMY -> PHYSICAL PHASE REVERSAL`

is **not** derived here as a P000 law.

What is proved is the stronger conditional uniqueness statement:

> if an admitted multi-chart relation/event context is required to feed a nontrivial compositional binary control into Ori6 dynamics, the control must be holonomy parity; and if an odd transposition holonomy is to be realized through a P000 triadic common-node event, its signed lift is the V13 phase reversal.

A future physical bridge must still explain when a chart/context loop corresponds to a real relational event rather than bookkeeping.

## 9. Pure spatial channel transport cannot supply this charge under current symmetry

The existing channel-frame flat-transport theorem proves that, under translation invariance, deterministic permutation transport and full S6 covariance, pure spatial channel transport is identity.

So the present nontrivial control cannot be attributed to bare translation alone without breaking those assumptions.

The possible source is necessarily richer relational context: chart switching, active triadic/internal state, symmetry breaking, field coupling, or retained event/path history.

This is consistent with V15's conclusion that the trigger cannot be derived from one isolated local phase state.

## 10. Exact synthesis with V15

Under the conditional bridge, V15's recurrence becomes

`r_{t+1}=r_t+epsilon_t mod6`,

`epsilon_{t+1}=(-1)^(sgn(h_t)) epsilon_t`,

where `h_t` is the declared chart/event-loop holonomy associated with event t.

Then

`epsilon_t = epsilon_0 (-1)^(sum_{s<t} sgn(h_s))`.

The accumulated chart-holonomy parity is exactly the local/global Ori6 ledger on this coupled interface.

This gives a concrete multi-context source for the V15 control bit without changing the fact that raw event/path provenance remains richer.

## 11. Current frontier

Closed conditionally:

- unique nontrivial compositional binary readout `S3 -> C2`;
- exact equality of chart-holonomy parity and restricted local Ori6 charge;
- two signed lifts of one transposition and unique triadic common-node lift;
- deterministic control/lift map for simple curved chart triangles once chart holonomy is admitted as event context.

Still open:

1. physical/Foundational admission of chart/context holonomy as a real event trigger;
2. multi-Cell mechanism producing or coupling such chart loops;
3. rates/weights when several event contexts compete;
4. application-specific meaning in physical/PDE/number-theory bridges.

No Foundation promotion or external novelty claim is made.
