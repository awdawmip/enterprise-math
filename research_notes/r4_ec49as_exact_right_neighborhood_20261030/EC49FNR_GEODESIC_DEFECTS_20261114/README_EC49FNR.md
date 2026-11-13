# EC49FNR — Exact geodesic obstructions in the frozen native-BRC seven-key plateau graph

Date: 2026-11-14. **Author-side finite proof, NOT_REVIEWED**. Continuation of EC49FNQ PR #2306, with unchanged scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is exact postprocessing of immutable EC49FNP native optimizer rows; it does not repeat their optimization. Formal Task/CLAIM/Result and review remain separate.

## Finite theorem

Let `S` be the 1,000 complete seven-key configurations indexed `32000..32999`. Each has a complete cache-key set `K_i` and its previously optimized signed native-prefix triple `v_i=(C_i,m_i,g_i)`, where `C` is optimal cost, `m` the number of optimal admissible root-demand assignments and `g` the gap to the next *distinct* assignment cost. Fix the native nine-state lawful-word grammar, 94 complete cache keys, 24 demands and the ordered signed microstep-prefix observer from the frozen input.

A *stable edge* swaps exactly one whole cache key and preserves all three quantities. The induced stable-graph distance is `d_s(i,j)`, infinity for disconnected pairs. The universal seven-subset Johnson lower bound is `r(i,j)=|K_i\\K_j|`.

**Exhaustive result for every unordered pair of distinct sampled vertices with equal `v`:**

| Johnson distance r | Stable distance d_s | Number of pairs |
|---:|---:|---:|
| 1 | 1 | 11,574 |
| 2 | 2 | 4,814 |
| 2 | 3 | **4** |
| 2 | disconnected | 140 |
| 3 | 3 | 162 |
| 3 | 4 | **4** |
| 3 | disconnected | 1,911 |

There are exactly **18,609** same-signature pairs. Of their **16,558** connected pairs, **16,550** have a shortest stable path of exactly `r` moves. Exactly **eight** require `r+1` moves, and **none** requires greater excess in this finite graph. The other **2,051** equal-signature pairs are in different stable components.

## All eight sharp detour certificates

| Pair | Signature | r -> d_s | Verified shortest stable route |
|---|---|---|---|
| 32275–32703 | (144,1,1) | 2 -> 3 | 32275 → 32288 → 32689 → 32703 |
| 32276–32719 | (152,1,1) | 2 -> 3 | 32276 → 32290 → 32691 → 32719 |
| 32315–32353 | (154,1,1) | 2 -> 3 | 32315 → 32264 → 32272 → 32353 |
| 32318–32353 | (154,1,1) | 2 -> 3 | 32318 → 32264 → 32272 → 32353 |
| 32703–32951 | (144,1,1) | 3 -> 4 | 32703 → 32689 → 32288 → 32275 → 32951 |
| 32703–32953 | (144,1,1) | 3 -> 4 | 32703 → 32689 → 32288 → 32275 → 32953 |
| 32719–32961 | (152,1,1) | 3 -> 4 | 32719 → 32691 → 32290 → 32276 → 32961 |
| 32719–32963 | (152,1,1) | 3 -> 4 | 32719 → 32691 → 32290 → 32276 → 32963 |

## Structural lemma and finite verification

**Complete-geodesic lemma.** Any path of one-key swaps from equal-sized key sets `A` to `B` has length at least `r=|A\\B|`. A path of exactly `r` swaps must, at each step, delete one as-yet-unremoved key from `A\\B` and insert one as-yet-uninserted key from `B\\A`. Conversely, every ordered pairing of these `r` removals and insertions gives a length-`r` path. A stable geodesic exists in the sampled graph *iff* at least one of at most `(r!)²` such schedules has all intermediate seven-key sets inside `S` with the same triple.

**Proof.** One swap removes at most one of the original `r` incorrect keys; reaching `B` in `r` swaps forces exactly one distinct removal and one distinct required insertion per step, without temporary keys. Conversely, these exchanges reach `B`. Requiring every intermediate key set to occur in the sample with the same triple characterizes stable geodesics. QED.

The executable `VERIFY_EC49FNR.py` retains the original EC49FNQ complete vector SHA check, graph comparisons, six-key-inverted-bucket crosscheck, component/BFS audit and direct path witnesses. Its EC49FNR extension enumerates BFS shortest distances for **all 18,609 same-signature pairs** and *independently* tests every ordered removal/insertion permutation for each pair. It asserts the complete seven-cell count table, every exceptional endpoint pair and explicit `r+1` stable route. Thus the finite obstruction count is a proof by justified exhaustive integer/set enumeration, with concrete counterexamples.

## Reproduction, provenance and scope

Run `python3 VERIFY_EC49FNR.py` with its sibling `EDGE_VECTOR_EC49FNP.u8x11.xz.b64`. The immutable source of those bytes is [EC49FNP@98cd8ce](https://github.com/awdawmip/enterprise-math/blob/98cd8ce66ba27609359d9182e94376f0e81a1600/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FNP_EDGE_SPECTRUM_32000_32999_20261113/EDGE_VECTOR_EC49FNP.u8x11.xz.b64); the copied file has the same Git blob SHA1 `1f2aaa3be3a37b49c7f5d0b0424dd70192bc3b4e`. Its decoded 11,000-byte SHA256 is `4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b`.

This is a finite **induced-subgraph** theorem for exactly the sampled 1,000 configurations. Paths may exist through configurations outside that sample in the full 38,169-case family. It establishes no new primitive BRC arithmetic or universal root-function perturbation law. The original native optimization and lawful-word evidence remain in the EC49FNN archive; they were not recomputed.

**Next question:** detect the eight non-geodesic pairs from local root-function differences and allowable intermediate-key schedules, using a certificate cheaper than full native reoptimization. This would distinguish intrinsic signature-preserving swaps from detours caused by the selected sample.

No secrets or changes to shared access privileges are included.