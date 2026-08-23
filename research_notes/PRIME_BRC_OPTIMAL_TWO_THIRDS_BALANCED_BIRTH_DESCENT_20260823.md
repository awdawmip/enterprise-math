# Prime-BRC Optimal Two-Thirds Balanced Birth Descent

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

Depends on the floor-birth tree definition

\[
\mathsf B(n)=\{d:d|n,\sqrt n\le d<n\}.
\]

## 1. Balanced divisor lemma

### Lemma

Let `n>=4` be composite and assume every prime factor of `n` is at most `sqrt(n)`. Then there exists a divisor `a|n` satisfying

\[
\boxed{n^{1/3}\le a\le n^{1/2}.}
\]

### Proof

Write the prime factors with multiplicity as

\[
n=p_1p_2\cdots p_m.
\]

Normalize logarithms

\[
x_i=\frac{\log p_i}{\log n}.
\]

Then

\[
0<x_i\le\frac12,
\qquad
\sum_i x_i=1.
\]

If some `x_i` lies in `[1/3,1/2]`, take `a=p_i`.

Otherwise every `x_i<1/3`. Add terms until the partial sum first reaches at least `1/3`.

- If the resulting sum is at most `1/2`, use that subset.
- If it lies in `(1/2,2/3)`, its complement has sum in `(1/3,1/2)` and supplies the required subset.

Exponentiating the selected logarithmic subset gives the divisor `a`. ∎

## 2. Two-thirds birth child theorem

Let `n` be composite.

### Case A — a prime factor above sqrt(n)

If

\[
q=P^+(n)>\sqrt n,
\]

then `q` is a proper divisor in the birth fiber and is itself prime. Thus the birth tree reaches a prime leaf in one edge.

### Case B — no prime factor above sqrt(n)

Apply the balanced divisor lemma and choose

\[
n^{1/3}\le a\le n^{1/2}.
\]

Let

\[
d=n/a.
\]

Then

\[
\boxed{n^{1/2}\le d\le n^{2/3}.}
\]

Since `d|n` and `d<n`, it is a proper birth child.

Therefore every composite integer has either an immediate prime birth child or a proper birth child with numerical size at most `n^(2/3)`.

Freeze:

\[
\boxed{
\forall n\text{ composite},\quad
\exists d\in\mathsf B(n):
\quad d\text{ prime}\ \text{or}\ d\le n^{2/3}.
}
\]

## 3. Shortest prime-leaf depth

Define `delta(n)` to be the minimum number of birth-tree edges from `n` to a prime leaf.

If `n` is prime, `delta(n)=0`.

For a composite nonterminal step, the theorem allows a child `d<=n^(2/3)`. Hence along a shortest balanced descent that has not already terminated,

\[
\log n_{j+1}\le\frac23\log n_j.
\]

Thus

\[
\boxed{
\log n_j\le
\left(\frac23\right)^j\log n_0.
}
\]

A composite integer is at least `4`. Consequently once

\[
\left(\frac23\right)^j\log n<\log4,
\]

the process must already have terminated at a prime.

Therefore

\[
\boxed{
\delta(n)
\le
1+
\left\lceil
\log_{3/2}\!\left(\frac{\log n}{\log4}\right)
\right\rceil
}
\]

is a valid coarse universal bound, and in particular

\[
\boxed{\delta(n)=O(\log\log n).}
\]

This is a shortest-path statement. The maximum birth-tree height remains exactly `Omega(n)-1`.

## 4. Sharpness of the exponent 2/3

Take

\[
n=p^3
\]

for a prime `p`.

The proper upper divisors are exactly

\[
\mathsf B(p^3)=\{p^2\}.
\]

Thus every birth path must begin with

\[
p^3\to p^2=(p^3)^{2/3}.
\]

Hence no universal theorem of the same form can replace the exponent `2/3` by any smaller exponent.

Freeze:

`UNIVERSAL_BALANCED_BIRTH_CONTRACTION_EXPONENT = 2/3 IS SHARP`.

## 5. Relation to deterministic least-factor descent

The canonical max-child path realizes the **maximum** tree depth

\[
\Omega(n)-1.
\]

Balanced branching instead realizes a prime leaf in double-logarithmic numerical depth.

Therefore the same birth tree simultaneously contains:

- a provenance-maximal least-factor path;
- a numerically fast balanced-collapse path.

This is a genuine distinction between deterministic factor stripping and branch-enabled BRC navigation.

## 6. Square-basin consequence

For a fully `K`-smooth state

\[
K^2<n<(K+1)^2,
\]

all prime factors satisfy

\[
p\le K<\sqrt n.
\]

Hence Case B applies immediately and there exists a proper birth child

\[
\boxed{
K<\sqrt n\le d\le n^{2/3}<(K+1)^{4/3}.
}
\]

For odd basin states, any such `d>K` can be the birth child of at most one odd basin root, by the previously proved odd unique-hit/no-recoalescence bound.

This gives an exact `2/3` downward-collapse interface for the fully-smooth branch, but by itself does not supply a small enough global child-capacity bound to prove Legendre.

## 7. Boundary

The theorem is existential. Finding the balanced child without divisor information is a separate algorithmic problem. No computational speedup is claimed.

Freeze:

`EVERY_COMPOSITE_HAS_PRIME_CHILD_OR_TWO_THIRDS_BIRTH_CHILD = true`.

`SHORTEST_PRIME_LEAF_BIRTH_DEPTH_IS_O_LOG_LOG_N = true`.

`TWO_THIRDS_EXPONENT_IS_SHARP_BY_PRIME_CUBES = true`.
