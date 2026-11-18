# EC49FIP — Exact six-path B=10,12 fixed-seven-key BRC classifications

Date: 2026-11-11. Author-side finite result on **frozen scientific input** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scientific predecessor: EC49FIO at PR #1730 commit `dda59d4db14676a0fdc83f432a9d9e03729a593f`, original EC49FGJ seven-key 94-prefix witness blob `e65c1598ad9fa2680558046ed1e59d83806536b8`. Research identity: `EM-DIRECT-B9C642 / TASK_RESEARCH`, native Activity `RA-0542BAEDBBDDC45AB734BD25` in Source `cb5929727610876f82c54faa3e29c738d6e1bacd`. Formal task CLAIM, Result and independent Driver approval remain outstanding.

## New exact finite theorem

Let A and B be the two original EC49FGJ BRC witnesses, each satisfying 24 labelled observations using exactly seven *complete* cache keys and 94 distinct nonempty ordered, signed, six-native-axis microstep prefixes. Pick any six demand labels `Q`, retain the other 18 original witness words, and denote their distinct native-prefix union by `F(Q)`. Consider cases in which the 18 fixed words retain **all seven** original complete cache keys and `|F(Q)|=93-B`, for `B in {10,12}`. For A and B separately there are exactly 2,572 cases with B=10, and exactly 2,970 cases with B=12.

For **every one of these 11,084 fixed-background subproblems**, among all legal six-word completions satisfying the original six BRC observations and using at most seven complete keys, the exact minimum total distinct native-prefix cost is **94**:

```
min_{legal w_1,...,w_6; |K(F(Q) union {w_i})|<=7}
|F(Q) union P(w_1) union ... union P(w_6)| = 94.
```

The fixed background already occupies all seven possible complete keys, hence any legal completion in the seven-key cap uses only those exact keys. The frozen nine-state observer enumerates 178,850 legal words globally; the restricted set comprises 9,838 complete words and 42,735 prefix-trie nodes. It is therefore the full candidate catalog for these cases.

## Exact coverage, lower-bound certificate

Define the 24-bit support of each original prefix `p` as the set of witness labels whose original words use `p`. A prefix disappears when removing Q iff its support is contained in Q. Thus `removed(Q)=94-|F(Q)|` can be computed exactly by testing bit-support inclusion. Only Q satisfying `removed(Q)=B+1` and preserving all seven complete-key supports are selected. This enumerates all `C(24,6)=134596` possible Q per original witness, without a heuristic candidate filter.

For any fixed background and any subset T of the six missing labelled observations, let

```
m_F(T) = min | (union_{i in T} P(w_i)) \ F |,
```

over all permitted BRC words for the labels in T. For the complete six-label cost, `m_F(all six) >= m_F(T)` for every T. Thus any pair or triple with `m_F(T)>B` rigorously excludes a 93-prefix completion. The solver computes each pair/triple minimum **exactly**, by a bottom-up rooted signed-prefix-trie DP. Each edge contributes zero if already in F and one otherwise. For child u, subset S and a nonempty assigned subset T, the recurrence is

```
d_new(S) = min_{T subseteq S} [ d_old(S\T) + d_u(T) + c(u) * 1_{T nonempty} ].
```

Rooted path unions are rooted prefix subtrees; child/subset decomposition exhausts all legal selections and charges each distinct prefix edge once. The pair/triple implementation uses descending mask order to preserve the old state for strict submasks, and unbounded integer DP entries. Every reported lower bound comes from the complete original-key-restricted catalogue.

The original removed six words supply `B+1` additional distinct prefixes, so each case has a matching admissible total cost `(93-B)+(B+1)=94`. Exact lower and upper bounds match for all cases.

| Exact screen | A B=10 | A B=12 | B B=10 | B B=12 |
|---|---:|---:|---:|---:|
| Fixed-key six-label Q | 2,572 | 2,970 | 2,572 | 2,970 |
| Exact pair lower bound > B | 2,572 | 2,893 | 2,572 | 2,970 |
| Further exact triple lower bound > B | 0 | 77 | 0 | 0 |
| Still permits 93 prefixes | 0 | 0 | 0 | 0 |
| Matched exact total optimum | 94 | 94 | 94 | 94 |

In addition to complete pair/triple verification for all 11,084 cases, the independent previous six-label full-prefix-trie solver was run on a deterministic 35-case sample per class (140 samples): each returned exactly `B+1` new prefixes and zero completions within budget B. All arithmetic is integral.

## Reproducibility and evidence

The exact source of the frozen observer, the two witnesses, the 42,735-node restricted prefix tries, and the exact C++ pair/triple and full-six DP kernels is preserved in EC49FIO's predecessor evidence. `VERIFY_EC49FIP.py` here independently re-enumerates all six-label Q from the signed original words, writes four Q lists, invokes the reused exact C++ solver and asserts the complete class counts and empty survivor sets. Run once per profile (`A` and `B`) when using bounded runtimes. For repository reproduction generate trie inputs with EC49FIO `MAKE_INPUT_EC49FIO.py`, compile EC49FIO `VERIFY_EC49FIO.cpp` with `g++ -O3 -std=c++17`, and place those dependencies beside the verifier as directed in its header. The old B=13 Q generation is an incidental output of this setup; the B=10/12 Q files are regenerated by EC49FIP.

The checked machine summary `EXACT_REPORT_EC49FIP.json` supplies exact counts and SHA256 of all four generated Q files. The local conversation evidence archive additionally contains the original trie and witness data, both compiled source programs, the complete Q lists, four actual solver logs, and 140 full-six crosscheck inputs/outputs.

The original scientific constraints include order, signed native steps, full key identity and observation signatures. The lemma is a finite six-label neighborhood statement, with the user-selected P000/X6 research foundations unchanged. The seven-key unrestricted global minimum remains at most 94; its exact value is open.

## Next discriminating unit

Extend the exact screen to the fixed-original-seven-key `B>=14` six-label classes, grouping equivalent fixed-prefix support masks, and test for any genuine cost-93 candidates. Separately develop a key-aware prefix-trie DP for cases in which deleting six original paths releases one or more complete cache keys. Preserve the frozen witness/observer pin and independent review scope.