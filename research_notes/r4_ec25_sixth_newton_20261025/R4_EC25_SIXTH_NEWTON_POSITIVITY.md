# R4-EC25 — Sixth-highest Newton coefficient: positivity for all grades

2026-10-25 · **Author-side exact algebraic proof and exact integer cross-check; no independent Driver review or native mathematical admission.**

## Scope, identity and fixed sources

Positive-weight ordered binary affine **auxiliary BRC** clean-source kernel only (no P000 X6 Cell or heartbeat-time dynamical transfer). P000 original blob SHA1 \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` matched global startup projection at \`GLOBAL_KNOWLEDGE_V1 main@76b5a9dadb9d5bed132f8c101d9d3232dffb0171\`; ACTIVE worldview and observer/provenance rules loaded. EM portable protocol and project routing read at \`enterprise-math main@0a807eb162573e056297ef91313f4534ef895d10\`. Scientific predecessor: [EC24 author proof](https://github.com/awdawmip/enterprise-math/blob/90e8c0ca377ef9f3b5b537109410035fb8845366/research_notes/r4_ec24_fifth_newton_20261025/R4_EC24_FIFTH_NEWTON_POSITIVITY.md). Authenticated connected GitHub user \`awdawmip\`; native task/Owner query \`CONTROL_QUOTA\`, active Owner/CLAIM not verified. Current site gateway \`static_machine_readonly\`, write relay disabled. Researcher local identifier is not service-issued authority.

## Definitions and theorem

Set
\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},\qquad f_j(n)=E[n,j]-E[n,j-1].
\]
The exact auxiliary-kernel Newton transform (EC20/EC24) is
\[
q_d(j)=\Delta^{j-d}f_j(2j+6)=[z^jt^d]H(z,t),\quad
H(z,t)=\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
\]

**Theorem:** for every integer \(c\ge5\), \(r\in\{0,1,2\}\), put \(d=3c+r\), \(v=c-5\). Then
\[
\boxed{[w^{c-5}]q_{3c+r}(3c+r+w)
=\frac{L_r(c)}{(c-5)!}>0.}
\]
Here \(L_r(v+5)\) is the exact rational polynomial specified below: its integer numerator coefficients are in descending degree order, divided by the indicated positive denominator. All 51 numerator coefficients are **strictly positive**, proving positivity for every \(v\ge0\).

**r=0**, degree 15, positive denominator **163459296000**:

`4096, 614400, 40983040, 1608821760, 41540017792, 748564776960, 9768785174720, 94648173185280, 691769604053528, 3839317562960880, 16110560542896365, 50233196898876810, 112384359608725359, 169151736435756210, 150986983410597600, 58477399684704000`

**r=1**, degree 16, positive denominator **81729648000**:

`256, 43008, 3243520, 145474560, 4340644672, 91479862656, 1413349171520, 16413401484480, 145689730224038, 997452396204264, 5271772389099125, 21325026708768510, 64697421158022384, 141854758681900572, 210441929514326685, 186020687214724950, 71630724044880000`

**r=2**, degree 17, positive denominator **1389404016000**:

`512, 95744, 8103424, 411568640, 14042030464, 341861356928, 6165359214768, 84469183942000, 894435854948636, 7398168454288612, 47992729160074517, 243407047380672175, 954091741091389363, 2826283293223047516, 6087272383737303066, 8914472552159596485, 7810640648831213550, 2991859243813440000`

## Exact finite symbolic proof

Write \(z=1-y\) and define
\[
\begin{aligned}
N_0&=(1+t)^6(1-t)(1-t(1+t)^2),\\
N_1&=(1+t)^6\{t(1-t(1+t)^2)+t(1+t)^2(1-t)\},\\
N_2&=t^2(1+t)^8,\\
Q_0&=1-2t,\quad Q_1=2t-t^2,\quad Q_2=t^2.
\end{aligned}
\]
Direct polynomial expansion proves numerator \(H(1-y,t)=N_0+yN_1+y^2N_2\) and denominator \(H(1-y,t)=y(Q_0+yQ_1+y^2Q_2)-t^3(1-y)^3\). Therefore the formal \(t\)-adic expansion is
\[
H(1-y,t)=\sum_{k\ge0}
\frac{t^{3k}(1-y)^{3k}(N_0+yN_1+y^2N_2)}
{y^{k+1}(Q_0+yQ_1+y^2Q_2)^{k+1}}. \tag{1}
\]
For \(0\le h\le5\), its Laurent coefficient in \([t^{3c+r}]\) is the following *finite* expression:
\[
R_h(c,r)=\sum_{\ell=0}^{h}[t^{r+3\ell}y^{h-\ell}]
\frac{(1-y)^{3(c-\ell)}(N_0+yN_1+y^2N_2)}
{(Q_0+yQ_1+y^2Q_2)^{c-\ell+1}}. \tag{2}
\]
Each term is explicitly computable over \(\mathbb Q(c)\): expand to \(y\)-order at most 5, and use \([t^m](1-2t)^{-p}=2^m(p)_m/m!\).

The proven numerator recurrence for \(H\) gives \([t^d]H(z,t)=P_d(z)/(1-z)^{c+1}\) and \(\deg P_d\le d+c-1\) for \(d=3c+r\). Any polynomial part of its partial-fraction expression has degree at most \(d-2\), so it cannot contribute to \([z^{d+w}]\) for \(w\ge0\). Coefficient extraction from (1) hence yields
\[
q_d(d+w)=\sum_{h=0}^{c}R_h(c,r){d+w+c-h\choose c-h}. \tag{3}
\]
Let \(e_m\) be the elementary symmetric polynomial, \(e_0=1\), and \((a)_{\underline m}\) the falling factorial. Since terms \(h\ge6\) have degree at most \(c-6\) in \(w\),
\[
\boxed{L_r(c)=\sum_{h=0}^{5}R_h(c,r)
\frac{e_{5-h}(d+1,\ldots,d+c-h)}{(c-h)_{\underline{5-h}}}.} \tag{4}
\]
Compute \(e_1,\ldots,e_5\) by the exact Newton relations \(m e_m=\sum_{i=1}^{m}(-1)^{i-1}e_{m-i}S_i\), where \(S_i=\sum_{j=1}^{c-h}(d+j)^i\) are exact Faulhaber polynomials. Substitution of (2) into (4), rational cancellation and \(c=v+5\) give **exactly** the three polynomials listed above. Positivity of every rational coefficient with \(v\ge0\) completes the all-grade proof; no interpolation or finite numerical extrapolation is used.

## Independent integer evidence

An independent \(d\)-first exact integer recurrence starts with \(a=\lfloor d/3\rfloor\) and
\[
\begin{aligned}
P_d(z)={}&(1-z)^a\left({6\choose d}
-z\left[{6\choose d-1}+{8\choose d-1}\right]
+z^2{8\choose d-2}\right)\\
&+2z(1-z)^{a-\lfloor(d-1)/3\rfloor}P_{d-1}(z)
+z(1-z)^{a+1-\lfloor(d-2)/3\rfloor}P_{d-2}(z)
+z^3P_{d-3}(z),
\end{aligned}
\]
with absent negative-index terms. Compute \(q_d(d+w)=[z^{d+w}]P_d(z)(1-z)^{-a-1}\) and recover \([w^{c-5}]\) by forward differences and signed Stirling numbers. All **54 cases** \(5\le c\le22\), \(r=0,1,2\) matched exact rational certificates.

A second, \(z\)-first **independent coefficient propagation** from \(H=N/D\), with \(A_n(t)=[z^n]H(z,t)\), obeys
\[
A_n=(1+t)^2A_{n-1}-2t(1+t)A_{n-2}+t^2(1+t)A_{n-3}+N_n,
\]
where \(N_0=(1+t)^6\), \(N_1=-(1+t)^6t(1+(1+t)^2)\), \(N_2=t^2(1+t)^8\), \(N_n=0\) for \(n\ge3\). Comparing \([t^d]A_{d+w}\) with the \(d\)-first recurrence produced **783 exact integer matches**. At the minimum \(c=5\), the coefficients are **357749, 876435, 2153340** for \(r=0,1,2\).

Source checks: proof is symbolic under the **auxiliary model**. The integer tests check implementation over declared finite ranges, not universal truth. No native P000 X6 arithmetic, heartbeat physical time trajectory, independent Driver review, signed cancellation, Source-issued research session or formal mathematical acceptance is claimed.

## Outcome and next unit

**REUSE_APPLIED** to existing positive BRC clean-provenance kernel and EC20/21/24 coefficient tools. Sixth-highest (thus top six, combined with earlier author results) is positive in the stated domain. Open: all lower Newton coefficients, near-center \(f_j(2j+s)\ge0\) for \(s=0,\ldots,5\), native X6/temporal attribution and formal independent admission. **R4-EC26:** find a uniform all-order positivity invariant, or a certified first negative shifted coefficient; do not keep raising the proved order without a uniform argument.
