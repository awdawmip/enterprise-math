# R749SSU — Effective exact inversion without a prior cutoff bound

Date: 2026-11-17. Evidence: **AUTHOR_EXACT_NOT_REVIEWED**, standalone author-side exact certificate PASS. Mode: independent five-*distinct-labeled*-source scalar-observer research, preserving the source science frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.

## Problem and main theorem

Let the first of five labeled sources with weights \((1,1,2,3,6)\) be marked. For integers \(q\ge6\), define
\[
\Omega_q=\{k\in{\mathbb Z}_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1,
\]
\[
S(x)=18x^4+54x^3-345x^2+2070x-16315,\qquad
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108}.
\]
The calibration errors \(e,d\in[-2,2]\) are real and **shared over an entire trajectory**. Write \(y_j=Y_{q+6j}(e,d)\), \(0\le j\le10\), and \(\Delta=\max_j y_j-\min_j y_j\).

**Theorem (effective inversion).** For any such exact ordered 11-reading vector, \(\Delta>0\), and
\[
\boxed{6\le q\le\left\lfloor\frac{40766}{\Delta}\right\rfloor.}
\]
Thus the R749SST global injectivity theorem has a **terminating finite exact reconstruction algorithm even without an a priori upper bound on \(q\)**: enumerate this bounded interval of integer candidates, solve a pair of *linear* equations for the candidate's \(e,d\), retain candidates in \([-2,2]^2\), and compare their complete ordered 11-reading vectors. Exactly one candidate survives by R749SST. The algorithm uses exact-real comparison/oracles if the supplied readings are arbitrary real numbers; rational input is handled entirely with rational arithmetic.

The estimate is a conservative sufficient search bound, not an optimal noise margin or a complexity-optimal inversion procedure.

## Proof A: a global explicit tail envelope

