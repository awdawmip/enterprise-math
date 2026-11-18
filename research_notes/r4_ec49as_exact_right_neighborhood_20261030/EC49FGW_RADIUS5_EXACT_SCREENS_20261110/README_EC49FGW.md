# EC49FGW — 七缓存键BRC 93边目标：半径五的精确必要条件筛选

Date: 2026-11-10. Status: exact finite **author-computed screening**; neither a radius-five completeness result nor a Driver-reviewed mathematical Result. Original frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact statement

The input consists of EC49FGJ baseline profiles A and B (24 original labeled nine-state BRC words, seven complete raw cache keys, 94 distinct nonempty ordered signed native X6 microstep prefixes). The canonical path witnesses are in `EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json`, immutable blob `e65c1598ad9fa2680558046ed1e59d83806536b8`. A local archival copy has different JSON formatting/metadata, but the 24 triples `(window,signature,word)` of each profile match the canonical witness.

For each witness, choose exactly five of its 24 labeled words and replace them with arbitrary words that satisfy the same labels, the original nine-state automaton and signed six-axis endpoint `(2,0,0,0,0,0)`. The resulting 24 words may use at most seven complete raw cache keys. We seek total native-prefix cost <=93.

The following **disjoint exhaustive partition of five-label positions** is proved computationally by exact integer enumeration; it is identical for profiles A and B:

| Necessary-condition class | A | B |
|---|---:|---:|
| Fixed 19 other words already occupy >=94 native prefixes | 8,568 | 8,568 |
| Some changed label has no individually budget-feasible word, even with unlimited keys | 16,760 | 16,760 |
| Each changed label individually fits, but all eligible raw cache keys fail the seven-key joint-cover bound | 1,120 | 1,120 |
| Not excluded by these screens; five-word joint prefix cost unresolved | **16,056** | **16,056** |
| **All five-label choices = C(24,5)** | **42,504** | **42,504** |

The key-cover exclusions split into exactly 704 cases requiring >=1 new key with 0 slots available, 384 requiring >=2 with 1 slot, and 32 requiring >=3 with 2 slots, per profile. Thus **26,448 / 42,504** radius-five positions around either original witness are excluded by sound necessary conditions. This is a new exact local reduction. A seven-key 93-edge witness remains an open possibility outside these exclusions. The already verified global seven-key bound remains `C_min(7)<=94`.

## Proof and complete original input domain

Let `P_i` denote the set of *all nonempty ordered signed six-axis microstep prefixes* of baseline word `i`, and `Q` be a chosen five-label set. Define `F(Q)=union_{i not in Q} P_i` and `B(Q)=93-|F(Q)|`.

The necessary baseline test is `B(Q)>=0`. This is exact, because unchanged words retain all their native signed prefix identities. EC49FGS's support-hypergraph identity gives `|F(Q)|=94-sum_e [S(e) subset Q]`. The 8,568 five-label choices wholly among H2-H7 leave H8/H9 unchanged; those six words already cover 94 native prefixes.

The frozen legal operator alphabet is `acdefg`, with nine-state transition table, sink 8, terminal signature observer and signed native X6 operation expansions specified in `EC49FGV_RADIUS4_COMPLETE_20261110/model_ec49fgv.py`. All six axes and signed step order are retained.

A legal length-`h` word with raw cache key `K=(x,y,z)` must have exact operator multiplicities
`a=z-1; c+d=x+y-h-1; e=z; f=h+1-y-2z; g=h+1-x`, each nonnegative. Enumerate `c=0..c+d` and all original nine-state-legal operation orders to attain the specified terminal observer signature. The full catalog has **178,850 legal labeled words over 94 complete keys**, across the original 24 labels.

For each demand label `l`, raw key `k` and fixed background `F`, let

`m(l,k,F) = min_{w legal for l, key(w)=k} |P(w) \\ F|`.

Because `F` is prefix-closed and each `P(w)` forms a chain of nonempty signed native microstep prefixes, for a word of native length `L(w)`:

`|P(w) \\ F| = L(w) - max( { |p|: p in P(w) intersect F } union {0} )`.

Consequently `m(l,k,F)` is computed *exactly* as the minimum over the empty prefix, and over the available `p in F`, of `L(w)-|p|` over all legal `(l,k)` words extending `p`. Indexing the minimum complete-word length per `(prefix,label,key)` gives this cost by pure integer comparisons. A target <=93 requires `m(l,k,F)<=B(Q)` for every changed label and at least one eligible key; failure for one label safely excludes Q **without imposing a key count bound**.

For the still surviving cases let `R(Q)` be the keys already used by the fixed 19 words and let
`O_l(Q)={k:m(l,k,F(Q))<=B(Q)}`. Every feasible completion must choose one raw key from each `O_l` while maintaining
`|R(Q) union {chosen keys}|<=7`.
Represent five required labels as a five-bit mask. Keys in `R(Q)` cover the labels for which they are eligible; every other key covers the subset of labels for which it appears in `O_l`. A minimum-cover DP over the 32 masks counts the **exact minimum number of additional distinct keys**, independent of word order. If it exceeds `7-|R(Q)|`, Q is impossible. Passing this cover bound is only a necessary condition; combined native-prefix unions are the remaining work.

All reported partitions are thus finite exhaustive **position screens**, not a declaration of five-word feasibility. No unsigned/endpoint-only path quotient, floating-point tolerance or unverified pruning step enters the exclusion logic.

## Reproducible evidence and validation

Executed locally (Python standard library, full exact arithmetic):
```sh
python EC49FGW_RADIUS5_SCREEN.py
python EC49FGW_KEY_SCREEN.py
python CROSSCHECK_EC49FGW.py
```
Run receipts from actual local execution: `EC49FGW_EXACT_PASS`, `EC49FGW_KEY_SCREEN_PASS`, `EC49FGW_DIRECT_CROSSCHECK_PASS`. The independent crosscheck re-evaluated 24 fixed deterministic A/B cases with *direct full legal-word signed-prefix-set subtraction*, recovering all indexed per-key minima exactly. Local evidence includes full scripts, all 85,008 five-label cases represented by reports, 24 crosschecks, logs, frozen baseline triple data, SHA256 manifest and a compressed evidence archive.

## Next exact question

For each profile, **16,056** radius-five position choices remain after the two sound screens. First compute exact feasible *pair* delta-prefix union lower bounds, prioritizing those survivors whose unchanged background fixes all seven raw keys. For released-key cases retain the five-bit key-cover DP while considering actual pair-key assignments. Then search the true five-way signed-prefix union, retaining the original seven-key budget. An exhaustive exclusion would prove the *two local radius-five neighborhoods* cost >=94, but **not** global seven-key optimality. A concrete <=93 word assignment would be a new constructive upper bound.

Current control provenance: main Source P000 V5, current continuation protocol and research method; previous exact EC49FGJ, EC49FGS and EC49FGV notes. Historical EC49AS currently lacks current immutable publication under the native control query; this author record has no formal CLAIM, Result, independent Driver admission or P000/worldview change.
