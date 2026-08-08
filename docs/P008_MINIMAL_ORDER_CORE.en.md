# P008 — Minimal equality-faithful order core

Status: `PROVED STRUCTURAL RESOLUTION`

## Result

For the current v0.1 root / quotient / collapse pattern, Enterprise Math does not need a lattice, complete lattice, field, topology, metric, or real-number completion.

Let `A` and `B` be partially ordered state spaces and let

\[
l:A\to B.
\]

For each \(b\in B\), define the principal sublevel

\[
L_b=\{a\in A:l(a)\le b\}.
\]

A right adjoint \(u:B\to A\) exists exactly when every \(L_b\) has a greatest element; that greatest element is \(u(b)\). Equivalently,

\[
l(a)\le b\iff a\le u(b).
\]

Thus the `max` definition used by integer roots and integer quotients is precisely right-adjoint structure, not an approximation device.

## Exact recovery

Assume \(l\dashv u\). Then

\[
u(l(a))=a\quad\text{for all }a
\]

if and only if \(l\) reflects order. Since every left adjoint is monotone, this is exactly the requirement that \(l\) be an order embedding onto its image.

This one statement explains both

\[
R_p(k^p)=k
\]

and

\[
Q_d(dq)=q.
\]

## Induced collapse

Define

\[
C=l\circ u:B\to B.
\]

On partial orders, standard Galois-connection theory gives

\[
C(b)\le b,
\]

monotonicity,

\[
C(C(b))=C(b),
\]

and

\[
C(b)=b\iff b\in\operatorname{im}(l).
\]

So the abstract collapse core is an ordinary interior/coreflection projection. Enterprise Math does not claim these general order-theoretic laws as new mathematics. `SRC-MATHLIB-CLOSURE` and `SRC-MATHLIB-FLOORDIV` already record the relevant mature structural neighborhood.

## Why preorder alone is insufficient for explicit state identity

A Galois connection can be defined on preorders, but distinct states may satisfy both \(x\le y\) and \(y\le x\). Then adjoint laws determine results only up to preorder equivalence.

Concrete counterexample: let `A={a0,a1}` and `B={b0,b1}` each carry the indiscrete preorder (every comparison is true). Define

\[
l(a_0)=b_0,\qquad l(a_1)=b_1,
\]

and

\[
u(b_0)=a_1,\qquad u(b_1)=a_0.
\]

This is a valid Galois connection because both sides of every adjunction comparison are true. But

\[
(l\circ u)(b_0)=b_1,
\qquad
(l\circ u)(b_1)=b_0,
\]

so equality-level idempotence fails:

\[
C(C(b_0))=b_0\ne b_1=C(b_0).
\]

Therefore the minimal equality-faithful choice is either:

1. a partial order directly; or
2. a preorder followed by quotient under
   \[
   x\sim y\iff x\le y\land y\le x.
   \]

## Lattices are not necessary

Take the three-element poset `0<a`, `0<b`, with `a` and `b` incomparable and no common upper bound. It is not a lattice, yet

\[
\operatorname{id}\dashv\operatorname{id}
\]

and its induced collapse is the identity.

Hence lattice operations are genuinely unnecessary for the abstract v0.1 adjoint-collapse pattern.

## Minimal package

For current equality-faithful v0.1 operations, the clean minimal package is:

1. partial orders `A,B` (or posetal reflections of preorders);
2. an order embedding \(l:A\hookrightarrow B\);
3. a greatest element in every relevant sublevel \(\{a:l(a)\le b\}\).

The right adjoint, exact recovery, and reductive idempotent projection then follow.

Future Enterprise Math operations may require richer structure. Such structure must be justified operation-by-operation rather than retroactively assumed at the foundation.
