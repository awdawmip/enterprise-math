# R059D Stage AR Report

Researcher-ID: `EM-R059D-AR-5B8D24`

Task: `RS-R059D-STAGE-AR-STATEFUL-LINE-SEGMENT-MULTIPATH-ESCAPE-TURN-CLOSURE`

Owner branch: `research/r059d-stage-ar-stateful-line-segment-multipath-escape-turn-closure`

Frozen parent / AQ Driver acceptance: `db226bb787620e6518f9be3c375c82ff3ffdd4ac`

Taskbook source: `69719bbc84842386f1a3005420da3bff284b3c84`

## Primary disposition

`STATEFUL_ALL_PATH_SEGMENT_ESCAPE_DERIVES_NATIVE_TURN_CLOSURE__NO_SINGLE_PATH_SELECTOR_NEEDED`

Scope qualifier:

`ONE_STEP_SIGNED_ORIGIN_SEGMENT_CLASS_ONLY__GENERAL_RADIUS_STATE_LIFT_OPEN`

## What AQ lost

AQ retained only the current cell after seeding. AR restores the object that is supposed to move: the one-step segment edge itself.

The minimal source-free state is

`S=(e,C)`

with fixed global origin `O_E`, primitive radial edge `e=[O_E,p]`, and one of the two elementary triangles `C` incident to `e`. The triangle is a side flag: it records which native side of the segment is being swept.

This is not previous-cell memory. Treating the two triangles incident to `e` as previous/current dual cells would be geometrically and combinatorially mistyped because the segment lies along their shared primal edge.

## Twelve legitimate lifts

Each of the six one-step A1 radial edges has exactly two incident elementary triangles. Therefore there are exactly twelve legitimate lifted states. Both side choices are retained; they are exchanged by reversal.

AQ had six endpoint-incident seed cells per visible endpoint. AR reduces that to the two segment-edge incident cells because it has strictly more native segment information, not because it selects circle-compatible seeds.

## Unique continuation from incidence

For `(e,C)`, the origin-star triangle `C` has exactly two primitive edges through `O_E`. One is the current edge `e`; call the other `e'`.

The next one-step segment state must use `e'`:

- crossing back through `e` merely undoes the selected side sweep;
- crossing the opposite edge loses the fixed-origin primitive one-step segment type because that edge does not contain `O_E`;
- `e'` is the unique remaining fixed-origin one-step continuation.

Let `D` be the other triangle incident to `e'`. Then `NEXT(e,C)={(e',D)}`.

No AK `tau`, no AK orbit membership, no AL A8, no source angle and no circle membership are used.

## AQ DAG obstruction is broken

Every AR side cell belongs to `STAR(O_E)`, so its AQ shell is zero. Since `NEXT` is a singleton,

`FAR_STATE=NEXT`

and every transition has

`Delta SHELL=0`.

Thus AQ's strict `+1` shell DAG is not preserved after the line segment is retained in the state.

## Exact state graph and closure

Index radial edges cyclically by `k mod 6` and side orientation by `d in {+1,-1}`. The transition is exactly

`T(k,d)=(k+d,d)`.

Hence the twelve-state graph is the disjoint union of two directed six-cycles. They are exchanged by reversal.

For every legitimate state:

- minimal positive state return time is 6;
- projected free endpoint minimal return time is 6;
- no equally admissible nonclosing branch survives;
- every legitimate side lift closes;
- reversal gives the inverse traversal.

The endpoint projection is the six A1 anchors in the two opposite cyclic orders.

## Pre-circle one-step length

AR does not need AK `SEG_E(1)` to define one-step length. The independent native invariant is:

`L_pre(e)=1 iff e is a primitive lattice edge incident to O_E`.

Every state and successor has such an edge, so one-step length is preserved exactly. Between-anchor turning state is represented by the side triangle rather than an invented source-continuous non-axis endpoint.

## Jump census

For the full twelve-lift seed family, every exact-J state set is again the same twelve states because `T` is a permutation. The projected free endpoints are always exactly A1.

For one visible starting anchor with both side lifts, the two endpoint indices after J jumps are `k+J` and `k-J mod 6`. The native first return is 6; it is not a tuned jump budget.

## AL support comparison

Post-freeze only: all primary AR states use only O_E, A1 points and origin-star triangles, already contained in `K_E(1)`. Therefore the AL support cap is inactive on this one-step state space for every `r>=1`.

At `r=1`, AR endpoint projection equals the AL canonical frontier. For `r>=2`, increasing the cap does not generate a radius-r state or frontier. A separately justified radius-r segment-state lift is still required.

## AP / AK / AL comparison

Post hoc only:

- AP-REISSUE: exact same visible A1 endpoint cycle; hidden state differs.
- AK radius 1: under accepted signed-origin conjugacy, endpoint order, D6, reversal and period 6 agree.
- AL radius 1: projected endpoint set equals the canonical frontier.
- Higher radius: no AR claim; general radius state lift remains open.

## Checker

Independent deterministic replay result before Git history gate:

`5075 / 5075 PASS`

Digest:

`ba4155ec2ad19084ff536086939fa091d4d9227ca21abe26d7dafdb39b8b6047`

Validation includes:

- all twelve lifts and exact incidence invariants;
- explicit AQ D6 cell rotation;
- reversal conjugacy;
- minimal period 6;
- two independent BFS/DFS implementations for J=0..64;
- larger checkpoints through J=4096;
- signed-origin no-native-zero encoding;
- AL support comparison for r=1..32.

## Boundaries

AR proves the preferred closure theorem only for the signed-origin one-step segment class. It does not provide a radius-r state model for `r>1`; it does not use source geometry; it does not derive or replace AL's general frontier theorem; and it does not consume a later stage.
