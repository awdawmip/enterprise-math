# EC49FJZ — radius-seven retained-key B=13 exact native-BRC minimum (2026-11-11)

**Status:** author-side exact finite theorem, exhaustive executable literal-word certificates; pending independent Driver review and formal Result. **Scientific frozen pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This continues EC49FJY with no scientific input change.

## Theorem: 17,128 new 94-prefix local optima

Fix either frozen EC49FGJ native BRC witness profile A or B (24 distinct labeled nine-state observation demands, seven complete raw cache keys and 94 distinct ordered signed X6 microstep prefixes). Choose seven labeled positions Q for replacement, retaining the other seventeen original operation words literally. Let F(Q) be their native signed-prefix union. Restrict to Q for which those seventeen paths already use all seven old full key identities, and |F(Q)|=80. Thus a hypothetical 93-prefix completion has at most **B=13** newly introduced native prefixes.

The exact complete subset census gives 346,104 seven-subsets per profile and 153,408 retained-key subsets. Exactly **8,564 per profile** have this B=13 condition, partitioning into **58 distinct fixed-prefix backgrounds per profile**. All **17,128** such fixed-background subproblems have exact minimum 94 prefixes.

| Disjoint finite certificate class | Profile A | Profile B | Combined |
|---|---:|---:|---:|
| Pair of omitted labels obstructs <=13 new prefixes | 274 | 548 | 822 |
| Triple of omitted labels obstructs <=13 | 3,442 | 3,168 | 6,610 |
| Four omitted labels obstruct <=13 | 4,848 | 4,848 | 9,696 |
| **New 94-prefix exact optima** | **8,564** | **8,564** | **17,128** |
| Unresolved within this B13 class | 0 | 0 | 0 |

The 58 native background classes per profile have sizes: 32 classes of 210 positions, 24 of 54 positions, and two of 274 positions (32×210 + 24×54 + 2×274 = 8,564). Every class admits one common obstructing pair, triple or four-label subset contained among the seven replaced labels of **every** Q in that class.

Adding EC49FJU–FJY's disjoint 113,316 certified retained-key cases per witness gives **121,880 exact local 94-prefix optima per profile** (**243,760** total A+B). Per profile **31,528** retained-key seven-replacement contexts remain unresolved, along with **192,696** contexts that release at least one original raw cache key. The global objective `C_min(7) ?= 94` remains open.

## Exact proof

For any frozen legal BRC word w, let P(w) be its set of all literal nonempty ordered, signed native-X6 microstep prefixes, let k(w) be the **complete raw** cache-key identity, and let label(w) be its typed observation (window, signature).

Because the fixed seventeen original words already use all seven original keys, an at-most-seven-key completion can only choose from those same keys. For a fixed F and omitted label ell, enumerate all members of

`A_F(ell,13) = { P(w)\\F : w is a legal pinned operation word, label(w)=ell, k(w) in K(F), |P(w)\\F|<=13 }`.

Any legal completion of total cost at most 93 would require one member from A_F for each omitted label, with their seven-way union having size <=13. For each of the 116 profile/background classes, `VERIFY_EC49FJZ_PORTABLE.py` identifies a pair, triple or four-label subset that appears in every omitted-label Q of the class and exhaustively checks **all** literal raw-word prefix-set unions for that subset. In every case there is no union with <=13 prefixes. This is a complete necessary-condition lower-bound certificate; candidate words adding >13 prefixes individually are irrelevant to any <=13-prefix completion. The checker only deduplicates *identical* intermediate literal unions, preserving every distinct prefix set; it performs no endpoint projection or subset antichain inference.

The original frozen EC49FGJ omitted seven words produce exactly 14 newly added native prefixes for every such background. Therefore each subproblem's minimum is **80+14=94**. The computation covers all 178,850 legal words with 94 full raw keys; 9,838 legal words use each witness's retained seven keys. This result is a finite local optimum under the exact frozen model, not a global seven-key optimum proof.

## Executed verification and files

The checker `VERIFY_EC49FJZ_PORTABLE.py` was actually executed locally on the frozen generator's mathematically equivalent source transcription and the unchanged explicit EC49FGJ A/B witness word lists, printing:

`EC49FJZ_ALL_17128_EXACT_PASS`.

Separately, a signed-prefix bitset antichain joint solver classified all 116 classes and produced exactly the same 822 pair, 6,610 triple and 9,696 four-label certificate counts; an independently coded literal full-catalog check without antichain verified all 116 class obstructions. Local evidence includes complete per-class JSON reports, the executed verifier log, exact input transcription and SHA256 inventory. The GitHub checker runs directly against the **original immutable source**; that original input is already published in the sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/` directory of this PR.

To reproduce, place the unchanged sibling `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` in an `EC49FJR/` subdirectory beside the checker (or arrange the equivalent Python path), and execute `python VERIFY_EC49FJZ_PORTABLE.py` in a writable directory. It emits `EXACT_REPORT_EC49FJZ.json` containing 116 explicit per-class labels, input word-counts and certificates; the script itself asserts all expected totals. `EXACT_SUMMARY_EC49FJZ.json` provides the checked scope and class census.

**Next scientific unit:** retained-key radius-seven B=14 and other remaining budgets, plus seven-position contexts that release one or more original raw keys and independent global search for a 93-prefix witness. Frozen science, P000, real native identities and project admission authority remain unchanged.
