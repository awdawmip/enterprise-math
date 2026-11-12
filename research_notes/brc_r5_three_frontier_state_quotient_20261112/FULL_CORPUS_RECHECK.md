# R5 actual selected-word corpus: exhaustive prefix-counter cross-check

2026-11-12 (Asia/Shanghai), author-side experiment. Continuing the **same immutable** 15-atom 28-coordinate R5 Blackwell auxiliary input (no scientific repinning), this local CPython standard-library implementation independently rebuilt all 1,065 selected labeled paths from the pinned transport model and checked the DFS-terminal-order Fenwick aggregate against direct active-membership prefix sums after each of the 953 threshold groups and for **every one of the 2,880 trie nodes**, a total of 2,744,640 exact integer count equality checks. All comparisons passed.

- Selected words: 1,065, total 6,379 atom labels; trie nodes: 2,880.
- Exactly 953 event groups, 6,277 Fenwick counter writes.
- Author-local source reconstruction: 1.718472 s; complete 953-event/2,880-prefix query cross-check loop: 4.350931 s. These are observed **test harness timings**, not a fair production performance comparison.
- The declared packed logical fields remain 5,452 bytes (BP/terminal index/Fenwick/three frontiers) vs 8,210 bytes (predecessor indexed LOUDS/prefix counters).

The original independent local test was a self-contained 28-coordinate regeneration using the pinned inputs. The companion `VERIFY_FULL_CORPUS_FENWICK.py` reproduces the full scientific-corpus prefix-count check by importing **unchanged** predecessor `VERIFY_RIGHT_PERSISTENCE.py` and `VERIFY_TRIE_CODEC.py` from immutable source commit `ad7013218d0474e1e942906e3beadec1eccb9213`; those two source files must first be placed in the sibling source directory, exactly as in that immutable predecessor. This code intentionally does not declare those historical files present on this Draft PR's main-based branch.

The prefix index calculation has now been checked on the **actual** word corpus, not solely the previous generic synthetic trie. The 28-coordinate selected-path certification itself is the pinned predecessor's author-side mathematical evidence; this run's reproduction remains author-side and unreviewed.

Next: implement proper BP/LOUDS rank-select support and compare runtime/memory on the same corpus, with all event-table, navigation and input conversion overhead counted. Formal owner, activity checkpoint, Result and independent review are separate pending operations.
