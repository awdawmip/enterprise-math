# R749SMI — Exact Blackwell gap for all non-deterministic A-feedback noise

Date: 2026-11-13 (Asia/Shanghai). Author-side continuation of R749SMG/R749SMH. Scientific input remains frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Predecessor proofs: R749SMG at \`07988762499e4897cc0458c2c8f2b0578da5a973\`; R749SMH at \`bbc89c4e1903eafa4c173647fce8b0f25b5f7974\`.

**Scope.** A finite three-historical-sign conditional observer, not a native V29/V39-authorized Cell/Link/Port event. P000 and the original scientific pin are unchanged.

## Statement

Write source \(z=(x,y,t)\in\{\pm1\}^3\), observed word \(o=(u,v,w)\in\{\pm1\}^3\), \(z_+=y,z_-=t\), and
\(\alpha=1-2\varepsilon_A,\ \beta=1-2\varepsilon_B,\ \gamma=1-2\varepsilon_C\).
The feedback-before-query and output-postprocessing experiments are the column-stochastic kernels
\[
F_{uvw,xyz}=\frac{(2+\alpha ux)(2+\beta vz_u)(2+\gamma wyt)}{64},
\]
\[
P_{uvw,xyz}=\frac{2+\gamma wyt}{128}
  \sum_{i=\pm1}(2+ix)(1+\alpha ui)(2+\beta vz_i).
\]
A Blackwell garbling \(K\to L\) means a single source-independent column-stochastic matrix \(G\) such that \(L=GK\).

**Theorem.** For every \(0<\varepsilon_A<1\), every \(\varepsilon_B\ne1/2\) and every \(\varepsilon_C\in[0,1]\), the experiments \(P\) and \(F\) are Blackwell-incomparable. Moreover, their worst-source total-variation simulation deficiencies satisfy
\[
\boxed{\delta(P\to F)\ge |\beta|(1-|\alpha|)/16>0},
\quad
\boxed{\delta(F\to P)\ge |\beta|(1-|\alpha|)/32>0},
\]
where \(\delta(K\to L)=\inf_{G\ {\rm stochastic}}\max_z
 {\rm TV}(L_{\cdot z},(GK)_{\cdot z})\).
These are lower bounds, not claims of optimal deficiency.

## Proof: two opposing strictly-positive-prior contrasts

Choose
\[
\mu_Y(x,y,t)=(1+y/2)/8,\quad
\mu_T(x,y,t)=(1+t/2)/8,
\]
\[
\pi_\pm(x,y,t)=(1\pm x(y-t)/4)/8.
\]
All four priors sum to one and assign each source atom at least \(1/16\).
Expanding the kernels in the finite Walsh basis and summing over the eight source states gives the exact signed output contrasts:
\[
\begin{aligned}
(F\mu_Y-F\mu_T)_{uvw}&=uv\beta(1-w\gamma/2)/32,\\
(P\mu_Y-P\mu_T)_{uvw}&=uv\alpha\beta(1-w\gamma/2)/32,\\
(F\pi_+-F\pi_-)_{uvw}&=v\alpha\beta(1-w\gamma/2)/64,\\
(P\pi_+-P\pi_-)_{uvw}&=v\beta(1-w\gamma/2)/64.
\end{aligned}
\]
For direct algebraic checking, the only nonzero Walsh contrasts contributing to the first pair are
\(\mathbb E_{\mu_Y-\mu_T}Y=1/2,\ \mathbb E_{\mu_Y-\mu_T}T=-1/2\);
those contributing to the second pair are
\(\mathbb E_{\pi_+-\pi_-}XY=1/2,\ \mathbb E_{\pi_+-\pi_-}XT=-1/2\).
These identities and the displayed kernel definitions imply every signed-output formula without a numerical approximation.

Because \(|\gamma|\le1\), the factor \(1-w\gamma/2\) is strictly positive. Summing the eight absolute word differences and dividing by two gives
\[
\begin{array}{ll}
{\rm TV}(F\mu_Y,F\mu_T)=|\beta|/8,&
{\rm TV}(P\mu_Y,P\mu_T)=|\alpha\beta|/8,\\
{\rm TV}(F\pi_+,F\pi_-)=|\alpha\beta|/16,&
{\rm TV}(P\pi_+,P\pi_-)=|\beta|/16.
\end{array}
\]
For \(|\alpha|<1,\beta\ne0\), the first pair has strictly larger TV under feedback; the second has strictly larger TV under postprocessing. Any source-independent stochastic garbling contracts total variation for *every* pair of source priors, so neither experiment garbles the other.

If a garbling approximates \(L\) from \(K\) with worst-source TV error \(\eta\), for arbitrary source priors \(\rho,\sigma\) the triangle inequality and convexity imply
\[
{\rm TV}(L\rho,L\sigma)\le {\rm TV}(K\rho,K\sigma)+2\eta.
\]
Apply this to the \(\mu_Y,\mu_T\) pair with \(K=P,L=F\), and the \(\pi_+,\pi_-\) pair with \(K=F,L=P\), and take infima over stochastic \(G\). This yields the two stated lower bounds. QED.

## Parameter boundaries and observer meaning

The strict theorem covers the entire stochastic A-flip interior \(0<\varepsilon_A<1\), including R749SMH's exactly random A channel \(\varepsilon_A=1/2\). If \(\varepsilon_A=0\), the internal selector and observed A agree, so \(F=P\). If \(\varepsilon_B=1/2\), the B-output is independent of the selected port and again \(F=P\). The deterministic complement case \(\varepsilon_A=1,\varepsilon_B\ne1/2\) remains to be separately classified.

C-output noise may take any value on its full parameter interval: the \(\gamma\)-dependence vanishes from the four TV totals. Thus a total branch mass or equal matrix rank cannot itself encode the ordering of noise relative to named-port selection. This is a precise BRC provenance/observer distinction within the declared finite model.

## Verification and next question

An independently written standard-library Python \`Fraction\` check executed \`PASS\` on the five-value parameter grid \(\alpha,\beta,\gamma\in\{-1,-1/2,0,1/2,1\}\): 125 triples, 1000 source columns per kernel, nonnegative column-stochastic kernels, four normalized strictly positive priors, and all four total-variation identities. Companion checker and result JSON are in this directory. The all-real theorem is the above algebraic proof; the grid is a regression check.

Next: the \(\varepsilon_A=1\) deterministic-complement boundary, followed by exact Walsh predictive closure for controllers that use multiple noisy public bits as memory. Separately obtain an actually permitted V29/V39 triadic event before attempting a native Cell/Link/Port correspondence. Independent review and shared-CLAIM admission are not asserted.
