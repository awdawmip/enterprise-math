# D25 — Exact Legendre-second-kind Wronskian and CM unit-derivative criterion

Date: 2026-11-10. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`, not maintenance. Frozen science pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; Source native frontier \`b58330b74576153cdadde5d80a3d92df3a819a0e\` retained. **AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.**

## Exact theorem over Q, for every integer n >= 1

Define the normalized Legendre polynomial and the finite signed second-kind polynomial
\[
P_n(x)=P_n^{\rm Legendre}(1-2x)=\sum_{k=0}^{n}C_kx^k,\qquad
C_k=(-1)^k\binom nk\binom{n+k}k,
\]
\[
U_n(x)=\sum_{r=0}^{n-1}U_rx^r,\qquad
U_r=\sum_{k=r+1}^{n}\frac{C_k}{k-r}.
\]
Let \(\mathcal D_n=x(1-x)\partial_x^2+(1-2x)\partial_x+n(n+1)\). The following are exact polynomial identities over \(\mathbb Q\):
\[
\boxed{\mathcal D_n U_n=2P_n'},\qquad
\boxed{x(1-x)(P_nU_n'-P_n'U_n)=P_n^2-1}. \tag{W}
\]

**Proof (formal Laurent algebra, no analytic continuation).** Set \(\Lambda(x)=\sum_{j\ge1}x^{-j}/j\) in \(\mathbb Q((x^{-1}))\). Then \(\Lambda'=1/[x(1-x)]\) and the nonnegative-power part of \(P_n\Lambda\) is \(U_n\) by coefficient comparison. The Legendre equation is \(\mathcal D_nP_n=0\). The product rule and \(x(1-x)\Lambda'=1\) yield \(\mathcal D_n(P_n\Lambda)=2P_n'\). Since \(\mathcal D_n\) maps negative Laurent powers to negative Laurent powers, polynomial-part extraction proves \(\mathcal D_nU_n=2P_n'\).

For \(W_0=P_nU_n'-P_n'U_n\), direct Sturm–Liouville cancellation gives
\[
[x(1-x)W_0]'=P_n\mathcal D_nU_n-U_n\mathcal D_nP_n
=2P_nP_n'=(P_n^2)'.
\]
At \(x=0\), the left primitive vanishes and \(P_n(0)^2=1\). The integration constant is \(-1\), proving (W), including endpoints and signs. QED.

## CM(-24): exact finite-log evaluation at a supersingular Hasse root

Let \(p\equiv13\pmod{24}\) be prime and \(q=(p-1)/4\), which is odd. Work over \(\mathbb F_p[t]/(t^2-2)\) and put
\[
s=\tfrac12-\tfrac t3,\quad s^*=\tfrac12+\tfrac t3,\quad
s+s^*=1,\quad ss^*=\tfrac1{36},\quad s^p=s^*.
\]
Use the earlier author-side CM result \(P_q(s)=0\bmod p\). Identity (W) itself proves this root is simple, since at a root \(a\notin\{0,1\}\),
\(-a(1-a)P_q'(a)U_q(a)=-1\).

The original finite-log object is \(L_p(x)=\sum_{j=1}^{p-1}x^j/j\) and \(A_p(x)=[P_q(x)L_p(x)]_{<p}\). Exact coefficient extraction in \(\mathbb F_p[x]\) gives
\[
P_q(x)L_p(x)=A_p(x)-x^p U_q(x).
\]
At \(s\) this gives \(A_p(s)=s^pU_q(s)\). The Wronskian supplies
\[
U_q(s)=\frac1{s(1-s)P_q'(s)},\qquad
\boxed{A_p(s)=\frac1{sP_q'(s)}=\frac{18+12t}{D_p}}, \tag{CM-W}
\]
where \(D_p=P_q'(s)\in\mathbb F_p^\times\). Indeed \(P_q(1-x)=-P_q(x)\) for odd \(q\), so \(P_q'(1-x)=P_q'(x)\), showing \(D_p\) is Galois-fixed.

Both distinct original observers now have closed forms:
\[
\boxed{\operatorname{Tr} A_p(s)=\frac{36}{D_p}},\qquad
\boxed{\operatorname{Coeff}_t A_p(s)=\frac{12}{D_p}},\qquad
\operatorname{Tr} A_p(s)=3\,\operatorname{Coeff}_t A_p(s).
\]
Here \(\operatorname{Tr}(a+bt)=2a\), while \(\operatorname{Coeff}_t(a+bt)=b\). This *fully evaluates* the former quarter-length finite-log tail using one Legendre derivative. The auxiliary quadratic ring remains separate from the native six-dimensional state and H0/B0 Frobenius.

## The remaining concrete p² proof obligation

The prior author-side first-jet relation (unchanged) is
\[
6pg_p\equiv3f_q(8/9)+f_{3q}(8/9)\pmod{p^2},\qquad
P_n^{\rm Legendre}(y)=y f_n(y^2)\quad(n\ \text{odd}).
\]
The previous unresolved relation \(\operatorname{Tr}A_p(s)\stackrel?=24g_p\bmod p\) is now *equivalent* to the single integral-residue condition
\[
\boxed{D_p\bigl(3f_q(8/9)+f_{3q}(8/9)\bigr)
\stackrel?{\equiv}9p\pmod{p^2}.} \tag{UD}
\]
Since the bracket is divisible by \(p\) and \(D_p\) is nonzero modulo \(p\), the product modulo \(p^2\) is independent of the chosen lift of \(D_p\). The all-prime identity (UD) remains **unproved**. An exact p² Legendre contiguous/Wronskian relation or local CM Frobenius lift is the next discriminating route.

## Reproducible exact tests and evidence strength

The companion standard-library Python file independently constructs the rational polynomial Wronskian, the untruncated finite-log coefficient product, the original \(G_p(s)\) recurrence modulo \(p^2\), and the derivative formula. All 22 primes \(p<1000\) with \(p\equiv13\bmod24\) passed each of these checks. A separate derivative-coefficient/Gauss recurrence path (without constructing \(U_n\) or \(A_p\)) tested (UD) for all 157 primes \(p\le10000\), all PASS. These tests support (UD) only on that stated finite window; (W) is separately proved over \(\mathbb Q\).

Rows \((p,q,\operatorname{Tr}A,\operatorname{Coeff}_tA,D_p,g_p)\):
\[
(13,3,7,11,7,3),\quad (37,9,19,31,35,27),\quad
(373,93,149,174,193,115),\quad
(613,153,599,404,85,357),\quad
(997,249,799,931,453,241).
\]
At \(p=373\), \(36/193=149=24\cdot115\bmod373\). No floating-point arithmetic was used.

## Frontier

Consume (W) and (CM-W) rather than redoing the earlier 157-prime Hasse zero scan and finite-log convolution. Focus next on proving (UD) directly, with the fixed original CM point and p-adic signs. Keep the original same-class p=373 native H0/B0 divided-power experiment [X]U modulo 139129 and rank, semilinearity/normalization, signed kappa, original Delta-R, independent replication **NOT_RUN** (support issue #1559). Source native checkpoint remains unchanged. No winning CLAIM, open run, frozen Result, review or native completion is asserted.
