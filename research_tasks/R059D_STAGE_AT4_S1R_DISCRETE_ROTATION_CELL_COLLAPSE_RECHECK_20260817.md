# R059D Stage AT4-S1R — Discrete Rotating-Segment Cell Collapse Recheck

Task-ID: `RS-R059D-STAGE-AT4-S1R-DISCRETE-ROTATION-CELL-COLLAPSE-RECHECK`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-at4-s1r-discrete-cell-collapse`

This is a focused correction/recheck of AT4-S1. It must not consume or modify AT4 main.

## 0. Read first / supersession

Read first:

- `driver_reviews/R059D_STAGE_AT4_S1_DISCRETE_CELL_STATE_CORRECTION_20260817.md`
- `driver_reviews/R059D_STAGE_AT4_S1_DRIVER_REVIEW_20260817.md` only for results not superseded by the correction;
- `definitions/ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md`;
- `definitions/ENTERPRISE_CHAMBER_LOCAL_ALGEBRAIC_VECTOR_OPERATIONS_20260817.md`;
- `research_results/R059D_STAGE_AT4_S1/R059D_STAGE_AT4_S1_PROOF.md` from the frozen S1 owner for q-range/incidence certificates.

Freeze current corrections:

- Enterprise geometry is discrete;
- a rotating fixed-length segment occupies exactly one native cell at each trajectory step;
- an algebraic crossing point is a guide/certificate, not a native state;
- an incident-cell set is an admissibility/support certificate, not a simultaneous state;
- if several cell choices are equally legitimate, branch into several trajectories, each trajectory remaining cell-single-valued;
- radius is vector norm, not jump count;
- within this local sector `q=x^2+y^2`;
- reverse minimum-jump paths are secondary realizations only.

The previous S1 result `D(1,1)` with q-range `[9/2,8]` remains a robust radius-3 square-gap hidden witness, but the minimality claim `r_*=3` is reopened.

## 1. Hard objective

Derive the correct **single-cell discrete rotation law** for one fixed chamber `Q0`, one representative fundamental sector `S0`, and one fixed integer vector radius `r`.

Then recompute the historical perimeter cell trace and first hidden interior radius under that corrected state law.

The hard questions are:

1. What is the minimal state of a rotating segment?
2. At an algebraic edge crossing, is the next discrete state the pre-crossing cell, the post-crossing cell, or a stronger stateful rule?
3. Does orientation alone select the next cell?
4. If several choices survive, how do they branch into multiple single-valued trajectories?
5. Under the resulting trajectory family, what is the true first hidden radius in the sector?

## 2. State typing: one cell per trajectory step

Start from candidate state

`S=(r,C,epsilon)`

where:

- `r` is fixed vector radius;
- `C` is exactly one current native cell;
- `epsilon` is local rotation orientation (`+` / `-`, or an equivalent native directed sweep label).

Audit whether this is sufficient.

If a vertex crossing or multi-edge event cannot be resolved from `(r,C,epsilon)`, test the minimal additions:

- incoming/shared edge;
- previous cell;
- local side/sweep flag;
- another strictly incidence-derived state component.

Do not add source angle or historical AK/AL state.

Output:

`R059D_STAGE_AT4_S1R_MINIMAL_DISCRETE_ROTATION_STATE.json`.

## 3. Oriented algebraic arc order without source angle

The algebraic shell remains

`q(x,y)=x^2+y^2=r^2`

inside the fixed two-component chamber sector.

Do not use trigonometric angle as the primary parametrization.

Derive an exact algebraic ordering of cell/edge encounters between the two sector boundary rays, e.g. by a monotone coordinate or rational/algebraic comparison compatible with the shell equation.

For each orientation `epsilon`, produce the ordered sequence of:

- cell interiors traversed;
- edge crossings;
- vertex events;
- boundary start/end events.

The continuous arc is used only to order/locate transitions; the native trajectory states are cells.

Output:

`R059D_STAGE_AT4_S1R_ORIENTED_EDGE_EVENT_ORDER.json`.

## 4. Correct PRE/POST objects are cells

At every transverse crossing of a shared edge `e` between cells `C_a,C_b`, define relative to orientation:

- `CELL_PRE(e,epsilon)` = the cell occupied immediately before crossing `e`;
- `CELL_POST(e,epsilon)` = the cell entered immediately after crossing `e`.

These are the correct discrete UP/DOWN-style candidates.

Do not use edge endpoint vertices as collapse states.

Audit candidate update laws:

1. `PRE_CELL_RULE`: retain `CELL_PRE` at the collapse/update;
2. `POST_CELL_RULE`: move to `CELL_POST` at the collapse/update;
3. `ORIENTED_ENTERED_CELL_RULE`: current state persists until a boundary crossing, then the next state is the cell entered in orientation `epsilon`;
4. any stronger native rule forced by discrete incidence/state.

Be explicit about whether 2 and 3 are actually the same once update timing is typed.

Output:

`R059D_STAGE_AT4_S1R_CELL_PRE_POST_COLLAPSE_THEOREM.json`.

## 5. Mandatory reversibility / orientation covariance

For any deterministic cell transition law `T_epsilon`, require exact reversal covariance:

`T_(-epsilon)=T_epsilon^{-1}`

on the same local trajectory support, modulo boundary start/end conventions.

Also require:

- adjacency: consecutive states share a native edge/allowed incidence;
- no teleportation;
- no simultaneous multi-cell state;
- D6 transport within the declared local scope;
- no graph-distance radius leakage;
- no source-angle oracle.

If a candidate rule violates reversal, reject it.

If two rules are equivalent after a precise before-step/after-step time convention, prove the equivalence rather than treating them as distinct physics.

Output:

`R059D_STAGE_AT4_S1R_REVERSAL_AND_CONTINUITY_AUDIT.json`.

## 6. Vertex events and branching

When the algebraic shell passes exactly through a native vertex shared by more than two cells, a set of incident cells may be admissible geometrically, but the discrete trajectory still must choose one next cell.

Use orientation + current state + minimal additional incidence data to determine the outgoing cell if possible.

If multiple outgoing cells remain equally valid, branch:

`trajectory -> branch_1` and `trajectory -> branch_2` etc.

Each branch must carry exactly one cell at each step.

Freeze no arbitrary tie-breaker.

Output:

`R059D_STAGE_AT4_S1R_VERTEX_BRANCHING_THEOREM.json`.

## 7. Perimeter trace: trajectory support versus instantaneous state

For each radius `r`, define every admissible single-cell oriented rotation trajectory.

Record separately:

- `STATE_t`: exactly one cell at each step of one trajectory;
- `TRACE_TRAJ(r,epsilon,branch)` = union of cells visited by that one full trajectory;
- `TRACE_ALL(r)` = union across all legitimate trajectory branches/orientations, only as a support summary.

Never use `TRACE_ALL` as an instantaneous state.

Determine whether all legitimate trajectories have the same full support. If they do, prove it. If they do not, preserve branch-specific histories.

Output:

`R059D_STAGE_AT4_S1R_DISCRETE_PERIMETER_TRAJECTORIES.json`.

## 8. Recompute first hidden radius under the corrected discrete trace

Use the same local interior policy as S1 for comparability unless a discrete-state contradiction forces a correction:

`FIRST_FULL_CONTAINMENT_IN_ALGEBRAIC_DISK`.

For each admissible trajectory history define branch-specific never-traced interior cells.

Distinguish:

- hidden for every trajectory branch;
- hidden for some branches only;
- traced by at least one branch;
- always traced by all branches.

Recheck radii `r=1,2,3` exactly before extending.

Mandatory checkpoints:

- determine whether a true single-cell rotation already creates hidden cells at `r=1` or `r=2`;
- verify that `D(1,1)` remains hidden at `r=3` whenever no trajectory is allowed to occupy a cell not actually reached by the discrete collapse law;
- determine the exact new minimum `r_*` if it is branch-independent;
- if different legitimate trajectories give different minima, freeze the interval/set of minima rather than selecting one.

Do not assume `r_*=3`.

Outputs:

- `R059D_STAGE_AT4_S1R_FIRST_HIDDEN_RECHECK.json`
- `R059D_STAGE_AT4_S1R_HIDDEN_CENSUS.json`.

## 9. Relation to previous S1 theorem

Classify each S1 claim:

- `PRESERVED_EXACTLY`;
- `PRESERVED_AS_ALGEBRAIC_SUPPORT_CERTIFICATE`;
- `PRESERVED_AS_R3_WITNESS_NOT_MINIMALITY`;
- `SUPERSEDED_BY_SINGLE_CELL_STATE`.

At minimum re-audit:

- cell q-range theorem;
- exact arc/cell incidence theorem;
- r=3 square-gap witness;
- r=3 minimality;
- endpoint PRE/POST negative result;
- set-valued incident-cell state conclusion.

Output:

`R059D_STAGE_AT4_S1R_S1_SUPERSESSION_MAP.json`.

## 10. Deterministic validation

After structural proofs freeze, replay at least radii `1..64`, with larger checkpoints if compressed.

Validate:

- every trajectory state is one cell;
- every consecutive state is incidence-valid;
- oriented event order;
- reversal covariance;
- all branch points;
- no state-set substitution;
- hidden histories per branch;
- r=1..3 minimality recheck;
- D(1,1) square-gap certificate;
- no native zero;
- no cross-chamber arithmetic;
- AT4 main and prior-stage immutability.

Proof dominates checker evidence.

## 11. Stop condition

Stop for Driver review.

Do not consume AT4 main and do not open a later stage automatically.
