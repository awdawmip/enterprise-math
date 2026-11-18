# EC49FJE — Released-key, B=15, six-demand neighborhood: exact 94-prefix theorem

Date: 2026-11-11. Status: **author-side exact finite proof, independent Driver admission pending**.
Source: EC49FGJ frozen A/B witnesses; pinned science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Prior frontier: EC49FJD, PR #1730 at `f8a803ca4ff8257382bcc3bff75e44e1cb4e60e7`.

## Statement and hypotheses

The unchanged BRC model has 24 **distinct labeled** observation demands (windows 2–9), 178,850 exactly enumerated legal nine-state operation words, 94 distinct **complete raw cache keys**, and native signed six-axis ordered microstep prefixes. A/B are different, explicitly stored legal witnesses with 7 complete cache keys and a 94-edge union.

For each profile separately choose **any six** of its 24 labeled witness paths to replace. Retain the other 18 paths, with native prefix union (F(Q)). Restrict to the **released-key** category: at least one of A/B's original seven complete cache keys is not present among those unchanged 18 paths; and exactly 16 original native prefixes are removed, so (|F(Q)|=78). The replacement words may be arbitrary legal words for their six labels and may reallocate the cache keys subject to at most seven distinct complete keys globally.

**Result:** all 1,001 such positions per profile, total **2,002**, have exact minimum total native edge cost **94**. There is no 93-edge legal completion in this category.

## Certificate argument

To improve the known 94-edge witness to at most 93, a completion must introduce at most (B=93-|F|=15) previously absent **ordered, signed native prefixes**. A/B's original six selected paths provide exactly 16 new prefixes, giving the upper bound 94 for *every* fixed background.

For each candidate (Q), let (K_F) be the complete raw cache keys of the unchanged 18 words, and (R=K_0\setminus K_F) the released old keys. Test the **necessary** exact key-cover property on the 94 legal full keys. If forbidding any individual (r\in R) makes the six labels uncoverable using (K_F) and at most (|R|) further keys, all of (R) are mandatory. Hence all replacements then use the same original seven full keys. This applies to **969 per profile**. An exact six-label trie/Steiner DP of *all legal words on those seven keys*, with zero cost for (F)'s existing edges, gives minimum incremental cost **16** for each of the 1,938 cases.

The 32 nonforced cases per profile split disjointly:

| Certificate class | A | B | Exact rejection of cost <=15 |
|---|---:|---:|---|
| H8 four signatures plus one H9 signature | 26 | 26 | unrestricted-key five-label native prefix DP: minimum **16** |
| H6 or H7 four signatures plus H9 pair | 2 | 2 | unrestricted-key six-label native prefix DP: minimum **16** |
| H6 one + H7 same signature + H8 four | 4 | 4 | six-label **joint key/prefix** DP: minimum **16** |
| **Nonforced subtotal** | **32** | **32** | — |

The first two nonforced certificates deliberately ignore the seven-key restriction. That relaxation can only *decrease* minimum cost; its exact 16-edge lower bound is thus sufficient.

For each of the last eight cases, (K_F) contains exactly **six** complete keys. Therefore at most one other full key may occur. A key outside (K_F) that supports no label with an individual path of at most 15 new prefixes cannot participate in a 93-edge solution; screening the complete 94-key catalog leaves **41** candidate new keys for each case. For each of these (8\times41=328) combinations, retain only legal paths using (K_F\cup\{k\}), and run the exact six-label signed-native trie DP. The minimum over 41 complete optimizations equals **16** in every case; no candidate has cost <=15. The discarded keys cannot occur in a <=15-edge union. The case of no new key is included in each optimization.

For a fixed full-key allowance, the trie DP uses a mask (S) of unmet labeled demands and a cost (d_v(S)) for a subtree at signed prefix (v); combining branches distributes (S) into submasks and charges the incoming native edge once if and only if it is absent from (F). This is an exact finite computation, not a greedy rule or a quotient of endpoint coordinates. All 178,850 words, six-axis sign/order, label identity and full raw key identities are retained.

## Executed arithmetic and reproducibility

All scientific computations are finite integer, Boolean support and native signed-word prefix operations in the frozen BRC generator: no classical trigonometry, floating physical approximation, or conversion to endpoint-only coordinates. An independently programmed Python five-label trie solver cross-checked a representative H8/H9 case with optimum 16, and C++ exact DPs checked the complete classification.

Executed report: forced 969+969, H8/H9 26+26, other unrestricted 2+2, joint cache-key search 4+4. Precisely 2,002 checked and **0** counterexamples to the stated local theorem. The 41-key screen is exhaustive **for the B=15 objective**, not a claim that only 41 full keys exist. The 6-label unrestricted DP returns 13–14 for some of the eight key-sensitive cases: such lower bounds **do not** prove 93-edge feasibility, which is why the full-key DP is necessary.

All native-input procedures and the previously independently revalidated EC49FIO six-label DP are sourced from the preceding EC49FJD/EC49FIO reproducibility directories. The complete actually executed program files, per-case CSV outputs, all key-option results, original witness, logs and SHA256 evidence manifest are preserved in the EC49FJE evidence archive in the originating conversation. The checked result summary and core exact-DP implementations are stored beside this note; regeneration requires the cited frozen witness and generator, not a new science pin.

## Scope and next discriminating question

This is a **finite neighborhood theorem for two specific existing constructions**, neither a proof that global (C_{\min}(7)=94) nor a claim that 93-edge witnesses are absent outside the six-word neighborhood. Do not silently upgrade author computation to independent mathematical admission.

Next: complete released-key six-word backgrounds at (B=17), then the other remaining budgets, while also testing constructive nonlocal moves that can bypass local minima. Any shorter witness must be returned as its 24 raw operation words, full keys, and exact signed-prefix union certificate.