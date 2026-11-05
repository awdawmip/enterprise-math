# D25 / LIFT — upper first-jet and reversed-shell reciprocal transport

**2026-11-05 · TASK_RESEARCH author-side exact algebra · UNREVIEWED / NOT_ADMITTED**

Source task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Immutable scientific input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. The original scalar mother objective is \(\Delta_p-R_p=0\bmod p\) for \(p\equiv13,19\bmod24\), while original native fixed-class p=373 H0/B0 remains NOT_RUN, tracked by #1559. This note is a portable author-side mathematical computation, not native Source execution or an H0/B0 surrogate.

## 1. Precise question and prior inputs

Use the existing exact centered parameter construction for every prime \(p=6n+1\ge7\), \(N=3n\), \(K=2n\):
\[
f_k(\epsilon)=\frac{(-N+\epsilon/2)_k(-K+\epsilon/3)_k(-4n+2\epsilon/3)_k}{(k!)^3}
=w_k+\epsilon v_k+\epsilon^2u_k+\cdots.
\]
Set \(P(X,\epsilon)=\prod_{\alpha\in\{(-N,1/2),(-K,1/3),(-4n,2/3)\}}(X+\alpha_1+\alpha_2\epsilon)=P_0+\epsilon P_1+\epsilon^2P_2+\cdots\). The exact coefficient recurrence is
\[
k^3(w_k,v_k,u_k)=\big(P_0w_{k-1},\;P_0v_{k-1}+P_1w_{k-1},\;P_0u_{k-1}+P_1v_{k-1}+P_2w_{k-1}\big)\big|_{X=k-1}.
\]
The preceding proven shell and endpoint laws are used at their original scope:
\[
T_A=-2U_p(3\theta+2)G_n(1/2),\quad
U_p=\frac{n^2v_N}{2^{N+2}(N+1)^3},\qquad
G_n(t)=\sum_{j=0}^{n-1}g_jt^j,\quad
g_j=\frac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3}
\quad(\bmod p).
\]
The prior exact third-digit input is \(D_{\rm center}+S_2+T_A\), where \(S_2=\sum_{k=0}^N (6k+1)2^{-k}u_k\).

## 2. New coefficientwise reciprocity theorem

For \(0\le j\le n-1\), write
\[
A_j=\frac{(1/2)_j^3}{j!(5/6)_j(7/6)_j},\qquad
\mathfrak h_j=\sum_{r=0}^{j-1}\left[\frac1{2(r+1)}+\frac1{3(r+7/6)}+\frac2{3(r+5/6)}\right].
\]
All displayed denominators are units mod \(p=6n+1\). Then
\[
\boxed{\frac{v_{N-j}}{v_N}=A_j,\qquad A_jg_j=(2j+1)^{-3}\quad\text{in }\mathbb F_p.}\tag{A}
\]
In particular, \(v_{K+1},\ldots,v_N\) and \(v_N\) are nonzero. With \(r_N=u_N/v_N\), the second-jet observer has the exact simultaneous transport
\[
\boxed{\frac{u_{N-j}}{v_{N-j}}=r_N+\mathfrak h_j\quad\text{in }\mathbb F_p.}\tag{B}
\]
Together (A)–(B) give
\[
u_{N-j}=v_N A_j(r_N+\mathfrak h_j).
\]
**Proof.** The parameter polynomial has \(P_0(K)=0\), \(P_1(K)=2n^2/3\). Hence \(w_k=0\) for \(k>K\), \(v_{K+1}=P_1(K)w_K/(K+1)^3\ne0\), and for \(K+1<k\le N\)
\[
v_k/v_{k-1}=P_0(k-1)/k^3,\qquad
u_k/v_k-u_{k-1}/v_{k-1}=P_1(k-1)/P_0(k-1).
\]
For \(k=N-j\), the reverse first-jet ratio is
\[
\frac{v_{N-j-1}}{v_{N-j}}
=\frac{(N-j)^3}{(j+1)(n-j-1)(n+j+1)}
\equiv\frac{(j+1/2)^3}{(j+1)(j+7/6)(j+5/6)}
\pmod p.
\]
Its product gives \(A_j\), and multiplying by the inherited \(g_j\) yields
\((1/2)_j^3/(3/2)_j^3=(2j+1)^{-3}\). Furthermore,
\[
\frac{P_1(N-j-1)}{P_0(N-j-1)}
=-\frac1{2(j+1)}+\frac1{3(n-j-1)}-\frac2{3(n+j+1)}
\equiv-\frac1{2(j+1)}-\frac1{3(j+7/6)}-\frac2{3(j+5/6)}.
\]
Reverse summation from \(N\) to \(N-j\) establishes (B). These are finite exact recurrences; no numerical inference is used. \(\square\)

