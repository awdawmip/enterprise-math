# R749SSW — Sharp normalized two-read gap and stable error inversion at known cutoff

**Date:** 2026-11-17. **Research status:** AUTHOR_EXACT_NOT_REVIEWED.
**Scope:** frozen auxiliary scalar model with five *distinct labeled* sources of weights (1,1,2,3,6).
**Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
**Prior frontier:** R749SST (11-read global exact identifiability), R749SSU (constructive inversion), R749SSV (sharp phase envelopes). Their evidence status is retained.

## Definitions and theorem

For every integer \(q\ge6\), define
\[
\Omega_q=\{(k_1,\ldots,k_5)\in\mathbf Z_{\ge0}^5:
k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
The first two weight-one sources are distinct. Let \(e,d\in[-2,2]\) be the same errors across all observations, and put
\[
X_q(e,d)=\frac{T_q+e}{C_q+d},\qquad
Y_q(e,d)=q^3X_q(e,d)-\frac{S(q)}{108},
\]
with \(S(q)=18q^4+54q^3-345q^2+2070q-16315\).

**Theorem 1 — exact global two-read gap.** For every integer \(q\ge6\) and every real \(e,d\in[-2,2]\),
\[
\boxed{X_{q+6}(e,d)-X_q(e,d)>1.}
\]
The constant 1 is asymptotically sharp: for every fixed admissible \(e,d\), the left side tends to 1 along every residue class modulo 6.

**Corollary 1 — known-cutoff two-read recovery.** For each fixed known integer \(q\ge6\), the map
\((e,d)\mapsto(Y_q(e,d),Y_{q+6}(e,d))\)
is injective on the entire real square \([-2,2]^2\). Given two exact readings \(y_0,y_1\), form
\[
x_0=\frac{y_0+S(q)/108}{q^3},\qquad
x_1=\frac{y_1+S(q+6)/108}{(q+6)^3}.
\]
Then \(x_1-x_0>1\), and both parameters are recovered by
\[
\boxed{d=\frac{x_0C_q-T_q-x_1C_{q+6}+T_{q+6}}{x_1-x_0}},
\qquad
\boxed{e=x_0(C_q+d)-T_q}.
\]
The normalized Jacobian determinant is exactly
\[
\det D_{(e,d)}(X_q,X_{q+6})
=\frac{x_0-x_1}{(C_q+d)(C_{q+6}+d)}<0.
\]

**Corollary 2 — explicit fixed-cutoff stability.** Take two admissible model states \((e,d)\), \((e',d')\) with the same cutoff, and let
\[
\delta=\max_{j=0,1}\left|X_{q+6j}(e,d)-X_{q+6j}(e',d')\right|.
\]
Then
\[
|d'-d|\le(C_q+C_{q+6}+4)\delta,
\]
and
\[
|e'-e|\le\left[(C_q+2)
+\frac{T_q+2}{C_q-2}(C_q+C_{q+6}+4)\right]\delta.
\]
When the corresponding raw \(Y\)-vectors differ by at most \(\varepsilon\) in sup norm, one may use \(\delta\le\varepsilon/q^3\). Comparing an admissible fit with the true state when each may deviate by \(\varepsilon\) from the observed vector requires using \(2\varepsilon\) for the two-state comparison.

## Exact proof by six residue classes

The labeled-source generating functions are
\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},
\]
\[
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
Every pole is a sixth root of unity. The pole at 1 has order 6 for \(C\) and order 7 for \(T\); the others have smaller order. Thus for each \(r=0,\ldots,5\), the sequences \(C_{6+r+6k}\) and \(T_{6+r+6k}\) are exactly polynomials in \(k\ge0\) of degrees 5 and 6. Six and seven exact initial values uniquely determine these polynomials for the entire infinite residue class. The accompanying certificate reconstructs their values from five labeled sources, interpolates over exact rationals, and checks extra instances.

Abbreviate \(C=C_q,\ C'=C_{q+6},\ T=T_q,\ T'=T_{q+6}\), and define
\[
A=T'C-TC',\qquad B=T'-T,\qquad D=C'-C.
\]
Here \(D>0\), and \(C_q\ge41\) for \(q\ge6\), so both \(C+d,C'+d\) are positive.

The numerator of the desired strict inequality is
\[
\begin{aligned}
N(e,d)
&=(C+d)(C'+d)[X_{q+6}(e,d)-X_q(e,d)-1]\\
&=A+dB-eD-(C+d)(C'+d).
\end{aligned}
\]
For fixed \(d\), \(N\) decreases in \(e\) because \(D>0\). For \(e=2\), it is a concave quadratic function of \(d\) with leading coefficient \(-1\). Therefore the minimum on the full square occurs at one of the two corners \((e,d)=(2,-2),(2,2)\).

Substitute \(q=6+r+6k\) into both corner polynomials. For all six residues and both endpoints, the resulting **12 polynomials are of degree 8 with every coefficient strictly positive**. The smallest coefficient among all 12 is \(69/40\). Their constant terms are:

| Residue \(r\) | \(N(2,-2)\), \(k=0\) | \(N(2,2)\), \(k=0\) |
|---:|---:|---:|
| 0 | 39 | 1679 |
| 1 | 945 | 3341 |
| 2 | 2184 | 5588 |
| 3 | 4527 | 9239 |
| 4 | 8685 | 15065 |
| 5 | 14859 | 23339 |

Every such polynomial is positive for \(k\ge0\). Therefore \(N(e,d)>0\) for the full continuous error square and all \(q\ge6\), which proves Theorem 1 after division by its positive denominators.

For sharpness, the coefficient of \(k^5\) in every phase polynomial \(C_{6+r+6k}\), and of \(k^6\) in \(T_{6+r+6k}\), both equal \(9/5\). Hence for any fixed \(e,d\), \(X_{6+r+6k}(e,d)=k+\mathrm{constant}+O(k^{-1})\); subtract successive values to get the limit 1.

For Corollary 1, solve the linear equations \(e-x_i d=x_i C_i-T_i\), \(i=0,1\), using the strictly nonzero denominator \(x_1-x_0\). The Jacobian expression follows by differentiation.

For Corollary 2, let \(\delta_i=X_{q+6i}(e',d')-X_{q+6i}(e,d)\), and subtract the defining equations:
\[
(e'-e)-x_i(d'-d)=\delta_i(C_{q+6i}+d').
\]
Subtract the equations for \(i=0,1\), use \(x_1-x_0>1\), \(C_i+d'\le C_i+2\), and then \(0<x_0\le(T_q+2)/(C_q-2)\).

## Concrete witness, validation and provenance

For \(q=6,e=2,d=-2\), the exact values are \(C_6=41,T_6=50,C_{12}=380,T_{12}=881\). Consequently
\[
X_6=4/3,\quad X_{12}=883/378,\quad X_{12}-X_6=379/378=1+1/378.
\]

Reproduction requires Python 3 and SymPy. Run the sibling file
R749SSW_TWO_READ_CONDITIONING_CERT.py; it emits an exact-rational JSON PASS record checking all 12 coefficient-positive polynomials, positivity of \(D\), leading coefficients and the witness. The all-cutoff coverage depends on the explicitly proved generating-function quasipolynomial lemma; extra numerical checks are not used as its replacement.

This result strengthens the previously employed two-read parameter elimination at **fixed known** \(q\). Unknown-\(q\) identification still uses its own R749SST 11-read result. Six-step spacing denotes the auxiliary scalar observer, not a native physical time interval. Five source labels, joint populations, provenance, common errors and future observer fibers are retained. A native X6/BRC result requires an independently verified typed preservation map; P000 remains unchanged.

**Next research:** finite-cutoff cross-\(q\) minimax gap and robust recovery; possible reduction of the unknown-\(q\) 11-read global upper bound; explicitly typed, signed and source-preserving BRC extension.
