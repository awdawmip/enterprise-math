# BRC N=4 / S23: strict mixed-vs-pure Chernoff advantage under an integer budget

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Required inherited analytic lemma: preceding author proof @8b88188ab137e5d35c92c4abb06b89463dcb5357, research_notes/brc_n4_s23_chernoff_global_unique_20261104_research1/PROOF.md. All frozen model inputs and source tags are unchanged.

## Model and correct common exponent

Fix v=2h=1/21 and 0<s<1. The source-tagged T laws are P_T=(s(1+v)/2,1-s,s(1-v)/2) and Q_T=(s(1-v)/2,1-s,s(1+v)/2). The B laws are Bernoulli with success probabilities p=s(1+v)/2 and q=s(1-v)/2. Trial costs c_T=2-s, c_B=1.

Define f_A(t)=-log(sum_y P_A(y)^t Q_A(y)^(1-t)), and C_A=max_{0<=t<=1} f_A(t), A=T,B. The joint Chernoff information of m independent T and n independent B observations is

  C_mix(m,n)=max_{0<=t<=1} (m f_T(t)+n f_B(t)).

This maximization uses ONE exponent for both sources. The budget is an integer K>=1, with m,n nonnegative integers and m(2-s)+n<=K. Symmetry of the three-outcome T laws and convexity of the log Chernoff coefficient imply f_T(1/2)=C_T>0. The distinct B laws give f_B(1/2)>0 by strict Cauchy-Schwarz. Write F(s)=C_T/(2-s)-C_B.

## Theorem A: rational-cost mixed-budget family and pure B regime

For every s with F(s)<=0 and any feasible counts m,n,

  C_mix(m,n) <= m C_T+n C_B
             <= (m(2-s)+n) C_B <= K C_B.

Hence all-B sampling is optimal among T/B allocations under budget K in this regime.

For a rational s with F(s)>0 write c_T=2-s=P/Q in lowest terms, with integers P>Q>=1. For every positive integer L set K=LP+1, m=LQ, n=1. The cost is exactly K. The best pure T count is floor(K/(P/Q))=LQ, and the best pure B count is K. By evaluating the JOINT coefficient at t=1/2,

  C_mix(LQ,1)>=LQ C_T+f_B(1/2)>LQ C_T.

Moreover LQ C_T = LP(C_B+F(s)), hence

  C_mix(LQ,1)-K C_B > LP F(s)-C_B.

Consequently for every integer L satisfying LP F(s)>C_B, this mixed allocation is strictly better than BOTH pure allocations at the SAME budget. Infinitely many such L exist. The claim is about strict dominance over pure strategies, not global optimality among all mixtures.

The preceding fixed-v author analytic theorem establishes that F is negative below its unique critical s_c, positive above, with s_c in (0.10243902443,0.10243902445). Thus at v=1/21 the pure B regime is s<=s_c; in the region s>s_c, every rational s admits infinitely many exact budget witnesses of mixed superiority.

## Theorem B: explicit witness K=75001, 50000 T + 1 B

Fix s=1/2, v=1/21. Then c_T=3/2 and the B parameters are p=11/42, q=10/42. Set L=25000, giving K=75001, m=50000, n=1. The mixed cost is 50000*(3/2)+1=75001. Best pure T: 50000 trials; best pure B: 75001 trials.

We give an exact rational certificate for

  C_mix(50000,1)-75001 C_B > 1/1600,
  C_mix(50000,1)-50000 C_T > 0.

### Positive lower bound on actual optimized efficiency gap

At s=1/2, the preceding author proof defines k=s/(2-s)=1/3, x=v^2=1/441 and J(k,x)=F(s)/[s(1-s)]. Its exact expansion reads

  J(k,x)=g2(k)*x^2+g3(k)*x^3+g4(k)*x^4+R(k,x)

with the rigorously derived Cauchy remainder magnitude <=256*(4x)^5/(1-4x). The rational substitutions are

  g2(1/3)=55/972,
  g3(1/3)=3007/78732,
  g4(1/3)=8565077/340122240.

Thus the EXACT lower bound is

  J(1/3,1/441)
  >= (55/972)*x^2+(3007/78732)*x^3
     +(8565077/340122240)*x^4-256*(4x)^5/(1-4x)
   =1548995022721369/5621740898642842135680 > 1/5000000.

Since F(s)=s(1-s)*J and s(1-s)=1/4,

  F(1/2)>1/20000000.

The inherited Cauchy lemma is an AUTHOR derivation, still awaiting independent project review; this run separately executes exact arithmetic for its specialization.

### Upper bound on optimized B Chernoff information

For any finite laws P,Q, Jensen gives
-log(sum P^t Q^(1-t)) <= (1-t)*D(P||Q) <= D(P||Q),
for 0<=t<=1. The inequality log u<=u-1 gives
D(P||Q)<=chi^2(P||Q). In the two-point Bernoulli case with p=11/42 and q=10/42,

  C_B<=D(P_B||Q_B)<=chi^2(P_B||Q_B)
     =(p-q)^2/[q(1-q)]
     =(1/42)^2/[(10/42)*(32/42)]=1/320.

### Joint comparison

At the common t=1/2 the joint objective equals
50000 C_T+f_B(1/2), strictly larger than 50000 C_T.
Also 50000 C_T=75000(C_B+F(1/2)). Therefore

  C_mix(50000,1)-75001 C_B
   > 75000 F(1/2)-C_B
   > 75000/20000000-1/320
   =1/1600.

The entire witness and strict margin use rational inequalities, not a computed floating-point optimum.

## BRC observer and theorem scope

The carrier is the labeled T/B observation sequence; the observer is joint Chernoff discrimination with one common t, followed by additive declared cost. Source provenance and the two coefficient laws are retained: replacing them by a homogeneous total-only statistic discards the distinguishing information. This is a source-aware BRC S23 statistical result, not an X6 dynamical or native heartbeat-time calculation.

Theorem A is an analytic argument under the stated frozen model. Theorem B reuses the prior author Cauchy bound and carries out a separately checked exact rational specialization. The original unrestricted ten-label decoder minimax target still has the recorded open interval [1/2,2/3]. No new native Source CLAIM/Result, reviewer independence, or Foundation admission is asserted.

## Next open unit

For bounded integer budgets K=6..100 and declared rational s>sc, use certified interval evaluation of the TRUE common-exponent mixed Chernoff information for every feasible integer pair (m,n). Identify the smallest provable mixed-vs-pure instance, determine whether an optimum can use n>1, and classify the integer budget transitions. Preserve rigorous transcendental truncation and optimizer errors.
