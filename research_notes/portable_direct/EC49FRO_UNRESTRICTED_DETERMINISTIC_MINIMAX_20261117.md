# EC49FRO — Exact unrestricted deterministic minimax regret, original BRC class 16943

Date: 2026-11-17. Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status: AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE_REUSED_AND_RECHECKED / NOT_REVIEWED. Independent portable research; no formal Task/CLAIM/Result/Review assertion.

Predecessors: [EC49FRI PR #2621](https://github.com/awdawmip/enterprise-math/pull/2621) (six original unrestricted Bellman anchors); [EC49FRJ PR #2624](https://github.com/awdawmip/enterprise-math/pull/2624) (hard terminal-observer fibers); [EC49FRL PR #2630](https://github.com/awdawmip/enterprise-math/pull/2630) (complete feasible trees); [EC49FRM–FRN PR #2633](https://github.com/awdawmip/enterprise-math/pull/2633) (randomized minimax). This theorem depends on six precise finite Bellman anchors and a terminal-fiber combinatorial fact, not on the entire inherited continuous Bellman-envelope theorem.

## Problem and exact result

The unchanged frozen model contains 310 original configurations, 141 fully named physical-response profiles with positive integer multiplicities m_i summing to 310, and all 228 original physical observations (144 terminal and 84 root). A legal identifying decision tree must distinguish all 141 profiles, preserving original observation identities and response semantics. Terminal observation cost t>0; root cost xt with real x>=1. The prior is p_i(lambda)=(1-lambda)/141+lambda*m_i/310, real lambda in [0,1]. A prior-blind deterministic controller fixes one complete tree Q before learning lambda.

Define normalized regret G_Q(x,lambda)=C_Q(x,lambda)/t - V(x,lambda)/t, with V the unrestricted original Bellman optimum.

**Theorem.** The infimum over *all* legal original deterministic identifying trees, without any depth restriction or five-tree candidate restriction, is attained and equals

\[
\boxed{\inf_Q\sup_{\lambda\in[0,1]}G_Q(x,\lambda)=
\begin{cases}(5-x)/141,&1\le x\le3,\\2/141,&x\ge3.\end{cases}}
\]

Existing complete native tree C, coefficient vector (U_R,U_T,M_R,M_T)=(5,295,5,685), attains the first branch. Existing complete native tree E, vector (4,298,4,688), attains the second. Both have maximum realized depth 3.

## Six fixed Bellman anchors and one original fiber certificate

For every complete Q let r_i,d_i be its numbers of root and terminal observations on profile i. Define integer sums U_R=sum r_i, U_T=sum d_i, M_R=sum m_i r_i, M_T=sum m_i d_i. Set U_s=U_T+s*U_R and M_s=M_T+s*M_R. Then

\[
C_Q(x,\lambda)/t=(1-\lambda)(U_T+xU_R)/141+\lambda(M_T+xM_R)/310.
\]

Let beta=620/3299, so (1-beta)/141=19/3299 and beta/310=2/3299. Previously computed unrestricted native Bellman JSON certificates (EC49FRI) give the exact table:

| Price x | lambda=0 | lambda=beta | lambda=1 |
|---|---|---|---|
| 1 | 296/141 | 7080/3299 | 690/310 |
| 3 | 308/141 | 7290/3299 | 700/310 |

Tree C attains V(1,beta) with (U_1,M_1)=(300,690). Tree E attains V(3,beta) with (U_3,M_3)=(310,700). Thus EVERY original feasible Q satisfies these **integer supporting inequalities**:

\[
19(U_1-300)+2(M_1-690)\ge0 \tag{S1}
\]
\[
19(U_3-310)+2(M_3-700)\ge0. \tag{S3}
\]

Independently reconstructed terminal response signatures of all 141 named profiles under all 144 terminal actions have exactly two nonsingleton indistinguishable pairs {8,139} and {46,140}. Each of those four profiles has original multiplicity 1. On a correct identification tree each must receive at least one root observation, since the full terminal action library can never distinguish its pair while their paths remain identical. Hence U_R>=4 and M_R>=U_R. Furthermore **U_R=4 forces M_R=4**: those four mandatory weight-one paths consume exactly the four root observations. This rigidity is essential.

## Proof

**Exact prior endpoints for every real price.** At lambda=0 the feasible A tree (U_R,U_T)=(6,290) attains the unrestricted Bellman optimum at both x=1 and x=3. For lambda=1, C (M_R,M_T)=(5,685) does likewise. Every competing complete tree cost is affine in x; at the two endpoints its gap from the indicated fixed candidate is nonnegative. Therefore, throughout 1<=x<=3,

\[
V(x,0)/t=(290+6x)/141,\quad V(x,1)/t=(685+5x)/310.
\]

At x=3 D and E, both with root masses four, attain these respective prior endpoints. Every Q has U_R,M_R>=4, so it grows no more slowly than D/E in the price direction. Hence for every real x>=3,

\[
V(x,0)/t=(296+4x)/141,\quad V(x,1)/t=(688+4x)/310.
\]

For a fixed Q its expected cost is affine in lambda, while Bellman V is concave in lambda as the pointwise infimum of affine tree costs. Hence G_Q is convex and its maximum over the entire real prior interval is attained at lambda=0 or lambda=1.

**Range 1<=x<=3.** C has endpoint regrets rho=(5-x)/141 and 0. Consider an arbitrary Q, put u=U_1(Q), m=M_1(Q), k=U_R(Q).

If k>=5 and u>=300, its uniform cost difference from C is (u-300)+(k-5)(x-1)>=0, so uniform regret is at least rho. If k>=5 and u<=299, (S1) and integrality give m>=700. The positive multiplicities ensure M_R>=k>=5; the multiplicity cost difference from C is at least 10, so its second-prior regret is >=10/310>4/141>=rho.

If k=4, fiber rigidity gives M_R=4. The following cases exhaust every integer u:

* u<=299: S1 gives m>=700. The multiplicity cost difference from C is at least 11-x; hence second-prior regret >=(11-x)/310>rho. The strict inequality follows from 141(11-x)-310(5-x)=1+169x>0.
* u=300: U_3=u+8=308. From S3, M_3>=719, so m>=711. Multiplicity cost difference from C is >=22-x; hence (22-x)/310>rho.
* u=301: U_3=309. From S3, M_3>=710, so m>=702. Multiplicity cost difference from C is >=13-x>=10, and 10/310>rho.
* u>=302: uniform cost difference from C equals (u-300)-(x-1)>=3-x>=0, so uniform regret >=rho.

Therefore every deterministic original Q has worst regret at least rho. The feasible C tree attains it.

**Range x>=3.** Set u_3=U_3(Q), m_3=M_3(Q), both integers. If u_3>=310, then U_T+xU_R>=310+4(x-3)=(296+4x)+2. Hence uniform regret >=2/141. Otherwise u_3<=309, and S3 forces m_3>=710 by integrality. As M_R>=4, M_T+xM_R>=710+4(x-3)=(688+4x)+10. Hence multiplicity regret >=10/310>2/141. The feasible E tree has endpoint regrets 2/141 and zero. Thus E is unrestricted deterministic minimax-optimal. QED.

## Exact benefit of prior-blind randomization

EC49FRM established the unrestricted optimal *randomized-before-observation* regret R_rand=19(5-x)/3299 on [1,3], and 38/3299 on [3,infinity). Combining with the present unrestricted deterministic result gives, for every real x>=1,

\[
\boxed{R_{\rm rand}(x)/R_{\rm det}(x)=2679/3299.}
\]

Thus pre-observation randomization lowers the optimal deterministic worst expected regret by exactly 620/3299, approximately 18.7936%, in this original typed finite BRC model. The earlier five-candidate deterministic bound is now an unrestricted original-tree equality.

## Reproducibility and provenance

The companion exact-Fraction Python checker verifies the new interval/case arithmetic. With original evidence archives extracted, it also (1) reconstructs all 141 named profiles and 228 physical responses from pinned frozen data, (2) checks precisely the four mandatory weight-one terminal-indistinguishable profiles, (3) matches SHA256 of the six original unrestricted Bellman certificates to EC49FRI's exact index, (4) checks their exact rational optima and (5) replays existing A–E coefficient vectors from full original trees. Source master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; BRC profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

No fresh exhaustive Bellman computation was performed in this continuation; its six load-bearing finite anchor certificates were inherited with precise original bytes and hashes and rechecked. The analytic case proof covers every feasible deterministic identifying tree, all real x>=1 and real lambda in [0,1] under those exact finite inputs. Source admission remains NOT_REVIEWED and no P000/X6 or future heartbeat dynamics equivalence is asserted.

**Next scientific question:** unrestricted deterministic robust regret on proper prior intervals [a,b] (rather than [0,1]); identify cost-vector Pareto facets and weight-integrality gaps. A separate direction is the exact number of randomized trees needed for multidimensional prior polytopes while retaining original observers and provenance.
