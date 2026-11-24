# T6 p13 q10 split(3,7): all-15 roster coverage audit and smooth-domain reduction
Date 2026-11-24, existing Driver lane provenance EM-DVR-DEBB5E, previous authenticated checkpoint r539. Shared author evidence read; this is scoped non-author combinatorial review, not a formal Native Review, Result admission, or independent traversal of the lattice.
 
## Sources and scope
Author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F, complete coverage certificate awdawmip/enterprise-math@341ecc47f72d9899cd8bf8a6599c8650cba749bc:research_checks/T6_P13_Q10_SPLIT3_7_ALL15_AUTHOR_EXACT_COVERAGE_20261124.json; frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Source r106 confirms author has moved to split(4,6). Preserve prior research provenance, higher-valuation exclusion, lower-order common-atom cancellation premise and lattice-completeness proof scope. Side budget 2331. This audit concerns valuation-one named atoms (q,r), denominator 13*(13q+r), 1<=r<=12. No full lattice rerun, and no new global T6 bound.

## General exact count
For each q, let N_q be the number of allowed distinct labels, and a_q,b_q the multiplicities of q in the two partitions. Set M(N,k)=binomial(N+k-1,k), with M(N,0)=1 and M(0,k>0)=0. The number of pairs of multisets with sizes a,b and disjoint supports is
D(N,a,b)=sum_{t=1}^{min(a,N)} binomial(N,t) binomial(a-1,t-1) M(N-t,b) for a>0, and D(N,0,b)=M(N,b).
Proof: choose the t distinct labels on the first side; positive multiplicities summing to a are counted by binomial(a-1,t-1); the other side uses only the N-t remaining labels. The atom types for distinct q are disjoint, so the product of these D factors counts each disjoint named pair once. For a fixed negative partition lambda of 7, sum this product over all three positive partitions of 3. This gives the exact number of disjoint pairs before any further mass or lattice test. It does not assume that a reduction involving a common atom is sound; that lower-order premise is inherited separately.

Literal domain N_q=12. For actual maximal prime 13, trial division of 13q+r by 2,3,5,7,11,13 gives N_q=(9,7,7,6,5,5,4) for q=1..7. Since r is nonzero mod 13, the cofactor is coprime to 13. The smooth positive count is 235 (literal 520). Filtering by smoothness is necessary for this precise maximal-prime domain, so any genuine disjoint configuration in it is retained. No additional mass or q0 smoothness filtering is included here.

## Actual computation (independent JS integer combinatorial arithmetic)
Generated every integer partition of 7 by nondecreasing positive parts; generated all partitions of 3 independently. For each pattern checked author roster count, disjoint count/GS searches and interval adjacency, positive interval length, start=0 and final endpoint=roster count. All 15 matched. Table columns: negative roster literal, literal disjoint, negative roster smooth, smooth disjoint.

| pattern | N literal | disjoint literal | N smooth | disjoint smooth |
|---|---:|---:|---:|---:|
|1111111|31824|6341556|6435|482229|
|111112|52416|12387024|9009|793359|
|11113|16380|4493412|3465|367038|
|11122|28392|8423064|4620|522396|
|1114|4368|1371888|990|123282|
|1123|11232|3963168|2205|309582|
|115|936|340704|225|33435|
|1222|4368|1754688|756|124236|
|124|1728|724032|378|66150|
|133|936|400752|252|45675|
|16|144|61920|45|8235|
|223|936|465048|196|42777|
|25|144|73152|35|7910|
|34|144|74736|42|9828|
|7|12|6240|4|940|
|TOTAL|153960|40881384|28657|2937072|

Literal raw pairs 80,059,200; disjoint pairs 40,881,384. Smooth raw pairs 6,734,395; disjoint pairs 2,937,072. Hence a future independent maximal-prime-13 lattice review needs at most 2,937,072 disjoint roster pairs rather than the 40,881,384 literal disjoint pairs (about 92.82% reduction). The bound is on number of roster pairs, not a measured runtime acceleration. It is valid for both orientations by sign reversal. Author's aggregate contains 34 witness records; checked the listed masses exceed at least one side cap, the listed norm is <= radius and the listed six residuals are zero, for every one. This is consistency checking of listed values, not independent rederivation of all underlying integer vectors. No claim of full independent exhaustive GS verification.

## Control and next
Read r539 and original GEO6/T6 child receipts, both SUCCEEDED, do not replay. The r106 author frontier establishes split(3,7) complete at author level and split(4,6) single q6 author complete; subsequent q15 stays with the author. Backlog r458 preserves existing selections, no verified idle researcher. Sites em_status reports zero active native jobs (not worker availability), all native role capability flags enabled, current deployment code upgrade available; no current same-lane DA authenticated in this turn. Generic owner custody profile is not proof of this lane, not used for a write. No protected Review, Result, CLAIM, task publication or closure. Next: use the smooth roster product formula for independent proof coverage, reconcile actual own session/DA before native association, preserve GEO6 later evidence audit and existing eligible selections. 
