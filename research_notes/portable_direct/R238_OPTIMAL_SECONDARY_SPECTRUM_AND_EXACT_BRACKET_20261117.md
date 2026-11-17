# R238 — Exact identity of the second observable spectral radius in the R234 family

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_RATIONAL_CERTIFIED / NOT_REVIEWED**. Native typed BRC integration: **NOT_EXECUTED**.

## Source and setup

Continue R237 at commit 63ba274a136da8f95b330542453a23fc551b79a5; retain R234 family commit 37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6 and original frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Scope: the auxiliary scalar source-support observation of a seven-source stationary reversible sticky-reset Markov model. P000 and native six-axis signed/port/source BRC provenance are unchanged.

For real \(s\in I=(39/100,41/100)\), let
\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\quad
t(s)=\frac{1691s-2615}{2615s-3539},
\]
\[
b_0=13/60,\qquad b_j=\frac5{18}|1/2-\alpha_j|\quad(1\le j\le6).
\]
The 63 killed symmetric blocks are
\(K_D=\mathrm{diag}(\alpha_j)_{j\in D}+(\sqrt{b_i b_j})_{i,j\in D}\),
\(D=\{0\}\cup U\), \(U\subsetneq[6]\). The sole dominant block is \(D_{-3}=\{0,1,2,4,5,6\}\), with Perron root \(r(s)>0.99\) by R235. Its leading amplitude \(A(s)\), the total spectral coefficient \(T(s)\), and the remainder \(R_n(s)\) are defined in R237.

## Theorem — Exact worst subleading block and optimal uniform spectral cutoff

For **every real** \(s\in I\), the **largest** among all scalar-observable eigenvalues *other than* \(r(s)\) is
\[
\boxed{\beta(s)=\lambda_{\max}(K_{D_{-4}}),\qquad
D_{-4}=\{0,1,2,3,5,6\}.}
\]
The root \(\beta(s)\) is strictly increasing in \(s\) and lies in \((49/50,99/100)\). Therefore the **least uniform upper spectral cutoff** over the open parameter interval is
\[
\boxed{\beta_*:=\sup_{s\in I}\beta(s)=\beta(41/100).}
\]
Here the right-hand endpoint value denotes the continuous extension of the rational family and is **uniquely** specified by
\[
\sum_{j\in\{0,1,2,3,5,6\}}
 \frac{b_j(41/100)}{\beta_*-\alpha_j(41/100)}=1,
\quad \beta_*\in(49/50,99/100).
\]
An exact rational isolating certificate is
\[
\boxed{\frac{9847337}{10000000}<\beta_*<
\frac{9847338}{10000000}=:\theta.}
\]
Consequently R237's positive-tail bound tightens, for every integer \(n\ge L\), to
\[
\boxed{0\le R_n(s)\le C(s)\theta^{n-1}.}
\]
Using the independently pinned R236 enclosure \(r(s)>594323/600000\), the relative one-mode bound is
\[
\boxed{\frac{R_n(s)}{A(s)r(s)^{n-1}}
\le\frac{C(s)}{A(s)}
\left(\frac{14771007}{14858075}\right)^{n-1}.}
\]
This cutoff is optimal in the sense of the largest **observable subleading eigenvalue**, not an assertion that the bound \(C(s)\beta_*^{n-1}\) has the sharpest possible coefficient for a specific \(n\).

## Proof

Put \(x\in[49/50,99/100]\), \(c=5/18\) and \(q_j(s,x)=b_j(s)/(x-\alpha_j(s))\). All denominators are positive. The contribution
\[
q_4(s,x)=c\,\frac{1/2-s}{x-s}
\]
decreases strictly in both \(s\) and \(x\), and thus
\[
q_4(s,x)\le q_4(39/100,49/50)=\frac{55}{1062}.
\]
For \(i=1,2,5\), \(q_i(s,x)\) is constant in \(s\) and decreases in \(x\). For \(i=6\), \(t'(s)>0\) and
\[
q_6(s,x)=c\,\frac{t(s)-1/2}{x-t(s)}
\]
increases in \(s\) and decreases in \(x\). Hence the minimum of each \(q_i\), \(i\in\{1,2,5,6\}\), on the closed rectangle occurs at \(x=99/100\) and (where relevant) \(s=39/100\). Their exact margins above \(55/1062\), in that source order, are
\[
\frac{3305}{78588},\quad \frac{2105}{73278},\quad
\frac{9415}{103014},\quad\frac{117124105}{381221538},
\]
each strictly positive. Thus \(q_i(s,x)>q_4(s,x)\) throughout the rectangle.

The single-deletion secular function
\[
f_{-i}(s,x)=\sum_{j\ne i}q_j(s,x)-1
\]
is strictly decreasing in \(x\) above all poles. Only the \(j=6\) summand varies with \(s\) in \(f_{-4}\), and it strictly increases with \(s\). Exact endpoint signs give
\[
f_{-4}(39/100,49/50)=
\frac{74402159402}{14279825475603}>0,
\]
\[
f_{-4}(41/100,99/100)=
-\frac{316533456883}{20880995759343}<0.
\]
Its unique Perron root \(\beta(s)\) therefore lies in \((49/50,99/100)\), depends continuously on \(s\), and is strictly increasing in \(s\).

At \(x=\beta(s)\), \(f_{-4}(s,x)=0\), while for each \(i\in\{1,2,5,6\}\),
\[
f_{-i}(s,\beta(s))=
f_{-4}(s,\beta(s))+q_4(s,\beta(s))-q_i(s,\beta(s))<0.
\]
Their Perron roots are strictly below \(\beta(s)\). All other proper source masks except \(D_{-3}\) are principal submatrices of one of these five single-deletion blocks, so their spectral radii are at most \(\beta(s)\). By rank-one interlacing, the non-Perron eigenvalues of the dominant block \(D_{-3}\) are at most \(t(s)<4/5<\beta(s)\). All killed matrices are positive definite. The \(D_{-4}\) Perron eigenmode has strictly positive scalar-observer coefficient \(W_5(v_{D_{-4}}\cdot u)^2\), so it is actually observable and attains the second largest observable spectral radius. This proves the pointwise identity and optimal supremum.

For the endpoint root, exact rational substitutions give
\[
f_{-4}(41/100,9847337/10000000)
=\frac{3132332617503244758272699544274954183}
{13909144609115584534601759609563113583045817}>0,
\]
\[
f_{-4}(41/100,9847338/10000000)
=-\frac{242915727357910165231220062349242699}
{3549734572987883149627215687627596048242699}<0.
\]
Strict monotonicity gives the stated exact isolating bracket. The nonnegative spectral expansion of R237 supplies the stronger tail inequality with \(\theta\), and
\[
\theta/(594323/600000)=14771007/14858075.
\]
QED.

## Validation and next frontier

The accompanying exact standard-library Fraction script asserts every displayed rational certificate and produces a machine-readable PASS verification record. The continuous-parameter claim is the analytic/secular/interlacing proof above, not an extrapolation from finite samples. No independent mathematical review or native BRC execution took place.

Next: derive a rational parameter-uniform lower bound on the positive leading-amplitude fraction \(A(s)/T(s)\), thereby turning the relative spectral-rate cutoff into an explicit **uniform \(n\)** threshold for any specified relative tolerance. Compare exact arithmetic bit complexity with 230-mode recurrence and 256-state propagation. Build a provenance-faithful, read-only native BRC EffectHistogram observer separately.
