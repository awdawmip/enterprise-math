# R059D Stage AT4-S1 — Discrete Cell-State Correction

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`

Supersedes the collapse/state semantics in:
- `driver_reviews/R059D_STAGE_AT4_S1_DRIVER_REVIEW_20260817.md`
- `research_results/R059D_STAGE_AT4_S1/R059D_STAGE_AT4_S1_ALGEBRAIC_COLLAPSE_DIRECTION_THEOREM.json`

The algebraic q-range computations and the existence of the radius-3 square-gap witness remain valid as stated below, but the earlier interpretation of `EXACT_ALGEBRAIC_CROSSING + INCIDENT_CELL_SET` as the native rotating state is not canonical.

## 1. User correction

Enterprise geometry is discrete. When a fixed-length segment rotates, the native state at each discrete step must be **one native cell**.

An exact algebraic crossing point on a cell edge is a local algebraic certificate for where the ideal vector shell crosses the discrete carrier. It is not itself a native rotating state.

Likewise, the set of all incident cells is an incidence/support certificate. It is not a valid simultaneous cell state.

Freeze:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CELL_PER_TRAJECTORY_STEP`.

`ALGEBRAIC_CROSSING_POINT = GUIDE/CERTIFICATE_NOT_NATIVE_STATE`.

`INCIDENT_CELL_SET = ADMISSIBILITY/SUPPORT_CERTIFICATE_NOT_SIMULTANEOUS_STATE`.

## 2. All-path retention is path branching, not set-valued state

The project rule that all equally legitimate paths are retained does not mean that one trajectory occupies several cells at the same step.

If a local crossing admits more than one equally justified discrete collapse, branch into multiple trajectories:

`trajectory_1: ... -> C_a -> ...`

`trajectory_2: ... -> C_b -> ...`

Each trajectory remains single-valued in cell state.

Freeze:

`ALL_LEGITIMATE_PATHS_RETAINED != MULTIPLE_CELLS_IN_ONE_STATE`.

`AMBIGUITY_BRANCHES_TRAJECTORIES__EACH_TRAJECTORY_IS_CELL_SINGLE_VALUED`.

## 3. Correct collapse candidates are cell-level, not vertex-level

The prior AT4-S1 comparison of PRE/DOWN versus POST/UP at integer **vertices** answered the wrong discrete question.

For an oriented algebraic shell crossing a shared edge between two native cells, define instead:

- `CELL_PRE`: the cell occupied immediately before the oriented crossing;
- `CELL_POST`: the cell entered immediately after the oriented crossing.

The true collapse question is which one-cell state represents the discrete rotating segment at the update/collapse event, or whether both rules remain as separate trajectory branches.

Do not substitute edge endpoints for these cells.

Freeze:

`PRE_POST_ENDPOINT_PROXY_THEOREM = RETAINED_ONLY_AS_NEGATIVE_ENDPOINT_RESULT`.

`NATIVE_COLLAPSE_DIRECTION_QUESTION = CELL_PRE_VS_CELL_POST_OR_STRONGER_ORIENTED_CELL_RULE`.

## 4. Orientation/state is mandatory

A rotating segment carries orientation/sweep information. A local state must therefore include enough data to distinguish the two directed traversals of the same cell sequence.

Minimum candidate state:

`S=(rho, C, epsilon)`

where `rho` is the fixed vector radius, `C` is the current native cell, and `epsilon` is one of the two local rotation orientations.

If previous-cell or incoming-edge data is necessary to resolve vertex/multi-edge events, prove that necessity and extend the state minimally.

Reversal must invert the discrete transition:

`T_(−epsilon) = T_epsilon^{-1}`

on every regime where a deterministic transition is claimed.

## 5. Status of the radius-3 hidden witness

The cell

`D(1,1)`

still has exact squared-norm interval

`[9/2,8]`

and hence lies strictly in the integer-square gap

`4 < q(D(1,1)) < 9`.

Therefore no exact integer-radius algebraic arc at radii 1, 2, or 3 intersects this cell, while the radius-3 algebraic disk fully contains it.

So `D(1,1)` remains a robust **hidden witness by radius 3** under any discrete perimeter rule that selects one cell from actual algebraically admissible rotating-cell states rather than inventing nonincident cells.

However, the previous claim that radius 3 is the **minimal** hidden radius used historical trace support in which all incident cells were retained. That trace can be larger than a true single-cell rotating trajectory.

Therefore reopen minimality:

`FIRST_SECTOR_HIDDEN_RADIUS <= 3`.

`D(1,1)_IS_A_ROBUST_HIDDEN_WITNESS_AT_R3 = true`.

`FIRST_SECTOR_HIDDEN_RADIUS_EQUALS_3 = REOPENED_PENDING_SINGLE_CELL_ROTATION_RECHECK`.

In particular, radii 1 and 2 must be re-audited under actual single-cell trajectories.

## 6. Consequence for AT4 main

AT4 main must not use `all incident cells` as the perimeter-state law.

It may use exact algebraic incidence to identify the local transition boundary and admissible neighboring cells, but it must construct the perimeter as one or more **cell-single-valued oriented trajectories**.

Perimeter support may later be the union of cells visited across a full trajectory or across all legitimate trajectories, but support union must never be confused with instantaneous state.

## 7. Routing

Open a focused correction stage before AT4 main consumes the old collapse conclusion:

`RS-R059D-STAGE-AT4-S1R-DISCRETE-ROTATION-CELL-COLLAPSE-RECHECK`.

Hard targets:

1. derive the minimal oriented cell state;
2. derive CELL_PRE/CELL_POST transitions from exact algebraic crossings;
3. decide whether a canonical one-cell collapse rule exists;
4. if not, retain multiple single-cell trajectories;
5. recompute historical perimeter traces and the first hidden radius under the corrected discrete state semantics;
6. preserve the radius-3 square-gap witness as a checkpoint, not as pre-imposed minimality.
