# EC49FIQ — Complete exact six-path local optimum for retained seven BRC cache keys

**Author-side finite theorem, 2026-11-11.** Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original EC49FGJ witnesses A and B (frozen word blob `e65c1598ad9fa2680558046ed1e59d83806536b8`) each satisfy 24 BRC observation labels with seven complete cache keys and 94 distinct nonempty *ordered signed X6 native microstep prefixes*. The current author session is `EM-DIRECT-B9C642 / TASK_RESEARCH`, Activity `RA-0542BAEDBBDDC45AB734BD25`, registered at Source commit `cb5929727610876f82c54faa3e29c738d6e1bacd`.

## Complete six-path theorem

For **either** original witness W, let Q range over all six-element subsets of its 24 labelled demands, fix the other 18 original words unchanged, and require that the fixed 18 words **already use all seven original complete cache keys**. Exactly **69,462 of the C(24,6)=134,596** possible Q satisfy this retained-key condition, for each witness separately.

For every such Q, among **all** six replacement words satisfying their frozen BRC observations under the `#complete cache keys <=7` rule,

```
 min |F(Q) ∪ P(w1) ∪ ... ∪ P(w6)| = 94,
```

where F(Q) is the native prefix union of the 18 fixed words, and P(w) is the full ordered signed six-axis prefix set. The equality holds for all **138,924** retained-key six-path subproblems across witnesses A and B.

The fixed 18 paths already occupy seven complete raw cache keys. Hence any admissible replacement must use one of the seven original keys. The frozen exact nine-state observer enumerates 178,850 complete legal operation words, of which **9,838** use these seven keys; their signed-prefix trie has **42,735** nodes. These are precisely all admissible replacements in this theorem.

## Exhaustive classification

For each original prefix p, let supp(p) be the 24-bit set of original witness word labels containing p. For Q with bit mask q, p disappears when deleting six original words iff `supp(p) & q == supp(p)`. Thus `r(Q)`—the number of original prefixes removed—is computed exactly, `|F(Q)|=94-r(Q)`, and the 93-edge target has residual budget `B(Q)=r(Q)-1`. A key is released by the deletion iff its own word-label support is contained in q. Enumerating every six-combination gives the same retained-key budget histogram for A and B:

| B | -1 | 1 | 3 | 5 | 7 | 9 | 10 | 11 | 12 | 13 | >=14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Q per witness | 6,941 | 10,824 | 9,344 | 4,400 | 6,582 | 8,700 | 2,572 | 6,284 | 2,970 | 2,498 | 8,347 |

Sum: 69,462. At B=-1, F(Q) itself already contains all 94 prefixes and requires no more computation.

For B>=0, every Q is excluded at budget B by **at least one exact lower-bound certificate**: singleton, pair, triple, or complete six-observation prefix-trie optimization. A subset T of the six required labels obeys

```
m_F(all six) >= m_F(T)
m_F(T) = min_{legal words for T} | (union_{i in T} P(w_i)) \ F(Q) |.
```

If an exact singleton, pair or triple minimum exceeds B, no six-word union can meet budget B. The full-six suffix cases are handled by the exact rooted signed-prefix-trie subset recurrence

```
d_new(S) = min_{T subseteq S} [
  d_old(S\T) + d_child(T) + c(edge)*1_{T nonempty}
].
```

`c(edge)=0` for F(Q) and 1 for a newly selected prefix; the rooted tree merge pays shared prefixes exactly once. The disjoint label-subset recurrence is exhaustive by induction over the prefix tree and its child branches.

**New exact computations completed in this unit:**

* Small budgets B=1,3,5,7: **62,300 Q combined** (A/B). A fast independently implemented singleton scan excludes 39,952; exact pair/triple screens close all remaining 22,348 cases; exact triple screens close the remainder. The complete per-budget rows in `EXACT_REPORT_EC49FIQ.json` are authoritative.
* High budgets B>=14 (15 nonempty budget categories, B=14..29): **16,694 Q combined**. Exact pair bound excludes 4,070; exact triple bound excludes another 7,264; complete six-label trie DP solves the remaining **5,360 Q**, returning **exactly B+1** in every case, and zero solutions with at most B new prefixes.
* Newly completed B=10/12 classes (11,084 Q combined): EC49FIP, exact pair/triple bounds and 140 full-six crosschecks.
* Inherited exact B=9 (17,400 Q): EC49FIM; B=11 (12,568 Q): EC49FIN; B=13 (4,996 Q): EC49FIO. Their published code, complete reports and exact proof scopes are cited in the machine report. Existing verified results are reused without renaming them as this run's new computations.

For every B>=0, retaining the original six witness words contributes precisely B+1 new prefixes, yielding `|F(Q)|+(B+1)=94`, so the lower bounds are sharp.

## Reproduction and evidence

`EXACT_REPORT_EC49FIQ.json` lists all 25 nonempty retained-key budget classes per witness, which algorithm stage excluded each class, and precise source file paths for prior work. `GENERATE_Q_EC49FIQ.py` reconstructs the full support histogram and any requested Q class from the original EC49FGW word/witness module. `VERIFY_SINGLETON_EC49FIQ.cpp` is the actually executed complete singleton-trie lower-bound kernel. Remaining pair/triple and full-six kernels are the already published EC49FIO `VERIFY_EC49FIO.cpp` and `VERIFY_FULL6_EC49FIO.cpp`. Local evidence archive carries the generated per-Q lists, original 42,735-node tries, actual solver logs and report assembler, frozen witness source, and full-six checks. All operations use exact integral counts, masks, and ordered signed prefix IDs.

This theorem closes the retained-all-seven-original-keys **six-word neighborhood** of both 94-prefix witnesses. Of the 134,596 Q per witness, **65,134** have fixed backgrounds that release at least one original key. Some may be excluded by previous independent screens or force restoration; their remaining exact key-reallocation subproblem is the next discriminating unit.

**Next:** combine native prefix-trie cost with a global complete-cache-key-selection state, then classify the key-release six-path cases and search for a legal 93-prefix witness. Also compare radius-seven neighborhoods as a route outside these fixed 18 backgrounds. Independent Driver mathematical review and formal Result admission remain pending.