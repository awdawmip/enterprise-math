# EC49FUH — Reciprocal-mass coordinate and sharp first-count minimax boundary

Date: 2026-11-20. Evidence: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. Portable research, not a Task CLAIM, formal Result/Review or Foundation admission.

Frozen scientific input: BRC16943 Source \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Predecessor: EC49FUG, PR #2827, commit \`cc3b206a70f7d69fd76c164d987b2a784b94144f\`. All results are for the **inherited clipped-price conditional observation model**, not native X6 physical dynamics or a fresh Bellman optimality proof.

## Definitions and exact affine-reciprocal coordinate

Fix
\[
 E=\frac{1048576}{18958647},\quad m=\frac{1469}{64},\quad
 L=\frac{951}{1280},\quad U=\frac34,\quad W=U-L,\quad
 a=\frac{m(L+U)}2=\frac{2807259}{163840}.
\]
For normalized detector width \(0<x<1\) and shared finite nuisance \(e\le E\), define
\[
 c(x)=m(U-xW/2),\qquad
 p_e(x)=x\frac{1-e c(x)}{1-e a},
\]
\[
 q_e=\frac{575(41217719e-2359296)}
 {45529434409e-2630615040},\qquad
 r_e=p_e+q_e(1-p_e).
\]
Conditional on \(e\), \(K\) has \(\mathrm{Bin}(n,p_e)\) under \(H_-\) and \(\mathrm{Bin}(n,r_e)\) under \(H_+\). Trials are conditionally independent, hypothesis priors equal, and \(e\) is common to both hypotheses. For the first-count test \(\phi=\mathbf 1_{\{K\ge1\}}\), the positive detection-probability difference is
\[
 D_{n,1}(e,x)=(1-p_e(x))^n[1-(1-q_e)^n].
\]

Introduce the exact coordinate
\[
 \theta=(1-ae)^{-1}\in(0,\theta_E],\quad
 \theta_E=(1-aE)^{-1},\quad\beta=3/637.
\]
The cancellation
\[
 a(2630615040-575\cdot2359296)
 =45529434409-575\cdot41217719=21829245984
\]
and the identity \(a\cdot2630615040-45529434409=-456083905\) yield
\[
 \boxed{1-p_e(x)=(1-x)(1-\beta x+\beta x\theta)},
\]
\[
 \boxed{u(\theta):=1-q_e=
 \frac{21829245984}{45529434409-456083905\,\theta}}.
\]
These transformations preserve the original nuisance and clipping-probability information. The reciprocal affine expression is a useful exact conditional-mass coordinate, not a replacement native geometry.

## Theorem 1 — universal endpoint infimum for the first-count test

For **every integer \(n\ge1\)** and **every real \(0<x<1\)**,
\[
 \boxed{\inf_{e\le E}D_{n,1}(e,x)
 =\min\left(D_{n,1}(E,x),D_{n,1}(-\infty,x)\right).}
\]
The notation \(D_{n,1}(-\infty,x)\) means the exact limit as finite \(e\to-\infty\), not another admissible finite nuisance. Thus the exact worst-case equal-prior risk of this particular decision rule is
\[
 \boxed{\sup_{e\le E}R_{n,1}(e,x)=
 \tfrac12\!\left[1-\min(D_{n,1}(E,x),D_{n,1}(-\infty,x))\right].}
\]

