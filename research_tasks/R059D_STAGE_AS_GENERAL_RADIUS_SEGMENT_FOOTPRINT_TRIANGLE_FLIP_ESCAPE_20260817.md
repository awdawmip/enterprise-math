# R059D Stage AS — General-Radius Segment Footprint, Triangle-Flip Escape, and Closure

Task-ID: `RS-R059D-STAGE-AS-GENERAL-RADIUS-SEGMENT-FOOTPRINT-TRIANGLE-FLIP-ESCAPE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-as-general-radius-segment-footprint-triangle-flip-escape`

Driver input review:

`driver_reviews/R059D_STAGE_AR_DRIVER_REVIEW_20260817.md`

## 0. Why this stage exists

Stage AR proved a clean but sharply scoped theorem for one primitive segment:

- the stateful object is not a memoryless cell;
- the minimal one-step state is `S=(e,C)`, where `e` is a primitive radial edge from the fixed signed origin and `C` is one of its two incident origin-star side triangles;
- both side lifts are retained;
- native incidence alone gives `T(k,d)=(k+d,d)`;
- the twelve lifted states split into two reversal-related directed six-cycles;
- every legitimate one-step lift closes with minimal period 6;
- AQ's strict `Delta SHELL=+1` DAG disappears because the retained segment state stays on the origin star.

But this does **not** define a segment of primitive length `r>1` before the old circle is used.

The next hard problem is therefore foundational:

> What is the native state of a longer fixed-origin line segment, and how may that state move through adjacent triangular cells while retaining every legitimate path and without importing the old circle as an oracle?

The user's earlier intuition about upward/downward collapse is especially relevant here: a path or footprint crossing a triangular cell may replace one boundary edge by two or two by one. Stage AS must test whether that local `1 <-> 2` triangle-flip grammar is the correct native source of length drift, compensation, or turn structure.

Do not assume that it is correct. Exact counterexamples are valid outcomes.

## 1. Frozen coordinate and prior-stage inputs

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `driver_reviews/R059D_STAGE_AR_DRIVER_REVIEW_20260817.md`
- AR report/proof/checkpoint from `research/r059d-stage-ar-stateful-line-segment-multipath-escape-turn-closure`
- AQ report/proof only as the frozen cell-only baseline
- AP-REISSUE only as frozen radius-1 comparison input
- AK/AL only under the post-freeze firewalls below.

Freeze:

`+1 ≡ -1 ≡ O_E`.

`0` is not a native Enterprise coordinate.

Negative native coordinates `-2,-3,...` are legal.

Auxiliary zero-centered A2 labels may be used only as typed incidence/CELL_ID charts through the signed-origin conjugacy.

## 2. Radius / anchor typing — mandatory

For this stage, `r>=1` means an **external primitive segment-unit count**, not a native coordinate value and not AK orbit membership.

The positive axis anchor after `r` primitive native adjacency steps from `O_E` has native coordinate magnitude `r+1` on that axis. Likewise in the negative direction.

Thus the six axis anchors for primitive count `r` are the signed-origin images of the six auxiliary A2 vectors of graph magnitude `r`.

Freeze the distinction:

`PRIMITIVE_SEGMENT_UNIT_COUNT = r`

versus

`AXIS_ENDPOINT_NATIVE_COORDINATE_MAGNITUDE = r+1`.

Do not reintroduce native zero, and do not call `r+1` the segment length merely because it is the coordinate label.

Required output:

`R059D_STAGE_AS_RADIUS_ANCHOR_TYPING.json`.

## 3. Circularity firewall

Primary AS state and transitions may **not** use:

- AK `tau`;
- membership in AK `SEG_E(r)`;
- the accepted AK endpoint orbit;
- AL A8 / primitive-support frontier maximality;
- source Euclidean angle, radius, circle, standard pi, or trigonometry;
- BRC teacher circle membership;
- any path pruning criterion of the form "keep it because it matches the old circle".

AL `SUP/K_E(r)` may be used only in a separately typed post-primary comparison arm after the AS state/transition/length law is frozen.

All legitimate state lifts and all tied escape branches survive.

