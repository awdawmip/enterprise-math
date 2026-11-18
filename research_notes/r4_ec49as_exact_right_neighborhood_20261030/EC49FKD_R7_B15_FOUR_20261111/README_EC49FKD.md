# EC49FKD — 2,835 new exact four-label obstructions for radius-seven B15 retained-key backgrounds (2026-11-11)

**Scope:** exact finite signed-native-X6 BRC, frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, A/B seven raw-key 94-prefix witnesses, seven replaced operation words and seventeen original fixed operation words. **Review:** author calculation, independent Driver not yet performed.

Earlier EC49FKB and EC49FKC proved 3524 and 801 disjoint B15 retained-key local cases; this study addresses further backgrounds requiring four omitted observation labels.

For the retained-key seven-position subset Q, define fixed literal signed-prefix union F(Q). Here `|F(Q)|=78`; achieving 93 original prefixes would require at most 15 distinct newly introduced prefixes. Since the seventeen fixed operation words already use all seven complete raw keys, each replacement path must use one of those exact keys.

There are exactly 67 fixed-prefix background classes for each A/B witness, and 4336 labeled seven-subsets per profile. Previous two-/three-demand certificates account for one large class plus 5(A)/8(B) classes. This study enumerates four-label subsets within the remaining 119 profile-specific backgrounds: 1075 proposed four-label cases, of which the C++17 exact native-prefix trie evaluates 821 (stops processing the later proposals of a class as soon as a sound obstruction is found). It finds a four-label obstruction in **47 classes A** and **44 classes B**. Their distinct seven-position weighted counts are **1515 in A and 1320 in B**, **2835 new 94-prefix local optima**.

Each exact trie edge represents one signed ordered six-axis microstep, with cost zero precisely when its full literal prefix belongs to the original fixed set F and cost one otherwise. Every terminal has the exact mask of demanded observation labels attained by legal words using the original seven keys. For a node v, the DP stores the minimal number of newly paid edge prefixes sufficient to cover each subset S of 4 labels within its descendant terminal masks. Child unions use disjoint label partitions, pay each child edge exactly once and saturate integer costs at 16. For each of the 91 certified backgrounds the root full-four-label value is exactly **16 (the clipped lower bound)**. Thus no 15-prefix completion can supply even these four labels. The unchanged original witness supplies a legal 16-new-prefix completion, proving exact 94 total optimum for all Q in the class.

The saved `EC49FKD_FOUR_RESULTS.tsv` lists all 91 certificates, with profile, canonical 1-based group index, labeled-context multiplicity, four missing observation labels, clipped exact minimum and trie-node count. `EC49FKD_FOUR_TRIE.cpp` is the actual executed C++ algorithm. Regenerate its two inputs with `python EC49FKD_MAKE_CATALOG.py` (178850 legal words, raw complete keys) and `python EC49FKD_MAKE_FOUR_CASES.py` (1075 deterministic candidates). Both scripts import the frozen generator/witness under adjacent `EC49FJD_RELEASE_B11_COMPLETE_20261111/`; the latter also consumes `../EC49FKC_R7_B15_TRIPLE_20261111/EXACT_TRIPLE_CERTS_EC49FKC.json`. Then:

```sh
g++ -O3 -std=c++17 -o ec49fkd EC49FKD_FOUR_TRIE.cpp
./ec49fkd FJR_CATALOG.tsv EC49FKD_FOUR_CASES.tsv regenerated.tsv
cmp regenerated.tsv EC49FKD_FOUR_RESULTS.tsv
python EC49FKD_PY_CROSSCHECK.py
```

The source generator and input source bytes were reused from PR #1730 without repinning science. The actually generated 1075-line input has SHA256 `749edf3b76c52b9b61aaabdc5c5fa8ba7fb61d9a3d7eac9e796470f43fea4db9`; 178850-row catalog SHA256 `b4e7bcc88306fa846f752f1ca1e6b31957e9ac65080d80a0c7506447004dc489`; resulting 91-line certificate list SHA256 `cc2a3e04979e2caa4f35e1bafe0bd2b1fc1b1c526dd59a656053825f1cacb562`. A second direct Python prefix-set/antichain checker independently verified five representative background classes of sizes 10, 54 and 65 across A/B; it returned `EC49FKD_PY_5_DISTINCT_CLASSES_PASS`. C++17 rerun regenerated exact identical TSV bytes.

**Continuation:** 14 classes per profile (54 seven-position contexts each) survive all two-, three- and four-label obstructions. Their five common missing labels form the next exactly specified subproblem EC49FKE, preserving the original key and frozen input semantics. EC49FKE is published in this PR as a separate additional result. Original mother objective `C_min(7) ?= 94` remains global.
