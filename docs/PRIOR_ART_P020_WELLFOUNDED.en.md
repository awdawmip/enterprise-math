# Prior Art Appendix — P020 Well-Founded Stabilization

Status: `CANONICAL PRIOR-ART APPENDIX`  
Updated: 2026-08-09

## 1. Well-founded induction and recursion

P020 directly uses mathlib's formal infrastructure for well-founded relations and `WellFoundedLT` induction. The pinned source is `Mathlib.Order.WellFounded`. [SRC-MATHLIB-WELLFOUNDED]

**Predecessor contribution.** Well-founded induction/recursion is established mathematics, and the cited mathlib module formalizes the relevant infrastructure.

**Enterprise Math use.** P020 applies that mature infrastructure to monotone reductive state endomaps in order to prove that ordinary finite iteration reaches the greatest fixed point below the initial state.

**Not claimed.** Enterprise Math does not claim well-founded induction, well-founded recursion, or the underlying order theory as project inventions.

## 2. Finite function iteration

P020 uses mathlib's `Nat.iterate` / `f^[n]` as the formal notion of repeated ordinary function application. [SRC-MATHLIB-FUNCTION-ITERATE]

**Predecessor contribution.** Finite iteration of a function and its basic algebra are established mathematics; the cited mathlib module provides the formal API.

**Enterprise Math use.** The existence theorem states explicitly that there is a finite natural number `n` such that `F^[n] x` is the greatest original fixed point below `x`; finite stabilization is therefore theorem content, not an implementation metaphor.

**Not claimed.** Function-iteration notation and laws are not Enterprise Math inventions.

## 3. Relationship to the P008 order-adjoint foundation

P020 also combines its stabilized operator with the already-credited Galois/interior framework used in P008. [SRC-MATHLIB-GALOIS-CONNECTION]

The P020 stabilized map is proved monotone, reductive, and idempotent, with exactly the same fixed points as the original monotone reductive endomap. This allows a precise bridge to the P008 interior/coreflection viewpoint, but it does not make established interior-operator theory novel.

## 4. Novelty boundary

The current component `EM-COMP-016` is classified as `PROJECT_SYNTHESIS`.

The project-specific contribution claimed at this stage is only the explicit integration of:

- well-founded finite descent;
- ordinary finite iteration;
- greatest-fixed-point selection below an initial state;
- completion of a monotone reductive map to an idempotent stabilized operator;
- the existing Enterprise Math P008/P019 semantics.

Historical novelty of that exact package has not been established by a dedicated priority review. No “first”, “unprecedented”, or equivalent priority claim is made.
