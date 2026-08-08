# P007 — General division without hidden fractions

Status: `PROVED DESIGN RESOLUTION`  
Open problem: `P007`  
Scope: natural-number division, same-state-space projection, reversible remainder extension

## 1. The question

Enterprise Math needs a division operation that is exact in explicit discrete states and does not define an integer result as an approximation to a hidden rational number.

There are three distinct mathematical objects that are often conflated:

1. the integer quotient;
2. the same-state-space projection to a divisible state;
3. the quotient/remainder pair that preserves all information.

P007 is resolved by separating them.

Throughout, let \(d\ge1\).

## 2. Exact quotient as an order right adjoint

Define

\[
Q_d(n)
=
\max\{q\in\mathbb N:dq\le n\}.
\]

This is the ordinary integer quotient

\[
Q_d(n)=n\operatorname{//}d.
\]

Inside Enterprise Math, this inequality definition is primary. It does not require a hidden rational value \(n/d\).

### P007-T01 — Quotient characterization

Status: `PROVED`

\[
\boxed{
Q_d(n)=q
\iff
dq\le n<d(q+1).
}
\]

This is the exact division analogue of T001 for integer roots.

## 3. Multiplication / quotient adjunction

Define

\[
M_d(q)=dq.
\]

### P007-T02 — Multiplication is left adjoint to quotient

Status: `PROVED`

For \(d\ge1\),

\[
\boxed{
M_d(q)\le n
\iff
q\le Q_d(n).
}
\]

Hence

\[
M_d\dashv Q_d.
\]

Also

\[
Q_d(M_d(q))=q,
\]

so multiplication and quotient form a Galois coinsertion on \(\mathbb N\).

This is the same order-theoretic pattern as

\[
P_p(k)=k^p
\dashv
R_p.
\]

Thus integer root and integer quotient are not unrelated special functions. They are two instances of the same “left map + greatest admissible right-adjoint state” construction.

## 4. Same-state-space division collapse

If division is intended as a forward transition that remains in the original state space, the quotient alone changes semantic coordinate: it returns an index \(q\), not the represented multiple \(dq\).

Define instead

\[
D_d(n)
=
M_d(Q_d(n))
=
d(n\operatorname{//}d).
\]

This is the greatest multiple of \(d\) not exceeding \(n\).

### P007-T03 — Multiple-collapse laws

Status: `PROVED`

For \(d\ge1\):

\[
D_d(n)\le n,
\]

\[
D_d(D_d(n))=D_d(n),
\]

and

\[
D_d(n)=n
\iff
d\mid n.
\]

The basin of \(dq\) is exactly

\[
\{dq,dq+1,\ldots,dq+d-1\},
\]

so every basin has cardinality \(d\).

Therefore \(D_d\) is a reductive monotone idempotent projection, directly parallel to perfect-power collapse

\[
C_p=P_p\circ R_p.
\]

## 5. Quotient composition is always path independent

### P007-T04 — Quotient composition law

Status: `PROVED`

For positive \(d,e\),

\[
\boxed{
Q_d(Q_e(n))=Q_{de}(n)=Q_e(Q_d(n)).
}
\]

Equivalently,

\[
(n\operatorname{//}e)\operatorname{//}d
=
n\operatorname{//}(de).
\]

So quotient-only division composes multiplicatively and the order of successive positive divisors does not matter.

This property belongs to the **index-changing quotient map**.

## 6. Same-state projections are not generally commutative

The same statement is false for \(D_d\).

### P007-T05 — Absorption for comparable divisors

Status: `PROVED`

If

\[
d\mid e,
\]

then

\[
D_d\circ D_e=D_e
\]

and

\[
D_e\circ D_d=D_e.
\]

Thus comparable divisors absorb to the finer divisibility constraint.

### P007-T06 — Global commutation classification

Status: `PROVED`

For positive \(d,e\),

\[
\boxed{
D_d\circ D_e=D_e\circ D_d
\text{ on all }\mathbb N
\iff
d\mid e\text{ or }e\mid d.
}
\]

### Proof of the noncomparable direction

Assume without loss of generality

\[
d<e
\]

and

\[
d\nmid e.
\]

Take the single witness

\[
n=e.
\]

Since \(e\) is already an \(e\)-multiple,

\[
D_e(e)=e,
\]

so

\[
D_d(D_e(e))=D_d(e)>0.
\]

Because \(d\nmid e\),

\[
D_d(e)<e.
\]

Hence

\[
D_e(D_d(e))=0.
\]

Therefore the two compositions differ.

This is the exact divisibility analogue of the perfect-power collapse commutation phenomenon studied in P003.

## 7. The remainder is a derived comparison, not an implicit hidden state

Define the division gap

\[
E_d(n)
=
n-D_d(n).
\]

### P007-T07 — Exact remainder relation

Status: `PROVED`

\[
0\le E_d(n)<d,
\]

and

\[
\boxed{
n=dQ_d(n)+E_d(n).}
\]

This is ordinary Euclidean division.

Enterprise Math does **not** deny this identity. The semantic distinction is different:

- if the active state transition is \(n\mapsto Q_d(n)\) or \(n\mapsto D_d(n)\), the quantity \(E_d(n)\) is a derived relation to the previous state;
- it is not automatically assumed to survive as an additional hidden post-transition state variable.

That is the same distinction already made for the collapse gap \(n-C_p(n)\).

## 8. Explicit reversible extension

If an application explicitly needs lossless reconstruction, define the extended Euclidean state

\[
\mathcal E_d(n)
=
(Q_d(n),E_d(n)).
\]

The allowed state space is

\[
\mathbb N\times\{0,1,\ldots,d-1\}.
\]

### P007-T08 — Quotient/remainder encoding is reversible

Status: `PROVED`

The map

\[
n\mapsto(Q_d(n),E_d(n))
\]

is a bijection between \(\mathbb N\) and

\[
\{(q,r)\in\mathbb N^2:0\le r<d\},
\]

with inverse

\[
(q,r)\mapsto dq+r.
\]

Therefore quotient-with-remainder is an **information-preserving encoding**, not a many-to-one collapse.

This distinction is essential. Adding a remainder coordinate changes the state model rather than merely “making division more exact.”

## 9. Three division semantics

P007 therefore distinguishes three legitimate operations.

### A. Quotient-only arithmetic

\[
Q_d(n)=n//d.
\]

Use when the result is an exact quotient/index state.

Properties:

- exact integer result;
- right adjoint to multiplication;
- many-to-one;
- composition \(Q_dQ_e=Q_{de}\).

### B. Same-state-space multiple collapse

\[
D_d(n)=d(n//d).
\]

Use when the forward state should remain in the original numerical coordinate and project to the nearest admissible lower multiple.

Properties:

- contractive, monotone, idempotent;
- fixed points are multiples of \(d\);
- structurally parallel to \(C_p\);
- projections commute globally exactly for divisibility-comparable divisors.

### C. Explicit reversible Euclidean state

\[
(Q_d(n),E_d(n)).
\]

Use when the model explicitly requires all pre-transition information to remain represented.

Properties:

- lossless;
- not a collapse;
- enlarges the state space.

No one of these should be silently substituted for another.

## 10. Zero divisor and signed division

The current minimal natural-state division requires

\[
d\ge1.
\]

Division by zero is undefined; Enterprise Math does not manufacture a sentinel hidden value.

Signed division should be layered on top of the explicit signed-state choices in P006. In particular, ordinary floor division, truncation toward zero, and sign-magnitude quotient are different operations on negative inputs and should not be conflated.

## 11. P007 resolution

The smallest division structure compatible with the v0.1 philosophy is not a new number field. It is the existing order-adjoint quotient

\[
M_d\dashv Q_d
\]

plus an explicit choice of state semantics:

- use \(Q_d\) for exact quotient states;
- use \(D_d=M_dQ_d\) for same-space many-to-one projection;
- add \(E_d\) to the represented state only when reversible Euclidean information preservation is intentionally required.

This resolves division without treating an unrepresented rational number as the hidden true answer.

## 12. Prior-art discipline

Euclidean division, floor division, quotient/remainder reconstruction, and the Galois-adjoint formulation of floor division are established mathematics. `SRC-MATHLIB-FLOORDIV` already records the relevant formal prior-art neighbor.

Enterprise Math does not claim invention of these ingredients. The project-specific role is to place quotient, multiple-collapse, root, and perfect-power collapse inside one explicit state-semantics framework and to distinguish information-losing transitions from reversible state enlargement.
