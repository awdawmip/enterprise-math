# Coefficient Collapse Can Mix Relation Branches

Status: `RESEARCH BRIDGE / NONCANONICAL`

The nonlinear profinite ghost has a second interpretation that connects directly to A4 witness identity. An exact disjunction encoded multiplicatively can stop being a faithful labelled-branch representation after coefficient collapse.

## 1. Exact integer branch semantics

Over the integers,

`F(x)=(x^2-13)(x^2-17)(x^2-221)`.

Because Z is an integral domain,

`F(x)=0`

iff at least one labelled branch holds exactly:

`x^2=13`, or `x^2=17`, or `x^2=221`.

So in the exact coefficient world, product-zero is a faithful encoding of the finite branch relation.

## 2. Composite modular precision changes the coefficient logic

For composite n, `Z/nZ` has zero divisors. Product-zero no longer implies one factor is zero.

Sharp reference:

`n=15`, `x=1`.

The factors are

`-12`, `-16`, `-220`.

Modulo3, the first factor vanishes.

Modulo5, the third factor vanishes.

Therefore the product vanishes modulo15, but none of the three factors is itself zero modulo15.

Thus mod15 sees one unlabelled product-solution that has **no global mod15 branch label**.

The finite quotient has mixed different prime-component witnesses into one state.

## 3. Prime fields repair only the within-modulus defect

For prime p, `Z/pZ` is a field. Therefore product-zero modulo p still implies that at least one labelled factor vanishes modulo p.

So using prime moduli prevents zero-divisor branch mixing **inside one finite coefficient ring**.

It does not solve the global witness problem.

## 4. Branch labels can still switch across primes

The ghost construction chooses a square factor separately at each p-adic component.

For example:

- at p=13 it uses the branch `x^2=17`;
- at p=17 it uses the branch `x^2=13`;
- other primes may select 13,17 or221 according to quadratic character.

Each prime field has a legitimate local branch, but the label is not constant across primes.

The profinite tuple therefore satisfies the unlabelled product equation while no single labelled branch is globally valid.

## 5. No branch survives all finite precisions

Each exact label has a finite blocker:

- `x^2=13` has no root mod5;
- `x^2=17` has no root mod3;
- `x^2=221` has no root mod3.

Hence no one labelled branch is locally solvable at every modulus.

Yet the unlabelled union/product is locally solvable at every modulus.

So erasing the branch identity **before** taking the precision inverse limit changes the existence answer.

## 6. Algebraic source: completion introduces zero divisors/idempotent selectors

The profinite completion decomposes as

`Z_hat ~= product_p Z_p`.

A product of domains is not a domain. It contains many nontrivial idempotents and zero divisors that can select different prime components.

Therefore a product

`f_1(x_hat)...f_k(x_hat)=0`

can vanish componentwise with different factors zero at different primes, even when no one `f_i(x_hat)` is zero globally.

The completion itself provides a hidden branch-selector algebra.

This is the coefficient-level mechanism behind the ghost.

## 7. A4/P023 interpretation

This is closely parallel to the earlier support compiler boundary:

- A4 raw relation retains branch/witness identity;
- a support projection may retain only the set of possible outcomes;
- coefficient product-zero may retain only the unlabelled statement “some factor vanishes locally.”

If future semantics later read the branch label, both projections are too coarse.

Here the erasure occurs across arithmetic precision components rather than along a time path.

A useful routing distinction is therefore:

`state precision`

versus

`coefficient precision`

versus

`witness/branch-label precision`.

A quotient can be exact on raw numeric outputs yet unsafe for a logical interpretation that depended on the coefficient ring being an integral domain.

## 8. Semantic-safe quotient rule

If an exact world law relies on an implication such as

`f g=0 -> f=0 or g=0`,

then this implication is part of the world semantics, not merely algebraic notation.

A coefficient quotient is safe for that interpretation only if it preserves the needed no-zero-divisor / branch-label property, or if the branch label is retained explicitly as separate state/witness data.

Reducing the polynomial syntax alone is not enough.

This is analogous to safe-operation descent: one must check that the operation/logical law descends through the chosen precision collapse.

## 9. Prime powers remain a warning

Even `Z/p^e Z` for `e>1` has zero divisors. Therefore restricting to one prime direction does not automatically preserve integral-domain branch semantics at finite depth.

Prime moduli are fields; prime-power moduli encode more p-adic numeric precision but simultaneously admit zero-divisor products.

So “higher p-adic precision” and “faithfulness of multiplicative branch logic” are different axes.

## 10. Prior-art boundary

Integral domains, zero divisors, CRT, profinite idempotents and factorized polynomial equations are standard prior mathematics. The Enterprise Math value is the precision-routing consequence:

> **coefficient collapse can erase or mix witness identity; algebraic syntax may survive a quotient while the exact logical branch semantics does not.**