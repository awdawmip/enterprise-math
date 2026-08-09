# Causal Absorption 03 — Linearity as LEGO Composition Preservation, Not an A Priori Vector-Space Axiom

Status: `CROSS-ROUTE RESEARCH WIP / EXACT FREE-INTEGER GENERATOR THEOREM + EXECUTABLE REFERENCE`

Starting directly from `X=Z^k` and `T(x)=Bx` would still leave matrices as prior ontology. The stronger absorption begins with unit slots and composition.

Let `e_1,...,e_k` be unit generators and let `x⊕y` denote LEGO composition. A causal operation is additive in this regime when

\[
T(0)=0,
\qquad
T(x\oplus y)=T(x)\oplus T(y).
\]

Every signed integer state has the finite decomposition

\[
x=\sum_i x_i e_i,
\]

so composition preservation forces

\[
\boxed{T(x)=\sum_i x_iT(e_i).}
\]

Thus the operation is completely determined by the causal effect of one unit in each slot. Placing those unit images as columns produces an integer matrix and only then yields the familiar formula `T(x)=Bx`.

The ontology order is therefore

\[
\boxed{
\text{unit LEGO blocks}
\to
\text{composition law}
\to
\text{composition-preserving operation}
\to
\text{unit effects}
\to
\text{integer matrix as a coordinate table}.
}
\]

For unsigned states `N^k -> N^m`, nonnegative unit images automatically give nonnegative integer matrices. Negative coefficients arise only after a signed/cancellation state completion is admitted.

This also gives a more primitive notion of nonlinearity: an operation is nonlinear when joint LEGO composition cannot be reconstructed by adding independent unit effects. Polynomial degree is then only an optional later representation.

Combined with the causal future module, the full chain becomes

\[
\boxed{
\text{LEGO composition}
\to
\text{additive causal operation}
\to
\text{matrix shadow}
\to
\text{future distinguishability}
\to
\text{rank/kernel shadow}.
}
\]

This first-stage absorption covers finite free integer additive operations. It does not derive arbitrary scalar fields, real/complex vector spaces, inner products, spectral theorems, or infinite-dimensional functional analysis.

Executable sources:

- `src/enterprise_math/lego_additive_operation.py`
- `tests/test_lego_additive_operation.py`

Next: characterize the exact interaction data required when composition preservation fails, rather than defining nonlinearity through derivatives or polynomial degree.
