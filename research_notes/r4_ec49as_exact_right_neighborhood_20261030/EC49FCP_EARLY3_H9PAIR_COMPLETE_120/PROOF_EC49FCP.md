# EC49FCP — exact early-three plus H9-pair five-path rigidity

**Author-side finite exact theorem (2026-11-06).** Science input frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Exact frozen model: research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FCN_EARLY3_H7PAIR_COMPLETE_720/frozen_model.py, Git blob c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b. The 24 original slots, H2/H3 roots, nine-state DFA, ordered signed primitive steps, and BRC keys L=(4,2,1), M=(7,3,2) are retained.

## Theorem
For every three-element subset of the ten H4–H6 observation slots and both H9 observation slots, fix the remaining 19 original words. Replace each of the five selected words by any legal word preserving its original window, BRC-key multiset and exact nine-state observation signature. The minimum number of distinct nonempty **ordered signed primitive-step prefixes** of all 24 paths is exactly **158** for all C(10,3)×C(2,2)=120 groups.

## Exhaustive proof
For selected slots S, let F be the union of frozen 19 words' prefix sets and let R_k(w) be the candidate prefix set minus F. The cost is |F|+|∪R_k(w)|. The original chosen words always attain 158. Put cap=158-|F|. A strict improvement is possible precisely when the five residual sets have union size below cap.

The frozen candidates(h) function completely enumerates permutations of the required key multiset accepted by the nine-state transition table with the target signature. The direct checker forms all distinct unions of residual candidates for the selected three H4–H6 slots with cardinality below cap, then checks the two H9 residual sets. It discards partial unions only after their cardinality reaches cap. Union cardinality is monotone under later additions, so these removals and deduplication preserve every strictly improving five-tuple. No group has such a tuple, and the original witness attains 158.

An independently represented exact literal signed-prefix frozenset implementation checks all 120 groups. The actually executed combined program also crosschecks the bitset and literal representations for all groups. Exact integer and set operations are used, with no floating-point inference.

| Exact finite measurement | Result |
| --- | ---: |
| Five-slot groups verified | 120 / 120 |
| Minimum in each group | 158 |
| Improving groups | 0 |
| Unpruned Cartesian tuple count (sum over groups) | 2,231,276,544,000 |
| Executed final-stage bitset unions | 81,432 |
| Maximum early-three residual unions retained | 34 |
| Frozen prefix size range | 143–149 |
| Full literal crosschecks | 120 / 120 |

The unpruned count is a cardinality, not an executed iteration count. Direct report SHA-256: 295af3f217c1d4b183b709523438881fd7a56e71e0fcf3a84ae4162aa3f7ba10. Literal report SHA-256: 5dad8e29b7df3a02fec1944dc65997f7d9ff8824d433bb45cc6b719370928c54. Actually executed combined checker SHA-256: b05893802a57ca3c11e1aa055812fafff005c547c4a219e74b3d35f9ac578059; its executed output SHA-256: aa0d4d77896cfa0a4c89f9a018339e8fbc837d0c8e7ca96f0937b3d9cae570cb.

Full per-group direct and literal JSON outputs are losslessly stored as gzip+base64 text files in this directory. To recover: base64 -d FILE.gz.b64 | gzip -dc > FILE.json; verify the declared SHA-256. To re-run, put the immutable frozen_model.py from EC49FCN alongside VERIFY_EC49FCP_COMBINED.py, then execute python VERIFY_EC49FCP_COMBINED.py. It uses both bitsets and literal ordered signed prefixes and writes EC49FCP_COMBINED_RESULT.json.

## Frontier
After EC49FCH–EC49FCP, the author-side five-path finite verification covers 7,752 distinct groups under this fixed-key model. Next: explore early-two + late-three selections, higher-order coordination and alternate legal BRC key assignments. The nine-window 93-edge mother question remains open. Classification: AUTHOR_FINITE_EXHAUSTIVE_PROOF / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Native CLAIM/Result and independent Driver approval require separate current Source authorization.
