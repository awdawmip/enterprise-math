# Partial-Operation Semantic Repair as an FQ-006 Consumption Bridge

Status: `RESEARCH BRIDGE / NONCANONICAL / NO NEW PARTIAL-QUOTIENT OWNERSHIP`

This note connects the task-relative semantic-precision preorder and its total-operation repair compiler to the already-canonical FQ-006/P023 partial-operation quotient. It does **not** claim a new generic partial-transition theorem.

## 1. Canonical source theorem is already FQ-006

For a finite state set X and deterministic partial operation

`u:D_u -> X`,

canonical FQ-006 requires an equivalent source pair to agree on both:

1. DOMAIN membership / definedness;
2. when enabled, the quotient class of the target.

For a family of partial operations, the canonical refinement signature is therefore

`current block + one (definedness,target-block) value per named operation`.

The stable partition is already proved to be the coarsest refinement of the initial observation through which the declared partial family descends with domains preserved.

This bridge only reinterprets that result as a **semantic capability repair**.

## 2. Partial operation capability demand

Suppose a task-relative precision state currently carries observational equivalence E_0 and the future theory additionally requires a family U of deterministic partial unary operations to remain executable after collapse.

For one current equivalence E, define the per-operation signature of x by

`UNDEFINED`

when x is outside the domain, and

`(DEFINED,[u(x)]_E)`

when x is enabled.

Two currently equivalent states may remain equivalent only when all required partial-operation signatures agree.

Iterating this split to a fixed point is exactly the FQ-006 legality-sensitive partition refinement.

## 3. DOMAIN and target precision can activate each other

Definedness is not merely one extra bit that can always be attached once.

Sharp four-state example:

initial partition

`{0,1}|{2,3}`,

partial operation

`0->2`, `1->3`, `2->0`, while 3 is undefined.

The first step sees only the DOMAIN difference at the downstream block and gives

`{0,1}|{2}|{3}`.

Only after that split do the targets of 0 and 1 become distinguishable, so the next step gives

`{0}|{1}|{2}|{3}`.

Thus DOMAIN refinement can activate later target refinement. The exact semantic repair is the fixed point, not a one-shot definedness annotation.

## 4. Total-operation specialization

If every required operation is total, the `UNDEFINED` case disappears. The partial signature becomes only the current target-block vector.

The DOMAIN-aware compiler then reduces exactly to the total-operation coarsest refinement from the semantic-operation branch.

So the current architecture is nested:

`total operation repair`

is the full-domain specialization of

`FQ-006 partial operation repair`.

## 5. Observable-UNDEFINED totalization is a verification equivalence

FQ-006 also admits a verification representation that adjoins a distinguished absorbing `UNDEFINED` state and totalizes each partial map.

If that extra state is kept observably distinct, ordinary total-operation refinement on the extended state set, restricted back to X, yields the same coarsest partition as direct partial-operation refinement.

This is useful because it lets total-operation congruence machinery verify the partial result.

It does **not** promote UNDEFINED into a physical successor state.

## 6. Semantic-preorder interpretation

In the task-relative semantic precision preorder, requiring a partial operation means demanding two capabilities simultaneously:

- its DOMAIN law must descend;
- its enabled target map must descend.

If the current representation allows arbitrary state partition refinement on the same finite X, FQ-006 supplies the canonical coarsest state lift realizing that capability join.

This is the partial-operation counterpart of the total-operation semantic repair theorem.

## 7. Ownership boundary

The generic theorem — legality-sensitive refinement, finite stabilization, coarsest compatible partition and observable-UNDEFINED totalization — is already FQ-006/P023 canonical mathematics.

This branch owns only:

- the explicit semantic-preorder consumption bridge;
- the DOMAIN-to-target cascade pressure test;
- executable equivalence with the total specialization and observable-UNDEFINED verification route.

It must not be cited as a replacement owner for the canonical partial-operation quotient.

## 8. Next boundary: multivalued relation support

A deterministic partial operation has successor support of size either zero or one.

The natural next generalization is an A4 relation-valued action whose source has an arbitrary finite set of target states. At support semantics, the analogous current signature is the **set of target partition blocks**, with the empty set preserving undefinedness.

That generalization belongs to the A4/P023 relation-support line and must explicitly stop before path multiplicity, witness provenance or branch-death history.