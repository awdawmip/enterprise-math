# EC49FQR: all-prior exact BRC slice at price 47/16 and 22-node global enclosure

Date: 2026-11-16. Science pin: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Parent frontier: EC49FQQ, PR #2565, head 689c90d17967fb70ff206ac498d59aaad7fe8909. Scope: native BRC class 16943, 310 original configurations, 141 **full named-root** profiles, 144 terminal observations and 84 named-root observations (228 physical labels / 209 distinct partitions). Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Model and fixed feasible strategies

Arbitrary finite correct adaptive trees distinguish all 141 full profiles, without a depth cap. A terminal observation costs t>0 and a named-root observation costs r>0. Put x=r/t. The prior is p_lambda(i)=(1-lambda)/141 + lambda*m_i/310 with 0<=lambda<=1 and sum m_i=310.

For 1<=x<=3, the three previously constructed full native trees have normalized expected costs

A(lambda,x)=(1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310;

B(lambda,x)=(1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310;

C(lambda,x)=(1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310.

Write F=min(A,B,C), beta=620/3299, K(x)=7557-169*x and gamma(x)=310*(3-x)/K(x). For x>=3 the inherited exact high-price policy has H=min(H1,H2), where H1=(1-lambda)*(4*x+296)/141+lambda*(4*x+707)/310, H2=(1-lambda)*(4*x+298)/141+lambda*(4*x+688)/310. Let P=F on [1,3] and P=H on [3,infinity). The true optimum normalized by t is v(lambda,x).

## Theorem 1: a new full continuum of priors

At **x=47/16**, gamma=**310/112969**, and for **every real 0<=lambda<=1**, the unrestricted exact optimum satisfies **v(lambda,47/16)=F(lambda,47/16)**. Exhaustive physically indexed optimal first observations are:

| Prior parameter | All optimal first observations |
|---|---|
| 0 <= lambda < 310/112969 | 32, 34 |
| lambda = 310/112969 | 32, 34, 140, 142 |
| 310/112969 < lambda < 620/3299 | 140, 142 |
| lambda = 620/3299 | 16, 23, 140, 142 |
| 620/3299 < lambda <= 1 | 16, 23 |

**Proof.** The fixed frozen inputs, verified by SHA256, reconstruct all 141 full named-root profiles, the 228 physical observations and 209 response partitions. Exact unrestricted subset Bellman recursion was run at the four anchors lambda=0,310/112969,620/3299,1 with price integers r=47,t=16. Its corresponding optimal integer mass-costs are 1525820, 172434900960, 5093744850, 1578495; mass normalization is 310*141*lambda_denominator. At all four anchors a second independently coded Bellman algorithm reproduced the same objective and enumerated all 228 physical first labels. Every tied first label has a fully replayed correct decision tree. The full tree count vectors (141-state-uniform root, terminal; 310-configuration root, terminal) are A=(6,290;6,751), B=(5,293;5,704), C=(5,295;5,685). Each fixed witness tree has cost affine in lambda. At consecutive certified anchors an affine competitor-minus-witness cost is nonnegative at both endpoints, hence throughout their interval. A competitor with another optimal first label at a strict interior point would have zero affine difference at both endpoints; the intersection of the two exhaustive endpoint first-label sets eliminates all additional labels. The listed labels are attained by the replayed witnesses. This proves the statement for every real prior and every finite correct adaptive tree. QED.

## Theorem 2: 22 certified prices and exact area

Insert the new rational node 47/16 between 23/8 and 3 in the certified EC49FQQ 21-node price grid, giving G22. For every adjacent pair a<b, the multi-affine four-corner witness certificate proves v=A on [a,b]x[0,gamma(b)], v=B on [a,b]x[gamma(a),beta], and v=C on [a,b]x[beta,1]. Strict interior optimal first labels are respectively {32,34}, {140,142}, {16,23}. Uncertified points are restricted to 21 open bands a<x<b, gamma(b)<lambda<gamma(a).

The *exact rational* band area, measured in [1,3]x[0,1], is

**S22 = 63266932358723791445 / 7398811896183040660488 = 0.00855095834932125...**.

Consequently the already certified proportion of this domain is

**1-S22/2 = 14734356860007357529531 / 14797623792366081320976 = 99.57245208253394...%.**

Proof: all rectangle corners are exact native-Bellman anchors, and any fixed competing tree's cost difference from the witness is separately affine in lambda and x. Four nonnegative corner values imply all interior differences are nonnegative. The area is the exact rational sum of (b-a)*(gamma(a)-gamma(b)). The high-price ray x>=3 remains exact by the inherited theorem. QED.

## Theorem 3: a sharper globally valid excess-cost certificate

For 1<=x<=3, v(lambda,x) is a pointwise infimum of fixed-tree affine x-costs, hence concave in x. Between consecutive certified price nodes, the secant supplies a lower bound, and P supplies an upper bound. The exact maximal secant envelope on [a,b] is

M_ab = 50*(b-a) / (sqrt(K(a))+sqrt(K(b)))^2.

On G22 its maximum is attained at **[19/8,5/2]**, giving for all real lambda in [0,1] and x>=1:

**0 <= P(lambda,x)-v(lambda,x) <= M22 = (25/4)/(sqrt(57245/8)+sqrt(14269/2))^2 = 0.000218682601258424...**, in units of terminal cost t.

Proof of maximizing interval without floating-point ordering: every G22 interval of width 1/8 ends at or before 5/2, and M_ab strictly increases with a at fixed width. Every other interval has width <=1/12. Their M_ab are <=50/(12*4*7050), which is strictly less than 50/(8*4*K(19/8)), itself <= M_[19/8,5/2]. This identifies the exact maximum. For x>=3 the inherited H=v, so the excess is zero. The old 21-node guarantee was 0.000221299772391955...t. M22 is a sharp bound of the **current chord-based certificate**, not a claim that an unknown competing native tree attains this cost difference. QED.

## Logarithmic splitting design

The old worst interval [23/8,3] has unique minimax real split x*=(7557-sqrt((56569/8)*7050))/169 = 2.9375467495769... by the inherited logarithmic-grid theorem. The exact rational 47/16 = 2.9375 is within 0.000047 of x*. It is the only new interior fraction with denominator dividing 16 in that interval. Four newly completed native Bellman anchor computations certify the whole new prior section.

## Evidence and next work

Full local self-contained archive: EC49FQR_NATIVE_SLICE_47_16_20261116, preserving original two frozen source files, 81 inherited plus 4 new complete exact Bellman certificates, two Bellman implementations, all tied-first witness trees, provenance hashes, executable independent verifier, independent-run log and a complete file SHA256 manifest. See the companion indexed verification record in this PR. The full bundle was independently re-executed in this run; mathematical peer review is pending. Neither this independent portable research note nor the draft PR creates a Source CLA﻿IM, Result, Review or Activity checkpoint.

Next: independently certify x=39/16 in the currently largest remaining chord interval [19/8,5/2] or establish a parameterized Bellman lower bound over the 21 open bands. Maintain the same frozen science pin, full named-root target, physical observation indices and provenance.
