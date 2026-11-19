# EC49FUE-S — Exact composite minimax at 17 trials and one rational detector width

Date: 2026-11-20. Status: **AUTHOR_PROVED / EXACT_INTEGER_POLYNOMIAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**. Scientific source and model are those of EC49FUD and the companion EC49FUE finite counterexample; frozen BRC16943 parent remains @fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This extension **strengthens** that counterexample to an exact solution of a special full half-line composite minimax problem.

## Exact setting and new theorem

Use the inherited one-sided price-clipping hypotheses and Bernoulli detector:
\[
E=\frac{1048576}{18958647},\
m=\frac{1469}{64},\
L=\frac{951}{1280},\
U=\frac34,\
W=\frac9{1280},\
x=\frac5{123},\
\delta=xW=\frac3{10496},\
n=17.
\]
The **same unknown finite real** \(e\le E\) governs both hypotheses and all 17 conditionally independent observations. Let \(p_e,r_e\) and \(q_e\) be defined exactly in EC49FUE; \(K=\sum Y_i\), and
\[
a_{e,k}=\Pr_{+,e}(K=k)-\Pr_{-,e}(K=k),\qquad
D_j(e)=\sum_{k=j}^{17}a_{e,k}.
\]
Subscript \(\infty\) denotes the *limit* as \(e\to-\infty\), not an additional admissible finite parameter. This limit exists and is rational.

Define two rational numbers from endpoint and limiting signed masses:
\[
t_*=\frac{a_{E,3}}{a_{E,3}-a_{\infty,3}},\qquad
\gamma_*=\frac{D_4(\infty)-D_4(E)}
                 {a_{E,3}-a_{\infty,3}}.
\]
Exact arithmetic proves \(0<t_*<1\), \(0<\gamma_*<1\); numerically \(t_*\approx0.008387657712098784\) and \(\gamma_*\approx0.9972465569727403\).

**Theorem (complete real half-line, exact rational saddle):**
Among all randomized tests of the *ordered* 17 Bernoulli observations, the minimax test is
\[
\boxed{
\Pr(\hbox{decide }H_+\mid K=k)=
\begin{cases}
0,&k\le2,\\
\gamma_*,&k=3,\\
1,&k\ge4.
\end{cases}}
\]
Its exact worst-case equal-prior risk is the rational number
\[
\boxed{
R_{17}^{\rm mm}(5/123)
=\frac{1-D_4(E)-\gamma_*a_{E,3}}2
\approx0.015229738902018461.}
\]
The worst risk is attained at finite \(e=E\) and approached as \(e\to-\infty\); every intermediate finite \(e<E\) has strictly smaller risk under this rule. In particular
\[
R_{17}^{\rm mm}(5/123)
-R_{17}^{\rm Bayes}(E,5/123)
=\frac{(1-\gamma_*)a_{E,3}}2>0
\quad(\approx2.7715964834\cdot10^{-7}).
\]

## Proof: lower bound by an exact limiting nuisance mixture

The signed masses satisfy, by finite exact binomial evaluation:
\[
a_{E,k}<0\ (k\le2),\quad a_{E,k}>0\ (k\ge3),
\]
\[
a_{\infty,k}<0\ (k\le3),\quad a_{\infty,k}>0\ (k\ge4).
\]
The limiting two-point common-nuisance prior places masses \(1-t_*\) at \(E\) and \(t_*\) at \(\infty\). Since
\[
(1-t_*)a_{E,3}+t_*a_{\infty,3}=0,
\]
its Bayes test is \(K\ge4\), with arbitrary randomization at \(K=3\); the mixed signs are negative below 3 and positive above 3. The mixed Bayes risk is \(R_*=(1-\bar D)/2\), where
\[
\bar D=(1-t_*)D_4(E)+t_*D_4(\infty).
\]
The definition of \(\gamma_*\) gives
\[
D_4(E)+\gamma_*a_{E,3}
=D_4(\infty)+\gamma_*a_{\infty,3}
=\bar D.
\]
For any test, its worst-case risk over finite \(e\le E\) dominates the limiting mixture's Bayes risk by continuity; the common nuisance is mixed *once* and the resulting observations are a mixture of binomials, not a binomial of averaged success probabilities. Exchangeability permits symmetrization of ordered-sequence tests. Hence \(R_{17}^{\rm mm}\ge(1-\bar D)/2\).

