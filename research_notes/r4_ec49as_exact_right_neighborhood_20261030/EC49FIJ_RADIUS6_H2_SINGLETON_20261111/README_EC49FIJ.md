# EC49FIJ — Radius-six forced-H2 lift and exact singleton screen (2026-11-11)

## Frozen problem and prior scientific frontier

Frozen science pin: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.
The nine-state causal BRC observer, ordered signed-native-X6 microsteps, 24 observation labels, raw complete cache-key identity, and known seven-key 94-prefix witnesses A and B are exactly those of EC49FGW/EC49FHH/EC49FHI. This is a finite theorem on the neighborhoods of these **two** witnesses.

The prior EC49FHH verified computation established: changing at most five actual witness paths, while keeping no more than seven complete raw keys, cannot beat 94 distinct nonempty native prefixes. The new screen reuses that precise proposition.

## New reduction: forced H2 paths lift a five-path theorem to six nominated positions

The exhaustive 178,850-word legal catalog contains exactly one legal word for each of the two H2 labels \`(2,16)\` and \`(2,32)\` (and the witness uses those words). If a six-position replacement set \`Q\` contains either H2 position, its replacement word is forced to be identical to the original. Thus at most five actual paths differ, so the earlier radius-five lower bound applies **even when six positions were nominated and cache keys may be released**. This covers \`C(24,6)-C(22,6)=59,983\` positions per witness. Of those, 10,556 were already excluded by the fixed-94-prefix bound, leaving 49,427 newly excluded positions.

## New exact singleton lower bound

For all other positions, let \`F(Q)\` be the union of the 18 unchanged words' nonempty signed-native prefixes; its exact cost is \`|F|\`. To reach at most 93, new words must contribute at most \`B=93-|F|\` additional distinct prefixes.

For a label j and allowed complete-key set K, define

\`m_j(F,K) = min_{w legal for j, key(w) in K} |P(w) \ F|\`.

Because F is prefix-closed, \`P(w) ∩ F\` is the initial segment of \`P(w)\` through its deepest shared prefix, hence

\`m_j(F,K)=min_w (L(w) - max({|p|: p in P(w) ∩ F} ∪ {0}))\`.

The script computes this minimum exactly by indexing baseline prefixes p, their exact 24-bit support masks, and the minimum legal extension lengths by label. When the 18 unchanged words already occupy all seven raw keys, \`K\` is exactly those seven keys. If an old key was released, the script relaxes K to **all** complete keys in the 178,850-word legal catalog (so a singleton impossibility remains valid with key redistribution).

If any selected label has \`m_j(F,K)>B\`, no six-path completion with total cost at most 93 exists. This is a sound necessary-condition screen; surviving cases require joint-prefix and key-budget optimization.

## Exhaustive results (each of A and B independently)

| Disjoint class | Position count |
| --- | ---: |
| Unchanged 18 words already cost 94 | 18,564 |
| H2-lift from proven radius-five result, excluding overlap | 49,427 |
| Full-seven-key cases rejected by exact singleton bound | 22,548 |
| Released-key cases rejected by unrestricted-key singleton bound | 2,072 |
| **Total excluded so far** | **92,611** |
| Seven-key fixed survivors | 39,973 |
| Key-release survivors | 2,012 |
| **Still open** | **41,985** |
| Total \`C(24,6)\` | 134,596 |

Additional exclusions beyond EC49FHI's first 18,564 trivial exclusions are 74,047 per witness, or 148,094 position instances across A and B.

## Reproduction and source scope

At this unchanged frozen ancestor of PR #1730, run from the new directory:

\`\`\`bash
python VERIFY_EC49FIJ.py
\`\`\`

The script imports \`../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py\`, reads the frozen witness JSON located alongside that module, exhaustively enumerates all 134,596 six-position sets per witness, saves \`EXACT_REPORT_EC49FIJ.json\`, and asserts every exact class count. Local execution returned \`EC49FIJ_EXACT_PASS\` and generated the full budget histogram. A source copy and the summary are committed here for exact reproduction; local script/report content hashes are in the summary.

## Next discriminating research unit

Apply two-demand pairwise exact prefix-union lower bounds to the 39,973 fixed-key survivors, then six-terminal native-prefix trie DP on the strongest residual families. For the 2,012 key-release survivors use key-set branch-and-bound and unrestricted pairwise necessary conditions first. Keep key identity as complete (x,y,z) occupancy; preserve native path order, signs, branch identity and the P000-defined X6 substrate. The global seven-key minimum remains open beyond these two witness neighborhoods.

**Research status:** author-verified finite classification and proof reduction; formal Result and independent Driver review remain governed by current Source authority. \`EC49FHH\` is a pinned scientific dependency for the lifted slice.