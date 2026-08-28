# P018 Quotient-Root Atlas / Ternary Carry — theorem and tool harvest

Status: `NO_NEW_MATHEMATICS / THEOREM_ALREADY_DRIVER_ACCEPTED / DOMAIN_OPERATOR_EXTRACTION`

Date: `2026-08-28`

Source theorem authority:

`driver_reviews/P018_TERNARY_CARRY_THRESHOLD_TO_CARDINALITY_DRIVER_REVIEW_20260827.md`

Accepted result:

`RR-046FB92F6C42BB24A56C / DR-674A8EC67ED785D968FA`

Extracted theorem node:

`research_notes/P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_DRIVER_ACCEPTED_THEOREM_NODE_20260828.md`

## 1. Theorem extraction

No new theorem is introduced by this harvest. The accepted L4 formal result is decomposed into three reusable theorem-facing assertions.

### T-A — exact quotient-root atlas decomposition

For `n>=1`, `r>=1`, define

`phi(d)=R_r(floor(n/d))`, `1<=d<=n`,

`H=R_(r+1)(r*n-1)`,

`D=floor(n/(H+1)^r)`.

Then:

- `1<=d<=D` gives roots strictly above `H`;
- the high chart is injective and therefore has exactly `D` states;
- `d>D` gives roots at most `H`;
- every root `1,...,H-1` occurs;
- `H` is the only optional low state and, for `H>0`, occurs iff `(D+1)H^r<=n`;
- the positive-horizon high and low charts are disjoint.

This is the reusable structural theorem. It is stronger than a cardinality identity because it exposes the exact chart decomposition that makes the count transparent.

### T-B — binary exact cardinality

With

`kappa = 1_((D+1)H^r<=n)`,

one has

`|S_r(n)|+1=D+H+kappa`.

The `H=0` case is included by the formal theorem and is not an omitted edge condition.

### T-C — ternary threshold normal form

Put

`q=floor(H/r)`,

`X=(H+1)^r`, `Y=H^r`,

`A=max(qX,(q+1)Y)`, `B=(q+1)X`,

and let `tau` be `0,1,2` on the intervals `n<A`, `A<=n<B`, `B<=n`.

Then

`|S_r(n)|+1=H+q+tau`.

This is the exact ternary carry closure of the state count.

## 2. Tool extraction decision

The binding toolbox rule is

`NEW_THEOREM != NEW_TOOL`.

The P018 result does **not** justify a new global family `T13` or a new top-level calculus. Cross-family reuse beyond quotient-root counting has not been established.

The reusable executable surface is therefore admitted only as a `DOMAIN_OPERATOR`:

`domain.precision.quotient_root_atlas_carry`.

Primary family routing:

`T1_SCALE_ENUMERATION_VALUATION`.

Supporting dependencies:

- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` for exact quotient-root fiber/collision capacity;
- `T5_PRECISION_REFINEMENT` for the carry/refinement viewpoint.

The operator is implemented by existing current-main modules rather than a new wrapper:

- `src/enterprise_math/p018_root_state_decomposition.py`;
- `src/enterprise_math/p018_root_state_carry.py`.

## 3. Public certificate API

### `state_coalescence_horizon(n, root_exp)`

Returns

`H=R_(r+1)(r*n-1)`.

This is the exact state-specific collision horizon used by the atlas split.

### `exact_distinct_root_state_count(n, root_exp)`

Returns the exact compressed count data

- `H`;
- `D=floor(n/(H+1)^r)`;
- horizon-fiber bit;
- exact number of distinct quotient-root states.

No denominator scan is required.

### `quotient_root_state_decomposition(n, root_exp)`

Returns a certificate-level materialization of

- high denominators;
- injective high roots;
- low roots;
- distinct roots;
- high/low disjointness checks;
- exact count and two-point state-count band.

This is the structural/debug API. It may enumerate the compressed output surface, but it does not scan all denominators `1,...,n`.

### `horizon_state_carry(n, root_exp)`

Returns the exact binary carry controlling the optional horizon root, both in direct threshold form and remainder-threshold form.

### `ternary_state_count_carry(n, root_exp)`

Returns

- `H` and `q=floor(H/r)`;
- the two thresholds `A,B`;
- `tau in {0,1,2}`;
- the exact state count.

It cross-checks against the binary carry formulation and the three-point `D` band.

### `ternary_state_count_band(n, root_exp)`

Returns the three consecutive cardinalities allowed by the coarse horizon before the exact threshold comparison chooses the realized one.

## 4. Input/output contract

Input:

- positive integer state `n`;
- positive integer root exponent `r`.

Output:

- exact integer horizon/cutoff data;
- exact high/low quotient-root atlas information;
- exact binary/ternary boundary-carry certificate;
- exact distinct-state cardinality.

No floating-point approximation, probabilistic inference, prime oracle, or continuum limit is part of the operator.

## 5. Structural law

The reusable law is:

`FULL DENOMINATOR SCAN`

`-> HIGH INJECTIVE CHART + CONTIGUOUS FORCED LOW CHART + ONE OPTIONAL HORIZON STATE`

`-> BINARY BOUNDARY CARRY`

`-> THREE-POINT D BAND`

`-> TERNARY COUNT CARRY`.

This is the reason the operator is reusable. It exposes a certificate decomposition rather than merely returning a fitted count.

## 6. Failure boundary

The operator must not be used to infer any of the following without a separate theorem:

- the same atlas decomposition for arbitrary monotone floor maps;
- arbitrary quotient semigroup or multistage quotient behavior;
- real/continuum asymptotics as exact semantics;
- primality or factoring-speedup claims;
- a universal T5 carry law;
- Foundation or native-geometry consequences.

The `H=0` boundary must be retained explicitly.

## 7. Verification surface

Formal theorem source:

`EnterpriseMath/Precision/RootStateAtlasCardinality.lean`

with accepted blob

`e46d6037257d4f330d6cd46459beb0bc1a11ba5d`.

Executable regressions:

- `tests/test_p018_root_state_decomposition.py`;
- `tests/test_p018_root_state_carry.py`;
- `tests/test_p018_root_state_exact_count.py`.

The frozen `19,992` finite cases remain regression only. General correctness is supplied by the Lean theorem package.

## 8. Registry posture

Method inventory addendum:

`research_method_inventory_addenda/20260828_p018_quotient_root_atlas_carry_harvest.json`.

Tool admission review:

`driver_reviews/P018_QUOTIENT_ROOT_ATLAS_CARRY_DOMAIN_OPERATOR_ADMISSION_20260828.md`.

Final extraction posture:

`DRIVER_ADMITTED_DOMAIN_OPERATOR / T1-ROUTED / NO_NEW_GLOBAL_TOOL_FAMILY`.
