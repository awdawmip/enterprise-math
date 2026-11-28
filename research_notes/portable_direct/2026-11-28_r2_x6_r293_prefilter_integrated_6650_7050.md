# X6 R293 — strict sixth-pencil continuation, prefixes 6650–7050

2026-11-28. Independent informed TASK_RESEARCH, author computation, NOT_REVIEWED. Native read r2-20261128-1108-x6-read SUCCEEDED at 2026-11-28T03:08:53.521584+00:00, Source 06a581da1e8b763e344a3ddb7e7aba757cff1130, NO_CANONICAL_PUBLICATION_DIRECTORY (absence only; native owner view not evaluated). Own researcher binding unconfirmed; no CLAIM or shared mutation. Activity association pending. Global main@04c5793f51795b518e137c9ff0f0dc83e3bd4698: both entry blobs verified at immutable ref, global P000 V4 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, Source P000 V5, ACTIVE worldview, joint/residual preservation and current portable/method policy read. Computation is exact auxiliary coefficient algebra and mask operations of the frozen BRC observer, not native spatial propagation or time dynamics.

## Frozen inputs and scope
R292@6a35a3bc561113e1564285277e15cd69f8cb0dbc:research_notes/portable_direct/2026-11-28_r2_x6_r292_prefilter_integrated_6250_6650.md (blob 5ab5f0d6662e37be1f3caa0caf84a4f06e8041bd, also read at current main). Prior frontier [6650,0], 525350 fully classified, 3742 necessary-condition survivors. Exact source reads:
- 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa)
- 001076e59298e45715cb58c87ab3395c53d005a8:research_notes/portable_direct/2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md (blob 9732c23573cf3071a782d0b84d511494ebb1c745)
- 33fba542db5f810e803d770b7046b5e26ac1ebb9:research_notes/portable_direct/2026-11-27_r2_x6_r276_strict_fifth_pencil_packed_frontier.md (blob 597a62f00fb89d9624e301bbca97f0073b37a040)
- a1df3c1aa315909d8c109ef8551f24a460a44b1f:research_notes/portable_direct/2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md (blob 07f98d725cf2ba6b0b2d5fa43ff632b1fdc73982)
- 3366eecf953f9943f8a9d88b36279f221cb1e1c7:research_notes/portable_direct/2026-11-27_r2_x6_r280_joint_affine_envelope_sixth_prefix.md (blob e04d3e08b0f2c503eee4890cef6b9818fca0720d)
- eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb:research_notes/portable_direct/2026-11-28_r2_x6_r281_active_pair_sweep_sixth_prefix.md (blob c4a80588e2161a2f0b9ae5aa709eee59a3d2941d)
- 7eaf45451067577903587a9f979a8e5d8742913a:research_notes/portable_direct/2026-11-28_r2_x6_r282_sorted_hull_merge_sixth_prefix.md (blob 7cccd762c6da794eea71683a5cdbfd2a141c63c0)
- 4238b205c0040ae3c89c96f7e124e09a2e00c064:research_notes/portable_direct/2026-11-28_r2_x6_r289_exact_next_slope_projection_remaining_bank.md (blob f6e9e2ffcf895228bfa66bac061b54a8cbb07a76)
Same Port 10, 1935 directions, 47 labels, 51 endpoints, 98 directed germs, 2225 pure-linear suffix partitions. Strict c=1 six multipoint pencils only; capacity exclusions inherit R247 necessary-wall and complete suffix premises. R289 marginal is used only as a necessary filter; no original joint words, endpoint/germ masks or full feasible region replaced.

## Actual computation
BigInt start=6650,size=400,ceiling=12000000. R292 reconstruction and original direct-capacity -> exact slope filter -> full joint algebra -> recursive-capacity classification order. R276 count checks and first 100 full-algebra comparisons with R275 complete elimination ran. No cutoff.
```json
{"hist":{"direct":11185,"alg":18041,"recursive":2335,"surv":39,"visits":31600,"checkedAgainstOld":100,"prefilter":13315},"checks":5424489,"next":[7050,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":400,"rawRows":16363,"hullRows":1625,"pairRows":1903,"hullIntersections":25920,"pairDominanceTests":69311,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":29720,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":54815,"mergeCompared":0,"mergeSort":2727432,"mergeComparisons":293855,"mergeIntersections":1197548},"partial":false,"remaining":110837,"remainingSlopePass":37139,"remainingSlopeReject":73698,"directSlopeOverlap":6827,"cumulative":556950,"cumulativeSurvivors":3781}
```
Full algebra rejects 4726; full solves 7100 out of 20415 after direct test. Prefilter avoided 13315 full solves (65.2217%). Direct-priority overlap with slope rejection 6827. No wall-clock improvement claim. All output bank entries verified strictly increasing in range, positive at most 79 bits, subset of corresponding R289 masks; popcount 39; classification total verified. Remaining suffix counts recomputed directly from R289 exact mask bank. Cumulative 556950/667787 classified, 3781 necessary-condition survivors; 110837 remaining = 73698 slope-proved impossible and 37139 not yet fully checked. K6 remains 1–2.

## Reproduction
Follow exact R292 source reconstruction; use start=6650,size=400,ceiling=12000000. Source assembly takes first JS block of every pinned file; parse R247 data JSON literal between 'const data=' and ';\nexperiment(data)'. Take R247 prefix before ' function actual(', change signature to (data,bank,start,size,masks), replace single-line cc/count with R276 first JS. Take R275 before 'let states=', append [1n,0n] to dirs. Insert R280/R281/R282 first JS before R277 function grow, increment pairCalls in grow's pair; set ceiling; replace st=grow(empty,R) by raw=grow(empty,R), check nonnull and st=prune(raw). Replace good=!!grow(st,N) by good=!!scanMerge(st,N). Insert R290 mask filter before 'let N=p.R.slice();' (if bit unset, increment hist.prefilter, hist.alg, hist.visits and continue). Add stats to both returns. Read first text blocks of R276 and R289, latter first two colon fields, verify all 3103 indices 5350+i. Keep first 100 full algebra comparisons. Run and check bank and remaining mask counts as stated.

## Actual new bank (prefix:hex sixth-mask)
```text
6666:1
6672:4020000000
6673:404030000000
6682:20000000
6683:8000404020000000
6689:8000004020000000
6691:8000004020080100
6693:8000000000000000
6694:20000000000
6695:4000000000000
6696:20000000000
6697:4000000000000
6838:8000000000000000
6889:4000000000000000
6890:18e000000000000000
6892:8000000000000000
6894:40000000000
6918:8000000000000000000
6955:300
6962:100
7014:400000
```

## Next
Resume [7050,0]. Preserve all earlier banks; finish remaining strict sixth-line prefixes then singleton directions and mixed zero/germ words. Independent mathematical review and Activity association pending.
