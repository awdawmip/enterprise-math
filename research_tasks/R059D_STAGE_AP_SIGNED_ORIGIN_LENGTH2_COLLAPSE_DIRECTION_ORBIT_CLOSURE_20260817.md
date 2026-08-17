# R059D Stage AP — Signed-Origin Length-2 Collapse Direction and Orbit Closure

Task-ID: `RS-R059D-STAGE-AP-SIGNED-ORIGIN-LENGTH2-COLLAPSE-DIRECTION-ORBIT-CLOSURE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-ap-signed-origin-length2-collapse-direction`

## 0. Why this stage exists

Stage AO was frozen as the end of the old circle/BRC refinement line. This stage is reopened only because the user supplied a stronger signed-origin foundation and a new geometric mechanism that may explain the circle closure law.

This is not an AO fluctuation continuation. It is a foundational revalidation of fixed-length turning under:

`+1 ≡ -1 ≡ O_E`

and

`0` absent from Enterprise native coordinates.

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
- frozen R059D AK/AL circle-turn results only as legacy/auxiliary-chart comparison material.

Do not modify prior-stage result files.

## 1. Frozen signed-origin semantics

The native axis is:

`...,-4,-3,-2,±1,+2,+3,+4,...`

with one glued origin state:

`+1 ≡ -1 ≡ O_E`.

One primitive step from origin reaches `+2` or `-2`; two primitive steps reach `+3` or `-3`.

Hence a **primitive segment length class 2** is not the same object as native coordinate magnitude 2.

For this task, a length-2 axis anchor has endpoint at coordinate magnitude 3, e.g.

`(3,1,1)` or `(-3,1,1)`.

This distinction is mandatory:

`NATIVE_COORDINATE_MAGNITUDE(±n)=n`

`PRIMITIVE_AXIS_STEP_LENGTH(O_E,±n)=n-1`.

## 2. User working hypothesis

Treat the following as the Driver working hypothesis to test rigorously:

> When a primitive-length-2 line is turned through a full sweep, a small but nonzero set of orientations naturally competes for six mixed signed-origin states. If the collapse rule chooses the upper/outward candidate, the line cannot complete one full orbit while preserving length: algebraically the segment length drifts upward / the orbit fails closure. If the collapse rule chooses the lower/inward candidate and uses the native axis to complete the missing length whenever an axis is encountered, the fixed-length orbit can close.

Freeze the hypothesis labels:

`UPWARD_COLLAPSE -> LENGTH_DRIFT_OR_ORBIT_NONCLOSURE`

`DOWNWARD_COLLAPSE_WITH_AXIS_COMPLETION -> LENGTH2_PRESERVING_FULL_ORBIT`

These are hypotheses, not results. Exact counterexamples must supersede them if found.

## 3. Mandatory six-state witness set

The task MUST explicitly analyze the cyclic sextet:

`M2 = {`

`(3,-3,1),`

`(1,-3,3),`

`(-3,1,3),`

`(-3,3,1),`

`(1,3,-3),`

`(3,1,-3)`

`}`.

Also track the six pure-axis length-2 anchors:

`A2 = {`

`(3,1,1), (-3,1,1),`

`(1,3,1), (1,-3,1),`

`(1,1,3), (1,1,-3)`

`}`.

The report must determine whether every member of `M2` is:

1. a legitimate length-2 orientation state;
2. a collapse competitor only;
3. an outward/overlength state;
4. an inward state needing axis completion;
5. or something else.

Do not assume the answer.

## 4. Auxiliary-chart decoding — allowed only as a bridge

The signed-origin conjugacy bridge is allowed as an auxiliary proof tool:

`DEC_SIGNED(O_E)=0`

`DEC_SIGNED(±n)=±(n-1)` for `n>=2`.

Under this bridge the mandatory sextet becomes:

`M2_aux = {`

`(2,-2,0),`

`(0,-2,2),`

`(-2,0,2),`

`(-2,2,0),`

`(0,2,-2),`

`(2,0,-2)`

`}`.

The six axis anchors become the obvious signed auxiliary radius-2 anchors.

This is highly relevant evidence, but native conclusions must be translated back to the signed-origin chart. `0` must never be called a native Enterprise coordinate.

## 5. Stage A — define the length-2 segment state independently of collapse

Construct a signed-origin native segment state for primitive length 2.

At minimum specify:

- fixed center `O_E=(±1,±1,±1)`;
- endpoint native state;
- orientation/sector data;
- the invariant that means `primitive length = 2`;
- how axis anchors in `A2` instantiate the same length class.

The length invariant must be operational/native. It must not be defined as source Euclidean distance, source `Q`, or by the desired collapse rule itself.

Legacy AK state machinery may be reused only after an exact signed-origin conjugacy is stated.

Required output:

`R059D_STAGE_AP_LENGTH2_SEGMENT_STATE.json`.

## 6. Stage B — expose the source sweep and the six mixed competitors

Use a continuous source/compatibility sweep only as a teacher/readout layer to enumerate which native candidates compete as the line turns.

Prove or refute:

- the six `M2` states occur as one D6 orbit of special competition states;
- they occupy a small but nonzero angular/fiber measure under a clearly declared source sampling measure;
- the measure/probability is D6 symmetric;
- the event is not an artifact of one arbitrary tie convention.

If the phrase “small probability” depends on the sampling measure, report the exact dependence rather than pretending it is intrinsic.

Required output:

`R059D_STAGE_AP_M2_COMPETITOR_EXPOSURE.json`.

## 7. Stage C — formalize UP and DOWN collapse without circularity

Define two candidate collapse policies from the same pre-collapse source fiber/state.

### UP / outward candidate

