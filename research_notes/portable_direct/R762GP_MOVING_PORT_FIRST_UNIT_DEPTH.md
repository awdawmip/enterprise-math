# R762GP — First unit common-depth return and asymptotic depth efficiency in the moving-Port STAR candidate

Research date: 2026-11-20, Asia/Shanghai. Exact published Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen taskbook: \`enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8\`. Frozen scientific P000: \`enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This is an author-side portable continuation of R762GM/GN/GO (latest \`PR #2833@671524861024cd6ce5550649eb7a46905dff5157\`). Prior researcher lineage: \`EM-X6-3050F6\`; no claim of a currently authorized native execution session. Independent review: **NOT_REVIEWED**.

## Exact candidate semantics

Use the six K4 edge axes \`E=(01,02,03,12,13,23)\` in the native signed X6 Cell chart. For vertex v in {0,1,2,3}, let \`S_v\` be its three incident edge axes, \`H_v\` their indicator vector, and \`g_v\` the specified 3-cycle of those axes. The candidate affine dynamics are in \`Z^6 ⋊ A6\`, with \`(x,p)(y,q)=(x+p·y,pq)\`. The event \`T(v,s)=(s H_v,g_v^s)\` has sign \`s=±1\` and is admitted at state \`(x,p)\` iff \`v\` is one of the two endpoints of the currently transported named Port \`p(01)\`. Initial state is \`(0,id)\`, and registered initial Port remains \`01\`. Four signed source branches are admitted at each step. A STAR event is an **ordered composite of three original signed native-axis steps**, never a seventh primitive direction. Time/order and source-word multiplicity are retained as separate BRC data.

Define \`D=(1,1,1,1,1,1)\`; \`C_m(k)\` counts ordered, gate-admitted length-m signed source words whose *complete affine* product is exactly \`(kD,id)\`. Define \`L(k)=min{m:C_m(k)>0}\` for nonzero integer k (and \`L(0)=0\`).

## Theorem 1 — sharp first unit-depth joint return

\`L(+1)=L(-1)=16\` and \`C_16(+1)=C_16(-1)=1\`.

More precisely, the full nonzero complete-diagonal return count table for even m≤16 is:

| m | k ↦ C_m(k), for nonzero counts only |
|---:|---|
| 2 | 0:4 |
| 4 | 0:28 |
| 6 | 0:224 |
| 8 | 0:1,884 |
| 10 | 0:16,256 |
| 12 | -6:8, 0:142,616, 6:8 |
| 14 | -6:324, 0:1,267,096, 6:324 |
| 16 | -6:7,936, -4:1, -1:1, 0:11,376,408, 1:1, 4:1, 6:7,936 |

In particular, depth ±4 also first appears at length 16, once per sign. The original R762GM 12-event ±6 histogram is reproduced.

### Proof and exact counting certificate

For any admitted event, the sum of the six Cell coordinates increases by \`3s\`, even after the current axis permutation, so \`(kD,id)\` requires \`sum s=2k\`. Therefore \`m\` is even and \`m≥2|k|\`. In particular all odd horizons are excluded.

Let \`F_n(x,p)\` be the number of legal n-step prefixes from \`(0,id)\` to \`(x,p)\`. Let \`B_n(x,p)\` be the number of legal n-step suffixes from \`(x,p)\` to \`(0,id)\`. Both follow the directed candidate gate, and both count source-word multiplicity. Reverse edges are generated only by reversing an **admitted** forward edge. Because the gate depends on p but not on the Cell translation x, the reverse count to \`(kD,id)\` from \`(x,p)\` is \`B_n(x-kD,p)\`. Hence the exact half-path convolution identity is

\`C_{2n}(k)=Σ_{(x,p)} F_n(x,p) B_n(x-kD,p).\`

The supplied checker enumerates all 360 even permutations of the six edge axes, constructs all four admitted signed forward branches at each orientation, and their complete reverse predecessor lists. It propagates exact nonnegative integer multiplicities for n=0..8, then performs the indicated half-path convolution for every k with |k|≤n. The complete state has all six signed Cell coordinates and all 360 orientation possibilities. The state codec uses radix 65 with a digit offset 25; every half-path coordinate has absolute value at most 8, each translated target adds at most 8, so no carry or alias is possible. This is exhaustive for all m≤16; counting suffixes backward requires their variable in-degrees, which the checker retains.

For an independent algorithmic cross-check, the full, one-sided forward recurrence (without half splitting) was also executed for all m≤12 and gives identical endpoint histograms. Explicit, separately replayed signed witness paths establish the two unit returns.

Unique +D word (vertex,sign) in temporal order:

\`(0,+),(2,+),(0,+),(2,-),(2,-),(1,-),(3,-),(1,-),(2,+),(0,+),(1,+),(3,+),(0,+),(1,+),(2,-),(1,-)\`.

Its Port edges before each event are

\`01,02,02,12,12,12,13,13,02,02,13,03,03,01,12,12\`.

Unique -D word:

\`(1,-),(3,-),(1,-),(3,+),(3,+),(0,+),(2,+),(0,+),(3,-),(1,-),(0,-),(2,-),(1,-),(0,-),(3,+),(0,+)\`.

Its Port edges before each event are

\`01,13,13,03,03,03,02,02,13,13,02,12,12,01,03,03\`.

Both pass every evolving Port gate and end at \`(±D,id)\`. The eight-step half-path maps have exactly one meeting full state for each sign, each with prefix and suffix multiplicity one; hence the signed source word is unique at m=16. Together with the absence of unit-depth return at 2,4,...,14 and odd-horizon exclusion this proves the sharp minimum. QED.

## Theorem 2 — full integer depth reachability and sharp asymptotic cost

Every integer diagonal depth is reachable as a complete affine return in this **candidate** model. For k≠0,

\`2|k| ≤ L(k) ≤ 2|k|+26.\`

For every integer a≠0, \`L(6a)=12|a|=2|6a|\`, and therefore

\`lim_{|k|→∞} L(k)/|k|=2.\`

### Proof

At the end of a complete return the orientation is id, so the Port is reset to \`01\`. Since permission is translation-invariant, concatenating complete-return source words adds depths and event lengths. Theorem 1 supplies complete loops for ±1 and ±4 at length 16; R762GM and the table above supply ±6 at length 12. Thus every integer depth is reachable by concatenating unit loops.

For positive k, write \`k=6q+r\` with q≥0 and r∈{0,1,2,3,4,5}. Concatenate q positive depth-6 loops (length 12q), followed by the following legal residue constructions:

| r | composite loop | additional events | extra over 2r |
|---:|---|---:|---:|
| 0 | empty | 0 | 0 |
| 1 | +1 | 16 | 14 |
| 2 | +6, -4 | 28 | 24 |
| 3 | +4, -1 | 32 | 26 |
| 4 | +4 | 16 | 8 |
| 5 | +6, -1 | 28 | 18 |

Thus \`L(k)≤12q+2r+26=2k+26\`. Negative k follows by the established -1, -4, -6 loops and the same construction for |k|. The lower bound follows from the six-coordinate sum. At k=6a, |a| sign-pure 12-event loops attain this lower bound exactly. The two-sided bound yields the limit. QED.

## Verification, observer scope, and open target

- Author-side standard-library integer script: \`R762GP_CHECK.py\`, PASS; full n=0..8 forward/reverse exact half-paths, all complete-diagonal endpoint counts through m=16; separately replayed ±D legal words. A larger local checker \`R762GP_VERIFY.py\` also ran successfully with a direct full recurrence to m=12 and explicit single-meeting checks, supplying the machine-readable evidence \`R762GP_EVIDENCE.json\`. No Lean or independent mathematical review: \`NOT_REVIEWED\`.
- This is a **constructed signed STAR moving-Port candidate**. The P000 primitive triadic-force constraint, PERP_E=120°, full X6 Cell torsor, typed time, branch provenance and original task science remain unchanged. This calculation does not establish that \`TRIADIC_CLOSURE_E\` licenses this Port-update law or that the probabilities measure physical force dynamics.
- New discriminator: derive the actual native Cell/Port/Link signed event permission, and test whether its Port-update functor supports the two explicit 16-event words or forbids a particular first step. If it preserves them, test the observer-safe lifting of complete state and provenance; if not, recompute the permitted language without collapsing to the candidate's positive-weight terminal observer. A separate open question is the exact minimum \`L(k)\` for every nonmultiple-of-six k.
- Storage is portable scientific material; there is no new protected Source PROGRESS, Result, independent Review, current CLAIM or P000 promotion claim.
