# P022 — Barlow Observation Lattice and Incomparable Precision Shadows

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE SEPARATIONS / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Scope: rooted shell observables of close-packed contact graphs  
Purpose: demonstrate concretely that exact precision is a partial order indexed by future observables, not a single scalar ladder

## 1. One geometry, several non-equivalent shadows

Fix a rooted Barlow contact graph and radius `n`.

The same finite shell supports many exact observations:

1. the coordinate-labelled endpoint set;
2. the coordinate-labelled shortest-path count function;
3. multiplicity spectra resolved separately on every target layer;
4. the global shortest-path multiplicity spectrum;
5. shell cardinality;
6. total number of shortest paths into the shell.

Some of these observations deterministically forget to others. Some are incomparable.

The resulting structure is a finite information **poset**, not a linear precision scale.

## 2. Defined observables

Let `X_n` be the rooted shell.

### Coordinate-labelled path-count function

\[
\boxed{
F_n(v)=g(0,v),
\qquad v\in X_n.}
\]

The domain keeps the actual Barlow coordinates/layer labels.

### Layer-resolved multiplicity spectrum

For each target layer `k`, define

\[
\boxed{
\Sigma_{n,k}(m)
=\#\{v\in X_n:\text{layer}(v)=k,\ g(0,v)=m\}.}
\]

### Global multiplicity spectrum

Forget the target layer:

\[
\boxed{
\Sigma_n(m)
=\sum_k\Sigma_{n,k}(m).}
\]

### Shell cardinality

\[
\boxed{
S_n=\sum_m\Sigma_n(m).}
\]

### Total geodesic multiplicity

\[
\boxed{
T_n=\sum_m m\,\Sigma_n(m).}
\]

Thus the global spectrum determines both `S_n` and `T_n`.

## 3. Exact forgetful maps

There are canonical maps

\[
F_n
\longrightarrow
(\Sigma_{n,k})_k
\longrightarrow
\Sigma_n
\longrightarrow
(S_n,T_n).
\]

The last node then projects separately to

\[
S_n
\quad\text{and}\quad
T_n.
\]

Every arrow is an exact finite postprocessing operation.

The question is whether any arrow can be reversed from the coarser observable alone. The counterexamples below show that, in general, none can.

## 4. P022-OL01 — shell cardinality does not determine total geodesic count

At radius `3`, consider the two period-three stackings

\[
(-,-,+)
\]

and

\[
(-,+,-).
\]

Both have

\[
\boxed{S_3=96.}
\]

But their total shortest-path multiplicities are

\[
\boxed{T_3=402}
\]

and

\[
\boxed{T_3=384}
\]

respectively.

Hence

\[
\boxed{S_n\not\Rightarrow T_n.}
\]

In precision language, the quadratic drift energy `Q_n` sufficient for shell cardinality is not sufficient for path multiplicity.

## 5. P022-OL02 — total geodesic count does not determine shell cardinality

At radius `2`, FCC and HCP both have

\[
\boxed{T_2=84.}
\]

But

\[
S_2^{FCC}=42,
\qquad
S_2^{HCP}=44.
\]

Therefore

\[
\boxed{T_n\not\Rightarrow S_n.}
\]

So `S_n` and `T_n` are genuinely incomparable observables. Neither is simply “higher precision” than the other.

Their joint observation `(S_n,T_n)` is strictly stronger than either coordinate separately.

## 6. P022-OL03 — even `(S_n,T_n)` does not determine multiplicity spectrum

At radius `3`, take the period-five words

\[
(-,-,-,+,-)
\]

and

\[
(-,-,+,-,+).
\]

Both satisfy

\[
\boxed{(S_3,T_3)=(96,390).}
\]

But their global multiplicity spectra are different.

For the first:

\[
\boxed{
\Sigma_3=\{1:18,\ 3:54,\ 6:6,\ 9:18\}.}
\]

For the second:

\[
\boxed{
\Sigma_3=\{1:14,\ 2:8,\ 3:42,\ 5:4,\ 6:8,\ 9:20\}.}
\]

Both spectra have the same zeroth moment `S_3=96` and first multiplicity moment `T_3=390`, but different distributions.

Thus

\[
\boxed{(S_n,T_n)\not\Rightarrow\Sigma_n.}
\]

This is exactly the finite-moment phenomenon expected from the count-enriched A4/P021 bridge: a few moments do not determine the full witness distribution.

## 7. P022-OL04 — global spectrum does not determine layer-resolved spectrum

At radius `2`, the period-four words

\[
(-,-,-,+)
\]

and

\[
(-,+,-,+)
\]

share the same **global** multiplicity spectrum

\[
\boxed{
\Sigma_2=\{1:18,\ 2:18,\ 3:2,\ 4:6\}.}
\]

However the multiplicities are allocated differently among target layers.

Therefore

\[
\boxed{
\Sigma_n\not\Rightarrow(\Sigma_{n,k})_k.}
\]

The global histogram has forgotten where each witness multiplicity lives.

## 8. P022-OL05 — layer-resolved spectrum does not determine coordinate-labelled geometry

Take the two constant-drift patterns

\[
(-)
\]

and

\[
(+).
\]

They are related by horizontal reflection. Consequently they have identical layer-resolved multiplicity spectra at every radius.

In a fixed axial coordinate chart, however, the coordinate-labelled path-count functions are reflected and therefore unequal:

\[
F_n^-\ne F_n^+.
\]

Thus

\[
\boxed{
(\Sigma_{n,k})_k\not\Rightarrow F_n.}
\]

This is not a physical inequivalence claim. It simply exhibits the exact information lost when coordinate labels are quotiented out.

## 9. The resulting observation poset

The proved relationships can be summarized as

\[
\boxed{
F_n
\to
(\Sigma_{n,k})_k
\to
\Sigma_n
\to
(S_n,T_n),
}
\]

with

\[
(S_n,T_n)\to S_n,
\qquad
(S_n,T_n)\to T_n,
\]

but

\[
S_n\not\to T_n,
\qquad
T_n\not\to S_n.
\]

Every displayed reverse failure has an explicit finite Barlow counterexample.

This is already enough to rule out a universal scalar notion of “how precise the shell state is.”

## 10. Relationship to coordinate-sensitive support moments

The coordination-moment supplement gives another branch of the poset.

For one selected target layer, the coordinate-sensitive shell set has first moment that recovers signed `delta_k`, while the non-extreme layer cardinality is independent of stacking.

So even within **existence-only geometry**, there is a strict split between

\[
\text{coordinate-labelled membership}
\]

and

\[
\text{cardinality of that membership set}.
\]

The difference is not caused by path multiplicity. It is already present at the Boolean support level.

## 11. P023/P024 consequence — precision should be organized by observation factorization

The Barlow examples suggest the right abstraction is not a scalar “precision level” but a factorization order on observations.

If observation `O_2` is a deterministic function of `O_1`, then `O_1` is at least as informative for that future language. If neither factors through the other, the two observations are incomparable.

Here:

- `Sigma_n` factors to both `S_n` and `T_n`;
- `S_n` and `T_n` do not factor through each other;
- their product observation `(S_n,T_n)` still does not reconstruct `Sigma_n`.

This is an exact finite specialization of the general quotient/factorization principles already owned by A2/P023/P024.

P022 should retain the concrete geometry and counterexamples; the abstract observation-poset theorem, if promoted, belongs upstream.

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_observables.py`;
- `tests/test_p022_barlow_observables.py`.

The tests encode all four strict separation examples and verify every forward forgetful map exactly.
