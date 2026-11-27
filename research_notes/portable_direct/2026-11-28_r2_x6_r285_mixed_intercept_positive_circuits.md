# X6 R285 — mixed intercept positive-circuit elimination and sixth-pencil continuation

2026-11-28. Independent informed TASK_RESEARCH; author proof and exact calculation, NOT_REVIEWED. Native read r2-20261128-0308-x6-read SUCCEEDED at 2026-11-27T19:08:22.184536Z, Source 3fc2f6dd01c6ee20e17a8adccd29f4d69f66ceb6, NO_CANONICAL_PUBLICATION_DIRECTORY; no owner projection, own researcher binding unconfirmed. No CLAIM or shared control change; Activity association pending. Global main entry snapshot dd3574b690b4b1099fe412bc50e983681f09a3e2. P000 V5, global V4 projection (canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, joint and residual fidelity retained. Auxiliary coefficient algebra of the frozen BRC observer, not a new native arithmetic calculation.

## Scope and sources

R283@d0fb62e0871f9ca48c692291d0caeca77d3e0055:research_notes/portable_direct/2026-11-28_r2_x6_r283_sixth_prefix_4700_and_mixed_slack.md; R284@b1dcb5bc4869113730d936e03be15ebc926a2ba1f:research_notes/portable_direct/2026-11-28_r2_x6_r284_mixed_lift_exact_reference_check.md. Preserve R283's exact R247/R275/R276/R277/R280/R281/R282 pins, Port 10, 1935 directions, six-pair BRC, 47 support labels, 51 endpoint rays, 98 directed germs, 2225 linear suffix partitions. Capacity classifications inherit R247 necessary-wall and complete pure-linear suffix premises. R283 strict frontier 410800/667787, 2800 necessary-condition survivors, next [5200,0].

## Theorem: exact mixed intercept projection by positive circuits

Let x=(a,d,b) be the three intercept coefficients, y=(e,f) the shared slope coefficients of Q(t,B,D)=a*t^2+d*t*B+b*B^2+e*t*D+f*B*D+D^2. A finite mixed row system has rows u_i dot x + v_i dot y + c_i >=_i 0 with rational coefficients, where >=_i denotes either > or >=. Encode equality as two weak rows. Set s_i=1 for strict, 0 for weak. Define the cone C={lambda>=0: sum_i lambda_i u_i=0}. For every inclusion-minimal nonempty support of a nonzero element of C, choose its primitive positive integer dependency lambda (on that support). A zero u_i gives a singleton. Then the projection onto y is EXACTLY the intersection of the following rows, one per minimal positive support:

sum_i lambda_i (v_i dot y + c_i) >= 0 if sum_i lambda_i s_i=0;
sum_i lambda_i (v_i dot y + c_i) > 0 otherwise.

Each support has size at most rank(u)+1 <=4. This is an exact generalization of the R275/R261 pencil-specific intercept test to include cross-pencil germ rows.

Proof: A support-minimal positive dependency has a one-dimensional restricted kernel: otherwise perturb along a nonproportional kernel vector until a coefficient vanishes, leaving a nonzero nonnegative dependency on a smaller support. Thus on support S the rank is |S|-1, so |S|<=4; its unique ray is rational and can be normalized to primitive positive integers. Any nonzero element of C is a nonnegative combination of these rays: choose a support-minimal positive dependency inside its support, subtract the maximal nonnegative multiple allowed by the coordinates, and iterate (support strictly shrinks). Necessity of all displayed rows is summing the original rows. For sufficiency fix a real y satisfying all circuit rows. For each circuit with positive strict weight w=sum lambda_i s_i, the ratio of its positive slack to w is positive. Finitely many circuits exist; choose a common real epsilon>0 at most their minimum (if none, choose 1). All circuits now satisfy sum lambda_i(v_i dot y+c_i-s_i epsilon)>=0. By the cone decomposition the same holds for all lambda in C. The ordinary real linear-inequality Farkas alternative implies existence of x with u_i dot x+v_i dot y+c_i>=s_i epsilon for every i. It satisfies the mixed original rows. This covers empty cone, rank deficiency, equality-only and empty systems. No numerical epsilon is needed in the algorithm: use the mixed row labels directly with R284. Projected region is identical, not merely its nonemptiness. Retain original rows or a witness recovery map whenever future constraints can involve x; projected y alone is not an equivalent state for those operations.

## Exact row generation for endpoint and germ constraints

For p=(t,B,D), endpoint evaluation uses u=(t^2,tB,B^2), v=(tD,BD), c=D^2. For p=(t,B,D), q=(T,U,V), the polarized derivative h=2 p^T A q uses u=(2tT,tU+BT,2BU), v=(tV+DT,BV+DU), c=2DV. For a known zero endpoint p, R275 gives lexsgn(h,Q(q)). Desired germ sign sigma=+/-1 uses sigma times the h row, weak if sign Q(q)=sigma, strict otherwise. Desired germ zero requires h=0 and Q(q)=0; reject immediately if the chosen endpoint word assigns q a nonzero sign. Endpoint zero uses two weak rows. All row directions remain exact and signed. These rows feed the same positive circuit theorem including cross-pencil germs (unlike the original pencil quartet dictionary).

For p=r(T,U,y0), q=s(T,U,y1) with r,s>0 on the same finite pencil and Q(p)=0, the derivative simplifies to h=rs*(y1-y0)*(2y0+eT+fU). This follows by replacing K=aT^2+dTU+bU^2 with -y0^2-(eT+fU)y0 in the polarization. Therefore same-pencil zero germs require no intercept coefficient at all once the endpoint equality is imposed. Cross-pencil germs retain their original intercept normals. This removes algebraic work, not germ identities.

Algorithm: enumerate subsets of up to four intercept rows, retain only one-dimensional kernel with all coordinates of one sign and none zero (including singleton zero row), normalize, combine v,c and strict flags exactly. Parallel/opposite rows and dependent triples are not skipped. One-dimensional kernel positive implies inclusion-minimal support. R284 solves resulting two-slope system. Worst-case subset enumeration O(n^4) fixed-dimension rank tests, plus output combinations and bit arithmetic; no claim this is faster than generic FM for all cases. Future useful optimization: cache the circuit directions by fixed endpoint/germ row normals and reuse them across mixed words with sign switches. Full mixed X6 classifier integration and empirical comparison remain open. The theorem is author proof; no independent review.

## Executed strict batch

Actual output (R282 algorithm, 150 five-line candidates, no cutoff):
{"hist":{"direct":6731,"alg":4657,"recursive":308,"surv":154,"visits":11850,"checkedAgainstOld":100},"checks":1509320,"next":[5350,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":150,"rawRows":8403,"hullRows":547,"pairRows":563,"hullIntersections":13527,"pairDominanceTests":50258,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":16410,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":39248,"mergeCompared":0,"mergeSort":2886387,"mergeComparisons":368446,"mergeIntersections":1146018},"partial":false}

New bank (index:hex 79-bit pattern mask):
```text
5209:60000
5211:c0180
5214:c000000
5216:40000
5223:380
5224:380
5226:380
5233:380
5234:403e0
5235:403e0
5245:200
5247:2038000000
5248:c0180
5249:201e03c0
5250:200
5251:180300
5252:180300
5260:1070783e000000
5261:6038000000
5263:20080000
5264:100000
5268:60703c000000
5269:4030000000
5270:20080000
5274:406038000000
5275:80000
5279:100
5287:100
5290:600
5292:201c0380
5293:1c0380
5294:6030000000
5295:2030000000
5296:300000
5297:300000
5298:4030000000
5299:30000000
5300:300000
5301:300000
5302:e0080000
5303:c0300000
5304:20400000000000
5330:60080
5334:80100
```

Reproduction: R283's exact reconstruction recipe, start=5200,size=150,ceiling=12000000, R247 data literal, R276 first text bank, R277 tail with R280/R281/R282 first JS blocks inserted before grow, increment pairCalls in grow, raw=grow(empty,R), st=prune(raw), good=!!scanMerge(st,N), stats in returns. First 100 algebra-tested extensions compared to R275 full elimination. R276 support count self-checks executed. No previous prefix reclassified. Mixed theorem not part of strict calculation.

Cumulative strict sixth-pencil frontier 422650/667787 classified, 2954 necessary-condition survivors, 245137 unclassified, next [5350,0]. Retain previous banks. K6 remains 1–2. Next: finish remaining strict prefixes, then singleton directions; implement circuit dictionary and compare mixed projection against full mixed FM, including actual germ row generation, before claiming mixed X6 search. Independent review and Activity association pending.
