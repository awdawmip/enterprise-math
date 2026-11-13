# Exact pure-B all-budget theorem at s=1/10, BRC N=4 / S23

2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immediate predecessor: author commit 9b2a85e7248c47c82d25e64d85ad872aa59e8c69.
This is the classical source-tagged Chernoff *observation* model, not a native BRC-Shor/physical evolution computation.

## Statement

Set s=1/10, h=1/42, v=2h=1/21, a=s(1+v)/2=11/210, b=s(1-v)/2=1/21.
Source-tagged full T laws: P_T=(a,1-s,b), Q_T=(b,1-s,a).
Coarse Bernoulli B laws: P_B=(a,1-a), Q_B=(b,1-b).
One T costs 2-s=19/10; one B costs 1.
For A in {T,B}, define f_A(t)=-log(sum_y P_A(y)^t Q_A(y)^(1-t)), and C_A=max_{0<=t<=1} f_A(t).
For m T and n B, C(m,n)=max_{0<=t<=1}(m f_T(t)+n f_B(t)): ONE shared Chernoff optimizer.

THEOREM. For every integer K>=1, the unique optimum over all integers m,n>=0 with 19m+10n<=10K is (m,n)=(0,K).

## Proof

Reflection of the full T laws gives C_T=f_T(1/2)=-log(1-s+s*sqrt(1-v^2)).
Let k=s/(2-s)=1/19, r=sqrt(1-v^2), rB=sqrt(1-k^2*v^2), alpha=atanh(v), gamma=atanh(kv), delta=2t-1.
For Bernoulli B, its exact Chernoff coefficient is
Z_B(delta)=(s*r/2)*exp(alpha*delta)+((2-s)*rB/2)*exp(-gamma*delta).
Select the rational probe delta0=3/400 (t0=403/800). The exact rational enclosure verifier included here proves

    19*f_B(t0)-10*C_T > 1/1000000000.    (1)

Thus 19*C_B>10*C_T, i.e. C_T<(19/10)C_B.
For all feasible (m,n), pointwise comparison with separate optimized information yields only the valid UPPER bound
C(m,n)<=m*C_T+n*C_B. For m>=1, C(m,n)<[(19/10)m+n]*C_B<=K*C_B=C(0,K).
For m=0 and n<K, C(0,n)=n*C_B<K*C_B because C_B>0 for a!=b.
The only maximizer is (0,K), simultaneously for ALL positive integer budgets. QED.

## Executed exact certificate

VERIFY.py is a pure Python 3 Fraction/isqrt program, requiring no external packages or floating arithmetic. It encloses:
- sqrt(x) on a 10^-26 rational grid using isqrt.
- atanh(x) by 10 positive terms through x^19/19 with error <= x^21/[21(1-x^2)].
- exp(x) by degree-8 polynomial with error <= x^9/[9!(1-x/10)] for 0<=x<1; negative exponents by reciprocal.
- -log(Z), 0<Z<1, using w=(1-Z)/(1+Z), seven positive terms of 2 sum w^(2j+1)/(2j+1), with tail <=2w^15/[15(1-w^2)].
Upper-bound Z_B(delta0) to lower-bound f_B(t0), lower-bound Z_T(0) to upper-bound C_T. All comparisons in (1) are exact Fraction assertions. The lower rational bound for the left side is >1659*10^-12, so the printed 10^-9 guarantee is conservative.
RUN_EVIDENCE.txt is stdout of the executed script. Finite arithmetic only verifies inequality (1); the separate analytic argument proves all-K optimality.

Scope: source-tagged observation laws, declared coarse map, common Chernoff exponent and rational trial cost. No conclusion about native X6 dynamics, physical residuals, or universally safe information erasure; P000 remains unchanged.
Unrestricted ten-label minimax mother problem remains open at last reported [1/2,2/3].
No native task CLAIM or independent mathematical review/admission is asserted.
