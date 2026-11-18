# S23 conditional AV: Hoeffding rate and exact five-point n=1000 witness

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous author frontier: ea3d2dda479970826418a4e770ae3c646e438d5b (all-n Chebyshev packing and three-point n=1000 certificate).
Mother objective: lawful six-source/ten-label S23 R_beh(k,10), k=4,6.

## Experiment and information typing

For real a,c in [1/2,7/8], let z=(1-a)c and
P_(a,c)=(a,z,1-a-z) on tagged complete labels (stop1,stop3,stop4);
B_(a,c)=(z,1-z) on binary (stop3,other).

For n>=1, the same unknown (a,c) governs n conditionally independent observations.
Define delta_n = inf_L sup_(a,c) TV(P_(a,c)^tensor n, B_(a,c)^tensor n L),
where L is any single row-stochastic common reconstruction kernel from the n binary observations to n complete labeled observations. It may correlate the outputs but cannot depend on the hidden parameter. The BRC typed observer is the stop3 projection; the stop1/stop4 distinction is retained in the complete source distribution, and the chosen future operation is common stochastic reconstruction at horizon n.

## Theorem 1: exponential multi-hypothesis bound

For every integer n>=1 and m>=2,

delta_n >= max{0, 1-1/m-2 exp[-9n/(392(m-1)^2)]}.  (1)

For every integer n>=1000,

1-delta_n <= (28/3) sqrt(log(n)/n) + 2/n^2.       (2)

The logarithm is natural.

Proof. Fix z=1/4 and take m legal hypotheses with
a_j=1/2+3j/[14(m-1)], c_j=(1/4)/(1-a_j), j=0,...,m-1.
They satisfy a_j in [1/2,5/7], c_j in [1/2,7/8], and (1-a_j)c_j=1/4.
Thus B_j^tensor n is identical for every j. Whatever common L is used,
Q=B^tensor n L is the same reconstruction distribution for all j.

Let X be the count of complete stop1 labels among n trials. Under j,
X~Bin(n,a_j). The a_j are spaced by Delta=3/[14(m-1)]. Partition the
complete sample space into E_j according to the nearest a_j to X/n
(fixed tie rule). If |X/n-a_j|<Delta/2, the classification is correct.
Hoeffding's Bernoulli inequality yields

P_j(E_j^c) <= P_j(|X/n-a_j|>=Delta/2)
            <= 2 exp[-2n(Delta/2)^2]
            = 2 exp[-9n/(392(m-1)^2)].

For each j, TV(P_j^tensor n,Q)>=P_j(E_j)-Q(E_j). The events E_j form
a partition and sum_j Q(E_j)=1; hence

m sup_j TV(P_j^tensor n,Q)
  >= sum_j[P_j(E_j)-Q(E_j)]
  >= m[1-2exp(-9n/(392(m-1)^2))]-1.

Dividing by m and taking the infimum over all common L gives (1);
nonnegativity supplies max{0,...}.

For n>=1000, set x=(3/28)sqrt(n/log n) and m=1+floor(x).
Since n/log n increases for n>e and x(1000)>1, m>=2.
We have m>x and m-1<=x, so
9n/[392(m-1)^2] >= 9n/(392x^2)=2log n
and 1/m<1/x=(28/3)sqrt(log n/n).
Substitute in (1) to obtain (2). QED.

This establishes a rate O(sqrt(log n/n)) for the auxiliary deficiency
gap, strengthening the previously saved explicit Chebyshev O(n^(-1/3))
rate. It does not assert a matching optimal rate.

## Theorem 2: exact rational n=1000 bound

For the following five legal hypotheses with common z=1/4, define
a=(1/2, 111/200, 61/100, 663/1000, 5/7),
c=(1/2, 50/89, 25/39, 250/337, 7/8).

Let X count stop1 among 1000 complete trials and partition the output by
E0=[0,527], E1=[528,582], E2=[583,636],
E3=[637,688], E4=[689,1000].
Let S_j=Pr_(a_j)[X in E_j].
If a_j=r_j/s_j, each S_j is exactly the following rational number:

S_j = [sum_(k=lower_j)^(upper_j)
        binom(1000,k)*r_j^k*(s_j-r_j)^(1000-k)] / s_j^1000.

For any common reconstruction L, Q=B^tensor1000 L is identical for
all five hypotheses, so the disjoint event inequality gives

delta_1000 >= (S_0+S_1+S_2+S_3+S_4-1)/5 > 92/125 = 0.736.  (3)

VERIFY.py checks the strict inequality by exact integers and Fraction
rather than a float approximation. Executed result for the exact
rational left-hand side: 0.7360749898014312019670508580885342509050...
Previously saved exact three-point witness: approximately 0.666338327539439.

## Scientific scope and next problem

The general bound follows analytically from Hoeffding and event
partitioning; the n=1000 strict bound has an executed exact-rational
certificate in VERIFY.py and RUN_EVIDENCE.txt. These are author-side
results pending independent review, not formal mathematical admission.

The binary projection loses tagged stop1/stop4 information in the
conditional AV row. The original frozen six-source/ten-label S23 game,
its lawful source policy, encoders, decoders, loss, and minimax order
still require an explicit bridge before a bound on R_beh(k,10) follows.

Next: optimize the five- or six-point rational grid and exact integer
partition; independently review the n>=1000 rate argument; and
construct/test a legal source-tagged map from the frozen ten-label S23
experiment to the auxiliary AV observer.
