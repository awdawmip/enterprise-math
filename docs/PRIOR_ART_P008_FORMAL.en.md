# Prior-Art Appendix — P008/P014 Mathlib Formal Foundation

Status: `CANONICAL PRIOR-ART APPENDIX`

## 1. Nat.nthRoot is established formal-library work

The pinned Enterprise Math Lean layer directly reuses mathlib `Nat.nthRoot`. The mathlib source proves the key order characterization and a Galois connection between positive natural-number powering and natural nth root. [SRC-MATHLIB-NTHROOT]

Enterprise Math therefore does **not** claim integer nth root, its floor inequalities, exact perfect-power recovery, or the corresponding Lean API as inventions.

There is an important semantic boundary. Mathlib is free to characterize or implement `Nat.nthRoot` using ordinary established mathematics, including real-root/floor viewpoints. Enterprise Math imports the proved integer/order behavior but does not make a hidden infinitely precise real root the internal primitive meaning of its state operation.

## 2. Galois connections are established order theory

Mathlib's GaloisConnection library provides the mature adjoint language, insertion/coinsertion structure, monotonicity consequences, composition laws and commuting-adjoint machinery used by the P008/P014 formal layer. [SRC-MATHLIB-GALOIS-CONNECTION]

The P008 conclusion that the current v0.1 operations are naturally organized by partial orders and adjoints is therefore not a claim to have invented Galois connections. The project contribution is the explicit finite-state packaging and the minimality question asked under Enterprise Math's state semantics.

## 3. Relation to existing registered sources

Flooring division as a right adjoint is already registered under [SRC-MATHLIB-FLOORDIV], and closure/interior-style idempotent operators are already registered under [SRC-MATHLIB-CLOSURE].

Together these established ingredients support `EM-COMP-014`:

- power formation / integer root as an adjoint pair;
- multiplication / flooring division as an adjoint pair;
- exact recovery through an order embedding / coinsertion;
- induced reductive idempotent collapse;
- transport of a commuting square of left adjoints into the root/division interchange used by P014.

## 4. What is project-specific

Enterprise Math's current project-specific synthesis is:

1. treat the integer state and its explicit resolution/scale as the represented state rather than as an approximation to a mandatory hidden real completion;
2. require equality-faithful explicit states, leading to a partial order (or prior posetal quotient) rather than leaving distinct preorder-equivalent states unidentified;
3. identify greatest-principal-sublevel existence as the literal right-adjoint existence condition relevant to the current operations;
4. reuse mathlib directly instead of implementing a parallel root/order framework;
5. interpret root/division/scale compatibility as one order-adjoint pattern.

Historical novelty of that synthesis remains `NOVELTY_UNVERIFIED`.
