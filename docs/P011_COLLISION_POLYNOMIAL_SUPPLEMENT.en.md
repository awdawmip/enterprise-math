# P011 Supplement — The integer collision polynomial

Status: `PROVED`  
Parent: `P011`

## 1. Definition

For a finite map

\[
F:X\to Y,
\qquad |X|=N,
\]

with nonempty fiber sizes

\[
m_F(y)=|F^{-1}(\{y\})|,
\]

define the **collision polynomial**

\[
K_F(t)
=
\sum_{y\in\operatorname{im}(F)}
\left((1+t)^{m_F(y)}-1\right).
\]

It lies in

\[
\mathbb N[t].
\]

Expanding each binomial gives

\[
K_F(t)
=
\sum_{k=1}^N
\left(
\sum_y\binom{m_F(y)}k
\right)t^k.
\]

Hence

\[
\boxed{K_F(t)=\sum_{k=1}^N J_k(F)t^k.}
\]

So the P011 collision spectrum is exactly the coefficient vector of one integer polynomial.

## 2. P011-S01 — Two-fiber merge factorization

Status: `PROVED`

Suppose one deterministic step merges exactly two old fibers of sizes \(a,b\) into one fiber of size \(a+b\), leaving all other fibers unchanged.

Then

\[
\Delta K(t)
=
(1+t)^{a+b}-1
-
\big((1+t)^a-1\big)
-
\big((1+t)^b-1\big).
\]

This factors exactly as

\[
\boxed{
\Delta K(t)
=
\big((1+t)^a-1\big)
\big((1+t)^b-1\big).
}
\]

### Proof

Expand the product:

\[
\big((1+t)^a-1\big)
\big((1+t)^b-1\big)
=
(1+t)^{a+b}-(1+t)^a-(1+t)^b+1.
\]

This is exactly the merge difference above. ∎

## 3. Combinatorial meaning

The factor

\[
(1+t)^a-1
\]

generates nonempty subsets chosen from the first old fiber, while

\[
(1+t)^b-1
\]

generates nonempty subsets chosen from the second.

Their product therefore generates exactly the newly colliding history subsets that contain at least one history from **each** old fiber.

Consequently, the coefficient of \(t^k\) in \(\Delta K\) is the exact number of newly identified \(k\)-history subsets created by this merge.

For \(k=2\), the coefficient is

\[
ab,
\]

recovering the P011 pair-increment formula.

## 4. P011-S02 — Coefficientwise monotonicity

Status: `PROVED`

For arbitrary deterministic postcomposition

\[
G:Y\to Z,
\]

\[
\boxed{
K_{G\circ F}(t)-K_F(t)
\in\mathbb N[t].
}
\]

Equivalently,

\[
K_F\preceq_{\rm coeff} K_{G\circ F},
\]

where \(\preceq_{\rm coeff}\) means coefficientwise order.

### Proof

Every coarsening of a finite fiber partition can be decomposed into finitely many pairwise block merges. P011-S01 shows that every elementary merge adds a polynomial with nonnegative integer coefficients. Summing the elementary increments gives the result. ∎

This is precisely the simultaneous monotonicity of all \(J_k\), packaged into one algebraic object.

## 5. P011-S03 — Strictness

Status: `PROVED`

If \(G\) is injective on \(\operatorname{im}(F)\), then

\[
K_{G\circ F}=K_F.
\]

If \(G\) merges two distinct reachable states, then

\[
K_{G\circ F}-K_F
\]

is a nonzero polynomial in \(\mathbb N[t]\).

Indeed, every actual merge has \(a,b\ge1\), so both factors in P011-S01 are nonzero.

Thus

\[
\boxed{
K_{G\circ F}=K_F
\iff
G|_{\operatorname{im}(F)}\text{ is injective}.
}
\]

## 6. P011-S04 — Completeness for block-size statistics

Status: `PROVED`

The collision polynomial uniquely determines the fiber-size multiplicities

\[
c_r(F)=\#\{y:m_F(y)=r\}.
\]

Reason: its coefficients are exactly the \(J_k\), and P011-T05 gives the integer binomial inversion

\[
c_r(F)
=
\sum_{k=r}^N
(-1)^{k-r}\binom kr J_k(F).
\]

Therefore \(K_F\) is a complete invariant of the **multiset of fiber sizes**.

It is not a complete invariant of the actual partition of labeled histories: different partitions with the same block sizes have the same polynomial.

## 7. Useful evaluations

### At \(t=0\)

\[
K_F(0)=0.
\]

### First derivative at zero

Formally,

\[
K_F'(0)=J_1=N,
\]

which is constant under every deterministic map on a fixed domain.

### At \(t=1\)

\[
K_F(1)
=
\sum_y(2^{m_F(y)}-1).
\]

This counts all nonempty history subsets already lying inside single fibers.

A merge of sizes \(a,b\) increases this evaluation by

\[
(2^a-1)(2^b-1)>0.
\]

So \(K_F(1)\) is one strictly increasing integer scalar whenever a new reachable merge occurs.

It is less informative than the whole polynomial but requires no logarithm or real arithmetic.

## 8. Relation to entropy

The collision polynomial is not defined from probabilities and does not use logarithms.

One may later compare transformations of \(K_F\), its coefficients, or normalized fiber frequencies with established entropy notions. Such comparisons are secondary constructions.

Enterprise Math should not call \(K_F\) “entropy” by definition.

## 9. Prior-art discipline

Binomial generating functions, subset-counting polynomials, partition block statistics and Vandermonde identities are established combinatorics. The factorization in P011-S01 is elementary algebra.

The project-specific use is to package the complete integer fiber-collision hierarchy into a single coefficientwise-monotone object before introducing probabilistic or logarithmic entropy. No historical-priority claim is made for the underlying combinatorics.
