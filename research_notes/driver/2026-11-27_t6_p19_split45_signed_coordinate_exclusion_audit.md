# T6 p19 high splits: final independent exact signed-coordinate exclusion (4,5)

2026-11-27, EM-DVR-DEBB5E. Nonblind independent alternative execution relative to original author EM-T6SM-B134BD and earlier contributor EM-T6-BFF294; common frozen input, not new authorship of original proof. Frozen RR-C428294CF760BD8D99AA retains partial/nonterminal status and original DR-0D8591E64A4073A61E6A. No P000 change, global T6 threshold proof or formal admission.

## Exact input and computation
6cdc7b061d6579d6993f2fbc30d396d9a5c29047:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/input.json, verified blob e2f33462b95e1f0fc4ccc5a38f3bb922a4ade388. Reuse prior exact kernel saturation, full atom carrier, affine representative and weighted triangular projector verification. For orders (4,5), combined residual budget <=4662-361*9-36=1377; checked all 18 exact inequalities 1377*(high_i-low_i)<D_i. Signed interval reversal is exhaustive with at most one choice per coordinate. Use the first-coordinate modular prefilter proved and executed in the (5,5) audit 186057cdc4fd939b886e2d2fdf5a6622f43d7336. Enumerate all 8124 order-four and 8506 order-five roster states (nondecreasing multiset indices, original composite atom carrier, both individual budgets), then all disjoint-support pairs, without j<k restriction for unequal orders.

Actual count 45287075, zero surviving necessary signed intervals. Rejection histogram: [39751284,4882185,576518,66259,9190,1333,244,54,7,0,1,0,0,0,0,0,0,0]. All reject before complete candidate recovery, matching original count and exclusion.

## Complete six-split audit ledger
- (3,6) 335374; (5,6) 1513179; (6,6) 20265: 5b0b3c43f941ce04f80d46754acaacf31e7a8fd1:research_notes/driver/2026-11-27_t6_p19_three_split_signed_coordinate_exclusion_audit.md.
- (4,6) 1724674: 474ed57da2ab20570f518e3b9637f9056569a887:research_notes/driver/2026-11-27_t6_p19_split46_signed_coordinate_exclusion_audit.md.
- (5,5) 21405127: 186057cdc4fd939b886e2d2fdf5a6622f43d7336:research_notes/driver/2026-11-27_t6_p19_split55_signed_coordinate_exclusion_audit.md.
- (4,5) 45287075: this note.

Total 70285694 canonical pairs, zero surviving completions across these six high splits. Earlier independent domain-count audit 3681aebc47928779663e2373ee3e9295ea77f1d0 preserved. Actual new execution this round 68416876 pairs across (4,6),(5,5),(4,5). This covers exactly the six designated p19 high splits, not all remaining layers, global observer matches, parent objectives or formal Result acceptance.

## Reproduce
Use the previous (5,5) exact modular prefilter and base audit(raw) from 5b0b3c43f941ce04f80d46754acaacf31e7a8fd1. Generate separate roster states for [4,5]; check counts 8124/8506; set split [[4,5,45287075]]; loop j over state[4], k from 0 over state[5]. Precompute lo,hi,L,H,width exactly as (5,5); same residue test then reverse integer coordinate loop. Check 1377 bound and full kernel/representative checks from original base. This records actual alternative algorithm execution and inherited input verification, not a blind replication.
