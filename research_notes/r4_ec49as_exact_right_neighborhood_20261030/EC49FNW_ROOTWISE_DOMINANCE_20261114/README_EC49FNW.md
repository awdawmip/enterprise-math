# EC49FNW — Rootwise one-sided dominance on native BRC cache-key swaps

**2026-11-14 · Exact frozen input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status **NOT_REVIEWED**. Independent author-side mathematical lemma and finite exact census; no formal CLAIM, Result or accepted theorem is asserted.

## Prior exact frontier and new question

This continues EC49FNV [PR #2331](https://github.com/awdawmip/enterprise-math/pull/2331), which transferred the exact two-layer cutoff certificate in both directions of 84 key swaps by checking 16,876 source cut nodes, performing bounded repairs of 18 failed target-cut tests, and handling four domain-changing directions. EC49FNS [PR #2318](https://github.com/awdawmip/enterprise-math/pull/2318) found 30 full-root-profile-equivalent edges. Neither result answers how many additional swaps admit a **single a priori rootwise domination certificate without target evaluation at each cut node**.

Use the original seven-key corpus, 94 complete cache keys, 178,850 legal native ordered-signed words, 24 labelled demands, roots 03/05/06/07, and the 84 first-neutral edges among 32000–32999. Original input SHA256:
- `master_and_radius3_cases.txt`: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- `FIRST_NEUTRAL_EDGES_EC49FNS.txt`: `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`
- `EXACT_NATIVE_32000_32999.txt`: `c9314021942397a0b5a3e7a90d965fb19a853bdc486f7610721fc748a057c0f9`.

## Theorem — one-sided root-profile domination transfers an entire pruned frontier

For cache configuration K and root r, let E_{K,r} be the set of labels eligible at r, and let D_{K,r}(S) be the exact minimal nonempty native rooted-prefix cover cost of S, permitting extra covered labels. All queried S are subsets of E_{K,r}. Define

`Delta_r(K→K') = max(0, max_{S ⊆ E_{K,r} ∩ E_{K',r}} (D_{K,r}(S)-D_{K',r}(S)))`,
`Delta(K→K') = Σ_r Delta_r(K→K')`.

Consider a lawful source cutoff traversal at threshold B, whose first-pruned partial assignments p satisfy `LB_K(p) = Σ_r D_{K,r}(S_r(p)) > B`. If p is also lawful for K', all its root subsets lie in the common domains, so

`LB_{K'}(p) ≥ LB_K(p) - Delta(K→K')`.

**Proof:** Apply the defining one-sided maximum independently to each root subset `S_r(p)`, sum the four inequalities, and use monotonicity of each target rooted cost under further demand assignment. If `m_* = min_p(LB_K(p)-B)` among target-lawful source cuts, then `m_*>Delta` certifies every such source cut subtree is target-above-cutoff simultaneously. Target-illegal source cuts have no target-lawful descendants. This is a general finite exact lemma, not a complexity bound.

**Domination corollary.** When `Delta=0`, every source cut remains valid, independently of the source cut margins; no target cost is needed for those cut nodes. If no target-only eligibility pairs exist, and each original source low leaf is still target-lawful with identical exact cost, then the complete target low-layer allocation identity/cost map equals the source map. Consequently, if B contains the two distinct lowest cost layers, the target has the same (C,m,g). For domain expansion, target-only choices still require separate exclusion; domination alone does not settle them.

## Complete frozen 84-edge classification

Exact native-root subset DP on the original frozen words gives:

| Condition | Undirected edges | Directed transfers |
|---|---:|---:|
| Both orientations have `Delta=0` | 30 | 60 |
| Exactly one orientation has `Delta=0` | 43 | 43 |
| Neither orientation has `Delta=0` | 11 | 0 |
| **Total** | **84** | **103 domination directions** |

These 103 directed dominance certificates include **43 additional unilateral dominance edges** that do not have globally identical root profiles. All 103 have no target-only root choices, unchanged costs on their 317 source low leaves, and 10,429 first-pruned source cut nodes, each of which is certified safe by the single `Delta=0` inequality. The remaining 65 directions require stronger predicates; the previous EC49FNV full transfer verifier already certifies all 168. Two expansions (`32315→32279`, `32318→32279`) have target-only root-03 choices for labels 11 and 13 and are not covered by the corollary alone.

Representative strict one-way edge: `32315→32274` has `Delta=7`; the reverse `32274→32315` has `Delta=0`. Representative bidirectionally incomparable edge: `32318↔32274`, with `Delta=7` and `3`. The **entire 84-edge paired directed Delta certificate** is in `EC49FNW_ALL_84_EDGE_DELTAS.txt`. In all 168 source cut frontiers, the minimum source pruning margin happens to be 1, so this all-subset envelope alone passes precisely the 103 zero-Delta directions; it does not pretend to explain the 65 others.

## Verification and limits

1. Extract the previous full EC49FNV or EC49FNT original evidence archive; check its frozen SHA256 manifest.
2. Compile and execute the included complete C++17 verifier (`VERIFY_EC49FNW.cpp` in the accompanying full local artifact), which reuses FNV's native ordered-signed word trie DP and adds `root_delta` over every subset of the four roots' common eligible labels. The compact source extension is also in `ROOT_DOMINANCE_EXTENSION.cpp.txt`; it describes the exact insertion into the immutable original FNU verifier, whose source is available in [PR #2330](https://github.com/awdawmip/enterprise-math/pull/2330). The local complete verifier's SHA256 is `69262c99dba1e175f57d4b9e59def3c3184da7d7d27a6e7fffde456e71c8f758`.
3. Each `ENVELOPE` output gives source/target IDs, domination flag, source min margin, Delta, rootwise deltas, target-lawful cut count, baseline target failing cuts and target-only eligibility count. The 168 `TRANSFER` rows agree byte-for-byte with a separately compiled execution of the unmodified FNU source; this checks the original baseline behavior was preserved.
4. All original FNV source manifest items passed SHA256 verification, including the exact word corpus. The full local output `FNW_RESULTS.txt` SHA256 is `c5be84fe8e47b0f487ceaf9cebc5bc6c67cc7d54b36cabd4d0e7beeac89946a2`. The source output is reproducible from the pinned original corpus, not from a recomputed optimization of 1,000 configurations.

**Boundary:** the lemma is general for exact rooted subset cost systems. The numbers 30/43/11 and 103/168 refer only to the fixed 84-edge finite family. Computing all root-subset tables has a cost; no universal speedup or mathematical acceptance is claimed. The next question is a tighter, root-coupled envelope that certifies the 65 non-dominated directed cases, especially the 11 edges incomparable in both directions, without per-cut target root evaluation.

Evidence package as supplied with this run: `EC49FNW_ROOTWISE_DOMINANCE_EVIDENCE_20261114.tar.xz` SHA256 `e9f7c4e4a0daf0472c876ddb64ccd74e629fad9e6dfeb4a25fb834603e0d09d1`. GitHub files and this report are independent scientific materials; no formal RS-EC49AS Task authority or Result is inferred from publication.
