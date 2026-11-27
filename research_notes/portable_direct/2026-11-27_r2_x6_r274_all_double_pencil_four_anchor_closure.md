# X6 R274 — complete double-pencil four-anchor closure, c=1

2026-11-27. Independent informed TASK_RESEARCH, author calculation, NOT_REVIEWED. Client identity check successful, no own researcher binding confirmed. Native read r2-20261127-r274-task-read SUCCEEDED 2026-11-27T10:08:06.620576Z at Source 8d89db776e66c4d473ddc466afabf5391006ab3a, NO_CANONICAL_PUBLICATION_DIRECTORY; not an active-owner projection. No CLAIM, Result, Review or shared control mutation. Activity association pending. P000 V5 and ACTIVE worldview retained; the coordinates and arithmetic below are auxiliary observer coefficient computations, not native spatial dynamics.

## Frozen inputs and inherited proof
R247 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa); R272 c3e405cc28d132404e5c9280b364d58a179a8ef8:research_notes/portable_direct/2026-11-27_r2_x6_r272_double_pencil_four_anchor_affine_scan.md; R273 9a92a7a6be912cfbad2efeb719db6c117dce1384:research_notes/portable_direct/2026-11-27_r2_x6_r273_infinity_double_pencil_closure.md. Same Port 10, 1935 directions, six-pair BRC, (17t,B,22t,D), strict 3/2, 47 labels, 51 endpoints, 98 germs, 2225 linear suffix partitions. All conclusions inherit necessary-wall and complete pure-linear suffix premises. R272 proof: with two zeros on each of two independent pencils, normalized c=1 form in auxiliary coordinates x,y,D is D²-(h1+h2)xD-(h3+h4)yD+h1h2 x²+h3h4 y²+lambda xy. Each of all three germ jet rows is affine in lambda. Exact rational event points plus open-interval representatives exhaust every lexicographic germ observation, including additional zeros and tangent cases. Identically zero germ unassigned as necessary relaxation. Apply direct support count and frozen can(mask,5) on both branches; only exchange symmetry deduplicated. No change to pins or arithmetic.

## Actual execution
Six separate executions of exact R272 patch on pinned R247 JS. All 5457 previously unclosed families covered, no CUT, no survivors. First run aggregates two groups; the rest as printed below. Per-group figures count per-family distinct masks, not globally distinct conics; memo reset per execution. Columns: pencil combination; families; rational events; samples; mask bank; direct exclusions; recursive exclusions; capacity checks.
```
B=4t with B=9t or 2B=5t     180  29826  59832  11112  10988 124 205085
2B=5t with B=9t              45   7528  15101   2895   2892 3 141
2B=5t with B=17t            540  86900 174340  29314  29109 205 311303
B=17t with B=9t             108  17557  35222   6499   6254 245 430993
B=17t with B=4t             360  57344 115048  20069  19713 356 628252
B=0 with B=9t               198  32203  64604  12026  10995 1031 1576662
B=0 with B=4t               660 104836 210332  37720  36459 1261 2900752
B=0 with 2B=5t              990 158477 317944  55116  52161 2955 6206445
B=0 with B=17t             2376 372284 746944 118937 109655 9282 12366400
TOTAL                      5457 866955 1739367 293688 278226 15462 24626033
```
All arithmetic BigInt, exact rational cross products. Each run returned cut:null and empty surviving masks. Checks include repeated cache costs across runs. Author calculation, not independent review.

## Reproduce exact six runs
Use first JS block of R247 and first javascript block of R272; replace the original return inside experiment with R272 patch and terminal experiment(data) with return experiment(data), as in R272. For each run replace the original directions literal [[0n,1n],[1n,9n],[1n,4n],[1n,17n]] with the literal below. For runs 5 and 6 also replace loop 'of [1,2]' with 'of [1]'. No other change. Aggregate out per J group as required; assert cut===null, every survivors array empty, direct+excluded===bank and samples===2*events+1 per family. Actual output IDs:
```
1 [[1n,4n],[1n,9n],[2n,5n]]
  [[21,23,29,46,48],[5,6,43],[3,4,8,12,14,16]]
2 [[2n,5n],[1n,9n],[1n,17n],[1n,4n]]
  [[3,4,8,12,14,16],[5,6,43],[1,19,20,25,26,28,34,37,39],[21,23,29,46,48]]
3 [[1n,17n],[1n,9n],[1n,4n]]
  [[1,19,20,25,26,28,34,37,39],[5,6,43],[21,23,29,46,48]]
4 [[1n,0n],[1n,9n],[1n,4n]]
  [[9,10,11,15,38,40,42,44,45,47,49,50],[5,6,43],[21,23,29,46,48]]
5 [[1n,0n],[2n,5n]]
  [[9,10,11,15,38,40,42,44,45,47,49,50],[3,4,8,12,14,16]]
6 [[1n,0n],[1n,17n]]
  [[9,10,11,15,38,40,42,44,45,47,49,50],[1,19,20,25,26,28,34,37,39]]
```

## Consequence and next
The six multipoint pencil sizes (4,9,12,5,6,3) yield 6237 distinct pairs of two-anchor choices on different pencils. R272+R273 cover 780 involving t=0, this run covers all other 5457. Each normalized restriction is monic in the finite ordinate, so at most two distinct finite zeros per pencil. Thus a viable sole quadratic root with c=1 can have two finite zeros on at most ONE pencil. The other pencils can have zero or one finite zero each, including singleton pencils; no assumption of exactly four zeros in exclusion. This is a full closure of double-pencil families, not general c=1 closure. Next prioritize the generic strict/weak sign extension of R259/R261 using shared slopes e,f and circuit inequalities, with at most one doubled pencil. Do not repeat these 6237 families. K6 remains 1–2, independent review pending.
