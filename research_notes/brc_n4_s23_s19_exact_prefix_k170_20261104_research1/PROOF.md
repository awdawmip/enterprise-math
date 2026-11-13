# BRC N=4 / S23 at s=1/9: exact finite-prefix classification and minimal period-17 onset

Date: 2026-11-04. State: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Input provenance: immutable `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`, continuing source commit `d161550d6e4e402eb8b34b590b2c50e8ff0a06d4` in PR #1765. This is a classical, source-labelled Chernoff observer comparison; it neither replaces the six-axis P000 ontology nor asserts a native BRC–Shor computation.

## Exact model and new theorem

Fix `s=1/9`, `h=1/42`, `v=1/21`, `a=11/189`, `b=10/189`. Source-retaining observation T has distributions `(a,1-s,b)` and `(b,1-s,a)`, while coarse B has `(a,1-a)` and `(b,1-b)`. Independent sampling costs are `17/9` for T and `1` for B. Define `f_X(t)=-log(sum_y P_X(y)^t Q_X(y)^(1-t))`, `C_X=max_[0,1] f_X(t)` and `C(m,n)=max_[0,1](m f_T(t)+n f_B(t))`, with a **single common exponent** for both experiments. The budget set is `17m+9n<=9K`, where `K>=1` and `m,n` are nonnegative integers.

**Theorem.** Every positive integer K has a **unique** optimal allocation. For `1<=K<=16`, it is `(m,n)=(0,K)`. For `17<=K<=169`, put `L=floor(K/17)` and `r=K mod 17`. Let the following exact threshold table hold:

| L | K interval | largest remainder r where period endpoint wins |
|---|---|---|
| 1 | 17–33 | 1 |
| 2 | 34–50 | 3 |
| 3 | 51–67 | 5 |
| 4 | 68–84 | 6 |
| 5 | 85–101 | 8 |
| 6 | 102–118 | 10 |
| 7 | 119–135 | 12 |
| 8 | 136–152 | 13 |
| 9 | 153–169 | 15 |

For `0<=r<=threshold[L]`, the optimum is `(9L,r)`. For larger r the optimum is `(0,K)`. **For every K>=170**, the unique optimum is

`(m_K,n_K)=(9 floor(K/17), K mod 17)`.

The least integer `K0` with this allocation formula valid for **all K>=K0** is exactly **170**: it fails at K=169, where the unique optimum is `(0,169)`.

## Analytic reduction to nineteen rational-sign tests

Write `CB=C_B`, `CT=C_T`, `E=CT-(17/9)CB`, `d=CB-f_B(1/2)`. The preceding proven-in-author-notes all-K endpoint lemma and this run's independently rechecked exact rational inequalities give

`E>0`, `CB/9 - 8E - 16d > 0`, and `99E-16d>0`.

For any `K=17L+r` with `0<=r<17`, the candidate `A=(9L,r)` has

`C(A)>=K CB+9L E-rd`.

For a feasible `(m,n)`, with unused cost `u=K-(17/9)m-n`,

`C(m,n)<=K CB+mE-uCB`.

When `9` does not divide m, integrality and coprime costs imply `u>=1/9`, and `m<=9L+8`. Thus

`C(A)-C(m,n)>=CB/9 -8E-16d>0`.

When `m=9j`, feasibility gives `0<=j<=L`, and optimal B count at that j is `n=K-17j`. For real j the function

`H_K(j)=max_[0,1](9j f_T(t)+(K-17j)f_B(t))`

is convex as a supremum of affine functions. Hence every interior integer j has value no greater than the better endpoint `H_K(0)=K CB` or `H_K(L)=C(9L,r)`. Strict endpoint comparison gives unique optimum.

Define `D(L,r)=C(9L,r)-(17L+r)CB`. For each fixed L>=1, **D is strictly decreasing in integer r**: if `t` maximizes the r+1 mixture, then `f_B(t)<=CB`; equality in `C(9L,r+1)<=C(9L,r)+CB` would demand that t simultaneously maximize f_B and the r mixture. The unique B maximizer lies above 1/2 because `f_B'(1/2)>0`, whereas T has unique maximizer 1/2 and `f_T'(t_B)<0`; hence the simultaneous maximizing condition is impossible for L>=1. Therefore, for each L it suffices to certify the sign at the final T-winning remainder and the following B-winning remainder. For L=10 only `D(10,16)>0` is needed. The preceding all-K lemma with L0=11 covers all K>=187.

