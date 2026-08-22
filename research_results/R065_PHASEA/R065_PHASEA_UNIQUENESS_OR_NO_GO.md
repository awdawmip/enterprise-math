# R065 Phase A — Uniqueness / No-Go Classification

Researcher-ID: `EM-R065A-7E6F46`

## Theorem A — canonical structure exists

The blind primitive substrate canonically determines:
1. the component-type equivalence relation on tokens;
2. its unlabeled partition into occupied type fibers;
3. the complete `S3` orbit signature `Lambda(n)=sort(n)`.

Thus Phase A does **not** yield a blanket “nothing intrinsic exists” no-go.

## Theorem B — unique scalar readout is not forced

The same substrate admits multiple inequivalent parameter-free intrinsic scalar readouts, including:

`TOTAL`, `SUPPORT`, `MAXBLOCK`, `CROSS2`, `SAME2`.

All are invariant under token renaming and the full `S3` action, and all are exact finite cardinal/readout operations on objects definable from the primitive substrate.

A particularly strong two-candidate witness is:

- `TOTAL(n)=|U(n)|`;
- `MAXBLOCK(n)=largest occupied type-fiber cardinality`.

Both satisfy:
- `F(0)=0`;
- `F(unit)=1`;
- full token-renaming invariance;
- full `S3` invariance;
- componentwise monotonicity.

But at `(0,1,1)`:

`TOTAL=2`, `MAXBLOCK=1`.

Therefore even adding zero normalization, unit normalization, symmetry, and monotonicity does not force uniqueness.

## Theorem C — exact location of the missing datum

Every intrinsic scalar factors through the canonical orbit signature:

`F=f(Lambda)`.

The primitive packet supplies `Lambda` but supplies no principle selecting `f`.

The exact missing datum has three separable layers:

1. **observation-carrier selection** — which definable finite object is to be read (all tokens, occupied type classes, largest class, same-type pairs, cross-type pairs, etc.);
2. **valuation/composition selection** — which numerical valuation and which algebraic law, if any, the readout must satisfy;
3. **semantic role assignment** — why the resulting number should mean “magnitude”, “scale”, or another physical/geometric notion.

No one of these layers may be silently promoted to primitive status.

## Conditional separation result

Within `N`-valued scalar readouts, the extra axiom

`F(n⊕m)=F(n)+F(m)` for every admissible composition

reduces the invariant family to `F=c*TOTAL`.  Adding unit normalization `F(unit)=1` then uniquely gives `TOTAL`.

This package is **sufficient** to select `TOTAL`, but it is extra structure:
- additivity is not supplied;
- unit normalization of an unknown scalar is not supplied.

The package also exposes why both parts matter: remove additivity and `MAXBLOCK` survives; remove normalization and `c*TOTAL` survives.

## Orbit-composition obstruction

Even the maximally informative unlabeled orbit `Lambda` does not inherit primitive composition as a single-valued operation without relative component alignment.  Two unit orbits can combine on the same component or on distinct components and produce different output orbits.

Thus quotienting away component labels loses composition-alignment data, although it loses no information about a single isolated state up to isomorphism.

## Final Phase-A classification

`MULTIPLE_INTRINSIC_FINITE_READOUTS_SURVIVE_WITH_EXACT_MISSING_DATUM`

Exact missing datum:

> A primitive or independently justified observation/valuation principle selecting one orbit function (and, if composition behavior is required, the corresponding law and normalization).  A semantic magnitude/scale interpretation remains an additional assignment even after a numerical function is chosen.

`UNIQUENESS_OR_EXACT_MISSING_DATUM_CLASSIFIED = PASS`.
