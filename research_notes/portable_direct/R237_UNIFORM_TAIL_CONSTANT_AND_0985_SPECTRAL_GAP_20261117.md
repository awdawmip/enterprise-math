# R237 — Uniform 0.985 spectral-tail bound for the R234 sticky-reset family

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_RATIONAL_CERTIFIED / NOT_REVIEWED**. Native typed BRC: **NOT_EXECUTED**.

## Frozen scientific provenance and scope

Source family: R234 at commit 37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6; unique Perron bottleneck and rate bound: R235/R236 at commit 2bb1983d60bbd3312662e8a52b7df065e03e2ef6. Frozen scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This result is for the derived **scalar source-support observer** of a seven-source finite Markov chain. P000, the six-axis native X6 world, independent time and signed/port/provenance-carrying native BRC structures retain their original types.

For real \(s\in I=(39/100,41/100)\), define
\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t),\quad
t(s)=\frac{1691s-2615}{2615s-3539},\quad c=\frac5{18},
\]
\[
b_0=13/60,\quad b_i=c|1/2-\alpha_i|\ (1\le i\le6),\quad
\pi_i=\frac{b_i}{1-\alpha_i},\quad
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j.
\]
The R234 normalization gives \(\sum_i\pi_i=1\). The stationary vector is
\[
Z=\sum_{j=0}^6\frac{b_j}{(1-\alpha_j)^2},\qquad
\rho_i=\frac{b_i}{(1-\alpha_i)^2Z}.
\]
For proper \(U\subsetneq[6]\), put \(D_U=\{0\}\cup U\),
\(K_D=\mathrm{diag}(\alpha_j)_{j\in D}+a_Da_D^\top\),
\(a_j=\sqrt{b_j}\), \(v_D=(\sqrt{\rho_j})_{j\in D}\).
For R215/R220 positive source-support ideal weights \(W_0,\ldots,W_6\), the R235 expectation law for integers \(n\ge L\) is
\[
\Phi_n(s):=\mathbb E[F_n]-W_6
=\sum_{U\subsetneq[6]}W_{|U|}\,v_{D_U}^\top K_{D_U}^{n-1}v_{D_U}.
\]

## Theorem (uniform separation and effective tail)

Let \(D_*=\{0,1,2,4,5,6\}\), let \(r(s)\) be its unique positive Perron root, and put
\(\sigma=197/200=0.985\). For **every real \(s\in I\)**, including all exceptional spectral-collision parameters, every eigenvalue of each of the other **62** proper-mask blocks and every non-Perron eigenvalue of \(K_{D_*}\) lies in \([0,\sigma)\). Also \(r(s)>99/100>\sigma\).

The positive Perron amplitude has the exact one-root formula
\[
\boxed{
A(s)=\frac{W_5}{Z}
 \frac{\left(\sum_{j\ne3}\frac{b_j}{(1-\alpha_j)(r-\alpha_j)}\right)^2}
 {\sum_{j\ne3}\frac{b_j}{(r-\alpha_j)^2}}>0.}
\]
Let
\[
\Gamma_0=\sum_{u=0}^5\binom6uW_u,\quad
\Gamma_1=\sum_{u=1}^5\binom5{u-1}W_u,\quad
T(s)=\rho_0\Gamma_0+(1-\rho_0)\Gamma_1,\quad
C(s)=T(s)-A(s)>0.
\]
Then for **every integer \(n\ge L\)**,
\[
\boxed{
\Phi_n(s)=A(s)r(s)^{n-1}+R_n(s),\qquad
0\le R_n(s)\le C(s)\left(\frac{197}{200}\right)^{n-1}.}
\]
By the sharper R236 root enclosure \(r(s)>594323/600000\), the relative error also satisfies
\[
\boxed{\frac{R_n(s)}{A(s)r(s)^{n-1}}
\le \frac{C(s)}{A(s)}
\left(\frac{591000}{594323}\right)^{n-1}.}
\]
Consequently the second spectral radius is uniformly at most \(0.985\), with gap \(r(s)-\sigma>3323/600000\). The coefficient and error envelope are computable from one one-dimensional secular root, the original weights and seven rational functions of \(s\); no 230-dimensional matrix is needed.

## Proof of the uniform spectral bound

Fix \(x=197/200\) and define \(q_j(s)=b_j/(x-\alpha_j)\). All holding parameters are \(<4/5<x\). The single-deletion block \(D_{-i}=\{0,\ldots,6\}\setminus\{i\}\) has secular function
\[
f_{-i}(x,s)=\sum_{j\ne i}q_j(s)-1.
\]
For \(x\) above all holding poles it is strictly decreasing in \(x\), and its unique zero is the largest killed-block eigenvalue.

