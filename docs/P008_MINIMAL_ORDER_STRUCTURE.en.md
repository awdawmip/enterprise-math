# P008 Minimality Closure — Weakest order structure needed by the v0.1 core

Status: `PROVED STRUCTURAL RESOLUTION`  
Parent: `P008`

## 1. Question

P008 asks for the minimal algebraic/order structure that supports the v0.1 root/collapse core without importing continuum assumptions.

The earlier P008 work identified Galois connections as the correct mature language. This note sharpens that answer into necessity/sufficiency statements and separates three levels that should not be conflated:

1. inequality-level adjunction;
2. equality-faithful collapse on distinct states;
3. exact recovery of left-generated states.

No lattice, complete lattice, field, topology, or real-number completion is required.

## 2. Principal sublevel sets

Let \(A,B\) be partially ordered sets and let

\[
l:A\to B.
\]

For \(b\in B\), define the principal sublevel

\[
L_b=\{a\in A:l(a)\le b\}.
\]

A right adjoint to \(l\) is a map

\[
u:B\to A
\]

such that

\[
\boxed{l(a)\le b\iff a\le u(b).}
\]

## 3. P008-M01 — Right adjoints are exactly greatest-sublevel selectors

Status: `PROVED`

A map \(u:B\to A\) is right adjoint to \(l\) if and only if, for every \(b\in B\), \(u(b)\) is the greatest element of \(L_b\).

### Necessity

Assume

\[
l(a)\le b\iff a\le u(b).
\]

Taking \(a=u(b)\) gives

\[
l(u(b))\le b,
\]

so \(u(b)\in L_b\).

If \(a\in L_b\), then \(l(a)\le b\), hence

\[
a\le u(b).
\]

Therefore \(u(b)\) is greatest in \(L_b\).

### Sufficiency

Conversely, suppose every \(L_b\) has greatest element \(u(b)\). Then

\[
l(a)\le b
\]

means exactly \(a\in L_b\), which holds exactly when

\[
a\le u(b).
\]

Thus \(l\dashv u\). ∎

### Consequence

The `max` construction used in Enterprise Math is not an implementation trick. It is precisely the order-theoretic content of a right adjoint.

No arbitrary suprema are required. Only these specific sublevel maxima are needed.

## 4. Roots and quotients are instances

### Integer roots

Take

\[
l(k)=k^p
\qquad(p\ge1).
\]

For every \(n\in\mathbb N\),

\[
L_n=\{k:k^p\le n\}
\]

has greatest element \(R_p(n)\). Hence

\[
k^p\le n
\iff
k\le R_p(n).
\]

### Integer quotient

Take

\[
l(q)=dq
\qquad(d\ge1).
\]

For every \(n\),

\[
L_n=\{q:dq\le n\}
\]

