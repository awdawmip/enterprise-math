# R059D Stage T — Full D12 Straightness / Unoriented Axis Memory / Orientation Reversal Separation

Task-ID: `RS-R059D-STAGE-T-BRC-3D-FULL-AXIS-STRAIGHTNESS-ORIENTATION-REVERSAL`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-t-brc-3d-axis-memory-orientation-reversal`
Frozen parent: `7ec96d50055203293fe1161264246e1ccba88c84`

## 0. Frozen inputs and immutability

Stage S is frozen and immutable. Read but do not modify its artifacts.

Read and obey:

- `PROJECT_DEFINITION.md`
- `FOUNDATIONAL_LOGIC.md`
- `PACKET_PATH_FOUNDATION.md`
- `THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md`
- `three_dimensional_relational_axis_convention.json`
- `research_notes/R059D_STAGE_S_DRIVER_FREEZE_20260816.md`

Project mode remains `REFOUND, NOT REJECT`.

## 1. Scientific correction

Stage S proved a **fixed-recipient** theorem:

`donor_(k+1)=donor_k`

for rank-one straight continuation.

This must not be promoted to full-path straightness. Project PATH semantics explicitly allow immediate reversal and repeated adjacency. Under the frozen definition

`STRAIGHT(sequence) iff realized displacement vectors generate a rank-one integer submodule`,

a sequence may contain both `t` and `-t` and remain straight.

Stage T must determine the exact full-`D12` straightness law.

## 2. Frozen 3D transfer carrier

Use

`Lambda3={(d1,d2,d3,d4) in Z^4 : d1+d2+d3+d4=0}`

and

`D12={e_i-e_j : i!=j}`

with frozen notation

`{±u,±v,±w,±p,±q,±r}`.

Axis names/signs are notation only.

## 3. Unoriented transfer-axis primitive

For each unordered carrier pair `{i,j}`, define the candidate unoriented axis class

`A_{ij}={e_i-e_j, e_j-e_i}`.

There are exactly `C(4,2)=6` such classes.

Must prove or refute:

`FULL_D12_RANK_ONE_IFF_SINGLE_UNORIENTED_AXIS`

meaning that a nonempty sequence `t_1,...,t_n in D12` has rank-one integer span iff there exists one unordered pair `{i,j}` such that every `t_k in A_{ij}`.

Proof must include the primitive-vector fact that two `D12` vectors are Z-linearly dependent iff they are equal or additive inverses.

## 4. Immediate reversal audit

Mandatory exact cases:

- `t,t,t`
- `t,-t,t,-t`
- `t,-t`
- `t,s` with `s` on a different axis
- `t,-s` with different unordered carrier pair

Freeze the correct status of immediate reversal under rank-one straightness.

If `t,-t` is straight, explicitly freeze:

`IMMEDIATE_REVERSAL_IS_STRAIGHT_UNDER_RANK_ONE_DEFINITION`.

Do not add monotonicity, shortest-path, no-backtracking, velocity, or physical direction assumptions.

## 5. Axis versus orientation factorization

For each directed transfer `e_i-e_j`, separate:

- `AXIS={i,j}` — unordered pair;
- `ORIENTATION=(j -> i)` — directed donor/recipient relation on that axis.

Prove or refute exact factorization of the 12 directed states into six 2-state orientation fibers.

This is a relational factorization only. Do not infer physical positive direction from the frozen `+u,+v,...` notation.

Audit symmetry:

- `S4` action on six unordered axes;
- stabilizer of one axis;
- transitivity and freeness;
- orientation swap within a fixed axis;
- whether the orientation fiber is a free Z2 torsor once an axis is fixed.

Do not call the six-axis set an S4 torsor unless free+transitive is actually proved.

## 6. Full straightness memory law

Using only rank-one straightness, derive the exact continuation condition on full `D12` histories.

Priority hypothesis:

`axis_(k+1)=axis_k`

while orientation may be either sign.

Must prove or refute:

`STRAIGHTNESS_FULL_AXIS_MEMORY_CONTINUATION_LAW_ESTABLISHED`

and explicitly determine whether straightness constrains orientation at all.

If both signs remain admissible, freeze:

`STRAIGHTNESS_DOES_NOT_SELECT_AXIS_ORIENTATION`.

## 7. Minimal context audit

For continuation over all 12 directed states, audit minimum context needed to preserve rank-one straightness.

Candidate contexts:

- previous directed transfer (12 states)
- previous donor relation
- previous unoriented axis (6 states)
- previous recipient only (4 states)
- previous donor only (4 states)
- Boolean orientation only (2 states)
- composite encodings

Prove minimality in exact finite-state/cardinality terms where possible.

Priority expected result:

previous unoriented axis is sufficient and representation-minimal for unrestricted full-D12 straight continuation.

But do not freeze this unless proved.

## 8. Recover Stage-S fixed-recipient theorem as specialization

Show exactly why, when recipient `i` is frozen, the inverse transfer `e_j-e_i` no longer belongs to the allowed fixed-recipient candidate set.

Then recover Stage S:

`same axis under fixed recipient` iff `same donor`.

Freeze only if exact:

`STAGE_S_FIXED_RECIPIENT_DONOR_MEMORY_IS_SPECIALIZATION_OF_FULL_AXIS_MEMORY`.

## 9. Initial-axis symmetry no-go

At a fully `S4`-symmetric local state, study the six-axis branch set under carrier permutations.

Prove or refute:

`STATELESS_S4_EQUIVARIANT_UNIQUE_AXIS_SELECTOR_IMPOSSIBLE_AT_FULLY_SYMMETRIC_STATE`.

Also test whether S4-invariant exact post-credit can reduce the six-axis set to a singleton without independent symmetry-breaking context.

As before, hidden axis ordering, frozen axis names, random selection, and Euclidean geometry are forbidden as positive selector evidence.

## 10. Orientation initialization after axis selection

Conditional on an axis `{i,j}` already being selected by an independent exact context, the remaining two directed states form an orientation fiber.

Audit whether the Stage-P/O Z2 symmetry logic applies exactly to this two-state fiber:

- stateless swap-equivariant unique orientation selector at an orientation-symmetric state;
- tau-odd contextual singleton criterion;
- continuation versus initialization;
- immediate reversal compatibility.

Do not transfer scalar midpoint law into orientation selection unless an independently typed ordered completion gap is actually present.

## 11. Contextual exact feasible sets

Define exact feasible sets separately for axis and orientation:

`A_axis(s,h) subseteq six axes`

and, conditional on chosen axis,

`A_orient(s,h,axis) subseteq {+,-}`.

Classify cardinalities exactly and preserve multibranch ambiguity.

No argmax, arbitrary weights, nearest rounding, ML fitting, or random tiebreak.

## 12. d-dimensional generalization audit

For integer `d>=2`, Stage S gives `d+1` carriers and directed transfers `{e_i-e_j}`.

Audit the full straightness generalization:

- unoriented axis count `d(d+1)/2`;
- directed orientations 2 per axis;
- rank-one iff one unordered carrier pair is used;
- reversal remains straight;
- full straightness context cardinality candidate `d(d+1)/2`;
- fixed-recipient donor-memory cardinality `d` as a scoped specialization.

This is algebraic only; do not infer physical dimensionality.

## 13. Required artifacts

At minimum freeze:

1. `R059D_STAGE_T_FULL_D12_STRAIGHTNESS_PROTOCOL.json`
2. `R059D_STAGE_T_UNORIENTED_AXIS_PARTITION.json`
3. `R059D_STAGE_T_IMMEDIATE_REVERSAL_AUDIT.json`
4. `R059D_STAGE_T_AXIS_ORIENTATION_FACTORIZATION.json`
5. `R059D_STAGE_T_FULL_AXIS_MEMORY_CREDIT.json`
6. `R059D_STAGE_T_MEMORY_MINIMALITY_LEDGER.json`
7. `R059D_STAGE_T_FIXED_RECIPIENT_REDUCTION.json`
8. `R059D_STAGE_T_S4_AXIS_SYMMETRY_NOGO.json`
9. `R059D_STAGE_T_ORIENTATION_FIBER_CONTEXT_PROTOCOL.json`
10. `R059D_STAGE_T_D_DIMENSIONAL_FULL_STRAIGHTNESS_LEDGER.json`
11. `R059D_STAGE_T_TRIVIALITY_LEAKAGE_LEDGER.json`
12. deterministic checker + output
13. report
14. manifest
15. frozen checkpoint

## 14. Hard firewalls

Do not use as premises:

- Euclidean angle or metric
- visual straightness
- shortest path
- no-backtracking
- velocity or momentum
- physical probability
- frozen `+/-` notation as a preferred direction
- scalar midpoint selector as an orientation law
- Stage-S fixed-recipient result as a universal full-path theorem

Negative results must be preserved.

After all artifacts/checker/checkpoint are complete:

`STOP_FOR_DRIVER_REVIEW`.
