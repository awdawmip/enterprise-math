# R5 F4: Four-signature rank-two convex-rate compression theorem

2026-10-29 (Asia/Shanghai). Author-side portable derivation. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. No Source CLAIM, Result, Driver review, native X6 dynamics or physical calibration is asserted.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@9214cbb64c3d620dcfdae9cec0559b3bff3b9cca; enterprise-math main@07d7781680ed037c98970164d35ba5ee4fb0ee86. Prior research: research_notes/brc_r5_repeated_lr_3point_no_go_20261028_t2337/RESEARCH.md (project commit ebf1df364abc3bbb14b784fba47701b80ea9e627). P000, the ACTIVE joint-residual worldview, and the existing portable research protocol remain unchanged.

## Model

Let S be any finite set of distinct positive terminal likelihood ratios containing r. At time 1, hidden origins i=A,B, distinguishable to a full-history strategy but not to a likelihood-ratio strategy, carry Q masses a_i>0 and P/Q ratio r. Other origins stop at time 1 and are not acted upon. At origin i the strategy may stop or continue (probability alpha_i). A continuation reaches time-2 signature s with strictly positive Q kernel mu_i(s); mu_i(r)=c_i in (0,1), sum_s s mu_i(s)=r. Only the time-2 center r may continue (probability gamma_i) through a second strictly positive mean-r kernel sigma_i, stopping at time 3; other signatures stop immediately. P transition kernels equal (s/r) times Q transition kernels. The full-history class may remember origin and use arbitrary real local behavioral randomizations and stopping declarations. The seedless LR class uses only (time,current s). The observer is exactly (e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P) and both expected stopping times.

For a point mass delta_r define signed measures A_i=mu_i-delta_r and K_i=(A_i+c_i(sigma_i-delta_r))/(1+c_i). Both have total mass 0 and first moment 0. For such measures X,Y define X >=cx Y iff sum_s (X-Y)(s) phi(s)>=0 for every convex phi on S. This signed comparison is an information-rate condition, not a probability distribution.

## Theorem R5-F4 (sufficient, all real strategies and every finite signature count)

If K_A=K_B=K as FULL signed measures and K>=cx A_A and K>=cx A_B, then the actual four-observation sets coincide: O_full=O_LR (not merely their convex hulls). The same holds for any finite number of r-colliding origins. This does not assert preservation of path-time laws or hidden provenance.

An exact finite rational certificate for K>=cx A_i is: with ordered S=(s_1<...<s_m), check sum_k (K-A_i)(s_k) max(0,s_k-s_j)>=0 for j=2,...,m-1; endpoint tests are 0 by zero mass and first moment. Every convex piecewise-linear function is affine plus nonnegative interior hinges, so these checks are necessary and sufficient for ALL convex functions on this finite support.

## Complete proof

For any full behavioral policy, define the conditional continue probabilities alpha_i at time 1 and gamma_i at the center r at time 2. Conditional probabilities already incorporate any earlier randomized dependencies. The exact extra Q expected waiting time beyond time 1 is
E=sum_i a_i alpha_i(1+c_i gamma_i), 0<=E<=Emax=sum_i a_i(1+c_i).
Write W_out for the unchanged Q terminal law of forced-stop outside origins, and M=sum_i a_i. The full Q terminal signature law is
W_full=W_out+M delta_r+sum_i a_i alpha_i[A_i+c_i gamma_i(sigma_i-delta_r)].

Construct a concrete no-seed LR policy: at time-1 r continue with common probability alpha=E/Emax; upon reaching time-2 r always continue. The construction is valid because 0<=alpha<=1. It has the same extra Q waiting time E and, by K_i=K, its terminal Q signature law is
W_LR=W_out+M delta_r+E K.
The identity (1+c_i)K=A_i+c_i(sigma_i-delta_r) gives, exactly as signed measures,
W_LR-W_full=sum_i a_i alpha_i(1-gamma_i)(K-A_i).     (1)
Every coefficient is nonnegative, hence (1) and the assumptions imply W_LR>=cx W_full. Both terminal laws have equal total Q mass and equal first moment, the latter being total P mass. All continued nodes have likelihood ratio r, so every extra unit of Q occupancy has r units of P occupancy: both policies have T_Q=1+E and T_P=1+rE.

