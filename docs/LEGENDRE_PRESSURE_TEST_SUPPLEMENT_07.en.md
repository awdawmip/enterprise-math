# Legendre Pressure Test — Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: binary second-factor branches, pairwise support separation, and finite prime-resource bounds in the high least-factor band  
Depends on: P017 L020–L033  
Discipline: no new sieve formalism is introduced here. The input recursion is established least-prime-factor/Buchstab machinery; the results below come from combining it with the square-basin window contraction already proved in P017.

## 1. High-band setup

Fix a square basin parameter `k` and a least shell prime `p` satisfying

\[
\boxed{p^2\ge2k.}
\]

Let

\[
W_p(k)=[A,B]
\]

be the exact cofactor window of L021 and write

\[
N=B-A+1.
\]

L030 gives

\[
\boxed{N\le p.}
\]

L032 gives

\[
\boxed{\Omega(n)\le3}
\]

for every state `n in L_p(k)`.

Thus every shell state is either

\[
pq
\]

with prime `q`, or

\[
p\ell s
\]

with primes

\[
p\le\ell\le s.
\]

The remaining question is whether these three-prime branches have further deterministic structure.

---

## 2. L034 — Every second-factor branch is one exact response bit

Status: `PROVED`.

Fix a prime

\[
\ell\ge p
\]

with

\[
\ell\le\sqrt B.
\]

The number of multiples of `ell` in `[A,B]` is

\[
M_\ell
=
\left\lfloor\frac B\ell\right\rfloor
-
\left\lfloor\frac{A-1}\ell\right\rfloor.
\]

By L029,

\[
M_\ell
=
\left\lfloor\frac N\ell\right\rfloor
+
\kappa_\ell((A-1)\bmod\ell,\ N\bmod\ell).
\]

Because

\[
N\le p\le\ell,
\]

we have

\[
\boxed{M_\ell\in\{0,1\}.}
\]

Define the residue step

\[
\boxed{
d_\ell=(-A)\bmod\ell,
\qquad
0\le d_\ell<\ell.
}
\]

Then

\[
\boxed{
M_\ell=1
\iff
d_\ell<N.
}
\]

### Proof

The least nonnegative `d` for which `A+d` is divisible by `ell` is exactly `d_ell`. Since the interval consists of

\[
A,A+1,\ldots,A+N-1,
\]

it contains a multiple of `ell` exactly when `d_ell<N`. Since its length is at most `ell`, such a multiple is unique. ∎

When the bit is `1`, the unique raw multiple is

\[
\boxed{
q_\ell=A+d_\ell
=\ell\left\lceil\frac A\ell\right\rceil.
}
\]

Put

\[
s_\ell=\frac{q_\ell}{\ell}
=\left\lceil\frac A\ell\right\rceil.
\]

Because L032 allows at most two prime factors in the cofactor `q`, this branch produces an actual three-prime shell state exactly when

\[
\boxed{
s_\ell\ge\ell
\quad\text{and}\quad
s_\ell\text{ is prime}.}
\]

Then the unique state is

\[
\boxed{
n_{p,\ell}=p\ell s_\ell.}
\]

Thus the second Buchstab layer is not another interval sieve in this band. For each candidate second prime it is:

\[
\boxed{
\text{one carry/residue bit}
+
\text{one explicit primality test}.
}
\]

---

## 3. L035 — Distinct high-band cofactor survivors are pairwise coprime

Status: `PROVED`.

Let

\[
q_1,q_2\in W_p(k)
\]

be two distinct `p`-rough survivors.

Then

\[
\boxed{\gcd(q_1,q_2)=1.}
\]

### Proof

Suppose a prime `ell` divides both. Since both integers are `p`-rough,

\[
\ell\ge p.
\]

But `ell` also divides the nonzero difference

\[
q_1-q_2.
\]

The parent window has length `N<=p`, hence

\[
0<|q_1-q_2|\le N-1\le p-1<\ell,
\]

which is impossible for a nonzero multiple of `ell`. ∎

Therefore for distinct shell states

\[
n_i=pq_i,
\]

we have

