# X6 R290 — integrate exact next-slope prefilter into strict sixth-prefix classifier

2026-11-28. Independent informed TASK_RESEARCH; author computation, NOT_REVIEWED. Native query r2-20261128-0811-x6-read SUCCEEDED at 2026-11-28T00:11:11.259075Z, Source bdac3034d85ea327262fe850b4a5e92ec4efda09: NO_CANONICAL_PUBLICATION_DIRECTORY (not native owner projection). Own researcher binding unconfirmed; no CLAIM or shared task-state mutation. Activity association pending. Global immutable main snapshot fa3d69131c0aff6ad25c208ec5403f16a1e1fc16; global P000 V4 projection canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, Source P000 V5, ACTIVE worldview, joint/residual fidelity. Auxiliary coefficient arithmetic, not new native geometry.

## Scientific input and scope
Frozen R289@4238b205c0040ae3c89c96f7e124e09a2e00c064:research_notes/portable_direct/2026-11-28_r2_x6_r289_exact_next_slope_projection_remaining_bank.md; its R288 and R247/R275/R276 pins unchanged. R283 reconstruction recipe at d0fb62e0871f9ca48c692291d0caeca77d3e0055:research_notes/portable_direct/2026-11-28_r2_x6_r283_sixth_prefix_4700_and_mixed_slack.md; exact R277/R280/R281/R282 pins there. Same Port 10, 1935 directions, 47 labels, 51 endpoints, 98 germs, 2225 suffix partitions. Prior full frontier [5350,0] (422650/667787, 2954 survivors). R289 mask bank is an exact necessary slope-only predicate, not a full joint state. All classifications inherit the pinned necessary-wall and pure-linear suffix premises.

## Exact integration and result
For each previously unclassified extension, preserve original classification order: first direct label count >31 on either branch; then consult R289's slope mask; if bit unset classify algebraic infeasible, otherwise generate the full local and quartet rows and solve by R282 scanMerge; finally apply can(x,5) and can(y,5). The additional slope check changes no classification because R289 proved it is necessary for full endpoint coefficient feasibility. It avoids generating full quartet constraints for extensions rejected after the direct test. All original words, both germ masks, and the old full slope envelope are retained; the marginal is not substituted for the joint feasible region. This is a compositional application of R289 and R282, not a new general theorem.

Actual BigInt execution (start=5350,size=400, capacity ceiling=10000000):
```json
{"hist":{"direct":18856,"alg":11259,"recursive":1124,"surv":361,"visits":31600,"checkedAgainstOld":100,"prefilter":6381},"checks":4368098,"next":[5750,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":400,"rawRows":22209,"hullRows":1498,"pairRows":1708,"hullIntersections":36459,"pairDominanceTests":154551,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":33026,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":58202,"mergeCompared":0,"mergeSort":3805189,"mergeComparisons":515105,"mergeIntersections":1438934},"partial":false}
```
All 31600 visits finished, no cutoff. 6381 of 11259 algebra rejections were decided directly by R289 after the direct capacity test; 4878 needed full algebra. After direct count 12744 extensions remained, 6363 full algebra solves were needed, including 1485 algebra-feasible extensions. Compared to running full algebra on all 12744, the prefilter avoids 6381 solves (50.07% of this batch's would-be full solves); no wall-clock speed claim. 100 full-algebra-tested extensions agree with R275 full Fourier–Motzkin. R276 count-observer self checks executed in inherited code. The prefilter's skipped branch uses R289's already verified projection certificate, not a new direct full-algebra cross-check for those 6381. Serialized bank cross-checked after execution: strictly increasing indices, positive masks <=79 bits, popcount 361, every set bit permitted by corresponding R289 mask.

Across the entire 400-prefix block, the R289 slope-only bank had 18829 rejected and 12771 passed before capacity tests; direct-priority overlap with slope rejections was 12448. In the still-unclassified suffix [5750,8453), 139911 slope-rejected and 73626 slope-compatible extensions remain, total 213537. These slope-only rejections are already proved impossible but not yet assigned to original sequential categories; do not double-count.

## Reproduce
Use exact R283 reconstruction: R247 first JS prefix before ' function actual(', change function signature to experiment(data,bank,start,size,masks); replace single-line original cc/count with R276 first JS block. R275 first JS before 'let states=', append [1n,0n] to dirs. R277 first JS tail, insert first JS blocks of R280/R281/R282 before function grow, increment pairCalls at the start of grow's pair(p,m), set ceiling=10000000. Replace old st=grow(empty,R) by raw=grow(empty,R), check raw nonnull, then st=prune(raw). Replace good=!!grow(st,N) by good=!!scanMerge(st,N). Immediately before 'let N=p.R.slice();' insert:
```javascript
if(!(masks[i-5350]&(1n<<BigInt(j)))){
 hist.prefilter=(hist.prefilter||0)+1;
 hist.alg++;hist.visits++;continue;
}
```
Decode masks from R289 first text block in order: split each record on ':', verify +field[0]===5350+i and length 3103, use BigInt("0x"+field[1]). R247 data literal parsed as JSON from its first JS block. Pass R276 first text bank trimmed, start=5350,size=400,masks. Include stats in both returns. First 100 full algebra comparisons stay intact. Preserve partial frontier if future batch hits capacity ceiling. Do not revisit earlier classified words.

## New bank (prefix:hex sixth-mask)
```text
5379:40000000000000000
5390:40601c0380
5391:c060000000
5392:201c0380
5393:40601c0300
5395:60f0000000
5396:c0c060000000
5397:c0700000
5398:80c0100000
5399:40700000
5400:c0300000
5402:20000000000000
5403:f0000000
5404:c0c060000000
5405:c0700000
5406:c0100000
5407:40700000
5408:c0300000
5409:101c0e0000000
5410:c060000000
5411:100c0300000
5412:c060000000
5413:10080200000
5414:10080200000
5415:430e1c00000000000
5416:638c1800000000000
5417:10000000000
5418:1010000000000
5419:10080000000
5420:10000000000
5438:4020000000
5440:c1e0000000
5445:800020000000
5448:81e0000000
5453:180600000
5454:783c0000000
5456:180600000
5457:783c0f00000
5460:103030000000000
5462:2030000000000
5463:6070000000000
5465:4000000000000
5466:4000000000000
5471:4000000000000000000
5478:100000000000000
5479:300000000000000
5480:8000000000000000
5486:f00
5487:300
5489:400
5490:100
5492:200400
5493:200000
5503:c00000
5504:c00000
5506:800000
5507:800000
5509:c00
5510:e00
5511:c00
5518:c01800
5519:c01800
5522:1000
5524:1000
5525:600
5528:1000
5542:600
5543:200
5544:200
5545:200
5557:20
5561:c0
5598:80
5600:180
5601:c0
5602:80
5605:80
5606:c0
5609:c0
5610:c0
5611:10
5613:1c0
5614:1c0
5634:60000
5636:40180
5644:40000
5661:380
5662:380
5664:380
5671:380
5672:403e0
5674:403e0
5696:200
5698:2038000000
5699:180
5700:201e03c0
5703:180300
5705:180300
5719:1030783e000000
5720:6038000000
5721:20080000
5728:60703c000000
5729:4030000000
5730:20080100
5734:406038000000
5735:80000
5738:100
5746:100
5749:200
```

## Next
Full sequential frontier 454250/667787 classified, 3315 necessary-condition survivors, 213537 not fully classified, next [5750,0]. Complete remaining strict prefixes with R289 mask integration then singleton directions and mixed zero/germ families; K6 remains 1–2. No correct tree or independent review claimed. Activity association pending.
