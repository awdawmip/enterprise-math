# EC49FOG — Exact three-factor decomposition of native BRC cutoff-DFS neighbor workload

**Date:** 2026-11-14. **Research status:** author-proved finite algorithmic claim; exact native C++17 O2/O3 and independently reconstructed Python trie-DP; **NOT_REVIEWED**.

## Frozen source, reuse, and question

Preserve frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input is the original 94-key, 178,850 ordered signed-prefix words and 38,169 seven-key cache sets, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Reuse EC49FOF PR #2375, signed-prefix DP and native DFS procedure; do not recompute the original 1,000 full optimal solutions. All costs and counts are exact integers.

The one-key exchange cache `A=32279` (key 45) -> `B=32315` (key 81) preserves complete optimal tuple `(154,1,155)` but changes B=155 native cutoff DFS visited nodes from 436 to 173. EC49FOF found simultaneous root-eligibility, root-cover-cost and DFS-label-priority changes. What exact amount of the observed *algorithmic workload change* is attributable to each controlled intervention?

## Model and theorem

Roots are the named 03,05,06,07, demands are labels 0..23. Let `D^A_r(S)` and `D^B_r(S)` be the exact rooted signed-prefix cover cost on the two frozen seven-key caches, including all original eligible domains. For vector `x=(x03,x05,x06,x07)` in `{0,1}^4`, construct the **mixed rooted-table test system** `D^x_r=D^{A}_r` if `x_r=0`, otherwise `D^{B}_r`. Root assignment eligibility comes from the selected table's actual label set. This defines a valid combinatorial test even when the mixture is not an actual original seven-key cache. Fix one of the exact label permutations `O_A` or `O_B` computed by native DFS priority: increasing eligible-root count, decreasing minimum singleton cover cost, then increasing label.

For each `(x,o)` run DFS with roots in order 03,05,06,07, process the next label in order `O_o`, and prune a visited node when `sum_r D^x_r(S_r)>155`. Count **all recursion entries**, including cut entries and leaves. The resulting function `N(x,o)` is an exact finite observer of the original rooted-cover model, conditioned on the chosen order. Both original endpoints are `N(0000,A)=436` and `N(1111,B)=173`.

**Exact finite trace result:** For all 32 mixtures/order combinations, toggling root05 or root06 leaves the complete *ordered labelled DFS-visit trace and cut flags* unchanged. Hence N factors through only three binary factors: root03 table, root07 table, and priority order. This is a trace equivalence for this specific finite input, threshold and two orders, not equality of underlying rooted cost functions.

The exhaustive eight distinct visit-count results are:

| root03 from B | root07 from B | order A count | order B count |
|---:|---:|---:|---:|
| 0 | 0 | 436 | 397 |
| 1 | 0 | 259 | 206 |
| 0 | 1 | 418 | 361 |
| 1 | 1 | 245 | 173 |

For example, with fixed A priority, changing only root03 reduces 436 -> 259; changing only root07 reduces 436 -> 418; changing both gives 245. With the B root03 and root07 functions fixed, changing only priority gives 245 -> 173. Joint effects are nonadditive: `(245-436)-[(259-436)+(418-436)]=+4` visits on A priority.

**Exact permutation-averaged allocation:** Define `v(S)=N` after interventions in `S` of the three factors `{root03,root07,priority}`. Shapley weights for subsets `S` not containing factor i are `|S|!(2-|S|)!/3!`. Direct rational substitution of all eight counts yields:

- root03 table: `-547/3` visited nodes,
- root07 table: `-76/3` visited nodes,
- DFS order: `-166/3` visited nodes.

The sum is exactly `-263`, the measured 436 -> 173 change. These are explicitly defined *order-averaged intervention contributions* in the finite mixed-table model; they do not claim a unique physical cause or an independent wall-clock speedup.

## Why root05/06 trace preservation is nontrivial

Independent rooted-table recalculation found all 24 labels covered in every mixture, but root05's 2,048-entry cost array differs at 308 masks, and root06's 4,096-entry array differs at 3 masks. Thus the claim is a lossless quotient **only for the declared two fixed DFS orderings and threshold-pruning trace observer**. The exact Python checker compared every visited prefix (sequence of root choices) and its cut Boolean for all 32 runs: for each fixed `(root03,root07,order)` the four variants of root05/06 yielded identical full ordered traces. Changing future observer or threshold requires a new certificate.

## Exact complete verification and limits

The evidence bundle contains `VERIFY_EC49FOG_CROSSED_DFS.cpp` which reads all frozen words/caches, rebuilds signed-prefix rooted trie DP with multi-label prefix selection, applies 16 mixed four-root tables under two original orders, and emits `fo_g_results.tsv` (32 records). C++17 `-O2` and `-O3` output compared byte-for-byte equal. `VERIFY_EC49FOG_INDEPENDENT.py` with reused prior independent `VERIFY_EC49FNY_INDEPENDENT.py` reconstructs eight root tables independently from original words, recomputes all 32 DFS runs, checks every count and exact trace invariance of the 05/06 variants. The frozen input SHA256 is checked. Comparison of native root DP arrays identifies the 308 and 3 changed masks.

This is a complete finite algorithm test of these 32 intervention configurations. Original all-cache neutrality from EC49FOF remains sourced there; no general prediction over 38,169 caches is asserted. Root-table hybrid combinations are explanatory mathematical interventions, not necessarily genuine cache swaps.

## Reproduce

Obtain the original `master_and_radius3_cases.txt` from EC49FOF PR #2375's complete evidence bundle (SHA256 above). Decode the committed `EC49FOG_COMPLETE_SCIENCE.tar.xz.b64` with base64 and xz/tar; it contains full proof, source, Python verifier, TSV, SHA256SUMS, and execution logs. Run:
```sh
g++ -std=c++17 -O2 -Wall -Wextra VERIFY_EC49FOG_CROSSED_DFS.cpp -o ec49fog
./ec49fog < master_and_radius3_cases.txt > compare.tsv
cmp compare.tsv fo_g_results.tsv
python VERIFY_EC49FOG_INDEPENDENT.py master_and_radius3_cases.txt fo_g_results.tsv
```

## Remaining question

Find an exact, cheap sufficient certificate predicting when the 05/06 cost changes are invisible to cutoff-DFS, without running all 32 full searches. Extend the intervention comparison to original neutral edges where workload changes, and test whether an interaction-aware root signature can bound workload or maximal actual forcing horizon before full DFS. Retain source eligibility and priority order as separate typed influences.

**Provenance:** EC49FOF PR #2375 and original signed-prefix frozen evidence. Formal Task `RS-EC49AS` previously read as `NO_CANONICAL_PUBLICATION_DIRECTORY`; this independent-source study neither creates a CLAIM nor a formal Result. Research Activity historical contributor `EM-DIRECT-204C14`, historical RA `RA-6893088D0A7347CE7F4D8720`. New Source Activity update requires a genuine permitted write and readback; report the actual status.
