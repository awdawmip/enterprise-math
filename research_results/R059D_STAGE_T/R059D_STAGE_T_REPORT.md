# R059D Stage T — Full D12 Straightness / Unoriented Axis Memory / Orientation Reversal Separation

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `89cb38967d0780d40d06f528deb73640f398cb89`  
Frozen parent: `7ec96d50055203293fe1161264246e1ccba88c84`

## Primary correction

Stage-S `donor_(k+1)=donor_k` is a fixed-recipient specialization only. For unrestricted `D12`, the frozen straightness definition is:

`STRAIGHT(sequence) iff the realized displacement vectors generate a rank-one integer submodule`.

Since project PATH semantics allow immediate reversal, both `t` and `-t` may occur in one straight sequence.

## Full D12 theorem

For `D12={e_i-e_j:i!=j}`, every primitive transfer has one `+1` and one `-1`. Two D12 primitives are Z-linearly dependent iff they are equal or additive inverses. Hence a nonempty D12 history is rank-one iff all transfers use one unordered carrier pair `{i,j}`.

Freeze:

- `FULL_D12_RANK_ONE_IFF_SINGLE_UNORIENTED_AXIS`
- `STRAIGHTNESS_FULL_AXIS_MEMORY_CONTINUATION_LAW_ESTABLISHED`
- `IMMEDIATE_REVERSAL_IS_STRAIGHT_UNDER_RANK_ONE_DEFINITION`

The exact continuation rule is:

`axis_(k+1)=axis_k`

while either orientation on that axis remains admissible.

Therefore rank-one straightness does **not** select orientation.

## Axis / orientation factorization

`D12` is the disjoint union of six two-state fibers:

`A_ij={e_i-e_j,e_j-e_i}`.

`S4` acts transitively on the six unordered axes. The stabilizer of one axis has order 4 and is `S2 x S2`, so the six-axis set is not an S4 torsor.

Conditional on a fixed axis, orientation reversal `t -> -t` acts freely and transitively on the two directed states, giving a free Z2 torsor with no preferred origin.

## Memory minimality

For unrestricted straight continuation, the previous unoriented axis is sufficient: it determines the exact admissible next-transfer fiber `{t,-t}`.

It is also representation-minimal. The six axis fibers are pairwise disjoint; any context alphabet with fewer than six states must identify two distinct axes, after which no nonempty next-transfer set can be safe for both histories.

Thus:

`minimum full-D12 straightness context cardinality = 6`.

The previous directed transfer (12 states) is sufficient but nonminimal; previous recipient, previous donor, or orientation-only contexts are insufficient.

## Stage-S reduction

With recipient `i` fixed, the inverse of `e_i-e_j` is `e_j-e_i`, whose recipient is `j`, so it is excluded from the fixed-recipient candidate set. Inside that restricted set, same unordered axis is exactly same donor.

Thus:

`STAGE_S_FIXED_RECIPIENT_DONOR_MEMORY_IS_SPECIALIZATION_OF_FULL_AXIS_MEMORY`.

## S4 initial-axis symmetry no-go

At a fully S4-symmetric local state, a deterministic S4-equivariant unique axis selector would have to choose an S4-fixed axis. No such axis exists.

Because the six-axis set is transitive, an S4-invariant exact feasible subset is either empty or all six axes; invariant post-credit alone cannot produce a singleton.

Freeze:

- `STATELESS_S4_EQUIVARIANT_UNIQUE_AXIS_SELECTOR_IMPOSSIBLE_AT_FULLY_SYMMETRIC_STATE`
- `S4_INVARIANT_POST_CREDIT_CANNOT_INITIALIZE_UNIQUE_AXIS_AT_FULLY_SYMMETRIC_STATE`

## Orientation fiber

Once an axis has been independently selected, its two directed orientations form a Z2 torsor. At an orientation-symmetric state, the Stage-P/O swap-equivariant no-go applies: no stateless equivariant unique orientation exists without independent tau-odd context.

However, straightness does not provide an orientation continuation law. Both `t -> t` and `t -> -t` remain rank-one, so previous orientation is not a straightness selector.

Immediate reversal is therefore exactly compatible with full-axis straightness.

## d-dimensional audit

For integer `d>=2`, with `d+1` carriers and directed transfers `{e_i-e_j}`:

- directed states: `d(d+1)`;
- unoriented axes: `d(d+1)/2`;
- two orientations per axis;
- rank-one iff one unordered carrier pair is used;
- immediate reversal remains straight;
- unrestricted straight-axis context cardinality: `d(d+1)/2`;
- fixed-recipient donor-memory cardinality: `d`.

This is algebraic only and does not establish physical dimensionality.

## Firewalls

No Euclidean angle/metric, visual straightness, shortest path, no-backtracking, velocity/momentum, physical probability, frozen `+/-` preference, scalar midpoint selector, hidden axis ordering, or random tie-break is used as a positive premise.

## Checker

Deterministic checker: `17667 / 17667 PASS`.

Checks digest:

`dc516daafd4f02ca1d9e8b381d17bce8fae4e4796d2e174166b8daed26e02c51`

The parent immutability gate passed before the final checker run.

## Current boundaries

- initial absolute axis at a bare fully S4-symmetric state: `NOT_IDENTIFIED`;
- orientation within a selected axis: `NOT_SELECTED_BY_RANK_ONE_STRAIGHTNESS`;
- physical direction preference: `NOT_ESTABLISHED`;
- physical probability: `NOT_ESTABLISHED`;
- physical dimensionality: `NOT_ESTABLISHED`.

`STOP_FOR_DRIVER_REVIEW`
