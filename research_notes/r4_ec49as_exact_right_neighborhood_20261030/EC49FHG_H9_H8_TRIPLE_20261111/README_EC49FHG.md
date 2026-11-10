# EC49FHG — H9-pair + H8 triple lower bound closes 112 more five-path neighborhoods (2026-11-11)

**Research mode:** independent TASK_RESEARCH author-side exact finite proof. **Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Witnesses:** EC49FGJ seven-raw-cache-key, 94-native-prefix BRC witnesses A and B. **Prior frontier:** EC49FHF (62 high-budget key-release positions excluded per witness). This result uses exactly the nine-state frozen observer and the full 178,850-word legal generator.

## Proposition and result

For each of the two fixed witnesses, select any five labels Q from the 24 original observations, leaving 19 paths fixed. Let F(Q) be their nonempty ordered, signed-native-X6 prefix union, and B(Q)=93-|F(Q)|. Consider those Q with all of:
1. both H9 observation labels (9,16) and (9,32) belong to Q;
2. at least one of the seven original full raw cache keys is released by Q;
3. B(Q)=17.

Exactly **112** such Q exist per witness, and each has |F(Q)|=76. Every Q contains exactly one H8 observation (8,s), s in {1,2,4,8}, with 28 Q per signature. For each witness and each s, a complete, key-unrestricted three-terminal prefix-trie calculation gives

```
m(F(Q); H9/16,H9/32,H8/s)
  := min_{u in W_(9,16), v in W_(9,32), w in W_(8,s)}
       |(P(u) union P(v) union P(w)) minus F(Q)|
  = 18.
```

Each H8/signature case has one unique fixed-prefix background F; there are precisely four such backgrounds per witness. The two H9 legal-word groups each contain 11,440 candidates; H8 signatures 1 and 4 have 28,063 each; H8 signatures 2 and 8 have 34,777 each. The trie solver is exact over every group.

Every five-path completion contains all three mandatory paths, so its total union contains at least |F(Q)|+18=76+18=**94** distinct native prefixes. The original seven-key witness achieves 94. Consequently all **112** such Q per witness have exact minimum 94 under the original <=7-key requirement; the lower bound itself holds without any cache-key limit. These are **224** newly closed witness/position instances, not 224 distinct global configurations.

The earlier EC49FHF frontier of 164 unclassified released-key radius-five positions per witness is reduced to **52 per witness**, with remaining B17 (16 positions involving only one H9 signature), B19 (20) and B20 (16). These 52 remain separate from the unrestricted seven-key global question `C_min(7) ?= 94`.

## Exhaustiveness and proof mechanism

The exact original A/B 24-demand records and the pinned frozen nine-state BRC generator are loaded from `../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/`. Prefix supports and full raw-key supports are computed directly from witness paths. All 5-element subsets of the 24 labels are enumerated (`choose(24,5)=42504`), and the three conditions above select exactly 112 for each witness.

The solver is the existing tested exact rooted native-prefix trie group-cover DP from EC49FHF. A trie edge has cost zero if its complete ordered signed-native prefix is already in F(Q), and one otherwise. At each node, subset-convolution DP ranges over every assignment of the three terminal groups to subtrees. The induction on the rooted tree proves that its root full-group value is precisely the minimum union of newly paid prefixes. Key identities never enter this bound, so cache-key reallocations cannot defeat it.

The witnessed executable author run, using the EC49FHD implementation of the same exact recurrence over all legal words, reported for each profile:

| H8 signature | positions | exact min new prefixes | prefix trie nodes |
|--:|--:|--:|--:|
| 1 | 28 | 18 | 261,390 |
| 2 | 28 | 18 | 299,979 |
| 4 | 28 | 18 | 261,390 |
| 8 | 28 | 18 | 299,979 |

**Validation:** `VERIFY_EC49FHG.py` uses the same complete candidate domains and the independently published EC49FHF recursive group-cover implementation; it asserts every count and all minima. The author-side complete 224-row report in the execution evidence bundle has SHA256 `11101ebc53b14ca84ccdc9cfb838b0d3319c4c1845ee15f6ecfb2721362af25e`; the actual run log SHA256 is `da7a669aadebba60de6dedcf84b45a67f57ed4bb02366c4e94ba9301b1b965c2`. Per-case report is regenerable with this script. The proof's limited radius-five witness scope and its author-side review status are preserved.

## Source and next unresolved problem

- EC49FGJ baseline: `../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGJ_SEVEN_KEY_94_WITNESSES.json`.
- EC49FHD: exact five-label native-prefix trie solver, frozen scientific pin.
- EC49FHE: all key-release five-label instances with B<=15 excluded.
- EC49FHF: exact H9-pair lower bound and 164-instance frontier (per witness).
- Research activity: `RA-6474640ADE1A6AC80E938BF2`, Researcher `EM-DIRECT-FEEAA1`; no EC49AS formal CLAIM or Driver admission asserted.

**Next:** For the remaining 52 Q per witness, test triples combining H9 with other mandatory H8/H6 labels for B17 single-H9 groups, and four-demand or complete key-aware prefix-tree bounds for B19/B20. Preserve frozen source pin and the exact full-cache-key budget.
