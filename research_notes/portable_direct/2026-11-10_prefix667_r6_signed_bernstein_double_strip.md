# PREFIX-667-R6 — Signed Bernstein localization doubles the certified BRC variance strip

Date: 2026-11-10 (Asia/Shanghai). Research mode: TASK_RESEARCH, direct independent author derivation; native session registration pending at the first write. Frozen scientific pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Exact model: unchanged 189-layer two-direction first-stop BRC statistical observer from PREFIX-659–666. Status: AUTHOR_PROVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem — 2x extension beyond PREFIX-666

Let \(\mu(p,z)=E[Y]\), \(H(p,z)=E[Y^2]/2\), \(W=2H-\mu^2\), and \(V_q(p,z)=q^2W-q\mu\). In the *continuous* rectangle
\[
0\le p\le\frac1{128},\quad \frac{607}{4096}\le z\le\frac{609}{4096},
\]
we establish the following strict inequalities for every real parameter point:
\[
\boxed{\mu>\frac{438}{5}=87.6,\qquad \mu_{pp}>226,\qquad
H_{pp}<15362,\qquad W_{pp}<-8900.}
\]
Consequently, for **all real** \(12\le q\le24\),
\[
\boxed{(V_q)_{pp}<-8900q^2.}
\]

Combining the already certified PREFIX-660 edge maximum \(z_*(q)\), edge gap \(V_q(0,z_*)-V_q(0,z)\ge 6400000(z-z_*)^2\), and PREFIX-661 strict edge normal slope \((V_q)_p(0,z)<-76650\) on the stated \(z\)-band, the strip has the **unique** maximum \((0,z_*(q))\). Moreover,
\[
\boxed{M_q-V_q(p,z)\ge76650p+4450q^2p^2+6400000(z-z_*(q))^2},
\quad M_q=V_q(0,z_*(q)).
\]
This new strip is twice the area of PREFIX-666 and 32 times that of PREFIX-665 (same \(z\)-band). This theorem concerns the frozen statistical observer; the mother question is its global \([0,1]^2\) variance maximum.

## Mathematical proof and exact finite certificate

Let \(A_n(k)\) count the frozen surviving paths and \(f_n(k)=A_n(k)/\binom nk\in[0,1]\). Write \(s_n(p)=\sum_k A_n(k)p^k(1-p)^{n-k}\), \(t_m(z)=s_m(z)\), and
\[
w_{nm}=2^{-(n+m+1)}\binom{n+m}{n}.
\]
The fixed maximum-of-two-Gamma-clocks formulas from PREFIX-659/665/666 give
\[
\begin{aligned}
a_n(z)&=1-\sum_{m=0}^{188}w_{nm}t_m(z),\\
b_n(z)&=n+1-\sum_{m=0}^{188}\frac{n+m+1}{2}w_{nm}t_m(z),\\
\mu(p,z)&=\sum_{n=0}^{188}a_n(z)s_n(p)+\sum_{m=0}^{188}t_m(z),\\
H(p,z)&=\sum_{n=0}^{188}b_n(z)s_n(p)+\sum_{m=0}^{188}(m+1)t_m(z).
\end{aligned}
\]
All quantities in this certificate are exact rational numbers. The recurrence regenerates every path-count row from the *unchanged* PREFIX-665 frozen predicate.

Put \(Q=19/128\), \(\delta=1/4096\), \(\varepsilon=1/128\), \(R=22\). Differentiate exactly at \(p=0,z=Q\) to obtain the signed jets \(D^{\mu}_r=\partial_p^r\mu(0,Q)\), \(D^H_r=\partial_p^rH(0,Q)\), and their \(z\)-derivatives for \(2\le r\le R\). From
\[
s_n^{(r)}(0)=n^{\underline r}\Delta^r f_n(0),\qquad
|s_n^{(r)}(p)|\le2^{r-1}n^{\underline r},
\]
the signed degree-19 polynomials
\[
P_\mu(p)=\sum_{j=0}^{19}\frac{D^\mu_{j+2}}{j!}p^j,\qquad
P_H(p)=\sum_{j=0}^{19}\frac{D^H_{j+2}}{j!}p^j
\]
enclose the exact second derivatives after adding the explicit order-20 Taylor remainder bounds
\[
R_\mu=\frac{\varepsilon^{20}}{20!}\,2^{21}\sum_{n=22}^{188}n^{\underline{22}},\qquad
R_H=\frac{\varepsilon^{20}}{20!}\,2^{21}\sum_{n=22}^{188}(n+1)n^{\underline{22}}.
\]