## 4. Stage A — classify possible pre-circle general-radius segment carriers

Starting only from native vertex/edge/triangle incidence and the radius-r axis anchor, determine what object can legitimately represent a longer line segment.

At minimum audit the following candidate carrier families; they are hypotheses, not preferred answers:

### A1. Ordered primitive edge chain

A connected ordered primal edge path

`P=(e_1,...,e_m)`

starting at `O_E`, with the axis anchor represented by the unique straight axis chain of `r` primitive edges.

Questions:

- must `m=r` in every turned state, or only on the axis anchor?
- is simplicity/no-backtracking justified?
- does path order carry enough segment semantics?
- does this reduce exactly to AR `e` at `r=1`?

### A2. Nested prefix / packet stack

A line segment may be represented as `r` ordered primitive segment units or nested prefixes sharing one fixed endpoint and one sweep-side structure.

Questions:

- is a packet/layer index intrinsically justified by the axis anchor?
- can all units be transported locally without presupposing a global angle?
- does the model force an unjustified coherent motion axiom?

### A3. Connected swept strip / triangle footprint

A segment may require an ordered boundary chain together with the native triangles presently touched on one or both sides.

Questions:

- what is the minimal footprint sufficient for continuation?
- is the side data local or radius-growing?
- is there a canonical active frontier cell, or several legitimate ones?

### A4. Exact stronger carrier discovered by the Researcher

Allowed only if derived from native incidence and shown to reduce to AR at `r=1`.

For every carrier candidate classify:

- `JUSTIFIED_PRE_CIRCLE`;
- `UNDERDETERMINED_BUT_POSSIBLE`;
- `REJECTED_BY_EXACT_INCIDENCE_COUNTEREXAMPLE`;
- `LEAKS_OLD_CIRCLE_OR_SOURCE_GEOMETRY`.

If multiple inequivalent carrier models satisfy all frozen pre-circle requirements and cannot be distinguished natively, freeze that underdetermination rather than choosing one by fit.

Required output:

`R059D_STAGE_AS_GENERAL_RADIUS_STATE_CLASSIFICATION.json`.

## 5. Stage B — mandatory reduction and consistency axioms

Any surviving general-radius state model must satisfy all of:

1. **AR reduction:** at `r=1` the legitimate lifted state space is exactly the twelve AR states, up to an explicitly proved representation isomorphism.
2. **Axis-anchor correctness:** the six radius-r axis anchors are represented without using AK/AL circle data.
3. **D6 covariance.**
4. **Reversal covariance.**
5. **Translation typing:** if the fixed origin is translated, the whole incidence carrier translates consistently.
6. **Prefix/restriction consistency where meaningful:** removing the outermost axis primitive unit from an axis anchor of count `r` gives the count `r-1` anchor state.
7. **No hidden source angle.**
8. **No hidden old-orbit membership.**
9. State size may grow with `r`; constant-size memory is **not** required at this foundational stage.

Required output:

`R059D_STAGE_AS_STATE_CONSISTENCY_AUDIT.json`.

## 6. Stage C — triangle-flip / local sweep grammar

For every surviving primal-chain or strip-like carrier, derive all elementary changes caused by sweeping across one adjacent triangular cell.

Mandatory diagnostic:

If the current segment footprint uses exactly one edge of a triangle, replacing that edge by the other two is a local `1 -> 2` edge-boundary flip.

If the footprint uses exactly two edges of a triangle, replacing them by the third is a local `2 -> 1` flip.

Determine exactly:

- when each flip is legal under fixed-origin segment semantics;
- whether either flip changes the chosen segment-length invariant;
- whether paired/coherent flips can preserve a fixed length class;
- whether the user's earlier "upward makes the line longer / downward shortens then needs completion" intuition is literally realized by this grammar, only analogous to it, or false;
- whether a local axis encounter creates a canonical compensation/completion operation without defining it as "whatever restores the old circle".

All locally legal flips must remain available unless a **pre-circle native invariant** excludes them.

Do not call raw edge-count change a physical/native length change unless Stage D proves edge count is the native length invariant.

Required output:

`R059D_STAGE_AS_TRIANGLE_FLIP_GRAMMAR.json`.

