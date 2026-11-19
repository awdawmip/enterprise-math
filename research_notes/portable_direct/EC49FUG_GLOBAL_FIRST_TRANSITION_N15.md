# EC49FUG — First global endpoint-minimax failure occurs at 15 binary observations

2026-11-20. Evidence: AUTHOR_PROVED / EXACT_INTEGER_BERNSTEIN_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
Scientific pin: BRC16943 source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Immediate predecessor: EC49FUF, PR #2825, commit f2ba5ff553de826faaf710875f3cba04b1052f9a. Independent portable research; not a formal Task CLAIM/Result/Review or Foundation promotion.

## Model

Under the frozen one-sided price-clipping observation model, let

\[
E=\frac{1048576}{18958647},\quad m=\frac{1469}{64},\quad
L=\frac{951}{1280},\quad U=\frac34,\quad W=U-L=\frac9{1280}.
\]

Let \(x=\delta/W\in(0,1)\) be an arbitrary normalized detector width. The same unknown finite real nuisance \(e\le E\) is shared across both hypotheses and all trials. Define

\[
a=m(L+U)/2,\quad c(x)=m(U-xW/2),
\quad p_e(x)=x\frac{1-ec(x)}{1-ea},
\]
\[
q_e=\frac{575(41217719e-2359296)}{45529434409e-2630615040},
\quad r_e(x)=p_e(x)+q_e[1-p_e(x)].
\]

Under H- the n conditionally independent binary observations have probability p; under H+ they have probability r. Equal hypothesis priors and randomized tests are permitted. The count K is sufficient. For threshold j put

\[
T_{n,j}(v)=\sum_{k=j}^n {n\choose k}v^k(1-v)^{n-k},\quad
D_{n,j}(e,x)=T_{n,j}(r_e(x))-T_{n,j}(p_e(x)).
\]

The equal-prior risk of choosing H+ exactly when K≥j is (1-D)/2.

## Sharp first-count theorem (width free)

**(A)** For every real 0<x<1, every n=1,...,14, and every endpoint-e=E Bayes threshold j=j_n(x),

\[
\boxed{D_{n,j}(e,x)\ge D_{n,j}(E,x)\quad
\text{for every finite }e\le E.}
\]

Hence the endpoint Bayes test is composite minimax and the exact risk is

\[
\boxed{R_n^{mm}(x)=\frac{1-D_{n,j_n(x)}(E,x)}{2}},
\quad 1\le n\le14.
\]

At an endpoint likelihood-ratio tie, either neighboring Bayes threshold is minimax.

**(B)** Every real x in the rational interval

\[
\boxed{\frac1{3500}\le x\le\frac{29}{100000}}
\]

has the *unique* endpoint Bayes rule K≥1, but for the admissible finite e=-1,

\[
\boxed{D_{15,1}(-1,x)<D_{15,1}(E,x).}
\]

Thus the endpoint Bayes rule is not minimax and the composite minimax value is strictly larger than the endpoint Bayes lower bound on this interval. Consequently the **first trial count permitting failure when width is free is exactly n=15**. The previously certified n=17 for x=5/123 remains correct for that fixed width.

At x=1/3500 the rational difference is approximately -7.0461745475959085×10^-6 (decimal for scale only; all sign evidence is exact).

## Exact proof of (A)

At e=E, p_E(x) is strictly increasing in x, since

\[
p_E(x)=\frac{x[(1-EmU)+(EmW/2)x]}{1-Ea},\quad
1-EmU=\frac{302525}{6319549}>0.
\]

Also 0<q_E<1. The endpoint count likelihood ratio is

\[
\Lambda_{n,k}(x)
=\left(\frac{r_E(x)}{p_E(x)}\right)^k(1-q_E)^{n-k}
=\left(1+\frac{q_E[1-p_E(x)]}{p_E(x)}\right)^k(1-q_E)^{n-k}.
\]

For fixed x it strictly increases with k; for k≥1 it strictly decreases with x. For each k=1,...,n-1 its signed binomial mass has one width crossing from positive to negative. The k=0 mass is negative and k=n positive at all interior widths. Therefore the endpoint Bayes threshold j lies in the width interval between consecutive crossings. Exact rational signed-mass evaluations bracket each crossing between adjacent integer multiples of 1/100000. Widening the adjacent crossing brackets outward produces rational envelope I_(n,j) covering the *entire* endpoint Bayes j-region, including boundary ties.

Set s=E-e≥0 and define