At fixed \(x\), the only variable term in \(f_{-4}\) is \(q_6=c(t-1/2)/(x-t)\). Since
\[
t'(s)=\frac{853776}{(2615s-3539)^2}>0,\qquad
\frac{\partial}{\partial t}\frac{c(t-1/2)}{x-t}
=\frac{c(x-1/2)}{(x-t)^2}>0,
\]
\(f_{-4}(x,s)\) strictly increases in \(s\). Exact endpoint evaluation yields
\[
\boxed{f_{-4}(x,41/100)=
-\frac{34189956955753}{43781593262648493}<0.}
\]
The contribution \(q_4(s)=c(1/2-s)/(x-s)\) strictly decreases with \(s\), hence
\[
q_4(s)\le q_4(39/100)=55/1071.
\]
For \(i=1,2,5\) the \(q_i\) are constant; \(q_6\) increases in \(s\). Their exact lower margins above \(55/1071\), in order \(i=1,2,5,6\), are
\[
970/22491,\quad 485/16303,\quad
6415/68187,\quad 712475045/2252753181,
\]
all positive. Therefore \(q_i(s)>q_4(s)\) for \(i=1,2,5,6\), giving
\(f_{-i}(x,s)<f_{-4}(x,s)<0\) for those \(i\); the \(i=4\) case is already negative. Thus all five deletion-block Perron roots with \(i\in\{1,2,4,5,6\}\) are strictly less than \(x\).

Any proper \(D_U\ne D_*\) lies inside at least one of these five deletion blocks. Principal-submatrix eigenvalue monotonicity bounds its largest eigenvalue by \(x\). For \(D_*\) itself, the rank-one interlacing theorem bounds its second eigenvalue by
\[
\max_{j\ne3}\alpha_j=t(s)
\le t(41/100)=192169/246685<4/5<x.
\]
Each block is positive definite because \(\alpha_j>0\) and \(a_Da_D^\top\succeq0\); every eigenvalue is nonnegative. R235 proves the unique top eigenvalue \(r(s)>99/100\), while R236 sharpens its lower bound. This proves the spectral assertions.

## Proof of amplitude and remainder

The Perron unit eigenvector of \(K_{D_*}\) is proportional to
\(a_j/(r-\alpha_j)\), for \(j\ne3\), by the rank-one secular equation. Because
\(v_ja_j=b_j/((1-\alpha_j)\sqrt Z)\), its squared overlap with \(v_{D_*}\), multiplied by \(W_5\), is the displayed \(A(s)\).

The spectral theorem gives the nonnegative decomposition
\[
v_D^\top K_D^{n-1}v_D
=\sum_\ell (v_D\cdot u_{D,\ell})^2\lambda_{D,\ell}^{n-1}
\quad(n\ge1).
\]
The sum of **all** scalar spectral coefficients is exactly
\[
\sum_{U\subsetneq[6]}W_{|U|}\|v_{D_U}\|^2
=\rho_0\Gamma_0+(1-\rho_0)\Gamma_1=T(s);
\]
this counts proper masks containing source \(0\), or any fixed nonneutral source, respectively. Only \(A(s)\) corresponds to the unique eigenvalue above \(\sigma\). The remaining coefficient sum is \(C(s)=T(s)-A(s)>0\). Bounding each remaining eigenvalue by \(\sigma\) gives the stated absolute and relative error inequalities. QED.

## Exact validation and next frontier

Companion Python checker uses only standard-library Fraction operations; its JSON reports PASS for the exact endpoint rational identity, four positive margins, stationary normalization, 62-mask containment and three rational configurations \(s=39/100,2/5,41/100\). The general real-interval conclusion rests on the symbolic monotonicity, secular equation and rank-one interlacing proof; finite samples are auxiliary checks. Independent mathematical review is NOT_REVIEWED; no native BRC EffectHistogram operation was run.

Next: sharpen the competing \(D_{-4}\) Perron-root upper enclosure with exact rational isolating bounds; certify an explicit uniform lower bound for \(A(s)/T(s)\) to obtain a parameter-independent truncation horizon; compare end-to-end bit complexity against 230-mode recurrence and 256-state propagation, and separately build a read-only provenance-faithful native BRC observer retaining signed direction, port, source, exact weights, multiplicity and cross moments.
