# X6 R292 — strict sixth-pencil continuation, prefixes 6250–6650

2026-11-28. Independent informed TASK_RESEARCH, author computation, NOT_REVIEWED. Native original read r2-20261128-1009-x6-read SUCCEEDED at 2026-11-28T02:09:20.357432+00:00, Source cf24efc9ac30c393c49bc143fe34f7d2959d7ae4, NO_CANONICAL_PUBLICATION_DIRECTORY; native operational owner view not evaluated. Own binding unconfirmed; no CLAIM or shared state mutation. Activity association pending. Global canonical main@d70c456e72846a5058b5538fc91aeab0190d4471 (both entry blob SHAs verified at immutable ref), P000 V4 startup projection canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, Source P000 V5, ACTIVE worldview and joint/residual fidelity read. Auxiliary coefficient arithmetic of frozen observer, not native spatial or temporal computation.

## Frozen input and scope
Continue R291@85bbc56e42f05e392ce8a4ec6338bb219aaf895f:research_notes/portable_direct/2026-11-28_r2_x6_r291_prefilter_integrated_5750_6250.md, blob 60121cf7a0a758189216e2b965760171cc489e23. Exact pins read for execution: R247@7e54892a45579bdc497c27e061399339d1fb3512, R275@001076e59298e45715cb58c87ab3395c53d005a8, R276@33fba542db5f810e803d770b7046b5e26ac1ebb9, R277@a1df3c1aa315909d8c109ef8551f24a460a44b1f, R280@3366eecf953f9943f8a9d88b36279f221cb1e1c7, R281@eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb, R282@7eaf45451067577903587a9f979a8e5d8742913a (exact paths in R283@d0fb62e0871f9ca48c692291d0caeca77d3e0055:research_notes/portable_direct/2026-11-28_r2_x6_r283_sixth_prefix_4700_and_mixed_slack.md), and R289@4238b205c0040ae3c89c96f7e124e09a2e00c064:research_notes/portable_direct/2026-11-28_r2_x6_r289_exact_next_slope_projection_remaining_bank.md. Port 10, 1935 directions, 47 labels, 51 endpoints, 98 directed germs, 2225 linear suffix partitions unchanged. Strict c=1 six multipoint pencils only; inherited R247 necessary-wall and pure-linear suffix premises. Prior frontier [6250,0], 493750/667787 fully classified, 3699 necessary-condition survivors.

## Actual execution
Same R291/R290 classification order and R282 exact scanMerge. R289 mask is a necessary marginal check; joint coefficient state and both germ masks retained. BigInt start=6250,size=400,ceiling=12000000. The first 100 full-algebra checks agree with R275 complete Fourier–Motzkin; inherited R276 count self-checks ran. No cutoff.

```json
{"hist":{"direct":15149,"alg":15061,"recursive":1347,"surv":43,"visits":31600,"checkedAgainstOld":100,"prefilter":11817},"checks":2851649,"next":[6650,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":400,"rawRows":19376,"hullRows":1960,"pairRows":2439,"hullIntersections":31354,"pairDominanceTests":117671,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":23097,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":38648,"mergeCompared":0,"mergeSort":2236263,"mergeComparisons":311979,"mergeIntersections":937068},"partial":false,"remaining":142437,"remainingSlopePass":48597,"remainingSlopeReject":93840}
```

All 31600 visits completed. Direct 15149; prefilter algebra rejection 11817; full algebra rejection 3244; recursive rejection 1347; survivors 43. 16451 passed direct count, only 4634 needed full algebra (11817 avoided, about 71.83%). 1390 passed full algebra. No timing claim. R289 slope-only rejection in this block is 22670, of which 10853 overlap direct-priority exclusions. Output bank checked strictly increasing indices in range, positive <=79-bit masks, subset of corresponding R289 mask; popcount 43. Classification sum checked. Remaining slope-pass and reject counts recomputed directly from R289 mask bank.

Cumulative 525350/667787 fully classified, 3742 necessary-condition survivors. Remaining 142437 = 93840 slope-proved impossible + 48597 slope-compatible not fully classified. Thus 619190/667787 classified or proved impossible without overlap. No new tree or lower-bound improvement; K6 remains 1–2.

## Reproduction
Use R291 exact recipe, replacing start=6250,size=400. Actual source assembly: extract first javascript block of each pinned source, parse R247 JSON literal after 'const data=' before ';\nexperiment(data)'; take R247 prefix before ' function actual(', change experiment signature to (data,bank,start,size,masks), replace single-line cc/count by R276 first JS. Take R275 before 'let states=', replace '[1n,17n]]' by '[1n,17n],[1n,0n]]'. Insert R280/R281/R282 blocks before R277 'function grow('; increment pairCalls in grow's pair; set ceiling=12000000; replace st=grow(empty,R) with raw=grow(empty,R), verify raw and prune; replace good=!!grow(st,N) by good=!!scanMerge(st,N). Before 'let N=p.R.slice();' insert R290 prefilter (increment hist.prefilter, hist.alg, hist.visits and continue if mask bit unset). Include stats in both returns. Decode R276 first text bank and R289 first text block (first two colon-separated fields only); verify R289 index 5350+i, length 3103. First 100 full algebra comparisons retained. Invoke assembled function with exact input. Check output and suffix counts as above.

## Actual new bank (prefix:hex sixth-mask)
```text
6275:e01c0
6276:80100
6278:80300
6295:80000
6316:200
6317:200
6596:100000
6598:4020000000
6599:100000
6600:40000000
6601:4020000000
6612:10000000
6613:100200
6615:20000000
6616:100200
6617:40000000
6618:20000000
6625:4020000000
6626:100000
6629:80000000
6631:80200400
6632:400
6635:1018000000000
6636:8000000000
6637:10000000000
6640:8000000000000000
```

## Next
Resume [6650,0], not [6250,0]. Finish remaining strict sixth-line prefixes; then singleton directions and mixed zero/germ words. Prior banks unchanged. Independent review and Activity association pending.
