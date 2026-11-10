# EC49FHF — Exact H9-pair lower-bound for released-cache-key five-path neighborhoods (2026-11-11)

**Status:** Author-side exact finite proof and computation. Original frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Existing seven-raw-cache-key, 94-native-prefix BRC witness profiles A and B from EC49FGJ. Follows EC49FHE at PR #1730 commit `f7b6a1b121a5a4abf38fcfcd1143bf10b3210ddb`.

## The new proposition

For either witness A or B, select five of the 24 exact BRC observation-label paths for replacement. Let `Q` be those labels, `F(Q)` the ordered signed-X6 native-prefix union of the other 19 fixed paths, and

`B(Q) = 93 - |F(Q)|.`

Assume `Q` contains **both** H9 observations, with original signatures 16 and 32. Let `W_9,16` and `W_9,32` denote the complete frozen observer's legally typed words for those two signatures. Define

`m_9(F) = min_{u in W_9,16, v in W_9,32} |(P(u) union P(v)) \ F|,`

where `P(w)` is the set of **all nonempty ordered and signed native six-axis step prefixes** of word `w`. This minimum has *no restriction on cache keys*, hence it is a valid necessary bound even with arbitrary key reassignment.

**Theorem.** Each witness has exactly 62 high-budget, key-releasing five-path position sets that require **at least 94 native prefixes** solely from the two mandatory H9 observations:

- 60 position sets with `B(Q)=18`, `m_9(F(Q))=19`;
- 2 position sets with `B(Q)=21`, `m_9(F(Q))=22`.

Thus every corresponding complete five-path replacement, even allowing any number of raw cache keys, costs at least `|F(Q)|+m_9(F(Q)) = 94`. The original full witness already realizes 94, so these 62 fixed-background completion problems have exact optimum **94** under the original at-most-seven-key condition.

Combining this result with EC49FHE and preceding fixed-key radius-five work leaves **164** unclassified released-key five-path positions **per witness** (not 164 distinct global constructions); the prior 226 has been reduced by 62. The remaining budgets per witness are `B=17:128`, `B=19:20`, `B=20:16`. The global minimum `C_min(7)` still has a known upper bound of 94; its precise value remains under investigation.

## Exact proof of pair-bound reduction

For every legal completion containing H9/16 path `u` and H9/32 path `v`, its total used prefix union contains `F(Q) union P(u) union P(v)`. Consequently

`C_native >= |F(Q)| + |(P(u) union P(v)) \ F(Q)| >= |F(Q)| + m_9(F(Q)).`

The argument applies to every assignment of the other three paths and every raw cache-key configuration, since neither can erase a retained or mandatory H9 prefix. The finite minimum `m_9` is solved exactly by a rooted prefix-trie group-cover DP. Each edge corresponds to its full signed and ordered X6 prefix and has cost zero precisely if that prefix is in `F`, otherwise cost one. A node's terminal mask records which required observation(s) can legally stop there. For mask `S`, combine disjoint child demand subsets by exact subset convolution

`(d*g)(S)=min_{T subseteq S} (d(S\T)+g(T)).`

The root value at full mask equals the minimum union edge cost by induction on the tree: an admissible connected subtree is the union of paths from the root to selected legal terminals, and the recurrence tries each distribution of its required observation labels among children. One selected terminal may cover multiple groups when legal. Every edge is counted once. No continuous geometry, floating-point arithmetic, axis-order collapse, or cache-key approximation appears.

The frozen catalog enumerator reports `178850` BRC-legal words in all, including exactly `11440` H9/16 and `11440` H9/32 legal words. Across the high-budget, key-releasing search (226 sets per witness), **210** sets include both H9 labels and share only **25 distinct fixed-prefix backgrounds** per witness. The exact trie solver evaluates each distinct background once; all 25 are then linked back to all their position sets.

## Exhaustive finite audit

For **each** of A and B, the 210 both-H9 positions give:

| B(Q) | m_9(F(Q)) | position sets | B < m_9? |
| ---: | ---: | ---: | :---: |
| 17 | 16 | 112 | No |
| 18 | 19 | 60 | **Yes** |
| 19 | 16 | 20 | No |
| 20 | 19 | 16 | No |
| 21 | 22 | 2 | **Yes** |

An additional 16 positions per witness contain only one H9 label, and are not decided by this pair test. Thus `62` new excluded sets per witness, `124` total **witness/position instances**, with no claim that this is a global independent-construction count.

The accompanying `VERIFY_EC49FHF.py` includes the exact two-group trie DP **self-contained**; its only scientific dependencies are the existing original BRC generator and baseline witnesses at `../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, under the frozen research branch. Running it in the declared repository layout generates `EXACT_REPORT_EC49FHF.json` with all inspected label sets and produces `EC49FHF_EXACT_PASS`. The original author-side run separately executed the prior verified trie implementation (`VERIFY_EC49FHD.py` from EC49FHD) against the frozen exact catalog; the locally generated per-case report is retained in the handoff evidence package. The two-group self-contained implementation uses the same recurrence and exact semantics.

**Proof scope:** finite BRC observer, frozen signed-six-axis word generator, each of the two specified 94-edge witness neighborhoods. This result is author-side and awaits independent mathematical Driver review; EC49AS has no active immutable formal publication/CLAIM at this snapshot.

## Next discriminating action

The remaining released-key radius-five positions are exactly the 164 per witness above: 128 of budget 17 (112 both H9; 16 single H9), 20 of budget 19 and 16 of budget 20. Apply an exact key-aware prefix-trie group-cover DP with one or two globally selected *new raw-key identities*, or a branch-and-bound formulation with a preserved key-mask. In each case the finite certificate is either a feasible five-path set with at most seven raw keys and cost ≤93, or an exhaustive exact infeasibility result. If the entire 164-per-witness neighborhood is closed, move to larger-radius/global constructions, preserving the original mother problem.

## Provenance

- Immutable science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
- Frozen baseline: EC49FGJ witness profiles A, B, 7 raw keys and 94 ordered signed X6 prefixes.
- Immediate predecessor: EC49FHE README, summary and reproducer, PR #1730 `f7b6a1b121a5a4abf38fcfcd1143bf10b3210ddb`.
- Native author activity for this turn: `RA-4A22EBBA09F9E715F87F4585` (`EM-DIRECT-B875FC`, research only).
- No new P000 or worldview modification, no formal Result/Driver approval.
