# EC49FJO — released-one-key B=20–22 exact radius-six local minima

Date: 2026-11-11. Evidence: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Frozen sources: EC49FGW_RADIUS5_SCREEN.py; EC49FGJ_SEVEN_KEY_94_WITNESSES.json. Nine-state typed BRC, complete raw cache-key identity, ordered and signed six-axis microsteps.

## Exact finite result

Let A and B be the original 24-distinct-labelled-demand BRC witnesses, each using seven full raw cache keys and 94 distinct signed ordered native X6 prefixes. For each choice Q of six witness words to replace, retain the other 18 words, write F(Q) for their native prefix set, and let K_F be their complete raw key set. Consider precisely the Q where |K_F|=6 and |F(Q)| is 73, 72, or 71. Let B=93-|F(Q)| be 20, 21, or 22 respectively. Every legal six-path completion using no more than seven full raw cache keys has at least B+1 new prefixes. The original six words supply exactly B+1, so the exact combined optimum is 94.

The complete six-position choice universe has C(24,6)=134596 locations per witness. After enumerating and selecting exactly-one-key-release locations:

| Budget B | Fixed prefixes | A | B | All | Exact new-prefix minimum |
|---|---:|---:|---:|---:|---:|
| 20 | 73 | 240 | 240 | 480 | 21 |
| 21 | 72 | 69 | 69 | 138 | 22 |
| 22 | 71 | 40 | 40 | 80 | 23 |
| Total | | 349 | 349 | 698 | |

Nine other released-key cases per witness in these budgets release **two** original keys (eight at B20 and one at B21) and are not part of this theorem.

## Exhaustive seventh-key lemma

The frozen all_words() generator produces 178850 legal operation words and 94 distinct raw cache-key triples. For each k, define Cov(k) as the set of labelled demands realizable by some legal word with full key k. Each fixed 18-path context in this theorem uses six original keys. For each six-demand set Q define M as the labels in Q not covered by the fixed keys. A legal <=7-key completion can use the six fixed keys and at most one additional key k; hence M must be a subset of Cov(k).

Enumeration of all 94 key identities shows that **every one of these 698 cases has exactly one qualifying additional key**, namely the released original key. This establishes the full-key restriction for the ensuing exact trie calculation without presupposing that the new construction must reuse the old key.

## Exact prefix-tree proof engine

For each case, insert *all* legal words realizing the six labels under those original seven full cache keys into the ordered/signed microstep trie. The edge at signed native prefix p has cost c(p)=0 when p is in F(Q), and 1 otherwise. For a node v and six-bit label mask S, let d_v(S) be minimum new-prefix cost of meeting exactly the assigned subset S inside its descendants (not counting the entering edge). Terminal subsets are initialized at zero.

For child u and disjoint label subsets S,T, update

    d_new(S union T)=min(d_old(S)+d_u(T)+c(u)*[T nonempty]).

This enumerates all assignments of six distinct labels to root-to-terminal legal paths; shared native prefixes are charged once. It is an exact finite minimum. Clip costs at B+1 because only existence of a cost <=B would contradict the target.

Local executed generator MAKE_EC49FJO_INPUT.py returned EC49FJO_INPUT_698_PASS. Independent compiled C++ 64-mask trie engine EC49FJO_EXACT_TRIE.cpp returned SOLVED 698. Each of all 698 per-case lines had options=1, feasible_93=0, best_clipped=B+1; the original witness is an explicit B+1 upper-bound solution. Thus each case attains total 94.

## Exact execution integrity

Catalogue TSV: SHA256 b4e7bcc88306fa846f752f1ca1e6b31957e9ac65080d80a0c7506447004dc489.
Case TSV: SHA256 93f4658b405e011ff84633d88c837ee2ae5f9fbf9e4b054ad9d06b606c3cb2c4.
Full 698-row executed JSONL: SHA256 404d5ca9a0cc67e7291d2308022f6267181006e458b2e23d9559ece71c4709f2.
Source and full log, full TSV and per-case JSONL are also retained in complete author-side evidence archive EC49FJO_B20_B22_698_complete_evidence_20261111.tar.xz (SHA256 0c26d9718c60f2879e0ab04cd89fdc3cda3d6b02ed8564549bfb0f8512e89980).

To reproduce, put the two unchanged frozen EC49FGW/FGJ inputs alongside the supplied Python generator, run python MAKE_EC49FJO_INPUT.py, then compile g++ -std=c++17 -O2 EC49FJO_EXACT_TRIE.cpp -o exact; invoke ./exact EC49FJO_CATALOG.tsv EC49FJO_CASES.tsv result.jsonl. Require 698 lines, every one of which satisfies the above integer assertions.

## Next research problem

Resolve the two-key-release B20 (8 per witness) and B21 (1 per witness) cases with a key-set-aware joint trie; continue other uncovered radius-six budgets. EC49FJK covers 18 further released-key B23 positions, giving a combined 716 new local instances in this author turn. Global seven-key optimum C_min(7) ?= 94 remains open. This author-side result is stored in draft PR #1730; native role registration, formal Result and independent Driver review have their separate current authority.
