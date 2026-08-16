# R059D Stage U — BRC Stabilizer-Filtered Contextual Selector Calculus

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `320e0525f0aa4d5ccc9faec2a408187b2e6f9222`  
Frozen parent: `c78ff5956a237c36eb6f51c2889eba5882271b81`

## Primary theorem

Let a finite group `G` act on exact typed input/context space `X` and output candidate space `Y`. Let `A(x) subseteq Y` be an exact G-equivariant feasible relation and let `H_x=Stab_G(x)`.

Define:

`E(x)=A(x) intersect Fix_Y(H_x)`.

A choice `f(x)=y` extends by `f(g.x)=g.y` to a well-defined deterministic G-equivariant feasible selector on the orbit `G.x` iff `y in E(x)`.

Representative independence is exact: if `g1.x=g2.x`, then `g2^{-1}g1 in H_x`, so `g1.y=g2.y` iff `y` is fixed by `H_x`.

Therefore:

- `E=empty` -> no deterministic equivariant feasible selector exists on the orbit;
- `|E|=1` -> unique equivariant output for the frozen feasibility relation;
- `|E|>1` -> equivariant output remains noncanonical with current context/constraints.

Freeze:

- `STABILIZER_FILTERED_EQUIVARIANT_SELECTOR_THEOREM_ESTABLISHED`
- `BRC_SELECTABLE_SET_EQUALS_EXACT_FEASIBLE_INTERSECT_STABILIZER_FIXED_SET`

This is scoped to the declared finite-group equivariant selector calculus.

## Context theorem

Context can change both the stabilizer and the exact feasible relation.

Shrinking a stabilizer does not imply uniqueness. A free Z2 context has trivial stabilizer, so the fixed output set becomes both branches; if `A` remains full, both outputs remain selectable.

Conversely, `A` need not itself be singleton. For the S3 donor fiber, a genuinely preexisting donor relation `h=d2` has stabilizer `S2`, whose fixed donor set is exactly `{d2}`. Thus full three-donor feasibility already yields singleton `E={d2}`.

Hence the exact uniqueness criterion is singleton `E`, not singleton `A`.

Freeze:

- `SYMMETRY_BREAKING_CONTEXT_IS_NECESSARY_IN_MANY_NO_GO_CASES_BUT_NOT_SUFFICIENT_IN_GENERAL`
- `FILTERED_SINGLETON_NOT_FEASIBILITY_SINGLETON_IS_THE_EXACT_UNIQUENESS_CRITERION`

The stronger claim that symmetry breaking can never be sufficient unless `A` itself is singleton is refuted.

## Z2 replay

Fully symmetric input: `H=Z2`, `Fix_Y(H)=empty`, so the stateless no-go is recovered.

A tau-odd free context gives `H={e}` and `Fix_Y(H)=Y`. With full `A`, both branches remain; with independent singleton `A`, the output is unique.

This recovers the Stage-P/O contextual singleton logic without arbitrary preference.

## S3 donor replay

For `Y={d2,d3,d4}` under natural S3 action:

- fully symmetric `H=S3` -> no fixed donor;
- preexisting donor relation `h=d2` -> `H=Stab(d2)~=S2`, `Fix={d2}`.

So a genuine pre-collapse donor relation can itself make the donor symmetry-compatible and unique. Copying the selected donor into context after the fact remains circular.

## S4 axis replay

For the six unordered axes:

- `H=S4` -> no fixed axis;
- preexisting carrier `X1`, `H~=S3` -> still no fixed axis;
- preexisting axis `{1,2}`, `H=Stab({1,2})~=S2 x S2` -> fixed axes are exactly `{1,2}` and the complementary disjoint axis `{3,4}`.

Freeze:

- `PREEXISTING_AXIS_CONTEXT_RETAINS_COMPLEMENT_AXIS_AMBIGUITY`
- `PREEXISTING_AXIS_CONTEXT_ALONE_DOES_NOT_CANONICALLY_IDENTIFY_AXIS_OUTPUT_UNDER_FULL_S4_EQUIVARIANCE`

## Directed-transfer context audit

For preexisting directed relation `(recipient=1, donor=2)`, the S4 stabilizer fixes carriers 1 and 2 individually and swaps 3/4.

In the six-axis output space the fixed set is `{1,2}` and `{3,4}`.

In full D12 the fixed directed states are `(1,2)` and `(2,1)`.

Therefore ordered context alone does not automatically select the same directed transfer. If an independent exact equation explicitly imposes `output=context`, then `A` becomes singleton and the selection is unique; the uniqueness comes from the feasibility constraint, not from stabilizer reduction alone.

## Axis/orientation hierarchy

Stage-T factorization is retyped as two selector stages.

For a nonempty straight history with previous axis `{1,2}`:

- symmetry fixed axes under its stabilizer are `{1,2}` and `{3,4}`;
- rank-one straightness supplies exact feasibility `A_axis={{1,2}}`;
- therefore `E_axis={{1,2}}`.

So straightness forces the axis.

Conditional orientation stage:

- rank-one straightness gives `A_orient={+,-}`;
- at orientation-symmetric input, the Z2 swap has no fixed orientation;
- a free tau-odd context alone gives both orientations;
- only an independently constrained singleton surviving the filter gives a unique orientation.

Freeze:

`STRAIGHTNESS_FORCES_AXIS_BUT_NOT_ORIENTATION`.

## Scalar midpoint control

For an ordered scalar gap, bare completion gives `A={L,U}`.

At exact midpoint, endpoint reflection fixes the input but swaps the two outputs, so the stabilizer fixed set is empty and the no-go is recovered.

Away from midpoint the local stabilizer is trivial, so stabilizer filtering leaves both endpoints. It does not derive lower/upper collapse.

Thus Stage-R `A0+A3+A4+A5` contributes cross-state order/reflection/single-valuedness information beyond stabilizer filtering.

Freeze:

`STABILIZER_FILTERING_UNIFIES_SYMMETRY_NO_GO_BUT_DOES_NOT_REPLACE_ORDER_POST_CREDIT_AXIOMS`.

For `L=4,U=9,q=5`, stabilizer filtering alone still leaves `{4,9}`; `5->4` remains conditional on the Stage-R midpoint-core package.

## Post-credit typing

Exact post-credit is retyped as constraints that shrink `A(x)`, not as a scalar reward.

The exact finite-group formula is:

`BRC_SELECTABLE_SET(x)=EXACT_FEASIBLE_SET(x) intersect SYMMETRY_FIXED_OUTPUT_SET(x)`.

Examples:

- straightness shrinks axis feasibility to the previous axis;
- symmetric supervision leaves axis feasibility unchanged;
- independent oriented certificates may create a singleton;
- branch-conditioned readout reused as its own certificate is circular and rejected.

## Checker

Deterministic checker: `324 / 324 PASS`.

Digest:

`1538acd6933798066b5717932b4027f41e77fc017144b45eed2249aba2d4781a`

The checker verifies the frozen registry, Z2/S3/S4 stabilizers and fixed sets, representative-independence orbit extension, all S4 carrier/axis/directed contexts, all 64 axis-feasible subsets for the selectable-set identity, hierarchy, scalar control, and firewalls.

## Boundaries

- no universal physical BRC law is claimed;
- initial S4 axis at a fully symmetric state remains nonselectable;
- straightness does not select orientation;
- scalar off-midpoint choice still needs order/post-credit information beyond the stabilizer filter;
- no probability or physical direction follows from symmetry.

`STOP_FOR_DRIVER_REVIEW`
