# X6 R283 — sixth-pencil continuation and mixed strict/weak infinitesimal lift

2026-11-28. Independent informed TASK_RESEARCH; author proof and computation, NOT_REVIEWED. P000 V5/global V4, ACTIVE worldview and joint/residual fidelity retained. Auxiliary affine coefficient algebra of the frozen BRC observer only, not native geometry or dynamics. Native request r2-20261128-0214-x6-read SUCCEEDED at 2026-11-27T18:14:39.174622Z, Source df6911494c9a585daf126950a8f3c7ad8dd386ed, NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection; own binding unconfirmed. No CLAIM or shared state mutation. Activity association pending.

## Frozen inputs
- R247: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md
- R275: 001076e59298e45715cb58c87ab3395c53d005a8:research_notes/portable_direct/2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md
- R276: 33fba542db5f810e803d770b7046b5e26ac1ebb9:research_notes/portable_direct/2026-11-27_r2_x6_r276_strict_fifth_pencil_packed_frontier.md
- R277: a1df3c1aa315909d8c109ef8551f24a460a44b1f:research_notes/portable_direct/2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md
- R280: 3366eecf953f9943f8a9d88b36279f221cb1e1c7:research_notes/portable_direct/2026-11-27_r2_x6_r280_joint_affine_envelope_sixth_prefix.md
- R281: eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb:research_notes/portable_direct/2026-11-28_r2_x6_r281_active_pair_sweep_sixth_prefix.md
- R282: 7eaf45451067577903587a9f979a8e5d8742913a:research_notes/portable_direct/2026-11-28_r2_x6_r282_sorted_hull_merge_sixth_prefix.md
Same Port 10, 1935 directions, six-pair BRC, 47 support labels, 51 endpoints, 98 oriented germs, 2225 suffix partitions. Capacity exclusions inherit R247 necessary-wall and complete suffix premises. Strict c=1 six multipoint pencils only in computation. Prior R282 371300 classified, 2764 survivors, next [4700,0].

## Mixed strict/weak lift lemma (proof, not executed in X6)
For any finite system of rational affine rows r_i(e,f)=A_i e+B_i f+C_i with either >0 or >=0, write s_i=1 for strict and 0 for weak. Replace all rows with r_i(e,f)>=s_i delta in the ordered field Q(delta) of rational functions at positive infinitesimal delta (sign of first nonzero coefficient at zero). Equality is two weak rows. This lifted system has a solution over Q(delta) iff the original system has a real solution. Forward: choose a sufficiently small positive rational delta avoiding poles and preserving the signs of finitely many rational-function differences; the evaluated rows satisfy the original strict/weak requirements. Reverse: if a real solution exists, rational solutions exist: eliminate equality rows by rational Gaussian elimination on the tight weak rows at that solution; the resulting rational affine subspace has rational points dense in its real points, and sufficiently nearby rational points preserve the finitely many remaining positive slacks. A constant rational solution then satisfies the lifted weak rows for infinitesimal delta. This argument also handles empty sets, all weak rows, and equality-only systems.

All line intercepts and pair projections are affine in delta, with rational slopes (the original A,B are fixed). Thus exact comparisons of values or switch events need only lexicographic rational pairs (constant, delta coefficient); division only by nonzero rational constants. Construct each max envelope in this ordered field, merging equal slopes by lexicographic intercept. For positive A take lower bound (-Bf-C+s_i delta)/A; for negative A take the negative of the upper bound, (Bf+C-s_i delta)/A. Both have slope -B/|A| and constant (-C+s_i delta)/|A|. Existence of e iff L(f)+H(f)<=0, not <0. Flat rows retain weak sign in lifted field. Closed projected bounds must be allowed to coincide. The R281 simultaneous active-pair proof works over this ordered field: every selected pair is a globally necessary inequality, at each f some selected pair attains the maximum sum, including coincident switch events by algebraic equality. At most p+m-1 pairs when both sides nonempty. A hull line with only point activity may be removed because all lifted bounds are weak and the other tied lifted line enforces the same value. This is the critical difference from discarding a point-only strict row in the original real envelope.

Example: e>=f, e>=-f, e>0, e<=0. The real value envelope max(f,-f,0)=|f| and upper 0 would wrongly accept (0,0) if strict point activity were lost. Lift gives e>=max(f,-f,delta), e<=0, hence impossible; the formerly point-only row has a genuine interval (-delta,delta). No numerical epsilon or approximation. Projection intervals, hulls and delta coefficients must be retained; do not replace them by standard-part intervals. Original endpoint/germ data stay distinct. This lemma is a coefficient feasibility method; not a proof that the full mixed X6 search is already implemented. R275 zero-germ residual lifting still requires exact generation and elimination of the intercept rows, before applying a two-parameter solver. A common strict margin applies to any finite number of rows (including all future finite intersections), not a uniform physical margin. Ordinary R282 strict solver unchanged.

## Executed strict batch
```json
{"hist":{"direct":23291,"alg":14835,"recursive":1338,"surv":36,"visits":39500,"checkedAgainstOld":100},"checks":3492285,"next":[5200,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":500,"rawRows":20450,"hullRows":1973,"pairRows":3718,"hullIntersections":33288,"pairDominanceTests":270072,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":37742,"scanIntersections":0,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":91772,"mergeCompared":0,"mergeSort":7005650,"mergeComparisons":866671,"mergeIntersections":2928070},"partial":false}
```
Cumulative classified 410800/667787; necessary-condition survivors 2800; remaining 256987; next [5200,0]. Each new bank index increasing, in range, positive mask within 79 bits, popcount equals survivor count. No previous prefix reclassified. R275 full elimination compared on first 100 algebra-tested extensions. R276 count self-checks rerun. No wall-clock speed claim. All computational arithmetic exact BigInt.

New bank:
```text
4968:c000000000000000
5124:e00
5125:800
5127:1000
5128:800
5141:600
5142:200
5143:200
5157:c0
5183:80
5185:180
5186:1c0
5187:180
5190:80
5191:c0
5192:c0
5194:c0
5195:c0
5196:10
5198:c0
5199:c0
```

## Reproduction
Use R277 exact reconstruction with R276 count block and R275 six-direction patch, insert R280, R281 and R282 first JavaScript blocks immediately before grow. Increment pairCalls in grow's pair function as R280 specifies. Base raw=grow(empty,R), st=prune(raw). Sixth extension predicate good=!!scanMerge(st,N) (no per-extension dual diagnostic); first 100 R275 full elimination checks remain. Include stats in both returns. start=4700,size=500,ceiling=12000000; retain partial frontier if cutoff. Same R276 text bank order. This reproduces the actual executed batch. Mixed lemma above is a separate author proof, not part of this strict calculation.

## Next
Continue from [5200,0], keeping all earlier banks. Complete six strict pencils then singleton directions. Implement and compare mixed lift on finite rational row systems; integrate actual R275 germ residual and intercept elimination, including equality and singleton projection. K6 remains 1–2. Independent review and Activity association pending.