## 3. New joint upper-jet/shell formula, preserving original signs

Write \(S_{2,\rm upper}=\sum_{k=K+1}^N(6k+1)2^{-k}u_k\) and \(S_{2,\rm lower}=\sum_{k=0}^K(6k+1)2^{-k}u_k\). From the theorem:
\[
S_{2,\rm upper}
=\frac{v_N}{2^N}\sum_{j=0}^{n-1}(6(N-j)+1)2^j A_j(r_N+\mathfrak h_j).
\]
By the previously proved signed shell/terminal formula and \(6N+1=3p-2\), \(N+1\equiv1/2\), \(n\equiv-1/6\bmod p\), one obtains
\[
\boxed{S_{2,\rm upper}+T_A=\frac{v_N}{2^N}\mathcal J_n\pmod p,}\tag{C}
\]
where the **dimensionless signed terminal observer** is
\[
\boxed{\mathcal J_n=
-2\sum_{j=0}^{n-1}(3j+1)\,2^jA_j(r_N+\mathfrak h_j)
-\frac19\sum_{j=0}^{n-1}(3j+2)\,2^{-j}g_j.}\tag{D}
\]
The coefficients form a reciprocal pair \(A_jg_j=(2j+1)^{-3}\); the first sum retains the signed first/second-jet information, and the second retains the original nonzero \(216\)-shell. This is an exact finite-field reduction with one terminal pair \((v_N,r_N)\) in place of independently carrying the entire upper jet and shell arrays. It does **not** assert \(\mathcal J_n=0\).

The still-open all-target identity is now the two-block statement
\[
\boxed{D_{\rm center}+S_{2,\rm lower}+\frac{v_N}{2^N}\mathcal J_n=0\pmod p, \qquad p\equiv13,19\bmod24.}\tag{E}
\]
Equation (E) uses the previously established exact original third-digit interface; it is not a new independent claim that the original \(\Delta-R\) scalar and \(W-p\) are interchangeable without the frozen source port.

## 4. Exact executed checks and source separation

The checked standard-Python implementation \`d25_upper_jet_shell_reciprocity_checker_20261105.py\` constructs the three parameter coefficient jets from their original recurrence modulo \(p\); independently constructs \(g_j\) and the generalized harmonic sum; tests (A), (B), (C) **for every j** and all 611 primes \(7\le p\le10000,\ p\equiv1\bmod6\). Failures: zero.

At \(p=373\), original arithmetic yields \(v_N=371\), \(u_N=31\), \(r_N=171\), \(S_{2,\rm lower}=82\), \(S_{2,\rm upper}=158\), \(S_2=240\), \(U_p=83\), \(T_A=266\), and \(S_{2,\rm upper}+T_A=51\) mod 373. At \(j=1\), \(A_1=144\), \(g_1=229\), their product is \(152=27^{-1}\), and \(\mathfrak h_1=284\) modulo 373. All figures use integer residues in \([0,p-1]\).

**BRC observer audit:** finite weighted coefficient carrier \((w_k,v_k,u_k)\), distinct \(K\) and \(N\) boundary sources, signed weights, mod-\(p\) readout, and invertible upper-jet/shell reciprocal map retained. Classification: COMPOSE_APPLIED (original residual observer and reversed shell). The current native H0/B0 module/Frobenius, semilinear direction, \(\eta,\kappa\), and signed odd Green/Hesse observer are separate raw evidence requirements. They remain NOT_RUN/PENDING_OWNER under #1559.

**Next smallest mathematical action:** Analyze whether (D) admits a finite \(\!p\)-dependent adjoint pairing with the **lower block** \(D_{\rm center}+S_{2,\rm lower}\), preserving the boundary and signs. Also pursue the original-class native p373 experiment via the already-open capability ticket #1559 without treating these ordinary hypergeometric checks as its execution.

**Control provenance:** logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`; maintenance lane excluded. Previous own Source session \`MCP-491afa3ba2b94ec9b900ed3df6e345a3\` is a historical registered source, with no accessible session key in this run. No own native CLAIM/run/Source checkpoint, freeze or review asserted. Formal status UNREVIEWED / NOT_ADMITTED.