## Exact arithmetic certificate, including its error semantics

Let `U=sqrt(ab)`, `V=sqrt((1-a)(1-b))`, `l1=log(a/b)`, `l2=log((1-a)/(1-b))`, `Delta=l1-l2>0`. At `t=1/2+delta`, write

`Z_T=1-s+U(exp(delta*l1)+exp(-delta*l1))`, `Z_B=U exp(delta*l1)+V exp(delta*l2)`, `f_X=-log Z_X`.

Derivative identities are exact: `f_B'=-(U e^(delta*l1)l1+V e^(delta*l2)l2)/Z_B` and `f_T'=-U l1(e^(delta*l1)-e^(-delta*l1))/Z_T`. For all t in [0,1], set `m_B=b(1-a)Delta^2>0` and `m_T=2sqrt(ab)(1-s)l1^2>0`. These are valid strong-concavity lower bounds because `-f_B''=w(1-w)Delta^2`, `w(t) in [b,a]`; for T, `-f_T''=l1^2(u-v0^2)>=l1^2u(1-u)`, with `u=(x+y)/(1-s+x+y)>=2sqrt(ab)`, `1-u>=(1-s)`. Therefore for any trial `t0` and each `g=f_B`, or `g=9L f_T+r f_B`,

`g(t0)<=max_[0,1]g<=g(t0)+g'(t0)^2/(2m)`,

with `m=m_B` in the first case and `m=9L m_T` in the second. The upper bound follows from global strong concavity and is valid even when the unconstrained upper quadratic maximizer lies outside [0,1].

`VERIFY.py` evaluates these expressions with interval endpoints **entirely in `fractions.Fraction`**: outward square-root enclosure from integer `isqrt`, outward rounding at scale `10^35`, the positive atanh log series with 24 terms and remainder `2*y^49/(49*(1-y^2))`, and the 25th-degree nonnegative exponential Taylor polynomial with remainder at most `3*x^26/26!` for `0<=x<=1` (negative arguments use reciprocals). All intervals enclose their exact analytic values. Trial deltas are rational numbers selected from the center-quadratic approximation; each actual maximum is rigorously enclosed by its value and derivative at that trial plus the strong-concavity gain bound. Floating formatting is **only for readable display**: every mathematical assertion is a rational strict comparison.

The program verifies 19 decisive sign tests:

| L | D(L, r_T) positive | D(L, r_T+1) negative |
|---|---|---|
| 1 | r=1, >2.361034e-9 | r=2, <-7.90087e-10 |
| 2 | r=3, >1.485774e-9 | r=4, <-1.58017e-9 |
| 3 | r=5, >6.68309e-10 | r=6, <-2.37026e-9 |
| 4 | r=6, >2.97154e-9 | r=7, <-1.35277e-10 |
| 5 | r=8, >2.14849e-9 | r=9, <-9.33409e-10 |
| 6 | r=10, >1.33661e-9 | r=11, <-1.72883e-9 |
| 7 | r=12, >5.31065e-10 | r=13, <-2.52272e-9 |
| 8 | r=13, >2.81541e-9 | r=14, <-2.70554e-10 |
| 9 | r=15, >2.00492e-9 | r=16, <-1.06959e-9 |
| 10 | r=16, >4.29698e-9 | not needed |

Each display bound is intentionally rounded inward from the exact Fraction enclosure printed in RUN_EVIDENCE.txt. Strict sign and monotonicity classify the full finite prefix. At K=169 (L=9,r=16), `D<0`; at K=170 (L=10,r=0), `D=90E>0`. Since all K>=170 are covered by L=10 signs and previous L>=11 lemma, 170 is the minimal onset. QED.

## Verification scope / next question

The proof covers **all positive integer budgets for this fixed s,h and the specified source-labelled two-observation Chernoff model**. The test code certifies the finite base signs; the analytic endpoint/convexity/monotonicity reductions and the previously preserved all-K lemma establish the unbounded quantifier. The preliminary published L0=11 theorem remains valid and is strengthened to the sharp threshold L0=10, K0=170. Independent mathematical review and native admission are pending. The unrestricted ten-label minimax mother question remains in its recorded [1/2,2/3] open bracket.

Next: vary s rationally around 1/9 and look for exact changes in the first and final winning remainders; derive uniform parameter intervals where both the finite-prefix signatures and the eventual period-17 conclusion remain valid, or identify a phase transition certificate. Preserve the original frozen observer/source pins.
