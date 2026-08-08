# P019 Supplement 10 — Direction transport is a relation, not generally a map

Status: `TESTING / FINITE COMBINATORIAL CORE PROVED`

## 1. Motivation

Stage 8 defined intrinsic direction classes as marked-section automorphism orbits of outgoing primitive incidences. Stage 9 proved that causal phase roles are a coarser structural partition than those direction orbits.

The next question is dynamical: given

\[
A_{t+1}=F(A_t),
\]

can a direction class at time \(t\) be canonically identified with one direction class at time \(t+1\)?

A static anisotropy diagnostic cannot legitimately be called shear-like unless some non-arbitrary transport of direction classes exists.

## 2. Canonical composability matrix

Let

\[
D_1^{(t)},\ldots,D_r^{(t)}
\]

be the intrinsic direction classes of incidences from \(A_t\) into \(A_{t+1}\), and let

\[
D_1^{(t+1)},\ldots,D_s^{(t+1)}
\]

be those from \(A_{t+1}\) into \(A_{t+2}\).

Define

\[
\boxed{
T_{ij}
=
\#\{((u,v),(v,w)):(u,v)\in D_i^{(t)},\ (v,w)\in D_j^{(t+1)}\}.
}
\]

Thus \(T_{ij}\) counts primitive composable two-paths through the shared middle section. It is an integer object determined only by the directed incidence structure and the chosen intrinsic direction partitions.

No Euclidean direction, angle, probability, or fractional normalization is used.

## 3. Transport support

Only the support

\[
S_{ij}=1[T_{ij}>0]
\]

is needed to ask whether direction-class identity can be transported.

For a current class \(D_i^{(t)}\), its support row can meet:

- no next class: a direction death at this resolution;
- exactly one next class: locally functional continuation;
- several next classes: direction split.

Dually, a next class can receive support from zero, one, or several current classes, producing birth, unique predecessor, or merge.

## 4. Canonical one-to-one transport criterion

A one-to-one identity transport exists from composability alone exactly when the support matrix is a permutation matrix:

1. the number of current and next classes is equal;
2. every row has exactly one nonzero support entry;
3. every column has exactly one nonzero support entry.

Then there is a unique matching

\[
\pi:\{1,\ldots,r\}\to\{1,\ldots,r\}
\]

such that

\[
T_{i,\pi(i)}>0.
\]

The positive values \(T_{i,\pi(i)}\) need not equal one. They measure two-path multiplicity, not direction-class identity.

## 5. No-go for generic direction identity

In general the support need not be a permutation matrix.

A single current direction can split into several next directions. Several current directions can merge into one next direction. Classes can appear or disappear at the chosen structural resolution.

Therefore:

\[
\boxed{
\text{intrinsic direction evolution is canonically a relation, not generally a function.}
}
\]

Consequently, assigning persistent labels such as `direction 1`, `direction 2`, ... across arbitrary time steps would introduce an extra choice not determined by the primitive causal structure.

This is a structural no-go against naive dynamic shear analogies.

## 6. Consequence for anisotropy evolution

The Stage-8 static diagnostic

\[
A_C
=
\sum_{i<j}(E_jC_i-E_iC_j)^2
\]

is well-defined independently on each section.

But the difference

\[
A_C(t+1)-A_C(t)
\]

is only a change in an aggregate scalar. It does **not** by itself describe transport of particular directional deformations.

A componentwise directional evolution law is canonical only on steps where the transport support gives a unique one-to-one matching. On split/merge/birth/death steps, any componentwise correspondence requires additional structure.

P019 therefore does not identify static \(A_C\), nor its raw time difference, with physical shear.

## 7. Stronger structural picture

The current hierarchy is

\[
\text{phase/boundary}
\to
\text{causal roles}
\to
\text{direction orbits}
\to
\text{transport relation }T
\to
\text{one-to-one identity only on permutation-support steps}.
\]

This allows direction identity itself to split or merge, rather than presupposing a fixed tangent vector basis.

## 8. Next gate

The next useful question is whether a weaker invariant can be transported through arbitrary relation matrices without choosing a matching. The natural candidates are not new scalar observables, but functorial data already present in P019:

- total incidence flow through transport support;
- causal-role preservation or change;
- collision-spectrum information aggregated over transport-connected components.

If these admit exact composition across multiple steps, P019 gains a genuine categorical/relational dynamics of direction classes. If not, the no-go boundary should be retained.

## 9. Scope discipline

This supplement does not claim a discrete Levi-Civita connection, parallel transport, tangent bundle, geodesic deviation equation, Raychaudhuri equation, or physical shear tensor. The word `transport` means only the canonical finite relation induced by composable primitive causal incidences.
