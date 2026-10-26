# D25/LIFT — Two-stratum harmonic reduction of the corrected-Clausen signed reflection

Date: 2026-10-26. Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` **unchanged**.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** The argument is in an external finite hypergeometric model; it is not a native CM/Frobenius result, formally authorized Source checkpoint, independent review, or proof of D25/LIFT/JT2.

## Source and question

Consume (do not re-credit) the three-channel corrected-Clausen ordered-reflection theorem from \`research_notes/portable_direct/20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md\` at commit \`a4483dc0fb56e7b29f8f85b131e28f08a65ba589\`. The later already-published labelled binomial-fibre tomography and quadratic rank/flux laws are different results; this unit reduces the scalar three-channel Hasse source by precise logarithmic derivatives, keeping its middle single-zero stratum.

For a prime \`p=6m+1>=7\`, work in \`Z_(p)\` and put \`D_n=prod_{i=1}^n(i-p/2)\`. For \`0<=n<p\` all displayed denominators are p-units. Define
\[
u_{k,n}=[t^k]\frac{(-m-t)_n(-2m-2t)_n}{(1-p/2-3t)_n\,n!},
\]
and the original **ordered** reflection
\[
r_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2},\quad
Q_p=\sum_{\substack{0\le a,b<p\\a+b\ge p}}(6(a+b)+1)r_ar_b.
\]
The prior verified theorem provides, using the oriented lower triangle,
\[
\frac{Q_p}{p^2}\equiv\frac{2^{-p}}{18}
\left[T_{02}+p\left(6U_{02}-\frac{T_{12}+T_{03}}6\right)\right]\pmod{p^2},\tag{IN}
\]
where
\[
U_{ab}=\sum_{j=1}^{2m}\sum_{\ell=1}^{j}2^{\ell-j}u_{a,j}u_{b,p-\ell},\qquad
T_{ab}=\sum_{j=1}^{2m}\sum_{\ell=1}^{j}(6(j-\ell)+1)2^{\ell-j}u_{a,j}u_{b,p-\ell}.
\]

## Theorem 1 — explicit zero strata and two logarithmic Hasse laws

For \`1<=j<=m\`, \`m<j<=2m\`, and \`1<=ell<=2m\`, respectively, set the following exact rational principal coefficients:
\[
L_j=\frac{(-m)_j(-2m)_j}{D_j j!},
\quad A_j=(-1)^{m+j+1}\frac{m!(j-m-1)!(2m)!}{(2m-j)!D_jj!},
\]
\[
B_\ell=2(-1)^m
\frac{m!(2m)!(p-\ell-1-m)!(p-\ell-1-2m)!}{(p-\ell)!\,D_{p-\ell}}. \tag{1}
\]
Then \`u_{0,j}=L_j\` for \`j<=m\`; \`u_{0,j}=0,u_{1,j}=A_j\` for \`m<j<=2m\`; and \`u_{0,p-ell}=u_{1,p-ell}=0,u_{2,p-ell}=B_ell\` for \`1<=ell<=2m\`. Each displayed principal coefficient is a p-unit.

Write \`H_0=0\`, \`H_s=sum_{i=1}^s i^{-1}\` in \`F_p\` for \`s<p\`, and
\[
\lambda_j=H_m-H_{m-j}+2H_{2m}-2H_{2m-j}+3H_j,\tag{2}
\]
\[
\Lambda_\ell=H_m+2H_{2m}-H_{m+\ell}-2H_{2m+\ell}+3H_{\ell-1}.\tag{3}
\]
Then
\[
\boxed{u_{1,j}\equiv L_j\lambda_j\pmod p\quad(1\le j\le m),\qquad
u_{3,p-\ell}\equiv B_\ell\Lambda_\ell\pmod p\quad(1\le\ell\le2m).}\tag{4}
\]

**Proof.** For \`n>m\`, \`(-m-t)_n\` has the **literal** zero factor \`-t\` at index \`i=m\`; for \`n>2m\`, the second numerator has the second factor \`-2t\` at \`i=2m\`. Strip each before differentiating. The remaining signed factorials give (1) and the asserted zero orders, over exact rationals. For \`j<=m\`, logarithmic differentiation of the zero-free product gives
\[
\frac{u_{1,j}}{u_{0,j}}=\sum_{i=0}^{j-1}\left(\frac{-1}{i-m}+\frac{-2}{i-2m}\right)+\sum_{i=1}^{j}\frac3{i-p/2}\equiv\lambda_j\pmod p.
\]
For \`n=p-ell>2m\`, differentiate after removing \`(-t)(-2t)=2t^2\` to obtain
\[
\frac{u_{3,n}}{u_{2,n}}\equiv H_m-H_{n-1-m}+2H_{2m}-2H_{n-1-2m}+3H_n\pmod p.
\]
The reflection law \`H_{p-1-a}=H_a (mod p)\`, from \`H_{p-1}=0\` and inverse-pair cancellation, maps the three terminal indices to \`m+ell,2m+ell,ell-1\`, proving (3)-(4). All indices are below \`p\`. QED.

## Theorem 2 — exact scalar four-prefix reduction

Use \`L_j,B_ell\` modulo \`p²\` and \`A_j,lambda_j,Lambda_ell\` modulo \`p\`. Put
\[
f_j=2^{-j}L_j\ (j\le m),\quad a_j=2^{-j}A_j\ (m<j\le2m),\quad
g_\ell=2^\ell B_\ell\ (1\le\ell\le2m).
\]
Define the two precision-\`p²\` and two precision-\`p\` prefix observers
\[
P_j=\sum_{\ell\le j}g_\ell,\qquad Q_j=\sum_{\ell\le j}\ell g_\ell\pmod{p^2},\tag{5}
\]
\[
R_j=\sum_{\ell\le j}\bar g_\ell\Lambda_\ell,\qquad
S_j=\sum_{\ell\le j}\ell\bar g_\ell\Lambda_\ell\pmod p,\tag{6}
\]
bars meaning reduction modulo \`p\`. Set
\[
T=\sum_{j=1}^{m}f_j[(6j+1)P_j-6Q_j],\quad U=\sum_{j=1}^{m}f_jP_j\pmod{p^2},\tag{7}
\]
\[
\begin{aligned}
C_{\rm low}&=\sum_{j=1}^{m}\bar f_j
\{\lambda_j[(6j+1)\bar P_j-6\bar Q_j]+(6j+1)R_j-6S_j\},\\
C_{\rm middle}&=\sum_{j=m+1}^{2m}a_j[(6j+1)\bar P_j-6\bar Q_j],\\
C&=C_{\rm low}+C_{\rm middle}\pmod p.
\end{aligned}\tag{8}
\]
Then
\[
\boxed{\frac{Q_p}{p^2}\equiv\frac{2^{-p}}{18}
\left[T+p\left(6U-\frac C6\right)\right]\pmod{p^2}.}\tag{9}
\]

**Proof.** The first zero stratum has \`u_{0,j}=0\` for \`j>m\`; hence the original \`T_02,U_02\` are exactly (7), preserving the original lower-triangle orientation. In the correction \`T_12\`, the low ranks satisfy \`u_1=u_0 lambda\`, whereas the middle ranks have \`u_0=0,u_1=A\` and therefore **cannot** use that quotient. Independently, the high double-zero stratum gives \`u_3,p-ell ≡u_2,p-ell Lambda_ell (mod p)\` for the \`T_03\` channel. Substitute in the precise signed rank weight \`6(j-ell)+1\` and exchange only the finite \`ell<=j\` sums. This gives \`T_12+T_03≡C_low+C_middle=C (mod p)\`. Insert into (IN); division by 6 is valid at all target primes. QED.

Factorial, shifted-factorial, inverse-factorial, harmonic and power-of-two arrays can be computed in \`O(p)\` finite-ring operations (unit inverses of terminal products suffice); all four prefix moments and the scalar then use \`O(p)\` operations and \`O(p)\` memory. No uniform bit-complexity assertion is implied.

**Strict observer-fibre witness.** In the middle stratum \`u_{0,j}=0\` but \`u_{1,j}=A_j\` is a p-unit. Thus forgetting the middle single-zero source is not an observer-safe compression. At \`p=13\`, original ordered direct arithmetic yields \`Q_13/169=104 mod169\`, with \`T=130,U=138,C_low=1,C_middle=10\` (properly reduced). The same formula after deleting the middle source incorrectly produces **78 mod169**, rather than 104. This falsifies that compression, not the original reflection or native LIFT.

## Actual exact checks, BRC typing, continuation

The accompanying Python standard-library checker builds the **original** ordered \`Q_p mod p^4\` directly from \`r_n\`, independently computes the four-prefix formula, and for smaller primes independently constructs all \`u_{0..3,n}\` by an unspecialized truncated polynomial recurrence. **PASS:** all 80 target primes \`7<=p<=997\` on scalar equality; all 22 target primes \`7<=p<=211\` on each low/middle/high coefficient and mod-\`p\` logarithmic derivative. Examples \`(p,Q_p/p² mod p²,C_middle mod p,wrong omission)\`: \`(7,38,4,10)\`, \`(13,104,10,78)\`, \`(19,221,5,183)\`, \`(31,225,9,907)\`, \`(37,1084,18,973)\`, \`(43,1563,38,1348)\`. These are **author** checks; they do not replace a proof, independent review or a native CM experiment.

**BRC COMPOSE_APPLIED.** The carrier comprises signed p-adic weighted ordered \`(j,ell)\` cells, source stratum, Hasse order and precision. Allowed operations here: cutoff, convolution, reflection, logarithmic-derivative transport and affine oriented rank readout. The compression is certified for the **isolated scalar** \`Q_p/p² mod p²\`; arbitrary future quadratic rank operators need separate labelled rank moments from previously proved binomial-fibre work. Middle source is retained as a structural residual. The auxiliary variable is not an Enterprise native plane or six-axis coordinate.

**Current native read-only control:** own recovery [#6477](https://github.com/awdawmip/kimi-query-bridge/issues/6477) and exact Source continuation [#6478](https://github.com/awdawmip/kimi-query-bridge/issues/6478), complete 36,483-char receipt [#6481](https://github.com/awdawmip/kimi-query-bridge/issues/6481) + [#6482](https://github.com/awdawmip/kimi-query-bridge/issues/6482). Current Researcher \`EM-ENTERPRISE-9C0A7C\`, session \`MCP-22fdc1ed9a2d44d8bcf5fd6b5cf810dd\`; no live claim/authorized run. Exact Task is \`HANDOFF_READY/NEEDS_DISPATCH\`, prior Source checkpoint \`SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED\`, \`execution_authorized=false\`; latest historical claim \`MCP-d0d70cd041b01e5db192870a\` differs from checkpoint predecessor \`MCP-87631b892b41fa18d799f2d8\`, supported by [control issue #1558](https://github.com/awdawmip/enterprise-math/issues/1558). The present portable Git note is **not** Source-native checkpoint, CLAIM, OPEN, Result or review.

**Next independent scientific unit:** transport both mod-\`p\` logarithmic-source recurrences and the separate middle single-zero port through the already established labelled-binomial-fibre finite-boundary flux operator; seek an actual signed WZ/adjoint cancellation with both rank orientations and the infinity correction. Canonical mother objective **OPEN**: obtain real authenticated original-class \`H0/B0\`, divided-power \`[X]U mod p²\`, semilinear Frobenius direction/normalization \`eta\`, \`kappa\` and \`Delta_p-R_p\` comparison. Original native CM experiment \`NOT_RUN\`; independent review still required.
