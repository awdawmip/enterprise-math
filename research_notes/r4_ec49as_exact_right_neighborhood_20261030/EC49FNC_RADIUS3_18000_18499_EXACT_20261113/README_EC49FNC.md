# EC49FNC — Exact BRC seven-cache-key radius-three cases 18000–18499 and a root-functional dominance certificate

Date: 2026-11-13. Scientific inputs remain frozen to `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is author-side continuation of [EC49FNB PR #2226](https://github.com/awdawmip/enterprise-math/pull/2226), without repinning its nine-state BRC model, 178850 legal original operation words, 94 complete cache keys, 24 observation labels, or 38169 seven-key radius-three cases. The cost is the cardinality of distinct **nonempty ordered signed native X6 microstep prefixes** of legal words selected to cover the labels.

## Exact finite computation

The original cached C++ prefix-trie and label-subset integer optimizer was compiled with `g++ -std=c++17 -O3 -DNDEBUG`. Its original frozen integer input has SHA-256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. A complete contiguous prefix of **500 outputs, IDs 18000–18499**, was retained from an interrupted larger run. Their raw output SHA-256 is `INVALID_PLACEHOLDER`. Exactly 500 line IDs were checked for continuity; only completed outputs are counted.

The minimum is **98**, attained precisely at IDs **18111, 18123 and 18383**; maximum **204**, attained precisely at ID **18196**; there are **81** distinct attained costs. The globally contiguous computed portion of this 38169-case search therefore extends to **18500/38169 (48.47%)**. The best observed cost among these 18500 cases remains **96**, first attained at 17965; the separate unrestricted seven-key problem continues to have its prior 84-prefix constructive upper bound.

For each of 18111, 18123 and 18383, 24 frozen legal operation words were reconstructed, one for each observation label. The distinct nonempty ordered signed X6 prefixes are **49+49=98** over first-microstep roots `05` and `06`; root `07` is unused in these witnesses. The independent Python prefix-tree/subset implementation recalculated **18111→98, 18123→98, 18383→98, 18499→131**, in agreement with the C++ exact optimizer. Independent calculations were performed for the four stated IDs, not all 500.

## Root-functional dominance: a stronger, reusable finite claim

Define `F_{K,r}(S)` as the minimum number of nonempty prefix nodes in root `r` needed to cover the exact requested subset `S` of eligible observation labels, using frozen original words allowed by key set `K`; `F(empty)=0`. Each root function is calculated exactly by bottom-up trie dynamic programming over label masks, followed by superset closure.

**Dominance lemma.** For two key configurations `A,B` with the same root and eligible-label domains, if `F_{A,r}(S) <= F_{B,r}(S)` for every root `r` and subset `S`, then the globally optimal cost of `A` is no greater than that of `B` for **every requested label subset**. Proof: take an optimal admissible root assignment for B; use that same partition for A. Pointwise inequalities bound the summed cost, and minimizing over A assignments cannot increase it.

**Verified instance:** `A=17965` has keys `[0,4,5,6,11,14,26]`; `B=18383` has keys `[0,4,5,7,11,14,26]`. Only complete key **6 versus 7** differs. The exact root functions have identical eligible-label domains: roots `05` and `06` each have 12 labels (4096 masks), and `07` has 8 labels (256 masks). Checking all **8448** root-mask pairs gives `F_A <= F_B` in every case, strict in **1608** masks at root 05, **1872** at root 06 and **54** at root 07 (3534 strict cases total). The full-demand minima are `F_{A,05}=48,F_{A,06}=48` and `F_{B,05}=49,F_{B,06}=49`, with root 07 not needed. Thus `C(A)=96 < C(B)=98`. This exact finite certificate proves a replacement improvement for every demand subset and extends beyond comparing a single optimal witness.

**Non-equivalence at equal full-demand cost:** `18111=[0,4,5,6,11,32,49]` and `18123=[0,4,5,6,11,34,49]` both achieve 98, but their root subset functions cross in both directions. Comparing `F_{18111}-F_{18123}` gives per-root counts `old-better/equal/new-better`: root 05 `1672/804/1620`, root 06 `1672/804/1620`, root 07 `105/63/88`. Equal optimum therefore does not imply functional equivalence of the underlying BRC prefix observers.

## Proof of each fixed-configuration optimum

Within one leading signed native microstep, form the trie of every allowable original operation word and label its endpoints. Bottom-up DP stores the minimum retained-node count for each exact coverage mask; combining child masks costs the sum, and a nonempty retained child charges its first node. Superset closure yields `F_r(S)`. Exhaustively distribute all 24 requested labels among eligible roots and minimize the summed root functions. Every lawful selected-word solution induces such a partition, giving a lower bound; each DP realization gives lawful selected words and matching upper bound. The emitted 24-word witnesses independently confirm their stated attainable prefix counts. All arithmetic is exact finite integer combinatorics on frozen typed BRC words, without a classical numerical surrogate.

## Reproduction, source identity, and next frontier

The full local evidence package records the frozen generator, original 9.3-MB input, compiled solver source, raw 500-line output, three complete legal 24-word certificates, an independently implemented Python exact verifier, root-function comparison script, all four root-function tables, execution logs and SHA-256 manifest. The compact companion `EXACT_CERTIFICATE_EC49FNC.json` carries losslessly encoded 500 costs, root functions and witnesses; the verifier checks compression hashes, full vector continuity/minima and exact finite root dominance. Run the included scientific programs against the exact frozen input to regenerate the data and check legality/optimality.

**Next continuous search index is 18500**, with 19669 radius-three configurations remaining. A separate useful direction is to derive symbolic sufficient conditions for key substitutions to induce pointwise domination of the root subset functions, rather than enumerate individual configurations.

**Authority:** This is a committed author-side scientific result, not a formal Source CLAIM, Result or independent Driver acceptance. The exact `RS-EC49AS` query request [#6905](https://github.com/awdawmip/kimi-query-bridge/issues/6905) was last observed `QUEUED`; no winning owner assertion is made. Preserve the frozen task pin and live owner boundary before later formal intake.
