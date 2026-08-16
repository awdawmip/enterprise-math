# R059D Stage T Driver Freeze

Status: DRIVER_ACCEPTED / IMMUTABLE RESULT
Date: 2026-08-16
Researcher-ID: `EM-R059D-9C6B2A`
Taskbook source: `89cb38967d0780d40d06f528deb73640f398cb89`
Owner branch: `research/r059d-stage-t-brc-3d-axis-memory-orientation-reversal`
Frozen parent: `7ec96d50055203293fe1161264246e1ccba88c84`
Final owner head: `c78ff5956a237c36eb6f51c2889eba5882271b81`

## Driver disposition

`VALID_FULL_AXIS_STRAIGHTNESS_RETYPE_WITH_ORIENTATION_SEPARATION`

Accepted freezes:

- `FULL_D12_PRIMITIVE_DEPENDENCE_IFF_EQUAL_OR_INVERSE`
- `FULL_D12_RANK_ONE_IFF_SINGLE_UNORIENTED_AXIS`
- `IMMEDIATE_REVERSAL_IS_STRAIGHT_UNDER_RANK_ONE_DEFINITION`
- `D12_EXACT_AXIS_ORIENTATION_FACTORIZATION_ESTABLISHED`
- `FIXED_AXIS_ORIENTATION_FIBER_IS_FREE_Z2_TORSOR`
- `SIX_AXIS_SET_IS_TRANSITIVE_S4_HOMOGENEOUS_SET_NOT_TORSOR`
- `STRAIGHTNESS_FULL_AXIS_MEMORY_CONTINUATION_LAW_ESTABLISHED`
- `STRAIGHTNESS_DOES_NOT_SELECT_AXIS_ORIENTATION`
- `PREVIOUS_UNORIENTED_AXIS_IS_REPRESENTATION_MINIMAL_CONTEXT_FOR_FULL_D12_STRAIGHT_CONTINUATION`
- `STAGE_S_FIXED_RECIPIENT_DONOR_MEMORY_IS_SPECIALIZATION_OF_FULL_AXIS_MEMORY`
- `STATELESS_S4_EQUIVARIANT_UNIQUE_AXIS_SELECTOR_IMPOSSIBLE_AT_FULLY_SYMMETRIC_STATE`
- `S4_INVARIANT_POST_CREDIT_CANNOT_INITIALIZE_UNIQUE_AXIS_AT_FULLY_SYMMETRIC_STATE`
- `STATELESS_SWAP_EQUIVARIANT_UNIQUE_ORIENTATION_SELECTOR_IMPOSSIBLE_AT_ORIENTATION_SYMMETRIC_STATE`
- `STRAIGHTNESS_LEAVES_ORIENTATION_UNRESOLVED`
- `D_DIMENSIONAL_FULL_STRAIGHTNESS_AXIS_MEMORY_PATTERN_ESTABLISHED_ALGEBRAICALLY_FOR_D_GE_2`

## Core correction

Stage-S `donor_(k+1)=donor_k` is a fixed-recipient specialization only.

For unrestricted `D12`, a nonempty history is straight iff all realized primitive transfers lie in one unordered axis fiber

`A_ij={e_i-e_j,e_j-e_i}`.

Thus exact straight continuation preserves `AXIS` but does not preserve or select `ORIENTATION`.

Immediate reversal `t,-t` remains rank-one and is therefore straight under the frozen rank-one definition.

The minimum representation context for exact unrestricted straight continuation is the previous unoriented axis: 6 states. Previous directed transfer is sufficient but nonminimal.

## Symmetry boundary

The six-axis set is the transitive `S4/(S2 x S2)` homogeneous set, not an S4 torsor. A fully S4-symmetric local state admits no deterministic stateless S4-equivariant unique axis selector.

Conditional on a selected axis, its two orientations form a free Z2 torsor with no preferred origin. Straightness itself supplies no orientation selector, including after a previous orientation exists.

## Checker

`17667/17667 PASS`
Digest: `dc516daafd4f02ca1d9e8b381d17bce8fae4e4796d2e174166b8daed26e02c51`

Stage T is frozen. Do not mutate the owner artifacts.
