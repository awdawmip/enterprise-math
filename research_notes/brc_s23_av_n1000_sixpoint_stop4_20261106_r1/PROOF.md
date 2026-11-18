# S23 conditional AV: six-point exact stop4 n=1000 reconstruction lower bound

Date: 2026-11-06. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Verified predecessor: PR #1777 @84a5a82beee9f521f893f62b2ac66253fdf48a88, five-point stop1 bound delta_1000 > 92/125.

## Experiment, observer and minimax order

For a,c in [1/2,7/8], define z=(1-a)c, the tagged complete law
P_(a,c)=(a,z,1-a-z) on (stop1, stop3, stop4), and binary compressed
law B_(a,c)=(z,1-z) on (stop3, other). Conditioned on a,c, the 1000
observations are independent with common unknown a,c.

Define delta_1000 := inf_K sup_(a,c) TV(P_(a,c)^tensor1000,
B_(a,c)^tensor1000 K), where K ranges over all common stochastic kernels
from binary 1000-word observations to complete tagged 1000-word outputs.
The full sample may be reconstructed with arbitrary output correlations.

## Exact theorem

Under the preceding experiment,

    delta_1000 >= R_6 > 201/250 = 0.804,

where the exactly rational number R_6 is specified below and evaluated
by VERIFY.py with integer arithmetic.

Fix the observer fiber z=1/4. Choose six distinct stop4 masses

    q_j = (1/28, 3217/50000, 10091/100000,
           14447/100000, 9727/50000, 1/4).

For every j let a_j=3/4-q_j and c_j=1/(1+4q_j). Each
a_j lies in [1/2,5/7] and c_j lies in [1/2,7/8]. Directly,

    P_j=(a_j,1/4,q_j),    B_j=(1/4,3/4).

All six compressed 1000-word laws are identical. For any admissible K
their reconstructed output law Q=B_j^tensor1000 K is therefore one common Q.

Let T be the number of stop4 labels in the complete 1000-word. The
six disjoint exhaustive classification events E_j are the integer
intervals for T:

    [0,48], [49,81], [82,121], [122,168], [169,221], [222,1000].

Under P_j^tensor1000 the random variable T~Bin(1000,q_j).
Write S_j=P_j^tensor1000(E_j). With q_j=r_j/d_j reduced,

    S_j = {sum_(k=lo_j)^hi_j binom(1000,k) r_j^k
               (d_j-r_j)^(1000-k)} / d_j^1000.

Every S_j is an exact rational. As each E_j is a subset of the complete
output space, total variation gives

    TV(P_j^tensor1000,Q) >= P_j(E_j)-Q(E_j).

Summing the six inequalities, and using sum_j Q(E_j)=1,

    6 * max_j TV(P_j^tensor1000,Q) >= sum_j S_j - 1.

Consequently

    delta_1000 >= R_6 := (sum_j S_j - 1)/6.

The integer-binomial/Fraction checker evaluates the exact rational
quantity and proves R_6 > 201/250 with a strict rational comparison.
Its displayed decimal is

    R_6 = 0.804408737716329439880177025619762911876192... .

This is a lower bound on the minimax deficiency, not a determination
of the exact minimax value. The proof is finite, complete, and valid
for all stochastic reconstruction kernels K.

## BRC interpretation and limits of transfer

The retained tagged stop1/stop4 relation distinguishes six hidden
states on one fixed observer fiber. This is an exact BRC observer
information-loss witness for the chosen horizon of 1000. It improves
the earlier published five-point stop1 witness R_5>0.736 by at least
0.068. The frozen ten-label S23 mother problem R_beh(k,10), k=4,6,
still requires its own legal source-policy/encoder/decoder bridge.

Computation uses exact integers and Fraction. The bounded double
precision optimization that suggested q_j and the event boundaries
is not used by the proof: all six rational hypotheses and their
finite integer intervals are explicitly fixed before verification.
The code was executed locally on 2026-11-06; see RUN_EVIDENCE.txt.
Independent mathematical review is pending.
