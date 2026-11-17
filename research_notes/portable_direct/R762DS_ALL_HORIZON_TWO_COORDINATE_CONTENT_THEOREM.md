# R762DS — All-horizon exact 3-adic content of the two-coordinate positive BRC observer

**Date:** 2026-11-18 (Asia/Shanghai). **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Original researcher:** EM-X6-3050F6; SID MCP-4b2d70a97f594366a7c94a0f8b45df38. **Independent review:** NOT_REVIEWED. Native control writes use the original authenticated Run and require a fresh owner-checked receipt.

## Frozen inputs and exact mathematical scope

- Taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md.
- P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.
- Candidate paired-triad six-branch positive polynomial: P(X,Y,Z)=1+X+Z+XY+YZ+XYZ (R762DI–DK).
- The explicitly typed terminal marginal pi_XZ(u,v,w)=(u,w) gives F(X,Z)=P(X,1,Z)=1+2X+2Z+XZ.
- Earlier R762DP/DQ/DR solved all n<9d; most recent source PR #2680@db2ec0700c7a1af3c41e5503f30a8d85eee36a06.

This is the six-positive-microbranch *candidate* BRC observer at a terminal endpoint. The full signed six-axis X6 Cell and the chosen native three-axis slice, the unobserved third area, branch names, paths, and signed Port provenance remain present in the upstream model. Their redundancy under future authorized operations has not been certified.

## All-horizon theorem

Fix **every** integer a>=2, Q=3^a, d=3^(a-1), and n>=0. Work in the integral group ring R_Q=Z[X,Z]/(X^Q-1,Z^Q-1). Let c_Q(n) denote the positive gcd of all Q^2 coefficients of F^n in the monomial basis X^i Z^j, 0<=i,j<Q. Then

\[
\boxed{c_Q(n)=3^{\,2\max(0,\lfloor (n-d)/(2d)\rfloor)}.}
\]

Equivalently c_Q(n)=1 for 0<=n<3d, and for each t>=1,

\[
(2t+1)d\le n<(2t+3)d \quad\Longrightarrow\quad c_Q(n)=3^{2t}.
\]

In particular **c_Q(9d)=3^8=6561 for all a>=2**, and all later changes occur exactly at 11d,13d,15d,... . The minimal number of equiprobable deterministic seeds that reproduces the *terminal marginal only* is

\[
M_Q(n)=6^n/c_Q(n)=\frac{6^n}{3^{2\max(0,\lfloor(n-d)/(2d)\rfloor)}}.
\]

For k paired candidate blocks use n=2k. This has no asserted native TRIADIC_CLOSURE_E event permission.

## Proof

### Lemma 1: sharp one-axis nilpotent filtration

In A_Q=Z[T]/(T^Q-1), let x=T-1. The characteristic-three algebra is A_Q/3=F_3[x]/(x^{3d}). The binomial relation gives x^{3d}=3H, where

\[
H=-\sum_{i=1}^{3d-1}\frac{\binom{3d}{i}}3 x^i.
\]

For 0<i<3^a, v_3(binomial(3^a,i))=a-v_3(i), using binomial(3^a,i)=(3^a/i)binomial(3^a-1,i-1) and Lucas's unit test on the row 3^a-1. Therefore \bar H=x^d u(x), with u(0) nonzero modulo 3, hence u a unit in F_3[x]/(x^{3d}).

For every s>=0, induction gives

\[
x^{(2s+1)d}=3^s B_s,\qquad \bar B_s=x^d u_s(x),\quad u_s(0)\ne0.
\]

Base s=0: B_0=x^d. For the step write B_s=x^d\widetilde u_s+3R_s; then

\[
x^{(2s+3)d}=3^{s+1}(H\widetilde u_s+x^{2d}R_s).
\]

Its normalized mod-3 quotient is x^d(u u_s+x^d\bar R_s), preserving the nonzero degree-d coefficient. Multiplication by x^r for 0<=r<2d yields the **exact integral coefficient valuation**

\[
x^{(2s+1)d+r}/3^s\bmod3=x^{d+r}u_s(x)\ne0.\tag{1}
\]

Indeed d+r<3d. The bases 1,T,...,T^{Q-1} and 1,x,...,x^{Q-1} are unimodularly equivalent over Z, so their coefficient gcds agree.

