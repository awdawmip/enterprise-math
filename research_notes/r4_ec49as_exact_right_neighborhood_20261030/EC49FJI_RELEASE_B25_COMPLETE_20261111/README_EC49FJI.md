# EC49FJI — released original key, six-replacement budget 25: exact 94-edge local optimum

Date: 2026-11-11. Status: `AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED`.
Scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Researcher-ID: `EM-DIRECT-7E6456`; native research activity `RA-447EA47BD40819D4990A3BCA`.

## Statement and precise domain

Use the EC49FGJ frozen A and B witnesses, each with 24 **distinct labeled** BRC observation requirements, seven full raw cache-key types and 94 distinct ordered/signed native six-axis prefixes. Choose any six witness words Q for substitution, and keep the other 18 paths unchanged. Let F(Q) be their native prefix union and K_F their full raw key set.

**Finite theorem.** Every such Q with |F(Q)|=68 and |K_F|<7 has exact minimum total native prefix cost **94**, allowing arbitrary legal replacement words with at most seven full cache keys. Exhaustively enumerating all C(24,6)=134596 position choices per witness gives 8 qualifying Q for A, 8 for B, total 16. The 93-edge target permits only 25 new prefixes.

All 16 positions have Q=(i,10+j,14+j,18+j,22,23) with i in {0,1}, j in {0,1,2,3}, under the original sorted witness-label indexing. Each releases exactly one key: (3,0,1) for i=0 or (2,1,1) for i=1. The retained paths occupy six original keys, so at most one additional key can be selected.

## Key-cover lemma

Enumerate the frozen **178850** legal nine-state words and their **94** full raw key types. For each of the 16 Q, let M be the six labels to replace, and K_F the fixed six keys. Compute the missing labels M' not covered by K_F. Exhaustive comparison over each of the other 93 available key identities shows no key outside K_F other than the released original key covers M'. Hence any legal seven-key completion must restore exactly the original seven-key set. This is a necessary support statement; it does not use or assume prefix-cost optimality.

## Exact trie recurrence and bound

Build the ordered/signed native prefix trie of *all* legal words for the six labels restricted to the forced original seven keys. For a trie node v and label subset S of the six requirements, d_v(S) is the least number of newly used native prefix edges in the rooted subtree satisfying S, excluding the edge entering v. Terminal masks cost 0 for their submasks. A child u with edge cost c(u)=0 for an edge already in F and 1 otherwise obeys

```
d_new(S) = min_{T subset S} (d_old(S \ T) + d_u(T) + c(u) * 1[T != empty]).
```

The disjoint label assignment enumerates every valid collection of six root-to-terminal paths; each shared native prefix is charged exactly once. States above 25 are clipped at 26. The Python verification instead keeps sparse label-mask dictionaries, using the identical exact recurrence; a separate C++ full-trie implementation, with distinct code and data layout, was also executed locally.

Every one of the 16 full six-label tries returns **26** as its clipped minimum (and in fact is attained by its original six words). Trie node counts are 12084, 13199, 14212, 15971 in each repeated symmetric family. The frozen witness always contributes exactly 26 new prefixes on top of 68 fixed ones, giving the matching upper bound.

Therefore for every specified Q,

```
min_{legal six-path completion, total full keys <=7} |F(Q) union P(new paths)| = 68+26 = 94.
```

This is a scoped finite local theorem about the two explicit EC49FGJ witnesses. The global seven-key existence/optimality question remains open.

## Reproduction and evidence

Run `VERIFY_EC49FJI.py` beside the frozen `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from the prior EC49FGW/FGJ immutable research inputs, unchanged. It enumerates all positions, does all-key cover elimination, builds all 16 exact signed native tries, checks the original 94-edge witnesses, prints 16 per-case records and `EC49FJI_ALL_16_PASS`. The actually executed independent Python run returned this sentinel on all 16; the independently compiled C++ full-trie run returned 16 results all `best_clipped=26`, `feasible_93=0`, with the same trie-node counts.

The complete local evidence archive includes `B25_EXACT_TRIE.cpp`, `MAKE_B25_INPUT.py`, `B25_CATALOG.tsv`, `B25_CASES.tsv`, `B25_RESULTS.jsonl`, `INDEPENDENT_B25.py`, output logs and SHA256 manifest. GitHub primary code is the complete executable Python verifier; the expanded archive remains a separate user-facing deliverable.

Next: classify previously uncovered released-key six-position budget classes (in particular 10,12,13,14,16,19–22) and then examine seven-or-more changed-path neighborhoods and nonlocal 93-edge construction searches. Preserve original input pin, typed complete keys, signed ordered prefixes and independent Driver review scope.
