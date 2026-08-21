# R005-B — Wang 2026 Maximal Prime-Gap Claim Audit

Status: `EXTERNAL CLAIM REJECTED FOR CONSUMPTION / EXACT ALGEBRAIC COUNTERCHECK`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Object audited: Cheng-Ting Wang, arXiv:2605.14871v5, `On Maximal Prime Gaps`

## 1. Why this audit matters

The current v5 preprint claims the unconditional bound

\[
\boxed{g_n<\frac{13}{3}\log^2 p_n}
\]

for every consecutive prime gap, and derives Oppermann's conjecture from it.

If valid, this would immediately dominate the R005-B cubic cube-root prime-gap
barrier and settle the asymptotic full-forcing frontier far beyond current
accepted unconditional technology.

R005-B therefore does not accept or reject the claim by plausibility.  We
inspect the proof chain directly.

## 2. Exact definitions used by the paper

The paper defines

\[
B_n=\sum_{k=2}^n\frac{g_k}{k-1}.
\]

In Lemma 2.3 it then sets

\[
y_n=B_n-B_{n-1}.
\]

Therefore, identically,

\[
\boxed{y_n=\frac{g_n}{n-1}.}
\]

The correct telescoping identity is consequently

\[
\boxed{
\sum_{k=3}^n y_k=B_n-B_2.
}
\]

## 3. Exact proof-chain break in Lemma 2.3

The current v5 proof instead states

\[
\boxed{
\sum_{k=3}^n\frac{k}{k-1}y_k=B_n-B_2.
}
\]

This is false.  Since

\[
\frac{k}{k-1}y_k
=
\frac{k}{k-1}\frac{g_k}{k-1},
\]

the extra factor \(k/(k-1)\) does not telescope.

The difference from the correct sum is

\[
\sum_{k=3}^n\left(\frac{k}{k-1}-1\right)y_k
=
\sum_{k=3}^n\frac{y_k}{k-1},
\]

which is strictly positive for prime gaps.

### Minimal exact counterexample

Take n=3.  Then

\[
p_2=3,\quad p_3=5,\quad p_4=7,
\]

so

\[
g_2=2,\qquad g_3=2.
\]

Hence

\[
B_2=\frac{g_2}{1}=2,
\]

\[
B_3=B_2+\frac{g_3}{2}=3,
\]

and

\[
y_3=B_3-B_2=1.
\]

The paper's claimed identity gives

\[
\frac32 y_3=\frac32,
\]

while

\[
B_3-B_2=1.
\]

Thus

\[
\boxed{3/2\ne1.}
\]

The stated identity is already false at the first nontrivial index.

## 4. Downstream dependency

The false weighted telescoping identity is used immediately to derive equation
(2.10) in Lemma 2.3.  The remainder of Lemma 2.3 uses that equation to obtain

\[
g_n<\frac{13}{3}B_n.
\]

The paper's Theorem 2.5 then depends on Lemma 2.3 to claim

\[
g_n<\frac{13}{3}\log^2 p_n.
\]

Its Theorem 3.1 derives the two Oppermann intervals from Theorem 2.5.

Therefore the current published arXiv proof chain has the dependency

\[
\text{false weighted telescoping identity}
\to
\text{equation (2.10)}
\to
\text{Lemma 2.3}
\to
\text{Theorem 2.5}
\to
\text{claimed Oppermann theorem}.
\]

The later claims are not established by the current proof.

## 5. Scope of the negative conclusion

This audit does **not** prove that a bound of order \(\log^2 p\) is false.
Nor does it prove that the author's intended argument cannot be repaired by an
entirely different proof.

It proves only the statement relevant to R005 source consumption:

> arXiv:2605.14871v5, as currently written, does not supply a valid proof of its
> maximal-gap theorem because a central algebraic identity in Lemma 2.3 is
> false by a direct exact counterexample.

Disposition:

\[
\boxed{\texttt{DO NOT CONSUME / PROOF CHAIN BROKEN}.}
\]

R005-B therefore retains the established Baker--Harman--Pintz / Jia /
Gafni--Tao / verified-computation boundaries and does not use Wang's claimed
Cramér-scale upper bound.

## 6. Version note

The audited object is arXiv v5 dated 23 July 2026.  Earlier versions advertised
different numerical constants.  The current v5 abstract claims
\(13/3\log^2 p_n\), and the exact algebraic break above occurs in that current
version.
