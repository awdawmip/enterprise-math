# R064 Phase A — Interaction Law or No-Go

Freeze: `2026-08-22T15:49:42+08:00`

## Theorem

Final Phase-A classification:

`N0_DEFINABLE_LOCAL_PROCESS_RELATION_FAMILY_NONUNIQUE_WITH_EXACT_MISSING_AXIOM`

with the precise refinement:

> N0 contains a parameter-free nontrivial binary operation on the primitive native **component-tag carrier**, but N0 does not force a unique binary process on the full elementary-event context. A unique nontrivial component-only law appears only after requiring factorization through component tags, and a single output event occurrence additionally requires an event-lift rule.

## 1. N0-definable component operation

Let `A={E1,E2,E3}` be the three primitive positive axis objects. Define

`x ⊙ y = x` when `x=y`;

and when `x!=y`, define `x ⊙ y` as the unique `z in A` with `z!=x` and `z!=y`.

This is reconstructed only from:
- the N0 fact that `A` has exactly three distinct axes;
- axis equality;
- finite singleton complement.

No sign, orientation, multiplication table, identity, group law or target cardinality was imported.

### Definability DAG

`three N0 axis objects -> equality/off-diagonal distinction -> singleton complement of {x,y} -> output axis`.

Every output is one of the pre-existing N0 axes; no new internal state is invented.

## 2. Exact component-only equivariant family

For a total deterministic `S3`-equivariant map `F:A×A->A`:

- on `(x,x)`, the stabilizer of `x` swaps the other two axes, so equivariance forces `F(x,x)=x`;
- for one ordered off-diagonal pair, e.g. `(E1,E2)`, the stabilizer is trivial, so the output may be `E1`, `E2` or `E3`; equivariance propagates that choice to every off-diagonal pair.

Hence exactly three component-only equivariant total laws exist:

1. left projection;
2. right projection;
3. `⊙`, the unique-third-axis component complement.

The task definition classifies the first two as trivial. Therefore `⊙` is the **unique nontrivial law after factorization to component tags**.

## 3. Why this does not solve the full event-level mother question uniquely

The frozen elementary event carries more N0 information than its component tag: sector, source identity, and intrinsic source order. The local-context quotient has 11 `S3` orbits. Each orbit has trivial stabilizer, so for an axis-valued deterministic law each local orbit independently permits any of the three axis outputs.

Therefore the exact smallest full-context family at this codomain strength has

`3^11 = 177147`

`S3`-equivariant laws.

This is not a counting artifact: the checker exhibits two explicit N0-definable, target-free, equivariant laws that disagree on the length-2 source `E1 E1` in sector `S12` for its ordered positions `0<1`:

- component-only law outputs `E1`;
- a context-sensitive law outputs the other axis of the same source sector, `E2`, on that context and otherwise follows the component-complement law.

Thus N0 does not force context erasure.

## 4. Exact missing operational axiom

To select the component-only candidate as **the** local process law, at least the following additional operational statement is needed:

`PROCESS_FACTORS_THROUGH_COMPONENT_TAGS`

meaning that equal ordered component-tag pairs must receive the same process output regardless of source identity, source order, and sector-local contextual distinctions.

If an actual output event rather than only an axis-state output is required, another lift is necessary:

`COMPONENT_OUTPUT_TO_EVENT_LIFT`

because for distinct inputs `E1,E2` in `S12`, the derived component output is `E3`, while `E3` belongs to both `S31` and `S23`. N0 contains no single-valued event placement/source-position rule selecting one resulting event occurrence.

These are N1 operational additions if introduced. They are not added in Phase A.

## 5. Semantic strength

- Local context classes: `N0_DEFINABLE_DERIVED` at relation strength.
- Component-complement operation: `N0_DEFINABLE_DERIVED` at component-relation/function strength.
- Claim that this is the unique full event process: **not N0 forced**.
- Same/different pair labels: quotient/readout only.
- Single output event lift: `UNRESOLVED` without an N1 placement rule.

Accordingly Phase A freezes the nonunique family and stops. No downstream comparison is performed.
