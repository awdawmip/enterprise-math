# EC49FGR — Exact three-word stability of both seven-key 94-prefix BRC witnesses

**Date:** 2026-11-10. **Frozen science input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** author-side exact finite theorem; independently computed; Driver review and canonical mathematical admission pending.

## Result

Let W be either of the two EC49FGJ original-24-demand, seven-raw-key, 94-native-prefix witnesses A or B, with ordered signed-X6 paths and the frozen nine-state BRC observer. Fix all but at most three of W's 24 labelled complete operation words literally. Replace those three words with **arbitrary valid** words meeting their original window/signature/endpoint obligations, while using **at most seven distinct complete raw cache keys across the 24 words**. Then the native nonempty signed-microstep-prefix union has **at least 94 elements**, attained by W.

```
C_min(W; at most 3 labelled words changed, at most 7 full keys) = 94.
```

Hence any seven-key, 93-prefix global witness must differ from **each** of A/B in **at least four** of the 24 labelled paths. The global question `C_min(7) ?= 94` is not settled by this local theorem.

## Why all admissible radius-three cases use the original seven keys

There are `binom(24,3)=2,024` unordered triples. Let `F` be the union of native prefixes of the 21 unchanged words, and `B=93-|F|`. An alleged 93-prefix completion requires the union of three added difference-prefix sets to contain at most B prefixes.

For **each** baseline profile, 816 triples have `|F|>=94` and are immediately excluded. Of the other 1,208 triples, 974 still retain all seven original full keys in the 21 unchanged words. Among 228 triples with only H2-key vacancies, the unique original H2 realizations `(H2,16):fe` and `(H2,32):ge` must be restored; thus the seven original keys are occupied. Six further triples remove both H3 paths (`feg` and `gef`) plus a single H8 or H9 path, leaving only six original keys including a vacancy for `(3,1,1)`.

The complete frozen-model H3 key supports, obtained by exhaustive literal six-letter enumeration, are:

```
(H3,16): {(3,1,1), (4,0,1)}
(H3,32): {(3,1,1), (2,2,1)}
```

Their intersection is exactly `{(3,1,1)}`. With six fixed keys, using any other H3 alternative would require at least eight total keys (one old and one new or two distinct new keys). Consequently the six exceptional triples must also restore `(3,1,1)`. This proves the **complete seven-key restriction** in the surviving 1,208 triples; no feasible 93-prefix triple is lost by generating replacement words only from the original seven keys.

## Exact exhaustive result

For each admissible triple, generate all original seven-key legal words with the frozen nine-state automaton and exact signed-X6 endpoint, retain their full ordered-microstep prefix sets, and take differences against F. Prune individual candidates with more than B new prefixes, and exhaustively compare the remaining pair unions and final third sets. Two separate executed Python programs agree:

| Measure | Witness A | Witness B |
|---|---:|---:|
| Label triples exhaustively classified | 2,024 | 2,024 |
| Fixed-prefix exclusion | 816 | 816 |
| Screened triples | 1,208 | 1,208 |
| At least one label individually has no feasible path | 914 | 914 |
| Two-label difference unions already impossible | 52 | 60 |
| Three-label unions checked and excluded | 242 | 234 |
| Exact pair-set tests | 42,855 | 42,787 |
| Exact three-set tests | 151,570 | 150,451 |
| Valid completions costing ≤93 | **0** | **0** |

The first checker uses exact integer bitmasks and count-vector generation. The independent checker uses direct six-letter DFA recursion and immutable tuples of signed axis microsteps. All tested sets and cardinalities are exact integers; this is exhaustive finite evidence within the described neighborhoods.

## Sources, reproduction and next action

Parent pinned witnesses: [EC49FGJ/WITNESSES](https://github.com/awdawmip/enterprise-math/blob/2e4d05d4270f646336dcdfa0470ec93dbd4f036e/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json), Git blob `e65c1598ad9fa2680558046ed1e59d83806536b8`; frozen BRC model blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. Companion exact two-word verifier and corresponding BRC operation/count definitions are stored in sibling `EC49FGQ_RADIUS_TWO_NO93_20261110/EC49FGQ_EVIDENCE_20261110.tar.xz.b64`; independent six-letter generator in that sibling's `EC49FGQ_DIRECT_CROSSCHECK.py`.

The complete executed evidence package `EC49FGR_radius3_evidence_20261110.tar.xz` is retained in the conversation and contains the three-label exact solver, separate independent checker, original seven-key parent witnesses, inherited frozen BRC utilities, 2,416 per-triple records (1,208 for each profile), two independent summary reports and other validation files. Running the two programs regenerates all results.

Next task: extend this proven radius-three bound to radius-four combinations, prioritizing cross-window changes that can release and reuse raw keys while preserving the exact original 24 signatures. No prior task CLAIM is presumed. The historical `EC49AS` task currently returns `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`. P000 and protected worldview remain unchanged.
