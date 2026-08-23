# FQ010 — Relation Admissibility and Maximality

Researcher-ID: `EM-FQ010-CA2555`

## Statement

Let `U` be a finite token set equipped with the supplied component observation

`tau:U->C`.

Define

`R_type={(x,y):tau(x)=tau(y)}`.

Then `R_type` is an equivalence relation and is the **unique greatest equivalence relation on `U` through whose quotient the exact component observation still factors**.

Equivalently, if `E` is any equivalence relation on `U`, with quotient map `q_E:U->U/E`, then

`tau = bar_tau o q_E`

for some `bar_tau:U/E->C`

if and only if

`E subseteq R_type`.

## Proof

### Existence and equivalence

Equality in `C` is reflexive, symmetric and transitive. Pulling it back along `tau` makes `R_type` reflexive, symmetric and transitive on `U`.

### Factorization criterion

Suppose `tau=bar_tau o q_E`. If `x E y`, then `q_E(x)=q_E(y)`, hence

`tau(x)=bar_tau(q_E(x))=bar_tau(q_E(y))=tau(y)`.

Therefore `(x,y) in R_type`, so `E subseteq R_type`.

Conversely, suppose `E subseteq R_type`. Every `E`-class is contained in one `tau`-fiber. Hence the assignment

`bar_tau([x]_E):=tau(x)`

is well defined and satisfies `tau=bar_tau o q_E`.

Thus the component-preserving equivalence relations are exactly the equivalence subrelations of `R_type`. Since `R_type` itself is component-preserving, it is the greatest such relation under inclusion. Greatest elements are unique. QED.

## Semantic strength of the theorem

This is a relation-strength theorem. It needs only:

1. a finite token carrier `U`;
2. the already-supplied exact component observation `tau`;
3. ordinary equality and quotient/equivalence-relation mathematics.

It does **not** need:

- orientation;
- metric or distance;
- norm or length;
- current line formula;
- sum-of-squares target;
- pair capacity;
- any scalar readout;
- a preferred axis ordering.

The weakest hypothesis is simply the existence of the exact component observation whose information is required to survive quotienting.

## Choice independence and covariance

### Token renaming

Let `f:U->U'` be a bijection preserving typing, so `tau'(f(x))=tau(x)`. Then

`(x,y) in R_type <=> (f(x),f(y)) in R'_type`.

Therefore

`(f x f)(R_type)=R'_type`.

Under a pure token renaming of the same typed presentation this is invariance.

### Component relabeling

Let `sigma:C->C'` be a bijection and suppose

`tau'(f(x))=sigma(tau(x))`.

Since `sigma` preserves equality,

`tau(x)=tau(y) <=> tau'(f(x))=tau'(f(y))`.

Thus `R_type` is equivariant under all component relabelings, including the full `S3` action of the R065 substrate. No absolute component name is selected.

## Canonicity classification

`R_type` is not merely one convenient relation among many. Relative to the declared observation `tau`, it has an exact universal property:

> it is the coarsest token identification, equivalently the greatest equivalence relation, that loses no component-observation information.

This is stronger than scalar invariance because it certifies the relation object itself.

However, the theorem is **relative to preserving the exact component observation**. It does not prove that component observation is the only possible observation resolution relevant to every future semantic role. FQ010 therefore pressure-tests finer and coarser resolutions separately.

## Admission result

- `RELATION_DEFINABILITY = PASS`
- `RELATION_MAXIMAL_COMPONENT_PRESERVATION = PASS`
- `TOKEN_RENAMING_INVARIANCE = PASS`
- `S3_COMPONENT_RELABELING_EQUIVARIANCE = PASS`
- `METRIC_OR_TARGET_DEPENDENCE = NONE`
- semantic typing: `R_type = N0_DEFINABLE_DERIVED`

This theorem alone does not promote any scalar valuation of `R_type` to N0 and does not assign a squared-line-scale role.
