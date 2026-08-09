# Causal Absorption 04 — Exact LEGO Interaction Spectrum Instead of Primitive Nonlinearity/Taylor Language

Status: `CROSS-ROUTE RESEARCH WIP / EXACT FINITE INTERACTION DECOMPOSITION`

If additive behavior is defined causally by

\[
T(x\oplus y)=T(x)\oplus T(y),
\]

then nonlinearity should first mean that multiple units jointly create an effect not reconstructible from lower-order unit effects.

For labeled finite unit sets, define

\[
\boxed{
I(A)=\sum_{B\subseteq A}(-1)^{|A|-|B|}T(B).
}
\]

`I(A)` is the residual effect requiring the units in `A` to coexist after every lower-order subset contribution has been removed. Boolean Möbius inversion gives the exact reconstruction

\[
\boxed{T(A)=\sum_{B\subseteq A}I(B).}
\]

This is finite integer interaction accounting, not a Taylor approximation: there are no limits, derivatives, epsilon, or remainder terms.

When `T(empty)=0` and all interactions of order at least two vanish, the response is exactly the sum of independent unit effects. Thus LEGO additivity is the zero-higher-interaction regime.

A causal interaction order can be defined as the largest `|A|` with nonzero `I(A)`. The primitive interpretation is coexistence-generated effect, while Möbius inversion remains a standard coordinate/proof tool.

This stage covers finite labeled unit subsets only. Repeated indistinguishable units require a different multiplicity formulation, developed separately through the P011 collision basis.

Executable sources:

- `src/enterprise_math/lego_interaction_spectrum.py`
- `tests/test_lego_interaction_spectrum.py`
