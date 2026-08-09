# P022 — Exact Order Repair After Collision-Polynomial Geometry Recovery

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE IDENTIFIABILITY BOUNDARY`  
Owner: `program/p022-geometry-v2`  
Depends on: collision-polynomial inversion, checkpoint fiber convolution  
Cross-route relevance: P011 completeness boundary; P023/P024 exact repair of an aggregated observation

## 1. The last loss after complete collision inversion

The complete P011 collision polynomial of a selected-layer Barlow quotient recovers exactly

\[
\boxed{
(\{\ell_1,\ldots,\ell_m\},u),
}
\]

where the `ell_j` are the observed checkpoint segment lengths as a **multiset** and `u` is the completely hidden tail length.

It does not recover the order

\[
(\ell_1,\ldots,\ell_m).
\]

That lost order is not a vague residual.  Its exact finite fiber size can be counted.

---

## 2. P022-OR01 — exact ordered-geometry fiber cardinality

For each positive integer segment length `ell`, let

\[
t_\ell
=
\#\{j:\ell_j=\ell\}.
\]

There are `m!` permutations of `m` labelled positions.  Permuting equal segment lengths does not change the ordered segment sequence, so the number of distinct ordered geometries represented by the recovered multiset is

\[
\boxed{
M_{\rm ord}
=
\frac{m!}{\prod_\ell t_\ell!}.
}
\]

Every distinct ordered segment sequence gives a distinct cumulative checkpoint tuple, because the original ordered segment sequence is recovered from consecutive differences of that tuple.

Conversely all permutations have the same collision polynomial because multiplicative fiber convolution is commutative.

Therefore

\[
\boxed{
|K_O^{-1}(K_O)\ \text{inside ordered checkpoint geometry}|
=
M_{\rm ord}.
}
\]

The hidden tail length `u` is already recovered by the collision polynomial and does not contribute another order ambiguity.

---

## 3. P022-OR02 — exact order-repair state

The collision polynomial plus one label in a finite set of cardinality

\[
M_{\rm ord}
\]

is sufficient to reconstruct the fully ordered segment sequence and hence the exact checkpoint locations.

No smaller uniform repair set can distinguish every ordered geometry in the same collision-polynomial fiber.

Thus, up to a bijective relabelling of the finite repair states,

\[
\boxed{
\text{minimal order-repair cardinality}=M_{\rm ord}.
}
\]

This formulation intentionally uses state cardinality rather than declaring logarithms primitive.

---

## 4. Equal spacing is a zero-repair special case

If all segments have the same length,

\[
\ell_1=\cdots=\ell_m=q,
\]

then

\[
t_q=m
\]

and

\[
\boxed{M_{\rm ord}=1.}
\]

So in the exactly equally spaced case the complete collision polynomial already identifies the **full ordered checkpoint geometry**; there is no remaining order repair.

This is stronger than saying equal spacing is good for image size or pair collision.  Its repeated segment symmetry also eliminates the last ordering ambiguity of the complete collision state.

---

## 5. P022-OR03 — near-uniform schedule order ambiguity

For the ordinary balanced schedule, write

\[
N=qm+r,
\qquad
0\le r<m.
\]

The segment multiset consists of

- `m-r` copies of `q`;
- `r` copies of `q+1`.

Therefore

\[
\boxed{
M_{\rm ord}^{\rm bal}
=
\binom mr.
}
\]

This has two important boundaries:

- if `r=0`, exact equal spacing gives `M_ord=1`;
- if both segment lengths occur, the collision polynomial still forgets which checkpoint gaps receive the longer intervals.

So near-uniform spacing need not be uniquely located even though its unordered geometry is already fully determined by the collision state.

---

## 6. Relationship to P011 completeness

P011 proves that the complete collision polynomial is a complete invariant of the **fiber-size multiset**, not of the labelled partition that generated it.

P022 sharpened that statement in two steps:

\[
\boxed{
K_O(t)
\Longleftrightarrow
(\text{segment multiset},\text{hidden tail})
}
\]

and now

\[
\boxed{
(\text{segment multiset},\text{hidden tail})
+\text{one }M_{\rm ord}\text{-state repair}
\Longleftrightarrow
\text{ordered checkpoint geometry}.
}
\]

Thus the exact P022 information chain is

\[
\boxed{
\text{ordered checkpoint geometry}
\to
\text{complete collision polynomial}
\to
\text{low-order collision shadows},
}
\]

with explicit inverse-repair cardinalities on the first arrow and explicit aliases on the second.

---

## 7. Why this is not a universal P011 theorem

The recovery of the segment multiset from the complete collision polynomial uses the special triangular binomial structure of Barlow prefix-imbalance segments.

For a general finite map, a collision polynomial need not reveal the mechanism or geometry that created the fibers.

Likewise, the multinomial order-repair formula is specific to the situation where the only remaining geometry is a permutation of an already recovered segment multiset.

So the general P011 theorem remains unchanged:

> collision polynomial = complete fiber-size statistics.

P022 adds a stronger inverse only inside its structured checkpoint family.

---

## 8. Precision interpretation

This result gives a clean example of **repair after commutative aggregation**.

The full collision state is strong enough to recover every segment length and the hidden tail, but commutative convolution erases temporal order.  The amount of repair is therefore controlled not by horizon length directly, but by the symmetry multiplicities of the recovered multiset:

\[
\boxed{
M_{\rm ord}=m!/\prod t_\ell!.
}
\]

Repeated segment lengths reduce order ambiguity; distinct segment lengths increase it.

This is another reason a single scalar “precision level” is inadequate: even after a statistically complete observation, the remaining hidden state may be purely **ordering information** rather than value uncertainty.

---

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_collision_order_repair.py`;
- `tests/test_p022_barlow_collision_order_repair.py`.

The tests enumerate distinct segment permutations on finite examples, verify that every permutation has the same complete collision coefficients, verify that the corresponding checkpoint layer tuples are distinct, and check the closed balanced-schedule value `C(m,r)`.
