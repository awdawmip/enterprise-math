# D25/LIFT GH-72–GH-73: full de Rham 2-isogeny transfer and Gauss–Manin/Hasse normalization

2026-10-29 Asia/Hong_Kong. Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This document preserves an author-side arithmetic-chart calculation, not a native Source checkpoint or mathematical admission. Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN; previously supplied task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT (TP2-B6F4FC938FF94941C1B7), whose current ownership must be verified separately. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Exact prior input and domain

In GH-70/GH-71, the auxiliary elliptic family over characteristic zero or a field of characteristic at least 5 is
\[
C_T:\ y^2=f_T(x)=x^3+x^2+b_Tx,\quad b_T=(1+T)/8,\quad T^2\ne1.
\]
Let \(\omega_T=dx/(2y)\) and \(\eta_T=x\,dx/(2y)\), the standard de Rham basis. Choose \(v^2=-2\). GH-71's preexisting separable degree-two isogeny (used as input, not recredited here) is
\[
\kappa_T:C_T\longrightarrow C_{-T},\quad
x_-=-\tfrac12(x+1+b_T/x),\quad
y_-=\frac{y(1-b_T/x^2)}{v^3},\quad
\kappa_T^*\omega_{-T}=v\omega_T.
\]

## GH-72: full two-component pullback and its exact correction

**Theorem.** In algebraic de Rham cohomology,
\[
\boxed{\kappa_T^*\omega_{-T}=v\omega_T,\qquad
\kappa_T^*\eta_{-T}=-v(\eta_T+\tfrac12\omega_T).}
\]
The statement includes the full second-kind differential class. It is stronger than the previously known invariant-differential multiplier.

