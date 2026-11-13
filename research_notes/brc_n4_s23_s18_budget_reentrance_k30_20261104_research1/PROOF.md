# BRC N=4 / S23 — exact integer-budget re-entrance at s=1/8

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: all-K theorem at s=1/2, author commit 2387f8bfb09b215af73a1013875a013a98e0a363. Model unchanged.

## The exact result

Let s=1/8 and relative contrast v=2h=1/21. Put a=s(1+v)/2=11/168 and b=s(1-v)/2=10/168. The source-tagged T laws are P_T=(a,1-s,b), Q_T=(b,1-s,a). The coarse B laws are P_B=(a,1-a), Q_B=(b,1-b). Cost(T)=2-s=15/8 and Cost(B)=1.

For A in {T,B}, define f_A(t)=-log(sum_y P_A(y)^t Q_A(y)^(1-t)) and C_A=max_{0<=t<=1} f_A(t). Crucially, mixed information uses ONE shared exponent:
C(m,n)=max_{0<=t<=1}[m f_T(t)+n f_B(t)].
The integer-budget feasibility condition is 15m+8n<=8K, m,n>=0 integers.

THEOREM. For every integer 1<=K<=30 the unique global maximizer (m,n) is:
* K=1..14: (0,K), pure B.
* K=15: (8,0), pure T.
* K=16..19: (8,K-15), mixed.
* K=20..29: (0,K), pure B AGAIN.
* K=30: (16,0), pure T.

The budget re-entrance is genuine: although C_T/(15/8)>C_B, the uniquely optimal strategy returns to pure B for K=20..29 after a positive mixed window K=16..19.

## Analytic proof reducing every feasible integer allocation

T is reflection-symmetric in t, so C_T=f_T(1/2). Let E=C_T-(15/8)C_B. Our independently executed exact rational certificate proves 0<E<1.91e-9, C_B>7.5633e-5, and 8C_T-15C_B>1.52e-8.

For any feasible (m,n), use the *separate* optimizers only as an UPPER bound:
C(m,n)<=m C_T+n C_B.
Define slack u=K-(15/8)m-n>=0. Then
C(m,n)-K C_B <= mE-u C_B.

For K<=30, m<=16. If 8 does not divide m, the fractional part of 15m/8 gives u>=1/8 for any integer n. As verified exactly, 16E<C_B/8; hence
C(m,n)-K C_B <=16E-C_B/8<0.
All allocations with 8 not dividing m are therefore strictly worse than the feasible all-B allocation.

The only remaining T counts are m=0,8,16. At fixed m, adding a feasible B trial strictly improves positive-information Chernoff information, so use the largest allowed n. For K<=29, m=16 is infeasible, leaving all-B (0,K) and, at K>=15, (8,K-15).

For K=15+j, 0<=j<=14, set
D(j)=C(8,j)-(15+j)C_B.
Since f_B(t)<=C_B for every t, the one-shared-exponent variational formula gives C(8,j+1)<=C(8,j)+C_B, hence D(j+1)<=D(j). The exact global certificates below give
D(4)>2.11e-9>0,
D(5)<-3.45e-10<0.
Therefore D(j)>0 for j=0..4, and D(j)<0 for j=5..14, resolving every K from 15 through 29.

For K=30, (16,0) is feasible and
C(16,0)=16 C_T > 8 C_T+15 C_B >=C(8,15),
where the strict inequality follows from 8C_T>15 C_B. It also exceeds pure B, and the already eliminated 8-nondivisible T counts. QED.

## Exact rational interval certificate, with no floating-point proof assumptions

Write delta=2t-1 in [-1,1], k=s/(2-s)=1/15, r=sqrt(1-v^2), rB=sqrt(1-k^2 v^2), alpha=atanh(v), gamma=atanh(kv). The coefficients and derivatives are explicit:

Z_T(delta) =1-s+s*r*cosh(alpha*delta);
Z_B(delta) =(s*r/2)*exp(alpha*delta)+((2-s)*rB/2)*exp(-gamma*delta).

Their joint exponent is C(m,n)=max_delta[-m log Z_T(delta)-n log Z_B(delta)].

A rigorous rational interval evaluator in VERIFY.py uses only Fraction and isqrt: square roots are bracketed on a denominator 10^30 grid; atanh uses 13 positive power-series terms and the tail x^27/[27(1-x^2)]; exp uses 12 terms plus the positive geometric upper tail x^13/[13!(1-x/14)], with reciprocal bounds for negative x; -log Z uses seven atanh-power terms in w=(1-Z)/(1+Z) with remainder 2w^15/[15(1-w^2)]. Operations propagate exact lower and upper rational bounds throughout.

To obtain global optimizer UPPER bounds from a rational probe delta0, use strong concavity: if F''<=-mu<0 throughout [-1,1], then
max F <=F(delta0)+F'(delta0)^2/(2mu).
The probe F(delta0) itself is a LOWER bound.

Proof of global curvature bounds: B has tilted success weight w_B in [b,a]. Hence
(log Z_B)''=w_B(1-w_B)(alpha+gamma)^2>=b(1-a)v^2>1/10000.
For T, the tilted exponent takes values {-alpha,0,alpha}. Since Z_T<=1 by Holder's inequality, its tilted nonzero mass is at least s*r, and the magnitude of its signed mean (in alpha units) is <=tanh(alpha)=v. Therefore
(log Z_T)'' >= alpha^2[s*r-v^2] >=v^2[s(1-v^2)-v^2].
Combining with B,
(log (Z_T^8 Z_B^5))''
 >=8v^2[s(1-v^2)-v^2]+5b(1-a)v^2>1/400.
These lower bounds are uniform for all real delta in [-1,1].

The exact rational probes are deltaB=7413/1000000, delta4=1561/1000000, delta5=1853/1000000. For C_B, the probe yields its lower bound and the derivative-square correction with mu=1/10000 yields its upper bound. For D(4), evaluation of -8log Z_T(delta4)-4log Z_B(delta4) gives a lower bound. For D(5), the derivative-square correction with mu=1/400 gives an upper bound on the TRUE jointly optimized information. Results below are decimal displays of exact rational intervals:

C_T ~ 1.4181384437557781447647e-4;
7.5633034359952527179612e-5 <=C_B<=7.5633034359955134037308e-5;
1.5239605295505252167945e-8 <=8C_T-15C_B;
D(4)>=2.1149932118769478205896e-9;
D(5)<=-3.4582776703406476425649e-10;
0<E<1.91e-9 and 16E<C_B/8.

All strict comparisons are asserted on Fraction objects, before printing PASS. VERIFY.py reports all 30 winning allocations, but their universally quantified global optimality is proved by the analytic slack/exchange argument and exact three certificates, not by a floating-point scan.

## Meaning and remaining goal

T retains the source tag; B is the declared erasure/minus coarse observer. This quantifies discrimination information under the specified future Chernoff observer and independent sampling budget. Provenance is not generally redundant, and the result does not claim native X6 time dynamics. P000 is unchanged. The unrestricted ten-label decoder minimax mother problem retains its last reported OPEN interval [1/2,2/3].

The immediate next unit is K=31..100 at s=1/8 where multiple 8-T blocks compete, together with an independent pure-B efficiency certificate at s=1/10. Native active Owner, authenticated CLAIM, Result freeze, independent review and mathematical admission remain distinct; this is author-side research.