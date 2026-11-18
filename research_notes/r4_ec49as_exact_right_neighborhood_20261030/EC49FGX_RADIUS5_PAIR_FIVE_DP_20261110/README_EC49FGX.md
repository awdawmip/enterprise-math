# EC49FGX — Exact pair screen and five-way small-budget exclusion at radius five

Date: 2026-11-10. Role: independent research author, TASK_RESEARCH. Immutable scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source witness: EC49FGJ A/B, 24 legal signed-native X6 BRC paths, 7 original complete raw keys and 94 distinct nonempty ordered signed-native microstep prefixes. Parent: EC49FGW radius-five screen. This is a new finite local result, not a claim of global `C_min(7)=94`.

## The precise question

For either fixed 94-prefix A/B baseline, choose five of the 24 labeled words for replacement, preserving the original nine-state DFA, terminal signatures, native endpoint `(2,0,0,0,0,0)`, and **at most 7 complete raw cache keys**. Can the resulting 24 paths have at most 93 distinct nonempty **ordered signed six-axis microstep prefixes**?

EC49FGW proved that out of the `C(24,5)=42,504` labeled replacement positions per baseline, 16,056 remained after sound single-path and raw-key-cover screens. This round studies the **no-key-release** shell (unmodified 19 paths already occupy all 7 original raw keys). This shell has 25,158 positions, 3,992 fixed-background exclusions, 10,008 single-path exclusions, and 11,158 cases surviving the earlier checks.

## New exact pair theorem

Let `F` be the union of unchanged words' native prefix sets, and `B=93-|F|`. For any legal replacement native words `u,v`, let `L_u,L_v` be microstep lengths and let `k_u,k_v` be the lengths of their longest prefixes in the prefix-closed set `F`. Put `d_u=L_u-k_u`, `d_v=L_v-k_v`, `t=lcp(u,v)` measured in exact signed-native microsteps.

Then

```
|(P(u) union P(v)) \\ F|
  = d_u + d_v - max(0, t - max(k_u,k_v)).
```

Proof: `P(u)\\F` and `P(v)\\F` are suffix chains after `k_u,k_v`, respectively. Their common elements are exactly the nonempty prefixes of lengths strictly exceeding `max(k_u,k_v)` and not exceeding `t`; this gives the intersection count in the formula. Consequently, **if for any pair of changed labels no legal pair has union-cost <= B, then the entire five-word replacement is impossible**. Because the 19 fixed words already retain all 7 raw keys in this shell, only the original seven keys need be enumerated, without losing any seven-key solution.

The complete frozen-model candidate catalog has 178,850 legal words / 94 raw keys, with 9,838 words using each baseline's fixed seven-key domain. All 11,158 previously surviving no-key-release positions for each baseline were checked exhaustively across all ten pairs of changed labels.

| Stage within 11,158 surviving no-key-release positions | A | B |
|---|---:|---:|
| **Excluded by new exact pair test** | **7,884** | **7,910** |
| Retained after pair test | 3,274 | 3,248 |

This pair calculation used 17,295,371 literal word-pair comparisons for A and 17,286,746 for B, besides the sound early accept when the sum of individual delta costs is within `B`. An independent direct prefix-set crosscheck evaluated all ten pairs in 20 deterministic sampled positions for each baseline and agreed.

## New exact five-way exclusion for small budgets

For every remaining no-key-release position with `B<=9`, enumerate each legal replacement's **exact** set of native prefixes outside `F`. Give each such missing prefix a distinct local bit. Each label yields finitely many bitmasks; the five-label feasibility question becomes whether one mask per label has union popcount <= `B`.

An exact dynamic program starts from the empty mask and successively takes all unions with each label's possible masks, discarding unions exceeding `B`. After every layer it retains only subset-minimal masks (antichain): if `A subset B`, then any future union with `A` is contained in the corresponding union with `B`; deleting `B` is lossless for feasibility.

**All 464 remaining positions per baseline with `B<=9` are infeasible.**

| Remaining pair-pass budget B | 5 | 7 | 9 |
|---|---:|---:|---:|
| A and B, each | 308 | 144 | 12 |
| Exact five-way exclusions, each | 308 | 144 | 12 |

The maximum DP antichain reached 22 states for A and 33 for B; the largest examined transition work was 1,256 and 1,676 unions respectively. The full independent direct set-DFS crosscheck on 12 deterministic cases for each baseline agrees with the bitset DP.

## Combined newly certified reduction and live frontier

The earlier 16,056 five-position candidates **per witness** are reduced by (7,884 + 464) = **8,348** for A and (7,910 + 464) = **8,374** for B, leaving **7,708 (A)** and **7,682 (B)** position sets still requiring joint checking. Of the remaining sets, **2,810 (A)** and **2,784 (B)** retain all seven original keys with individual new-prefix budget `B>=11`; an additional **4,898** per baseline release a key and require key-aware joint search.

These are proven finite local necessary exclusions. The global seven-cache-key cost question `C_min(7) ?= 94` remains open; the established 94-edge upper bound is unchanged. A known five-key 112-edge optimization is a separate frozen-science result and is not repinned here.

## Executable, provenance and scope

`VERIFY_EC49FGX.py` reproduces the 178,850-word catalog from the unmodified original nine-state BRC generator and signed native six-axis path expander in the adjacent predecessor research unit `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py`; it reads that unit's archived EC49FGJ witness JSON and writes `EXACT_REPORT_EC49FGX_PORTABLE.json`. Run from repository checkout with Python 3.10+: `python research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110/VERIFY_EC49FGX.py`. No extra Python dependencies.

Local tests: main pair enumeration `EC49FGX_EXACT_PASS`, exact five-way `EC49FGX_FIVEWAY_SMALL_EXACT_PASS`, 400 direct pair-vs-prefix-set crosschecks `EC49FGX_CROSSCHECK_PASS`, and 24 direct five-way DFS checks `EC49FGX_FIVEWAY_CROSSCHECK_PASS`. The current consolidated source additionally asserts every numerical conclusion. The explicit historical source witnesses are pinned by Git blob `e65c1598ad9fa2680558046ed1e59d83806536b8` (EC49FGJ); no credentials or private executable capability are stored.

BRC reuse: `REUSE_EXECUTED` — prior frozen generator, exact signed native prefix semantics, key identities and support-hypergraph lemma. New work is a finite pair-union and five-way subset-antichain **application**, not a claim of a new universally admitted toolbox mechanism.

## Next smallest unfinished mathematical unit

Apply the same exact five-way subset-union DP to the 2,810/2,784 no-release survivors with `B>=11`, using branch-and-bound and antichain dominance; separately combine released-key assignments with key-aware union states for 4,898 remaining cases per baseline. A valid 93-edge seven-key witness, or complete exact absence over both local radius-five neighborhoods, would be a new scoped result; neither would by itself classify every seven-key construction.

Research/control separation: author-side evidence is stored on PR #1730's draft research branch; independent Driver review and formal Result acceptance require their own current authority. The previous historical task identifier EC49AS currently has no immutable publication and is not claimed by this research author.