Formalize the smallest reasonable algebraic meaning of “upward collapse”: choose the outward/higher admissible candidate according to a declared shell/support/partial order.

### DOWN / inward candidate

Formalize “downward collapse”: choose the inward/lower admissible candidate according to the same underlying order.

### Axis completion

Formalize the user’s “遇到数轴补齐长度” rule as a target-side local operation:

when the downward choice reaches a state whose representation touches an Enterprise native axis/origin component, the missing primitive length budget may be completed along that axis, but the completed segment must remain in the same primitive length-2 equivalence class.

The exact completion law is research output. It must not be defined by “whatever makes the orbit close”.

Required outputs:

- `R059D_STAGE_AP_UP_DOWN_COLLAPSE_SPEC.json`
- `R059D_STAGE_AP_AXIS_COMPLETION_SPEC.json`

## 8. Stage D — algebraic length-drift theorem

For every collapse event around the full sweep, compare the pre-collapse length-2 class to the post-collapse segment state.

Primary target:

`UPWARD_COLLAPSE_LENGTH_DRIFT_PROVED`.

A strong acceptable theorem is one of:

- every UP event at `M2` strictly increases a native length budget;
- at least one unavoidable D6 orbit of UP events increases it, making global fixed-length closure impossible;
- or a precise alternative obstruction showing why UP cannot produce a full length-2 orbit.

Do not merely say “coordinates get bigger”. Prove that the operational segment length class changes or that the turn machine becomes inconsistent.

Required output:

`R059D_STAGE_AP_UPWARD_LENGTH_DRIFT_THEOREM.json`.

## 9. Stage E — downward collapse + axis completion closure theorem

Construct the DOWN+completion turn sequence starting from one axis anchor, for example `(3,1,1)`.

Prove or refute all of:

1. every step preserves primitive segment length 2;
2. all signed sectors are traversed in cyclic order;
3. every required axis encounter is completed by the same radius-uniform local rule;
4. no state returns prematurely;
5. the endpoint/state orbit closes after one full turn;
6. the six `M2` states are handled consistently with D6 symmetry;
7. reversing orientation gives the inverse traversal.

If successful, isolate the minimal period and compare it to the legacy radius-2 R059D orbit through `DEC_SIGNED`.

Required outputs:

- `R059D_STAGE_AP_DOWNWARD_LENGTH_PRESERVATION_THEOREM.json`
- `R059D_STAGE_AP_FULL_ORBIT_CLOSURE_THEOREM.json`

## 10. Stage F — upward-vs-downward uniqueness / necessity

Determine whether the stronger necessity statement is true:

`FULL_LENGTH2_ORBIT_CLOSURE => DOWNWARD_COLLAPSE_WITH_AXIS_COMPLETION`

within a clearly stated local admissible policy class.

If both policies can close under different lawful completions, report that and identify the missing axiom.

If only DOWN closes, prove the first-divergence obstruction.

Required output:

`R059D_STAGE_AP_COLLAPSE_DIRECTION_NECESSITY_THEOREM.json`.

## 11. Stage G — signed-origin conjugacy audit of the radius-2 legacy circle

Because `ENC_SIGNED/DEC_SIGNED` gives a natural bridge to the old zero-centered auxiliary chart, test whether the successful signed-origin turn law is exactly conjugate to the previously frozen radius-2 auxiliary orbit.

Must distinguish:

- combinatorial equivalence;
- state-graph conjugacy;
- length semantics;
- source/BRC comparison semantics.

A successful radius-2 conjugacy does NOT automatically revalidate all radii; freeze only what is proved.

Required output:

`R059D_STAGE_AP_RADIUS2_SIGNED_ORIGIN_CONJUGACY.json`.

## 12. Deterministic validation

After theorem statements are frozen, replay at minimum:

- dense source sweep for length 2 with exact/rational angle ordering where possible;
- all D6 images of every special event;
- all six `A2` anchors;
- all six `M2` mixed states;
- UP and DOWN policies under identical pre-collapse inputs;
- axis-completion events;
- full forward and reverse cycles;
- state uniqueness / premature return check;
- exact bridge comparison through `ENC_SIGNED/DEC_SIGNED`.

Finite sampling validates implementation only; closure/length claims require symbolic or finite-exhaustive proof on the finite length-2 state system.

## 13. Mandatory firewalls

- `0` may appear only in auxiliary/ambient coordinates, never as a native Enterprise coordinate.
- `+1` and `-1` are one glued origin state.
- Primitive segment length 2 is not the same type as native coordinate magnitude 2.
- Source Euclidean distance / `Q` / trigonometry may expose competition fibers but may not define target length or choose the winner.
- Do not assume DOWN succeeds merely because it closes in a replay.
- Do not define axis completion by the desired final answer.
- Do not reopen AO asymptotic measure analysis unless it is strictly necessary to quantify the length-2 competition probability.

## 14. Dispositions

Use the strongest justified terminal status:

1. `DOWNWARD_COLLAPSE_WITH_AXIS_COMPLETION_NECESSARY_AND_SUFFICIENT_FOR_LENGTH2_FULL_ORBIT`
2. `DOWNWARD_COLLAPSE_LENGTH2_ORBIT_PROVED__UNIQUENESS_OPEN`
3. `UPWARD_COLLAPSE_NONCLOSURE_PROVED__DOWNWARD_COMPLETION_PARTIAL`
4. `M2_COMPETITOR_MECHANISM_PROVED__COLLAPSE_DIRECTION_THEOREM_OPEN`
5. `USER_HYPOTHESIS_PARTIALLY_FALSE__EXACT_CORRECTED_MECHANISM_PROVED`
6. `USER_HYPOTHESIS_FALSE__EXACT_COUNTEREXAMPLE`

Stop for Driver review. Do not consume a later stage automatically.
