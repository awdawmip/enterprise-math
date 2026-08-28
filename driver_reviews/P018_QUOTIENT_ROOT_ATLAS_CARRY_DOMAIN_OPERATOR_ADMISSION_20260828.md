# Driver Admission — P018 Quotient-Root Atlas Carry Domain Operator

Status: `DRIVER_FINAL / ADMIT_DOMAIN_OPERATOR / T1_ROUTED / NO_NEW_GLOBAL_TOOL_FAMILY / NO_FOUNDATION_MUTATION`

Date: `2026-08-28`

Driver-ID: `EM-FREE-C19420 / CONTROL_PLANE`

Source theorem result:

`RS-P018-TERNARY-CARRY / RR-046FB92F6C42BB24A56C / DR-674A8EC67ED785D968FA`

Source formal theorem:

`EnterpriseMath/Precision/RootStateAtlasCardinality.lean`

Theorem node:

`research_notes/P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_DRIVER_ACCEPTED_THEOREM_NODE_20260828.md`

Harvest note:

`research_notes/P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_THEOREM_TOOL_HARVEST_20260828.md`

## 1. Final disposition

`DRIVER_DISPOSITION = ADMIT_DOMAIN_OPERATOR`.

`METHOD_ID = domain.precision.quotient_root_atlas_carry`.

`CLASSIFICATION = DOMAIN_OPERATOR`.

`PRIMARY_FAMILY = T1_SCALE_ENUMERATION_VALUATION`.

`SUPPORTING_FAMILIES = T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA + T5_PRECISION_REFINEMENT`.

`NEW_GLOBAL_TOOL_FAMILY = false`.

`FOUNDATION_MUTATION = false`.

The Driver admits the existing P018 executable atlas/count/carry surface as one reusable domain operator. This admission does not introduce new mathematics and does not reopen the already terminal L4 theorem result.

## 2. Why this is a tool surface

The accepted surface has a stable input/output contract:

Input:

- `n>=1`;
- root exponent `r>=1`.

Output:

- state-coalescence horizon `H`;
- high-denominator cutoff `D`;
- exact high/low quotient-root decomposition;
- exact distinct-state count;
- binary horizon carry;
- ternary state-count carry and threshold band.

It also has a structural certificate law:

`high injective chart + forced contiguous low chart + one optional horizon state`

which compresses the count to one boundary bit and then to a three-valued carry.

The failure boundary is explicit: the operator is not an arbitrary floor-map theorem, not a generic quotient-semigroup compiler, not a prime oracle, and not a continuum semantics package.

## 3. Why this is not a new global T-family

The result is mathematically strong but presently domain-specific. The reusable mechanism already composes naturally from existing Enterprise families:

- T1 owns finite count/enumeration compression;
- T4 supplies exact fiber/collision-capacity support;
- T5 supplies the integer carry/refinement viewpoint.

No evidence establishes an independent cross-domain calculus requiring `T13`.

Therefore

`NEW_THEOREM != NEW_GLOBAL_TOOL_FAMILY`

is enforced here by admitting only a T1-routed domain operator.

## 4. Accepted executable API

Current-main implementation owners:

- `src/enterprise_math/p018_root_state_decomposition.py`;
- `src/enterprise_math/p018_root_state_carry.py`.

Accepted public API:

- `state_coalescence_horizon`;
- `exact_distinct_root_state_count`;
- `quotient_root_state_decomposition`;
- `horizon_state_carry`;
- `ternary_state_count_carry`;
- `ternary_state_count_band`.

Support API from the earlier P018 coalescence layer, not re-promoted by this review:

- `exact_root_fiber_capacity` in `src/enterprise_math/p018_power_coalescence.py`.

## 5. Verification and theorem linkage

The load-bearing exact theorem is Lean-checked in

`EnterpriseMath/Precision/RootStateAtlasCardinality.lean`

at blob

`e46d6037257d4f330d6cd46459beb0bc1a11ba5d`.

The accepted theorem endpoints are

- `quotientRootStates_binary_cardinality`;
- `quotientRootStates_ternary_cardinality`.

Executable regression owners:

- `tests/test_p018_root_state_decomposition.py`;
- `tests/test_p018_root_state_carry.py`;
- `tests/test_p018_root_state_exact_count.py`.

The finite regression is not used as proof of the universal statement.

## 6. Hard boundaries

The admitted operator must not silently infer:

- the same formula for arbitrary floor maps;
- a universal carry law outside the declared quotient-root carrier;
- prime/factoring or Legendre consequences;
- continuum/real semantics from finite integer formulas;
- Foundation changes.

The `H=0` edge branch is part of the interface contract and may not be erased.

## 7. Registry action

Admit the method inventory record

`domain.precision.quotient_root_atlas_carry`

through

`research_method_inventory_addenda/20260828_p018_quotient_root_atlas_carry_harvest.json`.

Because `tools/enterprise_toolbox.py` automatically loads dated inventory addenda, no mutation of the top-level T0-T12 registry is required for routing.
