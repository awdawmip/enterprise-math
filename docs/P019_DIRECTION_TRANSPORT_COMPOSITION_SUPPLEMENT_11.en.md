# P019 Supplement 11 — Transport matrices are cardinality shadows

Status: `TESTING / FINITE COUNTEREXAMPLE AND WITNESS COMPOSITION ESTABLISHED`

## 1. Question

Supplement 10 defined the direction transport matrix

\[
T_{ij}=|W_{ij}|,
\]

where \(W_{ij}\) is the set of composable primitive incidence pairs from direction class \(D_i^{(t)}\) to \(D_j^{(t+1)}\).

A natural next guess is that multi-step transport should compose by ordinary integer matrix multiplication.

That guess is false in general.

## 2. Minimal overcount counterexample

Take three consecutive incidence layers:

\[
a\to x\to p\to r,
\qquad
b\to y\to q\to s.
\]

Put each layer's two incidences into one direction class.

Between the first and second direction classes there are exactly two two-path witnesses:

\[
(a\to x,\ x\to p),
\qquad
(b\to y,\ y\to q).
\]

Thus \(T_{01}=2\).

Between the second and third classes there are again exactly two witnesses:

\[
(x\to p,\ p\to r),
\qquad
(y\to q,\ q\to s).
\]

Thus \(T_{12}=2\).

Naive matrix multiplication gives

\[
T_{01}T_{12}=4.
\]

But there are only two genuine three-edge chains:

\[
a\to x\to p\to r,
\qquad
b\to y\to q\to s.
\]

The two spurious products pair the first two-path witness with the second continuation, or vice versa, even though their shared middle incidences differ.

Therefore

\[
\boxed{
|W_{01}|\,|W_{12}|
\neq
|W_{01}\Join W_{12}|
}
\]

in general.

## 3. What information was lost?

The count \(|W_{ij}|\) remembers how many composable pairs exist but forgets **which primitive middle incidence witnesses the composition**.

Exact composition requires the join

\[
(e_0,e_1)\Join(e_1,e_2)
=
(e_0,e_1,e_2)
\]

on the same actual middle incidence \(e_1\).

Consequently the witness sets \(W_{ij}\), not only their cardinalities, are the composition-complete transport data at this level.

The integer matrix is a cardinality projection / decategorification of the witness relation.

## 4. Exact witness composition

For two successive witness relations define

\[
W^{(t,t+1)}_{ij}
\subseteq
D_i^{(t)}\times D_j^{(t+1)},
\]

\[
W^{(t+1,t+2)}_{jk}
\subseteq
D_j^{(t+1)}\times D_k^{(t+2)}.
\]

Their exact composition is the fibered join

\[
\boxed{
W^{(t,t+2)}_{ik}
=
\{(e_0,e_1,e_2):(e_0,e_1)\in W^{(t,t+1)}_{ij},
(e_1,e_2)\in W^{(t+1,t+2)}_{jk}\}.
}
\]

The equality of the middle primitive incidence is essential.

This construction is still finite, coordinate-free, and integer-compatible. No probability or continuum interpolation is introduced.

## 5. Relation to P010/P011

This no-go has the same structural lesson already seen elsewhere in Enterprise Math:

- P010: after histories merge, a coarse present state does not reconstruct which predecessor history occurred;
- P011: low-order collision totals do not reconstruct the full multiplicity spectrum;
- P019 Stage 11: transport cardinalities do not reconstruct which middle incidence supports multi-step continuation.

In all three cases, aggregation is useful but loses witness identity. Exact later composition requires retaining the relevant fiber/witness structure.

## 6. Consequence for the P019 kernel

The direction-dynamics layer should therefore be represented as

\[
\boxed{
\text{direction classes}
\xrightarrow{\text{witness relation }W}
\text{direction classes}
\xrightarrow{|\cdot|}
T.
}
\]

The matrix \(T\) remains useful for support, split/merge detection, and bounded counting. It should not be treated as the primitive composition law.

## 7. Implication for shear-like comparison

A dynamical direction observable cannot be transported correctly by class-level matrix counts alone unless additional hypotheses make the witness identity irrelevant.

Therefore P019 gains a stronger no-go:

> A static direction partition plus integer transport-count matrices is insufficient, by itself, to define exact multi-step directional deformation dynamics.

Any future shear-like comparison must either:

1. use witness-complete transport; or
2. prove a restricted regime in which cardinality matrices become composition-complete.

## 8. Next gate

The next useful theorem is to characterize such restricted regimes. Candidate sufficient conditions include deterministic middle incidence continuation or orbit structures in which every nonzero transport cell has a single shared witness fiber pattern.

The project should seek a sharp condition under which

\[
|W\Join W'|
\]

is determined by the cardinality data alone. If no broad condition exists, witness transport becomes the retained primitive and matrix transport remains derived.

## 9. Scope discipline

This supplement does not claim category-theoretic novelty, a physical connection, or quantum path amplitudes. `Witness relation`, `join`, and `cardinality shadow` are used in their finite combinatorial meanings.
