# P017 — Prime-Lift Factorization Support Map

Status: `PROVED_WIP SOURCE-MAPPING CORRECTION + EXACT EXPONENT BOUNDARIES / NOT FULL W1 ERROR / NOT CANONICAL`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Sources:

- Iwaniec–Laborde, *P2 in short intervals* (1981), Lemma 2 and the p.53 W1 formula;
- the general Iwaniec linear-sieve formulation for `S(A_q,u)` in later applications.

Purpose: determine whether the external prime in a W1 prime-lift remainder destroys the newly exploited smooth support of the factorable variables, and locate exactly where the factorable Lemma-2 representation is legal.

---

## 1. External prime remains external

Let `A_q` denote the subsequence supported on multiples of squarefree `q`. For a sieve modulus `d`, the natural remainder is

\[
r(A_q;d)=|A_{[q,d]}|-\frac{X}{[q,d]}
\]

in the dimension-one interval case.

If `(q,d)=1`, then

\[
\boxed{r(A_q;d)=r(A;qd).}
\tag{PL1}
\]

In particular, for a prime `p` at or above the sifting cutoff and for

\[
d=mn,\qquad mn\mid P(u),
\]

we have `(p,mn)=1` and hence

\[
\boxed{r(A_p;mn)=r(A;pmn).}
\tag{PL2}
\]

The source Iwaniec factorable remainder therefore has the form

\[
\boxed{
R(A_p;M,N)
=
\sum_{m<M,\,m\mid P(u)}
\sum_{n<N,\,n\mid P(u)}
 a_m b_n\,r(A;pmn),
}
\tag{PL3}
\]

with `|a_m|,|b_n|<=1` and squarefree `m,n`.

Thus the external prime does **not** get absorbed into either factorable variable. The smooth/squarefree support used in the support-sensitive Cauchy compression survives prime lift.

---

## 2. The physical level and the sieve level are different objects

If the desired total physical modulus level is `D`, choose

\[
MN=\frac Dp.
\]

Then

\[
pMN=D,
\]

so the physical modulus `pmn` remains on the same total level, while the linear-sieve parameter is

\[
s=\frac{\log(MN)}{\log u}
=
\frac{\log(D/p)}{\log u}.
\tag{PL4}
\]

This exactly explains the two sieve-function arguments displayed in the source W1 formula.

Write

\[
p=D^t.
\]

### Fixed cutoff `u=z=D^(1/a)`

Then

\[
\boxed{s_z=a(1-t)=a-at.}
\tag{PL5}
\]

### Moving cutoff `u=p`

Then

\[
\boxed{s_p=\frac{1-t}{t}.}
\tag{PL6}
\]

These are exactly the source arguments `F(a-at)` and `F((1-t)/t)` on p.53.

---

## 3. Exact factorable-Lemma-2 legality boundaries

The source factorable Lemma 2 assumes

\[
u\le\sqrt{MN},
\]

i.e.

\[
s\ge2.
\]

For the live a6 packet `a=6`:

### Fixed cutoff z

From `6(1-t)>=2`,

\[
\boxed{t\le\frac23.}
\]

Equivalently,

\[
\boxed{p\le D^{2/3}=X^{10/27}.}
\tag{PL7}
\]

### Moving cutoff p

From `(1-t)/t>=2`,

\[
\boxed{t\le\frac13.}
\]

Equivalently,

\[
\boxed{p\le D^{1/3}=X^{5/27}=z^2.}
\tag{PL8}
\]

The second boundary is exactly the same `z^2` scale already forced by the a6 distinct-prime collision-core compression.

---

## 4. Consequence for the support-sensitive Cauchy theorem

The theorem

`docs/P017_P2_SUPPORT_SENSITIVE_CAUCHY_COMPRESSION_20260826.md`

remains a valid theorem for a factorable block whose two sieve variables are supported on `P(u)`. The prime-lift map (PL3) shows that this support persists with an external prime.

However, its frozen **numerical top-scale values** `M=X^mu`, `N=X^nu`, `MN=D` describe the unlifted top level. A prime-lift block instead has

\[
MN=D/p.
\]

Therefore the numerical constant `0.058 y` may not be copied unchanged into the full W1 prime-lift sum. Each p-regime requires a p-dependent factor split and frequency replay.

Likewise, the source factorable Lemma-2 representation cannot be invoked beyond (PL7) or (PL8). The complementary high-p sectors require a different finite treatment, most naturally an absolute bound on the original bounded sieve remainder before factorable decomposition.

---

## 5. New W1 error partition

The W1 remainder problem should now be partitioned by the **sieve parameter** rather than by one global modulus level:

\[
\boxed{
\begin{array}{lll}
 u=z, & p\le D^{2/3}: & \text{factorable smooth-support Cauchy sector},\\
 u=z, & p>D^{2/3}: & \text{high-p finite absolute sector},\\
 u=p, & p\le D^{1/3}=z^2: & \text{factorable moving-cutoff sector},\\
 u=p, & p>D^{1/3}: & \text{high-p finite absolute sector}.
\end{array}
}
\]

This corrects the earlier temptation to charge the same full-level block constant uniformly to every W1 prime lift.

No full W1 finite error bound, finite P2 threshold, P2-in-every-square theorem or Legendre theorem is claimed here.
