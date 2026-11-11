# EC49FJB — complete the forced-seven-key released B=9 neighborhood (2026-11-11)

## New exact finite result

Continue EC49FJA on the same frozen nine-state ordered signed six-axis BRC model, scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, and original EC49FGJ witnesses A and B (each: 24 distinct observations, 7 complete raw cache keys, 94 distinct native prefixes).

Fix 18 of the 24 witness words; allow the other six positions Q to vary. Consider the cases that release an original key, yet exhaustive legal-key coverage forces the eventual completion to reuse **all seven** original keys, and have `|F(Q)|=84`, i.e. a 93-prefix solution has at most 9 new prefixes.

The preceding EC49FJA proves **7,080** Q per witness with one selected H8 and one selected H9 observation require a 10-prefix H8–H9 union. The *complementary forced-key B=9 class* has **744** Q per witness and no selected H9 observation; this report solves all 744:

- **720** Q per witness each have a selected pair of observations for which the *exact* legal seven-key minimum new-prefix union is **11**.
- **24** Q per witness select three H8 observations. Every selected pair can have a new-prefix union of at most 9, but the *exact triple H8* minimum is **10**.

Thus, for every complementary Q, all legal completions require at least 10 new native prefixes. Original A/B witnesses attain total 94, giving a **new 1,488-case exact local optimum of 94** (744 per witness). Together with EC49FJA:

```
Per witness, released-key B=9 and forced-original-seven-key:
  one H8 + one H9: 7080    (EC49FJA)
  no H9:              744    (EC49FJB)
  total:             7824
Both witnesses: 15,648 exact 94-optimum six-position subproblems.
```

There are also **64** released-key B=9 cases per witness not forced to retain all original keys. The present argument does not address those, nor other six-path budget classes. This does not prove all-global 7-key optimum.

## Exact coverage and reproducibility

The unchanged frozen generator enumerates 178,850 legal words and 94 raw key types. For each six-position Q, compute all original-prefix support masks and determine released keys. Requiring `|F|=84`, no H9 among selected observations, and one or three H8 observations, exhaustively test key-cover feasibility after excluding *each* original released key. Exclusion infeasibility for every released key forces the full original seven-key set.

For each selected observation, enumerate all legal words from those original seven keys, preserve complete ordered signed six-axis native prefixes, and retain only paths adding at most nine new prefixes. Every omitted word alone exceeds the 93-edge increment budget. Test all pairs; if no pair has union >9, test all selected triples of H8. Compute minima as exact finite set-cardinality, without floating arithmetic. Actual 2026-11-11 local execution:

```
EC49FJB_PROFILE_PASS A {'forced_no_H9': 744, 'PAIR': 720, 'TRIPLE_H8': 24}
EC49FJB_PROFILE_PASS B {'forced_no_H9': 744, 'PAIR': 720, 'TRIPLE_H8': 24}
EC49FJB_EXACT_PASS 1488
```

For all 1,440 pair-certified cases the program returns minimum **11**; for all 48 triple-certified cases minimum **10**. The executed source archive `VERIFY_EC49FJB.py.gz.b64` decodes to Python source, verified original SHA256 `7fc820e7108ba3ba1f15de707e9be028ad364e6075934e7e82e13f97d80c869c` (4,689 bytes). In a Python standard-library environment decode via `base64 -d VERIFY_EC49FJB.py.gz.b64 | gzip -d > VERIFY_EC49FJB.py`, place it beside the EC49FGW frozen generator and exact A/B compact witness file, then run `python VERIFY_EC49FJB.py`. It writes `EXACT_REPORT_EC49FJB.json` containing all **1,488** explicit Q/certificate records; executed report SHA256 `0be3df4e4e5837a8dce451bd71a31fcb3b9da6c4c899b840a312995237d0a04b` (1,441,617 bytes). Report can be reproduced from the immutable script and pinned inputs; the original full report is also in the local handoff archive.

Frozen model and witness sources are the EC49FGW sibling directory at the exact research ancestor `f1cfadff6d9949c5278195f0b3f5f0f39a42531d`. Their 48 witness demand strings were checked against the actual remote GitHub compact serialization; this computation preserves all original key identifiers, six-axis signed order and observer windows.

**Status:** `AUTHOR_EXACT_FINITE_PROOF / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. This is author-side evidence, not a Source-native Result or an independent Driver review. Researcher `EM-DIRECT-1F534E`, activity `RA-3D374FF8D860D14A0A87B9FA`; no task CLAIM.

**Next:** investigate the 64 released-key B=9 positions per witness that permit key reallocation, and other higher-budget six-position neighborhoods, while maintaining global mother question `C_min(7) ?= 94`.