\[
A=1-Ea+as,\quad P=x[1-Ec(x)+c(x)s],
\]
\[
B=2630615040-45529434409E+45529434409s,\quad
Q=575[2359296-41217719E+41217719s].
\]

Then p=P/A, q=Q/B, r=J/V with V=AB and J=PB+QA-PQ. Multiply A,P by the same positive common coefficient denominator and separately B,Q by their own positive common denominator, producing exact **integer bivariate polynomials** without changing the ratios. All A,B,V and V(0) are positive for s≥0.

Let

\[
F_{n,j}(N,D)=\sum_{k=j}^n {n\choose k}N^k(D-N)^{n-k},
\]
\[
G_{n,j}(s,x)=F_{n,j}(J,V)-B^nF_{n,j}(P,A),
\]
\[
H_{n,j}(s,x)=V(0)^nG_{n,j}(s,x)-G_{n,j}(0,x)V(s)^n.
\]

Thus the following is an **exact identity**, not a numerical approximation:

\[
D_{n,j}(E-s,x)-D_{n,j}(E,x)
=\frac{H_{n,j}(s,x)}{V(0)^nV(s)^n}.
\]

Its denominator is positive and H(0,x)=0. For n≤14, every threshold j=1,...,n, and every h=1,...,2n, the attached verifier certifies that the integer polynomial C_(n,j,h)(x)=[s^h]H_(n,j)(s,x) is nonnegative **throughout the rational interval I_(n,j)**.

The certificate uses exact Bernstein coefficients: expand C(u+(v-u)t) for t∈[0,1], convert to the Bernstein basis of degree d=2n by the identity

\[
b_i=\sum_{h=0}^i a_h\,\frac{{i\choose h}}{{d\choose h}},
\]

and check all b_i≥0 after exact positive denominator clearing. Every checked coefficient polynomial has degree 2n; no floating sign tests or dense-width sampling are used. For all n≤14 the executable checks 2030 coefficient polynomials and 46130 Bernstein control signs, all nonnegative, along with root-bracket sign/order checks.

Therefore H(s,x)=Σ_(h=1)^(2n) s^h C_(n,j,h)(x)≥0 whenever s≥0 and j is endpoint optimal. The endpoint-e=E Bayes value is a universal minimax lower bound. The exhibited endpoint threshold has no larger risk at any admissible e; hence it attains the lower bound.

## Exact proof of (B)

For threshold j=1,

\[
D_{n,1}(e,x)=(1-p_e(x))^n[1-(1-q_e)^n].
\]

The verifier checks every endpoint mass sign for k=0,...,15 at both rational interval ends. Combined with the monotonic likelihood ratios, the unique endpoint Bayes rule K≥1 holds throughout [1/3500,29/100000].

At n=15 the difference G(x)=D_(15,1)(-1,x)-D_(15,1)(E,x) is a degree-30 **rational polynomial** in x. Exactly expanding

\[
G\left(\frac1{3500}+
\left(\frac{29}{100000}-\frac1{3500}\right)t\right)
\]

in the degree-30 Bernstein basis gives **31 strictly negative coefficients**, all verified using Fraction arithmetic. Therefore G(x)<0 for every real width throughout the closed interval. This is an exact real-interval counterexample.

The risk supremum over e of a randomized test is lower semicontinuous, and the finite-dimensional test cube is compact. A minimax rule attaining the endpoint Bayes lower bound would have to equal the *unique* endpoint Bayes test on all binary strings (both endpoint laws give every string positive probability). But that test incurs strictly greater risk at e=-1. Thus the minimax value is strictly greater than the endpoint Bayes value, proving non-minimaxity rather than merely failure of one comparison.

## Verification, provenance and next questions

Run Python 3 standard library file EC49FUG_GLOBAL_FIRST_TRANSITION_VERIFY.py without external packages. It reconstructs all input rationals, derives the threshold-crossing envelopes with exact signed masses, computes integer (x,s) polynomial identities, tests all Bernstein signs and the rational witness interval, and prints PASS only after assertions succeed. The author-run check passed. Research proof is author-checked / parent-dependent / NOT_REVIEWED; independent scientific review and inherited Bellman optimality remain separate. This does not assert a current native CLAIM, task publication, Activity source association or Source deployment.

Next useful work: characterize the complete n=15 width failure region and its algebraic endpoints; solve the sharp n=15 composite minimax randomized rule and least-favorable nuisance law; examine subsequent n/x transitions while retaining the common nuisance and clipped-origin residual.
