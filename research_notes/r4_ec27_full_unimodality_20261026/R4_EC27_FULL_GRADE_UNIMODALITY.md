# R4-EC27 — Complete full-grade unimodality of the auxiliary BRC clean-source kernel

**Date:** 2026-10-26 Asia/Shanghai. **Status:** author-side exact algebraic proof plus integer regression; not a native Result, independent Driver review, or Foundation promotion.

**Verified account control:** GLOBAL_KNOWLEDGE_V1 main@1fe18ba120c1f8f901246acb659589849b7e9147; P000 ACTIVE_LOCKED and ACTIVE worldview loaded. **Enterprise Math source:** main@24bcde1d8e98a6d8ce0f73ce8d9af283e5c85373; portable research and BRC/research-activity protocols read. Predecessor EC26 at 3d199096e78f81889fb5abd940879c4515102e91. Connected GitHub principal: awdawmip. Native task lookup returned CONTROL_QUOTA; session start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); neither active Owner nor formal CLAIM has been established.

## Exact theorem

Work solely in the existing **auxiliary positive-count ordered-binary BRC** clean-source observer, with
\[
E(x,u)=\sum_{n,j}e_{n,j}x^nu^j
=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6}.
\tag{1}
\]
The prior BRC construction supplies its clean-source count interpretation. The exact symmetry \(E(x,u)=E(ux,1/u)\) independently proves \(e_{n,j}=e_{n,n-j}\).

**Theorem.** For all integers \(n\ge10\) and \(1\le j\le\lfloor n/2\rfloor\):
\[
\boxed{e_{n,j}-e_{n,j-1}\ge0}
\tag{2}
\]
with equality **only** at \((n,j)=(10,3),(12,4)\). Therefore each full coefficient row \(E_n(u)\) is symmetric and unimodal for **all** \(n\ge10\). The statement has no grade cutoff or asymptotic qualification.

## Proof: exact diagonal factorization

Put \(a(t)=1+2t^2-t^3\). Let \(R(t)\in\mathbb{Z}[[t]]\) be the unique series with \(R(0)=1\) satisfying
\[
tR^2-aR+1=0,\qquad 1/R+tR=a.
\tag{3}
\]
Existence and uniqueness follow recursively because the coefficient of \(R\) at \(t=0\) is \(-1\).

Set \(x=z,\ u=t/z^2\) in (1) and expand \(t\)-adically:
\[
E(z,t/z^2)=\frac{1-t}{a-z-t/z}
=\frac{(1-t)R}{(1-Rz)(1-tR/z)}.
\tag{4}
\]
The expansion is legitimate in the ring of \(t\)-adic Laurent series in \(z\): at fixed power of \(t\), the negative \(z\) powers are bounded; the other factor is a formal \(z\)-power series. For every \(s\ge0\),
\[
B_s(t):=\sum_{j\ge0}e_{2j+s,j}t^j
=[z^s]E(z,t/z^2)
=\frac{(1-t)R^{s+1}}{1-tR^2}.
\tag{5}
\]
Reindexing \(e_{2j+s,j-1}=e_{2(j-1)+(s+2),j-1}\) (with \(e_{n,-1}=0\)) yields the **exact first-difference diagonal identity**
\[
\boxed{\sum_{j\ge0}(e_{2j+s,j}-e_{2j+s,j-1})t^j
=B_s-tB_{s+2}=(1-t)R^{s+1}.}
\tag{6}
\]
No numerical approximation or positivity hypothesis is used in this identity.

## Proof: positive algebraic certificate

Write \(R=1+t+Y\). Substitution in (3) gives
\[
\boxed{Y=t^4+(2t+t^3)Y+tY^2.}
\tag{7}
\]
Consequently \(Y=\sum y_mt^m\) has \(y_0=\cdots=y_3=0,\ y_4=1\) and all integer coefficients nonnegative. For \(m\ge5\):
\[
y_m=2y_{m-1}+y_{m-3}+\sum_{i=0}^{m-1}y_i y_{m-1-i}
\ge 2y_{m-1}>y_{m-1}.
\tag{8}
\]
Thus \(H=(1-t)Y\) has precisely zero coefficients below degree 4, and **strictly positive** coefficients at every degree \(m\ge4\).

