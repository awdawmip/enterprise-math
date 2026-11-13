# S23/AV: exact finite-history prediction risk via Diophantine best returns

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE PROVED DERIVATION AND EXACT FINITE CERTIFICATE; independent review pending.
Frozen scientific pin: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous proof and readout: enterprise-math@5d16d7e7428440cae7b88e814422a9599c19d750, research_notes/brc_s23_av_linear_word_complexity_20261109_research1/PROOF.md.
This is the auxiliary S23/AV irrational rotation, not a claim about native X6 physics, the mother ten-label capacity, Result or Review.

## Definitions

Set r=ln(7)/ln(10/7), alpha=(2074774-380295r)/(79r-431), and theta=79 alpha-46. The previous irrationality result and rational bounds give 1/4<theta<1/3, theta irrational. With phase x on the circle [0,1), the B=79-symbol observable is

\[
C_j(x)=\lfloor 79\{x+j\alpha\}\rfloor.
\]

An m-symbol history consists of j=0,...,m-1, and the target is the next symbol j=m, under the uniquely invariant uniform phase measure. Earlier work proved the precise best deterministic prediction error

\[
\varepsilon_m=\min(t_m-L_m,R_m-t_m),\quad t_j=\{-79j\alpha\}=\{-j\theta\},
\]

where L_m,R_m are consecutive old cutpoints on either side of t_m among 0,1,t_1,...,t_(m-1). This is the declared BRC-style auxiliary observer; the phase or its residual is additional information not present in the m integer symbols.

## Theorem 1 — exact best-return identity, all history lengths

For every integer m>=1,

\[
\boxed{\varepsilon_m=\min_{1\le d\le m}\|d\theta\|},\qquad
\|y\|=\min_{n\in\mathbb Z}|y-n|.
\]

Proof. Identify the endpoints 0 and 1 of the circle. The distance to the closer neighbor of t_m among all old cutpoints, including 0, is exactly the smallest circular distance between t_m and one of t_j (0<=j<m). These distances are \|(m-j)\theta\| because t_m-t_j=-(m-j)\theta (mod 1). The values m-j run through 1,...,m. All distances are positive because theta is irrational. QED.

The risk is nonincreasing and positive. There are m+1 distinct circle points 0,theta,...,m theta (mod 1), whose m+1 cyclic gaps sum to 1. At least one gap is <1/(m+1), since equality of every gap would make theta rational. Its endpoints differ by d theta (mod 1) for some 1<=d<=m. Hence

\[
\boxed{0<\varepsilon_m<1/(m+1)}.
\]

This gives a proved O(1/m) quantitative prediction guarantee, improving the earlier qualitative limit epsilon_m -> 0.

## Theorem 2 — exact convergent jump schedule, all history lengths

Write the regular continued fraction theta=[0; a_1,a_2,...] and its convergents p_n/q_n. Because theta lies in (1/4,1/3), the initial convergents are 0/1,1/3,1/4,5/19,... . For every n>=0 and q_n<=m<q_(n+1),

\[
\boxed{\varepsilon_m=|q_n\theta-p_n|}.
\]

Consequently risk is constant throughout each half-open integer interval [q_n,q_(n+1)), and strictly drops exactly at convergent denominators.

Proof. Consecutive convergents (p_n,q_n) and (p_(n+1),q_(n+1)) form a basis of the integer lattice, determinant +/-1. Put e_n=q_n theta-p_n and e_(n+1)=q_(n+1)theta-p_(n+1); their signs are opposite, and |e_(n+1)|<|e_n|. For arbitrary 1<=d<q_(n+1) and integer p, write (p,d)=A(p_n,q_n)+B(p_(n+1),q_(n+1)) with integer A,B. If B=0 then A>=1, giving |d theta-p|=A|e_n|>=|e_n|. If B<0 then A>=1 because d>0; A e_n and B e_(n+1) have equal signs, so their sum has magnitude at least |e_n|. If B>0 then d<q_(n+1) implies A<=-1, and again the two error terms have equal signs, with magnitude at least |e_n|. Thus every candidate obeys \|d theta\|>=|e_n|. At d=q_n this bound is attained: all stated convergents have p_n nearest to q_n theta (the first since theta<1/2, the remaining by standard convergent error bound). Now apply Theorem 1. QED.

For any desired asymptotic one-step error tolerance eta>0, the smallest adequate finite history is the first convergent denominator q_n with |q_n theta-p_n|<=eta. This identifies an exact constructive compression/prediction tradeoff instead of scanning every history length.

## Certified finite computation

VERIFY_BEST_RETURN.py computes strict logarithm intervals using 160 terms of a positive rational atanh series and a geometric remainder, then propagates them through alpha and theta. The exact 24-decimal-digit enclosure is

\[
262204504569236716045286/10^{24}<\theta<
262204504569236716045287/10^{24}.
\]

The first sixteen partial quotients are [0,3,1,4,2,1,2,3,1,1,2,3,1,10,3,1]; all are certified by exact rational interval inversion, rather than inferred from floating-point approximations. The convergent denominators that are records up to m=200000 are exactly

1,3,4,19,42,61,164,553,717,1270,3257,11041,14298,154021.

The verifier checks each integer d from 1 through 200000 by strict integer rational interval decisions; it compares the entire record list against the continued-fraction list. For m=1,2,3,4,8,16,32,64,128 it independently reconstructs and sorts the old cutpoints, and checks that the partition-neighbor prediction risk matches the best-return formula.

Selected certified open intervals (every width 10^-18):
- m=2: (0.262204504569236716, 0.262204504569236717);
- m=4: (0.048818018276946864, 0.048818018276946865);
- m=32: (0.018114413184502395, 0.018114413184502396);
- m=128: (0.005525221276560321, 0.005525221276560322);
- m=1000: (0.000629776142725404, 0.000629776142725405);
- m=10000: (0.000071382003984159, 0.000071382003984160);
- m=200000: (0.000001741591757988, 0.000001741591757989).

No float-based decision occurs in the script. All-m conclusions are by the exact arguments above; the finite computation independently confirms the listed coefficients, intervals and 200000-point record coverage.

## Next scientific unit

The integer carry readout and its phase residual form an exactly analyzed auxiliary BRC observer: the finite-history Bayes loss improves at Diophantine return times, despite p(m)=79m and zero topological entropy. Next implement a direct Bayes predictor from phase partition atoms at convergent lengths and account for preprocessing/input/bit costs. Independently inspect the frozen S23/AV coverage checker at plateau i=413 to test whether geometric covering witnesses can be transferred by carry-phase classes; prediction risk alone is not a geometric covering witness. Retain full source/provenance of any verified local transport.