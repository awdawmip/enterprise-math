# P008 — Minimal Order-Theoretic Framework

Status: `VERIFIED-RESEARCH`  
Open problem: `P008`  
Scope: mathematical structure only

## 1. Question

P008 asks for the weakest mature algebraic or order-theoretic structure that contains the v0.1 integer-root and collapse laws without importing a hidden continuum.

The first-stage conclusion is deliberately small:

> The v0.1 root/collapse core does not require a lattice, a complete lattice, a residuated lattice, a field, or a real-number completion. Its essential mature structure is a Galois connection between partially ordered sets. In the integer-root case the connection is a Galois coinsertion, and the induced collapse is an interior operator.

This is established order theory, not a new Enterprise Math invention. Enterprise Math's project-specific contribution is the way this structure is selected and interpreted inside the finite-state / explicit-scale framework. Relevant registered prior art includes `SRC-MATHLIB-NTHROOT`, `SRC-MATHLIB-FLOORDIV`, and `SRC-MATHLIB-CLOSURE`.

## 2. Right-adjoint notation

Let \(A,B\) be partially ordered sets and let

\[
F:A\to B.
\]

When a right adjoint exists, write it in this project note as

\[
F^\downarrow:B\to A.
\]

The defining condition is

\[
F(a)\le b\iff a\le F^\downarrow(b).
\]

The notation \(F^\downarrow\) is project notation only. The underlying concept is the standard right adjoint in a Galois connection.

For maps on \(\mathbb N\), a common concrete realization is

\[
F^\downarrow(n)=\max\{k\in\mathbb N:F(k)\le n\}.
\]

## 3. Existence on natural-number states

### P008-T01 — Sufficient existence condition

Status: `PROVED`

Let \(F:\mathbb N\to\mathbb N\) be monotone, satisfy \(F(0)=0\), and be unbounded. Then for every \(n\in\mathbb N\),

\[
F^\downarrow(n)=\max\{k:F(k)\le n\}
\]

exists and is a right adjoint of \(F\).

Proof. The set is nonempty because \(F(0)=0\le n\). Since \(F\) is unbounded, choose \(m\) with \(F(m)>n\). Monotonicity implies every \(k\ge m\) also satisfies \(F(k)>n\), so the admissible set is finite and has a maximum. If \(r\) is that maximum, monotonicity gives

\[
F(k)\le n\iff k\le r.
\]

Thus \(F(k)\le n\iff k\le F^\downarrow(n)\). ∎

This theorem is only a convenient construction principle on \(\mathbb N\). The abstract framework should assume the adjunction directly rather than unnecessarily imposing these sufficient conditions.

## 4. Universal adjunction consequences

Assume from here that \(F\dashv F^\downarrow\).

### P008-T02 — Unit and counit inequalities

Status: `PROVED`

For all \(a\in A\) and \(b\in B\),

\[
a\le F^\downarrow(F(a)),
\]

and

\[
F(F^\downarrow(b))\le b.
\]

These are immediate by applying the defining equivalence to the reflexive inequalities \(F(a)\le F(a)\) and \(F^\downarrow(b)\le F^\downarrow(b)\).

### P008-T03 — Adjoint monotonicity

Status: `PROVED`

Both \(F\) and \(F^\downarrow\) are monotone.

This is a standard consequence of a Galois connection.

## 5. General collapse operator

Define

\[
C_F=F\circ F^\downarrow:B\to B.
\]

### P008-T04 — General collapse is an interior operator

Status: `PROVED`

\(C_F\) is:

1. monotone;
2. reductive: \(C_F(b)\le b\);
3. idempotent: \(C_F(C_F(b))=C_F(b)\).

Proof. Monotonicity follows from P008-T03. Reductivity is the counit inequality from P008-T02. For idempotence, reductivity gives

\[
C_F(C_F(b))\le C_F(b).
\]

The unit inequality applied to \(F^\downarrow(b)\) gives

\[
F^\downarrow(b)\le F^\downarrow(F(F^\downarrow(b))),
\]

and applying monotone \(F\) gives the reverse inequality

\[
C_F(b)\le C_F(C_F(b)).
\]

Antisymmetry yields equality. ∎

Thus the existing perfect-power collapse \(C_p\) is not an isolated construction: it is a special case of the standard interior-operator construction induced by an order adjunction.

### P008-T05 — Fixed states are exactly the image of \(F\)

Status: `PROVED`

\[
\operatorname{Fix}(C_F)=\operatorname{im}(F).
\]

Proof. For every \(a\), P008-T02 gives both

\[
F(F^\downarrow(F(a)))\le F(a)
\]

