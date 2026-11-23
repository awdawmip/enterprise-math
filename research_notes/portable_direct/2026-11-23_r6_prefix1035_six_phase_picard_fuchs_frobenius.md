# PREFIX-1035 — All-order six-phase collision recurrence and an exact spectral Picard–Fuchs equation

Date: 2026-11-23 Asia/Shanghai. Parent: PREFIX-1034. Status: AUTHOR_EXACT_PROOF / EXACT_SYMBOLIC_CROSSCHECK / NOT_REVIEWED.

## Frozen object and actual new content

Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5). The Stage46 candidate signed BRC W=J12-6I12, incoming -e1, bidirectionally excluded Link {0,e1}, exactly one outgoing negative step, and coherent X6 Cell–terminal-port–grade square-mass observer remain unchanged. The six-phase Haar model is only the already-derived scalar spectral observer, not a replacement for native signed/provenance-preserving X6 states.

PREFIX-1030 used a sixth-label moment recurrence for exact calculations. PREFIX-1034 established Morse cusp terms in a signed contrast density g. This result supplies (A) a self-contained *all-index* proof of the moment recurrence; (B) a fifth-order differential equation satisfied globally by the compactly supported spectral distribution; and (C) exact local indicial exponents at the four spectral critical levels.

## Theorem A. All-index integer recurrence

For r >= 0, define
\[
A_r=\sum_{k_1+\cdots+k_6=r}\binom{r}{k_1,\ldots,k_6}^{2}
=\int_0^{36} y^r\,d\mu(y).
\]
Then A_0=1, A_1=6, A_2=66, and for all integers r >= 2,
\[
\begin{aligned}
(r+1)^5 A_{r+1}={}&
2(2r+1)(14r^4+28r^3+28r^2+14r+3)A_r\\
&-4r^3(196r^2+59)A_{r-1}\\
&+1152(2r-1)r^2(r-1)^2 A_{r-2}. \tag{A}
\end{aligned}
\]
For r=0,1, terms with unavailable negative indices carry zero prefactors and are omitted.

**Proof.** Define the formal power series
\[
f(z)=\sum_{j\ge0}z^j/(j!)^2,\quad F(z)=f(z)^6
=\sum_{r\ge0} A_r z^r/(r!)^2,\quad T=z\,d/dz.
\]
Coefficientwise, z f''+f'=f. For V_j=f^{6-j}(f')^j, j=0,...,6, with omitted out-of-range terms, differentiation yields the exact seven relations
\[
TV_j=z(6-j)V_{j+1}+jV_{j-1}-jV_j. \tag{A1}
\]
Repeated application of (A1) to F=V_0 establishes the finite polynomial identity
\[
\begin{aligned}
0=\mathcal P F,\quad \mathcal P={}&T^7
-2z(2T+1)(14T^4+28T^3+28T^2+14T+3)\\
&+4z^2(T+1)(196(T+1)^2+59)-1152z^3(2T+3). \tag{A2}
\end{aligned}
\]
Indeed the coefficients of each of V_0,...,V_6 separately vanish as polynomials in z; the accompanying independent symbolic script checks all seven identities exactly. Comparing coefficients of z^{r+1} in (A2) and multiplying by (r!)^2 gives (A), including its low-index boundaries. This is an all-order formal-series proof, not extrapolation from finite tested values. QED.

## Theorem B. Distributional fifth-order equation

Let \(\mu\) be the compactly supported six-phase spectral probability measure on \([0,36]\), interpreted as a distribution on the entire real line; set \(\theta=y\partial_y\). Then
\[
\boxed{\mathscr L\mu=0} \tag{B}
\]
in the distributional sense, for the exact polynomial-coefficient operator
\[
\begin{aligned}
\mathscr L={}&-y^3(\theta+1)^5\\
&+2y^2(2\theta+1)(14\theta^4+28\theta^3+28\theta^2+14\theta+3)\\
&-4y\theta^3(196\theta^2+59)
+1152\theta^2(\theta-1)^2(2\theta-1). \tag{B1}
\end{aligned}
\]
The theta-polynomials act before multiplication by the displayed powers of y.

