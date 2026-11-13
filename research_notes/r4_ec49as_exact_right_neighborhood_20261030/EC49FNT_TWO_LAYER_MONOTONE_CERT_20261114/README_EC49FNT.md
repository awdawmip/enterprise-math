# EC49FNT — Exact two-layer native-root certificate by monotone pruning

**2026-11-14** · Author exact finite proof and computations · `NOT_REVIEWED`.
Science uses frozen pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This continues [EC49FNS, PR #2318](https://github.com/awdawmip/enterprise-math/pull/2318) and the source files of [EC49FNN, PR #2298](https://github.com/awdawmip/enterprise-math/pull/2298). No original optimization over 1,000 cases was repeated.

## Proposition 1 — monotone partial-assignment cutoff

Let `L={0,...,23}` be the 24 frozen labels and `R={03,05,06,07}` the lawful root microsteps. For a complete seven-key cache configuration `K`, define `D_{K,r}(S)` as the **exact minimum number of nonempty native ordered signed rooted-prefix nodes** covering every label in `S` using lawful words rooted at `r`; extra covered labels are permitted. The root node is counted whenever `S` is nonempty. A lawful assignment `a` sends every label to a root with at least one valid word of that label. Its global root-assignment cost is
`F_K(a)=Σ_r D_{K,r}({l:a(l)=r})`.

For label sets `S⊆T`, `D_{K,r}(S)≤D_{K,r}(T)`: every word selection covering `T` also covers `S`. Therefore, for **any partial assignment** `p`,
`LB_K(p)=Σ_r D_{K,r}({l already assigned to r})`
is a lower bound on every complete extension's `F_K`. Given a fixed integer cutoff `B`, prune precisely when `LB_K(p)>B`. Every omitted complete assignment has cost strictly greater than `B`, and **every** complete assignment of cost at most `B` survives. Thus traversal returns exactly the low-layer identity-and-cost map
`A_K(B)={(a,F_K(a)) : a lawful and F_K(a)≤B}`.
Proof is monotonicity for every descendant and exhaustive branching among remaining lawful roots. No floating-point or heuristic assumption is involved.

## Proposition 2 — two-layer identity-map equivalence

For `K,K'`, even when their permitted root-label domains differ, suppose their **complete** cutoff maps `A_K(B)` and `A_{K'}(B)` are equal, and contain both a minimum `C` and a distinct next cost `S` with `C<S≤B`. Then both configurations have the same first two distinct global costs, the same number `m` of minimizing assignments and the same gap `g=S-C`. Every assignment omitted on either side costs more than `B` by Proposition 1, hence cannot alter either layer. **Full equality of the four rooted DP tables is not required.** This theorem preserves the two cost layers and assignment identities, not all higher costs.

## Frozen 84-edge exact census

Reuse the exact first-neutral swap list of EC49FNS (84 edges in the induced 32000–32999 graph; 51 distinct endpoints), the original EC49FNN corpus of 94 complete keys and 178,850 lawful native words, and the original 11,000-byte packed vector (SHA256 when decompressed `4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b`). For each endpoint, choose `B=S=C+g` from the unchanged original full-exact certificate. Independently compute rooted word-trie DP arrays, enumerate 24-label assignments with monotone lower-bound pruning, verify the original minimum `C`, its multiplicity `m` and next distinct cost `S`, and compare the complete low-layer **identity maps** along all 84 edges.

| Exact result | Count |
|---|---:|
| Selected first-neutral edges | 84 |
| Distinct endpoint vertices | 51 |
| Edges with equal full root tables (prior EC49FNS sufficient condition) | 30 |
| Edges with different root tables | 54 |
| **Edges whose full low-layer identity-and-cost maps coincide** | **84** |
| All allowable complete root assignments over the 51 endpoints, for reference | 34,344 |
| Complete low-layer assignments actually reached by pruning | **159** |
| Partial DFS nodes visited, including pruned nodes | 8,924 |
| Partial nodes pruned because their lower bound exceeds `B` | 5,111 |
| Vertices with exactly three low-layer complete assignments | 45 |
| Vertices with exactly four low-layer complete assignments | 6 |

Among these 51 vertices, 41 have `(C,m,S)=(154,1,155)`, six have `(152,1,153)` and four have `(144,1,145)`. The new certificate therefore applies to **all 54** first-neutral exchanges where the stronger all-root-function-equality test failed. It does not assume matching sets of allowable root allocations in advance.

A separate exhaustive Python spot-check of 648 lawful assignments per configuration proves the high-cost spectrum can actually change despite the low-layer map being fixed:

- `32318→32264`: 55 rooted-subset entries change; eight of the 648 full assignment costs differ, lowest changed cost 164; all three assignments of cost ≤155 agree exactly.
- `32315→32274`: 765 rooted-subset entries change; 238 of 648 full assignment costs differ, lowest changed cost 156; all three assignments of cost ≤155 agree exactly.

These two strict witnesses rule out interpreting low-layer equality as a statement about the entire cost spectrum.

## Reproduction, provenance and verification range

The exact frozen original inputs are available in PR #2298 (file `master_and_radius3_cases.txt` and `EXACT_NATIVE_32000_32999.txt`), and the first-neutral edges and original vector in PR #2318. A complete original-byte evidence archive with these same input files, the newly executed C++ validator, actual 84 EDGE/51 VERTEX output and SHA256 manifest is supplied with the research turn.

C++17 rerun:

```sh
g++ -O2 -std=c++17 VERIFY_EC49FNT.cpp -o verify_fnt
./verify_fnt FIRST_NEUTRAL_EDGES_EC49FNS.txt EXACT_NATIVE_32000_32999.txt < master_and_radius3_cases.txt > EC49FNT_RESULTS.txt
```

The executed stderr summary was
`EC49FNT_DONE edges=84 vertices=51 strong=30 low_equal=84 low_unequal=0 root_cache=168`.
The input native-root DP counts the root prefix, uses ordered signed microsteps and never collapses distinct lawful prefixes to final-coordinate endpoints.

**Scope:** complete finite result for the specified 51 vertices and 84 edges; no universal claim for all possible BRC caches or arbitrary swaps. This is independent author research material; formal Task CLAIM, Result, Driver review and Foundation admission are separate operations. **Next concrete problem:** derive a cross-endpoint sensitivity bound that can transfer the low-layer certificate from one endpoint to the next without recomputing even the second endpoint's pruned 24-label assignment tree.
