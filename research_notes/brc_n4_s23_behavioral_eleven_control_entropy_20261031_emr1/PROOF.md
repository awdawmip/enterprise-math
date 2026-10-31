# BRC N=4 / S23 behavioral stopping-time observer: eleven-dimensional policy information-rate theorem

2026-10-31. Portable author-side analytic theorem, independently executable exact-integer checks. Status: **UNREVIEWED / NOT_ADMITTED**. This concerns an external finite positive-probability BRC observer, not physical X6 Cell dynamics, a signed/phase BRC identity, or an S2 theorem.

## Frozen experiment and target

The six latent cells in order are AU0, AU1, AV, BU0, BU1, BV. The six distinct prepared input rows are the stochastic matrix

\[
M={1\over20}
\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]

This is the same strictly positive 16-leaf P/Q source and same law-independent S23 causal grammar as the predecessor. The full S23 timing grammar has **two distinct first-stage A/B controls**, **three distinct second-stage controls U (shared AU/BU), AV, BV**, and **six third-stage controls, one for each latent likelihood-ratio cell**. There are 2+3+6=11 genuine distinct information-set controls. A complete deterministic table has 2^11=2048 choices. Behavioral randomization allows each control probability to vary independently in [0,1].

The public observable is stopping time T in {1,2,3,4} only, omitting terminal decision, BU sensor, and its presence flag. A fixed common source-to-k-state stochastic encoder E is chosen before the policy. At most m fixed decoding kernels D_l are chosen before the policy; the policy may choose a **deterministic** label l based on itself but the decoder cannot read the whole policy, realized coin, source or analog side information. Define

\[
R_{k,m}^{beh}=\inf_{E,D_1,\ldots,D_m}
\sup_{H\in S23_{beh}}\min_{\ell\le m}
\max_{i=1,\ldots,6}\operatorname{TV}
\big(P_i^H(T),(M E D_\ell)_i\big).
\]

The P/Q duplication for AV/BV is suppressed in the six-row representation; keeping both identical rows does not change the maximum. All mixtures are positive probability measures, with no signed cancellation.

## Theorem: the complete lawful behavioral policy family has dimension eleven

For all positive integers k,m, put n = floor(m^(1/11)). Then

\[
\boxed{R_{k,m}^{beh}\ \ge\ {1\over672\,n}.}\tag{A}
\]

For every k>=6,

\[
\boxed{R_{k,m}^{beh}\
\le\min\left\{{3\over4},\
1-\left(1-{1\over2n}\right)^3\right\}.}\tag{B}
\]

Consequently, for **every fixed k>=6**, the exact information-rate exponent of the entire full S23 behavioral timing family under finite fixed policy labels is

\[
\boxed{R_{k,m}^{beh}=\Theta(m^{-1/11})\quad(m\to\infty).}\tag{C}
\]

This improves the previous six-coin subfamily result (whose exponent was 1/6) to the **full eleven-control family**. It does not determine R_(4,10) or R_(6,10): their previously supported interval [1/2,2/3] remains intact. The lower constant in (A) is deliberately elementary, not claimed sharp.

### Exact eleven-parameter causal chart

Write the eleven law-independent behavioral stop parameters as
\[
\theta=(a_A,a_B,b_U,b_{AV},b_{BV},c_{AU0},c_{AU1},c_{AV},c_{BU0},c_{BU1},c_{BV})\in[0,1]^{11}.
\]
For cell x, denote its first-stage class by s(x) in {A,B}, its second-stage class by g(x) in {U,AV,BV}, and its third-stage individual parameter by c_x. Its lawful terminal-time probabilities are
\[
f_x^\theta(1)=a_{s(x)},\quad
f_x^\theta(2)=(1-a_{s(x)})b_{g(x)},\quad
f_x^\theta(3)=(1-a_{s(x)})(1-b_{g(x)})c_x,\quad
f_x^\theta(4)=(1-a_{s(x)})(1-b_{g(x)})(1-c_x).
\tag{1}
\]
Here g(AU0)=g(AU1)=g(BU0)=g(BU1)=U, g(AV)=AV and g(BV)=BV. On prepared input i, the law is (M f^\theta)_i. Every theta is a lawful behavior strategy, including boundary values; no future information is read at an earlier stage.

The matrix is invertible with det M=1/50, and its induced infinity-norm inverse is
\[
M^{-1}=
\begin{pmatrix}
11&-10&0&0&0&0\\
-9&10&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&9/4&-5/4&0\\
0&0&0&-1/4&5/4&0\\
0&0&0&0&0&1
\end{pmatrix},\quad \|M^{-1}\|_{\infty}=21.
\tag{2}
\]
Thus exact prepared output laws determine every latent law f_x. On the interior (0,1)^11 they in turn determine all eleven controls:
\[
a_s=f_x(1),\qquad b_g={f_x(2)\over1-f_x(1)},\qquad
c_x={f_x(3)\over1-f_x(1)-f_x(2)}.
\tag{3}
\]
Choose for a_A,a_B the time-one outputs of AU0 and BU0; for b_U,b_AV,b_BV choose the time-two outputs of AU0,AV,BV; and choose all six latent time-three outputs. The 11-by-11 Jacobian is block-lower-triangular. Its diagonal product, up to variable ordering, is
\[
(1-a_A)^5(1-a_B)^4(1-b_U)^4(1-b_{AV})(1-b_{BV})>0.
\tag{4}
\]
Hence the image in the 18 independent prepared time-probability coordinates is genuinely locally eleven-dimensional (not merely an eleven-parameter redundant representation). This is an auxiliary statistical policy manifold, **not** eleven native space/time dimensions.

