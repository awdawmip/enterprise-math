# EC49FQR second exact BRC slice at x=39/16 and new 23-node theorem

Date: 2026-11-16. Native science pin: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Parent: EC49FQQ PR #2565 and EC49FQR first x=47/16 theorem in this Draft PR. This paper uses the native class 16943 with 310 original configurations, 141 **full named-root** response profiles, and 228 physical observations (144 terminal / 84 named-root). The decision tree can have any finite depth and must distinguish the full named-root profile. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Theorem 4 — a second complete continuum of priors

At the rational root-to-terminal price ratio x=r/t=**39/16**, the transition parameter is **gamma(x)=930/38107**. For every real 0<=lambda<=1, the unrestricted complete native-BRC Bellman minimum v(lambda,39/16) equals the known feasible policy F=min(A,B,C), where

A=(1-lambda)*(6*x+290)/141+lambda*(6*x+751)/310,

B=(1-lambda)*(5*x+293)/141+lambda*(5*x+704)/310,

C=(1-lambda)*(5*x+295)/141+lambda*(5*x+685)/310,

and beta=620/3299. All optimal physical first labels are exactly:

| lambda | Optimal first physical labels |
|---|---|
| 0 <= lambda < 930/38107 | 32,34 |
| lambda = 930/38107 | 32,34,140,142 |
| 930/38107 < lambda < 620/3299 | 140,142 |
| lambda = 620/3299 | 16,23,140,142 |
| 620/3299 < lambda <= 1 | 16,23 |

**Exact finite proof.** The frozen original source and original native-cost profiles were checked by SHA256. All 228 legal physical first observations, all distinct partition children and all smaller subsets were handled by a complete exact positive-mass Bellman recursion (unlimited finite tree depth). For integer costs root=39 and terminal=16, at prior anchors lambda=(0,930/38107,620/3299,1), exact integer mass-cost optima are respectively **1,510,940; 57,778,558,880; 5,057,028,450; 1,572,855**. A separately implemented weighted-mass subset Bellman solver independently reproduced all four optima and the exhaustive physical first-label sets. Complete trees were replayed for each tied first label; leaf correctness and the fixed tree count vectors were checked. The A, B, C counts (141-profile root, terminal; 310-config root, terminal) are respectively (6,290;6,751), (5,293;5,704), (5,295;5,685). Fixed feasible tree costs are affine in lambda; nonnegative affine differences at two adjacent certified priors stay nonnegative throughout the interval. A newly tied interior first action would force the difference to vanish at both endpoints, making its label an element of the intersection of the corresponding endpoint optimal-action sets. These intersections give exactly the displayed list. QED.

## Theorem 5 — 23-node exact two-parameter enclosure

Add the price node 39/16 between 19/8 and 5/2 to the 22-node certified set obtained by the first theorem in this PR. For each adjacent certified a<b, multi-affine four-corner contact proves full optimality of the fixed A policy on [a,b]x[0,gamma(b)], B on [a,b]x[gamma(a),beta], and C on [a,b]x[beta,1], with corresponding exhaustive first-label sets on strict interiors. The remaining possible exceptions occupy only 22 open bands a<x<b, gamma(b)<lambda<gamma(a), whose **exact rational area** in the domain [1,3]x[0,1] is

**S23 = 696012280557809479893905 / 84708997399399632521927112**.

The exactly certified fraction of the rectangular target domain is

**1-S23/2 = 168721982518241455563960319 / 169417994798799265043854224 = 99.58917452577313...%.**

Define P=F for 1<=x<=3 and P equal to the inherited exact optimal high-price policy for x>=3. For all lambda in [0,1] and x>=1, the global expected-cost regret in units of terminal price obeys

**0 <= P(lambda,x)-v(lambda,x) <= M23 = (25/4)/(sqrt(28707/4)+sqrt(57245/8))^2 = 0.0002180379523461403267469... .**

**Proof.** Concavity of v(lambda,x) in x makes the secant joining exact certified price nodes a lower bound. The maximum feasible-policy excess above this secant on [a,b] equals 50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2, K(x)=7557-169*x. All G23 intervals of width 1/8 end no later than 19/8; for equal width the envelope maximum strictly increases with the interval's left endpoint. All remaining intervals have width <=1/12 and their maxima are <=50/(12*4*7050), strictly smaller than 50/(8*4*K(9/4)), which in turn is a lower bound on the maximum for [9/4,19/8]. Hence the global maximum occurs at that interval, where K(9/4)=28707/4, K(19/8)=57245/8. The band area is a finite exact rational sum of (b-a)*(gamma(a)-gamma(b)). The x>=3 high-price tail is exactly optimal by the inherited theorem. QED.

## Evidence, review and next question

The self-contained EC49FQR_TWO_SLICES_23GRID_20261116 archive holds 89 complete Bellman certificates (81 inherited and 8 new), both frozen source files, the native constructor, a separately implemented independent verifier, all tied-first correct trees, the exact proof manuscripts and a file-by-file SHA256 manifest. Verification at both new price ratios was executed separately; the exact-rational geometry and inherited hashes were checked. See the SHA256 evidence indices in this PR. Review/admission remains pending; independent portable GitHub publication does not imply a formal CLAIM, Result or Source Activity checkpoint.

The next useful exact price is x=37/16 in the currently largest remaining uncertified chord interval [9/4,19/8]. A separate route is a parametric lower bound for any of the 22 curve bands, or a strict native full-profile tree improvement over F.
