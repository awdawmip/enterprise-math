# PREFIX-1034 — Exact Morse saddle cusps and sharp critical Bernstein scaling for the X6 positive-port contrast

**Date:** 2026-11-23 (Asia/Shanghai). **Parent:** PREFIX-1033.  
**Status:** AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_INTEGER_CROSSCHECK / NOT_REVIEWED.  
**Frozen science:** P000 V5 at \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`; Stage46 candidate signed BRC \`W=J12-6I12\`, incoming \`-e1\`, bidirectionally forbidden Link \`{0,e1}\`, exactly one outgoing negative step and coherent joint Cell–terminal-port–grade square-mass observer. The five-angle Haar model used below is only the already-proved **auxiliary scalar spectral observer**, and is not a replacement for signed/provenance-preserving X6 BRC state.

## Research question and result

PREFIX-1033 established a continuous signed spectral density \(g\) on \([0,36]\), whose nonnegativity is equivalent to all Hausdorff differences \(E_{m,k}\ge0\). Its proof identified the interior Morse critical levels 4 and 16 but did not quantify their local singularities. Here we determine the **exact one-sided cusp coefficients**, and the resulting **sharp \(N^{-1/4}\) bias of normalized Bernstein/Beta probes at those levels**. This is a local structural result, not a proof of \(g\ge0\).

Write \(Y=|z_1+\cdots+z_6|^2\), with independent Haar phases, \(\rho\) its probability density, and (from PREFIX-1033)
\[
 g(y)=\frac{4(H\rho)'(y)-2P(y)\rho(y)+12(11+y)F(y)}5,\qquad
 H=y^2(36-y)^2,\quad P=y(y-36)(17y-91),\quad
 F(y)=\int_y^{36}(6-t)\rho(t)\,dt.
\]
The support is \([0,36]\); \(\nu[f]=\int f(y)g(y)\,dy\), and \(E_{m,k}=\nu[y^m(36-y)^k]\).

### Theorem 1 — exact local singular parts

There exist smooth functions \(R_4,R_{16}\) in neighborhoods of their indicated levels, with differentiable remainders, such that as \(y\to v\),
\[
\boxed{\rho(y)=R_4(y)-\frac{5}{32\pi^3}(4-y)_+^{3/2}
       +O(|y-4|^{5/2})\quad(v=4),}
\]
\[
\boxed{\rho(y)=R_{16}(y)+\frac{1}{64\pi^3}(y-16)_+^{3/2}
       +O(|y-16|^{5/2})\quad(v=16).}
\]
The \(O\)-terms describe the singular part after subtraction of the smooth background; their first derivatives are \(O(|y-v|^{3/2})\). The formulas are invariant under the choice of local Morse coordinates and sum **all** critical points at each value. Here \(x_+=\max(x,0)\).

It follows that there are smooth functions \(G_4,G_{16}\) in the same neighborhoods for which
\[
\boxed{g(y)=G_4(y)+\frac{3072}{\pi^3}(4-y)_+^{1/2}
                    +O(|y-4|^{3/2}),}
\]
\[
\boxed{g(y)=G_{16}(y)+\frac{1920}{\pi^3}(y-16)_+^{1/2}
                    +O(|y-16|^{3/2}).}
\]
In particular \(g\) is locally \(C^{0,1/2}\), and is **not locally Lipschitz** at either Morse level:
\[
g'(y)\sim-\frac{1536}{\pi^3\sqrt{4-y}}\quad(y\uparrow4),\qquad
g'(y)\sim+\frac{960}{\pi^3\sqrt{y-16}}\quad(y\downarrow16).
\]
The displayed asymptotic derivatives include bounded smooth-background contributions, which are negligible against the displayed divergent terms. Thus any proof relying on a global finite Lipschitz constant for this particular \(g\) requires repair; PREFIX-1030 stated its Lipschitz error bound conditionally and did not assert that hypothesis.

**Proof.** Remove global phase by fixing \(z_6=1\), and write \(z_j=e^{i\theta_j}\) for \(1\le j\le5\). At an isolated nonzero stationary point, \(z_j=\varepsilon_j\in\{\pm1\}\); put \(s=1+\sum_{j=1}^5\varepsilon_j\ne0\). The Hessian is exactly
\[
{\cal H}_{jk}=2(\varepsilon_j\varepsilon_k-s\delta_{jk}\varepsilon_j),\qquad
|\det{\cal H}|=32s^4.
\]
The exact nonzero critical-point strata, including all choices of \(\varepsilon\), are:
\[
\begin{array}{c|c|c|c}
Y=s^2&\#\text{ points}&\text{Morse negative index}&|\det{\cal H}|\\
4&15&3&512\\16&6&4&8192\\36&1&5&41472
\end{array}
\]
These integers were independently checked by exact symbolic Hessian eigenvalue/inertia and determinant enumeration; the independent executable reproduction is \`PREFIX1034_R6_MORSE_EXACT_CHECK.py\`.

At \(Y=4\), the Morse normal form has two positive and three negative quadratic directions. In the normalized quadratic coordinates, radial integration against \(\delta(t-(|u|^2-|w|^2)/2)\) has singular part
\(-\frac{16\sqrt2\pi^2}{3}(-t)_+^{3/2}\).
At \(Y=16\), one positive and four negative directions produce
\(+\frac{16\sqrt2\pi^2}{3}(t)_+^{3/2}\).
Multiplying by Haar normalization \((2\pi)^{-5}\), the inverse-square-root Hessian determinant and the counts 15/6 gives respectively
\[
-\frac{15}{3\sqrt2\pi^3\sqrt{512}}(4-y)_+^{3/2}
=-\frac5{32\pi^3}(4-y)_+^{3/2},
\quad
+\frac6{3\sqrt2\pi^3\sqrt{8192}}(y-16)_+^{3/2}
=+\frac1{64\pi^3}(y-16)_+^{3/2}.
\]
The Morse lemma and smooth angularized amplitude yield a smooth regular background and a higher-order singular expansion in half-integer powers. The noncritical region contributes a smooth density, as in PREFIX-1033. Differentiating the singular parts once is valid. In the formula for \(g\), only \(4H\rho'/5\) contributes at exponent \(1/2\); the terms \(H'\rho,P\rho\) contribute at exponent \(3/2\), and the integrated term \(F\) at exponent \(5/2\). Since \(H(4)=16384\) and \(H(16)=102400\),
\[
\frac65H(4)\frac5{32\pi^3}=\frac{3072}{\pi^3},
\qquad
\frac65H(16)\frac1{64\pi^3}=\frac{1920}{\pi^3}.
\]
Both coefficients are nonzero and positive. The derivative assertions follow. QED.

### Theorem 2 — sharp critical Beta/Bernstein scale

Let \(v\in\{4,16\}\). For positive integers \(N\) divisible by \(9\), put \(m=Nv/36\), \(k=N-m\), and
\[
D_{m,k}=\frac{(N+1)\binom Nm}{36^{N+1}}E_{m,k}
       =\mathbb E[g(36T)],\quad T\sim\mathrm{Beta}(m+1,k+1).
\]
Then
\[
\boxed{
\lim_{\substack{N\to\infty\\9\mid N}}
N^{1/4}\big(D_{N/9,8N/9}-g(4)\big)
=\frac{6144\,\Gamma(3/4)}{\pi^{7/2}}>0,
}
\]
\[
\boxed{
\lim_{\substack{N\to\infty\\9\mid N}}
N^{1/4}\big(D_{4N/9,5N/9}-g(16)\big)
=\frac{1920\,2^{3/4}5^{1/4}\Gamma(3/4)}{\pi^{7/2}}>0.
}
\]
The same limits hold if \(m\) is rounded to the nearest integer to \(Nv/36\). In particular, the \(O(N^{-1/4})\) uniform approximation rate near the critical levels **cannot be improved to** \(o(N^{-1/4})\) for the frozen scalar observer.

**Proof.** The exact beta representation is PREFIX-1033 Theorem B. For fixed \(v\), the beta central limit theorem gives
\(\sqrt N(36T-v)\Rightarrow \sigma_v Z\) with \(Z\) standard normal and \(\sigma_v^2=v(36-v)\). The beta second-moment bound gives uniform integrability for the positive-part square-root. The smooth \(G_v\) contribution differs from \(G_v(v)\) by \(O(N^{-1/2})\), and the higher singular remainders have expectation \(O(N^{-3/4})\) after restricting to a fixed local neighborhood (outside it the beta tail is exponentially small). Thus
\[
N^{1/4}(D_{m,k}-g(v))
\to A_v\sqrt{\sigma_v}\,\mathbb E[(Z_+)^{1/2}],
\quad
\mathbb E[(Z_+)^{1/2}]
=\frac{2^{-3/4}\Gamma(3/4)}{\sqrt\pi},
\]
where \(A_4=3072/\pi^3\), \(A_{16}=1920/\pi^3\), \(\sigma_4=8\sqrt2\), \(\sigma_{16}=8\sqrt5\). By symmetry of the normal, the left-sided cusp at 4 has the same positive-part expectation. Simplifying gives the two constants. QED.

A consequence relevant for interval certification is that on any compact interior spectral interval, \(g\) is \(1/2\)-Hölder (smooth away from 4 and 16); its beta-probe convergence is therefore \(O(N^{-1/4})\) locally uniformly. The upper bound may be made effective once a concrete Hölder constant is certified. An assumed global Lipschitz constant would give a misleading faster rate at the saddle points.

## Local exact validation and numerical diagnostic

1. Exact SymPy enumeration of all \(2^5\) sign patterns with \(s\ne0\): stationary multiplicities 15/6/1, Morse indices 3/4/5, determinant magnitudes 512/8192/41472, and the four \(\pi^{-3}\)-normalized density/cusp coefficients above. **PASS**; script saved alongside this paper.
2. Using the already published PREFIX-1030 recurrence for exact six-phase collision moments \(A_6(r)\), the PREFIX-1016 rational three-shift contrast formula, exact-integer difference recursion \(E_{m,k+1}=36E_{m,k}-E_{m+1,k}\), and an exact rational normalization, the critical probes were independently evaluated without floating-point arithmetic in the sign computation. The displayed decimals were converted only after forming \`Fraction\` values:

| \(N\) | \(D_{N/9,8N/9}\) at \(y=4\) | \(D_{4N/9,5N/9}\) at \(y=16\) |
|---:|---:|---:|
| 72 | 140.707048229177 | 61.394177127729 |
| 144 | 139.982025611135 | 55.456044040411 |
| 288 | 138.605844753500 | 50.101673990836 |
| 576 | 136.730258484880 | 45.498583136025 |
| 1152 | 134.558060462450 | 41.633092650672 |
| 2304 | 132.287643348048 | 38.420302627817 |

All 12 sampled \(E_{m,k}\) are positive integers. This finite calculation is a diagnostic of the already established observer, not a numerical proof of the new asymptotic constants. The constants are approximately \(136.9968079314\) and \(107.6652287830\) for the \(N^{-1/4}\) bias. The full \(N\le5000\) positive triangle is inherited from PREFIX-1030; it was **not re-enumerated** in this run.

## Scope, unresolved questions, continuation

Theorems 1–2 depend on the inherited PREFIX-1033 global density/regularity theorem and on the specified **six-phase** frozen observer; author proof, not independent project review. They identify explicit non-Lipschitz saddles and quantitative sampling bias, not positivity of \(g(4)\), \(g(16)\) or \(g\) on the three open spectral bands. Next derive rigorous values or lower bounds for \(g(4),g(16)\) and a certified \(C^{0,1/2}\) modulus away from the endpoints; combine with adaptive beta probes to prove positive intervals or exhibit an exact negative witness. The mother problem \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\) remains open.

Provenance: previous series PREFIX-1016, 1026, 1030, 1031, 1032, 1033, all under their original frozen assumptions. Historical researcher \`EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056\`, SID \`MCP-45ad6d29cd534c1aad25595a72e3c532\` retained as attribution, not as a fresh session/CLAIM. Current portable research has no formal Task/CLAIM/PROGRESS/Result/Review or Activity promotion inferred from this paper.