**Proof.** In (A), put r=n+2, and write the resulting identity as a sum of four terms R_j(n) A_{n+j}=0, indexed j=0,1,2,3, for every n>=0. For compactly supported distributions,
\[
\langle y^n,y^j Q_j(\theta)\mu\rangle
=Q_j(-n-j-1)A_{n+j}.
\]
Choosing Q_j(u)=R_j(-u-j-1) and simplifying yields (B1), so every polynomial moment of \(\mathscr L\mu\) is zero. Its Fourier transform is entire because it is compactly supported. Every Taylor coefficient vanishes, whence the transform and the original distribution are zero. This proves (B) without dropping possible endpoint distribution terms. On each smooth open spectral band, (B1) becomes an ordinary fifth-order linear ODE for the density \(\rho\). QED.

## Theorem C. Exact polynomial singular locus and Frobenius exponents

Writing the scalar-density ODE as a sum of \(a_j(y)\rho^{(j)}(y)=0\) gives
\[
\boxed{a_5(y)=-y^5(y-4)(y-16)(y-36),}
\]
\[
\boxed{a_4(y)=-5y^4(3y^3-140y^2+1568y-3456).} \tag{C}
\]
Thus the finite singular points are precisely 0,4,16,36. At each c in {4,16,36}, the zero of a_5 is simple and
\(a_4(c)/a_5'(c)=5/2\). The local indicial equation
\[
\lambda(\lambda-1)(\lambda-2)(\lambda-3)
[a_5'(c)(\lambda-4)+a_4(c)]=0
\]
has roots \(\{0,1,3/2,2,3\}\). At y=0 the Euler-leading term is \(1152\theta^2(\theta-1)^2(2\theta-1)\), with exponents \(\{0,0,1/2,1,1\}\). This independently matches the \(3/2\) Morse saddle exponent found in PREFIX-1034, while the equation alone does not identify a particular solution's cusp coefficient or rule out logarithmic solutions.

Together with the inherited signed contrast observer,
\[
5g=4(H\rho)'-2P\rho+12(11+y)U,\quad
H=y^2(36-y)^2,\quad P=y(y-36)(17y-91),
\]
and \(U(y)=\int_y^{36}(6-t)\rho(t)dt\), so \(U'=(y-6)\rho\), this yields a six-component first-order system with rational polynomial coefficients on every open spectral band. This is a finite-dimensional route for later rigorous interval enclosures of g.

## Exact verification and evidence limits

- PREFIX1035_R6_A6_ALL_ORDER_RECURRENCE_PROOF.py: the seven components of \(\mathcal P F\) in the basis \(V_0,\ldots,V_6\) are exactly zero polynomials. Local SymPy execution PASSED; this finite symbolic identity proves the recurrence for all indices.
- PREFIX1035_R6_SPECTRAL_PICARD_FUCHS_CHECK.py: independently derives the adjoint operator, factors the top two ODE coefficients, and checks the nonzero-level indicial exponent \(3/2\) at 4,16,36 using exact rationals. Direct six-label collision summation for A_0 through A_12 agrees with the recurrence; 13 corresponding shifted identities are checked. Local execution PASSED.
- No fresh native Stage46 BRC propagation or numerical proof of g(y)>=0 was performed. Formal task Result, independent review and theorem promotion remain unclaimed.

## Next discrimination

Construct rational interval enclosures for the actual signed density g separately on (0,4), (4,16) and (16,36), using B1 and U'=(y-6)rho, with Frobenius matching near 4 and 16. A certified negative interval yields a counterexample to infinite Hausdorff positivity; certified positive coverage would prove it. The mother question B_fix,odd(32) in {19,20} remains open.

Historical contributor: EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056; prior SID MCP-45ad6d29cd534c1aad25595a72e3c532 (provenance, not fresh authorization). Reuse source: PREFIX-1016, PREFIX-1030, PREFIX-1033 and PREFIX-1034. Source publication, Activity association, formal CLAIM/PROGRESS/Result and Review have distinct statuses.
