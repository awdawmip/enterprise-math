# D25/LIFT · GH-102–GH-103 — finite-log moment compression, ramification and polynomial contact lift

2026-10-29 · TASK_RESEARCH lane: chatgpt-research-hourly-enterprise-math-20260923.
Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION / D25/LIFT/JT2 OPEN; exact task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. The frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 is not changed.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** No authorized native CLAIM/OPEN, Source checkpoint, Result, independent review, or P000 modification is asserted.

## Exact inputs and source separation

Fix any prime \(p=8m+3\ge11\); put \(d=2m,\ N=(p-1)/2=2d+1=4m+1\), \(k=\mathbb F_p\). The cubic Hasse/Legendre descent from GH-100 gives a degree-\(m\) polynomial \(E(Y)\) with
\[
\operatorname{Ha}_p(T)=P_d(T)=E(T^2),\qquad
D=\binom{3m+1}{m}\in k^\times,\qquad
G(z)=z^m E(1-z^{-1})\in k[z].
\]
Here \(G(0)=D,\ G(1)=P_{2m}(0)\ne0\), \(G\) is monic of degree \(m\), and the **separate** reflected GH-16 source is
\[
U_d(z)=D^{-2}G(z)^2,\quad H_{\rm ref}(z)=(8\theta+5)U_d(z),\quad\theta=z\,d/dz.
\]
The GH-93 reflected tail is \(R_p(z)=\sum_{j=0}^d (8j+5)h_j z^{d+1+j}/(d+1+j)\), with \(R_p'=z^dH_{\rm ref}\) (GH-96). The GH-101 **signed finite-log Hasse moment** is
\[
M_p(a)=\sum_{y\in k}\chi(1-y)E(y)^2L_p(a(1-y)),
\quad L_p(t)=\sum_{n=1}^{p-1}t^n/n,\quad \chi(0)=0.
\]
The cubic Hasse coefficient, reflected \(U,H,R\), original GH-3 \(T_{p,9}\), and GH-83 Laurent \(B_0L\) are distinct sources and cannot be silently identified.

## GH-102 · Exact support and full tame ramification

**Theorem 102.1 (polynomial, not merely pointwise equality).** Let
\[
B(r)=E(1-r)^2=\sum_{j=0}^d b_j r^j.
\]
Then the polynomial defined by the *complete* finite-field moment has the exact form
\[
\boxed{M_p(z)=-\sum_{j=0}^{d}\frac{b_j}{N-j}z^{N-j}}. \tag{102.1}
\]
Its degree is exactly \(N\), its order at zero is exactly \(d+1\), its top coefficient is \(2\), and
\[
\boxed{M'_p(z)=-z^dG(z)^2=-D^2z^dU_d(z)} \quad\text{in }k[z]. \tag{102.2}
\]

**Proof.** Put \(r=1-y\) and use \(\chi(r)=r^N\) in \(k\). Expand the finite logarithm **before** specializing \(z\):
\[
M_p(z)=\sum_{n=1}^{p-1}\frac{z^n}{n}
       \sum_{j=0}^d b_j\sum_{r\in k}r^{N+j+n}.
\]
The exponents lie strictly between zero and \(2(p-1)\). The complete field power sum is \(-1\) exactly at exponent \(p-1\), otherwise zero. Hence the only surviving exponent satisfies
\(n=p-1-N-j=N-j\), proving (102.1) and showing precisely which \(p-1-(d+1)\) finite-log coefficients disappear. Since \(b_0=E(1)^2=P_d(1)^2=1\), the coefficient of \(z^N\) is \(-1/N=2\) in \(k\). As \(\deg E=m\) and its leading coefficient \(e_m\) is nonzero, \(b_d=e_m^2\ne0\) (because \(d\) is even), so the first nonzero coefficient occurs at \(z^{d+1}\). Differentiation gives
\[
M'_p=-\sum_{j=0}^d b_jz^{N-j-1}
=-z^{N-1}E(1-z^{-1})^2=-z^dG(z)^2,
\]
which is a polynomial identity with no negative powers. All denominators \(N-j\) lie in \([d+1,N]\subset[1,p-1]\).

**Theorem 102.2 (complete finite critical divisor).** Over the algebraic closure \(\bar k\), \(G\) has exactly \(m\) simple roots, all outside \(\{0,1\}\). The derivative \(M'_p\) has critical divisor
\[
\boxed{d[0]+2\sum_{G(\alpha)=0}[\alpha]}.
\]
Thus \(M_p\) has local ramification order exactly \(d+1\) at zero and order exactly \(3\) at each of the \(m\) distinct roots of \(G\); there are no other finite critical points.

**Proof.** GH-100 gives the exact second-order ODE
\[
z(1-z)G''+\left(\tfrac54-\tfrac74z\right)G'-\tfrac9{64}G=0.
\]
We have \(G(0)=D\ne0\) and \(G(1)=P_{2m}(0)=(-1)^m\binom{2m}{m}/4^m\ne0\) since \(2m<p\). If an ordinary root \(\alpha\notin\{0,1\}\) had \(G(\alpha)=G'(\alpha)=0\), the ODE and its repeated derivatives would force all Taylor coefficients to vanish (the leading factor \(\alpha(1-\alpha)\) and factorials \(1,\ldots,m\) are units), contradicting \(G\ne0\). Hence all \(m\) roots are simple. Equation (102.2) gives an order-\(d\) derivative zero at zero and double derivative zeros at these \(m\) roots. As \(d+2m=4m=N-1=\deg M'_p\), no others exist. Integrating local Taylor terms is valid because all local exponents are \(<p\), giving exact orders \(d+1\) and \(3\). QED.

This is a strong but **observer-scoped** compression: \(M\) remembers a Hasse square, not the full signed Hasse chart. Future sign/inverse operations must retain \(E,G\) or explicit repair data. No classical finite-field chart is promoted to an Enterprise X6 native law.

## GH-103 · Polynomial contact lift and nonstationary tangency

**Theorem 103.1.** Define a genuine polynomial
\[
C_p^*(z)=8z^{d+1}G(z)^2,\qquad\Delta_p(z)=C_p^*(z)-3M_p(z).
\]
Then
\[
\boxed{\Delta_p(z)=D^2 R_p(z)}\qquad\text{in }k[z]. \tag{103.1}
\]
At any \(a\in k^\times\), \(C_p^*(a)=8\chi(a)E(1-a^{-1})^2\), exactly the GH-101 contact value. The polynomial identity, unlike a character-function equality, is valid for taking derivatives and algebraic-extension observations.

**Proof.** Use (102.2):
\[
(C_p^*-3M_p)'=
z^d\big[(8(d+1)+3)G^2+16G\theta G\big].
\]
Since \(8(d+1)+3=2p+5\equiv5\pmod p\), this equals
\(z^d(5G^2+16G\theta G)=D^2z^dH_{\rm ref}=D^2R'_p\).
Both sides of (103.1) vanish at zero, proving equality of the entire polynomials. For \(a\ne0\), \(d+1+2m=N\), so
\(C_p^*(a)=8a^NE(1-a^{-1})^2=8\chi(a)E(1-a^{-1})^2\). QED.

**Corollary 103.2: exact \(p=3347\) transverse witness.** Independent integer modular reconstruction gives, at \(a=9\),
\[
\begin{array}{c|rrrrrrrr}
 &D&G(9)&M(9)&C^*(9)&R(9)&M'(9)&(C^*)'(9)&R'(9)\\
 \hline
 \bmod3347&3073&3333&1568&1357&0&2166&3151&0
\end{array}
\]
with \(3M(9)=C^*(9)=1357\) and \(3M'(9)=(C^*)'(9)=3151\), while
\[
R''(9)=2331\ne0,\qquad\Delta''(9)=914\ne0,
\qquad [ (z-9)^2 ]\Delta(z)=457\ne0\pmod{3347}.
\]
Therefore the two **individually moving** values \(C^*\) and \(3M\) agree in value and first derivative but not in second derivative. The exceptional equality is an exact double contact, rather than either observer vanishing or being stationary. For any other prime with \(H_{\rm ref}(9)=0\), (103.1) already forces the *slopes* to agree; equality of *values* is the additional arithmetic obligation. No universal classification or second-digit GH-3 claim follows.

## Exact execution and BRC provenance

A standalone Python standard-library checker was executed this run and has been published byte-for-byte as
research_notes/portable_direct/d25_gh102_gh103_hasse_moment_power_sum_check.py,
Git blob 0f8d0c90ce6bf93902a118a4735a9cf8f82cafb7, SHA256 9c96eb8b312a87a0aaa08936a3c5902ca7b5ed05f829011167bd09fb84e0e5b4.
It builds Legendre \(P_d\) independently from the three-term recurrence, computes \(E,G\), independently computes the reflected \(h_j\) recurrence and \(R\), checks (102.1), (102.2) and (103.1) coefficient by coefficient, verifies \(G\) squarefree with polynomial gcd, and checks selected direct finite-log/Fermat-quotient sums. **60 primes** (\(p\equiv3\pmod8\), \(11\le p<1500\), plus \(3347\)); all checks PASS. Concrete witness values above are re-derived by this exact program. Actual local execution log SHA256: 1f76fb934cca04372ee622dc4ff7068b40fc24fb4401f99201b882c3291f9b22. It is author evidence, not an independently reviewed proof or native Enterprise Math run.

**BRC COMPOSE_APPLIED:** population \(y\in\mathbb F_p\), signed \(\chi\)-sectors, original cubic/Hasse coefficients, separate reflected source, and the order of polynomial expansion, field summation, differentiation and evaluation are all retained. The full finite log is provably compressed **only for this exact moment and its polynomial-derivative future horizon**. It does not authorize removing the joint relation background, the sign of \(E\), the original GH-3 source, GH-83 Laurent residual, or the proof obligations of P000/Heartbeat X6. The polynomial contact is an auxiliary arithmetic observer with its own algebraic chart; no custom axiom, sorry or admit is used.

## Control status, next action and boundaries

This run's native gateway status: version 0.6.11, research_authority_granted=false, executor_binding_configured=false, source control CODE_REVIEW_REQUIRED, active control jobs 5/5. A directly callable recovery_status is not exposed on this authenticated connector. Previous exact D25 recovery and continuation requests are preserved under enterprise-math issue #1558; no historical pending write, old session, staged bytes or maintenance-lane identity was modified. No new CLAIM, OPEN, run or Source checkpoint was issued. GitHub author work does not supersede the Source's native persisted checkpoint.

**Next exact mathematical unit:** seek an independent CM/Jacobi/WZ evaluation of the *critical value* \(\Delta_p(9)\) or the exact polynomial quadrature \(-M_p(9)=\int_0^9 t^d G(t)^2\,dt\). A mere transformation of GH-101's formula is not such an evaluation. At \(3347\) explain why the value vanishes without assuming the observed cancellation; at general p seek a justified exceptional-prime criterion. Independently retain GH-92's \(T_{p,9}=0\pmod p\), GH-20/21 p-adic source moments and native \(p=373\) obligations. Do not repeat GH-98–GH-101's already completed finite-log identity or misapply this mod-p polynomial lift to mod-\(p^2\) precision.
