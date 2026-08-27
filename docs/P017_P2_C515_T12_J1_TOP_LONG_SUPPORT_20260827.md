# P017 — c=103/20 j=1 Residual Triple Top-Block Long-Support Compression

Status: `PROVED_WIP EXPLICIT TOP-BLOCK SUPPORT DENSITY / SUPPORT-SENSITIVE CAUCHY INPUT / NOT FULL REMAINDER CONSTANT / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_VALUATION_LADDER_20260827.md`;
- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_CANONICAL_BN_FACTORIZATION_20260827.md`.

Purpose: prove a finite density bound for the canonical long coefficient support of the only large residual valuation shell `nu_r=1` in the top c515 geometric block.

---

## 1. Top long block

Put

\[
B=W^{31/36}=x^{31/72}.
\]

Use the ratio-`6/5` top block

\[
\boxed{
\frac56B<M\le B.
}
\tag{L1}

A canonical `j=1` long modulus has the form

\[
\boxed{m=rqp\,b_1,}
\tag{L2}

where

\[
z\le r<q<p,
\]

and `b_1` is the long hard part of the P(23)-stripped Rosser modulus.

At the corrected residual level the hard Rosser depth is at most four, while the canonical short suffix contains at least one hard prime whenever the full hard modulus is nontrivial of maximal depth. For a safe support envelope it is enough to allow `b_1` to be any squarefree product of at most three primes from

\[
29\le\ell\le1439.
\]

This is a superset of the actual canonical long support.

---

## 2. Bound the small hard reciprocal mass

Let

\[
S_h=\sum_{\substack{29\le\ell\le1439\\\ell\ {m prime}}}\frac1\ell.
\]

The checker upper-encloses every reciprocal with common denominator `10^12` and proves

\[
\boxed{S_h<\frac34.}
\tag{L3}

Therefore the reciprocal mass of all squarefree hard products of depth at most three is bounded by the repeated-prime majorant

\[
\begin{aligned}
C_h
&\le
1+S_h+\frac{S_h^2}{2}+\frac{S_h^3}{6}\\
&<
1+\frac34+\frac{(3/4)^2}{2}+\frac{(3/4)^3}{6}\\
&=
\boxed{\frac{269}{128}.}
\end{aligned}
\tag{L4}

---

## 3. Large-prime pair reciprocal mass

A modulus in (L1) has `m<=B`. Since `p>q`, necessarily

\[
rq^2<B.
\]

Also `r>=z`, and the exact Tier-A cutoff gives the first possible prime

\[
r\ge1447.
\]

Define

\[
R_B
=
\sum_{\substack{1447\le r<q\\r,q\ {m prime}\\rq^2<B}}
\frac1{rq}.
\]

Using the exact integer value

\[
\lfloor B\rfloor=494793856728459,
\]

the checker enumerates the ordinary primes needed only up to `584760`, upper-encloses each reciprocal by a `10^12` fixed-point integer, and proves

\[
\boxed{R_B<\frac{27}{200}.}
\tag{L5}

No prime-number theorem is used in (L5).

---

## 4. Brun–Titchmarsh on the largest external prime

Fix `b_1,r,q`. Put

\[
X_1=\frac{(5/6)B}{b_1rq}.
\]

For (L2) to lie in the top block, `p` lies in

\[
X_1<p\le\frac65X_1.
\]

The interval length is `X_1/5`.

If it contains an admissible prime `p>q`, then

\[
\frac65X_1>q
\]

and hence

\[
\frac{X_1}{5}>\frac q6\ge\frac{1447}{6}.
\]

The elementary bound `e<11/4` implies

\[
e^5<\left(\frac{11}{4}\right)^5<\frac{1447}{6},
\]

so

\[
\log(X_1/5)>5.
\]

Brun–Titchmarsh therefore gives

\[
\#\left\{p:X_1<p\le\frac65X_1\right\}
\le
\frac{2(X_1/5)}{\log(X_1/5)}
<
\boxed{\frac{2}{25}X_1.}
\tag{L6}

Dropping the source upper endpoint and other ordering restrictions only enlarges the count.

---

## 5. Final top-block support density

Let `A_M` be the number of canonical `j=1` long coefficient states in the top block. Summing (L6) over the support envelope for `b_1,r,q` gives

\[
\frac{A_M}{(5/6)B}
<
\frac{2}{25} C_h R_B.
\]

Using (L4),(L5),

\[
\boxed{
\frac{A_M}{(5/6)B}
<
\frac{2}{25}\frac{269}{128}\frac{27}{200}
=
\frac{7263}{320000}
<0.0227.
}
\tag{L7}

Thus fewer than 2.27 percent of the complete top long block need be retained in the outer Cauchy support, before any cancellation is used.

This bound is intentionally conservative: it ignores the Rosser activation condition, the exact canonical-suffix ordering, the upper source endpoint for `p`, and the fact that not every hard `b_1` has depth three.

---

## 6. Short-side companion fact

At the corrected `j=1` level every hard sieve prime is below `z<1447`. The canonical short factor contains at most two hard primes and is bounded by

\[
N_0=\lfloor W^{1/4}\rfloor=18455.
\]

There are exactly

\[
1+219+895=1115
\]

possible short hard integers globally: identity, 219 single primes `29..1439`, and 895 two-prime products at most `18455`.

In the top ratio-`6/5` short block

\[
\frac56N_0<N\le N_0,
\]

exact enumeration leaves only

\[
\boxed{185}
\tag{L8}

short states.

This is the finite short support to use in the next support-sensitive Cauchy replay.

---

## 7. Next

Replay the explicit reciprocal/Cauchy estimate on the corrected `j=1` top block with

\[
A_M/M<7263/320000,
\qquad B_N=185,
\]

rather than the old generic factorable support. Use exact `hn`-diagonal multiplicity for the 185-state short set and optimize the Fourier cutoff for the full-basin `theta=1/2` normalization.

No full residual-remainder bound, finite P2 theorem or all-K claim is made here.
