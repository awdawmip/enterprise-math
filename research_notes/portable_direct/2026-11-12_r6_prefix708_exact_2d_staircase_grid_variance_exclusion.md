# PREFIX-708-R6 — Exact 1024-by-1024 staircase exclusion certificate

Date: 2026-11-12 (Asia/Shanghai)
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Mother objective: PREFIX-675, maximizing the frozen two-stream auxiliary clock variance statistic over the full square D=[0,1/2]^2.
Prior sources: PREFIX-700 integer survivor recurrence, PREFIX-705 survivor stochastic monotonicity, PREFIX-706 certified witness, PREFIX-707 partitioned cell and Efron-Stein inequalities.
Evidence grade: AUTHOR_RECOMPUTED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Main theorem (uniform all-real-q staircase exclusion)

Let T_p be the frozen independent first-stop clock, p in [0,1/2], with first-stop survivor tails from the 189-row labelled recurrence. For two independent clocks let Y(p,z)=max(T_p,T_z), mu(p,z)=E[Y(p,z)] and W(p,z)=Var(Y(p,z)). Define V_q=q^2 W-q mu for every real q>=2. Let e=(0,3/20).

Partition [0,1/2] into 1024 closed intervals I_i=[i/2048,(i+1)/2048], i=0,...,1023. For l_i,r_i their endpoints, define the exact rational number

u_i = min { C(r_i)+A(l_i)-A(l_i)^2, 189+D2(l_i)-d(r_i)-d(r_i)^2 },

where A(t)=E[N_t], C(t)=E[N_t^2], d(t)=E[189-N_t], D2(t)=E[(189-N_t)^2].

With b=559812917/1000000, define the exact finite index set

S = {(i,j): 0<=i,j<1024 and u_i+u_j<b},
R = union over (i,j) in S of (I_i times I_j).

**Theorem 708.1.** The set S has exactly 345931 ordered pairs. For every real q>=2 and every (p,z) in R,

V_q(e)-V_q(p,z) > (2672/1000000) q^2 > 0.

Thus all of R is excluded from the global maximizer set on D, and

area(R)=345931/4194304,
area(R)/area(D)=345931/1048576 = 32.990550994873047... %.

The excluded-area ratio relative to the 2026-11-11 PREFIX-707 four-rectangle certificate is exactly 28020411/16777216, approximately 1.67015. This comparison is between certified areas; it does not assume literal containment between their exclusion sets. Their union may be reused.

## Exact proof

The PREFIX-705 polynomial Bernstein certificate establishes nondecreasing survival tails s_n(t)=Pr(N_t>n) for 0<=t<=1/2. It follows that A,C are nondecreasing, while d,D2 are nonincreasing. On this count domain A>=25 and d>=0. The functions a-a^2 and -d-d^2 are decreasing. Hence, for any p in I_i,

Var(T_p)=C(p)+A(p)-A(p)^2
        =189+D2(p)-d(p)-d(p)^2
        <=u_i.

For independent T_p and T_z, Efron-Stein gives
W(p,z)=Var(max(T_p,T_z))<=Var(T_p)+Var(T_z)<=u_i+u_j.
The frozen rational witness from PREFIX-706 satisfies W(e)-mu(e)/2>b. Because mu(e)>=0 and q>=2, W(e)-mu(e)/q>=W(e)-mu(e)/2>b. For every selected cell (i,j), this implies

[V_q(e)-V_q(p,z)]/q^2
 = W(e)-mu(e)/q - W(p,z)+mu(p,z)/q
 > b-u_i-u_j.

Every first-stop clock is nonnegative, so mu(p,z)>=0. The exact rational computation below establishes
min over (i,j) in S of (b-u_i-u_j) > 2672/1000000.

These inequalities hold on all closed selected cells, including boundaries. Since the 1024-by-1024 cells have pairwise disjoint interiors and each has area 1/2048^2, the count 345931 gives the claimed area. QED.

## Finite certificate and algorithm

The companion Python checker reconstructs the 189 integer survivor rows (9529 nonzero count cells) with the original WIDTH threshold test, computes A,C,d,D2 at all 1025 dyadic grid endpoints using integer arithmetic and Fraction, and forms each u_i. It sorts the exact upper bounds and evaluates

k_i = number of j with u_j < b-u_i
    = bisect_left(sorted(u), b-u_i).

It verifies the exact equalities

sum_i k_i = 345931,
345931/1024^2 = 345931/1048576,
(area fraction)/(16/81) = 28020411/16777216,

and verifies every row's strictly positive last eligible gap using exact rationals. The minimum of these gaps exceeds 2672/1000000. Selection is therefore an exhaustive finite certification of all 1024^2 ordered grid-cell candidates, not a floating-point sampling experiment.

Observed local recomputation using the same recurrence and exact Fraction logic: 345931 cells selected, minimum positive gap approximately 0.0026727575985, certificate ALL_CHECKS_PASS PREFIX708-R6. Approximate decimal displays are explanatory; the deciding comparisons are rational.

## Provenance, scope, and next question

The theorem concerns the frozen auxiliary statistical observer. It retains the original 189-level labelled count recurrence, independent stream model, and existing provenance. It uses the earlier published PREFIX-705 monotonicity and PREFIX-706 witness certificates as dependencies; those underlying Bernstein/witness calculations are not independently rerun by this script. It neither replaces P000 nor asserts an X6 native physical law.

Next: improve candidate exclusion with joint-clock W(p,z) upper bounds instead of the Efron-Stein sum, or adaptively subdivide only near the strict boundary of R. For 12<=q<=24, apply the endpoint-affine parameter lemma to both t=1/24 and t=1/12, using exact Bernstein certificates on remaining cells. The global optimizer location and full PREFIX-675 mother problem remain open.
