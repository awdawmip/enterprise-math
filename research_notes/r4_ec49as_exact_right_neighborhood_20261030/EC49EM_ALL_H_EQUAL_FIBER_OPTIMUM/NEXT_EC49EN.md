# EC49EN — Joint native-prefix / BRC-factor / terminal-observer cache Pareto problem

**Predecessor:** EC49EM, this Draft PR branch, retaining EC49EL's frozen scientific source pins and all P000/ACTIVE constraints.

**Established facts:** In the native seven-operation terminal A/B nine-history model, for H>=5 and equality of the complete positive count *within each horizon*, the minimum primitive-prefix cost is exactly 4H+30. The attaining schedule uses the mandatory h=2 words ce,de,ec,ed and, for each h>=3, F_h=feg f^(h-3), G_h=gef f^(h-3). Its per-h full positive count is (h,1,1,0,0,0), so distinct BRC monomials can be cached by that vector. EC49EJ establishes that different h can sometimes share one p.

**Specific next research question:** Find the exact Pareto frontier of (T(H), M(H), O(H)), where T is the signed-native distinct prefix-edge count, M is the number of distinct *symbolic* complete six-axis positive-count monomials needed across all horizons, and O is the number of distinct terminal transfer signatures needed for labelled observation recovery. All three metrics are to be counted from the same concrete word sets. Start with H=3,4,5 under the same frozen model and enumerate exactly. Determine whether minimizing M above the native-optimal T=4H+30 is possible without changing the full observer rank, and provide an exact construction or obstruction.

**Suggested first lemma:** At h=2 the sole full-rank fiber has p=(3,1,1,0,0,0); per EC49EJ this p can support exactly h=2 and h=3, not h>=4. Analyze whether globally identical p across *all* horizons h=2..H is infeasible for H>=4, and solve H=3 exactly. Do not conflate mathematical monomial identity with accidental numerical equality at special positive weights.

**Evidence requirement:** Genuine signed-X6 paths, proof of return, exact positive-count vectors in both strictly positive BRC channels, rank-9 terminal observation columns, prefix trie cost, complete finite coverage where claiming optimality, and separate native/monomial/observer cost accounting. Preserve task's exact scientific pins. No automatic Source task admission, Driver review or P000 modification.

**What is no longer open:** A 65-or-less prefix-edge witness at H=9 is impossible in the declared per-h equal-positive-count model; EC49EM gives the exact all-H>=5 theorem.