## 7. Stage D — derive or refute a general-radius pre-circle length invariant

The central foundation problem is to extend AR's

`L_pre=1 iff e is a primitive radial edge`

to `r>1` without AK orbit membership or source distance.

Test candidate invariants including, but not limited to:

- primitive edge-chain cardinality;
- conserved packet/layer count;
- nested-prefix count;
- a footprint quantity derived purely from vertex/edge/triangle incidence;
- a path-independent class label induced from the six axis anchors and local flip relations.

For a candidate to be accepted as `L_pre=r`, prove:

1. the six radius-r axis anchors have class `r`;
2. every primary legal transition has a declared effect on the class;
3. if the class is intended to be conserved, path-independence is proved rather than assumed;
4. different radii are distinguishable without old-circle period information;
5. the definition reduces to AR at `r=1`.

If no such invariant is derivable, freeze:

`GENERAL_RADIUS_PRE_CIRCLE_LENGTH_UNDERDEFINED`

and do **not** substitute coordinate magnitude, source radius, or AL support rank.

Required output:

`R059D_STAGE_AS_GENERAL_RADIUS_LENGTH_AUDIT.json`.

## 8. Stage E — derive the stateful adjacent-cell escape relation

Only after the carrier and length typing are frozen, implement the user's escape idea on the **whole segment state**.

For a state `S`, identify every native adjacent triangular cell that the segment can legitimately sweep into next.

The candidate relation must be derived from the segment footprint, and may involve one active frontier cell or several simultaneously active local sites.

For each candidate successor `S'`, record:

- local cell(s) crossed;
- footprint/chain change;
- free-endpoint change;
- segment-length-class change if defined;
- shell change of every relevant entered/free-end cell;
- whether the transition is a triangle flip, axis completion, tangential move, inward recovery, or another exactly defined native type.

Then define the escape score from a source-free native shell observable. Do not assume the AQ current-cell score is still the correct segment score; audit at least:

1. shell of the active/free-end cell;
2. maximum shell among newly entered cells;
3. any alternative incidence score proved necessary by the state semantics.

A score is admissible only if it is native, D6-covariant, and not tuned to the old circle.

For the accepted score, retain **all** maximizing successor states.

Required outputs:

- `R059D_STAGE_AS_STATEFUL_CANDIDATE_RELATION.json`
- `R059D_STAGE_AS_STATEFUL_ESCAPE_SCORE.json`.

## 9. Stage F — finite exhaustive atlas before circle comparison

For every surviving canonical/underdetermined model, compute exact state graphs for the smallest nontrivial radii before comparing to prior circles.

Minimum target:

- exhaustive `r=1..6` where tractable;
- for each r, jump budgets `J=0..64` or until the complete finite state graph is exhausted;
- larger `r` checkpoints if a closed form or compressed representation is available.

Record:

- total legitimate states;
- number of outgoing branches by state type;
- shell increment distribution;
- length-class increment distribution;
- SCC decomposition;
- number and lengths of cycles;
- escaping/nonclosing branches;
- path mergers;
- projected free-endpoint sets;
- reversal/D6 orbit decomposition;
- whether all-path acceptance produces a finite turn object, an annulus/envelope, a mixed cyclic+escaping object, or unbounded growth.

Required output:

`R059D_STAGE_AS_GENERAL_RADIUS_ESCAPE_ATLAS.json`.

## 10. Stage G — intrinsic closure theorem

Before any AK/AL comparison, state the strongest theorem supported by the all-path state graph.

Required questions for each `r` in the proved scope:

1. Do all legitimate branches preserve `L_pre=r` if such an invariant exists?
2. Do all legitimate branches close?
3. Do only some close while others escape?
4. Is there a natural first-return time independent of tuned `J`?
5. Are there reversal-related cycle families?
6. Does the projected free endpoint close even when hidden footprint state differs?
7. Is the state graph finite or infinite?
8. Is there a strict Lyapunov function that still forbids cycles?

Never promote one lucky closed branch to a circle if equally admissible nonclosing branches survive.

Required output:

`R059D_STAGE_AS_GENERAL_RADIUS_CLOSURE_THEOREM.json`.

