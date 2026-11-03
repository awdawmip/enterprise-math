# EC49FAC — Re-screen under strict 76-edge cutoff and 75 signed-X6 exact exclusions

**Author-side finite research, 2026-11-04.** Parent objective: minimize the total number of distinct nonempty **ordered signed primitive** prefix edges of the frozen h=2,…,8 native X6/BRC observer problem with exactly five complete positive-step six-axis cache keys, at most six nine-history transfer signatures, and rank-nine observer matrices. This is a scoped continuation of EC49FAB; accepted scientific input remains frozen at Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` and account `773d538180bfb49e24cffeb35c3ee75eb0628e2e`.

## Result FAC-1: full existing lower-bound threshold census

On the **complete 12,356-entry EC49EXY double-collision candidate list**, reapply the established, observer-aware lower bound `E >= B_EXY` under strict cutoff `E<76`. The previously published lower-bound histogram is a complete classification of these 12,356 schedules. Direct exact-integer aggregation gives:

| B_EXY | Schedules |
| --- | ---: |
| 62–75 inclusive | 5,042 |
| 76 | 1,622 |
| 77 | 1,410 |
| 78 | 2,260 |
| 79 | 2,022 |
| **Total** | **12,356** |

Thus precisely **7,314** schedules obey `B_EXY >= 76`, sufficient to rule out `E<76`. Relative to EC49FAB's **6,402** unexcluded schedules, **2,573 previously unexcluded** schedules fall into `B_EXY = 76` (1,395) or `77` (1,178). After removing exactly these distinct schedules, **3,829** arrangements remain. This is a reuse of a previously proved lower-bound theorem at a stronger cutoff, not new independently solved fixed arrangements.

**Reconciliation rule:** rank the exact immutable EXY TSV by total admissible native words ascending, then `-B_EXY` (Python stable sort). Remove schedules previously resolved by EXZ first 200, FAA ten, and FAB 1,506 successes; retain FAB timeouts. After the lower-bound update, five FAB timeouts remain below the lower-bound cutoff, with original ranks `272,273,517,1002,1003`. The other FAB timeouts (`387,914,915,950,951`) are now excluded by `B_EXY >= 76`.

## Result FAC-2: 75 new exact integer exclusion certificates

The **unchanged** native signed-path generator and integer OR-mask prefix-trie dynamic program (published under sibling `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/`) were executed on 75 distinct source-ranked fixed schedules with strict cutoff `E<76`, using `g++ -O3 -std=c++17`. All 75 runs terminated successfully with **`BOUND_PASS minimum_total_at_least=76`**. The entire finite input for each case consists of its full seven-window key assignment, actual native admissible operation words, signed primitive trie, and nine-history observer-color mask; `EC49FAC_CASE_RECEIPTS.tsv` records **all 75 zero-based schedule ranks and full SHA256 of each exact solver stdin**. A repository-source replay program is supplied.

- **5 recovered former timeouts:** ranks `272,273,517,1002,1003`, previously capped at cutoff 78; at 76 each now terminates with a strict exclusion.
- **70 previously untouched schedules:** ranks 2310–2407 with explicitly recorded gaps in the receipt TSV. They include 18- and 20-color inputs.
- Colors: **52 at 18**, **18 at 20**, **5 at 22**. Admissible word counts 217–438; signed-prefix trie nodes 917–2,678.
- No `E<=75` construction was found within these 75 exact cases.

**Why the integer certificate suffices.** A state at each trie node retains the minimum number of newly paid edges needed to cover a specified OR-mask of the node's descendant observer demands. Child disjoint subtries are combined by OR and exact addition of edge costs, charging a shared path prefix only once; the already mandatory 28 h2-core edges are prepaid. Pruning states with extra cost `>=48` is sound for strict total `28+extra<76`. Consequently a completed root DP without the full-demand mask at extra cost below 48 establishes `E_min>=76` for that exact fixed schedule. This finite claim depends on the frozen generator's complete enumeration and correct observer-color assignment and the optimizer's exact integer recursion. The independent EC49FAB explicit-witness validator confirms feasibility and cost of the previously published four 76-edge witnesses.

## Updated disjoint research frontier

`6,402 (FAB unresolved) - 2,573 (newly threshold-excluded) - 75 (newly exactly excluded) = 3,754`.

**Mother-problem author-side bounds remain `63 <= E* <= 76`.** The new exclusions refer to the double-collision candidate class after the earlier triple-collision exclusions; all numerical deductions are across disjoint zero-based source schedules.

The 75 certificates are author-side computations; neither a Source-native formal Result nor independent Driver acceptance is asserted. Current connected native backend has `research_authority_granted=false`; the live owner query returned `CONTROL_QUOTA` on 2026-11-04. No protected P000 or ACTIVE-worldview change has been made.

## Reproduction and further problem

Immutable historical inputs: EC49EXY candidate TSV and exact capacity source; EC49EXJ `SCREEN_H5_EC49EXJ.py` and `EXACT_OR_MASK_DP.cpp`; EC49FAB archived evidence and exact 76-edge witness validator. Compile the published DP C++17 source; from this directory invoke `python3 REPLAY_EC49FAC.py /path/to/exact_or_mask_dp`, which recomputes 75 full native inputs, checks each recorded SHA256 and demands the identical strict-76 `BOUND_PASS` result.

**Next EC49FAD:** search the **3,754** remaining double-collision schedules with `B_EXY<76`; prioritize exact DP for 18/20-color schedules and improve branch-and-bound for larger observer masks. If a strict `E<76` PASS occurs, recover complete signed words, six-axis BRC keys, all nine-history signatures, seven rational-rank-nine observer matrices and distinct primitive prefix edge set before reducing the mother's upper bound. Keep prior genuine TIMEOUT states open.

**Durable state:** GitHub author-side Draft PR #1730; retain actual submission/readback as the publication receipt.