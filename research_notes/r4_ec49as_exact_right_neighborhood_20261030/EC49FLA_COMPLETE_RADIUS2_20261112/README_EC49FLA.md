# EC49FLA — complete two-cache-key replacement neighborhood of the 84-prefix seven-key BRC witness

Date: 2026-11-12. Research mode: author-side exact finite computation, independent Driver review pending.

## Precise result

Use the **unchanged frozen** nine-state BRC catalogue and ordered signed-X6 native microsteps pinned by `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`: 178,850 allowed words, 94 distinct full three-coordinate cache keys, and 24 observation labels. For a seven-key set K, let W_d(K) be its catalogue words realizing demand d. Each word w gives the set P(w) of its nonempty *literal ordered signed native microstep prefixes*. Define

`C(K) = min_{w_d in W_d(K), one for every d} |union_d P(w_d)|`,

and `C(K)=infinity` if one or more labels have no allowed word.

The EC49FKX witness has keys
`K0={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`
and verified cost `C(K0)=84`. The original EC49FKY one-key replacement classification proved `C(K)>=84` for all one-key replacements of K0, with some equal to 84.

Here every **exact two-key** replacement has been classified. There are
`binom(7,2)*binom(87,2)=78,561` distinct target key sets. Exactly **72,246** fail key-level demand coverage; exactly **6,315** cover all 24 labels. For the 6,315 coverable sets, complete exact trie subset-DP yields:

- `min C(K)=84`, **uniquely attained at feasible index 5883**;
- `C(K)<=83` for **zero** of the 6,315 sets;
- the complete cost range is **84..204**;
- exactly two sets attain 86 (indices 2473 and 4515).
  
The unique index-5883 replacement is
`drop={(5,4,1),(6,4,1)}`, `add={(6,3,1),(7,3,1)}`.
It gives the new distinct 84-prefix key set
`{(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(6,3,1),(7,3,1)}`.

**Finite neighborhood theorem.** Let `N_2(K0)` be exactly the seven-key sets whose symmetric key-difference from K0 has cardinality at most 4. Then
`min_{K in N_2(K0)} C(K) = 84`.
This is the complete radius-2 key-replacement optimum of the frozen native model. The unrestricted seven-key question remains `C_min(7) <= 84`, with global equality open.

## Exhaustiveness and exact cost argument

First, compute each full-key demand support mask `L(k)` by a complete generator of the fixed catalogue, preserving the full signed words and their DFA signatures. For any dropped two-key subset D of K0 and added two-key subset A outside K0, a feasible completion requires
`union_{k in (K0\D) union A} L(k) = all_24_labels`.
All 21 x 3741 replacements are enumerated in deterministic Python tuple lexicographic order. Earlier EC49FKZ independently checked all 21 per-drop coverage counts via grouped support-mask frequencies.

For each of the 6,315 feasible K, the unchanged original signed-X6 exact C++ program builds a prefix trie of **every** allowed word with full key in K. Partition the words by the literal first signed microstep: distinct root tries have disjoint nonempty prefixes. At a trie node v, the bottom-up state for a demand mask S records the minimum selected prefix nodes in its subtree needed to cover S. Merge children by disjoint subtree cost addition and OR of covered demand masks. If any demand is served under v, charge one for the prefix at v. Terminal labels may already cover a demand without descending. The subset superset-min transform allows extra terminal observations to remain covered without extra charge. Finally, assign each of the 24 demand labels to an eligible root trie and minimize the sum of root costs. Every chosen word induces a feasible state with the same number of distinct prefixes, and every nonempty terminal selection induces actual allowed words whose union has no larger cost. Hence the DP optimum equals C(K); it does not merely estimate a lower bound.

The previously published unchanged `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` is the exact solver. The previously published `EC49FKZ_DOUBLE_KEY_COVER_20261112_R4/EC49FKZ_EXHAUSTIVE_RADIUS2.py` generates the deterministic coverable index order and full input words. To avoid long solver batches, this round split the remaining work into smaller batches without changing the scientific input or solver semantics. Results 0..399 came from the verified EC49FKZ original; this round ran indices **400..6314**. The merged 6,315-row result was checked for exact contiguous indices, no conflicting repeats, all 21 original coverability group counts, the complete 178,850-word source catalogue and all 94 raw keys.

An independently structured Python trie/subset-DP from EC49FKY cross-checked new cases **2473→86**, **4515→86**, **5541→204**, **5883→84**, including the unique minimum. The checker itself reconstructs full native signed prefixes from words.

## Full finite certificate and re-execution

The adjacent `EC49FLA_COST_VECTOR_6315.xz.b64` stores **all 6,315 exact minima**, one unsigned byte per feasible index in the deterministic original EC49FKZ order, compressed with LZMA/XZ and base64-encoded (1,300 compressed bytes). Decode with Python standard libraries `base64.b64decode` and `lzma.decompress`; demand that the raw vector length is 6,315.

- Raw cost-vector SHA256: `7a94b5b408a73e4be11405c238273e0313b829c0d0ddd4793028609b1851f248`.
- Compressed XZ SHA256: `f5a83e6fb6877f57e33aded9c4c864dcfc66450f184eb15488b063825bc59868`.
- Original consolidated full 6,315-line result SHA256: `06782c2c56ad3e3b7ae2e5aa9ad2e39fc8f5e4cb163f0917d39fbbe0a77e2c94` (included in author-side complete evidence package).

Regenerate any feasible index from the published EC49FKZ generator; solve that exact key set with published signed-prefix C++ and compare the cost at its position in the vector. The complete 6,315-index scan is independently reproducible from these pinned inputs and exact solver.

This is author-side exhaustive finite evidence, not an accepted Driver review or formal task Result. Native researcher issuance returned `SESSION_ISSUANCE_QUOTA`; a contemporaneous attempted formal task read returned `NO_CURRENT_IMMUTABLE_PUBLICATION`. No CLAIM, Result or authenticated activity checkpoint is asserted.

## Next research unit

Examine three-key replacements of K0 and one-key replacements of the new index-5883 84-prefix key set. Use the existing key-support cover screen before native-prefix exact optimization, looking first for a legal 83-prefix witness. Preserve this complete 0/1/2-swap classification unchanged and compare any new construction by the same full signed prefix definition.
