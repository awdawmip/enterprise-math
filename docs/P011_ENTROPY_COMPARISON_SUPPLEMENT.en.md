# P011 Supplement — Classical entropy as a derived transform of the integer collision spectrum

Status: `PROVED COMPARISON`  
Parent: `P011`

## 1. Purpose

P011 deliberately constructs integer irreversibility observables before introducing logarithms or probabilities.

That does not mean established entropy notions are irrelevant. It means they should enter as **derived comparisons** after the finite fiber structure is explicit.

This note gives exact translations for a deterministic map on a finite uniformly weighted history set.

## 2. Uniform-history probability model

Let

\[
F:X\to Y,
\qquad |X|=N,
\]

and put the uniform distribution on histories:

\[
\Pr[X=x]=\frac1N.
\]

For a reachable output \(y\), the pushforward probability is

\[
p_y
=
\frac{m_F(y)}N,
\]

where

\[
m_F(y)=|F^{-1}(\{y\})|.
\]

Thus the ordinary output probability distribution is obtained only after the integer fiber sizes are known.

## 3. P011-E01 — Pair-collision probability is an affine function of \(J_2\)

Status: `PROVED`

The probability that two independent uniformly sampled histories have the same \(F\)-image is

\[
P_{\rm same}
=
\sum_y p_y^2.
\]

Since

\[
\sum_y m_F(y)^2
=
N+2J_2(F),
\]

we obtain

\[
\boxed{
P_{\rm same}
=
\frac{N+2J_2(F)}{N^2}.
}
\]

Therefore P011's primitive integer pair-collision count contains exactly the same second-moment information as the usual collision probability, before normalization into rational numbers.

## 4. P011-E02 — Rényi-2 entropy is a logarithmic transform of \(J_2\)

Status: `PROVED COMPARISON`

The order-2 Rényi entropy of the output distribution is

\[
H_2(F)
=
-\log\sum_y p_y^2.
\]

Using P011-E01,

\[
\boxed{
H_2(F)
=
-\log\left(\frac{N+2J_2(F)}{N^2}\right).
}
\]

Because \(J_2\) is forward nondecreasing under deterministic postcomposition, \(H_2\) of the reachable output labels is nonincreasing.

Equivalently, the derived quantity

\[
L_2(F)=\log N-H_2(F)
\]

is nondecreasing and may be interpreted as a Rényi-2 style loss relative to the fully distinguishable uniform history set.

Enterprise Math does **not** make \(H_2\) or \(L_2\) primitive. The primitive state data remain \(N\) and the integer collision counts.

## 5. P011-E03 — Shannon entropy is determined by the fiber-size distribution

Status: `PROVED COMPARISON`

The Shannon entropy of the output is

\[
H_1(F)
=
-\sum_y p_y\log p_y.
\]

Substituting \(p_y=m_y/N\),

\[
H_1(F)
=
\log N
-
\frac1N\sum_y m_F(y)\log m_F(y).
\]

Hence

\[
\boxed{
\log N-H_1(F)
=
\frac1N\sum_y m_F(y)\log m_F(y).
}
\]

This is a real/logarithmic functional of the exact integer fiber-size multiset.

The full P011 collision spectrum reconstructs that multiset by integer binomial inversion, so the full spectrum determines \(H_1\) exactly once the logarithm convention is chosen.

## 6. P011-E04 — The full integer spectrum determines every symmetric output-probability functional

Status: `PROVED`

P011-T05 reconstructs

\[
c_r(F)=\#\{y:m_F(y)=r\}
\]

from the integer collision spectrum \((J_1,\ldots,J_N)\).

Therefore it reconstructs the multiset

\[
\{p_y\}_y
=
\left\{\frac{m_F(y)}N\right\}_y.
\]

Consequently, every quantity depending only on the multiset of output probabilities is determined by the integer spectrum, including:

- Shannon entropy;
- Rényi entropies of finite order;
- power sums \(\sum p_y^q\) for integer \(q\ge2\);
- collision probabilities;
- any symmetric statistic of fiber-size frequencies.

This does not mean every such quantity is a polynomial in one low-order \(J_k\). The **full** spectrum carries the complete block-size information.

## 7. Why \(J_2\) alone is not complete

Different fiber-size multisets can have the same pair-collision count.

For example, at sufficiently large \(N\), distinct partitions can share the same value of

\[
\sum_y\binom{m_y}2
\]

while differing in higher \(J_k\).

Therefore pair collision is a useful scalar detector but does not replace the full collision hierarchy.

The higher coefficients are not decorative: they are exactly what makes reconstruction possible.

## 8. Direction under many-to-one forward dynamics

For a deterministic postcomposition \(G\circ F\):

- all \(J_k\), \(k\ge2\), are nondecreasing;
- collision probability \(\sum p_y^2\) is nondecreasing;
- Rényi-2 output entropy is nonincreasing;
- Shannon output entropy is also nonincreasing because deterministic postprocessing cannot increase the entropy of a deterministic coarse-graining of a uniform source.

The integer statement is structurally prior in the Enterprise Math presentation: the partition blocks merge first; probabilistic/logarithmic monotonicities are consequences after a probability model is placed on those blocks.

## 9. Relation to preimage/folding entropy literature

Enterprise Math already records established prior work on preimage entropy and folding entropy:

- `SRC-NITECKI-PRZYTYCKI-1999`;
- `SRC-CHENG-NEWHOUSE-2005`;
- `SRC-RUELLE-1996`;
- `SRC-WU-ZHU-2021`.

Those literatures are evidence that noninvertibility/preimage structure and entropy have long been connected. P011 must not claim discovery of that connection.

The project-specific ordering is methodological:

1. record exact finite fibers;
2. use integer collision counts / collision polynomial as primitive observables;
3. introduce normalized probabilities and logarithmic entropy only as optional derived transforms.

## 10. Interpretation boundary

Nothing here establishes thermodynamic entropy production from Enterprise Math collapse.

To connect the integer collision spectrum to physical thermodynamics one would still need:

- a physical ensemble interpretation;
- energy/Hamiltonian structure;
- a time/process model;
- a definition of thermodynamic entropy or entropy production appropriate to that model;
- experimental comparison.

P011 therefore supports entropy **comparison**, not an identification theorem between history merging and thermodynamic entropy.
