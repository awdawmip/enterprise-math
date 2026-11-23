# X6 R160 — Unified globally minimal ten-direction strict-near support

2026-11-24. AUTHOR EXACT FINITE CERTIFICATE / NOT_REVIEWED. Frozen R121/R122 and static conditional three-axis X6 observer as in R159 (corrected text at 2bc75c0afe4bd3004625d24b9b10927573649a74). No native dynamics or P000 change.

## Theorem
For every real B,D>0 at w=(136,B,176,D), Port 10, let F and eta be exactly the six-gap score and minimum defined in R159. Let W6={(6,-1,0),(1,0,0),(5,-1,0),(9,-5,1),(4,-1,0),(6,-4,1)} and
T10=W6 union {(1,3,-1),(4,-4,1),(5,-4,1),(7,-1,0)}.
Then the complete strict 3/2 near set is
N(B,D)={v in T10 : 2F_v(B,D)<3 min_{w in W6}F_w(B,D)}.
T10 is the exact union over all positive B,D, hence the unique smallest fixed support for computing the full near set. This is NOT a simultaneous cardinality of ten. It consolidates the R146–R158 regional near atlases into a single exact formula without seam selection, valid at all finite equality boundaries. Every W6 score is reused when filtering T10: only ten direction scores are needed total, and all six labeled gaps per score remain. The 1935-to-ten count is not a measured runtime speedup.

## Proof
First R122 coordinatewise 3/2 domination excludes every direction v with some Pareto row u such that 2g_j(v)>=3g_j(u) for all j. The integer enumeration (using the R159 P12 list) finds exactly 20 survivors, 1915 excluded. For any survivor, R159 gives eta=min_W6 F_w; strict near is equivalent to 3F_w>2F_v for EVERY w in W6. Use R159's projective parameter triangle and active-channel clipping for v (positive numerator n in channel j); the only change is the strict comparisons 3g_k(w)s'_j-2n s'_k>0. The existence of a near point is an open condition. The closed active region and the finite union/intersection of strict comparisons have a positive-area closure cell iff the condition is realizable in the positive parameter interior, exactly as proved in R159; discard identically-zero strict comparisons and zero-area cells. The finite exact checker returns ten surviving rows and excludes the other ten. For each surviving row the mean of the vertices of one surviving positive-area convex polygon is an interior rational point; inverse projective transformation gives positive B,D. Independently compute all 1935 scores at each such witness and assert the strict inequality. This proves both exclusion and individual attainment, and the formula follows. This proof directly covers the whole positive parameter domain, without depending on seam claims in earlier atlases; it does not independently review every old explicit boundary expression.

## Actual run and source
Executed Python 3, integer/Fraction; imports the unchanged R159 companion. Source x6_r160_global_near_support_verify.py at bfc76ae24fc838aa8878bd7ca806733574f9d0d7; local executed Git blob f86e55a310e5f0c80696a4172d5e50eaf510eb6d, SHA256 f33910e25964d6513b2efd55c7776e7a74f153caf6f27cd6fbbce06e2155c418; remote full text and blob matched. Actual stdout after R159 replay:
```
STRICT NEAR SUPPORT 10
(1, 0, 0) 45412576744/464196617 1224480635542/1392589851
(1, 3, -1) 32087584/24437621 402455295/1879817
(4, -4, 1) 353879/6358 224344/3179
(4, -1, 0) 39030333/299896 1108916987/299896
(5, -4, 1) 21943364488/223127789 210199363354/223127789
(5, -1, 0) 5484643988/182774979 250168728941/365549958
(6, -4, 1) 3401/9 55369/9
(6, -1, 0) 81515/143404 656711/286808
(7, -1, 0) 97427808/74699407 16098061865/74699407
(9, -5, 1) 5925672524/38110809 9953449514/12703603
NEVER STRICT NEAR [(1, -3, 1), (2, -4, 1), (3, -7, 2), (3, -4, 1), (3, -1, 0), (3, 3, -1), (7, -8, 2), (7, -4, 1), (7, 2, -1), (9, -2, 0)]
GLOBAL TEN-ROW NEAR SUPPORT PASS
```
Each surviving row is individually realized, not necessarily at the same weight. The two scripts form the exact replay; no floating arithmetic.

## Control and continuation
Original native read r2-20261124-0710-x6-task-read SUCCEEDED/error=null; state owner=taskbook/unassigned, HANDOFF_READY, NEEDS_DISPATCH, claim_id=null, execution_authorized=false. Native task next_action is frozen C12 native transition and R063 benchmark, separate from this static research. Original own registration r2-20261124-0310-r155-own-session-v1 SUCCEEDED with EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317. No formal CLAIM/Result/Review submitted. Research activity association is separate. Next: vary the ratio C/A, derive maximal ratio interval of W6 and T10 sufficiency by lifting projective affine certificate to normalized four-weight simplex; review boundary expressions as needed. The current fixed-ratio minimum and support are closed at author-proof level; do not repeat.
