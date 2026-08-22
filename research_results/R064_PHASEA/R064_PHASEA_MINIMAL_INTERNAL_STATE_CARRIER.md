# R064 Phase A — Minimal Internal State Carrier

Freeze: `2026-08-22T15:49:42+08:00`

## Result

No generated internal state beyond the primitive native axis objects is required for the surviving component candidate.

Minimal candidate carrier:

`A = {E1,E2,E3}`.

Its cardinality `3` is not a target-selected state count; it is inherited directly from the frozen N0 declaration of three distinct positive native axes.

## Provenance DAG

For inputs `x,y in A`:

- if `x=y`, the output state is the already present primitive axis `x`;
- if `x!=y`, N0 proves that `A\{x,y}` is a singleton; the unique member is the output state.

Thus every state appearing under repeated application has the finite provenance:

`N0 axis set -> input component tags -> equality test -> singleton complement (if needed) -> existing N0 axis`.

There are no anonymous, signed, unit, inverse, phase, orientation or multiplication states.

## Closure

The component operation is closed on `A`. Repeated application never enlarges the state carrier, so finite closure has exact cardinality `3`.

Generation order in the sense of **parenthesization** is not confluent because associativity fails. For example the checker finds a three-input counterexample. This does not break state closure; it prevents replacing a parenthesized process tree by an unparenthesized associative product.

## Full event-level caution

The three-state component carrier does not provide a canonical output event occurrence. A component output axis can have more than one compatible sector/source realization. Those realizations are not additional N0 internal states unless an operational lift is separately declared.

## Minimality classification

| Ingredient | Phase-A type |
|---|---|
| three positive axes | `N0_PRIMITIVE` |
| component equality | `N0_PRIMITIVE` |
| unique-third-axis construction | `N0_DEFINABLE_DERIVED` |
| three-state closure | `N0_DEFINABLE_DERIVED` |
| factor full process through component tags | `NECESSARY_ADDITIONAL_N1` for uniqueness |
| choose a single output event realization | `NECESSARY_ADDITIONAL_N1` |
| identity / associativity / group structure | `REDUNDANT` as premises and in fact not satisfied |
