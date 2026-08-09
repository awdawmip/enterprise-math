# P018 — Finite-Precision Proof Calculus: Supplement 25

Status: `ACTIVE RESEARCH NOTE`  
Scope: minimum n-ary additive transport, associative carry/detail composition, operation-tree fusion, and the boundary between persistent state and composable transport  
Depends on: P018-T178, T198–T206, and the established carry coherence layer  
Prior-art boundary: radix carry arithmetic, Euclidean decomposition, and carry associativity/cocycle coherence are established. The project-specific content is the state/transport minimality split and its finite transport-complexity interpretation.

---

## 1. From binary carry to a whole addition tree

Supplement 24 proved

\[
B_{Q_r}(+)=2.
\]

For a single binary addition, one carry bit is the exact minimum one-step transport token once the decoder knows the two coarse quotient inputs.

But an expression tree with many additions raises a stronger question:

> must every binary node expose an independent carry bit, or can the whole tree be fused into a smaller exact transport object?

For addition, the answer is exact.

Write

\[
x_i=r a_i+u_i,
\qquad 0\le u_i<r,
\qquad i=1,\ldots,n.
\]

Then

\[
Q_r\!\left(\sum_{i=1}^n x_i\right)
=
\sum_{i=1}^n a_i
+
\left\lfloor\frac{\sum_i u_i}{r}\right\rfloor.
\]

All transport ambiguity is carried by one integer.

---

## 2. P018-T207 — Exact n-ary additive transport branching

Status: `PROVED / EXECUTABLE`

Define the total carry

\[
\boxed{
c_{r,n}(u_1,\ldots,u_n)
=
\left\lfloor\frac{u_1+\cdots+u_n}{r}\right\rfloor.
}
\]

The residue sum can realize every integer from `0` through

\[
n(r-1).
\]

Therefore the total carry realizes every integer from

\[
0
\quad\text{through}\quad
\left\lfloor\frac{n(r-1)}r\right\rfloor.
\]

Hence the exact one-shot transport branching is

\[
\boxed{
B_{Q_r}(+_n)
=
1+\left\lfloor\frac{n(r-1)}r\right\rfloor.
}
\]

In particular,

\[
B_{Q_r}(+_n)\le n.
\]

For `n=2`, this recovers T204.

---

## 3. P018-T208 — The total carry is the minimum one-shot token

Status: `PROVED / EXECUTABLE`

Given all coarse inputs `a_i`, the exact coarse output differs from

\[
\sum_i a_i
\]

only by `c_(r,n)`.

Since every value of the total carry range is realizable in one fixed coarse input cell, T200 applies sharply:

\[
\boxed{
|\mathcal C|_{\min}
=
1+\left\lfloor\frac{n(r-1)}r\right\rfloor.
}
\]

Thus the total carry itself is a minimum-cardinality deterministic one-shot transport token.

Its exact fixed-length binary cost is

\[
\boxed{
L_{r,n}
=
\operatorname{bitlen}
\left(\left\lfloor\frac{n(r-1)}r\right\rflooright).
}
\]

No floating logarithm is needed.

---

## 4. P018-T209 — Carry/detail composition law

Status: `PROVED / EXECUTABLE / ESTABLISHED ARITHMETIC FORM`

For any finite block of residues, retain its Euclidean transport state

\[
\boxed{
(c,t)
\quad\text{where}\quad
\sum u_i=rc+t,
\qquad 0\le t<r.
}
\]

For two blocks

\[
(rc+t),
\qquad
(rc'+t'),
\]

the combined state is

\[
\boxed{
(c,t)\star(c',t')
=
\left(
 c+c'+\kappa_r(t,t'),
 (t+t')\bmod r
\right),
}
\]

where