and, after applying monotone \(F\) to \(a\le F^\downarrow(F(a))\),

\[
F(a)\le F(F^\downarrow(F(a))).
\]

Hence \(C_F(F(a))=F(a)\). Conversely, if \(C_F(b)=b\), then \(b=F(F^\downarrow(b))\), so \(b\in\operatorname{im}(F)\). ∎

This identifies a collapse as a projection onto the distinguished subposet of reachable/fixed states.

## 6. Coinsertion case

If additionally

\[
F^\downarrow\circ F=\operatorname{id}_A,
\]

then \(F\dashv F^\downarrow\) is a Galois coinsertion in standard terminology.

### P008-T06 — Strictly increasing natural maps give a coinsertion

Status: `PROVED`

If \(F:\mathbb N\to\mathbb N\) is strictly increasing and its right adjoint is defined by the greatest-admissible-state rule, then

\[
F^\downarrow(F(k))=k.
\]

Therefore \(F\dashv F^\downarrow\) is a Galois coinsertion.

For the power map

\[
P_p(k)=k^p,
\]

we obtain

\[
P_p\dashv R_p,
\qquad
R_p(P_p(k))=k,
\qquad
C_p=P_p\circ R_p.
\]

Hence the v0.1 root/collapse pair is exactly a coinsertion followed by its induced interior projection onto the perfect \(p\)-th powers.

### P008-T07 — Basin characterization in the strictly increasing case

Status: `PROVED`

For strictly increasing \(F:\mathbb N\to\mathbb N\),

\[
F^\downarrow(n)=k
\iff
F(k)\le n<F(k+1).
\]

Consequently,

\[
C_F(n)=F(k)
\iff
F(k)\le n<F(k+1).
\]

The existing perfect-power basin theorem T007 is the specialization \(F(k)=k^p\).

## 7. Floor division is the same structure

Fix an integer \(a\ge1\) and define

\[
M_a(k)=ak.
\]

Its right adjoint is ordinary flooring division

