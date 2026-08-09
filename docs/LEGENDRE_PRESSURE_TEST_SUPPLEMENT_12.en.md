# Legendre Pressure Test — Supplement 12

Status: `ACTIVE RESEARCH NOTE`  
Scope: CRT/idempotent encoding of two-sided mirror support and bounded sign-pattern capacity  
Depends on: P017 L042–L045 and the surviving-mirror pairwise-coprime corollary  
Discipline: **this note does not prove Legendre's conjecture.** The Chinese remainder theorem, square roots of one modulo square-free products, and idempotents are classical algebra. The project-specific content is only the bounded-radius specialization tied to the common square-basin center.

## 1. Why use an idempotent at all?

For an anchor-surviving radius

\[
1\le r<k,
\qquad M=k(k+1),
\]

L043 gives disjoint transverse supports on the two mirror states. If both supports are nonempty, write

\[
P_-=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

with square-free products

\[
D_-=\prod_{p\in P_-}p,
\qquad
D_+=\prod_{p\in P_+}p,
\qquad
D=D_-D_+.
\]

The CRT does not add information to this partition. Its value is that the whole two-sided sign assignment can be stored in one residue class and its possible radii can then be counted exactly inside the finite window \(1\le r<k\).

---

## 2. L046 — Mirror support partition becomes a CRT idempotent

Status: `PROVED / CLASSICAL CRT SPECIALIZATION`.

Because every prime dividing \(D\) is transverse,

\[
\gcd(M,D)=1,
\]

and \(D\) is odd. Define

\[
u\equiv rM^{-1}\pmod D.
\]

For \(p\mid D_-\), the relation \(p\mid M-r\) gives

\[
u\equiv1\pmod p.
\]

For \(p\mid D_+\), the relation \(p\mid M+r\) gives

\[
u\equiv-1\pmod p.
\]

Therefore

\[
\boxed{u^2\equiv1\pmod D.}
\]

Since \(2\) is invertible modulo the odd integer \(D\), put

\[
e\equiv(1+u)2^{-1}\pmod D.
\]

Then

\[
\boxed{e^2\equiv e\pmod D.}
\]

Moreover

\[
e\equiv1\pmod p\quad(p\in P_-),
\qquad
 e\equiv0\pmod p\quad(p\in P_+),
\]

so the side partition is recovered exactly by

\[
\boxed{
D_-=\gcd(e-1,D),
\qquad
D_+=\gcd(e,D).
}
\]

Because both sides are nonempty, \(e\) is a nontrivial idempotent modulo \(D\).

This is classical CRT/idempotent algebra specialized to the centered mirror data; no novelty is claimed for the algebraic correspondence itself.

---

## 3. L047 — Exact bounded lifts of a fixed sign pattern

Status: `PROVED`.

Now reverse the viewpoint. Fix:

- the square-basin root \(k\) and center \(M=k(k+1)\);
- an odd square-free transverse modulus \(D\), so \(\gcd(M,D)=1\);
- a nontrivial idempotent \(e\pmod D\).

Set

\[
u\equiv2e-1\pmod D,
\]

so \(u^2\equiv1\pmod D\), and define

\[
\rho\equiv Mu\pmod D,
\qquad 1\le\rho\le D-1.
\]

A radius realizes this fixed CRT side-sign pattern if and only if

\[
\boxed{r\equiv\rho\pmod D.}
\]

Hence every positive bounded lift is

\[
\boxed{r=\rho+jD}
\]

with \(j\ge0\) and \(r<k\). The unfiltered sign-pattern capacity is therefore

\[
\boxed{
C^{\mathrm{sign}}_{D,e}(k)
=
\begin{cases}
0,&\rho\ge k,\\
1+\left\lfloor\dfrac{k-1-\rho}{D}\right\rfloor,&\rho<k.
\end{cases}
}
\]

Filtering by \(\gcd(r,A_k)=1\) can only decrease this count.

In particular,

\[
\boxed{D\ge k\Longrightarrow C^{\mathrm{sign}}_{D,e}(k)\le1.}
\]

Thus a fixed sufficiently large side-sign pattern can occur at at most one bounded mirror radius.

---

## 4. L048 — Exact-support capacity is bounded by sign-pattern capacity, not equal to it

Status: `PROVED`.

Suppose \(D\) is intended to be the **complete** combined transverse support of a mirror pair, with side assignment encoded by \(e\).

Every exact-support realization must satisfy the congruence of L047. Therefore

\[
\boxed{
C^{\mathrm{exact}}_{D,e}(k)
\le
C^{\mathrm{anchor}}_{D,e}(k)
\le
C^{\mathrm{sign}}_{D,e}(k),
}
\]

where the middle term counts sign-pattern lifts that also survive the anchor sieve.

The first inequality can be strict because a bounded lift may satisfy all prescribed congruences modulo \(D\) while acquiring an additional transverse prime not contained in \(D\).

### Strict example

Take

\[
k=46,
\qquad M=46\cdot47=2162.
\]

At radius \(r=7\), the transverse supports are

\[
P_-=\{5\},
\qquad
P_+=\{3\}.
\]

Thus

\[
D=15,
\qquad e=6\pmod{15}.
\]

The corresponding anchor-surviving bounded sign-pattern lifts are

\[
\boxed{r=7,37.}
\]

At \(r=7\), the prescribed combined transverse support is exactly \(\{3,5\}\).

At \(r=37\), the lower state is

\[
M-r=2125=5^3\cdot17,
\]

so the same sign pattern modulo \(15\) has acquired the additional transverse prime \(17\). Hence \(r=37\) is not an exact-support realization of \(D=15\).

Therefore in this example

\[
C^{\mathrm{exact}}_{15,6}(46)=1
<
C^{\mathrm{anchor}}_{15,6}(46)=2.
\]

This explicitly corrects the tempting but false interpretation that a CRT sign-pattern progression already classifies complete support cells.

---

## 5. Relation to L041 and the mirror route

The three layers now have distinct jobs:

\[
\boxed{
\text{L041: support closure after one large-modulus hit}
}
\]

\[
\boxed{
\text{L042--L045: cross-state mirror support separation}
}
\]

\[
\boxed{
\text{L046--L048: bounded CRT sign-pattern capacity}
}
\]

The CRT layer is useful only if it reduces a later capacity argument. It should not replace the original support sets in proofs that need exact prime content, because sign-pattern lifts are a superset of exact-support realizations.

The next meaningful question is whether the sum of these **upper capacities**, after imposing anchor survival and exact-support/smooth-closure filters, becomes smaller than the number of mirror pairs that a hypothetical prime-free basin would need to cover.

If it does not, the CRT route should be demoted to a coordinate tool rather than expanded further.

---

## 6. Executable validation

`src/enterprise_math/p017_mirror_crt.py` and `tests/test_p017_mirror_crt.py` check that:

- observed two-sided mirror supports produce a square root of one and a nontrivial idempotent;
- gcds with \(e\) and \(e-1\) recover the two support products;
- every bounded sign-pattern realization lies in one arithmetic progression modulo \(D\);
- anchor filtering never increases capacity;
- exact-support lifts are a subset of anchor-surviving sign-pattern lifts;
- the \((k,D,e)=(46,15,6)\) example makes the first inclusion strict;
- when \(D\ge k\), a fixed sign pattern has at most one bounded lift.

Finite tests audit the reference implementation; the CRT facts and counting formulas are proved above.