The all-phase exact quasipolynomials \(C_r(x)\) (degree 5) and \(T_r(x)\) (degree 6), \(r=x\bmod6\), follow from R749SST's exact generating-function identities
\[
\sum C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
They represent every integer \(x\ge6\) of each corresponding residue, not only interpolation samples. Put
\[
N_r(x;e,d)=x^3(T_r(x)+e)-\frac{S(x)}{108}(C_r(x)+d),
\quad
R_r(x;e,d)=\frac{N_r(x;e,d)}{C_r(x)+d}.
\]
The numerator and denominator have degree 5 and the leading ratio is the phase limit
\[
(L_0,L_1,L_2,L_3,L_4,L_5)
=(455,-295,-25,185,-25,-295)/36.
\]
Consequently \(V_r=N_r-L_r(C_r+d)\) has degree at most 4 and is affine in \((e,d)\):
\[
V_r(x;e,d)=A_r(x)+eB_r(x)+dD_r(x).
\]
For every \(x\ge6\),
\[
|V_r(x;e,d)|\le b_rx^4,\quad
b_r=\sum_{k=0}^4\frac{|[x^k]A_r|+2|[x^k]B_r|+2|[x^k]D_r|}{6^{4-k}}.
\]
Here the coefficients are rational and can be independently generated from the supplied exact certificate.

An elementary geometric lower bound eliminates asymptotic assumptions: the nonnegative real simplex \(\sum_iw_it_i<q\) has volume \(q^5/(5!\prod_iw_i)=q^5/4320\). Its integer-floor partition maps each point to an element of \(\Omega_q\); hence
\[
C_q\ge q^5/4320.
\]
Because \(C_6=41\), \(C_q\) is increasing, and \(-2\le d\le2\),
\[
C_q+d\ge C_q-2\ge \frac{39}{41}C_q
\ge \frac{39q^5}{41\cdot4320}.
\]
The **six exact rational envelope values** \(K_r=(41\cdot4320/39)b_r\) are:

| \(r\) | \(K_r\) |
|---:|---:|
| 0 | \(55442045/3159\) |
| 1 | \(41724295135/2047032\) |
| 2 | \(4955229250/255879\) |
| 3 | \(155263925/8424\) |
| 4 | \(4897450820/255879\) |
| 5 | \(3194235995/157464\) |

Their maximum is exactly \(41724295135/2047032<20383\). Therefore, **for all \(q\ge6\) and all admissible real errors**,
\[
\boxed{|Y_q(e,d)-L_{q\bmod6}|<20383/q.}
\]
All six readings along any \(6\)-shift trajectory have the **same phase limit**, giving \(\Delta<40766/q\) for any finite number of its readings. The claimed weak upper bound on the integer \(q\) follows.

## Proof B: the observed spread is never zero

Suppose the first six consecutive six-step readings were all equal to a constant \(c\). Then the degree-at-most-five polynomial
\[
N_r(x;e,d)-c(C_r(x)+d)
\]
would vanish at six distinct integers \(q,q+6,\ldots,q+30\) and hence would vanish identically. Its leading coefficients force \(c=L_r\), so \(V_r(x;e,d)\equiv0\).

Solving merely the \(x^4,x^3\) coefficient equations of \(V_r=0\) yields a **unique** pair of real parameters for every phase. The forced value of \(e\), in phase order \(r=0,\ldots,5\), is
\[
-\frac{83605}{17496},\
-\frac{417355}{69984},\
-\frac{47873}{8748},\
-\frac{352807}{69984},\
-\frac{46955}{8748},\
-\frac{413035}{69984}.
\]
Every value is strictly less than \(-2\), contradicting the permitted calibration square. Consequently six readings cannot be constant, and in particular \(\Delta>0\) for eleven readings.

## Proof C: an exact terminating reconstruction

For each candidate \(n\in\{6,\dots,\lfloor40766/\Delta\rfloor\}\), define
\[
X_0(n)=\frac{y_0+S(n)/108}{n^3},\qquad
X_1(n)=\frac{y_1+S(n+6)/108}{(n+6)^3}.
\]
If \(X_1(n)=X_0(n)\), discard the candidate; a genuine candidate has \(X_1>X_0\) by the known-cutoff two-reading theorem R749SSJ. Otherwise solve
\[
d_n=\frac{T_{n+6}-T_n-X_1(n)C_{n+6}+X_0(n)C_n}{X_1(n)-X_0(n)},
\quad e_n=X_0(n)(C_n+d_n)-T_n.
\]
Retain the candidate only when \(|e_n|,|d_n|\le2\) and \(Y_{n+6j}(e_n,d_n)=y_j\) for all \(0\le j\le10\). Proof A makes the scan finite, the actual generating triple passes it, and the previously established R749SST 11-read theorem makes it unique. No new claim about the sharp minimal observation horizon is needed.

## Exact verification and scope

The accompanying Python/SymPy program recomputes all six \(C_r,T_r\) rational quasipolynomials from labeled weights, verifies their degrees and additional sample values, checks every numerator cancellation, every coefficient-wise rational envelope, the strict universal \(K=20383\), and the six inconsistent constant-trajectory values. Exact rational inversion is exercised at \(q=6,7,12\) with permitted nontrivial errors; all tests PASS. The code and JSON are supplied as source material, not as an independent mathematical referee.

The full global finite-search uniqueness step invokes the earlier author's exact R749SST result (draft PR #2592); its mathematical review status remains **AUTHOR_EXACT_NOT_REVIEWED**. The current result supplies an independently recalculable effectivity and search bound. This model remains an auxiliary *scalar observer* with five retained source labels and shared temporal calibration. It is not by itself a typed native X6 state update or BRC Port theorem. A transfer must retain the exact observer fibres, source labels, time order, and allowed future operations.

**Next questions:** optimize \(K\) or derive an adaptive phase-specific stopping test; combine effective finite search with cutoff-range-dependent minimax noise certificates; tighten the 11-reading global upper bound, and formulate a provenance-preserving BRC observer carrier.
