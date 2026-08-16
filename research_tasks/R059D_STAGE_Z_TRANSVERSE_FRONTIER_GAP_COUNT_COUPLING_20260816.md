# R059D Stage Z — Transverse Frontier / Gap-Count Coupling

Task-ID: `RS-R059D-STAGE-Z-TRANSVERSE-FRONTIER-GAP-COUNT-COUPLING`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-4E8B71`
Owner branch: `research/r059d-stage-z-transverse-frontier-gap-count`
Frozen parent: `bcbcb997104a1042408276b3ab9eb0aa01e30f91`

## 0. Frozen input

Stage Y is canonically frozen after append-only semantic retype and Researcher-ID correction.

Consume only these Stage-X/Y facts:

- in the explicit cyclic + u-ray-reflection subcase, `C(nu)=(n,-a_n,-a_n)`;
- `a_0=0`, `a_1=1`, `a_(n+1)-a_n in {0,1}`;
- every binary staircase extends to a global UNIT_STEP atlas;
- `REALIZED_TRANSVERSE_CROSSING_COUNT_IDENTITY_ESTABLISHED=true`, but this is post-realization bookkeeping only;
- `INDEPENDENT_COORDINATE_VALUE_COUNT_MEANING_ESTABLISHED=false`;
- `B2(k)={1,...,k}^2` has abstract count `k^2` and frontier increment `2k+1`;
- no primary-prefix -> full B2 pointwise bijection/occupancy coupling is established;
- raw reflection-equivariant pointwise enumeration of all B2 states is obstructed;
- root degree and `5->4/9` remain unresolved.

Do NOT revive stabilizer/post-credit as the primary mechanism.
Do NOT assume `n=a_n^2`, floor/ceil/nearest/midpoint, or Euclidean area.

## 1. Scientific target

Do not ask again what the whole coordinate value counts.

Ask the smaller elementary question:

> Between two successive completed transverse integer levels `k` and `k+1`, how many primary `+u` cell steps/events are intrinsically associated with the new transverse two-slot states introduced by that level change?

For the predeclared two-slot carrier:

`B2(k)={1,...,k}^2`

its new frontier is

`F2(k)=B2(k+1) \ B2(k)`

with exact cardinality

`|F2(k)|=(k+1)^2-k^2=2k+1`.

The target is to construct or refute an independently justified coupling between a primary staircase gap and `F2(k)`.

If such a coupling is established for every k, square thresholds must emerge by summing odd integers. If not, freeze the failure.

## 2. Jump/gap notation

Let

`j_n=a_(n+1)-a_n in {0,1}`.

Define the successive primary indices at which level k is reached using an explicit convention, and keep phase conventions separate.

At minimum distinguish:

- `ACTIVATION_INDEX A_k`: first n with `a_n=k`;
- `COMPLETION_INDEX C_k`: last n in the k-layer before the next jump, when finite;
- `GAP_k`: the finite primary interval associated with transition k->k+1 under the candidate semantics.

Do not silently choose one phase convention.

The task must express precisely which interval is claimed to correspond to the frontier `F2(k)`.

## 3. Predeclare frontier carriers before scoring

Freeze before any coupling test:

### 3.1 RAW_ORDERED_PAIR_FRONTIER

`F2(k)=B2(k+1)\B2(k)`.

Exact decomposition:

- new row: `{(k+1,j):1<=j<=k+1}`;
- new column excluding corner: `{(i,k+1):1<=i<=k}`;
- total `2k+1`.

Under transverse slot swap `(i,j)<->(j,i)`:

- one diagonal fixed state `(k+1,k+1)`;
- k off-diagonal two-element orbits.

### 3.2 SWAP_ORBIT_FRONTIER

Quotient the frontier by slot swap. Exact orbit count is `k+1`.

### 3.3 FRONTIER_INCIDENCE_COUNT

Count raw frontier incidences with orbit multiplicity: fixed orbit contributes 1, each off-diagonal orbit contributes 2. Total `2k+1`.

This is a count, not yet a primary-step correspondence.

No other frontier carrier may be added after scoring unless separately predeclared before use.

## 4. Constructive coupling gate

Search only for simple exact couplings between primary gap events and the predeclared frontier.

Allowed positive forms:

1. exact bijection from primary gap event IDs to raw frontier states;
2. reflection-equivariant map to swap orbits plus a separately proved multiplicity/incidence accounting that makes one primary step correspond exactly to one raw incidence;
3. exact recurrence showing that the k->k+1 staircase transition consumes exactly all and only the `2k+1` new frontier incidences;
4. another elementary finite-set correspondence frozen before observing the answer.

Every positive coupling must:

- be definable without knowing the desired square-root jump schedule;
- preserve transverse slot reflection without an arbitrary slot ordering;
- be cyclically transportable to v and w rays;
- have no skipped or repeated counted event unless multiplicity is explicitly proved;
- not use `a_n^2` as a premise.

If reflection obstruction still kills the raw pointwise map, preserve that failure rather than choosing a preferred slot.

## 5. Gap-length theorem if coupling succeeds

Only if the constructive coupling is proved, derive:

`|GAP_k|=2k+1`.

Then telescope exactly:

`1+3+5+...+(2k-1)=k^2`.

Audit the indexing/phase convention carefully to determine whether the resulting threshold is:

- activation at `k^2`;
- completion at `k^2`;
- or another fixed offset.

Do not call the result square root until the exact threshold indexing is established.

## 6. m-slot control

For `m=1..4`, define the frontier

`Fm(k)=Bm(k+1)\Bm(k)`

with exact count

`(k+1)^m-k^m`.

Use these only as controls to ask:

- does the same coupling construction generalize canonically to m slots?
- does the actual triaxial semantics single out two transverse slots, or do arbitrary m remain possible?

Do not infer physical dimension from m.

A positive square result requires a reason the native frontier has exactly two independently indexed transverse slots.

## 7. Direct small-k table

Without assuming any root law, write exact frontier tables for at least k=0..6:

`|F2(k)| = 1,3,5,7,9,11,13,...`

and cumulative counts:

`1,4,9,16,25,36,49,...`.

Then compare candidate primary staircase jump/gap patterns only after the coupling semantics is explicit.

This table is arithmetic control, not proof by pattern matching.

## 8. 5 -> 4 / 9 control

Only if a square frontier coupling plus phase convention is independently established, revisit n=5.

Report exactly whether the coupling places n=5 in the completed k=2 layer, activated k=3 layer, or another typed state.

Allowed positive freezes:

- `FIVE_TO_FOUR_FORCED_BY_FRONTIER_COUNT`
- `FIVE_TO_NINE_FORCED_BY_FRONTIER_COUNT`

Otherwise preserve:

- `FIVE_TO_FOUR_OR_NINE_UNRESOLVED`.

No midpoint, nearest rounding, vote across candidate semantics, or probability.

## 9. Required negative controls

Explicitly preserve failures for:

- arbitrary enumeration of raw B2 frontier states;
- slot-name-preferred fill orders;
- coordinate-derived jump-event set used as the frontier coupling itself;
- defining GAP_k from a desired square threshold and then counting it;
- assuming `|GAP_k|=2k+1` before proving a correspondence;
- Euclidean square area;
- global inversion unless separately justified;
- Stage-U stabilizer selector or Stage-V post-credit selector as the answer.

## 10. Required artifacts

At minimum:

1. `R059D_STAGE_Z_FRONTIER_CARRIER_REGISTRY.json`
2. `R059D_STAGE_Z_RAW_PAIR_FRONTIER_COUNT.json`
3. `R059D_STAGE_Z_SWAP_ORBIT_FRONTIER_AUDIT.json`
4. `R059D_STAGE_Z_PRIMARY_GAP_DEFINITION_PROTOCOL.json`
5. `R059D_STAGE_Z_CONSTRUCTIVE_FRONTIER_COUPLING_LEDGER.json`
6. `R059D_STAGE_Z_GAP_LENGTH_THEOREM.json`
7. `R059D_STAGE_Z_M_SLOT_FRONTIER_CONTROL.json`
8. `R059D_STAGE_Z_SMALL_K_ODD_SUM_TABLE.json`
9. `R059D_STAGE_Z_FIVE_TO_FOUR_OR_NINE_CONTROL.json`
10. `R059D_STAGE_Z_TRIVIALITY_LEAKAGE_LEDGER.json`
11. deterministic checker source/output
12. report
13. manifest
14. frozen checkpoint.

## 11. Allowed outcomes

Positive or negative are both valid. Useful freezes include:

- `TRANSVERSE_FRONTIER_COUNT_2K_PLUS_1_ESTABLISHED_AS_ABSTRACT_COUNT`
- `PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_ESTABLISHED`
- `PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_NOT_ESTABLISHED`
- `ODD_GAP_SEQUENCE_FORCES_SQUARE_THRESHOLDS`
- `TWO_SLOT_FRONTIER_NATIVELY_SELECTED`
- `M_SLOT_AMBIGUITY_REMAINS`
- `ROOT_DEGREE_REMAINS_UNIDENTIFIED`
- `FIVE_TO_FOUR_FORCED_BY_FRONTIER_COUNT`
- `FIVE_TO_NINE_FORCED_BY_FRONTIER_COUNT`
- `FIVE_TO_FOUR_OR_NINE_UNRESOLVED`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

After all artifacts and checks:

`STOP_FOR_DRIVER_REVIEW`.