**New device:** split \([0,\varepsilon]\) into 16 equal rational subintervals \([u,u+h]\). On each, translate \(P(u+ht)=\sum_{j=0}^{19}c_jt^j\) and use the exact degree-19 Bernstein coefficients
\[
B_k=\sum_{j=0}^{k}\frac{\binom kj}{\binom{19}j}c_j.
\]
The Bernstein convex-hull property bounds the polynomial at *every real* point of that subinterval between \(\min_k B_k\) and \(\max_k B_k\). This preserves the signs of the exact Taylor jets instead of adding their absolute magnitudes and is the improvement over PREFIX-666.

To cover the full \(z\)-band, the score bound \(|t_m'(z)|<21\) for \(m\le188\) gives \(|a'_n|\le21\) and \(|b'_n|\le21(n+1)\). The same signed \(p\)-jets for \(\mu_z,H_z\), their absolute-value Taylor bounds and \(|a_n''|\le2(n+1)(n+2)\), \(|b_n''|\le2(n+1)(n+2)(n+3)\) yield exact explicit \(z\)-error budgets. In particular, set
\[
L_n=\sum_{r=2}^{21}\frac{\varepsilon^{r-2}}{(r-2)!}|s_n^{(r)}(0)|
+\frac{\varepsilon^{20}}{20!}2^{21}n^{\underline{22}},
\]
\[
Z_\mu=\sum_n2(n+1)(n+2)L_n,\qquad
Z_H=\sum_n2(n+1)(n+2)(n+3)L_n.
\]
If \(G_{\mu,z}\) is the Taylor/score bound for \(|\mu_{ppz}(p,Q)|\), then
\[
|\mu_{pp}(p,z)-\mu_{pp}(p,Q)|
\le\delta G_{\mu,z}+\tfrac12\delta^2 Z_\mu,
\]
and likewise for \(H\). The executable companion contains the full exact definitions of both \(G\) quantities and evaluates all interval controls with \`Fraction\`.

The full rational calculation verifies these compact *strict* brackets:
\[
\begin{array}{c|c}
\text{certified envelope}&\text{exact bracket}\\\hline
\text{lower bound for }\mu&87.6<\mu_{\rm low}<87.7\\
\text{lower bound for }\mu_{pp}&226<L_{\mu_{pp}}<227\\
\text{upper bound for }H_{pp}&15361<U_{H_{pp}}<15362\\
\text{upper bound for }W_{pp}&-8994<U_{W_{pp}}<-8993 .
\end{array}
\]
The mean lower bound follows from the exact boundary mean, the uniform edge \(z\)-score bound, and \(\mu_{pp}>0\): \(\mu_p\) is increasing in \(p\), allowing the one-sided integral estimate at \(p=0\). Finally,
\[
W_{pp}=2H_{pp}-2\mu_p^2-2\mu\mu_{pp}
\le2U_{H_{pp}}-2\mu_{\rm low}L_{\mu_{pp}}<-8900.
\]
Therefore \((V_q)_{pp}=q^2W_{pp}-q\mu_{pp}<-8900q^2\). Integrating in \(p\) and combining with the PREFIX-660/661 boundary certificates proves the advertised stability gap and uniqueness.

## Reproducibility, dependencies, and next experiment

Companion code: \`PREFIX667_R6_SIGNED_BERNSTEIN_DOUBLE_CERTIFICATE.py\`. Execute it with Python 3 standard library from \`research_notes/portable_direct/\`; it imports only the *verified frozen predicate* \`PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE.py\` and computes its own 189-layer rows, kernel coefficients, signed Taylor jets, 16-part rational Bernstein bounds and \(z\)-error budgets. Local execution produced \`ALL_CHECKS_PASS 18\`, without floating-point inequality decisions. \`PREFIX667_R6_RESULTS.json\` records the certified envelope brackets and dependency scope. The code prints the exact rational envelope numerators/denominators for full replay.

The analytic edge premises used in the maximum/stability corollary are PREFIX-660 and PREFIX-661; their source scope has not been changed. Independent mathematical review, formal Result/Review, and full-domain global maximum are outstanding.

Next discriminating experiment: use the same interval-centered signed Bernstein jets on \(p\in[1/128,1/64]\), controlling \(\mu_p^2\) and \(\mu_{pp}\) *jointly* instead of separately. For global coverage, compare subtriangle Bernstein upper bounds with the verified \(p=0\) boundary candidate. Preserve the frozen scientific pin and exact owner authorization on any formal task return.
