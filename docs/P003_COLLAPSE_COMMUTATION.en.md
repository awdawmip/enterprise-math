# P003 — Commutation of perfect-power collapse operators

Status: `PROVED`  
Open problem: `P003`  
Scope: ordinary mathematics

## 1. Question

For positive integers \(p,q\), Enterprise Math defines

\[
C_p(n)=R_p(n)^p,
\]

where \(R_p(n)\) is the greatest natural number \(k\) satisfying \(k^p\le n\).

P003 asks when

\[
C_p(C_q(n))=C_q(C_p(n))
\]

holds for every natural state \(n\).

P008 supplies the useful structural view: each \(C_p\) is the reductive monotone idempotent projection onto the set of perfect \(p\)-th powers. The result below uses that structure but is specific to the nesting of perfect-power sets.

## 2. Divisibility gives absorption

### P003-T01 — Nested-exponent absorption

Status: `PROVED`

Let \(p,q\ge1\). If \(p\mid q\), then

\[
C_p\circ C_q=C_q
\]

and

\[
C_q\circ C_p=C_q.
\]

Hence \(C_p\) and \(C_q\) commute.

### Proof

Write \(q=pr\).

Every perfect \(q\)-th power is a perfect \(p\)-th power because

\[
a^q=a^{pr}=(a^r)^p.
\]

Therefore \(C_q(n)\) is already fixed by \(C_p\), so

\[
C_p(C_q(n))=C_q(n).
\]

For the other composition, first note that \(C_q(n)\le n\) and that \(C_q(n)\) is a perfect \(p\)-th power. Since \(C_p(n)\) is the greatest perfect \(p\)-th power not exceeding \(n\),

\[
C_q(n)\le C_p(n)\le n.
\]

Apply monotonicity of \(C_q\):

\[
C_q(C_q(n))\le C_q(C_p(n))\le C_q(n).
\]

Idempotence gives \(C_q(C_q(n))=C_q(n)\), so both inequalities are equalities:

\[
C_q(C_p(n))=C_q(n).
\]

Thus both compositions equal \(C_q\). ∎

The symmetric statement holds when \(q\mid p\): both compositions equal \(C_p\).

## 3. Incomparable exponents cannot commute globally

### P003-T02 — Universal witness for noncommutation

Status: `PROVED`

Let \(1\le p<q\) and suppose \(p\nmid q\). Then at

\[
n=2^q
\]

we have

\[
C_p(C_q(n))\ne C_q(C_p(n)).
\]

### Proof

Because \(n=2^q\) is a perfect \(q\)-th power,

\[
C_q(n)=n.
\]

Because \(p\nmid q\), the integer \(2^q\) is not a perfect \(p\)-th power. Indeed, if

\[
2^q=a^p,
\]

unique prime factorization forces \(a\) to be a power of \(2\), say \(a=2^m\), and then \(q=mp\), contradicting \(p\nmid q\).

Therefore

\[
C_p(n)<n=2^q.
\]

At the same time, since \(p<q\),

\[
2^p\le2^q,
\]

so the greatest perfect \(p\)-th power below \(2^q\) satisfies

\[
C_p(n)\ge2^p>1.
\]

The only positive perfect \(q\)-th power strictly below \(2^q\) is \(1^q=1\). Hence

\[
C_q(C_p(n))=1.
\]

But

\[
C_p(C_q(n))=C_p(n)>1.
\]

Thus the two compositions differ. ∎

## 4. Complete classification

### P003-T03 — Global commutation theorem

Status: `PROVED`

For all positive integers \(p,q\), the following are equivalent:

1. \(C_p\circ C_q=C_q\circ C_p\) on all \(\mathbb N\);
2. \(p\mid q\) or \(q\mid p\).

Equivalently, two perfect-power collapse operators commute globally **if and only if their exponents are comparable in the divisibility order**.

### Proof

If \(p\mid q\) or \(q\mid p\), P003-T01 gives commutation.

Conversely, suppose neither exponent divides the other. By totality of the usual order on \(\mathbb N\), either \(p<q\) or \(q<p\). In the first case P003-T02 gives the witness \(2^q\); in the second case its symmetric version gives the witness \(2^p\). Therefore global commutation is impossible. ∎

## 5. Exact composition in the commuting case

A useful strengthening is built into the proof:

\[
p\mid q \quad\Longrightarrow\quad C_pC_q=C_qC_p=C_q,
\]

and symmetrically

\[
q\mid p \quad\Longrightarrow\quad C_pC_q=C_qC_p=C_p.
\]

Thus when two exponents are comparable, composition selects the operator with the **larger exponent in the divisibility order**, i.e. the projection onto the smaller perfect-power image.

Examples:

\[
C_2C_4=C_4C_2=C_4,
\]

while \(2\) and \(3\) are incomparable and already fail at \(n=8\):

\[
C_2(C_3(8))=4,
\qquad
C_3(C_2(8))=1.
\]

The case \(p=1\) is included automatically because \(C_1\) is the identity and \(1\) divides every positive exponent.

## 6. Structural interpretation

The family \(\{C_p:p\ge1\}\) therefore remembers the divisibility order of the exponent set:

- exponent divisibility \(p\mid q\) means the fixed-state image of \(C_q\) is contained in that of \(C_p\);
- comparable images yield absorption and commutation;
- incomparable exponents admit an explicit prime-power witness to noncommutation.

The commutation graph of the collapse family is therefore exactly the comparability graph of positive integers ordered by divisibility.

This gives P003 a complete answer without requiring any additional algebraic structure beyond the P008 order-projection framework and elementary unique factorization.

## 7. Prior-art discipline

The general facts about Galois connections, interior operators, monotonicity, idempotence, and nested projections are established mathematics already credited by P008. A targeted search during this P003 pass did not identify an exact prior statement of the perfect-power-collapse classification above, but absence from that search is **not** a historical-priority result.

Accordingly:

- the mathematical theorem is `PROVED` from the stated definitions;
- the historical novelty of this exact formulation remains `NOVELTY_UNVERIFIED`;
- no “first” or “unprecedented” claim is permitted without a dedicated prior-art review.

## 8. Immediate consequences for the roadmap

P003 is mathematically resolved by P003-T03. The result immediately suggests two independent next attacks:

1. **P004:** fixed points of an arbitrary finite collapse composition should be the intersection of the constituent perfect-power sets, hence perfect powers of the least common multiple of the exponents;
2. **P009:** repeated application of any fixed collapse word is reductive, so it cannot have a nontrivial cycle; its eventual fixed state should be controlled by the same least-common-multiple exponent.

Those claims belong to their own problems and should be proved separately rather than silently folded into P003.