**Proof.** On the closed auxiliary interval \(0\le\theta\le\theta_E\) the denominator of \(u(\theta)\) is positive and \(0<u<1\). Its slope coefficient is negative; consequently \(u'>0\), \(u''>0\). Moreover
\[
 \log D_{n,1}(\theta,x)
 =n\log(1-x)+n\log(1-\beta x+\beta x\theta)
 +\log(1-u(\theta)^n).
\]
The second term is concave, strictly so for \(x>0\). The scalar function \(g(v)=\log(1-v^n)\), \(0<v<1\), is concave and decreasing for all \(n\ge1\). Since \(u\) is convex, \(g\circ u\) is concave. Hence \(\log D_{n,1}\) is strictly concave in \(\theta\); its minimum on a compact interval is attained at an endpoint. The \(\theta=0\) endpoint is the original \(e\to-\infty\) limit, and \(\theta=\theta_E\) corresponds to \(e=E\). Positivity converts the log conclusion to the stated conclusion. QED.

**Scope:** this endpoint-minimum theorem applies to \(\phi=\mathbf1_{\{K\ge1\}}\), not automatically to arbitrary threshold mixtures or full composite minimax risk.

## Theorem 2 — exact first failure boundary at n=15 within the first-count Bayes region

Put
\[
 u_E=\frac{4822040484}{8132285009},\qquad
 u_\infty=\frac{21829245984}{45529434409},\qquad
 \eta=\frac{141024}{1653649}.
\]
Then
\[
 D_{n,1}(E,x)=(1-x)^n(1+\eta x)^n(1-u_E^n),
\]
\[
 D_{n,1}(-\infty,x)=(1-x)^n(1-\beta x)^n(1-u_\infty^n).
\]
Let
\[
 t_{15}=\left(\frac{1-u_E^{15}}{1-u_\infty^{15}}\right)^{1/15},
 \qquad
 \boxed{x_{15}=\frac{1-t_{15}}{\beta+\eta t_{15}}}.
\]
The ratio \(D_{15,1}(-\infty,x)/D_{15,1}(E,x)\) is strictly decreasing in \(x\), equals one exactly at \(x_{15}\), and is smaller than one for \(x>x_{15}\). Exact rational sign comparisons isolate
\[
 \boxed{\frac{2797}{10^7}<x_{15}<\frac{2798}{10^7}},
 \quad x_{15}\approx0.00027974730814845366453.
\]

The **different** endpoint Bayes threshold boundary is the unique positive solution \(x_B\) of
\[
 \frac{1512625x_B+141024x_B^2}{1653649}
 = \frac{q_E u_E^{14}}{1-u_E^{15}},\qquad q_E=1-u_E.
\]
The binomial likelihood ratio is strictly increasing with count \(k\); the \(k=0\) signed mass is negative, and the \(k=1\) signed mass is positive exactly when \(p_E(x)<q_Eu_E^{14}/(1-u_E^{15})\). Hence the **unique** endpoint Bayes test is \(K\ge1\) for all \(0<x<x_B\), where
\[
 \boxed{\frac{2956}{10^7}<x_B<\frac{2957}{10^7}},
 \quad x_B\approx0.00029564755490901301761.
\]
In particular \(x_{15}<x_B\).

**Sharp classification on the entire interval \(0<x<x_B\):**
\[
 \boxed{0<x\le x_{15}\quad\Longrightarrow\quad
 R_{15}^{\mathrm{mm}}(x)=\frac{1-D_{15,1}(E,x)}2
 \quad\text{and the endpoint Bayes test is minimax}.}
\]
\[
 \boxed{x_{15}<x<x_B\quad\Longrightarrow\quad
 R_{15}^{\mathrm{mm}}(x)>\frac{1-D_{15,1}(E,x)}2
 \quad\text{and the unique endpoint Bayes test is NOT minimax}.}
\]

**Proof.** If \(x\le x_{15}\), Theorem 1 shows the endpoint Bayes test has its worst case at \(E\), attaining the universal endpoint Bayes lower bound. If \(x>x_{15}\), the limiting gap at \(-\infty\) is strictly smaller than at \(E\); by continuity some **finite negative** \(e\) also gives smaller \(D\) and therefore larger risk. All binary strings have positive probability under both endpoint hypotheses and \(0<x<x_B\), so any rule attaining the unique endpoint Bayes risk must coincide with its deterministic \(K\ge1\) rule at every string. This rule fails the composite bound. A composite minimax rule exists because the randomized test cube is compact and the pointwise supremum of continuous risks is lower semicontinuous. Consequently the actual minimax value must be **strictly** greater than the endpoint lower bound. QED.

This exactly classifies the previously reported EC49FUG subinterval \([1/3500,29/100000]\) and expands it to its sharp algebraic onset within the full \(K\ge1\) endpoint Bayes region. It does not claim the whole width range \(0<x<1\) is solved.

## Exact witness, verification and next question

At \(x=7/25000\), the endpoint Bayes rule is uniquely \(K\ge1\), while
\[
 \frac12\left[D_{15,1}(E,7/25000)
               -D_{15,1}(-\infty,7/25000)\right]>0,
\]
with approximate value \(1.69823354863\times10^{-7}\). A sufficiently negative **finite** nuisance gives the needed strict failure.

The accompanying standard-library Python Fraction script certifies the rational cancellation, sampled formula identities, the two rational algebraic-root brackets, and exact signed-mass witness comparisons. The universal real-domain concavity argument is the human proof above; the samples alone would not prove it. Scope is inherited conditional clipping; Bellman optimality is parent-dependent, and independent mathematical review is pending.

**Next:** solve the sharp composite minimax randomized rule and least-favorable nuisance distribution for \(x_{15}<x<x_B\). Theorem 1 proves the minimum for a pure \(K\ge1\) test; a randomization at count 1 changes the risk and requires a separate full-nuisance certificate and saddlepoint lower bound.