\[
D_a(n)=n\operatorname{//}a.
\]

Thus

\[
M_a\dashv D_a,
\qquad
D_a(M_a(k))=k,
\]

and the induced collapse is

\[
C_{M_a}(n)=a(n\operatorname{//}a),
\]

the largest multiple of \(a\) not exceeding \(n\).

Therefore integer root and flooring division are not merely analogous. They instantiate the same order-adjoint pattern with different lower-adjoint maps.

## 8. Composition theorem

### P008-T08 — Right adjoints compose in reverse order

Status: `PROVED`

Let

\[
F:A\to B,\qquad G:B\to C,
\]

with right adjoints \(F^\downarrow\) and \(G^\downarrow\). Then

\[
G\circ F\dashv F^\downarrow\circ G^\downarrow.
\]

Proof:

\[
G(F(a))\le c
\iff
F(a)\le G^\downarrow(c)
\iff
a\le F^\downarrow(G^\downarrow(c)).
\]

∎

This is already standard mathlib Galois-connection machinery; P008 does not claim it as new.

### Corollary P008-C01 — Integer roots compose multiplicatively in the exponent

Status: `PROVED`

For \(p,q\ge1\),

\[
R_{pq}=R_p\circ R_q=R_q\circ R_p.
\]

Reason: the power maps satisfy

\[
P_p\circ P_q=P_q\circ P_p=P_{pq},
\]

and right adjoints are unique.

This result has been promoted to T013/T014. It is Lean-checked in `EnterpriseMath.Arithmetic.IntegerRoot.root_mul` and `root_mul_comm`. The underlying composition principle is established order theory; whether the specialized `Nat.nthRoot` composition statement is useful upstream remains under audit.

## 9. Scale compatibility as an adjoint identity

Let \(M_b(k)=bk\) and \(D_b(n)=n\operatorname{//}b\). For \(b\ge1\),

\[
P_p\circ M_b=M_{b^p}\circ P_p.
\]

Both sides have right adjoints. Existing mathlib commuting-square machinery transfers this equality to

\[
D_b\circ R_p=R_p\circ D_{b^p}.
\]

### P008-T09 — Root/division interchange

Status: `PROVED`

For all \(n\in\mathbb N\), \(p\ge1\), and \(b\ge1\),

\[
R_p(n)\operatorname{//}b
=
R_p\left(n\operatorname{//}b^p\right).
\]

More precisely, the operator identity is

\[
D_bR_p=R_pD_{b^p}.
\]

This result is now T015 and is Lean-checked as `EnterpriseMath.Scale.root_div_scale`.

### Corollary P008-C02 — Existing T010 is structural

Status: `PROVED`

Using

\[
R_{p,b,s}(n)=R_p(nb^{ps}),
\]

apply P008-T09 to \(nb^{p(s+1)}\):

\[
D_bR_p(nb^{p(s+1)})
=
R_p(nb^{ps}).
\]

This is exactly the existing scale-compatibility theorem T010.

So T010 is not an isolated property of powers. It is the right-adjoint shadow of the commuting square

\[
P_pM_b=M_{b^p}P_p.
\]

The result is Lean-checked as `EnterpriseMath.Scale.scaledRoot_succ_div` and resolves P014.

## 10. Representation by fixed states

### P008-T10 — Every interior operator is a coinsertion projection

Status: `PROVED`

Let \(I:B\to B\) be monotone, reductive, and idempotent on a partial order \(B\). Let

\[
K=\operatorname{Fix}(I)
\]

with the inherited order, let \(J:K\hookrightarrow B\) be inclusion, and let \(\widehat I:B\to K\) be \(I\) with codomain restricted to its fixed points. Then

\[
J\dashv\widehat I,
\qquad
\widehat I\circ J=\operatorname{id}_K,
\qquad
J\circ\widehat I=I.
\]

Therefore the two descriptions are equivalent at this level:

- Galois coinsertion / coreflection onto a subposet;
- monotone reductive idempotent interior operator.

Again, this equivalence is established order theory. Enterprise Math reuses it rather than inventing parallel vocabulary.

## 11. Why the framework should not yet be enlarged

The following stronger structures are not required for the v0.1 laws above:

- lattice;
- complete lattice;
- residuated lattice;
- ring or field;
- topology;
- real-number completion.

They may become useful later, but adding them now would answer P008 with more structure than the current mathematics needs.

For literal equalities such as idempotence, partial orders are a clean minimal setting. In a preorder, the same arguments yield mutual inequalities and therefore equality only up to the preorder's induced equivalence relation.

## 12. Boundary counterexamples

### P008-CE01 — Monotonicity alone does not construct a global greatest-state adjoint

Let \(F(k)=0\) for all \(k\). It is monotone, but for every \(n\ge0\),

\[
\{k:F(k)\le n\}=\mathbb N
\]

has no maximum. Thus monotonicity alone does not guarantee that the concrete max formula defines a right adjoint on \(\mathbb N\).

Promoted to counterexample C011.

### P008-CE02 — Unboundedness without monotonicity does not give the adjunction law

Define

\[
F(0)=0,\quad F(1)=2,\quad F(2)=1,
\]

and \(F(k)=k\) for \(k\ge3\). The map is unbounded. For \(n=1\), the greatest \(k\) satisfying \(F(k)\le1\) is \(2\). But \(1\le2\) while \(F(1)=2\not\le1\). Hence

\[
F(k)\le n\iff k\le F^\downarrow(n)
\]

fails. Monotonicity is structurally essential to the greatest-state construction.

Promoted to counterexample C012.

## 13. First-stage answer to P008

The verified first-stage answer is:

> **A Galois connection between partial orders is sufficient for the v0.1 root/collapse core; the integer-root map is a Galois coinsertion, and its collapse is the corresponding interior/coreflection projection.**

For natural-number implementations, monotone unbounded maps with \(F(0)=0\) provide a broad constructive class whose right adjoints are greatest-admissible-state operators.

The order-theoretic mother results were found to be existing mathlib mathematics. P008 therefore reduced the required foundation rather than creating a parallel algebraic vocabulary. P008 remains `PARTIAL-RESOLUTION` only because the literal claim of *weakest possible structure for all future extensions* has not been proved.

## 14. Formal verification status

The mathlib-native Lean layer now kernel-checks:

- T001 root characterization;
- T002 exact perfect powers;
- T004 collapse contractivity;
- T005 collapse idempotence;
- T006 perfect-power fixed points;
- T010 scale compatibility;
- T012 history-merging monotonicity;
- T013 integer-root exponent composition;
- T014 iterated-root commutation;
- T015 root/division interchange;
- thin general adjoint-collapse wrappers.

The build is pinned and runs with warnings fatal. P013 and P014 are therefore resolved.

## 15. Next attacks

1. Keep `root_mul` / `root_mul_comm` only as provisional mathlib upstream candidates until a mathlib-facing API review confirms absence and usefulness.
2. Attack P003 (collapse commutation) using divisibility and the P008 projection structure, without merging P003 conceptually into P008.
3. Use the commuting-square/right-adjoint method to formulate P005 multi-base scale algebra.
4. Keep P008 open only for true minimality questions introduced by later structures; do not add heavier algebra pre-emptively.