\[
\boxed{\gcd(n_1,n_2)=p.}
\]

So the least factor `p` is the **only** prime resource shared by distinct states in one high-band shell. All cofactor prime supports are disjoint across survivors.

This is stronger than the branchwise uniqueness of L031: it separates the full prime support of every surviving cofactor from every other one.

---

## 4. L036 — Finite prime-resource bound for all three-prime branches

Status: `PROVED`.

Let a three-prime high-band state be

\[
n=p\ell s,
\qquad
p\le\ell\le s,
\]

with all three factors prime.

Let

\[
U=(k+1)^2-1
\]

and define

\[
\boxed{
K_p=\left\lfloor\frac{U}{p^2}\right\rfloor.
}
\]

Since

\[
p\ell\ge p^2,
\]

we have

\[
s
\le
\frac{U}{p\ell}
\le
\frac{U}{p^2},
\]

so

\[
\boxed{p\le\ell\le s\le K_p.}
\]

Thus every prime factor beyond the common `p` in a three-prime state lies in the finite prime-resource interval

\[
[p,K_p].
\]

Let

\[
R_p
=
\#\{\text{primes }q:p\le q\le K_p\}
=
\pi(K_p)-\pi(p-1).
\]

Let `T_p` be the number of three-prime states in `L_p(k)`.

By L035, distinct cofactor survivors are pairwise coprime. Therefore two different three-prime states cannot reuse any prime in their cofactor supports.

A state of the form

\[
p\ell^2
\]

uses only one distinct cofactor prime instead of two. But at most one such square cofactor can occur in the parent window.

### Why at most one square cofactor?

If

\[
a^2<b^2
\]

are two distinct squares with

\[
a,b\ge p,
\]

then

\[
b^2-a^2
=(b-a)(a+b)
\ge2p+1.
\]

But any two values in the parent cofactor window differ by at most

\[
N-1\le p-1.
\]

Contradiction.

Hence, if `E_p` records whether a square branch occurs,

\[
E_p\in\{0,1\}.
\]

The number of distinct cofactor prime resources consumed by `T_p` three-prime states is therefore exactly

\[
2T_p-E_p.
\]

Those resources all lie in `[p,K_p]`, so

\[
2T_p-E_p\le R_p.
\]

Since `E_p<=1`,

\[
\boxed{
T_p
\le
\left\lfloor\frac{R_p+1}{2}\right\rfloor.
}
\]

This is the first shell-wide resource bound produced by the high-band contraction.

A useful combined bound is

\[
\boxed{
T_p
\le
\min\left(
N,
\left\lfloor\frac{R_p+1}{2}\right\rfloor
\right).
}
\]

The first term comes from the parent interval length; the second from disjoint prime-resource consumption.

---

## 5. What this does and does not solve

The high least-factor band now has a much sharper finite structure.

For

\[
p^2\ge2k,
\]

we have:

1. `N<=p`;
2. each second-prime branch is one binary quotient-response/residue hit;
3. every successful branch has one explicit candidate tail;
4. all distinct cofactor survivors are pairwise coprime;
5. all three-prime cofactor resources are disjoint;
6. all such resources lie in `[p,K_p]`;
7. their total number satisfies L036.

This is real compression, but it still does not control the prime cofactors in the semiprime part of the shell. A Legendre proof would need enough additional information to bound both:

- prime cofactors in the short moving windows;
- binary three-prime branches.

The next pressure test should therefore not invent another structure. It should test whether the **common endpoints `A,B` across all second-prime branch bits** impose correlations stronger than generic short-interval sieve theory.

## 6. Next target

For the high band, define

\[
b_\ell(k,p)
=
\mathbf 1[d_\ell<N],
\qquad
 d_\ell=(-A)\bmod\ell.
\]

The raw branch family is now a deterministic binary vector indexed by primes `ell>=p`.

The next question is:

> Are the bits `b_ell(k,p)` sufficiently correlated by the shared square-derived `A` and `N` to force a non-generic upper bound on the number of successful prime-tail branches?

If the answer is no, record it and stop this route. If yes, that correlation—not Buchstab recursion itself—is the potentially new P017 leverage.