has greatest element \(Q_d(n)=n//d\). Hence

\[
dq\le n
\iff
q\le Q_d(n).
\]

So root and quotient require the same minimal sublevel-maximum structure.

## 5. P008-M02 — The induced same-space projection is an interior operator

Status: `PROVED`

Let

\[
l\dashv u
\]

between partial orders and define

\[
C=l\circ u:B\to B.
\]

Then:

### Reductive

\[
C(b)\le b.
\]

### Monotone

\[
b_1\le b_2
\implies
C(b_1)\le C(b_2).
\]

### Idempotent

\[
\boxed{C(C(b))=C(b).}
\]

### Fixed points

\[
\boxed{C(b)=b\iff b\in\operatorname{im}(l).}
\]

These are standard consequences of a Galois connection on partial orders and are already represented by mathlib APIs.

Thus the project does not need a new abstract “collapse algebra.”

## 6. P008-M03 — Exact left-state recovery is equivalent to order embedding

Status: `PROVED`

Assume \(A,B\) are partial orders and

\[
l\dashv u.
\]

Then the following are equivalent:

1. \(u(l(a))=a\) for every \(a\in A\);
2. \(l\) reflects order:

\[
l(a)\le l(a')\implies a\le a';
\]

3. since every left adjoint is monotone, \(l\) is an order embedding onto its image.

### Proof: embedding implies recovery

Adjunction always gives

\[
a\le u(l(a)).
\]

It also gives

\[
l(u(l(a)))\le l(a).
\]

If \(l\) reflects order, then

\[
u(l(a))\le a.
\]

Hence equality.

### Proof: recovery implies order reflection

If

\[
l(a)\le l(a'),
\]

adjunction gives

\[
a\le u(l(a'))=a'.
\]

Thus \(l\) reflects order. ∎

### Enterprise Math consequence

The laws

\[
R_p(k^p)=k
\]

and

\[
Q_d(dq)=q
\]

are not separate coincidences. They follow because positive power formation and positive multiplication are order embeddings.

## 7. Why preorder alone is not enough for equality-faithful state semantics

A Galois connection can be defined between preorders. For inequality reasoning this is sufficient.

But in a preorder, distinct states may satisfy

\[
x\le y
\quad\text{and}\quad
y\le x
\]

without being equal.

Therefore standard adjoint laws can determine results only up to preorder equivalence.

If Enterprise Math treats distinct explicit states as genuinely distinct, equality-level collapse semantics needs antisymmetry, or it must quotient by preorder equivalence first.

## 8. P008-C01 — A preorder Galois connection whose induced collapse is not equality-idempotent

Status: `COUNTEREXAMPLE`

Let

\[
A=\{a_0,a_1\},
\qquad
B=\{b_0,b_1\},
\]

and give both sets the indiscrete preorder: every element is \(\le\) every element.

Define

\[
l(a_0)=b_0,
\qquad
l(a_1)=b_1,
\]

and

\[
u(b_0)=a_1,
\qquad
u(b_1)=a_0.
\]

Because every comparison in both preorders is true,

\[
l(a)\le b\iff a\le u(b)
\]

holds for all \(a,b\). So \(l\dashv u\) is a valid Galois connection.

But the induced map

\[
C=l\circ u
\]

satisfies

\[
C(b_0)=b_1,
\qquad
C(b_1)=b_0.
\]

Hence

\[
C(C(b_0))=b_0\ne b_1=C(b_0).
\]

So equality-level idempotence fails even though all the involved states are preorder-equivalent.

This demonstrates exactly why partial-order antisymmetry matters if explicit state identity is part of the semantics.

### Quotient repair

If each preorder is quotiented by

\[
x\sim y\iff x\le y\land y\le x,
\]

then the two-element indiscrete preorder collapses to one partial-order state and the equality ambiguity disappears.

Thus the minimal choice is:

- partial orders directly; or
- preorders followed by explicit quotient to their posetal reflection.

## 9. Lattice structure is not necessary

### P008-C02 — A non-lattice poset can already support the adjoint/collapse core

Status: `COUNTEREXAMPLE TO OVER-STRONG ASSUMPTIONS`

Let

\[
P=\{0,a,b\}
\]

with

\[
0<a,
\qquad 0<b,
\]

and \(a,b\) incomparable, with no common upper bound in \(P\).

Then \(P\) is a partial order but not a lattice because \(a\vee b\) does not exist.

Nevertheless,

\[
\operatorname{id}_P\dashv\operatorname{id}_P,
\]

and its induced projection is simply the identity, satisfying all reductive/monotone/idempotent laws.

Therefore lattice operations are not required by the abstract adjoint-collapse core.

A fortiori, complete-lattice structure is not required.

## 10. What is actually minimal for the v0.1 equality semantics

Within the order-adjoint route, the smallest clean equality-faithful package is:

1. partial orders \(A,B\);
2. an order embedding

\[
l:A\hookrightarrow B;
\]

3. for every \(b\in B\), the sublevel

\[
\{a:l(a)\le b\}
\]

has a greatest element.

Then define that greatest element as \(u(b)\). Automatically:

\[
l\dashv u,
\]

\[
u\circ l=\operatorname{id}_A,
\]

and

\[
C=l\circ u
\]

is a monotone reductive idempotent projection with fixed set exactly \(\operatorname{im}(l)\).

No join, meet, arbitrary supremum, arbitrary infimum, addition, multiplication, field structure, topology, metric, or continuum completion is required at this abstract level.

## 11. Why this package is not claimed as new mathematics

Every component above is established order theory:

- Galois connections;
- order embeddings;
- greatest elements of principal sublevels;
- interior operators / coreflections;
- posetal reflection of preorders.

P008's contribution is **structural reduction**: identifying which established structure the v0.1 operations actually require and explicitly refusing stronger assumptions that do no work.

## 12. P008 resolution status

The literal P008 question can now be marked structurally resolved for the current v0.1 root/division/collapse family:

- preorder is sufficient for adjunction only up to equivalence;
- partial order is the minimal direct choice for equality-faithful distinct states;
- exact recovery of generated states requires the left map to be an order embedding;
- existence of the right adjoint requires exactly the relevant sublevel maxima;
- lattices and completeness are unnecessary.

Future operations may require richer structure. Such additions should be justified operation-by-operation rather than retroactively inflating the v0.1 foundation.