**Proof.** Differentiating the rational function \(y/x\) on \(C_T\) gives the exact identity
\[
d(y/x)=\frac{xf'_T(x)-2f_T(x)}{x^2}\,\omega_T
=(x-b_T/x)\omega_T.
\]
Thus \((b_T/x)\omega_T=\eta_T-d(y/x)\). Substituting into the pullback of \(x_-\omega_{-T}\) yields the exact meromorphic-differential identity
\[
\kappa_T^*\eta_{-T}
=-v(\eta_T+\tfrac12\omega_T)+\frac v2\,d(y/x).
\]
The exact correction has zero de Rham class; dropping it in a raw-differential equality would be incorrect. In the ordered basis \(e_T=(\omega_T,\eta_T)^t\),
\[
\kappa_T^*e_{-T}=vMe_T,\quad
\boxed{M=\begin{pmatrix}1&0\\-1/2&-1\end{pmatrix}},\quad M^2=I.
\]
The two-step action is \(v^2M^2=-2I\), agreeing with the geometric signed cocycle \(\kappa_{-T}\circ\kappa_T=[-2]\) of GH-71. This proof preserves the ordered two-step isogeny and differential origins.

## GH-73: explicit connection matrix, Picard–Fuchs operator and Hasse coefficients

Write \(b=b_T,\ D=x^2+x+b,\ f=xD\). Differentiating the relative differentials at fixed \(x\) gives
\[
\nabla_{\partial_b}\omega=-\frac{1}{2D}\omega,\qquad
\nabla_{\partial_b}\eta=-\frac{x}{2D}\omega.
\]
Use de Rham classes \(X=[\omega/D]\), \(Y=[x\omega/D]\). The exact differentials \(d(x/y)\), \(d(x^2/y)\) give
\[
Y+2bX=[\omega],\qquad
(1-2b)Y+bX=[\omega]+[\eta].
\]
Solving these **two explicit cohomological reduction relations**:
\[
X=\frac{2b[\omega]+[\eta]}{b(4b-1)},\qquad
Y=-\frac{[\omega]+2[\eta]}{4b-1}.
\]
Since \(db/dT=1/8\), the Gauss–Manin connection is
\[
\boxed{
\nabla_{\partial_T}
\begin{pmatrix}[\omega_T]\\[\eta_T]\end{pmatrix}
=\mathcal A(T)
\begin{pmatrix}[\omega_T]\\[\eta_T]\end{pmatrix},\qquad
\mathcal A(T)=
\begin{pmatrix}
-\dfrac{1}{4(T-1)}&-\dfrac{1}{T^2-1}\\[3pt]
\dfrac{1}{8(T-1)}&\dfrac{1}{4(T-1)}
\end{pmatrix}.}
\]
In particular \(\mathrm{tr}\mathcal A=0\), \(\det\mathcal A=-1/[16(T^2-1)]\). The **exact normalized isogeny/Gauss–Manin compatibility** is
\[
\boxed{M\mathcal A(T)+\mathcal A(-T)M=0.}
\]
This follows by rational matrix multiplication and expresses functorial horizontality under the parameter involution \(T\mapsto-T\), whose derivative supplies the minus sign.

For a locally horizontal period functional of \(\omega_T\), eliminate the \(\eta_T\) component from the displayed first-order connection. The scalar Picard–Fuchs equation is
\[
\boxed{(T^2-1)y''+2Ty'+\frac3{16}y=0.}
\]
For characteristic \(p\ge5\), this is the differential-module identity; complex analytic period integrals are claimed only in characteristic zero.

**Independent finite-field Hasse–Legendre proof.** Let \(p=8m+3\ge11\) be prime, \(N=(p-1)/2=4m+1\), \(n=2m\). Define the Hasse coefficient of the actual \(C_T\) model:
\[
\mathcal H_p(T)=[x^{p-1}]\bigl(x^3+x^2+\tfrac{1+T}{8}x\bigr)^N
=\sum_{j=0}^n\binom N{2j}\binom{2j}{j}\left(\frac{1+T}{8}\right)^j.
\]
For each \(0\le j\le n\), the coefficient of \((1+T)^j\) equals
\[
\frac{(-N)_{2j}}{8^j(j!)^2}
=\frac{(-N/2)_j((1-N)/2)_j}{2^j(j!)^2}
\equiv\frac{(-n)_j(n+1)_j}{2^j(j!)^2}\pmod p.
\]
Here \(-N/2\equiv1/4\equiv n+1\), \((1-N)/2\equiv3/4\equiv-n\pmod p\); all \(j!\) are units. The finite hypergeometric Legendre identity gives
\[
P_n(-T)=\sum_{j=0}^n\frac{(-n)_j(n+1)_j}{(j!)^2}
\left(\frac{1+T}{2}\right)^j.
\]
As \(n=2m\) is even,
\[
\boxed{\mathcal H_p(T)=P_{2m}(T)\quad\text{in }\mathbb F_p[T].}
\]
Thus this coefficientwise proof establishes the normalized Hasse invariant directly for \(C_T\), **without using** GH-69's external character-sum input for the different \(E_T\) model. The Legendre equation agrees with the connection's Picard–Fuchs operator since \(n(n+1)\equiv-3/16\pmod p\). This is a mathematical crosscheck of the full normalized transfer.

## Arithmetic special-value boundary and exact tests

The preceding covariance holds for a whole family; the remaining split-prime target is point-specific:
\[
t_0\mathcal H_p'(t_0)-\mathcal H_p(t_0)=0,\qquad
t_0^2=8/9,\qquad p\equiv11\pmod{24}.
\]
The generic isogeny/connection identities alone do not prove it: at \(p=11\), \(P_2=(3T^2-1)/2\), so \(TP'_2-P_2=(3T^2+1)/2\), which vanishes for \(T^2=8/9\) but is \(1/2\ne0\) at \(T=0\). A CM/Frobenius **point-specific** unit-root or independent character-sum calculation remains the next mathematical obligation.

The attached independent Python/SymPy checker has been executed locally. It verifies exact rational identities for the differential reductions, the full \(M,\mathcal A\) matrices, covariance and Picard–Fuchs elimination. It also compares the Hasse and Legendre coefficients for all **310** primes \(11\le p<10000\), \(p\equiv3\bmod8\), covering **362314** exact finite-field coefficients; all passed. These finite tests validate implementations, not universal claims by sampling. Universal statements above follow from the written algebraic proofs. No native \(p=373\) experiment was run; no research Source claim/run or Driver review is inferred.

**BRC scope:** retain the ordered \(T\to-T\to T\) isogeny steps, differential-basis origin, exact correction \(d(y/x)\), arithmetic field, prime, and Hasse/period observer distinctions. This is an auxiliary algebraic chart, not an asserted native X6 transfer or complete three-dimensional slice. P000 ACTIVE, W/S, six Hasse ports, R23/R36, GH-20/GH-21 second digits, and GH-3 remain subject to their separate obligations.

**Next:** combine the displayed normalized Gauss–Manin matrix with an independently computed CM/Frobenius unit-root line at \(t_0\), retaining model twists, and evaluate the Euler–Hasse derivative; a family-wide matrix identity must not be rebranded as the split-prime special-value certificate. Current native ownership/claim/run/request require fresh authorized Source recovery before any role-bound write; do not adopt old sessions or unstaged uploads.

## Provenance

- GH-71 signed 2-isogeny (inherited input): enterprise-math@4e9a9467fb8be2fba91bf9f358d821162c66e3bf, research_notes/portable_direct/20261029_hourly_d25_gh71_fricke_cocycle.md.
- GH-69/GH-70 Hasse/CM chart (inherited input): enterprise-math@e918c001304d337c9a76e2ccc925160e68abf972, research_notes/portable_direct/20261029_hourly_d25_gh69_gh70_cm_hasse_bridge.md.
- GH-55 original F/G Legendre source (inherited input): enterprise-math@9cceb3e48c0a7fca2d36918814cd9cefe00e8db3.
- Exact checker: research_notes/portable_direct/20261029_hourly_d25_gh72_gh73_gauss_manin_isogeny_check.py (locally executed identical Git blob 348cc6fb9563c1d3e242eba0f5a048042c17225c).
