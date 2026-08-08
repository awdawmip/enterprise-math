# Legendre Pressure Test — Supplement 08

Status: `ACTIVE RESEARCH NOTE`  
Scope: pairwise coprimality of surviving mirror triples, CRT idempotent encoding of two-sided transverse support, and bounded lift capacity.  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. From support separation to an algebraic selector

Supplement 07 proved that for a surviving mirror radius

\[
1\le r\le k-1,
\qquad
M=k(k+1),
\]

the transverse small-prime supports of

\[
M-r,\qquad M+r
\]

are disjoint.

That statement can be strengthened and compressed algebraically. The Chinese remainder theorem and the standard correspondence between square-free factor partitions, square roots of one, and idempotents modulo a product are classical mathematics. The project does **not** claim those facts as new.

The pressure-test specialization is the additional requirement that the CRT sign pattern must possess an actual representative

\[
1\le r<k
\]

tied to the common square-basin center \(M=k(k+1)\).

## 2. L030 — A surviving mirror triple is pairwise coprime

Status: `PROVED`

Assume

\[
\gcd(r,A_k)=1,
\]

so the mirror pair survives the anchor sieve.

Every prime divisor of \(\gcd(M,r)\) is at most \(r\le k-1\). Since it also divides \(M\), it is one of the small anchor primes and therefore divides \(A_k\). This contradicts \(\gcd(r,A_k)=1\). Hence

\[
\gcd(M,r)=1.
\]

Because \(2\mid A_k\), every surviving radius \(r\) is odd, while \(M=k(k+1)\) is even. Thus both \(M-r\) and \(M+r\) are odd.

Now

\[
\gcd(M,M\pm r)=\gcd(M,r)=1.
\]

If an odd divisor \(d\) divided both \(M-r\) and \(M+r\), it would divide both \(2M\) and \(2r\), hence both \(M\) and \(r\), impossible.

Therefore

\[
\boxed{
\gcd(M-r,M)=
\gcd(M,M+r)=
\gcd(M-r,M+r)=1.
}
\]

So the entire triple

\[
M-r,\quad M,\quad M+r
\]

is pairwise coprime.

L027 is an immediate small-prime consequence, but L030 is stronger: **the complete prime supports of the two mirror states are disjoint, not only their transverse factors below \(k\).**

## 3. L031 — Mirror involution and CRT idempotent

Status: `PROVED`

Assume both mirror states have nonempty transverse small-prime support. Let

\[
P_-=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

and define their square-free products

\[
D_-=\prod_{p\in P_-}p,
\qquad
D_+=\prod_{p\in P_+}p,
\qquad
D=D_-D_+.
\]

By L027 the supports are disjoint. Every prime in \(D\) is transverse, so

\[
\gcd(M,D)=1,
\]

and \(D\) is odd.

Define the normalized radius

\[
u\equiv rM^{-1}\pmod D.
\]

For every \(p\mid D_-\),

\[
r\equiv M\pmod p,
\]

so

\[
u\equiv1\pmod p.
\]

For every \(p\mid D_+\),

\[
r\equiv-M\pmod p,
\]

so

\[
u\equiv-1\pmod p.
\]

Hence

\[
\boxed{u^2\equiv1\pmod D.}
\]

Because \(2\) is invertible modulo the odd integer \(D\), define

\[
e\equiv(1+u)2^{-1}\pmod D.
\]

Then

\[
\boxed{e^2\equiv e\pmod D.}
\]

More precisely,

\[
e\equiv1\pmod p\quad(p\in P_-),
\]

and

\[
e\equiv0\pmod p\quad(p\in P_+).
\]

Therefore the idempotent exactly encodes the side assignment:

\[
\boxed{
D_-=\gcd(e-1,D),
\qquad
D_+=\gcd(e,D).
}
\]

The original mirror states recover the same partition:

\[
\boxed{
D_-=\gcd(M-r,D),
\qquad
D_+=\gcd(M+r,D).
}
\]

Thus a two-sided transverse support is equivalently represented by a nontrivial Boolean idempotent in \(\mathbb Z/D\mathbb Z\).

## 4. L032 — Exact bounded idempotent lifts

Status: `PROVED`

Fix:

- the square-basin root \(k\) and center \(M=k(k+1)\);
- an odd square-free transverse modulus \(D\), so \(\gcd(M,D)=1\);
- a nontrivial idempotent \(e\pmod D\).

Define

\[
u\equiv2e-1\pmod D,
\]

so \(u^2\equiv1\pmod D\), and define the radius residue

\[
\rho\equiv Mu\pmod D,
\qquad
1\le\rho\le D-1.
\]

A radius realizes this exact side-sign pattern if and only if

\[
r\equiv\rho\pmod D.
\]

Therefore every bounded lift is

\[
\boxed{r=\rho+jD}
\]

for some integer \(j\ge0\) satisfying \(r<k\).

The unfiltered number of possible radii is exactly

\[
\boxed{
C_{D,e}(k)
=
\begin{cases}
0,&\rho\ge k,\\
1+\left\lfloor\dfrac{k-1-\rho}{D}\right\rfloor,&\rho<k.
\end{cases}
}
\]

Anchor survival may delete some of these radii, but can never add any.

In particular,

\[
\boxed{D\ge k\Longrightarrow C_{D,e}(k)\le1.}
\]

So a sufficiently large transverse support together with a fixed CRT side partition can occur at **at most one** mirror radius in the square basin.

This generalizes the earlier unique-hit phenomenon: L023 treated one large divisor/support product hitting a state; L032 treats an arbitrary two-sided sign partition of a transverse support and counts its bounded mirror lifts.

## 5. What the idempotent does and does not buy us

The idempotent is not additional information beyond the factor partition; it is a compact algebraic encoding of it. By itself, CRT does not forbid enough bounded lifts to prove Legendre.

The possible leverage is the conjunction

\[
\boxed{
\text{nontrivial idempotent}
+
\text{common center }M=k(k+1)
+
\text{bounded lift }1\le r<k
+
\text{anchor survival}.
}
\]

A hypothetical Legendre counterexample would require every surviving radius to admit a two-sided composite support and hence, after choosing the complete transverse support, a nontrivial bounded idempotent lift.

The next question is therefore a **capacity problem for bounded CRT idempotents**, not a claim that nontrivial idempotents are rare in the abstract residue ring.

## 6. Next target

Group surviving mirror radii by their combined transverse modulus \(D\) and idempotent \(e\). L032 gives the exact capacity of each `(D,e)` cell.

The next useful inequality would compare

\[
|S_k|
\]

with the total capacity of cells compatible with:

1. both sides being composite;
2. the root-factor horizon;
3. exact-support/smooth-cofactor closure from L024;
4. half-scale support restrictions from L018–L022;
5. the bounded-lift progression from L032.

If raw CRT capacity is still too large, the failure itself is informative: it identifies exactly which additional square-basin constraint must be coupled to the idempotent partition.

## 7. Executable validation

`src/enterprise_math/mirror_idempotent.py` and `tests/test_mirror_idempotent.py` verify over bounded domains that:

- surviving mirror triples are pairwise coprime;
- normalized radii square to one modulo their transverse support product;
- the associated selector is idempotent;
- gcds with `e` and `e-1` recover the upper/lower support products exactly;
- the original radius belongs to the bounded-lift progression of its observed idempotent;
- anchor filtering never increases the unfiltered lift capacity;
- when the support modulus exceeds the radius window, a fixed idempotent pattern has at most one bounded lift.

The proofs above are elementary CRT/integer arguments; finite tests validate only the executable reference implementation.
