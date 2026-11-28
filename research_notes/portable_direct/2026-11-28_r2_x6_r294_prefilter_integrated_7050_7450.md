# X6 R294 — strict sixth-pencil continuation, prefixes 7050–7450

2026-11-28. Independent informed TASK_RESEARCH, author computation, NOT_REVIEWED. Native request r2-20261128-1210-x6-current SUCCEEDED at 2026-11-28T04:10:32.600114+00:00, Source fa1ede92939e8065881bd9ccc024602bf57ccaaa, NO_CANONICAL_PUBLICATION_DIRECTORY (absence only; native owner view not evaluated). Own researcher binding unconfirmed; no CLAIM or shared-state mutation. Activity association pending. Global canonical main@698f9c63ab45ac88cc817b34d6155bddfc24f1c7, both entry blobs checked at immutable ref; global P000 V4 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Source P000 V5, ACTIVE worldview, joint/residual fidelity and current portable/method policies read. Auxiliary exact coefficient algebra of frozen BRC observer, not new native geometry or dynamics.

## Frozen inputs and scope
R293@1b87856acaa150378c23abc1c33cd87f14d5f2e7:research_notes/portable_direct/2026-11-28_r2_x6_r293_prefilter_integrated_6650_7050.md (blob 21faa073e7170be065bf1fa710348d6d8b653113, also verified on main). Prior [7050,0], 556950 classified, 3781 necessary-condition survivors. All eight exact inputs re-read (paths relative to research_notes/portable_direct/):
- 7e54892a45579bdc497c27e061399339d1fb3512:2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (fdbef2ee6e6c32573f3a1ccd171cb5337de520fa)
- 001076e59298e45715cb58c87ab3395c53d005a8:2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md (9732c23573cf3071a782d0b84d511494ebb1c745)
- 33fba542db5f810e803d770b7046b5e26ac1ebb9:2026-11-27_r2_x6_r276_strict_fifth_pencil_packed_frontier.md (597a62f00fb89d9624e301bbca97f0073b37a040)
- a1df3c1aa315909d8c109ef8551f24a460a44b1f:2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md (07f98d725cf2ba6b0b2d5fa43ff632b1fdc73982)
- 3366eecf953f9943f8a9d88b36279f221cb1e1c7:2026-11-27_r2_x6_r280_joint_affine_envelope_sixth_prefix.md (e04d3e08b0f2c503eee4890cef6b9818fca0720d)
- eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb:2026-11-28_r2_x6_r281_active_pair_sweep_sixth_prefix.md (c4a80588e2161a2f0b9ae5aa709eee59a3d2941d)
- 7eaf45451067577903587a9f979a8e5d8742913a:2026-11-28_r2_x6_r282_sorted_hull_merge_sixth_prefix.md (7cccd762c6da794eea71683a5cdbfd2a141c63c0)
- 4238b205c0040ae3c89c96f7e124e09a2e00c064:2026-11-28_r2_x6_r289_exact_next_slope_projection_remaining_bank.md (f6e9e2ffcf895228bfa66bac061b54a8cbb07a76)
Same Port 10, 1935 directions, 47 labels, 51 endpoints, 98 directed germs, 2225 linear suffix partitions. Strict c=1 six multipoint pencils only; exclusions inherit necessary-wall and complete pure-linear suffix premises. R289 marginal filter is necessary, not a substitute for the joint state. All original words and both germ masks retained.

## Actual exact computation
BigInt start=7050,size=400,ceiling=12000000. R293 reproduction recipe; direct capacity then R289 prefilter then R282 joint algebra then recursive capacity. R276 count self-checks and first 100 full-algebra comparisons to R275 complete elimination executed. No cutoff.
```json
{"hist":{"direct":19158,"alg":11455,"recursive":817,"surv":170,"visits":31600,"checkedAgainstOld":100,"prefilter":6879},"checks":2521082,"next":[7450,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":400,"rawRows":15875,"hullRows":1297,"pairRows":1496,"hullIntersections":24284,"pairDominanceTests":92338,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":17828,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":42870,"mergeCompared":0,"mergeSort":2313083,"mergeComparisons":314774,"mergeIntersections":927831},"partial":false,"remainingSlopePass":24675,"remainingSlopeReject":54562,"cumulative":588550,"cumulativeSurvivors":3951}
```
Full algebra rejection 4576, full solves 5563 of 12442 direct-capacity passes. Prefilter avoids 6879 solves, about 55.29%; no wall-clock claim. All new bank entries checked for strictly increasing indices, range, positive at most 79 bits, subset of R289 masks and total popcount 170. Suffix mask count independently summed from R289. 588550/667787 fully classified; 3951 survivors. Remaining 79237 = 54562 slope-proved impossible + 24675 slope-compatible awaiting full classification. Total classified or proved impossible without overlap: 643112. K6 remains 1–2; no complete tree certificate.

## Reproduction
Use R293 exact source reconstruction, changing start to 7050 and size to 400. Actual source assembly: first javascript blocks of pinned notes; parse R247 data JSON after 'const data=' before ';\nexperiment(data)'; take R247 prefix before ' function actual(', change signature to experiment(data,bank,start,size,masks), replace original single-line cc/count with R276 first JS. Take R275 before 'let states=', append [1n,0n] to dirs. Insert R280/R281/R282 first JS before R277 function grow; increment pairCalls at grow's pair; set ceiling=12000000. Replace st=grow(empty,R) with raw=grow(empty,R), check raw nonnull, st=prune(raw); replace good=!!grow(st,N) with good=!!scanMerge(st,N). Insert R290 mask filter before 'let N=p.R.slice();': if(!(masks[i-5350]&(1n<<BigInt(j)))){hist.prefilter=(hist.prefilter||0)+1;hist.alg++;hist.visits++;continue;}. Include stats in both returns. Parse first text bank of R276 and first text block of R289, the latter first two colon fields; verify length 3103 and index 5350+i. Preserve first 100 full algebra comparisons. Invoke function with frozen data and masks; sum output mask bits and suffix mask bits. No earlier prefix reclassified.

## Actual new bank (prefix:hex sixth-mask)
```text
7067:400
7070:200
7089:1800
7091:40200000000
7093:1800
7117:1000
7120:40
7123:40
7124:40
7142:80
7158:200
7159:300
7189:600
7349:8
7350:8
7355:20000000000000
7356:40601c0300
7357:40601c0380
7363:40000000
7364:40300000
7370:40300000
7397:40c0e070000000
7398:c0e070000000
7400:40c00000000000
7401:303c1e0000000
7403:101c1e0180000
7404:3838380000000
7405:20000000000000
7406:800000000000
7407:20201c0000000
7408:100000000000000
7409:201e0180000
7410:3038380000000
7411:800000000000
7412:100000000000000
7413:20180000000
7414:4060380000000
7415:20180e00000
7416:4060380e00000
7421:206040000000000
7422:4060200000000
7423:4060300000000
7430:8000000000000000000
7436:8000000000000000
7437:200000000000000
7439:180
7440:200400
7445:100200
7447:c00000
7448:c00000
7449:800000
```

## Next
Resume [7450,0]; 1003 five-pencil prefixes left. Preserve earlier banks; finish strict sixth-line classification then singleton directions and mixed zero/germ words. Independent review and Activity association pending.
