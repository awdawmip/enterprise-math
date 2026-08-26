# P017 — Prime-Lift Factorization Support Map

Status: `PROVED_WIP SOURCE-MAPPING + SCOPE CORRECTION / DIRECT-A_p ROUTE ONLY / NOT FULL W1 ERROR / NOT CANONICAL`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Sources:

- Iwaniec–Laborde, *P2 in short intervals* (1981), Lemma 2, Section 6 and the p.53 W1 formula;
- Iwaniec, *A new form of the error term in the linear sieve* (1980).

Purpose: record the exact algebra of applying the factorable linear-sieve remainder **directly to a prime-lift sequence `A_p`**, while preventing that direct application from being mistaken for an exhaustive description of the original Chen/Iwaniec W1 bilinear routing.

---

## 1. External prime in a direct sieve of A_p

Let `A_q` denote the subsequence supported on multiples of squarefree `q`. For a sieve modulus `d`, write the natural dimension-one remainder as

\[
r(A_q;d)=|A_{[q,d]}|-\frac{X}{[q,d]}.
\]

If `(q,d)=1`, then

\[
\boxed{r(A_q;d)=r(A;qd).}
\tag{PL1}
\]

In particular, for an odd prime `p` at or above the direct sifting cutoff and

\[
d=mn,\qquad mn\mid P(u),
\]

one has `(p,mn)=1` and hence

\[
\boxed{r(A_p;mn)=r(A;pmn).}
\tag{PL2}
\]

If Iwaniec's factorable linear-sieve theorem is applied **to `A_p` as the sequence being sifted**, its remainder has the form

\[
\boxed{
R_{\rm direct}(A_p;M,N)
=
\sum_{m<M,\,m\mid P(u)}
\sum_{n<N,\,n\mid P(u)}
 a_m b_n\,r(A;pmn),
}
\tag{PL3}
\]

with `|a_m|,|b_n|<=1` and squarefree `m,n`.

Thus, in this direct-`A_p` representation, the external prime does not get absorbed into either smooth factorable variable. The smooth/squarefree support used in the support-sensitive Cauchy theorem survives.

---

## 2. Direct-A_p sieve level

If the direct `A_p` application is assigned total physical modulus level `D`, choose

\[
MN=\frac Dp.
\]

Then

\[
pMN=D,
\]

and the direct linear-sieve parameter is

\[
s=\frac{\log(MN)}{\log u}
=
\frac{\log(D/p)}{\log u}.
\tag{PL4}
\]

Writing

\[
p=D^t,
\]

gives the familiar source expressions:

### Fixed cutoff `u=z=D^(1/a)`

\[
\boxed{s_z=a(1-t)=a-at.}
\tag{PL5}
\]

### Moving cutoff `u=p`

\[
\boxed{s_p=\frac{1-t}{t}.}
\tag{PL6}
\]

These identities explain the sieve-function arguments `F(a-at)` and `F((1-t)/t)` that occur in the source W1 main-term calculation. They do not, by themselves, determine how every W1 remainder is grouped analytically.

---

## 3. Legality boundaries for the direct-A_p factorable theorem

The 1980/1981 factorable theorem in the form used here assumes

\[
u\le\sqrt{MN},
\]

i.e.

\[
s\ge2.
\]

For the live a6 packet `a=6` this gives, **for this direct-A_p application**:

### Fixed cutoff z

\[
6(1-t)\ge2
\Longrightarrow
\boxed{t\le\frac23},
\]

or

\[
\boxed{p\le D^{2/3}=X^{10/27}.}
\tag{PL7}
\]

### Moving cutoff p

\[
\frac{1-t}{t}\ge2
\Longrightarrow
\boxed{t\le\frac13},
\]

or

\[
\boxed{p\le D^{1/3}=X^{5/27}=z^2.}
\tag{PL8}
\]

The appearance of `z^2` is genuinely aligned with the separate a6 collision-core scale, but the two facts have different proofs and roles.

---

## 4. Critical scope correction

Equations (PL7) and (PL8) are **not** an exhaustive partition of the source W1 remainder.

The original Chen/Iwaniec–Laborde treatment is free to group the external prime together with another summation variable before invoking the bilinear remainder estimate. In that representation `p` itself participates in a physical bilinear block rather than merely remaining a fixed external parameter of an independently sifted `A_p`.

Source Section 6 explicitly distinguishes the ranges in which Lemma 3/Lemma 4 can be consumed after such regrouping; this is stronger than the direct-`A_p` legality test above.

Therefore freeze:

\[
\boxed{
\text{DIRECT-}A_p\text{ LEGALITY BOUNDARY}
\ne
\text{FULL SOURCE W1 ANALYTIC BOUNDARY}.
}
\tag{PL9}
\]

The earlier wording that treated `p>D^(2/3)` or `p>D^(1/3)` as necessarily belonging to a separate high-p absolute sector is superseded.

---

## 5. Consequence for the support-sensitive Cauchy theorem

`docs/P017_P2_SUPPORT_SENSITIVE_CAUCHY_COMPRESSION_20260826.md`

remains a valid theorem for any factorable block in which the two factorable variables are explicitly supported on `P(u)`. Equation (PL3) shows one legitimate prime-lift situation where this occurs.

However, its frozen numerical top-scale values `MN=D` describe an unlifted top block. A direct prime-lift application has

\[
MN=D/p,
\]

and the original source W1 regrouping can have yet another factor split. Hence the numerical constant `0.058 y` must never be copied unchanged to the aggregate W1 remainder.

The currently preferred finite route is now the sharp-odd conventional-error route, which attempts to consume `|e(q)|<1` before any factorable decomposition. The factorable support-sensitive theorem remains a fallback for whatever residual W1 sector survives that direct treatment.

No full W1 finite error bound, finite P2 threshold, P2-in-every-square theorem or Legendre theorem is claimed here.