## 11. Stage H — separately typed AL support experiment

Only after Stages A–G are frozen may `K_E(r)` be added as a support/incidence cap.

Restrictions:

- `SUP` is not length;
- AL A8 is disabled;
- AK `tau` is disabled;
- no primary branch may be deleted retroactively;
- run the same all-path segment transition law, merely rejecting states outside the independently accepted support carrier if that rejection is well-typed for the chosen state model.

Ask whether:

- support + stateful escape derives a finite frontier;
- support removes only length-drift branches by an independently meaningful incidence condition;
- support still leaves multiple lawful cycles/branches;
- support is irrelevant or incompatible with the general-radius segment state.

Required output:

`R059D_STAGE_AS_AL_SUPPORT_GENERAL_RADIUS_AUDIT.json`.

## 12. Stage I — post-freeze comparison to AK/AL/AP

Only now compare the intrinsic AS object with accepted prior circle objects.

At minimum compare radii in the proved AS scope.

Determine separately:

- endpoint set equality;
- endpoint cyclic order;
- hidden-state equality/inequality;
- period equality;
- containment among additional AS branches;
- whether prior canonical circle is one branch among many or the unique all-path object;
- whether a mismatch is caused by length typing, triangle-flip ambiguity, support, or state underdetermination.

No retuning and no pruning for fit.

Required output:

`R059D_STAGE_AS_CIRCLE_RELATION_AUDIT.json`.

## 13. Preferred theorem targets / terminal dispositions

Use the strongest exact disposition supported by proof.

Preferred if true:

`GENERAL_RADIUS_STATEFUL_ALL_PATH_SEGMENT_ESCAPE_DERIVES_FIXED_LENGTH_TURN_CLOSURE`.

Other valid outcomes:

1. `GENERAL_RADIUS_SEGMENT_STATE_DERIVED__CLOSED_AND_ESCAPING_BRANCHES_COEXIST`
2. `GENERAL_RADIUS_SEGMENT_STATE_DERIVED__TRIANGLE_FLIP_LENGTH_DRIFT_PREVENTS_ALL_PATH_CLOSURE`
3. `GENERAL_RADIUS_PRE_CIRCLE_LENGTH_UNDERDEFINED`
4. `MULTIPLE_INEQUIVALENT_GENERAL_RADIUS_SEGMENT_LIFTS_SURVIVE__NATIVE_STATE_UNDERDETERMINED`
5. `GENERAL_RADIUS_STATEFUL_ESCAPE_REMAINS_ACYCLIC`
6. `AL_SUPPORT_PLUS_STATEFUL_ESCAPE_DERIVES_FINITE_FRONTIER__PRIMARY_ESCAPE_ALONE_INSUFFICIENT`
7. `TRIANGLE_FLIP_UP_DOWN_MECHANISM_PROVED__AXIS_COMPLETION_LAW_OPEN`
8. an exact stronger countertheorem.

## 14. Mandatory firewalls

- native zero remains nonexistent;
- `r` primitive-unit count is typed separately from native coordinate magnitude `r+1`;
- all legitimate state lifts survive;
- all tied escape successors survive;
- path count is not intrinsic probability;
- no source angle/circle/pi in primary definitions;
- no AK `tau` / `SEG_E(r)` membership in primary state or transition law;
- no AL A8 in primary state or transition law;
- AL support arm only after primary freeze;
- do not modify prior-stage result files;
- proof dominates checker evidence.

## 15. Deterministic validation

After theorem statements are frozen, validate at minimum:

- exact AR reduction at `r=1`;
- all six radius-r signed-origin axis anchors for tested radii;
- every locally legal triangle flip;
- D6/reversal covariance;
- length-invariant replay and path-independence if claimed;
- exhaustive state graph for the declared small-r scope;
- two independently implemented traversals;
- SCC / cycle / first-return census;
- all tied branches retained;
- no-native-zero firewall;
- primary no-leakage firewall;
- post-freeze support and circle comparison isolation;
- external GitHub immutability compare.

## 16. Stop condition

Stop for Driver review after checkpoint freeze.

Do not consume a later stage automatically.
