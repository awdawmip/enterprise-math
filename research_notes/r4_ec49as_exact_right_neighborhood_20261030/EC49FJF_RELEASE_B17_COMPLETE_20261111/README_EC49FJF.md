# EC49FJF — released-key six-label BRC neighborhood at B=17: exact 94-native-prefix theorem

Date: 2026-11-11. Status: AUTHOR_EXACT_FINITE / UNREVIEWED.
Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Sources: EC49FGJ A/B witnesses and EC49FGW exact nine-state legal-word generator; previous frontier EC49FJE at `ffae7b3712d3853411b17c874faea8c33abebc1a`; PR #1730.

## Exact statement

For either of the two pinned 24-distinct-labeled observation-demand BRC witnesses A/B (seven complete raw cache keys and 94 ordered signed native X6 microstep prefixes), choose any six of its 24 paths to replace. Hold the other 18 witness paths fixed. Write F(Q) for their complete signed ordered native prefix union and K_F for their full raw cache key set. Restrict to Q such that |F(Q)|=76 and K_F excludes at least one of the witness's original seven keys. The replacement words may be any legal BRC words for the six original labeled window/signature demands, using no more than seven distinct complete raw keys globally.

Then for **every** such Q, the exact minimum of the overall distinct native prefix count is 94. There are exactly **936** qualifying Q per witness, **1,872 cases total**. The original six words give a feasible 94-edge completion (18 newly added edges), so it suffices to exclude a completion adding <=17 new edges.

## Exhaustive case partition, separately for both A and B

| Certificate | A | B | Exact reason no <=17-edge completion exists |
|---|---:|---:|---|
| HIGH | 720 | 720 | All original seven keys forced; high-window (H8/H9) label prefix-union antichain DP empty at budget 17. |
| PLUS_1 | 104 | 104 | All seven forced; high-window labels plus one specified lower-window label DP empty. |
| PLUS_2 | 104 | 104 | All seven forced; high-window labels plus two lower-window labels DP empty. |
| UNFORCED | 8 | 8 | Six original keys fixed and any seventh raw key allowed; exact complete six-label signed trie DP excludes <=17 for all budget-compatible seventh-key choices. |
| **Total** | **936** | **936** | A/B original words provide 18-edge upper bound. |

The forced-key condition follows from finite exact 94-key covering, not a fixed-key assumption. Let K0 be the original seven keys, R=K0\K_F. For each r in R, exhaustively check whether the six labels can be covered by K_F and at most |R| extra keys excluding r. If no such cover exists for every r, then all R keys must return, exhausting the maximum seven-key allowance. `ec49fjd_shared.py:key_cover` uses exact bitset subset covering over all 94 raw-key types.

For an eligible word w let D_F(w)=P(w)\F, where P(w) preserves every signed, ordered native six-axis microstep prefix. The exact antichain solver for fixed allowed keys iterates over chosen labels, using the union U of their D_F(w). It discards states with |U|>17 and inclusion-dominated states: if U1 subset U2, any future continuation union is no more costly from U1. An infeasible subset of six requirements is a sufficient lower-bound certificate for all six. Actual executed exact classifications: A HIGH=720, PLUS_1=104, PLUS_2=104; B identically. The 1,872-row complete Python case ledger was generated (647,564 JSON bytes, SHA256 `95693d80af3ad95fd85bd6249688a93124f6cb868d11ab4c3c5bee5eee2c14e7`).

The **16 UNFORCED cases** (8 per witness) each retain exactly six full keys in fixed words. With seven-key cap, the seventh key must be from the other 88 legal raw key types. A new key having no legal path for any selected label with <=17 new prefixes cannot occur in a <=17-edge completion; a complete screening of the 94-key catalogue leaves 44,44,43,43,44,44,43,43 candidate keys per witness, or **348+348=696** candidate-key exact DPs overall. For each candidate allowed set K_F U {k}, a C++ exact signed native prefix trie solver considers every legal operation word under those keys, assigns terminal labeled masks, merges child subtrees by disjoint demand-mask partition, and charges a native edge only when missing from F. This includes solutions using no new key. All 696 computations have clipped minimum cost 18, hence no solution with <=17 additional edges. Original witnesses realize cost 18. The actual full result log contains sixteen records, all `feasible_93=0` and `best_clipped_cost=18`, SHA256 `5fe09bb8bebc8aa5d211ab4f2285fb07c7249463da7a4a2b1dc2c763998a549f`.

## Exhaustiveness, reproducibility and status

The finite exact nine-state grammar generates 178,850 legal operation words, 94 full raw-key types and exactly 24 labeled window/signature demands, using all `C(24,6)=134596` six-position sets per witness before restriction. No floating arithmetic, endpoint quotient, sign loss, branch erasure or greedy pruning enters the certificates. In the C++ program the 18 cost cap is a precise decision representation of all costs >17; true equality 18 follows from the explicitly retained original witness.

Executed source: `SOLVE_B17_FINISH.py`, `MAKE_B17_CPP_INPUT.py`, `B17_EXACT_TRIE.cpp`; source dependencies `EC49FGW_RADIUS5_SCREEN.py`, `ec49fjd_shared.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from the preceding frozen evidence set. Generate `B17_CATALOG.tsv` and `B17_CASES.tsv` using input generator, compile `g++ -std=c++17 -O3 B17_EXACT_TRIE.cpp -o B17_EXACT_TRIE`, run with arguments `B17_CATALOG.tsv B17_CASES.tsv B17_CPP_RESULTS.jsonl`; compare all 16 cases to `EXECUTED_SUMMARY_EC49FJF.json`. Python antichain solver was additionally run on all eight A and the first two B UNFORCED cases, with consistent exclusion.

All 1,872 case rows were generated in the author's full 647,564-byte JSON ledger, preserved in the separate conversation evidence archive (SHA256 stated above); the exact GitHub Python verifier deterministically reproduces that ledger. The GitHub branch contains the theorem, both complete executed verifiers, the input generator, the 16-case C++ result log, and the structured execution summary; it does not contain the large raw case ledger. The separate author archive contains the full native word catalogue, run logs, C++ executable, inputs and SHA256 manifest. These are author-side finite certificates; independent Driver mathematical review and formal Result have not occurred, and PR #1730 is an unmerged draft. The mother question `C_min(7) ?= 94` remains open globally.

**Next:** released-key radius-six backgrounds for B=18/23 and nonlocal 93-edge candidate construction across all 24 labeled demands. A candidate must include 24 exact operation words, full raw keys and independently checkable signed-prefix union.
