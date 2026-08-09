# P022 — Barlow Coordination History Reconstructs Hidden Drift and Geodesic Totals

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE HISTORY RECONSTRUCTION / HIGHER-DIMENSION BOUNDARY PROVED`  
Owner: `program/p022-geometry-v2`  
Depends on: BC04 shell-energy formula and BG01/BG02 layer geodesic formula  
Cross-route relevance: P010 history, P018 kernel-time/predictive closure, P023/P024 observation factorization

## 1. Instantaneous shell cardinality is not enough

At one fixed radius `n`, shell cardinality determines only

\[
Q_n=\delta_n^2+\delta_{-n}^2.
\]

Static sum-of-two-squares ambiguity eventually appears. At radius seven,

\[
\boxed{
50=1^2+7^2=5^2+5^2.}
\]

So one shell count `S_7` cannot determine the unordered pair

\[
\{|\delta_7|,|\delta_{-7}|\}.
\]

This note proves that keeping the **whole preceding coordination history** removes that ambiguity exactly.

## 2. Absolute drift evolves by one reflected unit

For one one-sided ±1 prefix, let

\[
d_q=|\delta_q|.
\]

Appending one sign changes signed imbalance by `±1`. Therefore

\[
\boxed{
d_{q+1}\in
\begin{cases}
\{1\},&d_q=0,\\
\{d_q-1,d_q+1\},&d_q>0.
\end{cases}}
\]

For the two sides of the Barlow root, the hidden state relevant to whole-shell symmetric observables is the unordered pair

\[
\boxed{P_q=\{d_q^+,d_q^-\}.}
\]

The initial state is

\[
P_0=\{0,0\}.
\]

## 3. P022-CH01 — successor energy is injective on two-channel drift orbits

Fix one current unordered absolute pair

\[
P=\{a,b\}.
\]

Choose a signed representative. Under one microscopic step, squared energy changes by

\[
(a+\epsilon)^2+(b+\eta)^2-(a^2+b^2)
=2+2(a\epsilon+b\eta),
\]

where `epsilon,eta in {−1,+1}` with the obvious reflected convention at zero.

The four cross terms are

\[
a+b,\quad a-b,\quad-a+b,\quad-a-b.
\]

If two of these values coincide, then either

- `a=b`;
- one coordinate is zero;
- or the two choices differ only by exchanging the coordinates.

In every such case the resulting **unordered absolute successor pair is the same**.

Therefore distinct successor orbits have distinct next squared energies:

\[
\boxed{
P_{q+1}\ne P'_{q+1}
\Longrightarrow
\|P_{q+1}\|_2^2\ne\|P'_{q+1}\|_2^2.}
\]

This is the crucial two-channel injectivity theorem.

## 4. P022-CH02 — the complete Q-history uniquely reconstructs unordered drift history

Suppose

\[
Q_q=(d_q^+)^2+(d_q^-)^2
\]

is known for every `0<=q<=n`.

Reconstruct recursively:

1. start with `P_0={0,0}`;
2. enumerate the finite successor orbits of `P_q` under the one-step reflected rule;
3. choose the unique successor whose squared energy equals `Q_{q+1}`.

CH01 proves uniqueness at every step.

Hence

\[
\boxed{
(Q_0,Q_1,\ldots,Q_n)
\longleftrightarrow
(P_0,P_1,\ldots,P_n)
}
\]

for legal Barlow two-sided windows, where the right side remembers the pair only up to exchanging the two sides.

Since fixed-radius shell cardinality is equivalent to `Q_q`,

\[
\boxed{
(S_0,S_1,\ldots,S_n)
\longrightarrow
(P_0,P_1,\ldots,P_n).}
\]

The map is exact and finite.

## 5. Static ambiguity is resolved by history

At radius seven, `Q_7=50` admits the two static representations

\[
\{1,7\}
\quad\text{and}\quad
\{5,5\}.
\]

But no legal Barlow history can reach both from the same radius-six drift orbit with the same `Q_6`.

Thus two microscopic windows ending in these two states necessarily differ in earlier shell cardinalities.

The ambiguity is not removed by a finer instantaneous coordinate; it is removed by **retaining temporal/radial observation history**.

## 6. P022-CH03 — coordination history reconstructs whole-shell geodesic total

BG01/BG02 express the radius-`n` whole-shell shortest-path total as

\[
T_n
=L_{n,0}(0)
+
\sum_{q=1}^{n}
\left(
L_{n,q}(d_q^+)
+L_{n,q}(d_q^-)
\right).
\]

For each height `q`, the right side is symmetric under exchanging the positive and negative sides. Therefore the unordered pair `P_q` is sufficient.

CH02 then gives

\[
\boxed{
(S_0,S_1,\ldots,S_n)
\Longrightarrow
T_n.}
\]

No literal stacking word is needed.

Applying the same reconstruction at every prefix radius yields the stronger history map

\[
\boxed{
\mathcal H_S(n)
:=(S_0,\ldots,S_n)
\Longrightarrow
\mathcal H_T(n)
:=(T_0,\ldots,T_n).}
\]

## 7. P022-CH04 — the history map is not reversible

FCC-like constant drift and HCP-like alternating drift give, through radius two,

\[
\boxed{
\mathcal H_T(2)=(1,12,84)
}
\]

for both geometries.

But their coordination histories are

\[
\boxed{
\mathcal H_S^{FCC}(2)=(1,12,42),}
\]

and

\[
\boxed{
\mathcal H_S^{HCP}(2)=(1,12,44).}
\]

Therefore

\[
\boxed{
\mathcal H_T(2)
\not\Rightarrow
\mathcal H_S(2).}
\]

So the coordination history is strictly more informative than the path-total history on this finite domain.

This is striking because the **instantaneous** observables `S_n` and `T_n` are themselves incomparable. Retaining history changes their information order.

## 8. Observation-order reversal induced by history

We now have three distinct statements:

### Single radius

\[
S_n\not\Rightarrow T_n,
\qquad
T_n\not\Rightarrow S_n.
\]

### Coordination history

\[
\mathcal H_S(n)\Rightarrow\mathcal H_T(n).
\]

### Reverse history

Already at radius two,

\[
\mathcal H_T(n)\not\Rightarrow\mathcal H_S(n).
\]

Hence adding the **history axis** does not merely add more information to each observation; it can reorder the factorization poset.

This is a concrete geometry realization of the P010/P018 principle that a time-labelled kernel/history can preserve distinctions absent from a terminal coarse statistic.

## 9. P022-CH05 — two dimensions are essential

The injective successor-energy property is not a generic theorem for quadratic energy histories.

In three hidden drift coordinates, start from absolute state

\[
(3,2,1),
\qquad Q=14.
\]

Two legal one-step absolute successor orbits are

\[
(2,3,2)
\]

and

\[
(4,1,0).
\]

Both have

\[
\boxed{Q'=17,}
\]

but they are not related by coordinate permutation or sign reflection.

Therefore scalar quadratic-energy history fails to determine the hidden orbit already in dimension three.

So CH02 is a genuine **two-channel Barlow theorem**, not a generic statement that energy history always reconstructs hidden state.

This negative boundary must be preserved if the result is abstracted upstream.

## 10. What else coordination history can reconstruct

Each target-layer multiplicity histogram depends on its layer height and `|delta_q|`, while changing the drift sign only reflects coordinates. Therefore the unordered pair trajectory also determines any **global shell observable** that combines the positive and negative layer contributions symmetrically and forgets the side label.

Examples include:

- whole-shell total geodesic count `T_n`;
- global shortest-path multiplicity spectrum, once evaluated from the existing Barlow coefficient formulas;
- any symmetric polynomial/moment of the two layer contributions at every height.

It does **not** determine:

- which drift magnitude belongs to the positive versus negative side when the history permits side exchange;
- signed coordinate centroids;
- fully coordinate-labelled shell geometry.

Those require orientation-sensitive observations.

## 11. Upstream consequence

This note gives a precise warning for general precision mathematics:

> a coarse observable that is insufficient instantaneously can become sufficient after enough labelled history is retained.

But the effect depends on the transition law. In Barlow geometry, the hidden two-channel ±1 dynamics makes the energy observation recursively observable; in three dimensions the same scalar observation already fails.

Any generic promotion belongs to P018/P023/P024 and must state the transition-specific observability condition. P022 retains the exact close-packed instance and counterexample.

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_coordination_history.py`;
- `tests/test_p022_barlow_coordination_history.py`.

The tests reconstruct unordered drift histories and geodesic totals from complete shell-cardinality histories for all short microscopic two-sided windows, preserve the static radius-seven ambiguity, and encode the FCC/HCP reverse-history counterexample.