## Proof: all-real-parameter exact polynomial upper certificate

Put \(s=E-e\ge0\), and define the rational linear polynomials
\[
a=m(L+U)/2,\qquad c=m(U-xW/2),
\]
\[
A(s)=1-Ea+as,\quad P(s)=x(1-Ec+cs),
\]
\[
B(s)=2630615040-45529434409E+45529434409s,
\]
\[
Q(s)=575(2359296-41217719E+41217719s).
\]
All \(A,B\) coefficients are strictly positive. Then
\[
p_{E-s}=P/A,\quad q_{E-s}=Q/B,\quad
r_{E-s}=(PB+QA-PQ)/(AB).
\]
Let \(\mathcal T_\gamma(y)=\sum_{k=4}^{17}\binom{17}{k}y^k(1-y)^{17-k}
+\gamma\binom{17}{3}y^3(1-y)^{14}\).
The test's signed advantage is
\(D_{\gamma_*}(E-s)=\mathcal T_{\gamma_*}(r_{E-s})-\mathcal T_{\gamma_*}(p_{E-s})\).

The accompanying **standard-library-only exact integer certificate** clears the positive rational denominators of \(A,P\) jointly and of \(B,Q\) jointly, writes \(\gamma_*=g_n/g_d\), \(d_0=D_{\gamma_*}(E)=d_n/d_d\), and constructs
\[
H(s)=d_d\{G(R,AB)-G(P,A)B^{17}\}
       -d_ng_d(AB)^{17},
\]
where here \(A,P,B,Q\) are the jointly scaled **integer** polynomials,
\(R=PB+QA-PQ\), and
\[
G(J,V)=g_d\sum_{k=4}^{17}\binom{17}{k}J^k(V-J)^{17-k}
+g_n\binom{17}{3}J^3(V-J)^{14}.
\]
The code computes every integer coefficient (no floating comparisons) and certifies:
\[
\boxed{\deg H=33,\quad H(0)=0,\quad [s^j]H(s)>0\
\text{for every }j=1,2,\ldots,33.}
\]
Therefore
\[
D_{\gamma_*}(E-s)-d_0
=\frac{H(s)}{d_dg_d(AB)^{17}}>0\quad(s>0).
\]
It follows that the test's risk at every finite \(e<E\) is **strictly below** its risk at \(E\); at the limiting endpoint the advantage tends to \(d_0\), by the exact definition of \(\gamma_*\). This supplies the matching minimax upper bound and proves the theorem.

## Reproducibility and epistemic scope

Companion: EC49FUE_SHARP_17_TRIAL_CERTIFICATE.py. Its first independent step reconstructs the exact endpoint/limit probabilities, all 18 binomial signs, the mixture and randomization values; its second step constructs the univariate integer polynomial from elementary list arithmetic, checks degree/constant and all 33 nonzero coefficients. A separate local SymPy Poly(QQ) expansion was also evaluated and yielded the same sign pattern: 33 positive, one zero, degree 33. The proof is exact but machine-assisted; no independent mathematical Review or formal Lean proof has occurred.

The analysis concerns the declared finite-resolution external observer and preserves its clipped-port/source provenance. It neither modifies P000 nor proves the frozen Bellman optimality or native six-axis transfer. The full minimax classification for arbitrary \(x\) and \(n\ge3\), and the smallest \(n\) exhibiting a failed pure endpoint saddle, remain open.
