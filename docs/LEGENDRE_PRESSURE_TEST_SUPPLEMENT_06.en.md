# Legendre Pressure Test — Supplement 06

Status: `ACTIVE RESEARCH NOTE`  
Scope: large transverse-support incidence and anchor-surviving smooth-cofactor closure  
Discipline: **this note does not prove Legendre's conjecture.**

Let

\[
M=k(k+1),
\qquad
I_k=M+\{1-k,\ldots,k\}.
\]

Thus \(I_k\) is exactly the open basin between \(k^2\) and \((k+1)^2\) and contains \(2k\) integer states.

For a finite set \(P\) of distinct transverse primes \(p\le k\), meaning \(p\nmid M\), write

\[
G_P=\prod_{p\in P}p.
\]

This supplement keeps only the part of the former four-support aggregation route that is independent of the missing graph-tail implementation.

## 1. L028 — Large support products have an exact zero-or-one basin incidence

Status: `PROVED`.

Assume

\[
G_P>2k.
\]

Then at most one state in \(I_k\) is divisible by \(G_P\).

Let

\[
a_P=M\bmod G_P,
\qquad 0\le a_P<G_P.
\]

A divisible state exists exactly in either of the two cases

\[
\boxed{a_P<k}
\]

or

\[
\boxed{a_P\ge G_P-k}.
\]

When it exists, its centered offset \(s_P\) is

\[
\boxed{
s_P=
\begin{cases}
-a_P,&a_P<k,\\
G_P-a_P,&a_P\ge G_P-k.
\end{cases}}
\]

and the state is

\[
n_P=M+s_P.
\]

### Proof

The allowed offsets form the interval

\[
1-k\le s\le k,
\]

which contains \(2k\) integers and has diameter \(2k-1<G_P\). Therefore two distinct allowed offsets cannot be congruent modulo \(G_P\); incidence is at most one.

The divisibility condition is

\[
a_P+s\equiv0\pmod{G_P}.
\]

The only possible representative in the negative part of the offset interval is \(-a_P\), which is admissible exactly when \(a_P<k\). The only possible positive representative is \(G_P-a_P\), admissible exactly when \(a_P\ge G_P-k\). ∎

### Half-scale cofactor

If the hit exists, write

\[
n_P=G_Ph_P.
\]

Because \(G_P\ge2k+1\) and \(n_P\le(k+1)^2-1=k^2+2k\),

\[
\boxed{h_P\le\left\lfloor\frac{k+1}{2}\right\rfloor.}
\]

So a large support-product event is determined by one residue class plus a cofactor living at half the original scale.

## 2. L029 — Exact-support closure requires anchor survival

Status: `PROVED`.

Let \(A_k\) be the product of the anchor primes \(p\le k\) dividing \(M\). Suppose L028 produces the unique hit

\[
n_P=G_Ph_P.
\]

Then among **anchor-surviving** basin states,

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(n_P)=P
\iff
h_P\text{ is }P\text{-smooth}.
}
\]

Here `P-smooth` means every prime divisor of \(h_P\) belongs to \(P\).

### Proof

The forward direction now explicitly includes anchor survival. Since

\[
h_P\le\left\lfloor\frac{k+1}{2}\right\rfloor\le k,
\]

every prime divisor \(q\mid h_P\) is a small prime. Anchor survival excludes \(q\mid A_k\), so \(q\) is transverse. Exact transverse support therefore forces \(q\in P\).

Conversely, if every prime divisor of \(h_P\) belongs to \(P\), then all prime factors of \(n_P=G_Ph_P\) belong to the transverse set \(P\). Hence \(n_P\) automatically survives the anchor sieve and its transverse support is exactly \(P\). ∎

The anchor-survival qualifier is essential. Raw transverse support alone does **not** exclude hidden anchor factors in the cofactor.

## 3. Boundary example that fixes the old overstatement

Take

\[
k=10,
\qquad M=110,
\qquad P=\{3,7\},
\qquad G_P=21>20.
\]

L028 gives the unique basin hit

\[
105=21\cdot5.
\]

The raw transverse support of 105 is indeed

\[
\{3,7\},
\]

because 5 is an anchor prime dividing \(k\). But

\[
\gcd(105,A_{10})>1,
\]

so this state is **not** anchor-surviving. Therefore the former statement “exact transverse support iff the cofactor is P-smooth” was too strong unless anchor survival was included.

A positive example is

\[
k=16,
\qquad P=\{5,11\},
\qquad G_P=55>32,
\]

with unique hit

\[
275=55\cdot5.
\]

Here the cofactor is \(P\)-smooth and the state is anchor-surviving with exact transverse support \(\{5,11\}\).

## 4. What is not promoted from the former aggregation Draft

The old Supplement-06 Draft also attempted to aggregate exact four-prime support contributions using a `four_support_square_tail` graph-tail routine. That implementation is absent even on the historical branch, so the corresponding aggregate theorem is **not canonicalized here**.

This supplement therefore promotes only the two independent, fully auditable facts:

1. large support-product incidence is exactly zero-or-one;
2. exact transverse support closes through a half-scale cofactor only after the anchor-survival condition is made explicit.

The four-support graph-tail aggregation remains a separate Draft obligation. No cancellation estimate strong enough to prove Legendre's conjecture follows from L028–L029 alone.

## 5. Executable validation

`src/enterprise_math/support_incidence.py` and `tests/test_support_incidence.py` audit:

- the residue criterion against direct basin enumeration;
- the zero-or-one incidence theorem for bounded transverse support sets;
- the half-scale cofactor bound;
- the anchor-surviving exact-support equivalence;
- the explicit `k=10, P={3,7}` anchor-contamination counterexample;
- the positive `k=16, P={5,11}` closure example.
