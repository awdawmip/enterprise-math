# R236 — Monotone Perron mode and uniform parametric sensitivity in the R234 230-mode family

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTERVAL_CERTIFIED / NOT_REVIEWED**. Native typed BRC: **NOT_EXECUTED**.

## Frozen scientific context

Continuation of R235 at \`awdawmip/enterprise-math@24f836536351000ec4d044d4c7f7cfae0758c8d1\`; R234 source at \`37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6\`; science frozen at \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. The claim concerns only the exact auxiliary scalar source-support observer of a seven-source stationary sticky-reset Markov chain. The P000 six-dimensional native Cell space, independent time, signed direction, native three-dimensional slice and BRC joint-state provenance remain unchanged.

Use R234's positive rational family for real s in I=(39/100,41/100):
\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\quad
t(s)=\frac{1691s-2615}{2615s-3539},\quad c=5/18,
\]
\[
b_0=13/60,\quad b_i=c|1/2-\alpha_i|\ (1\le i\le6).
\]
By R235 the unique maximal proper killed Perron radius r(s) is the root
\[
f(s,r(s))=0,\qquad
f(s,x)=\sum_{j\ne3}\frac{b_j(s)}{x-\alpha_j(s)}-1,\qquad
99/100<r(s)<991/1000.
\]

## New theorem — Strict monotonicity, Lipschitz bound and improved enclosure

For every real s in I, r(s) is differentiable and
\[
\boxed{0<r'(s)<1/60}.
\]
Consequently r is strictly increasing and for all s,s'∈I,
\[
\boxed{|r(s)-r(s')|<|s-s'|/60\quad(s\ne s')}.
\]
The full-interval enclosure sharpens from R235's (0.990,0.991) to
\[
\boxed{\frac{594323}{600000}<r(s)<\frac{1486309}{1500000}\quad(s\in I)}
\]
(that is, approximately 0.99053833 < r(s) < 0.99087267), with exact rational endpoints.

### Proof: an explicit derivative identity

The only s-dependent secular terms are those indexed 4 and 6:
\[
f(s,x)=\text{constant-in-}s+
c\frac{1/2-s}{x-s}+c\frac{t(s)-1/2}{x-t(s)}.
\]
Thus, setting \(\partial_s f=f_s\),
\[
f_s(s,x)=c(x-1/2)\left(\frac{t'(s)}{(x-t(s))^2}-\frac{1}{(x-s)^2}\right),
\quad t'(s)=\frac{853776}{(2615s-3539)^2}>0.
\]
Direct common-denominator expansion gives
\[
\frac{t'}{(x-t)^2}-\frac1{(x-s)^2}
=\frac{-2615(s-1)(x-1)Q(s,x)}
 {(x-s)^2(2615sx-1691s-3539x+2615)^2},
\]
where
\[
Q(s,x)=2615sx-767s-4463x+2615.
\]
On the rectangle \(s\in I,\ x\in(99/100,991/1000)\), Q increases with s and decreases with x. Its maximal value is
\[
Q(41/100,99/100)=-2112823/2000<0,
\]
and its minimal value is \(Q(39/100,991/1000)=-21925833/20000>-1100\). Since s<1 and x<1, the factored identity has positive right side, hence f_s>0. Moreover
\[
f_x=-\sum_{j\ne3}\frac{b_j}{(x-\alpha_j)^2}<0.
\]
The implicit-function theorem gives \(r'(s)=-f_s/f_x>0\).

### Proof: rational quantitative bound

Exact differentiation gives t'>0 on I. Its endpoint bounds (using t increasing) yield
\[
97/125<t(s)<39/50,\qquad t'(s)<141/1000.
\]
The factorization above, together with \(1-s<61/100,\ 1-x<1/100,\ |Q|<1100\), and
\[
x-s>58/100,\quad
|2615sx-1691s-3539x+2615|
=(3539-2615s)(x-t)
>(3539-2615\cdot41/100)(99/100-39/50),
\]
provides the strict uniform upper bound
\[
0<f_s<c(991/1000-1/2)\,
\frac{2615(61/100)(1/100)1100}
 {(58/100)^2[(3539-2615\cdot41/100)(99/100-39/50)]^2}
=:N.
\]
For the denominator of the implicit derivative, the source-6 contribution alone yields
\[
-f_x>\frac{b_6}{(x-t)^2}>
c\,\frac{97/125-1/2}{(991/1000-97/125)^2}
=:D.
\]
Exact rational arithmetic gives
\[
\frac ND=\frac{995617757646875}{62291552106829941}<\frac1{60}.
\]
Therefore \(0<r'<1/60\). Integrating the bound across any pair s,s'∈I proves the Lipschitz inequality.

At the base s_0=2/5, direct exact rational evaluation of the secular equation gives
\[
f(2/5,990705/1000000)>0,\quad
f(2/5,990706/1000000)<0.
\]
Since |s−2/5|<1/100, the Lipschitz bound yields
\[
990705/1000000-1/6000<r(s)
<990706/1000000+1/6000,
\]
which reduces to the stated pair of rational bounds. QED.

## Reproducibility, evidence and next problem

Run \`R236_uniform_sensitivity_check.py\` beside the pinned \`R235_unique_slowest_source_mode_check.py\` using standard Python. It checks the exact rational boundary inequalities, base root brackets, derivative-factorization identity at nine rational input pairs and the strict upper bound N/D < 1/60. Output in \`R236_verification.json\` is PASS. The continuum result is a direct symbolic proof, supplemented by exact checks. Independent mathematical review NOT_REVIEWED; native BRC EffectHistogram integration NOT_EXECUTED.

Next: obtain sharper near-optimal derivatives from certified interval subdivisions, prove explicit spectral tail constants and determine the number of retained modes needed for a target rational absolute/relative error at fixed n. Compare complete bit costs against exact 230-mode and 256-state propagation. Preserve joint provenance in native BRC work.
