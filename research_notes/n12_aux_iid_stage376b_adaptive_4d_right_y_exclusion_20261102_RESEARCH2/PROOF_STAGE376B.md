# Stage376-B — exact adaptive four-parameter exclusion of the right-source upper y strip

Date: 2026-11-02 (Asia/Shanghai).
Status: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Input provenance and model

The scientific freeze is inherited unchanged from the Stage375-B handoff:
GLOBAL main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53,
EM main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419,
P000 blob@bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Current behavioral rules were separately read on 2026-11-02 at
GLOBAL main@673990aaae249ab9148e95c8cca59017ddb5b44a and
EM main@a982e23f441826119d0fe511070f523be1d9345f.
Verified predecessor: Stage375-B, commit 491aa9b46dfefaf6400e53f03f10382c01e59448.

Let k=0,1,2,3; B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9). For a source (x,y), define

r_k(x,y)=[4 B_k(x)+B_k(y)]/5 - m_k/160,
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|,
D(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|,
c(x,y)=[63 D(1/4,x)+D(3/4,x)+9 D(1/4,y)+7 D(3/4,y)]/256.

This retains the sixteen separately weighted anchor/word audit comparisons and four independent residual channels of the frozen Bernoulli/BRC two-source auxiliary model. Let q_* be the pinned unique r_0=r_1=0 root; beta_*=b(q_*). At E=11/5000 minimize T(P,Q)=33/1024+c(P)+c(Q) over real P,Q in [0,1]^2 subject to b(P)+b(Q)<=2 beta_*+E.

## Theorem

Every global minimizer, after the source ordering of Stage375-B, satisfies

P in (577/2500,469/2000) x (11/20,14/25),
Q in (473/2000,239/1000] x (143/250,72/125).

Thus the right-source upper y-bound improves from 0.5794 to 0.576.

More precisely, every budget-feasible pair in the whole **closed four-dimensional box**

R=[577/2500,469/2000] x [11/20,14/25]
  x [473/2000,239/1000] x [72/125,2897/5000]

has c(P)+c(Q)>C_0, where C_0 is the exactly evaluated cost of a specified feasible rational comparator.

## Exact comparator and dual separation

Set P_0=(231138/10^6,555681/10^6) and Q_0=(237807/10^6,575694/10^6). The executable exact Fraction checker verifies the inherited root isolation and exact comparison:

b(P_0)+b(Q_0)<2 beta_*+11/5000 < B_up=61/6250,

C_0=c(P_0)+c(Q_0)
   =16174439790495832521/256000000000000000000.

With lambda=13/10, write L(P,Q)=c(P)+c(Q)+lambda[b(P)+b(Q)] and

H=C_0+lambda B_up
 =19422567790495832521/256000000000000000000.

The checker performs a **genuinely adaptive four-axis dyadic partition** of R. At each four-dimensional box J=J_P x J_Q, it computes exact certified lower bounds b_J and c_J for total b and c using the independent four residual channels and all sixteen separately weighted audit comparisons. Each leaf closes by one of:

- BUDGET: b_J>B_up. Then J contains no feasible pair.
- DUAL: c_J+lambda b_J>H. Then any feasible pair in J satisfies

  c(P)+c(Q)=L(P,Q)-lambda[b(P)+b(Q)]
    >=c_J+lambda b_J-lambda B_up > C_0.

The lower bounds are rigorous on each *entire continuous box*: the extrema of the cubic B_k(z) on an interval occur at its endpoints and, if interior, at z=k/3. For target t and an interval [l,u], the distance lower bound is 0 when t is inside [l,u], otherwise min(|t-l|,|t-u|). Apply the distance rule separately to every signed residual and every anchor/word comparison with its positive weight, then sum. No sampled-point assertion is used for all-real coverage.

On a nonclosed box the checker splits the longest of its four coordinate intervals at its exact rational midpoint. It verifies both splits cover the original box, and at completion checks that (i) leaves=splits+1 and (ii) the exact rational sum of leaf four-dimensional volumes equals volume(R). Shared boundaries are included. This is a single joint four-parameter budget/cost decision tree, not a pair of independent 2D source covers.

## Executed exact certificate

Actual Python Fraction execution (repeated without emitting a CSV, with byte-identical stdout) returned

STAGE376B_EXACT_COUPLED_FOUR_PARAMETER_RIGHT_Y_EXCLUSION_PASS

with 66,245 splits and **66,246 closed leaves**: 19,175 BUDGET and 47,071 DUAL, maximum depth 38, no unresolved cells. The minimum reported strictly positive rational closure margin is

3889567101150619/16777216000000000000000000.

The deterministic full CSV has 66,246 rows, 15,996,423 bytes, SHA256
5f0452e3b8488d7a843233c0c12f5f6b2cc9cf6916a38e8f5cbdf143b9bfb8ac.

The full executable source REPRO_STAGE376B.py is supplied alongside this proof. To reproduce the certificate run:
python REPRO_STAGE376B.py --emit CERTIFICATE_STAGE376B_4D_RIGHT_Y.csv

The original full CSV was generated and hash-checked locally. The remote source and executed stdout are byte-identical to the actually executed originals. The compact feasible set and the feasible rational comparator give existence of a minimizer. Since no feasible point of R can minimize, combining with Stage375-B yields the theorem.

## Next question and project status

Stage377-B: use cell-dependent dual multipliers, sign-aware algebraic support, or a more targeted budget/cost branch-and-bound to exclude a lower y_Q strip, starting with y_Q<=23/40=0.575, or construct a strict feasible rational counterexample to the algebraic cusp candidate. The algebraic audit cusp is y_alpha=(1+sqrt(13))/8. Record all unfinished four-dimensional cells and preserve frozen scientific inputs. Full global optimality and the native P000 X6 observer-preserving transfer remain separate open research questions.

Native control read returned CONTROL_QUOTA, and session_start was rejected with STATIC_READONLY_SCOPE_DENIED (operation_sent=false). GitHub authentication is awdawmip, with repository write access. This portable research note is not a native CLAIM, Source Result, or independent Driver acceptance.
