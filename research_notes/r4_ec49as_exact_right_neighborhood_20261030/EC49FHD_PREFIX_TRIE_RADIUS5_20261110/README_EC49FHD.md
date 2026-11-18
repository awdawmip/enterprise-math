# EC49FHD — Native-prefix trie DP closes five-path non-releasing radius (2026-11-10)

**Frozen scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Scope:** original 9-state BRC observer, native ordered signed X6 microstep prefixes, 24 demands H2–H9, EC49FGJ 7-key/94-prefix witnesses A and B. This is an author-side exact finite result, awaiting independent Driver review.

## Exact theorem: rooted group-cover on a prefix tree

For finite native-step candidate word families `W_1,...,W_k` and a prefix-closed fixed background `F`, build the rooted trie of all candidate native-step prefixes. Give the edge entering prefix `p` weight 0 if `p in F`, and 1 otherwise; mark every complete candidate word as a terminal of its demand group. Then

`min_{w_i in W_i} |(union_i Prefixes(w_i)) minus F|`

equals the minimum edge-weight of a rooted connected subtree meeting every group. Define `d_v(S)` as its minimum cost in the subtree below node `v`, required to meet every group in subset `S`. Each terminal at `v` serves its own group at zero cost. A child state transferred to its parent costs `d_child(S)+edge_cost` when `S` is nonempty; the empty state costs zero. Merge each child's contribution by exact subset min-convolution:

`(d*g)(S)=min_{A subseteq S}(d(S minus A)+g(A))`.

**Proof:** a selection of candidate words determines a rooted trie subtree of precisely the charged prefix edges. Conversely any rooted connected subtree meeting all groups contains a candidate root-to-terminal word for each group; choosing those words cannot increase its cost. A tree decomposes uniquely at every child; the required group labels can be assigned disjointly among the current terminal and children, even if their subtrees cover extra labels. Induction proves the recurrence. The solver uses exact integer arithmetic; complexity `O(|E| 3^k)` and `O(|V| 2^k)` for fixed k, plus trie construction. The ordered, signed six-axis native prefix is the atomic edge; no endpoint-only quotient is used.

## New finite theorem and complete computation

For a five-label set `Q`, keep the other 19 words from witness A or B unchanged. Assume the fixed 19 still use all seven original complete raw cache keys, so all replacement words must use those same seven keys. Let `F(Q)` be the unchanged paths' native-prefix union and `B(Q)=93-|F(Q)|`. The trie DP computes the exact minimum additional prefixes `m(Q)` using **every** admissible word of those seven keys (not a shortlist).

The frozen catalog has **178,850** legal operator words; the original seven-key domain contains **9,838**. For *each* witness, all **62** eligible high-budget positions were checked: `B=21:34; B=22:20; B=23:4; B=25:4`. Every position has `m(Q)=B(Q)+1`, hence exactly **94** total prefix edges. Earlier pairwise screening excluded 14 B=21 positions; the other **48 per witness, 96 newly resolved positions in total**, were unresolved after EC49FHC. The new solver also rechecked independently all **116 B=20 positions per witness** with optimum 94. Prior exact author-side results EC49FGX through EC49FHC cover lower budgets.

**Combined scoped conclusion:** each original witness is a radius-five local minimum of cost 94 under the constraint that the unchanged paths retain all seven original keys. This includes arbitrary simultaneous native-path changes, not merely single-path swaps or operation-prefix-compatible swaps.

## Reproduce and inspect evidence

The three `.gz.b64` artifacts are base64-encoded deterministic-gzip files. Decode with `base64 --decode FILE.gz.b64 | gzip -dc > FILE` (strip `.gz.b64` from the output name). Put `VERIFY_EC49FHD.py` in this directory next to the pre-existing sibling folder `EC49FGW_RADIUS5_EXACT_SCREENS_20261110`, containing `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`. Execute `python VERIFY_EC49FHD.py 21 22 23 25`. The code enumerates the frozen BRC words and exact X6 prefix trie, executes a small independent direct exhaustive crosscheck, and asserts the all-case finite theorem. Expected final line: `SUMMARY [('A', 62, 0), ('B', 62, 0)]`.

Decoded verifier SHA256: `035b6ca404dc090c1da65c1d972bd37d43e225d40d129ccb43b59dc3dd6a2826`; decoded full high-budget report SHA256: `ebbeae4ed6152439cb7e4aebe49c06abc39498b8946d079c23fe854a0aa49328`. The B20 recheck report records the final 22 cases; the remaining 210 were checked in the local execution log, yielding 232/232 exact B20 crosschecks.

## Next problem / boundary

The prior EC49FGW screened frontier still has **4,898** five-label positions per witness which *release* one or more of the original seven cache keys. For those, if the fixed background uses `7-r` distinct keys, new candidate paths may introduce up to `r` distinct keys. Extend the exact trie method by key-union-budget or enumerate feasible new-key subsets. The unrestricted global 7-key optimum remains open, with verified upper bound `C_min(7)<=94`. P000 and the protected worldview remain unchanged. No active EC49AS CLAIM, formal Result, or independent Driver admission is claimed.