\[
\kappa_r(t,t')
=
\left\lfloor\frac{t+t'}r\right\rfloor.
\]

This is simply exact Euclidean addition in `(carry,remainder)` coordinates. The carry cocycle/coherence itself is established prior arithmetic and was already recorded in the earlier P018 carry layer.

The important project interpretation is:

- `t` is persistent exact state detail;
- `c` is accumulated transport information;
- the next transport correction depends on the persistent detail coordinates.

---

## 5. P018-T210 — Associativity and tree independence

Status: `PROVED / EXECUTABLE`

Because `(c,t)` losslessly represents the natural number `rc+t`, the operation `star` is associative:

\[
\boxed{
((c,t)\star(c',t'))\star(c'',t'')
=
(c,t)\star((c',t')\star(c'',t'')).
}
\]

Therefore any binary parenthesization of the same residue list yields the same final pair

\[
\boxed{
\left(
\left\lfloor\frac{\sum_i u_i}{r}\right\rfloor,
\left(\sum_i u_i\right)\bmod r
\right).
}
\]

So additive structured transport is independent of operation-tree shape once the persistent remainder state is carried alongside the accumulated transport token.

---

## 6. P018-T211 — Fusion beats independent binary carry fields

Status: `PROVED / EXECUTABLE`

A binary tree with `n` leaves has `n-1` internal addition nodes. If each node exposes an independent fixed one-bit carry field, the modular transport budget is

\[
\boxed{n-1\text{ bits}.}
\]

The globally fused minimum one-shot token instead uses

\[
L_{r,n}
=
\operatorname{bitlen}
\left(\left\lfloor\frac{n(r-1)}r\right\rfloor\right)
\]

bits.

Because

\[
B_{Q_r}(+_n)\le n,
\]

one has

\[
\boxed{
L_{r,n}\le\lceil\log_2 n\rceil\le n-1
}
\]

for `n>=2`.

Thus generic node-by-node carry transport can be dramatically nonminimal when the whole expression is available for fusion.

This does **not** say every sequential implementation can simply discard intermediate state. It compares the fixed-width information budget of separate carry fields with the exact one-shot token when all coarse leaf inputs are known.

---

## 7. P018-C23 — The minimum carry token alone is not recursively composable

Status: `COUNTEREXAMPLE / STRUCTURED-TRANSPORT BOUNDARY`

A minimum one-shot token need not contain enough state information to be composed as a reusable subtree interface.

For every `r>=2`, compare two left subtree transport states

\[
(0,0),
\qquad
(0,r-1).
\]

They have the **same carry token** `0` but different persistent remainder detail.

Combine either with right subtree state

\[
(0,1).
\]

Then

\[
(0,0)\star(0,1)
=(0,1),
\]

while

\[
(0,r-1)\star(0,1)
=(1,0).
\]

The next carry differs.

Therefore

\[
\boxed{
\text{carry token alone is not a closed recursive transport state.}
}
\]

The persistent remainder is not an implementation accident that can be deleted because a small transport token exists.

---

## 8. P018-T212 — A complete structured-transport solution for radix addition

Status: `RESOLVED FOR THIS OPERATION FAMILY`

For n-ary natural-number addition viewed through `Q_r`, the structured transport problem has an exact finite solution:

1. minimum persistent operand detail is the residue `u in {0,...,r-1}` from T178;
2. minimum one-shot operation token is the total carry from T207/T208;
3. recursive composition is performed by the associative `(carry,remainder)` law T209;
4. arbitrary binary tree grouping yields the same result by T210;
5. globally fused fixed-width carry cost is at most logarithmic in arity, while separate node carry fields cost `n-1` bits;
6. C23 proves why transport token and persistent state must remain distinct concepts.

Thus radix addition supplies a **positive structured-composability exemplar** for Q119.

It does not classify other operations. T205 already shows that multiplication has radically larger one-step branching and may require a different transport structure.

---

## 9. P018-C24 — Cardinality does not determine compositional structure

Status: `FOUNDATIONAL BOUNDARY`

Knowing only

\[
B_E(\mu)
\]

answers the minimum one-shot token alphabet question, but it does not determine:

- whether the token has a natural algebraic operation;
- whether local tokens compose without extra state;
- whether an associative fusion law exists;
- whether a representation change preserves the token law;
- whether generic operation-tree product bounds can be fused sharply.

Addition succeeds because Euclidean remainder state and carry satisfy an exact composition law. The same conclusion cannot be inferred from a small value of `B` alone.

Therefore Q119 must retain two distinct layers:

\[
\boxed{
\text{transport cardinality}
\quad\neq\quad
\text{transport algebra}.
}
\]

---

## 10. Q119 status after Supplement 25

The question is now split cleanly:

### Resolved

- exact one-step deterministic token cardinality for every finite operation: T198–T206;
- generic operation-tree product upper bound;
- persistent-state vs transport-token inequality;
- complete structured minimal transport for radix addition: T207–T212.

### Still open

A general criterion classifying when a finite operation admits a minimal or near-minimal **representation-stable composable transport algebra**.

The next pressure target should compare operation families with equal or similar `B_E(mu)` but different composability, rather than continue adding state quotients.

---

## 11. Executable validation

Added:

- `src/enterprise_math/transport_fusion.py`
- `tests/test_transport_fusion.py`

Tests verify:

1. the exact n-ary branching formula by exhaustive residue enumeration on bounded radices/arities;
2. total carry and Euclidean reconstruction;
3. associativity of `(carry,remainder)` composition;
4. independence of binary tree grouping;
5. fused bit cost is never worse than `n-1` separate one-bit carry fields;
6. C23 for every tested radix;
7. n-ary transport capacity grows at most linearly rather than as the naive binary-tree token-product count.
