# P020 — Lean-checked well-founded finite stabilization

Status: `PROVED / LEAN-CHECKED`  
Problem: `P020`  
Scope: ordinary order theory and formalization

## 1. Result

Let `(X, ≤)` be a partial order whose strict order `<` is well founded. Let

\[
F:X\to X
\]

be monotone and reductive:

\[
x\le y\Rightarrow F(x)\le F(y),
\qquad F(x)\le x.
\]

P020 formalizes the P019 mother theorem directly in Lean.

### P020-T01 — Finite ordinary iteration reaches the greatest fixed point below the start

For every `x`, there exists `n : ℕ` such that

\[
F^{[n]}(x)
\]

is the greatest state `z` satisfying

\[
F(z)=z,
\qquad z\le x.
\]

This is formalized as `exists_iterate_isGreatest` in
`EnterpriseMath/Order/WellFoundedStabilization.lean`.

The proof is by well-founded induction. If `F x = x`, zero iterations suffice. Otherwise reductivity plus inequality gives `F x < x`; the induction hypothesis applies below `x`. Monotonicity shows every fixed point below `x` is already below `F x`, so the greatest fixed point found in the recursive case is also greatest below the original state.

## 2. Canonical finite stabilization

The Lean layer selects one finite iteration count `stabilizationSteps` supplied by P020-T01 and defines

\[
\operatorname{stabilize}_F(x)
=F^{[\operatorname{stabilizationSteps}(x)]}(x).
\]

The definition is explicitly a **finite ordinary iterate**. No limit `n→∞`, real completion, or hidden continuum state is used.

Lean checks that `stabilize_F(x)`:

- is fixed by `F`;
- lies below `x`;
- dominates every `F`-fixed point below `x`.

Thus

\[
\boxed{
\operatorname{stabilize}_F(x)
=
\max\{y:F(y)=y,\ y\le x\}.
}
\]

## 3. Completion to an interior-like operator

### P020-T02 — Stabilization completion

Lean proves that the map

\[
x\mapsto\operatorname{stabilize}_F(x)
\]

is:

1. monotone;
2. reductive;
3. idempotent;
4. fixed at exactly the same states as `F`.

In particular,

\[
\operatorname{stabilize}_F(
\operatorname{stabilize}_F(x))
=
\operatorname{stabilize}_F(x).
\]

Therefore a monotone reductive endomap on a well-founded partial order can be completed, by finite iteration alone, into an interior/coreflection-like idempotent projection with the same fixed-point set.

This connects directly to P008: P008 begins with an idempotent coreflection such as `C_p`; P020 shows that well-founded finite dynamics can generate the corresponding idempotent stabilized operator even when the one-step map is not itself idempotent.

## 4. Relationship to P019

P019 proves mathematically that a fixed collapse word

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}
\]

stabilizes at

\[
C_L(n_0),
\qquad
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

P020 formalizes the general order-theoretic engine behind that argument. The collapse-specific identification of the greatest fixed point with `C_L(n_0)` remains the arithmetic specialization supplied by P004/P019.

## 5. Minimality boundary

P020 does **not** require:

- a lattice or complete lattice;
- a metric or topology;
- real numbers;
- an infinite iteration limit;
- compactness or continuity.

The assumptions used by the formal theorem are exactly the current Lean parameters:

- `PartialOrder X`;
- `WellFoundedLT X`;
- `Monotone F`;
- `∀ x, F x ≤ x`.

Whether any of these assumptions can be weakened while retaining the same conclusion is a separate research question.

## 6. Formal verification

The root `EnterpriseMath.lean` imports

`EnterpriseMath.Order.WellFoundedStabilization`.

The pinned warning-fatal Lean CI compiles the module against the repository's fixed Lean/mathlib revisions. The formalization uses established mathlib well-founded induction and finite function iteration APIs. [SRC-MATHLIB-WELLFOUNDED] [SRC-MATHLIB-FUNCTION-ITERATE]

Those facilities are established prior art; the project synthesis and novelty boundary are recorded under `EM-COMP-016`. The connection to the P008 order-adjoint/interior framework reuses established Galois-connection theory. [SRC-MATHLIB-GALOIS-CONNECTION]

Historical novelty of the exact P008/P019/P020 synthesis remains unverified.