For each \(p\ge1\), the binomial identity
\[
\boxed{(1-t)R^p=(1-t)(1+t)^p+
 \sum_{m=1}^{p}\binom pm(1+t)^{p-m}Y^{m-1}H}
\tag{9}
\]
has a coefficientwise nonnegative sum on the right. The first term is a polynomial of degree \(p+1\). Hence, using the \(m=1\) summand,
\[
[t^j](1-t)R^p\ge p[t^j]H>0
\quad\text{whenever }j\ge\max(4,p+2).
\tag{10}
\]

At \(p=6\), direct exact expansion of the formal recurrence (7) gives
\[
([t^j](1-t)R^6)_{j=0}^{7}=(1,5,9,5,1,27,97,209).
\tag{11}
\]
All entries are positive, while (10) covers \(j\ge8\). Thus \((1-t)R^6\) has strictly positive coefficients in **every degree**. Because \(R\) has nonnegative coefficients and constant term 1, for all \(p\ge6\) the product \((1-t)R^6\cdot R^{p-6}=(1-t)R^p\) is coefficientwise strictly positive.

For \(p=s+1\le5\), the theorem's depth constraint \(n=2j+s\ge10\) gives \(j\ge\lceil(10-s)/2\rceil\). Only these finitely many indices fall outside the strict tail certificate (10):

| s | p | j to inspect | exact \([t^j](1-t)R^p\) |
|---:|---:|---|---|
| 0 | 1 | none | — |
| 1 | 2 | none | — |
| 2 | 3 | 4 | 2 |
| 3 | 4 | 4,5 | 1,15 |
| 4 | 5 | 3,4,5,6 | 0,0,21,59 |

All entries are nonnegative, with exactly two zeros: \((s,j)=(4,3),(4,4)\), giving \((n,j)=(10,3),(12,4)\). The case \(s\ge5\) has \(p\ge6\) and is already strictly positive. Combining this finite exhaustion with (6) **completes the unbounded theorem**. QED.

## Corollary: complementary-source count ordering

Under the **previously proved EC17 exact auxiliary reflection identity**
\[
D[n,k]=C[n,n-k]-C[n,k]=e_{n-3,k-1}-e_{n-3,k-2},
\]
for all \(n\ge13\) and \(1\le k<n/2\),
\[
\boxed{D[n,k]\ge0}
\]
with equality only at \((n,k)=(13,4),(15,5)\); at \(k=1\), EC16 gives \(D[n,1]=1\). This corollary retains the original positive-count auxiliary BRC observer and EC17 model assumptions. It is not a native X6 source-count theorem.

## Reproducibility and boundaries

The executed integer-only verifier reconstructs two independent algebraic recurrences, checks the defining quadratic, positivity of \((1-t)Y\), diagonal identity, B6 base coefficients, symmetry, and full finite-grid unimodality. The short GitHub program checks all \(0\le n\le120\): **3,721 diagonal pairs** and **3,580 relevant nonnegative differences**, with exactly two equality cases. The separately retained full local package also checks all \(0\le n\le160\), 6,561 diagonal pairs and 6,380 admissible differences. Finite tests are cross-checks; (3)–(11) are the proof.

**BRC reuse:** REUSE_APPLIED to EC17 positive-count kernel, reflection identity and exact coefficient observer; EC26's gamma positivity failure is respected. The formal algebraic variable \(R\) is a certificate, not a physical branch weight, new signed-mass observer, X6 coordinate, or heartbeat time.

**Unfinished R4-EC28:** independent exact review of (4)–(10) and EC17-to-EC27 reflection transfer; assess whether a typed native X6 embedding exists with an explicit 3D-slice third coordinate, update, readout and preserved relations. Native control/CLAIM, independent Driver review, formal Lean check, prior-art review and native physical transfer remain pending.
