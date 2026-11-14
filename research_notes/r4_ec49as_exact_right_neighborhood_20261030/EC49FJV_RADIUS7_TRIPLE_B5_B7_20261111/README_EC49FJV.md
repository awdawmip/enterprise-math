# EC49FJV — complete retained-key radius-seven B=5,7 via exact triple-prefix certificates

**Date:** 2026-11-11. **Frozen BRC scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Independent author-side exact finite derivation/computation; not yet independently Driver-reviewed or admitted. Continuation of EC49FJU in Draft PR #1730.

## New theorem and final combined radius-seven frontier

For each of the pinned valid EC49FGJ 94-native-prefix witnesses A/B, choose any seven of the 24 distinct labeled BRC paths for replacement, fixing the other 17 unchanged. Restrict to the retained-key class: the fixed 17 original words collectively already use all seven of the witness's complete raw cache keys. Thus every permissible replacement must use one of these same seven full key identities.

Let `F(Q)` be the signed ordered native X6 microstep-prefix set of the 17 fixed words and `B(Q)=93-|F(Q)|`. The earlier EC49FJU exact singleton/pair screen left, per witness, 2,636 unexcluded cases with `B=5` and 2,520 with `B=7`. The present exhaustive **three-label prefix-union screen excludes every one**: for each case, some triple of its seven labels has exact required additional-prefix union minimum **strictly greater than B**. The original seven omitted witness paths supply a legal 94-prefix solution, so each of these **5,156 newly closed cases per witness (10,312 combined)** has exact optimum 94.

| Per-witness retained-key class | B=5 | B=7 |
|---|---:|---:|
| All seven-position cases | 10,556 | 12,252 |
| Earlier singleton exclusions | 0 | 8,472 |
| Earlier pair exclusions | 7,920 | 1,260 |
| **New exact triple exclusions** | **2,636** | **2,520** |
| Remaining within this class | 0 | 0 |

Combining with EC49FJU's 66,980 previously certified cases per witness yields **72,136 exact local 94-prefix optima per witness, 144,272 across A/B**. Among the 153,408 seven-position cases per witness that retain the original seven full keys, exactly 81,272 await stronger multi-demand certificates.

In particular, **all** retained-key seven-position cases with budget `B=-1,1,3,5,7,10` are now completely certified: 9,218 + 16,940 + 17,760 + 10,556 + 12,252 + 5,410 = **72,136 per witness**. Other budget classes require additional joint-observer optimization. In the full 346,104 seven-subset universe per witness, a further 192,696 release one or more of the original seven keys and require a separate complete-key selection analysis.

## Exact three-label lower bound

For a fixed background `F`, original complete-key set `K_F`, and label `l`, enumerate `A_F(l,B)`, the sets `P(w)\setminus F` of *every* pinned legal BRC word `w` satisfying `l`, using a key in `K_F`, and individually adding at most `B` native prefixes. Because `F` is prefix-closed, this is calculated exactly by the longest existing native initial prefix of each candidate word. Retain full signed native X6 microstep order and the complete raw cache-key identities.

For any triple of labels `(l1,l2,l3)`, calculate its exact within-budget completion test:

```
min {|A1 union A2 union A3| :
     Aj in A_F(lj,B)  for j=1,2,3}.
```

If the minimum is greater than `B`, then **no seven-word completion** can meet the total 93-prefix target. Every word omitted from `A_F(l,B)` individually exceeds `B` and so cannot belong to an at-most-`B) union. Thus the triple screen is a valid complete finite necessary-condition certificate, not a heuristic search. An explicit original seven-word 94-prefix solution supplies the sharp upper bound. At least one violating triple exists in **all 2,636 B=5 and 2,520 B=7 cases for each profile**.

The executed exact input contains **178,850** nine-state BRC legal words and 94 raw full cache keys; each witness's seven allowed original keys admit **9,838** full legal words. `R7_TRIPLE_B5_B7.py` executes the complete fixed-17-key-retained seven-position census, rechecks the one-label and two-label exclusions, and then enumerates the exact three-label signed-prefix set unions. The program returns **2,636 and 2,520** new triple certificates for both A/B. An independent direct-word-catalog `R7_TRIPLE_DIRECT_CHECK.py` rechecked **40 representative triple obstructions** from both budget classes and profiles, matching the exact lower bounds.

## Reproduction and evidence

Use the unmodified `EC49FGW_RADIUS5_SCREEN.py` generator and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` frozen witness file previously published in PR #1730. Place these together on `PYTHONPATH`, then run `python R7_TRIPLE_B5_B7.py` in a writable directory. Output: `R7_TRIPLE_B5_B7_REPORT.json`, including per-profile budget counts and explicit violating triples. `R7_TRIPLE_DIRECT_CHECK.py` independently traverses full labeled legal-word triples for selected cases.

The full author evidence archive contains both actual executed programs, their source dependencies, complete JSON reports, independent word-catalog check, and file hashes. These computations are scoped to a *finite local neighborhood of the two known 94-prefix witnesses*. The global seven-key optimum `C_min(7)?=94` is the remaining mother question; the next local unit should use three-/higher-observation and exact full-subset trie optimization for the 81,272 unresolved retained-key contexts per witness, and complete-key-aware optimization for the 192,696 seven-position contexts per witness releasing a key.

**Authority:** author-side material; no current EC49AS CLAIM, formally frozen Result, or independent Driver mathematical admission is asserted.
