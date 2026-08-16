# R059D Stage U — BRC Stabilizer-Filtered Contextual Selector Calculus

Task-ID: `RS-R059D-STAGE-U-BRC-STABILIZER-FILTERED-CONTEXTUAL-SELECTOR-CALCULUS`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-u-brc-stabilizer-context-selector`
Frozen parent: `c78ff5956a237c36eb6f51c2889eba5882271b81`

## 0. Scope and frozen inputs

Stage T is accepted and immutable.

Read as project-level sources:

- `PROJECT_DEFINITION.md`
- `PROJECT_DEFINITION.zh-CN.md`
- `FOUNDATIONAL_LOGIC.md`
- `native_semantics_admissibility.json`
- `RELATIONAL_AXIS_CONVENTION.md`
- `relational_axis_convention.json`
- `THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md`
- `three_dimensional_relational_axis_convention.json`
- `research_notes/R059D_STAGE_T_DRIVER_FREEZE_20260816.md`

Project mode remains `REFOUND, NOT REJECT`.

Do not mutate Stage O/P/Q/R/S/T artifacts.

## 1. Core scientific question

Stages O/P/S/T repeatedly established symmetry no-go results for different output fibers:

- two-branch Z2 orientation/branch fibers;
- three-donor S3 homogeneous branch set;
- six-axis S4 homogeneous branch set;
- two-orientation Z2 fiber on one selected axis.

Stage U must replace these case-by-case statements by one exact finite-group selector theorem.

The target is not a score and not a probability.

Let a finite group `G` act on a typed exact input/context space `X` and an output candidate space `Y`.

Let `A(x) subseteq Y` be the exact feasible output set after completion legality and independently declared algebraic/post-credit constraints.

Assume the feasibility relation is G-equivariant:

`A(g.x)=g.A(x)`.

For `x in X`, define

`H_x = Stab_G(x)`

and

`Fix_Y(H_x) = {y in Y : h.y=y for every h in H_x}`.

Define the stabilizer-filtered feasible set

`E(x)=A(x) intersect Fix_Y(H_x)`.

Stage U must prove the exact role of `E(x)` for deterministic G-equivariant selection.

## 2. Stage U0 — orbit-extension theorem

Prove or refute:

Given one orbit `G.x`, an assignment `f(x)=y` extends by

`f(g.x)=g.y`

to a well-defined deterministic G-equivariant selector on that orbit iff

1. `y in A(x)`, and
2. `H_x <= Stab_G(y)`,

which is equivalent to

`y in E(x)`.

The proof must explicitly handle representative independence:

if `g1.x=g2.x`, then `g2^{-1}g1 in H_x`, so well-definedness requires the chosen `y` to be H_x-fixed.

Then classify:

- `E(x)=empty` -> `EQUIVARIANT_DETERMINISTIC_SELECTOR_IMPOSSIBLE_ON_ORBIT`;
- `|E(x)|=1` -> `UNIQUE_EQUIVARIANT_OUTPUT_FOR_FROZEN_FEASIBILITY_RELATION`;
- `|E(x)|>1` -> `EQUIVARIANT_OUTPUT_NONCANONICAL_WITH_CURRENT_CONTEXT_AND_CONSTRAINTS`.

Do not call singleton uniqueness universal or physical. It is unique only relative to the declared G-action, input/context, and exact feasible relation A.

## 3. Context theorem

Let input be `(s,h)` with diagonal G-action.

Study how adding exact context changes

`H_{(s,h)} = Stab_G(s,h)`

and `A(s,h)`.

Critical required distinction:

`SYMMETRY_BREAKING_CONTEXT_IS_NECESSARY_IN_MANY_NO_GO_CASES_BUT_NOT_SUFFICIENT_FOR_UNIQUE_SELECTION`.

Shrinking the stabilizer may enlarge `Fix_Y(H)` rather than force a unique y. A separate exact feasible constraint may still be required.

Construct explicit positive and negative examples.

## 4. Required replay: Stage O/P Z2 branch/orientation fiber

Take `G=Z2`, `Y={0,1}` with flip action.

### Fully symmetric input

`H=Z2`.

Prove:

`Fix_Y(H)=empty`.

Recover the frozen stateless symmetry no-go.

### Tau-odd two-state context

Let context itself have free Z2 action, so at a chosen nonfixed context state `H={e}`.

Then

`Fix_Y(H)=Y`.

This must demonstrate that symmetry breaking alone allows both outputs and does not by itself select one.

Only if exact constraints reduce `A` to `{0}` or `{1}` may Stage U return a unique selector.

This must recover the Stage-P singleton criterion without arbitrary preference.

## 5. Required replay: Stage S three-donor fiber

For fixed recipient, let `G=S3` act naturally on the three donors `Y={d2,d3,d4}`.

### Fully symmetric input

`H=S3` -> prove `Fix_Y(H)=empty`.

Recover Stage-S stateless donor no-go.

### Preexisting donor-relation context

Let h be one independently preexisting donor relation, transforming naturally under S3.

At h=d2, `H=Stab(d2) ~= S2`.

Compute `Fix_Y(H)` exactly.

Test whether it is singleton `{d2}`.

If yes, distinguish carefully:

- context has enough typed relational information to make the donor itself the only symmetry-compatible donor;
- this is valid only when the donor relation genuinely exists before the collapse and is not copied from the output being selected.

## 6. Required replay: Stage T six-axis S4 fiber

Let `G=S4` act on the six unordered axes

`Y_axis={{i,j}:1<=i<j<=4}`.

### Fully symmetric input

`H=S4` -> `Fix_Y(H)=empty`.

Recover Stage-T axis no-go.

### One-carrier context

Fix carrier `X1`; then `H~=S3` on the other carriers.

Compute `Fix_Y(H)` exactly.

Do not assume any axis is fixed.

### Preexisting unoriented-axis context

Let h={1,2}. Then

`H=Stab({1,2}) ~= S2 x S2`.

Compute all H-fixed axes exactly.

Priority test:

Does `Fix_Y(H)` contain both `{1,2}` and its complementary disjoint axis `{3,4}`?

If yes, freeze an explicit negative result:

`PREEXISTING_AXIS_CONTEXT_ALONE_DOES_NOT_CANONICALLY_IDENTIFY_AXIS_OUTPUT_UNDER_FULL_S4_EQUIVARIANCE`

unless additional exact constraints remove the complementary fixed axis.

### Preexisting directed-transfer context

Take h=(recipient=1, donor=2), with exact S4 transformation law.

Compute its stabilizer and the fixed set in:

- the six-axis output space;
- the full D12 directed-state output space.

Do not assume that ordered context alone uniquely selects the same directed transfer. Score the exact fixed sets.

This is a high-priority anti-circularity audit.

## 7. Axis/orientation hierarchical selector

Use the frozen exact factorization

`D12 -> AXIS x ORIENTATION_FIBER`.

Construct a two-stage selector calculus:

1. axis feasibility/symmetry filtering;
2. conditional orientation feasibility/symmetry filtering after an axis is selected.

For each stage define its own:

- group action;
- stabilizer;
- exact feasible set;
- filtered feasible set E.

Prove that rank-one straightness supplies:

`A_axis = {previous_unoriented_axis}`

for continuation after a nonempty straight history, hence forces the axis if the previous axis is valid context.

But for orientation it supplies

`A_orient = {+,-}`

and therefore does not force orientation.

Do not introduce no-backtracking, velocity, momentum, visual straightness, or a frozen sign preference.

## 8. Scalar midpoint control

Replay Stage R in the same selector language without falsely forcing it into S4/Z2 vector symmetry.

For an ordered scalar gap `L<q<U`:

- completion legality gives A={L,U};
- endpoint reflection acts on the family of states/gaps;
- at exact midpoint q=(L+U)/2, the input is reflection-fixed and endpoint fiber has no reflection-fixed singleton, reproducing no-go;
- away from midpoint, the local stabilizer may be trivial, so the stabilizer filter alone leaves both endpoints possible.

Therefore Stage U must explicitly show why order monotonicity / the Stage-R midpoint-core axiom package contributes information to A beyond symmetry filtering.

Freeze if proved:

`STABILIZER_FILTERING_UNIFIES_SYMMETRY_NO_GO_BUT_DOES_NOT_REPLACE_ORDER_POST_CREDIT_AXIOMS`.

## 9. Post-credit interpretation

Retype exact post-credit as a source of constraints that shrink `A(x)`, not as an arbitrary scalar reward.

Examples:

- relative straightness may turn six possible axes into a singleton previous axis;
- symmetric supervision may leave A unchanged;
- independent oriented macro certificate may produce a singleton;
- branch-conditioned readout reused as its own certificate remains circular and rejected.

Formal target:

`BRC_SELECTABLE_SET(x) = EXACT_FEASIBLE_SET(x) intersect SYMMETRY_FIXED_OUTPUT_SET(x)`.

If this formula is established, freeze it only within the declared finite-group equivariant selector calculus.

Do not promote it as a universal law for every future nonlinear/multi-endpoint BRC mechanism without proof.

## 10. Registry and counterexamples

Freeze before scoring a finite exact registry including at least:

- Z2 symmetric branch;
- Z2 tau-odd context with A full;
- Z2 tau-odd context with singleton A;
- S3 fully symmetric donor;
- S3 donor context;
- S4 fully symmetric six-axis state;
- S4 one-carrier context;
- S4 axis context;
- S4 directed-transfer context;
- straight-history axis continuation;
- orientation continuation under straightness;
- scalar midpoint;
- scalar non-midpoint with bare completion;
- inconsistent exact feasible set.

Tiny enumeration may verify group actions, but symbolic stabilizer/fixed-set proofs must be primary.

## 11. Firewalls

Forbidden as positive selector premises:

- nearest rounding;
- Euclidean distance/angle/norm;
- endpoint argmax;
- arbitrary reward weights;
- ML fitting;
- hidden coordinate/axis order;
- random tie-break;
- physical probability from symmetry;
- physical direction preference;
- no-backtracking;
- treating serialization `+/-` labels as native orientation evidence.

## 12. Required artifacts

At minimum freeze:

1. `R059D_STAGE_U_FINITE_GROUP_SELECTOR_PROTOCOL.json`
2. `R059D_STAGE_U_ORBIT_EXTENSION_THEOREM.json`
3. `R059D_STAGE_U_STABILIZER_FILTERED_FEASIBLE_SET_THEOREM.json`
4. `R059D_STAGE_U_CONTEXT_STABILIZER_LEDGER.json`
5. `R059D_STAGE_U_Z2_REPLAY.json`
6. `R059D_STAGE_U_S3_DONOR_REPLAY.json`
7. `R059D_STAGE_U_S4_AXIS_REPLAY.json`
8. `R059D_STAGE_U_DIRECTED_TRANSFER_CONTEXT_AUDIT.json`
9. `R059D_STAGE_U_AXIS_ORIENTATION_HIERARCHICAL_SELECTOR.json`
10. `R059D_STAGE_U_SCALAR_MIDPOINT_CONTROL.json`
11. `R059D_STAGE_U_POST_CREDIT_AS_FEASIBILITY_REDUCTION.json`
12. `R059D_STAGE_U_COUNTEREXAMPLE_REGISTRY.json`
13. deterministic checker + output
14. report
15. manifest
16. frozen checkpoint

## 13. Success boundary

Positive outcomes may include:

- `STABILIZER_FILTERED_EQUIVARIANT_SELECTOR_THEOREM_ESTABLISHED`
- `BRC_SELECTABLE_SET_EQUALS_EXACT_FEASIBLE_INTERSECT_STABILIZER_FIXED_SET`
- `SYMMETRY_BREAKING_CONTEXT_NOT_SUFFICIENT_WITHOUT_FEASIBILITY_SINGLETON`
- `PREEXISTING_AXIS_CONTEXT_RETAINS_COMPLEMENT_AXIS_AMBIGUITY`
- `STRAIGHTNESS_FORCES_AXIS_BUT_NOT_ORIENTATION`

Negative outcomes are equally valid and must be preserved.

Do not claim a universal physical BRC law.

After all artifacts/checker/checkpoint:

`STOP_FOR_DRIVER_REVIEW`
