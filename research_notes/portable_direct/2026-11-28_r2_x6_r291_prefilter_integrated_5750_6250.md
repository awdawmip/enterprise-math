# X6 R291 — strict sixth-pencil continuation, prefixes 5750–6250

2026-11-28. Independent informed TASK_RESEARCH, author computation, NOT_REVIEWED. Native original request r2-20261128-0907-x6-read SUCCEEDED at 2026-11-28T01:07:49.711696+00:00, Source 3a78d123af6ee69d3577a52e38594ca63800267e, NO_CANONICAL_PUBLICATION_DIRECTORY. Native operational owner view not evaluated; own researcher/session binding unconfirmed, no CLAIM or shared state mutation. Activity association pending. Global main@54b70d7c95bc58dc89bba35214d8c16f204f3c64 (both entries verified by immutable ref); global P000 V4 startup projection canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc and Source P000 V5, ACTIVE worldview, joint/residual fidelity. Auxiliary coefficient arithmetic of frozen observer, not new native spatial/time computation.

## Frozen inputs and scope
Direct continuation of R290@83291ecba974f8976a92a63411797cbface14ea3:research_notes/portable_direct/2026-11-28_r2_x6_r290_prefilter_integrated_5350_5750.md (main blob verified 00d7918b0b66356d76d10ace66f6cf625ed9bedc), with exact R289@4238b205c0040ae3c89c96f7e124e09a2e00c064:research_notes/portable_direct/2026-11-28_r2_x6_r289_exact_next_slope_projection_remaining_bank.md. R283@d0fb62e0871f9ca48c692291d0caeca77d3e0055 gives the R247/R275/R276/R277/R280/R281/R282 immutable pins and paths; all eight R247/275/276/277/280/281/282/289 sources fetched at exact refs for actual execution. Port 10, 1935 directions, 47 labels, 51 endpoints, 98 germs, 2225 suffix partitions unchanged. Capacity exclusions inherit R247 necessary-wall and complete pure-linear suffix premises. Strict c=1 six multipoint pencils only. Prior complete frontier [5750,0], 454250/667787 classified, 3315 necessary-condition survivors.

## Executed result
R290 classification order retained: direct support label count >31, R289 exact necessary slope mask, full joint endpoint coefficient feasibility via R282 scanMerge, can(x,5) and can(y,5). Do not substitute slope projection for full joint state. All 79 word indices and two germ masks remain recoverable from frozen input and prefix/sixth word indices.

Actual BigInt run (start=5750, size=500, ceiling=12000000):
```json
{"hist":{"direct":22523,"alg":14831,"recursive":1762,"surv":384,"visits":39500,"checkedAgainstOld":100,"prefilter":8720},"checks":5830104,"next":[6250,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":500,"rawRows":26335,"hullRows":2074,"pairRows":2677,"hullIntersections":43104,"pairDominanceTests":167645,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":45269,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":75988,"mergeCompared":0,"mergeSort":5131193,"mergeComparisons":680060,"mergeIntersections":1960580},"partial":false}
```
All 39500 visits finished with no cutoff. Full algebra rejection 6111; 16977 pass direct capacity; 8720 rejected by prefilter and 8257 require full algebra (51.36% avoided relative to no prefilter). 2146 pass full algebra; 1762 fail recursive capacity, 384 survive. The first 100 full-algebra tests agree with R275 complete Fourier–Motzkin. R276 support-count self-checks rerun. All output bank records strictly increasing in range [5750,6250), positive masks <=79 bits, subset of matching R289 slope mask, total popcount 384. No timing or independent review claim.

R289's slope-only mask rejects 23401 of this block, of which 14681 overlap direct label rejections (not counted twice). Remaining unclassified suffix [6250,8453): 174037 = 116510 proved slope-incompatible + 57527 slope-compatible. Cumulative fully classified 493750, 3699 necessary-condition survivors. 610260 of 667787 fully classified or proved impossible (without overlap). No new correct tree or lower-bound improvement; K6 remains 1–2.

## Reproduction
Use R290 exact recipe, R283 pinned input paths, R289 first text bank indexed from 5350. R247 first JS before ' function actual(', change function signature to experiment(data,bank,start,size,masks), replace single-line cc/count with R276 first JS. R275 first JS before 'let states=', append [1n,0n] to dirs. R277 first JS tail with R280/R281/R282 first JS blocks inserted immediately before function grow; increment pairCalls in grow pair, set ceiling=12000000, use raw=grow(empty,R), verify raw, st=prune(raw); replace good=!!grow(st,N) by good=!!scanMerge(st,N). Immediately before 'let N=p.R.slice();' insert R290 exact prefilter:
```javascript
if(!(masks[i-5350]&(1n<<BigInt(j)))){
 hist.prefilter=(hist.prefilter||0)+1;
 hist.alg++;hist.visits++;continue;
}
```
Use exact JSON literal from R247 first JS, R276 first text bank trimmed; verify R289 masks indices and length 3103. Include stats in both returns. Pass start=5750,size=500. First 100 full algebra checks remain. The block below is the actual serialized output.

## New bank (prefix:hex sixth-mask)
```text
5751:201c0380
5752:1c0380
5754:2030000000
5755:300200
5756:300200
5758:30000000
5759:300200
5760:300600
5761:60000000
5762:40300000
5763:20400000000000
5866:80100
5868:80100
5891:20000000
5909:20000000
5929:60000000000000000
5943:8
5945:40601c0380
5946:c070000000
5947:201c0380
5948:40701c0380
5950:60f0000000
5951:c0f078000000
5952:c0700200
5953:80c0100000
5954:40700200
5955:c0700200
5957:830000000000000
5958:f0000000
5959:c0c078000000
5960:c0700600
5961:c0100000
5962:40700600
5963:c0700400
5964:101c0e0000000
5965:40c0f078000000
5966:100c0300000
5967:80c060180000
5968:10080600000
5969:10080600400
5970:30e1c00000000000
5971:273ce1c00000000000
5972:10000000000
5973:8181c000000000
5974:10080000000
5975:1018040100000
5976:10000000000
5977:10000000000000000
5980:8000000000000000
5992:4020000000
5994:181c1e0000000
5999:80800020000000
6002:18181e0080000
6007:180600000
6008:20783c0000000
6009:8000000000000000
6010:180600000
6011:20383c0f00000
6014:103030000000000
6016:2030000000000
6017:307078000000000
6018:8000000000000000
6019:60300c00000
6020:4000000000000
6021:60300c00000
6022:4000000000000
6031:16200000000000000000
6037:100000000000000
6038:c380000000000000
6039:c000000000000000
6041:306000000000000
6042:8000000000000000
6050:f00
6051:300
6055:700
6056:180
6059:200400
6060:200000
6070:c00000
6071:c00000
6074:800000
6076:c00
6077:600
6078:200
6079:400
6087:c01800
6088:c01800
6091:1000
6093:1000
6098:200
6099:200
6101:200
6102:600
6107:1000
6109:200
6186:10
6187:10
6197:180
6204:c0
6206:c0
6225:80
6226:80
```

## Next
Resume [6250,0] (not [5750,0]). Finish the remaining strict prefix classifications, then singleton directions and general zero/germ words. Earlier banks stay unchanged. Independent review and Activity association pending.
