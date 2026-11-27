# T6 p19 split (5,5): independent exact signed-coordinate exclusion

2026-11-27; EM-DVR-DEBB5E. Same nonblind Driver audit context, original author EM-T6SM-B134BD and contributor EM-T6-BFF294 retained. Frozen input 6cdc7b061d6579d6993f2fbc30d396d9a5c29047:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/input.json, verified blob e2f33462b95e1f0fc4ccc5a38f3bb922a4ade388. Reuse exact kernel/representative, triangular projector, complete carrier checks in prior audits 5b0b3c43f941ce04f80d46754acaacf31e7a8fd1 and 474ed57da2ab20570f518e3b9637f9056569a887. No change to frozen congruences or model. Both sides nonempty; total residual budget <=1016. All 18 inequalities 1016*(high_i-low_i)<D_i actually rechecked. Exact signed-coordinate inversion has no branching.

## Fast first-coordinate filter
For a roster state s of remaining budget A_s, precompute projected vector v_s and lo_s=A_s*low, hi_s=A_s*high, W_s=hi_s[17]-lo_s[17]. Let L_s=(v_s[17]-lo_s[17]) mod D_17 and H_s=(v_s[17]-hi_s[17]) mod D_17. For opposite disjoint-support states u,v, the residue of (v_u-v_v)-(lo_u-hi_v) is (L_u-H_v) mod D_17. A necessary and sufficient first-coordinate interval condition is that this residue <= W_u+W_v, because the width is strictly less than D_17. The two precomputed residues belong to [0,D_17), so a single conditional addition computes their difference modulo D_17. Surviving pairs proceed through the original exact reverse-coordinate loop including the first coordinate. No approximate arithmetic.

## Actual execution
One order-five roster has 8506 states; enumerate unordered disjoint-support pairs j<k, retaining all integer composite atoms and multiplicity. Actual pair count 21405127, agrees with original. Zero survivors, all rejected before final norm verification. Rejection histogram (reverse order): [19866867,1426036,103680,7778,691,66,9,0,0,0,0,0,0,0,0,0,0,0]. Cumulative 5/6 high splits, 24998619 pairs independently exhausted; remaining (4,5) 45287075 retains original execution and independent coverage count only.

## Reproduce
Use audit(raw) from 5b0b3c43f941ce04f80d46754acaacf31e7a8fd1:research_notes/driver/2026-11-27_t6_p19_three_split_signed_coordinate_exclusion_audit.md with roster [5], assert 8506, split [[5,5,21405127]]. Store lo,hi,L,H,width as defined above for every state; immediately after disjointness and incrementing pairs, run:
```js
let h=u.L-v.H;if(h<0n)h+=D[17];
if(h>u.width+v.width){depth[0]++;continue}
```
Then original BigInt reverse loop; lo=u.lo[i]-v.hi[i], hi=u.hi[i]-v.lo[i], reuse zs only as higher entries overwritten before access in same pair. All previous frozen basis/rep checks remain valid. This is a nonblind mathematical crosscheck, not native acceptance, Result completion or mother closure.
