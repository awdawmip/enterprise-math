# R132 — Exact one-integer feasibility for arbitrary correlated carry words

Date: 2026-11-14 (Asia/Shanghai). Author-side S23 auxiliary mathematical research; independent mathematical review pending. Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: R131, branch research/r1-r131-pulse-query-trace-20261114, immutable commit ab4a62ab55bd83ac99f00c678d7d37acbd76baec; R130 research commit 7040bd2b6f134ea105f75370f0e35f1294818b64.

## Question and scope

Given integers B>=2, m>=1, and an arbitrary specified word w in {0,1}^m, does there exist real theta in the open interval (0,1) such that

  S_i(theta) = 1[ {(B+i)theta} < {theta} ] = w_i,

simultaneously for i=0,...,m-1, with {z}=z-floor(z) and strict inequality? This is the S23 auxiliary family x=0, A=B, d=E=1. B is binary encoded and may be arbitrarily large. The requested output is membership and one rational witness, not the complete ordered trace.

## R132.1 Exact floor-difference identity

For every real theta in (0,1) and integer n>=1,

  1[ {(n+1)theta} < {theta} ]
     = floor((n+1)theta) - floor(n theta).

Proof. Put u={n theta} in [0,1). Since theta in (0,1), the floor difference is zero if u+theta<1 and one otherwise. In the first case {(n+1)theta}=u+theta>=theta, so strict comparison is false. In the second case {(n+1)theta}=u+theta-1<theta, so it is true; equality u+theta=1 belongs to this second case. QED.

This is the classical lower-mechanical-word floor-difference construction, specialized here to the correlated S23 observer. The basic floor-difference identity is not a novelty claim.

## R132.2 Exact single-integer interval algorithm

For i=-1,0,...,m-1 put D_i=B+i, and define prefix sums s_{-1}=0, s_i=sum_{j=0}^i w_j. Telescoping R132.1 shows that the required word is realized precisely when there are theta in (0,1) and an integer

  q=floor((B-1)theta),  0<=q<=B-2,

such that all m+1 floor bands hold:

  q+s_i <= D_i*theta < q+s_i+1, i=-1,...,m-1.   (1)

For any q, let L_i(q)=(q+s_i)/D_i, U_i(q)=(q+s_i+1)/D_i. These are rational numbers with positive denominator. For q in 0..B-2 all lower bounds satisfy 0<=L_i(q)<1: for i>=0 use s_i<=i+1 and
q+s_i<=B-2+(i+1)=D_i-1<D_i; for i=-1 use q<=B-2<D_-1. All U_i(q)>0.

Thus (1) has a solution theta in (0,1) if and only if

  L_i(q) < U_j(q)     for every i,j in {-1,...,m-1}.   (2)

Indeed necessity is immediate, while sufficiency follows by choosing theta strictly between max(0,all L_i) and min(1,all U_j). These bounds are strictly ordered by (2) and the q-range observations above.

Cross multiplication of (2) gives one strict *linear integer inequality in q*:

  (j-i)*q < D_i*(s_j+1) - D_j*s_i.     (3)

For i=j, (3) is automatic. For c=j-i>0 and integer R=the RHS,
(3) is equivalent to q<=ceil(R/c)-1. For c<0 it is equivalent to q>=floor(R/c)+1. Intersect those O(m²) half-lines with 0<=q<=B-2.

**Theorem.** The exact feasible q set for a target word is either empty or a contiguous integer interval [q_min,q_max]. It can be computed by O(m²) signed-integer comparisons and divisions on O(log(B+m))-bit operands. A word is attainable if and only if q_min<=q_max.

If feasible, choose q=q_min, and set

  L=max(0, (q+s_i)/D_i for -1<=i<m),
  U=min(1, (q+s_i+1)/D_i for -1<=i<m),
  theta_w=(L+U)/2.

Then 0<theta_w<1 and all floor bands (1) hold (their upper endpoints are strict), so theta_w is a rational witness for exactly the desired word.

Proof of necessity: each attainable theta defines q=floor((B-1)theta), whose floor constraints imply every pairwise inequality (3). Sufficiency is the midpoint construction above. The projection of all such feasible (q,theta) pairs onto q is the intersection of integer half-lines, hence an integer interval without gaps. QED.

**Bit complexity.** Prefix sums cost O(m) additions; O(m²) inequalities require integer arithmetic on O(log(B+m))-bit data, plus O(m) rational comparisons and one exact midpoint. Standard exact arithmetic yields time polynomial in m+log B and O(m) retained working values, without scanning B potential q values or the Theta(B) parameter event cuts. Rational witness numerator and denominator are bounded in magnitude by O((B+m)^2), hence have O(log(B+m)) bits. The statement covers every m>=1, B>=2, every bit pattern (feasible or infeasible), all strict boundary cases.

## R132.3 Output-sensitive event lower bound

The first coordinate S_0 is the R131.1 pulse indicator and has 2B-3 genuine changes on (0,1). Every change of S_0 changes the complete m-bit word regardless of the other coordinates. Therefore any *explicit complete ordered trace* must emit at least 2B-3 distinct event records, growing exponentially in the input bit length along B=2^n. R132.2 decides one arbitrary requested word and recovers a rational witness in polynomial bit complexity. This is a separation between distinct output contracts, not a universal lower bound for succinct symbolic traces or an equal-output runtime-speedup claim.

## Exact computation

Companion check_r132.py implements equation (3) using exact Python integers and fractions.Fraction. An independent oracle enumerates exact integer-crossing cuts of (B+i)theta and (B+i-1)theta, evaluates all singleton cuts and open-cell representatives, and deduplicates the actually attained words.

Executed B=2..18 and m=1..8: 136 input parameter groups, all 8,670 binary word queries, 14,600 exact parameter atom representatives, 3,236 feasible words. Every decision agreed with the independent event enumerator; every returned witness was re-evaluated against the original strict fractional-part predicates. Additional checks: 5,000 seeded random target words, 790 with verified witnesses; B with 151 decimal digits and m=64, recovering four exact witnesses. Outcome R132_ONEINTEGER_FEASIBILITY_PASS.

Measured at m=12 and B=64,256,1024,4096, the exact membership decision and full exact trace enumerator were independently run on the same CPython/Fraction process, 3 repetitions per input, using medians. These produce different outputs; see COST.md for measured times and verification_r132.json for exact data.

The algebra establishes the stated infinite-family theorem; the finite program checks its implementation and strict endpoints. This is an author-side auxiliary S23 mathematical result, not a native X6/Cell/Link/Port transfer, authenticated CLAIM, independent review, or Foundation promotion.

## Further frontier

Can the pairwise O(m²) bounds be reduced to O(m log m) or O(m) while preserving full exactness? Determine the maximal extension to d=E and rational x (or general E/d) for which the q-projection remains a gap-free integer interval. Compare the complete bit cost, preprocessing, memory, and witness recovery of this exact query solver with R130 trace/index and R127/R126 integer feasibility methods, and separately investigate a typed native observer transfer.
