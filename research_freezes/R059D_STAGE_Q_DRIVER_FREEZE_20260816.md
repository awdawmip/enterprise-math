# R059D Stage Q — Driver Freeze

Status: `DRIVER_ACCEPTED_FROZEN`
Date: `2026-08-16`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-q-brc-cross-scale-torsor-synchronization`
Frozen owner head: `6e3e8334ab773a1b5710652da5dadc790fcf583a`
Frozen parent: Stage-P `a621f80d0294f5a5139eb4a2ed26e552e6368b18`
Taskbook source: `c13713d68635b51c78e9fd3e589a63230b441de5`

## Accepted freezes

- `BRC_RELATIVE_CONSTRAINT_SYNCHRONIZATION_ESTABLISHED`
- `CONNECTED_CONSISTENT_RELATIVE_BRC_COMPONENT_HAS_GLOBAL_Z2_TORSOR_AMBIGUITY`
- `GLOBAL_Z2_TORSOR_AMBIGUITY_ESTABLISHED`
- `ONE_EXACT_ANCHOR_SYNCHRONIZES_CONNECTED_COMPONENT`
- `ONE_ANCHOR_GLOBAL_COMPONENT_INITIALIZATION_ESTABLISHED`
- `ODD_PARITY_CYCLE_INCONSISTENCY_DETECTED`
- `CROSS_SCALE_POST_CREDIT_FIXED_POINT_ESTABLISHED` within finite acyclic pairwise-XOR factor trees
- `CROSS_SCALE_LOCAL_PROPAGATION_INSUFFICIENT` for unary-only cyclic propagation without cycle parity/correlation
- `CENTERED_GAP_TAU_ODD_CARRIER_ESTABLISHED`
- `CENTERED_GAP_CONTEXT_DOES_NOT_BY_ITSELF_SELECT_BRANCH`

## Exact component theorem

For a connected consistent relative constraint component

`b_u xor b_v = c_uv`,

choose root `r` and rooted parity `p_v`. Every solution is

`b_v = a xor p_v`, `a in {0,1}`.

Thus an unanchored connected component has exactly two globally complementary solutions. One independently justified exact singleton anchor fixes `a` and all nodes. An odd-parity cycle is inconsistent. With `u` unanchored consistent components, the joint solution count is `2^u`.

## Important boundaries

- Global complement is an exact torsor symmetry of the relative constraint system, but `GAUGE_EQUIVALENCE_NOT_ESTABLISHED`.
- Individual completed endpoints, individual bits and signed residues can change under global complement.
- `eta(q;L,U)=2q-L-U` is endpoint-reflection odd and, in the proved affine-linear class, unique up to scale; its sign is not a selector.
- For square completion `5 in (4,9)`, `eta=-3`, but `SCALAR_5_ABSOLUTE_SELECTOR_STILL_NONIDENTIFIED`.
- No independently justified absolute anchor is supplied by the bare Stage-Q substrate; `ABSOLUTE_INITIAL_SELECTOR_STILL_NONIDENTIFIED`.
- Pairwise-XOR synchronization is established only for the frozen class and is not declared the universal form of every future BRC mechanism.

## Validation

Deterministic checker: `3199/3199 PASS`.

Stage P and earlier artifacts remain immutable.
