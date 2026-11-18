# EC49FJU — exact 94-prefix certificates in radius-seven retained-key BRC neighborhoods (2026-11-11)

**Status:** author-side exact finite theorem, independently rechecked on selected individual instances; formal independent Driver mathematical admission pending. **Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This continues EC49FJT and the previously completed radius-six work without changing the frozen native model.

## Theorem: 133,960 newly certified seven-word neighborhoods

Let `W` be either of the two frozen, valid EC49FGJ witnesses A/B. Each has 24 **distinct, labeled** BRC observation demands, seven complete raw cache keys, and a union of 94 nonempty, **ordered and signed** native X6 microstep prefixes. Select any seven labeled word positions `Q` and keep the other 17 original words exactly fixed. Define `F(Q)` to be their native prefix union, `K_F` their set of full raw cache keys, and `B(Q)=93-|F(Q)|`.

This theorem considers the **153,408** seven-position selections per witness for which the fixed 17 words already occupy all seven original full keys. The global at-most-seven-key condition therefore confines *every possible replacement word* to those original seven raw key identities.

An exhaustive exact screen certifies **66,980** of those selections per witness, hence **133,960** separate fixed-background subproblems across A/B. For **every certified selection**, the exact minimum over all seven legal replacement words satisfying the seven original labeled demands is **94 distinct native prefixes**. The original selected seven words supply an explicit 94-prefix feasible completion; the screen below proves the corresponding lower bound.

| Exact certificate class | A | B | Combined |
|---|---:|---:|---:|
| Fixed 17 words already retain all 94 prefixes (`B=-1`) | 9,218 | 9,218 | 18,436 |
| Exact one-demand shortest-new-prefix lower bound exceeds `B` | 37,950 | 37,950 | 75,900 |
| Exact two-demand joint prefix-union bound exceeds `B`, for `B=3,5,7` | 19,812 | 19,812 | 39,624 |
| **Total certified** | **66,980** | **66,980** | **133,960** |
| Retained-key selections awaiting multi-demand optimization | 86,428 | 86,428 | 172,856 |

The *additional*, disjoint pair certificates are `10,632` each for `B=3`, `7,920` each for `B=5`, and `1,260` each for `B=7`. All `17,760` retained-key `B=3` selections per witness are closed: 7,128 by a singleton bound and 10,632 by a pair bound. Among `B=5`, 2,636 survive the pair screen; among `B=7`, 2,520 survive after 8,472 singleton exclusions and 1,260 pair exclusions.

These are seven-position subproblems fixing **17** original words, not a repetition or relabeling of the previous six-position theorems fixing 18 words. Their certificates hold for the full pinned legal BRC word catalog subject to the seven complete raw cache-key identities retained in the fixed background.

## Exact finite proof and algorithm

The frozen nine-state BRC catalog contains **178,850** legal operation words and **94** different raw complete cache keys. Of these, **9,838** legal words use one witness's seven original keys. For each candidate word `w`, write `P(w)` for its complete set of literal nonempty signed ordered native prefixes (each microstep, preserving origin/order/sign). For a fixed prefix-closed `F`, the minimum incremental cost for label `l` is:

```
m_F(l) = min_{legal word w satisfying l, fullkey(w) in K_F} |P(w) \ F|.
```

It is computed exhaustively from the 9,838 legal words using a shortest-suffix index `D(p,l)` over prefixes `p` plus the empty-root option. Since `F` is prefix-closed, for any word the number of new prefixes equals its full prefix length minus the longest existing initial prefix. Encode each baseline prefix `p` by the 24-bit support `supp(p)={i: p in P(w_i)}`. It remains fixed after deleting `Q` exactly when `supp(p)` is **not** a subset of `Q`. This support identity computes each exact fixed-prefix set and all singleton minima without recomputing the full catalog.

If `B<0`, the unchanged 17 words already cost 94. If `m_F(l)>B` for any omitted label, no completion can meet cost 93. Otherwise, at budgets `B=3,5,7`, compute the **actual two-label** minimum:

```
m_F(l1,l2) = min_{w1,w2 legal under K_F} |(P(w1) union P(w2)) \ F|.
```

Enumerate every legal word for each label with individual added cost at most `B`; excluding longer words is exact for a hypothetical union of cost at most `B`. A pair with `m_F(l1,l2)>B` proves the full seven-label union also exceeds the budget. Only *one* violating pair is needed per fixed background. All set unions are exact finite operations; no unsigned/endpoint quotient, floating approximation, trigonometric substitution, or non-BRC source of candidate words occurs.

The 7-position enumeration is complete because `binom(24,7)=346104` subsets per witness, of which exactly 153,408 keep all seven original keys among the fixed 17. The proof does not require 93-edge nonexistence over arbitrary 24-word constructions. It establishes a sharp 94 lower bound on the listed finite fixed-background subproblems.

## Reproduction, crosschecks and scope

`VERIFY_EC49FJU.py` is the actually executed combined exact enumerator and writes `EXACT_REPORT_EC49FJU.json` containing per-budget classifications, preserved-key counts, and concrete pair witnesses. Input dependencies are the frozen original `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` already published in PR #1730. Place both in one directory and add that directory to `PYTHONPATH`; run the verifier from a writable directory with Python 3.

The full catalog was separately scanned directly for 40 selected single-demand cases (20 excluded/20 survivors), and 60 selected pair obstructions across B=3,5,7 and both witnesses. All 100 direct-catalog rechecks agreed with the aggregated exact solver. The separate scripts `R7_CHECK.py`, `R7_PAIR_CHECK.py`, `R7_PAIR_B3.py`, `R7_PAIR_B5.py`, `R7_PAIR_B7.py`, raw generated JSON reports, pinned dependencies, and validation logs are retained in the complete author evidence archive. Those follow-up screens independently reproduce the combined category counts.

**Remaining scientific problem:** 86,428 retained-key seven-word selections per witness still need multi-demand exact optimization. A further 192,696 seven-word selections per witness release at least one original key and require actual full-key-selection treatment. Route one: use grouped prefix-support backgrounds and joint three-/seven-label weighted trie DP. Route two: search nonlocal legal 93-prefix constructions directly. The global `C_min(7) ?= 94` remains open. Formal task ownership, Result publication, and independent Driver admission remain separate from this author-side evidence.

**Source status at authoring:** immutable science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original baseline EC49FGJ on PR #1730. This publication makes no claim of a current EC49AS CLAIM, current adopted theorem, or completion of the global problem.
