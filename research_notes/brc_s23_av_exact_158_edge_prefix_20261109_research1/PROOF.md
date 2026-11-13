# S23/AV: exact 158 directed edge counts at every finite prefix

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Extends the exactly defined 79-symbol auxiliary observer at b642370f691040e3b800db1d9e3faf1e7ce36fcc, research_notes/brc_s23_av_carry_transition_histogram_20261109_research1/PROOF.md.
Research classification: exact theorem and independently executable certified integer computation for the S23/AV two-point auxiliary likelihood observer; not a native X6 dynamics or complete mother-model capacity result.

## Definitions and inherited hypotheses

Let r=ln(7)/ln(10/7) and
alpha=(2074774-380295r)/(79r-431), with 1/2<alpha<2/3 irrational (inherited certified theorem).
Let B=79, q=floor(79alpha)=46 and theta=79alpha-46 in (0,1).
For integer k>=1 define C_k=floor(79{k alpha}) in {0,...,78},
z_k={79k alpha}={k theta}, and
delta_k=floor(z_k+theta) in {0,1}.
The inherited all-index transition law reads C_(k+1)=(C_k+46+delta_k) mod 79.

For a finite K>=1 and state c in {0,...,78}, define E_(c,+)(K)
as the number of integers 1<=k<=K for which C_k=c and delta_k=1,
and E_(c,-)(K) for the same source state and delta_k=0.
The '+' edge goes from c to (c+47) mod 79 and the '-' edge goes to (c+46) mod 79.
For an integer n>=0 and rational beta let
A_K(beta;s)=sum_(k=1)^K floor((k+s)alpha+beta), where s=0 or 1.

## Theorem 1: exact directed edge prefix formula

For every integer K>=1 and every c=0,...,78,

E_(c,+)(K) =
  A_K((32-c)/79;1) - A_K((78-c)/79;0).                    (1)

Define F_c(K)=# {1<=k<=K:C_k=c} via the previously established
exact tail formula:
T_m(K)=sum_(k=1)^K [floor(k alpha+(79-m)/79)-floor(k alpha)]
for 1<=m<=78, with T_0(K)=K and T_79(K)=0;
F_c(K)=T_c(K)-T_(c+1)(K).
Then

E_(c,-)(K)=F_c(K)-E_(c,+)(K).                           (2)

Equations (1) and (2) give all 158 directed edge counts for
*every* finite K, using rational-shift floor sums and O(79) Euclidean
floor-sum evaluations rather than enumerating K states.

### Proof

Set x={k alpha}. The state C_k=c is equivalent to
c/79<=x<(c+1)/79. On this state, z_k=79x-c, so delta_k=1
is equivalent to 79x-c>=1-theta. Consequently the high-edge
event is exactly

  a_c<=(or equals)x<b_c,
  a_c=(c+1-theta)/79=(c+47)/79-alpha,
  b_c=(c+1)/79.

As 0<theta<1, for all c from 0 through 78 we have
0<=a_c<b_c<=1, including both boundary states.
For any 0<=a<b<=1 and 0<=x<1,
1_{a<=x<b}=floor(x+1-a)-floor(x+1-b).
Inserting the above a_c and b_c yields

floor((k+1)alpha+(32-c)/79)-floor(k alpha+(78-c)/79).

Summing over k proves (1). Partitioning state-c occurrences
by delta=0 versus delta=1 proves (2). QED.

## Theorem 2: telescoping of all high-edge occurrences

For every K>=1,

sum_(c=0)^78 E_(c,+)(K) = floor((K+1)theta),              (3)

sum_(c=0)^78 E_(c,-)(K) = K-floor((K+1)theta).          (4)

In particular, the finite-prefix high-branch discrepancy satisfies

 theta-1 < floor((K+1)theta)-K theta < theta,           (5)

and the high-branch asymptotic fraction is theta, without
assuming the 79-symbol process is Markov.

### Proof

Because z_k={k theta},
delta_k=floor((k+1)theta)-floor(k theta).
Sum for k=1,...,K and use floor(theta)=0. There is exactly
one source state at each k; (3) follows. Equation (4) is the
complement. Irrationality of theta gives the strict inequalities
in (5). QED.

## Certified computation of all 158 edge counts

The attached executable VERIFY_EDGE_PREFIX.py uses
Fraction throughout. It bounds ln(7) and ln(10/7) by the
positive atanh series, with explicit upper geometric remainders;
propagates them through the rational formula for alpha,
and computes each shifted floor sum by Euclid's algorithm.

For every floor sum separately it compares the rational lower
and upper-alpha endpoint totals. Every term is monotone in alpha,
so equality of the endpoint totals certifies *each individual term*
and hence the exact sum; subtraction takes place only after that
independent certification. Negative rational shifts are handled
by integer divmod before the floor-sum recurrence.

The test suite checks K=10,000, 10^6 and 10^12.
For K=10,000 it independently enumerates and certifies all actual
C_k and C_(k+1), matching all 158 edge counts. For each K it checks
nonnegative state partitions, the 158-edge sum K, and the exact
telescoping identity (3) via certified endpoint floors.

At K=10^12 the certified totals are:
  high = 262204504569, low = 737795495431;
  E_(0,-)=9339183472, E_(0,+)=3319044360;
  E_(1,-)=9339183480, E_(1,+)=3319044364;
  E_(39,-)=9339183489, E_(39,+)=3319044360;
  E_(77,-)=9339183486, E_(77,+)=3319044364;
  E_(78,-)=9339183502, E_(78,+)=3319044362.
All 158 edges have positive frequency in that finite prefix.
Actual complete execution evidence: RUN_EVIDENCE.txt.

## BRC observer reuse and scope

Carrier is the exact phase-aware state (C_k,z_k) and transition
label delta_k. The coarser integer-state observer C_k preserves
the state histogram but erases the edge choice. Equations (1)-(4)
recover the finite *aggregate edge counts* from alpha and K,
not the phase of a given unseen future k. For deterministic
step-by-step evolution retain z_k. This is typed auxiliary
BRC observer/fiber accounting (REUSE_APPLIED), with no native
six-axis or physical interpretation asserted.

## Remaining mathematical question

The present theorem controls finite prefix transition statistics.
Determine whether, for the S23/AV critical-cell covering
certificate at platform i=412, any witness interval can be
transported along either of the two edge types while preserving
its exact integer-cell coverage. Read the exact i=401..411 checker
and give one complete i=412 certificate or one explicit first
failure of witness transport. Transition counts alone do not
substitute for the exact-capacity coverage certificate.
