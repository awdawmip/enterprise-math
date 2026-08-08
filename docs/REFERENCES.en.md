# Neighboring Prior Work and Terminology

This document records external mathematics and computation that are close to parts of Enterprise Math. None of these references proves the project's ontological interpretation. They are used to avoid reinventing terminology, to borrow proven results when definitions match, and to identify where Enterprise Math makes a stronger or different claim.

## 1. Integer square root

Python's standard library defines integer square root as the greatest integer \(a\) such that \(a^2\le n\).

Reference:
- https://docs.python.org/3/library/math.html#math.isqrt

Relation to this project:

The inequality definition is directly useful. Conventional documentation also describes the result as the floor of the exact real square root. Enterprise Math does not need that real-valued interpretation as a primitive definition.

## 2. Interior and closure operators on ordered sets

Order theory studies monotone, idempotent projection-like maps. A closure operator is monotone, idempotent, and extensive; its order-dual notion is an interior operator, which is monotone, idempotent, and reductive.

Reference implementation and formalization:
- https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Order/Closure.lean

Relation to this project:

The collapse map \(C_p(n)=R_p(n)^p\) is monotone, idempotent, and reductive, so it has an interior-operator-like structure. The physical interpretation of such a map as natural state collapse is an additional hypothesis.

## 3. Exact algebraic-number arithmetic

FLINT can represent an algebraic number exactly using an integer minimal polynomial together with an isolating interval. Sage also has optimized quadratic-number representations whose internal state is a triple of integers representing \((a+b\sqrt D)/c\).

References:
- https://github.com/fredrik-johansson/flint/blob/main/doc/source/qqbar.rst
- https://github.com/sagemath/sage/blob/develop/src/sage/rings/number_field/number_field_element_quadratic.pyx

Relation to this project:

These systems demonstrate that exact symbolic arithmetic does not require storing decimal expansions. Enterprise Math goes further by questioning whether the traditional algebraic real value should be treated as a hidden primitive at all.

## 4. Preimage entropy for non-invertible dynamics

There is an established literature on measuring non-invertibility and dynamical complexity through preimage structure. Preimage-entropy invariants are specifically nontrivial for non-invertible maps and can quantify departure from invertibility.

References:
- https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/preimage-entropy/56C8283787288DCDD4462FA2727E7454
- https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/on-preimage-entropy-folding-entropy-and-stable-entropy/012FED8E4A51761352CDA5A4F4723C97

Relation to this project:

This is the closest mature mathematical neighborhood for the idea that a present state can have many earlier preimages. Enterprise Math initially keeps the primitive quantity integer-valued as preimage multiplicity and does not assume that conventional logarithmic entropy is fundamental.

## 5. Logical irreversibility and reversible computation

Landauer and later Bennett connected logically irreversible operations, information erasure, reversible computation, and thermodynamic cost.

References:
- Rolf Landauer, 1961, "Irreversibility and Heat Generation in the Computing Process", IBM Journal of Research and Development.
- Charles H. Bennett, work on reversible computation and later reviews of Landauer's principle.

Relation to this project:

This literature is important but conceptually different. Enterprise Math is testing a stronger ontology in which the natural transition itself may be many-to-one and no hidden remainder state is assumed to survive. Therefore the project should not describe its collapse maps merely as conventional information erasure.

## 6. Coarse-graining as a contrast class

Statistical mechanics often explains irreversible macroscopic behavior by projecting or coarse-graining a finer microscopic description, while the underlying dynamics may remain reversible.

Relation to this project:

Enterprise Math explicitly tests the alternative hypothesis that many-to-one evolution can be fundamental rather than merely observational. Coarse-graining is therefore a comparison framework and a potential competing explanation.

## 7. Terminology discipline

When a new Enterprise Math structure matches an established mathematical definition, use the established term for the mathematical structure and reserve project-specific terminology for the additional interpretation.

Examples:

- use "integer square root" for the inequality-defined root operation;
- use "interior-operator-like" when the order-theoretic properties match;
- use "preimage multiplicity" or "preimage structure" before inventing a new entropy name;
- use "ontological collapse" only for the stronger hypothesis that the many-to-one transition is itself fundamental.