### Lower bound: a uniform eleven-dimensional packing obstruction

Restrict all eleven behavioral controls to the smaller legal cube C=[0,1/2]^11. For two theta,theta' in C let
\[
\Delta=\max_{x,\ t=1,2,3}|f_x^\theta(t)-f_x^{\theta'}(t)|.
\]
The inverse formulas (3), denominators 1-a>=1/2 and (1-a)(1-b)>=1/4, and c<=1/2 give the explicit stability inequalities
\[
|a-a'|\le\Delta,\quad |b-b'|\le3\Delta,\quad
|c-c'|\le8\Delta.
\tag{5}
\]
For b: with v=1-f(1), w=f(2), the quotient difference is at most |w-w'|/v+b'|v-v'|/v<=2Delta+Delta. For c: with d=1-f(1)-f(2), z=f(3), it is at most |z-z'|/d+c'|d-d'|/d<=4Delta+4Delta. These are valid for all pairs in C and for each relevant cell/group.

Suppose two policies theta,theta' both use the **same fixed policy label** l and each incur prepared-row TV error <=r. The triangle inequality and singleton events t=1,2,3 imply
\[
\max_{i,t\le3}|(Mf^\theta)_i(t)-(Mf^{\theta'})_i(t)|\le2r.
\]
Multiplying by M inverse using (2) yields Delta<=42r. Equation (5) then implies
\[
\boxed{\|\theta-\theta'\|_\infty\le336r.}\tag{6}
\]
This conclusion holds for **every common randomized encoder, every k and arbitrary randomized label decoders**, since no assumption was made about their internally realizable output centers beyond the same label producing the same six reconstructed rows.

Let n=floor(m^(1/11)). Take the (n+1)^11 distinct legal parameters whose coordinates lie in {0,1/(2n),...,1/2}. Any two are separated in sup norm by at least 1/(2n), while m<(n+1)^11. If r<1/(672n), (6) implies no single label can serve two grid points. But there are more grid points than labels. Therefore no such r is feasible, and taking the infimum proves (A). This is a finite packing argument with a complete analytic counting certificate, not a sample-based universal extrapolation.

### Upper bound: eleven-control quantization with six faithful source states

For k>=6, let the common encoder faithfully retain the six latent cells. Quantize **each of the eleven law-independent behavior parameters** to the nearest center among the n intervals of [0,1]. There are n^11<=m fixed label kernels. For a selected label, the decoder on encoded latent cell x emits the four-time law (1) using the quantized control tuple. The full physical source mixture M is left intact.

Each original/quantized control pair differs by at most e=1/(2n). Couple the two sequential Bernoulli stopping mechanisms at stages 1,2,3 using the same uniform variate at each common reached node. Conditional on the paths still agreeing, the probability of divergence at the current node is <=e (and zero if both paths already stopped). Hence the probability of no divergence through three stages is >=(1-e)^3. By the coupling inequality,
\[
\operatorname{TV}(f_x^\theta,f_x^{\hat\theta})\le1-(1-e)^3.
\]
Convex mixing by each row of M cannot increase this bound, establishing the second term in (B). Independently, one fixed decoder uniform on {1,2,3,4} gives TV<=3/4 on every probability law; this yields the first term. Comparing the matching exponents from (A) and (B) proves (C).

## Exact executed checker, evidence and limitations

VERIFY.js constructs the same M, its fourfold inverse, the 11-slot causal map, and all 2^11=2048 **two-level randomized policy vectors with each coin equal to 1/4 or 1/2**. These 2048 are NOT the 2048 deterministic policy tables from earlier work. Each vector has 6 latent by 4 terminal probabilities; the checker verifies normalization, all 6 prepared mixtures, all 6x4 exact inverse reconstructions, and that all 2048 prepared laws are distinct. It also verifies an independent 11-column full-rank difference certificate modulo 65521 and 1024 pairwise consistency tests for the inequality used above. All arithmetic in the checker is integer (modular arithmetic is exact and used only for a sufficient rank certificate).

The universal real-parameter packing and coupling results are the above analytic proof. Running a finite checker alone would not establish them. The checker does not cover native X6 physics, S2 information-set embedding, signed amplitudes, independently audited mathematics or project admission. This author-side result has no native CLAIM/Result/Review authority.

## Provenance

GLOBAL_KNOWLEDGE_V1 fixed for this work at main@dcffdd3270d839d765c7cab630a66c20afc926c5. Enterprise Math initial pinned canonical main@fd980113f72132edbc47ee27efadf15dd118441c. P000 original V5 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488 (the global startup projection refers to an older blob, so the original was read); ACTIVE worldview, six-axis time/residual contracts, and portable research protocol were consulted. Mathematical predecessor: PR #1757 @e134799cb56541c3fec98bfd5d20ee89ee994e89, whose six-coin entropy lemma was used at its exact restricted scope, not silently generalized.
