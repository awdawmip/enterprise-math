# R059D Stage AR — Stateful Line-Segment Multipath Escape and Turn Closure

Task-ID: `RS-R059D-STAGE-AR-STATEFUL-LINE-SEGMENT-MULTIPATH-ESCAPE-TURN-CLOSURE`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-ar-stateful-line-segment-multipath-escape-turn-closure`

Driver input review:

`driver_reviews/R059D_STAGE_AQ_DRIVER_REVIEW_20260817.md`

Review acceptance commit:

`db226bb787620e6518f9be3c375c82ff3ffdd4ac`

## 0. Why this stage exists

AQ proved the user's memoryless cell-escape rule exactly:

- native elementary cells have three edge-neighbors;
- `SHELL(C)=d_dual(STAR(O_E),C)` is source-free and D6-invariant;
- `FAR(C)` consists exactly of shell-`+1` neighbors;
- all tied FAR branches survive;
- the resulting paths are exactly outward dual-geodesics;
- the directed AQ graph is a strict-shell DAG;
- for the one-step aggregate seed set, `END_J=S_J union S_(J+1) union S_(J+2)` and `REACH_LE_J=B_(J+2)`;
- this current cell-only object is not the accepted fixed-length turn circle.

But AQ also exposed a semantic loss: after the segment supplies the initial endpoint seed cells, the evolving state is only `current cell`. The object that is supposed to escape — **the line segment** — no longer persists in the transition state.

The user's rule is therefore not exhausted by AQ.

Stage AR asks the next exact question:

> If the escape process is lifted from a memoryless cell walker to a genuinely stateful native line-segment process, while all admissible tied paths remain valid and no old circle is inserted as an oracle, does the strict outward DAG obstruction survive? Can a set-valued native turn/closure object emerge?

This is a foundation/diagnostic stage. Do not tune it to recover the old circle.

## 1. Frozen inputs

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
- `driver_reviews/R059D_STAGE_AQ_DRIVER_REVIEW_20260817.md`
- AQ report/proof/checkpoint from owner branch `research/r059d-stage-aq-native-cell-escape-multipath-reachability`
- AP-REISSUE one-step signed-origin task/result as frozen prior input
- AK and AL results only under the circularity restrictions below.

Freeze coordinate semantics:

`+1 ≡ -1 ≡ O_E`.

`0` is not a native Enterprise coordinate.

Auxiliary zero-centered A2 labels are allowed only as typed incidence/CELL_ID charts through `ENC_SIGNED/DEC_SIGNED`.

Freeze AQ as a baseline theorem, not as the final segment model.

## 2. Hard objective

The unique hard objective is:

`DETERMINE_WHETHER_STATEFUL_LINE_SEGMENT_ESCAPE_BREAKS_THE_CELL_ONLY_DAG_AND_CAN_SUPPORT_NATIVE_TURN_CLOSURE`.

The stage must distinguish three logically different things:

1. `CELL_ESCAPE_STATE`: current cell only — already solved by AQ;
2. `SEGMENT_ESCAPE_STATE`: enough native state to represent an actual line segment moving through/among cells;
3. `CIRCLE/TURN_ORBIT`: a closed fixed-origin endpoint object — comparison only after the stateful escape law is independently frozen.

Do not conflate them.

## 3. Circularity firewall — mandatory

This stage is specifically testing whether escape can help **derive** a turn object. Therefore the following may not be used as primitive transition or membership oracles:

### 3.1 AK orbit-membership prohibition

AK defines `SEG_E(r)` as the legal `tau` orbit class and `L_E=r` through that orbit semantics.

Therefore it is forbidden to define an AR candidate as legal merely because

`candidate in SEG_E(r)`

or because AK `tau` would visit it.

That would recover the old circle by definition.

AK may be used only post hoc to compare a frozen AR object against the accepted turn orbit.

### 3.2 AL frontier prohibition

AL's support carrier `K_E(r)={p:SUP(p)<=9r^2}` is a source-free native incidence/support object and may be used only in a separately typed comparison arm.

However AL A8 — `PRIMITIVE_SUPPORT_FRONTIER_MAXIMALITY` — is forbidden as an AR transition selector during the primary stateful-escape construction.

If a later comparison arm shows that `K_E(r)` plus the independently frozen AR escape rule dynamically reproduces the AL outer frontier, that is a valid theorem. It must be typed as

`AL_SUPPORT_CARRIER_PLUS_ESCAPE => FRONTIER`

not as an independent derivation of the support carrier itself.

### 3.3 Source geometry prohibition

Source Euclidean radius, source angle, source circle arc, standard pi, and BRC teacher membership may not define:

- segment state;
- candidate neighbor set;
- escape score;
- branch pruning;
- jump budget;
- closure criterion.

They may appear only in a final comparison audit after the target object is frozen.

## 4. Stage A — audit what state a native line segment minimally requires

Start from the one-step signed-origin segment class because its anchor meaning is unambiguous.

The six one-step axis endpoint anchors are the frozen AP-REISSUE states

`A1={`
`(2,1,1),(-2,1,1),`
`(1,2,1),(1,-2,1),`
`(1,1,2),(1,1,-2)`
`}`.

Construct the smallest source-free state type that can legitimately be called a **line-segment escape state**, not merely a cell.

Audit candidate components separately:

- fixed endpoint `O_E`;
- free-endpoint native point/incidence state;
- current elementary cell(s) touched by the free endpoint or segment trace;
- incoming edge / previous-cell state if line continuity needs it;
- directed axis/sector/orientation data if it is genuinely native and not a hidden circle angle;
- a segment footprint / ordered incidence chain if required;
- a one-step or radius-r length/budget label only if independently meaningful before the old circle is used.

For each component prove either:

`NECESSARY_FOR_SEGMENT_SEMANTICS`,

`DERIVABLE_FROM_OTHER_STATE`,

or

`NOT_JUSTIFIED_PRE_CIRCLE`.

Do not add memory merely because it improves closure.

If no pre-circle state richer than AQ can be justified, freeze the obstruction

`PRE_CIRCLE_STATEFUL_SEGMENT_LIFT_UNDERDEFINED`

and stop rather than inventing one.

Required output:

`R059D_STAGE_AR_SEGMENT_STATE_AUDIT.json`.

## 5. Stage B — construct all legitimate one-step segment lifts

For each of the six one-step endpoint orientations, enumerate every native segment-state lift compatible with Stage A.

The lift must retain all legitimate ambiguity:

- if several incident cells are possible, keep all;
- if several incoming-edge states are possible, keep all;
- if orientation/trace data has several native representatives, keep all;
- do not select a preferred lift to imitate the accepted circle.

Record the projection maps

`segment_state -> current cell`,

`segment_state -> free endpoint`,

and any other native state projection actually used.

Prove D6/reversal covariance of the lifted seed family.

Required output:

`R059D_STAGE_AR_ONE_STEP_SEGMENT_LIFTS.json`.

## 6. Stage C — derive the stateful candidate-neighbor relation

The current AQ cell has three edge-neighbors `N3(C)`.

For a line-segment state `S` with current cell `C`, determine which of these three are legitimate next cells **from segment semantics**, not from desired closure.

At minimum compare, without prematurely identifying them:

1. the AQ memoryless baseline `N3(C)`;
2. a possible incoming-edge/non-backtracking continuation relation, but only if Stage A proves incoming-edge state is meaningful;
3. endpoint-incidence-preserving continuation if derivable;
4. any segment-footprint continuity constraint proved native in Stage A.

The Researcher may find that all three remain legitimate, only two remain legitimate, or that the candidate relation depends on state.

Freeze the exact relation before applying the escape score.

Required output:

`R059D_STAGE_AR_STATEFUL_CANDIDATE_RELATION.json`.

## 7. Stage D — stateful farthest escape with all ties retained

The phrase “尽量远离原点” remains frozen in spirit.

Use AQ's source-free shell only as a **cell-position escape observable**:

`SHELL(C)=d_dual(STAR(O_E),C)`.

For state `S`, let `NEXT(S)` be the Stage C candidate state set and define

`FAR_STATE(S)=argmax_{S' in NEXT(S)} SHELL(cell(S'))`.

All tied maximizers survive.

Do not add a tie breaker.

Now prove the actual shell-increment law on the lifted state graph. Classify exactly which increments occur:

`Delta SHELL in {...}`.

The central question is whether state retention destroys AQ's theorem

`Delta SHELL = +1 always`.

Possible outcomes include:

- strict `+1` survives globally;
- `0` tangential steps appear;
- `-1` inward recovery steps appear;
- several increments coexist by branch;
- the state graph has another Lyapunov function and remains acyclic even if shell is not strict.

Required output:

`R059D_STAGE_AR_STATEFUL_ESCAPE_LAW.json`.

## 8. Stage E — jump-budgeted all-path stateful reachability

For independent micro-jump budget `J>=0`, define the complete stateful path family.

Freeze:

`ALL_ADMISSIBLE_REACHABLE_PATHS_ARE_VALID`.

Record separately:

- complete state paths;
- projected cell endpoints;
- projected free-endpoint native points;
- state multiplicity and projection multiplicity as provenance only;
- exact-J and up-to-J reachability.

Do not assume `J=r`, `J=length`, or `J=precision`.

Minimum exhaustive one-step census:

`J=0..64`

for all six D6 segment lifts, plus larger deterministic checkpoints if tractable.

Required output:

`R059D_STAGE_AR_STATEFUL_ESCAPE_CENSUS.json`.

## 9. Stage F — cycle, return, and closure audit before any old-circle comparison

Analyze the frozen stateful transition graph intrinsically.

Required questions:

1. Is the graph still a DAG?
2. Are there strongly connected components?
3. Does any positive-length state path return to its starting state?
4. Can the projected free endpoint close even if hidden segment state does not?
5. Do **all** branches close, only some branches close, or none?
6. Are there simple D6 cycles?
7. Is there a natural first-return time independent of a tuned jump budget?
8. Does reversal generate inverse path families?

Do not call a single lucky branch “the circle” while other equally admissible branches escape elsewhere.

A valid closure theorem must state its quantifiers over the entire set-valued family.

Required output:

`R059D_STAGE_AR_STATEFUL_CLOSURE_THEOREM.json`.

## 10. Stage G — one-step fixed-length meaning, without old-orbit leakage

The user is moving a line segment, so determine what “one-step length preserved” can mean in the new state model **without** calling AK orbit membership.

Start from the primitive axis anchor meaning:

one positive/negative primitive step from `O_E` reaches the corresponding `±2` axis state.

Ask whether Stage A provides an independent native invariant that extends this one-step length meaning to non-axis intermediate segment states.

Accept any of the following exact outcomes:

1. a source-free pre-circle segment-length invariant is derived;
2. only a partial one-step admissibility test is derivable;
3. no such extension is available without importing later circle/support structure.

If outcome 3 holds, freeze it as a genuine foundational gap rather than using coordinate magnitude or source distance as a substitute.

Required output:

`R059D_STAGE_AR_PRE_CIRCLE_LENGTH_AUDIT.json`.

## 11. Stage H — separately typed AL support-carrier experiment

Only after Stages A–G are frozen, run a comparison arm using the already accepted native support carrier

`K_E(r)={p:SUP(p)<=9r^2}`

with the following restrictions:

- `SUP` is typed as support/incidence rank, never length;
- AL A8 frontier rule is disabled;
- AK `tau` is disabled as a transition oracle;
- the Stage D stateful escape law is unchanged;
- all tied branches remain valid.

Question:

> Does the independent support cap, combined with the stateful all-path escape rule, make the outer turn frontier emerge dynamically without A8?

At minimum test `r=1..32`, with exact proofs for the structural claim and larger deterministic replay if useful.

Possible outcomes:

- `AL_SUPPORT_CARRIER_PLUS_ESCAPE_DERIVES_AL_FRONTIER`;
- `AL_SUPPORT_CARRIER_PLUS_ESCAPE_CONTAINS_AL_FRONTIER_BUT_REMAINS_BRANCHING`;
- `AL_SUPPORT_CARRIER_DOES_NOT_REPAIR_ESCAPE_CLOSURE`.

This arm may not alter the primary AR transition law retroactively.

Required output:

`R059D_STAGE_AR_AL_SUPPORT_ESCAPE_AUDIT.json`.

## 12. Stage I — post-freeze comparison to AP/AK/AL circle

Only now compare the frozen AR projected endpoint object with:

- AP-REISSUE one-step visible six-axis orbit;
- AK fixed-length `tau` orbit;
- AL canonical support frontier.

Determine whether the AR path family:

1. equals the accepted turn orbit as a set-valued object;
2. contains the accepted orbit among additional lawful branches;
3. projects onto the accepted endpoint cycle while hidden states differ;
4. remains nonclosing/distinct;
5. cannot be compared because pre-circle segment length is underdefined.

No path may be pruned because it misses the old circle.

Required output:

`R059D_STAGE_AR_CIRCLE_RELATION_AUDIT.json`.

## 13. Primary theorem targets

Use the strongest justified disposition, without forcing the preferred one.

Preferred if true:

`STATEFUL_ALL_PATH_SEGMENT_ESCAPE_DERIVES_NATIVE_TURN_CLOSURE__NO_SINGLE_PATH_SELECTOR_NEEDED`.

Other valid terminal dispositions:

1. `STATEFUL_ESCAPE_BREAKS_STRICT_SHELL_DAG__SET_VALUED_CLOSURE_REMAINS_OPEN`
2. `STATEFUL_ESCAPE_CONTAINS_CLOSED_TURN_BRANCHES__NONCLOSING_BRANCHES_ALSO_SURVIVE`
3. `STATEFUL_ESCAPE_REMAINS_ACYCLIC__SEGMENT_MEMORY_INSUFFICIENT`
4. `PRE_CIRCLE_STATEFUL_SEGMENT_LIFT_UNDERDEFINED`
5. `PRE_CIRCLE_FIXED_LENGTH_INVARIANT_UNDERDEFINED__SUPPORT_CARRIER_REQUIRED`
6. `AL_SUPPORT_CARRIER_PLUS_ESCAPE_DERIVES_FRONTIER__PRIMARY_ESCAPE_ALONE_INSUFFICIENT`
7. an exact stronger countertheorem supported by proof.

## 14. Mandatory firewalls

- `0` never becomes a native coordinate.
- Do not use source circle/angle/pi to define target transitions.
- Do not use AK `tau` or `SEG_E(r)` membership to define the primary AR state or candidate relation.
- Do not use AL A8 to select a path in the primary AR construction.
- Keep all legitimate segment lifts.
- Keep all tied FAR_STATE branches.
- Path multiplicity is not probability.
- `J` is independent until a theorem relates it to another native parameter.
- Do not modify prior-stage result files.
- Proof is primary; checker evidence is secondary.

## 15. Deterministic validation

After theorem statements are frozen, validate at minimum:

- every Stage A state invariant on all enumerated one-step lifts;
- D6/reversal covariance;
- candidate relation completeness;
- all FAR_STATE ties;
- `Delta SHELL` classification;
- exhaustive `J=0..64` stateful replay;
- BFS/DFS or two independently coded reachability traversals;
- SCC/cycle/return audit;
- projection multiplicity;
- no-native-zero firewall;
- no AK/AL-A8/source leakage in primary transitions;
- AL support arm only after primary freeze;
- prior-stage immutability through external GitHub compare.

## 16. Stop condition

Stop for Driver review after Stage I and checkpoint freeze.

Do not consume a later stage automatically.