For a terminal law W let Z(W) be the set of all pairs (x,y)=(P(declare P),Q(declare P)) achievable by terminal signature-dependent randomized declarations:
Z(W)={(sum_s s W(s)theta_s,sum_s W(s)theta_s):theta_s in [0,1]}.
It is a compact convex planar zonotope. In any signed direction (u,v), its exact support is
h_Z(W)(u,v)=sum_s W(s) max(0,u*s+v).
The hinge max(0,u*s+v) is convex in s for any real u,v. Convex order therefore yields h_Z(W_LR)>=h_Z(W_full) in ALL signed directions and hence the geometric inclusion Z(W_full) subseteq Z(W_LR) by compact convex separation. A full source/time-dependent declaration rule still produces a pair in Z(W_full): average its declaration probability at each terminal signature with Q mass weights; P mass is s times Q mass at that signature, so the same averaging preserves both laws. The inclusion supplies a terminal LR declaration coin theta_s with precisely the same x,y and hence the same e_P=1-x,e_Q=y. This coin depends only on the observed signature, not a persistent random seed. The time coordinates already match. Thus O_full subseteq O_LR; the reverse inclusion is immediate because LR policies are full-history policies. QED.

For the finite-certificate statement, any convex function restricted to ordered finite S is affine plus nonnegative linear combinations of the interior call hinges (s-s_j)_+. Integrals of affine functions vanish against K-A_i, proving the claimed exact finite equivalence. No discretization of the allowed real policies is involved.

## Four-signature rank-two exact witness

Use S=(1/2,1,3/2,5/2), r=3/2. Initial Q masses of A,B,O are 1/4,1/4,1/2, with ratios r,r,1/2; hence initial P masses are 3/8,3/8,1/4 and both laws normalize. O is forced to stop at time 1. In ordered S coordinates define

K=(3/20,1/5,-3/5,1/4).
mu_A=(7/50,11/75,1/2,16/75).
mu_B=(17/200,23/150,3/5,97/600).
sigma_A=(17/100,23/75,1/5,97/300).
sigma_B=(31/120,5/18,1/15,143/360).

Each Q kernel and its induced P kernel is strictly positive and normalized. Direct fractions give K_A=K_B=K. The determinant of the first two off-center entries of A_A and A_B is 9/1000 !=0; thus the two first-kernel directions are NOT collinear (rank two), despite the common final information rate. At the two interior convex-order knots t=1,3/2, the exact nonnegative call gaps are respectively A:(1/200,11/300), B:(13/400,53/600). The theorem therefore applies and gives equality of actual four-observation sets across all real behavioral strategies, even in this rank-two example.

One full strategy sets (alpha_A,gamma_A)=(1,0), (alpha_B,gamma_B)=(1/2,1/3), declaring P only at signatures 1 and 5/2. It has E=2/5,
W_full=(53/96,113/1800,181/600,601/7200),
O*=(e_P,e_Q,T_P,T_Q)=(3497/4800,117/800,8/5,7/5).
The LR strategy takes common alpha=16/31 and gamma=1, giving
W_LR=(14/25,2/25,13/50,1/10).
At signature 1 it declares P with probability 113/144, at 5/2 with probability 601/720, and otherwise never. This reproduces O* exactly, although W_full != W_LR. This equality is observer-scoped, NOT pathwise or native X6 information preservation.

## Evidence, reuse, future boundary

The attached VERIFY.py was run using standard-library fractions.Fraction and deterministic Random(20261029). EXACT_OUTPUT.txt records all four positive kernels, both-law means, rate identity, nonzero rank-two minor, all exact convex-order knot margins, a concrete observer vector, and 1,400 exact-rational nonexhaustive strategy tests. The latter verify instance arithmetic and a finite planar zonotope membership criterion; the all-real theorem is proved above, not by sampling. The zonotope facet check for (x,y) tests for every t in S:
sum_s W(s) min(0,s-t) <= x-t*y <= sum_s W(s) max(0,s-t).
These are the precise supporting facet inequalities of the 2D zonotope generated by (sW(s),W(s)); finite rational verification establishes each sampled membership.

BRC reuse: retained hidden origins, strictly positive branch mass under both laws, time-indexed occupancy and provenance until proving an exact quotient for the declared observer. No X6 embedding, six-axis physical dynamics, unbounded-horizon preservation, or P000/worldview change was proved. No independent review or mathematical admission. Control readback: research_authority_granted=false and em_control_tasks returned CONTROL_QUOTA, so current active Source owner/CLAIM is not confirmed; author-side GitHub publication is evidence storage only.

Prior work: project commit ebf1df364abc3bbb14b784fba47701b80ea9e627. Relevant established comparison-of-experiments context: Khan, Yu & Zhang, Economics Letters 247 (February 2025), article 112146, DOI https://doi.org/10.1016/j.econlet.2024.112146; Vera & Lynch, Advances in Applied Probability 39 (2007), 105-127, https://www.cambridge.org/core/journals/advances-in-applied-probability/article/general-convex-stochastic-orderings-and-related-martingaletype-structures/1D8FB11D0EDDBA7E048F4360ACC8AF51. No novelty or prior-art duplication conclusion is claimed beyond this scoped new derivation.

Next mathematical target: remove common K or its convex domination, establish all-signed Bellman support equality by a finite polyhedral certificate, then seek a same-E ROC facet separation from every LR stopping rule. Such a candidate is not yet constructed.
