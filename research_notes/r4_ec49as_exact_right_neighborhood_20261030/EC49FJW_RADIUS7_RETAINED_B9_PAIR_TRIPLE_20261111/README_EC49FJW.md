# EC49FJW — Exact radius-seven retained-key B=9 classification

**Date:** 2026-11-11 · **Frozen science SHA:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · **Scientific status:** author-side finite exact theorem with independently implemented direct-word checks on sampled certificates; independent Driver review and formal Result admission pending.

## Statement and exact finite domain

Fix either of the two pinned BRC seven-cache-key, 94-native-prefix witnesses A and B from EC49FGJ. Each witness supplies 24 distinct labeled observation requirements with legal nine-state BRC ordered words. Choose a seven-element subset Q of those 24 labeled positions and fix the other 17 original words literally. Let F(Q) be the union of their **signed, ordered X6 microstep prefixes**, and K(F) be their **full raw cache-key identities**.

We consider the class with both:

* F(Q) contains exactly 84 original prefixes, hence the budget for attaining 93 prefixes is B=9;
* the fixed 17 words still use all seven original full raw keys, so any legal <=7-key replacement must use those same original keys.

Of the 346,104 seven-element subsets per witness, 153,408 retain all original seven keys. Precisely **17,424** of these per witness have B=9. They form **24 distinct F(Q) backgrounds** per witness.

**Theorem.** For every one of those 17,424 fixed-background subproblems for A and for B, the exact minimum total number of native prefixes among all legal replacements of the seven omitted words is **94**. Consequently this work gives **34,848 new local finite optimum certificates** across A and B. It is not a global proof that seven-cache-key minimum is 94.

| Per witness (A and B have equal counts) | Count |
| :-- | --: |
| All retained-key, B=9 contexts | 17,424 |
| Excluded at exact two-demand prefix-union stage | 16,776 |
| Further excluded at exact three-demand prefix-union stage | 648 |
| Remaining contexts in this class | **0** |
| Exact best total native prefixes | **94** |

This new B=9 class is disjoint from EC49FJU–FJV's previously certified 72,136 retained-key radius-seven contexts per witness. New cumulative total: **89,560** per witness, **179,120** across both; remaining retained-key radius-seven contexts: **63,848** per witness. Separately, **192,696** key-releasing seven-position contexts per witness remain to be studied.

## Proof and certificate semantics

For a complete legal pinned BRC word w, let P(w) be its full set of literal nonempty ordered signed native-X6 prefixes. Let label ell denote one of the seven omitted observation requirements. Given a fixed prefix-closed background F and budget B=9, form the finite family:

```text
A_F(ell, B) = { P(w) \ F :
                 w legal in the complete frozen BRC nine-state catalog,
                 raw_cache_key(w) in K(F),
                 w satisfies ell,
                 |P(w) \ F| <= B }.
```

Any valid seven-word completion with total <=93 must choose one member of this family per omitted label. It cannot use a word which *alone* introduces >9 prefixes. For any pair or triple of omitted labels, compute exact unions of their eligible families and test whether **every** union has size >9. One violating pair or triple proves no <=93 completion for those fixed 17 words.

The finite operations preserve the **full raw key**, ordered signed six-axis microsteps, and literal native-prefix sharing, not an endpoint-coordinate or unsigned multiset quotient. For efficiency, each per-label candidate family is reduced to a set-inclusion antichain: a superset is dominated by its subset for all future union-size decisions. The same valid inclusion domination is applied to merged pairs when searching triples. No eligible <=9 union is discarded.

The exact full-key screen gives 24 fixed-prefix-background classes. Pair-screen enumeration excludes 16,776 seven-position subsets per witness; 648 survive. The triple-screen enumerates **all** of those 648 per witness. They fall into 12 fixed-prefix-background classes of 54 subsets each and are all excluded. Original omitted paths from the frozen EC49FGJ witnesses provide an actual completion with 94 prefixes, yielding the upper bound. Combining the lower and upper bounds proves the sharp local optima.

**Interpretation caution:** when the candidate families exclude words individually costing >9, a filtered pair/triple minimum of 10 or 11 is a valid **impossibility certificate for <=9**, not an assertion about an *unfiltered* pair/triple minimum. Original seven replacement words produce only 10 additional prefixes collectively. The theorem claims no feasible <=9 addition, plus the existing 10-addition construction.

## Execution and reproducibility

The same immutable BRC generator from EC49FGW enumerates **178,850** native legal words under 94 complete raw keys. Of these, **9,838** use the original seven keys of either witness. Executed scripts here:

* `EC49FJW_RADIUS7_B9_PAIR.py` — exhaustive radius-seven key-retained B9 classification and exact pair antichain search;
* `EC49FJW_RADIUS7_B9_TRIPLE.py` — exhaustive triple-antichain search on all pair survivors;
* `EC49FJW_DIRECT_CROSSCHECK.py` — separately written literal signed-prefix word enumeration, with no antichain/support optimization, checking **192** actual obstructions (48 pair and 48 triple per A/B profile).

They actually ran in Python against the frozen generator and witness JSON. GitHub contains all three executable scripts and `EXACT_SUMMARY_EC49FJW.json`, which records the classifications and SHA256 of each original executable input, full per-case report, and execution log.

**Dependencies:** obtain unchanged `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from the previously published sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/` directory of this same Draft PR; place both files together in an `EC49FJR/` subdirectory beside these three scripts, or make them available through `PYTHONPATH`. From this directory run in order:

```bash
python EC49FJW_RADIUS7_B9_PAIR.py
python EC49FJW_RADIUS7_B9_TRIPLE.py
python EC49FJW_DIRECT_CROSSCHECK.py
```

The scripts regenerate `EC49FJW_B9_PAIR_REPORT.json`, `EC49FJW_B9_TRIPLE_REPORT.json`, and `EC49FJW_DIRECT_CHECK_REPORT.json`. Their SHA256 values are given in the GitHub JSON summary.

A separately delivered, locally verified user evidence archive `EC49FJW_R7_B9_34848_COMPLETE_EVIDENCE_20261111.tar.xz` (16,064 bytes, SHA256 `661a71e0f749fd2c7e4914ea14e0aaa43cf30d646e9a652186e25d2650a856bb`) contains the unchanged frozen inputs, executables, all full per-case reports, direct checker report, logs and manifest. **This complete archive is a conversation attachment, not presently a GitHub file**; GitHub saves readable proof/code/summary and the exact steps to reproduce all reports. A nonempty archive and its content were verified locally.

## Remaining research and formal authority

Continue the **B=11** retained-key radius-seven category (15,736 contexts per witness in EC49FJU); attempt pair/triple certificates, then higher-demand native-prefix trie dynamic programming. Explore the 192,696 key-releasing seven-position contexts per witness using full-key-aware selection, and independently seek a globally valid 93-prefix construction.

This is author-side mathematical evidence under the pinned native-BRC finite model. A formal EC49AS claim, authenticated native Researcher-Activity, result freeze and independent Driver mathematical admission are **not** inferred from a PR commit; any native session/owner operation requires its own conclusive remote receipt.
