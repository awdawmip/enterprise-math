# S23 AV: exact three-hypothesis deficiency exceeds 1/2 at n=45

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor exact n=1000 six-hypothesis author certificate: b2ce7a69d6784bc826a3ed9281e7bbb671599f8b (Draft PR #1777).

## Statement

Let P_(a,c)=(a,(1-a)c,(1-a)(1-c)) on labeled (stop1,stop3,stop4), B_(a,c)=((1-a)c,1-(1-a)c), a,c in [1/2,7/8]. For n conditionally independent repetitions with shared unknown (a,c), define delta_n = inf_K sup_(a,c) TV(P_(a,c)^tensor n, B_(a,c)^tensor n K), K a parameter-independent stochastic kernel.

**Theorem:** An explicit rational three-hypothesis certificate establishes delta_45 >= R3(45) > 501/1000 > 1/2; moreover **for every n>=45**, delta_n >= R3(45) > 501/1000. For this fixed three-hypothesis certificate, its lower bound first exceeds the corresponding endpoint-pair half-TV at n=42 and first exceeds 1/2 at n=45 (finite exhaustive check n=1..45). This is not a claim that 42 or 45 is the earliest possible transition among all hypothesis selections or that delta_n is known exactly.

## Rational witness and full word-space certificate

Take denominator D=56, common stop3 weight Z=14, stop1 weights A=(40,35,28) and stop4 weights B=(2,7,14), so the three full distributions are P_j=(A_j,Z,B_j)/56. The lawful original parameters are (a,c)= (5/7,7/8), (5/8,2/3), (1/2,1/2), respectively. They all satisfy (1-a)c=Z/D=1/4; therefore B_(a,c)^tensor n has identical law for all j. Any kernel K gives the same reconstructed Q for all j.

For a length-n tagged word with u stop4, s stop3 and v=n-u-s stop1, its likelihood is L_j=56^(-n) B_j^u 14^s A_j^v. Assign each word to the smallest index maximizing L_j; the events E_0,E_1,E_2 form a partition. Their summed correct classification probability is M_n/56^n, where

M_n = sum_(u=0)^n sum_(s=0)^(n-u) C(n,u)C(n-u,s)14^s
      max { 2^u 40^(n-u-s), 7^u 35^(n-u-s), 14^u 28^(n-u-s) }.

For every Q, TV(P_j^n,Q) >= P_j^n(E_j)-Q(E_j). Sum over j and use sum_j Q(E_j)=1. Thus
**delta_n >= R3(n) := (M_n-56^n)/(3*56^n).**
Every count type and its exact multinomial multiplicity appears in the sum.

At n=45, exact integer evaluation yields
M_45 = 11671160188453256537179383381392773347838541974475787594372279588210185299003107
56^45 = 4660808027410506132900915088997417305944355117847144307414511042169984019070976.

The exact comparison 1000*(M_45-56^45) > 1503*56^45 holds, proving R3(45)>501/1000; noncertifying decimal R3(45)=0.501368869933742... .

For n>=45, project any common reconstructed n-word distribution Q_n and true P_j^n onto their first 45 coordinates. TV contracts under this projection. Apply the n=45 partition inequality to the resulting Q_45, proving delta_n>=R3(45) without any monotonicity assertion for delta_n.

## Finite comparison with endpoint pair

Let T_n = sum_(u,s) C(n,u)C(n-u,s) 14^s |2^u40^v - 14^u28^v|. Then half of endpoint total variation is T_n/(4*56^n). The three-hypothesis certificate strictly exceeds it iff 4*(M_n-56^n)>3*T_n. Exact integer enumeration for n=1,...,45 gives first strict crossing at n=42, and first R3(n)>1/2 at n=45; n=41 and n=44 respectively fail these tests. Full integer witnesses are in VERIFY.py and RUN_EVIDENCE.txt.

Any ordinary **two-hypothesis triangle/data-processing** lower certificate equals (TV(P_i^n,P_j^n)-TV(B_i^n,B_j^n))/2, a number <=1/2. Thus the bound strictly above 1/2 documents a genuinely multi-hypothesis obstruction for this lower-bound method.

## Observer discipline, evidence and scope

BRC mapping: retain the labeled stop1/stop3/stop4 weighted branch population, multiplicity and its exact integer histogram; the compression merges stop1 and stop4 at fixed stop3 probability. Equal compressed totals do not identify hidden branches. Count grouping is justified for this declared finite word-likelihood observer and horizon. BRC status COMPOSE_APPLIED (observer/fiber distinction); computation is standard exact rational probability algebra, not a new native heartbeat/BRC primitive.

VERIFY.py uses the standard library, enumerates 17,295 count types across n=1..45, checks legal inputs, all finite integer inequalities and exact comparisons. RUN_EVIDENCE.txt is the actual captured output of the identical verification program. No float/LP solver influences the certified inequalities. This auxiliary conditional tagged-AV result needs a separate lawful source/encoder/decoder bridge to the frozen original ten-label S23 R_beh(k,10). Independent review, a formal Task CLAIM and project admission have not been asserted.

Next unresolved unit: determine whether delta_44>1/2 via a different lawful multiway certificate or establish a box-wide kernel upper bound <=1/2 at n=44; also pursue the original ten-label bridge.
