# EC49FOX — Four complete original-BRC legal-root classes and exact sparse observers

**Author-side science status:** `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.  
**Frozen science pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.  
**Original input:** SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; 94 keys, 178,850 byte-labeled words, 38,169 seven-key cache configurations.  
**Prior frontier:** [EC49FOW PR #2442](https://github.com/awdawmip/enterprise-math/pull/2442) at `f8ee43220dee5061e068cb89943cf51c9ca29b18`. Existing original-corpus nonzero cross-root gauges of EC49FOR and EC49FOT remain valid.

## Finite theorem: four full legal-domain equivalence classifications

Roots are named `03,05,06,07`; demand labels are `0..23`. The legal-root domain vector `D(K)` for a configuration `K` is computed from the union of the seven selected source keys' named label/root appearances. For `D`, write `C_D={K:D(K)=D}`. `P(K)` is the integer vector of all reachable root-subset costs, with uniquely required labels included. `T(K)` is the vector of total costs for all complete legal root allocations of optional labels, using the same native byte-prefix Trie DP cost operator as the frozen original research.

**FOX-1.** For the four original complete classes identified by first configuration numbers `14300, 14304, 14309, 14313`:

```text
for every K,K' in C_D:
    T(K) = T(K')  iff  P(K) = P(K')
```

| Complete class representative | Configurations | Root coordinates/configuration | Complete legal assignments/configuration | Number of P/T classes | Equal unordered pairs under each observer | Nonzero terminal-invisible P changes |
|---:|---:|---:|---:|---:|---:|---:|
| 14300 | 75 | 164 | 432 | 29 | 1,036 | 0 |
| 14304 | 75 | 160 | 432 | 40 | 596 | 0 |
| 14309 | 75 | 160 | 432 | 40 | 596 | 0 |
| 14313 | 75 | 164 | 432 | 29 | 1,036 | 0 |
| **Total** | **300** | — | — | — | **3,264** | **0** |

**Proof/certificate coverage.** Independently reconstruct all 625 legal-root vectors from the frozen 38,169 configurations; each of the selected classes has exactly 75 configurations. For every selected configuration and root enumerate all subsets of multiply eligible labels (mandatory labels always included) and compute the native Trie minimum prefix cost. There are 48,600 exact root-subset costs. Enumerate all 432 legal assignments for every configuration and sum the four pertinent rooted costs, yielding 129,600 exact terminal integer totals. Partition each complete class by its full `P` and `T` vectors; compare the partitions over every one of the 11,100 unordered within-class pairs. The two partitions coincide in all four classes. The implication `P(K)=P(K') => T(K)=T(K')` is direct; the reverse in these four *finite* classes follows from exhaustive equivalence comparison.

## Sparse observer mathematics

For a class `C_D`, let `m_D` be the minimum number of **fixed** complete root assignments whose terminal cost values distinguish all different rooted cost profiles realized in the class.

**FOX-2: exact optimum 2.** Both `m_14300=m_14313=2`. In zero-based lexicographic order of the Cartesian product of optional demand roots, the sufficient observation indices are:
- Class `14300`: indices `0,329`. Optional labels `[7,11,13,15,17,19,21]`; assigned roots `[06,05,06,03,03,03,03]` and `[07,07,06,03,03,05,07]`.
- Class `14313`: indices `0,277`. Optional labels `[5,11,13,15,17,19,21]`; assigned roots `[05,05,06,03,03,03,03]` and `[07,05,07,03,03,07,06]`.

Both selected two-column cost vectors separate all 29 different rooted profiles; exact enumeration of every original single assignment confirms no one assignment separates them all. This proves equality, rather than only an upper bound.

**FOX-3: exact lower and upper bounds.** For representatives `14304` and `14309` there are 40 rooted profiles, each with 432 legal terminal assignments and 425 distinct masks of still-indistinguishable profile pairs. Every selection of at most three masks has a nonempty intersection (exhaustive enumeration of all `C(425,3)=12,704,100` distinct triples); explicit sets of five observations separate every profile. Consequently `4 <= m_14304 <= 5` and `4 <= m_14309 <= 5`; exact optimality at four versus five is open. The five assignment indices are `[78,99,226,2,63]` and `[119,153,237,6,135]`, respectively; complete label/root tuples are in the machine certificate.

**Exact mask lemma.** Number unordered pairs of distinct rooted profiles. To each terminal assignment associate the bitset of profile pairs that remain equal under that assignment. A family separates all profiles iff the bitwise intersection of its bitsets is zero. This is a direct pairwise equivalence and needs no probabilistic assumption.

## Reproducibility

The full standalone evidence archive contains the original frozen input, four exact 75-member ID lists, all four rooted CSVs, C++17 original native Trie generator, self-contained independent Python Trie verifier, exact sparse observer bitmask verifier, results JSON, explicit witness assignments, run logs and SHA256SUMS. C++17 `-O2` and `-O3` recomputations are byte-identical for all four complete CSVs. The independent Python byte-Trie recalculates **1,296** named root-subset costs for eight boundary configurations, all agreeing with C++ output. The paired cost-group classifier independently tests every terminal allocation.

The scopes are original finite BRC cache configurations and their declared terminal/root observers. This is not a universal theorem about all cache systems, a native six-axis reduction, or a formal Working Truth/Result/Review.

**Continuation:** 547 of 625 classes were complete through EC49FOW; this increment adds four disjoint, previously unclassified size-75 classes, bringing the supported total to **551/625**, with **74** original classes remaining. Next: seek nonconstant high-order cross-root gauge witnesses in the remaining large legal domains; independently decide whether the five-observer certificates for `14304` and `14309` admit four.

**Control observation:** `RS-EC49AS` was checked by original request `r4-ec49fox-current-task-20261115-0432`, with final `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` at control Source `ff7e95ab9f8687a53a00199e814065b5a2c37300`, observed 2026-11-14T20:33:49Z. No formal Task, CLAIM, new Result or independent review is inferred. Independent portable research retains the prior verified scientific pin.
