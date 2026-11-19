# EC49FUF — First endpoint-saddle failure at 17 trials for the fixed rational detector width

Date: 2026-11-20. Evidence: AUTHOR_PROVED / EXACT_INTEGER_POLYNOMIAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Scope: external one-sided price-clipping observer from frozen BRC16943 science (parent commit fc0f038e7bfd12c886b4d37f900bfb770c0f61ab). Direct predecessor: EC49FUE-S at immutable commit 191fb5ec2276c7caa28f6c42c6b6c9699d660e0b. This is independent portable research evidence, not a formal Task CLAIM, Result, Review or P000 amendment.

## Theorem: sharp first failure count, at one fixed width

Fix the inherited common nuisance parameter e in (-infinity,E], where

E = 1048576/18958647, m = 1469/64,
L = 951/1280, U = 3/4, W = U-L = 9/1280,
x = 5/123, delta = xW = 3/10496.

The same finite real e is shared across both hypotheses and across all n conditionally independent readings. Under H- a reading is Bernoulli(p_e); under H+ it is Bernoulli(r_e), where

p_e = x[1 - e m(U-xW/2)]/[1-e m(L+U)/2],
q_e = 575(41217719e-2359296)/(45529434409e-2630615040),
r_e = p_e + q_e(1-p_e).

The clipped-source identity and continuous/source mixture remain in the observer model even when only the count K of positive detector outputs is used in this specific testing decision. The hypotheses have equal prior probability. Randomized tests of the ordered n binary readings are allowed.

**Theorem.** For every n=1,2,...,16 at this one fixed x=5/123, the endpoint-e=E Bayes test is minimax over the entire real half-line e<=E. The exact optimal count thresholds are:

| Trial count n | Decide H+ if and only if |
| --- | --- |
| 1 through 5 | K >= 1 |
| 6 through 11 | K >= 2 |
| 12 through 16 | K >= 3 |

Writing j_n for this threshold and
T_{n,j}(y)=sum_{k=j}^n C(n,k)y^k(1-y)^(n-k),
D_{n,j}(e)=T_{n,j}(r_e)-T_{n,j}(p_e),

the exact minimax risk is

R_n^mm(5/123) = [1-D_{n,j_n}(E)]/2     (1<=n<=16).

For **each** such n and every finite e<E there is a strict inequality D_{n,j_n}(e)>D_{n,j_n}(E). Thus E is the unique worst nuisance value for this optimal test.

For n=17 the endpoint-e=E Bayes threshold is K>=3, but it is not minimax; the full 17-trial composite minimax rule was proved in EC49FUE-S and randomizes at K=3. Consequently, **17 is the smallest trial count at which the endpoint Bayes test fails to be minimax, for the fixed width x=5/123**. This theorem does not assert minimality when detector width is also allowed to vary.

## Exact proof: integer-polynomial certificate for all n<=16

Put s=E-e >=0 and let

a=m(L+U)/2,  c=m(U-xW/2).

Define rational degree-one numerator/denominator pairs:

A(s)=1-Ea+as, P(s)=x(1-Ec+cs),
B(s)=2630615040-45529434409E+45529434409s,
Q(s)=575(2359296-41217719E+41217719s).

Then p_{E-s}=P/A, q_{E-s}=Q/B, and
r_{E-s}=J/V, where J=PB+QA-PQ and V=AB.
A and B are strictly positive for all s>=0.

For every pair (A,P) and (B,Q), multiply its numerator and denominator by the SAME positive least common multiple of coefficient denominators. From here A,P,B,Q denote these jointly scaled **integer** polynomials; the probability ratios remain unchanged. Define

F_{n,j}(J,V)=sum_{k=j}^n C(n,k) J^k(V-J)^(n-k).

With d_n/d_d=D_{n,j}(E) reduced to lowest terms, construct the integer polynomial

H_{n,j}(s) =
d_d{F_{n,j}(J,V)-F_{n,j}(P,A)B^n}
 - d_n V^n.

The following is an exact polynomial identity, valid for all s>=0:

D_{n,j}(E-s)-D_{n,j}(E)
=H_{n,j}(s)/[d_d V(s)^n].

The bundled standard-library-only Python checker uses exact fractions and integer polynomial operations to verify all load-bearing algebraic sign claims. It establishes for each n=1..16:

* The endpoint binomial signed mass a_{E,k}=C(n,k)[r_E^k(1-r_E)^(n-k)-p_E^k(1-p_E)^(n-k)] is strictly negative for k<j_n and strictly positive for k>=j_n. Hence the unique endpoint Bayes test is exactly K>=j_n, even among tests on the entire ordered binary sequence (exchangeability).
* H_{n,j_n}(0)=0; deg H_{n,j_n}=2n; **every** coefficient [s^h]H_{n,j_n} for 1<=h<=2n is a strictly positive integer. The total number of individually checked positive coefficients is sum_{n=1}^{16}2n = 272. No floating-point sign inference is used.
* The polynomial identity is also compared with independently evaluated rational binomial tails at s=0,1,7/3, a focused implementation cross-check.

Since d_d>0 and V(s)>0 for s>=0, these exact coefficient signs yield D_{n,j_n}(E-s)>D_{n,j_n}(E) whenever s>0. The threshold test therefore has worst risk [1-D_{n,j_n}(E)]/2, while every test has worst risk at least its Bayes lower bound at e=E. Equality gives the stated minimax value for each n<=16.

At n=17 the checker independently verifies j_17=3, deg H_{17,3}=34, H_{17,3}(0)=0, exactly 33 positive nonconstant coefficients and a **negative leading coefficient** [s^34]H_{17,3}<0; it also checks D_{17,3}(-1)<D_{17,3}(E) in exact rational arithmetic. The unique endpoint Bayes rule K>=3 therefore incurs strictly greater risk at a finite admissible nuisance value. Because randomized count tests form a compact finite-dimensional cube and the worst-risk objective is lower-semicontinuous, a minimax rule exists; attaining the endpoint Bayes lower bound would force this unique endpoint Bayes rule, contradiction. Hence its minimax risk is strictly greater than the endpoint Bayes risk. The companion EC49FUE-S already gives an explicit sharp randomized rule and a more detailed exact saddle certificate.

This proves the fixed-width first-count transition by finite **exhaustive coverage of n=1..16** plus a certified n=17 failure, not by sampling widths or nuisance values.

## Verification, evidence and next question

Reproduction: run EC49FUF_FIXED_WIDTH_FIRST_TRANSITION_VERIFY.py with Python 3 standard library. It reconstructs the original rational probabilities, derives every threshold from all n+1 signed counts, expands integer polynomials rather than using floating approximations, checks the 272 coefficient inequalities and the n=17 sign transition, and prints a PASS only after all assertions hold. The actual author-run result was PASS. The theorem is machine-assisted, author-proved, not independently reviewed. The inherited one-sided clipping/Bellman formulas are kept at their original evidence level.

The remaining stronger question is to determine whether n=17 is the smallest counterexample **when x is free in (0,1)**. Exact uniform-in-x positivity for n<=16 would discharge that; numerical width scans are exploratory only. Another route is to characterize the algebraic width intervals where the leading coefficient of the endpoint-test excess first changes sign, then analyze finite-e obstructions separately. In either route, do not collapse the clipped-source residual outside the explicitly sufficient binomial-count hypothesis test.

Source attribution: historical EC49FUE-S Researcher EM-DIRECT-8454C6, original portable research line. This new note preserves the prior provenance without asserting new authenticated CLAIM or Activity authority.
