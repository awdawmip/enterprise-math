# S23 tagged AV: exact full six-state maximum-likelihood partition at n=1000

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This extends the 60-strip six-hypothesis certificate at d154ff8a37271a509bddc835bd42ee32b8393eed. Current normative behavior is read separately. This theorem is about the auxiliary conditional tagged AV model, not the original ten-label S23 game.

## Definitions and result

For a,c in [1/2,7/8], the full one-trial distribution on tagged outcomes (stop1,stop3,stop4) is P_(a,c)=(a,(1-a)c,(1-a)(1-c)); the binary compressed observer is B_(a,c)=((1-a)c,1-(1-a)c). At n=1000, conditional trials are IID with one common hidden (a,c). Define

delta_1000 = inf_K sup_(a,c) TV(P_(a,c)^(tensor 1000), B_(a,c)^(tensor 1000) K),

with any parameter-independent stochastic kernel K, including correlated outputs.

Choose six stop4 probabilities q=(1/28,3217/50000,10091/100000,14447/100000,9727/50000,1/4). For each q let a=3/4-q and c=1/(1+4q). Each (a,c) lies in the lawful box and satisfies (1-a)c=1/4, so every binary law is identical and K produces a common Q for all six states. Their full laws are P_j=(3/4-q_j,1/4,q_j).

**Theorem:** Let D=700000, Z=D/4=175000, B_j=D*q_j, A_j=D-Z-B_j. For every integer u=0,...,1000 and s=0,...,1000-u define j*(u,s) as the smallest maximizing index j in

H_j(u,s)=B_j^u A_j^(1000-u-s).

Set

M = sum_(u=0)^1000 sum_(s=0)^(1000-u) [ C(1000,u) C(1000-u,s) Z^s max_j H_j(u,s) ].

Then the exact rational R_ML=(M-D^1000)/(6 D^1000) is a valid lower bound on delta_1000, and exact integer evaluation yields

**delta_1000 >= R_ML > 808109/1000000 = 0.808109.**

Decimal display: R_ML=0.808109549737987955234063560834168190788363733... . This is the exact maximum of the six-hypothesis *classification* objective for the listed states; it is not claimed to be the minimax reconstruction value.

## Proof

1. Every complete length-1000 word is classified by U=#stop4, S=#stop3 (T=1000-U-S stop1). Under hypothesis j, its probability is (B_j/D)^U (Z/D)^S (A_j/D)^T. The multinomial type multiplicity is C(1000,U) C(1000-U,S). Thus maximizing its probability across the six j is equivalent to maximizing H_j(U,S), with all comparisons integer-exact.

2. For i<j, B_j>B_i and A_j<A_i. At fixed u, H_j(u,s)/H_i(u,s) = (B_j/B_i)^u (A_j/A_i)^(1000-u-s), which strictly increases as s increases. If a higher indexed state beats a lower indexed state at s, it also beats it at every larger s. Choosing the smallest maximizing index on ties implies the winner index j*(u,s) is nondecreasing in s. Therefore the exact argmax partition for each u is a sequence of at most six contiguous S-intervals, discoverable with integer-only binary searches. The verifier checks all endpoints, adjacent transitions, increasing indices and complete interval coverage. Analytical pairwise monotonicity establishes correct class assignment between breakpoints.

3. Let E_j be the set of complete words assigned to hypothesis j by the exact argmax. These six events are disjoint and exhaustive. For any common Q, TV(P_j^(tensor 1000),Q) >= P_j^(tensor 1000)(E_j)-Q(E_j). Summing j yields 6 max_j TV(P_j^(tensor 1000),Q) >= sum_j P_j^(tensor 1000)(E_j)-1 = M/D^1000-1. The infimum over K preserves the lower bound.

4. Each interval probability numerator is computed by the exact identity
C(1000,u) B_j^u sum_(s=lo)^hi C(1000-u,s) Z^s A_j^(1000-u-s).
Starting from the exact integer term at lo, advance with T_(s+1)=T_s*(1000-u-s)*Z/((s+1)*A_j). Integer divisibility is asserted. The verifier visits all 501501 (U,S) types through 1854 exact winner intervals, finds switches at 295 U values, and proves the rational threshold by cross multiplication R_num*1000000 > 808109*R_den. It uses Python standard-library integers/Fraction/Decimal solely for decimal display.

## Coverage and next obligation

The actual executed script and stdout are in VERIFY.py and RUN_EVIDENCE.txt. Class interval counts per j: [33018,21821,26838,31354,35356,353114], totaling 501501 types; exact integers have numerator and denominator bit length 19420. No floating approximation participates in winner selection, probability accumulation or certificate inequality. Independent mathematical review and official task admission are pending. Next: optimize the lawful hypothesis parameters, consider m>6, and establish any proposed lawful bridge to the original S23 source/encoder/decoder problem.