### Lemma 2: exact normalized two-axis leading term

Let x=X-1, z=Z-1, w=2+x+z. The identity F=xz+3w holds in R_Q. For t>=1 put N=(2t+1)d. Expanding,

\[
F^N=\sum_{j=0}^{N}3^j\binom Nj(xz)^{N-j}w^j.\tag{2}
\]

By (1), the j=0 term is divisible by 3^{2t}, with normalized reduction x^d z^d u_t(x)u_t(z). Terms j>=2t+1 vanish modulo 3^{2t+1}.

For 1<=j<=2t set h=ceil(j/(2d)) and s=t-h>=0. Then

\[
N-j=(2s+1)d+r,\qquad r=2dh-j\in[0,2d-1].
\]

The two pure-axis factors contribute at least 3^{2s}, so the whole j-term has valuation at least

\[
2t+j-2h+v_3\left(\binom Nj\right).\tag{3}
\]

For j>=3, d>=3 implies j-2ceil(j/(2d))>=1, making these terms multiples of 3^{2t+1}. For j=2, v_3(binomial(N,2))=v_3(N)>=1, so it also vanishes. For j=1, the valuation is at least 2t-1+v_3(N)>=2t. Its possible normalized mod-3 contribution lies in (x^{3d-1}z^{3d-1}): by (1) each axis quotient has leading degree 3d-1, and multiplication by w cannot reduce degrees.

Consequently F^N is divisible by 3^{2t}, and its normalized quotient satisfies

\[
F^N/3^{2t}\bmod3=x^d z^d U_t(x,z),\qquad U_t(0,0)\ne0.\tag{4}
\]

The potential j=1 contribution has strictly higher bidegree, leaving the x^d z^d coefficient of the j=0 term nonzero. Equation (4) describes the reduction of an integral quotient, not division in the characteristic-three ring.

### Proof for all n

For 0<=r<2d, multiply (4) by F^r. Since F mod3=xz,

\[
F^{N+r}/3^{2t}\bmod3=x^{d+r}z^{d+r}U_t(x,z)\ne0,
\]

as d+r<3d and U_t is a unit. This proves v_3(c_Q(n))=2t throughout every t>=1 interval. For 0<=n<3d, F^n mod3=x^nz^n is nonzero, giving valuation zero.

The sum of coefficients of F^n equals F(1,1)^n=6^n, so c_Q(n) has only 2 and 3 as possible prime divisors for n>=1. Modulo 2, F=1+XZ; the group algebra F_2[C_Q^2] is reduced for odd Q (Maschke, or squarefreeness of both cyclotomic relations), and 1+XZ is nonzero. Hence every positive power remains nonzero, proving v_2(c_Q(n))=0. At n=0 the gcd is 1. The stated formula follows. **QED.**

## Exact computational evidence

A companion dependency-free Python integer recurrence computes all Q^2 cyclic coefficient counts modulo 3^30:

\[
A_{n+1}(i,j)=A_n(i,j)+2A_n(i-1,j)+2A_n(i,j-1)+A_n(i-1,j-1).
\]

For each exponent it checks divisibility by the theorem's 3^e, finds an explicit coefficient nonzero modulo 3^{e+1}, and checks total mass modulo 3^30 equals 6^n. The executed author verification on 2026-11-18 returned **PASS** on Q=9 (n=1..80), 27 (1..160), 81 (1..297), and 243 (1..245): **782 configurations and 16,538,742 coefficient visits**. All expected exponents are <30, so modular witnesses give exact v_3 values throughout this finite domain. Full per-boundary sample witnesses and final-vector SHA256 hashes are in the companion JSON evidence. The general theorem is proved symbolically above; independent review remains NOT_REVIEWED.

## Remaining scientific frontier

1. Classify all-a three-adic content for **full three-coordinate** P(X,Y,Z), rather than only the XZ marginal.
2. Obtain native licensed TRIADIC_CLOSURE_E signed Cell/Link/Port event rules and V17/V29/V39 transport; test the exact observer-fibre constancy required for future-safe BRC reduction.
3. Independently review the one-axis induction, binomial-valuation bound, and special j=1 contribution; formal Result/admission requires its own current Source authority and review.
