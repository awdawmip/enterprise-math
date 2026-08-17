# R059D Stage AP REISSUE — Signed-Origin One-Step Segment Sweep, Collapse Direction, and Orbit Closure

Task-ID: `RS-R059D-STAGE-AP-REISSUE-SIGNED-ORIGIN-ONE-STEP-SEGMENT-COLLAPSE-CLOSURE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-ap-reissue-one-step-segment-collapse`

Supersedes the misinterpreted task:

`research_tasks/R059D_STAGE_AP_SIGNED_ORIGIN_LENGTH2_COLLAPSE_DIRECTION_ORBIT_CLOSURE_20260817.md`

Reason: the user clarified that the rotating segment is **one primitive step away from the glued origin**, not primitive length 2.

## 0. Frozen signed-origin foundation

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`

Freeze:

`+1 ≡ -1 ≡ O_E`

`0` is not a native Enterprise coordinate.

One positive primitive step from origin reaches `+2`; one negative primitive step reaches `-2`.

Therefore the one-step axis anchors are

`A1 = {`
`(2,1,1), (-2,1,1),`
`(1,2,1), (1,-2,1),`
`(1,1,2), (1,1,-2)`
`}`.

This task must never reinterpret these as length-2 anchors.

## 1. User working hypothesis — corrected

The user’s corrected intuition is:

> A segment whose endpoint is one primitive step from the signed origin appears, under the naive discrete picture, to sweep a full turn by visiting only the six axis anchors in `A1`. But the continuous turning/collapse mechanism is probably not that simple. There may be non-axis competition fibers between axis encounters. A small but nonzero set of source orientations may admit an upward/outward collapse to larger mixed states; if that happens the segment length grows and a fixed-length full orbit cannot close. A downward/inward collapse, together with a local axis-completion rule when the sweep encounters an Enterprise axis, may be the mechanism that preserves the one-step length class and closes the full turn.

Treat this as a hypothesis to test, not a result.

Freeze hypothesis labels:

`NAIVE_ONE_STEP_ORBIT = SIX_AXIS_ANCHORS_ONLY`

`UPWARD_COLLAPSE_CANDIDATE = POSSIBLE_OVERLENGTH_MIXED_STATE`

`DOWNWARD_COLLAPSE_WITH_AXIS_COMPLETION = CANDIDATE_ONE_STEP_CLOSURE_MECHANISM`

Exact counterexamples must supersede any false part.

## 2. Mandatory six mixed states

The task MUST analyze the user-specified sextet

`M_UP = {`
`(3,-3,1),`
`(1,-3,3),`
`(-3,1,3),`
`(-3,3,1),`
`(1,3,-3),`
`(3,1,-3)`
`}`.

Do **not** assume these are legitimate one-step circle points.

Their role to test is specifically whether they arise as:

1. upward/outward collapse competitors of a one-step continuous orientation;
2. overlength post-collapse states;
3. boundary/tie artifacts only;
4. states of zero source-fiber measure;
5. or something else.

Under the allowed auxiliary bridge

`DEC_SIGNED(O_E)=0`

`DEC_SIGNED(±n)=±(n-1)` for `n>=2`,

these decode to

`{(2,-2,0),(0,-2,2),(-2,0,2),(-2,2,0),(0,2,-2),(2,0,-2)}`.

By contrast `A1` decodes to the six auxiliary radius-1 axis anchors.

This shell mismatch is a primary diagnostic: determine whether it is exactly the algebraic signature of upward length inflation.

## 3. Hard questions

The stage must answer, in order:

1. **Does a one-step continuous sweep have non-axis native competition states at all?**
2. **Do the six states in `M_UP` occur with positive source angular/fiber measure, or only at isolated ties?**
3. **If UP selects `M_UP`, does the operational native segment length strictly exceed one step?**
4. **What is the exact DOWN competitor on the same pre-collapse input?** Derive it; do not guess it from the desired answer.
5. **What exactly means “遇到数轴补齐长度” as a local target rule?**
6. **Does DOWN + axis completion produce a closed one-step full orbit?**
7. **Is the resulting orbit really only the six axis anchors, or are additional legitimate one-step states required?**
8. **Is DOWN necessary for closure within a clearly stated admissible local policy class?**

## 4. Stage A — native one-step segment class

Define the one-step segment without using source Euclidean distance or the desired collapse rule.

At minimum specify:

- fixed center `O_E=(±1,±1,±1)`;
- endpoint state;
- sector/orientation state;
- the operational invariant `L_E=1 primitive step`;
- all six axis anchors in `A1` as the same length class;
- signed-origin reversal and D6 covariance.

Legacy AK radius-1 machinery may be used only after an explicit signed-origin conjugacy statement.

Required output:

`R059D_STAGE_APR_ONE_STEP_SEGMENT_CLASS.json`.

## 5. Stage B — source sweep and competition fibers

Use the orthogonal/source compatibility sweep only as a teacher/readout layer after target semantics are frozen.

For every source orientation in one fundamental sector:

- enumerate admissible target competitors under the declared local collapse relation;
- locate all intervals where more than one target candidate competes;
- distinguish open intervals from isolated ties;
- compute exact/rational boundary certificates where possible;
- transport by D6 around the full turn.

Explicitly test whether `M_UP` is hit on positive-measure orientation fibers.

If “probability” depends on source sampling measure, report the exact dependence. Do not call it intrinsic native probability unless proved.

Required outputs:

- `R059D_STAGE_APR_ONE_STEP_SWEEP_FIBERS.json`
- `R059D_STAGE_APR_MIXED_UP_COMPETITOR_EXPOSURE.json`.

## 6. Stage C — define UP and DOWN on identical pre-collapse inputs

Construct a common admissible order/partial order on candidate target states.

Define:

- `UP`: choose the outward/higher candidate;
- `DOWN`: choose the inward/lower candidate.

The definitions must be local and independent of whether the final orbit closes.

For every competition fiber, record both choices side-by-side.

Required output:

`R059D_STAGE_APR_UP_DOWN_COLLAPSE_SPEC.json`.

## 7. Stage D — one-step length drift under UP

Primary test:

`UPWARD_COLLAPSE_FROM_ONE_STEP_CAUSES_LENGTH_INFLATION`.

For the mandatory sextet `M_UP`, determine whether choosing such a state from a one-step pre-collapse orientation forces a larger operational length class.

A valid proof must use the target operational length semantics or exact signed-origin conjugacy; “the coordinates are numerically larger” is insufficient.

If `M_UP` is not actually reached or does not inflate length, freeze the exact countertheorem.

Required output:

`R059D_STAGE_APR_UPWARD_ONE_STEP_LENGTH_DRIFT_THEOREM.json`.

## 8. Stage E — derive the DOWN competitor and axis completion

Do not pre-impose that the DOWN winner is an axis anchor.

For each competition fiber derive the lower admissible native state.

Then formalize the user’s phrase “遇到数轴补齐长度” as a local operation:

- detect a native axis encounter using signed-origin semantics;
- compute any missing one-step budget using a target-local rule;
- complete along the encountered Enterprise axis;
- preserve the one-step length class;
- use the same rule in every sector and under reversal.

The completion may not be defined as “whatever makes the orbit close”.

Required outputs:

- `R059D_STAGE_APR_DOWN_COMPETITOR_TABLE.json`
- `R059D_STAGE_APR_AXIS_COMPLETION_SPEC.json`.

## 9. Stage F — full-turn orbit theorem

Starting from `(2,1,1)`, execute the DOWN+completion turn law through all six sectors.

Prove or refute:

1. one-step length is preserved at every post-collapse state;
2. D6 cyclic order is respected;
3. no premature return occurs;
4. a full turn closes exactly;
5. reversal gives the inverse cycle;
6. determine whether the final native endpoint orbit is exactly `A1` or strictly larger.

The report must explicitly answer the user’s intuition:

> “It looks like the one-step segment only passes through axis points, but is the actual collapse dynamics more complicated?”

A valid outcome may be:

- the endpoint orbit is indeed six axis points **but** the hidden competition/collapse fibers are nontrivial;
- the true endpoint orbit contains additional native states;
- or the user hypothesis is false.

Required output:

`R059D_STAGE_APR_ONE_STEP_FULL_ORBIT_THEOREM.json`.

## 10. Stage G — necessity of downward collapse

Within the smallest meaningful local policy class, test:

`ONE_STEP_FULL_ORBIT_CLOSURE => DOWNWARD_COLLAPSE_WITH_AXIS_COMPLETION`.

If UP fails at the first unavoidable `M_UP`-type competition fiber, prove the first-divergence obstruction and D6 propagation.

If more than one lawful policy closes, identify the missing independent axiom rather than forcing uniqueness.

Required output:

`R059D_STAGE_APR_COLLAPSE_DIRECTION_NECESSITY.json`.

## 11. Stage H — radius-1 signed-origin conjugacy audit

Compare the successful one-step signed-origin orbit against the legacy auxiliary radius-1 circle, not radius 2.

Use

`ENC_SIGNED(0)=O_E`

`ENC_SIGNED(k)=sign(k)(|k|+1)` for `k!=0`.

Determine exactly which of the following are conjugate:

- endpoint graph;
- turn order;
- D6 action;
- length class;
- collapse competition fibers;
- axis completion.

A six-axis endpoint cycle may be conjugate even if the hidden source-fiber collapse semantics are new.

Required output:

`R059D_STAGE_APR_RADIUS1_SIGNED_ORIGIN_CONJUGACY.json`.

## 12. Deterministic validation

After theorem statements are frozen, validate at minimum:

- dense sweep over one sector plus D6 transport;
- every `A1` anchor;
- every `M_UP` state;
- identical pre-collapse inputs for UP and DOWN;
- all axis-completion events;
- forward/reverse full cycle;
- exact length-class checks;
- bridge comparison to legacy radius-1 auxiliary orbit.

Finite sweep is implementation evidence only. Positive-measure and closure claims need symbolic/fiber or finite-state proof.

## 13. Firewalls

- `0` may appear only in the auxiliary chart.
- `+1 ≡ -1` is one native origin state.
- The rotating segment is **one primitive step from origin**.
- Do not call `M_UP` a one-step circle state before proving it.
- Source Euclidean distance/Q/trig may expose fibers, but may not define target length or select the winner.
- Do not define DOWN or axis completion from the desired closure result.
- Do not reopen AO asymptotics unless needed to type a source probability measure.

## 14. Dispositions

Use the strongest justified terminal status:

1. `ONE_STEP_HIDDEN_COMPETITION_PROVED__DOWNWARD_AXIS_COMPLETION_NECESSARY_AND_SUFFICIENT_FOR_FULL_ORBIT`
2. `ONE_STEP_DOWNWARD_FULL_ORBIT_PROVED__UPWARD_LENGTH_INFLATION_PROVED__NECESSITY_OPEN`
3. `SIX_AXIS_ENDPOINT_ORBIT_PROVED__NONTRIVIAL_COLLAPSE_FIBERS_PROVED`
4. `MIXED_UPWARD_COMPETITOR_MECHANISM_PROVED__FULL_CLOSURE_LAW_OPEN`
5. `USER_HYPOTHESIS_PARTIALLY_FALSE__CORRECTED_ONE_STEP_MECHANISM_PROVED`
6. `USER_HYPOTHESIS_FALSE__EXACT_COUNTEREXAMPLE`

Stop for Driver review. Do not consume a later stage automatically.
