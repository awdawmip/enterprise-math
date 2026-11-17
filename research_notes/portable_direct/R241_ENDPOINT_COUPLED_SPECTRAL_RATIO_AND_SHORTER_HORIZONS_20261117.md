# R241 — Endpoint-coupled spectral ratio and shorter uniform horizons

2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED.

## Scientific inputs and scope

This is independent portable continuation of the stationary seven-source reversible sticky-reset *scalar* source-support principal-ideal-cardinality observer. Frozen original scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immutable dependencies: R234@37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6 (family), R236@2bb1983d60bbd3312662e8a52b7df065e03e2ef6 (derivative), R238@f052feb457712a8f621e9111404e7da69a542196 (second root), R240@9b817400bb9e3a4286ba68958ea9c1a6a95cf763 (amplitude).

For real \(39/100<s<41/100\), define
\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\quad t(s)=\frac{1691s-2615}{2615s-3539},
\]
\[
b_0=13/60,\qquad b_j=(5/18)|1/2-\alpha_j|\ (1\le j\le6),\quad \pi_j=b_j/(1-\alpha_j).
\]
The stochastic chain has \(P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j\) and \(\sum\pi_j=1\). Let \(r(s)\) be the Perron eigenvalue of the killed block omitting source 3 and \(\beta(s)\) of that omitting source 4. R237–R240 give for integer \(n\ge2\)
\[
\Phi_n=\mathbb E[F_n]-W_6=A(s)r(s)^{n-1}+R_n(s),\quad
0\le R_n(s)\le (T(s)-A(s))\beta(s)^{n-1}.
\]
Here \(A>0\) and \(T\) is the sum of nonconstant positive spectral weights. This is a derived scalar observer: native P000 X6 spatial axes, separate time, signed BRC ports, sources, provenance, multiplicity, rational weights and cross moments remain independent, untouched typed data.

## Theorem 1: pointwise second-to-first Perron ratio strictly increases

For every real \(s\in I=(39/100,41/100)\),
\[
\boxed{\frac{d}{ds}\frac{\beta(s)}{r(s)}>0},\quad
\boxed{\sup_{s\in I}\frac{\beta(s)}{r(s)}
=\frac{\beta(41/100)}{r(41/100)}
<q_{241}=\frac{1641223}{1651305}}.
\]
The endpoint is the continuous family extension; the ratio constant improves the earlier separated-extrema bound \(14771007/14858075\).

**Proof.** R238 shows \(49/50<\beta<99/100\) and \(3/4<t<4/5\). For \(D=\{0,1,2,3,5,6\}\), define the strictly decreasing secular function
\[
f_{-4}(s,x)=\sum_{j\in D}\frac{b_j}{x-\alpha_j}-1,\quad
Q_\beta=\sum_{j\in D}\frac{b_j}{(\beta-\alpha_j)^2}.
\]
Only the \(j=6\) contribution varies in \(s\), and implicit differentiation gives
\[
\beta'=\frac{(5/18)t'(s)(\beta-1/2)}{(\beta-t)^2Q_\beta},\quad
t'(s)=\frac{853776}{(2615s-3539)^2}.
\]
This last function increases on \(I\), with left-endpoint value \(341510400/2538446689>13/100\). Further \(\beta-1/2>12/25\), \(0<\beta-t<6/25\), and the positive secular weights \(b_j/(\beta-\alpha_j)\) sum to 1. Therefore
\[
Q_\beta
<(\beta-\max_{j\in D}\alpha_j)^{-1}
<50/9,
\]
so
\[
\boxed{\beta'(s)>
\frac5{18}\frac{13}{100}\frac{12}{25}
\left(\frac{25}{6}\right)^2\frac9{50}
=\frac{13}{240}}.
\]
R236 proves \(0<r'<1/60\), \(r>99/100\). Since \(\beta<1\),
\[
(\log(\beta/r))'=\beta'/\beta-r'/r
>13/240-5/297>0.
\]
At the upper endpoint, exact fraction calculations establish
\[
f_{-4}(41/100,9847338/10^7)=
-\frac{242915727357910165231220062349242699}
{3549734572987883149627215687627596048242699}<0,
\]
\[
f_{-3}(41/100,990783/10^6)=
\frac{112072487204099343594283677439981}
{438555730828095144535515566369513660019}>0.
\]
Both secular functions decrease with \(x\) above their poles, so \(\beta(41/100)<9847338/10^7\), \(r(41/100)>990783/10^6\). Their quotient yields \(q_{241}=1641223/1651305\). QED.

## Theorem 2: improved uniform spectral amplitude and strict integer horizons

Set
\[
\boxed{\eta_{241}=\frac{1042768025600}{8424836672439}}.
\]
For every real \(s\in I\) and integer \(n\ge2\),
\[
\frac{A(s)}{T(s)}>\eta_{241},\qquad
\boxed{0\le\frac{R_n(s)}{A(s)r(s)^{n-1}}
<\frac{1-\eta_{241}}{\eta_{241}}
\left(\frac{1641223}{1651305}\right)^{n-1}}.
\]
The first integers certified by this strict majorant are **1073 for relative error below 1%**, and **1449 for relative error below 0.1%**. These sufficient thresholds improve R240's 1118/1510 by 45/61 events.

**Proof.** R240's increasing normalizer is
\[
Z(s)=5(4538s-7153)/(16632(s-1)),\quad
Z(s)>Z(39/100)=122345/46116.
\]
R240's Kantorovich argument, with \(z_3=50/1089\), \(a=65/192\), \(W_5=86400\), \(\Gamma_1=655776\), and \(\Gamma_0-\Gamma_1=233424\), gives
\[
\frac{A}{T}\ge
\frac{86400(1680/1681)(Z-z_3)}{655776 Z+233424a}.
\]
The right side strictly increases in \(Z\) because its numerator-derivative cross-product is proportional to \(655776z_3+233424a>0\). Exact insertion of the endpoint \(Z\) gives \(\eta_{241}\). Theorem 1 and the nonnegative spectral expansion give the relative remainder bound. With reduced \(\eta=N/D\), \(q=u/v\), crossing strictly below \(1/d\) is equivalent to the exact integer comparison \(d(D-N)u^{n-1}<Nv^{n-1}\). This first holds at \(n=1073\) for \(d=100\), and \(n=1449\) for \(d=1000\), fails at each predecessor, and remains true for all higher \(n\) since \(0<q<1\). QED.

## Reproduction, review and continuation

The accompanying standard-library Python Fraction checker was actually run. Its JSON evidence has result PASS, with two exact secular signs, exact derivative/normalization bounds, rational eta/q, and the threshold and immediate-predecessor cross-products. The all-real-parameter conclusion is the symbolic argument plus exact pinned earlier results, not extrapolation from tests. Independent mathematical review: NOT_REVIEWED. Native BRC EffectHistogram operation: NOT_EXECUTED. Formal Task CLAIM/Result/Review not asserted.

Next: certify *actual* one-mode horizons rather than sufficient majorant horizons using positive spectral weights and rigorous interval subdivision of \(s\); compare exact bit complexity of two-root evaluation, 230-order recurrence and 256-state propagation. A native BRC observer requires a joint sign/port/source/provenance/multiplicity/weight/cross-moment certificate before any state collapse.
