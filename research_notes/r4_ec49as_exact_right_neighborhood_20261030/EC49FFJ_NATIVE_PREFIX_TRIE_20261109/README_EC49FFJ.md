# EC49FFJ — Four-signature native-BRC prefix Steiner dynamic program and infinite witness family

Date: 2026-11-09. Role: author-side TASK_RESEARCH, independent Driver review pending. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent objective: at most five distinct complete BRC keys and at most 93 native signed-prefix edges. This result treats a one-window/one-key subproblem.

## Original carrier and finite problem

Use the same six-operation alphabet `ORDER='acdefg'`, ordered signed native-six-axis expansion `OPS`, and original nine-state DFA `T` / signature map from the frozen EC49FFH verifier, copied into `BRC_ORIGINAL_MODEL_EC49FFJ.py`. A length-h operation word and complete key `K=(x,y,z)` satisfy

`#a=z-1, #e=z, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x`,

with all counts nonnegative integers. For each h=2,...,8 enumerate every such key and select exactly one original word with each of the distinct signatures `1,2,4,8`. Cost is the number of distinct nonempty **ordered signed native X6 microstep prefixes** of the chosen four words. Each word has endpoint `(2,0,0,0,0,0)` and native length `2(x+y+z-1)`. No unsigned/endpoint-only quotient is taken.

## Theorem A — exact rooted-prefix-tree four-colour DP

At fixed (h,K), build a trie of all native signed prefixes of eligible operation words; mark every terminal node with the signatures of its realizing original words. Define F_v(S) to be the minimum number of trie edges strictly below node v connecting v to terminals realizing the required subset S of signatures. Set F_v(empty)=0. Split a nonempty S among signatures already terminal at v and disjoint subsets S_w demanded from each child w. Charge `1+F_w(S_w)` for a nonempty child assignment and 0 for an empty assignment. Minimize over all splits.

**Exactness proof.** Any selected four-word solution induces a rooted edge subtree. Assign each demanded signature to one of its realizing terminal words; this partitions signatures across the terminal node and child subtrees, producing a feasible DP choice whose cost is no greater than the original union. Conversely each finite DP choice determines actual terminal words covering all required signatures, with edge union counted by its recurrence; duplicating a signature is unnecessary. Hence F_root({1,2,4,8}) equals the global optimum for this (h,K); minimizing over the complete finite key enumeration gives the one-key optimum at h.

For q signature classes and N trie nodes, the direct recurrence has at most `O(N 3^q)` integer transitions and `O(N 2^q)` stored values, plus input-enumeration/trie construction cost. For q=4, precisely 16 states/node replace fourfold Cartesian enumeration. The algorithm needs no LP/MILP, floating point or probabilistic inference.

## Theorem B — completed one-key classification h=2..8

The executed exact integer verifier enumerates all legal count configurations and words, independently checks DFA signatures, full BRC key, original signed X6 endpoint and length, computes the trie DP, backtracks four witnessing original operation words, then recomputes their native-prefix union from tuple sets.

| h | All admissible full keys | Original eligible words | Total trie nodes | Minimum native-prefix edges |
|---:|---:|---:|---:|---:|
| 2 | 1 | 4 | 29 | 28 |
| 3 | 3 | 30 | 235 | 34 |
| 4 | 7 | 176 | 1,451 | 32 |
| 5 | 13 | 950 | 7,983 | 36 |
| 6 | 22 | 4,932 | 41,770 | **40** |
| 7 | 34 | 25,060 | 212,902 | **44** |
| 8 | 50 | 125,680 | 1,069,184 | **48** |
| **Total** | **130** | **156,832** | **1,333,554** | — |

The original complete 130-row report (with cost, group sizes, trie size and four witnesses for each key) is preserved losslessly as `EXACT_REPORT_EC49FFJ.json.gz.b64`. Decode with `base64 -d EXACT_REPORT_EC49FFJ.json.gz.b64 | gzip -d > EXACT_REPORT_EC49FFJ.json`. Original uncompressed report SHA-256 is `5c27e67e5c5d0b5f5e0c8dc6a9145f6e2021f71a1f815f1e07532409ed8a24a1`. The separate `VERIFY_EC49FFJ_BRUTE_SMALL.py` exhaustively computed all 3,389,185 four-word combinations for h=2..5 across all 24 keys; all 24 values match the new trie DP. A second full local trie run reproduces every one of the 130 rows and witness words.

## Theorem C — explicit infinite upper-bound family

For every integer h>=4, use one complete key `K_h=(4,h-2,1)` and these four original words (exponents mean repetition):

| Signature | Word |
|---:|---|
| 4 | `f e g^(h-3) c` |
| 2 | `f e g^(h-3) d` |
| 8 | `g f e g^(h-4) c` |
| 1 | `g f e g^(h-4) d` |

**Proof.** Each word has h operations and exactly the required counts for `K_h`; the declared original DFA yields signatures 4,2,8,1, respectively. Each signed X6 native expansion has endpoint (2,0,0,0,0,0) and length L=2h+4. Within each pair, the c-ending and d-ending words share exactly their first L-4 native steps, because the four-step expansions of c and d differ at their first step. Across pairs, the first microstep is respectively +e1 (from f) versus +e2 (from g), so no nonempty prefix coincides. Each pair contributes L+4 edges and therefore the entire four-word system has

`C_native = 2(L+4) = 4h+16`.

Thus `C_min(h) <= 4h+16` for **every** h>=4. The complete finite theorem above certifies equality for h=4,5,6,7,8. Equality for larger h is a specific new mathematical question; the construction itself is already valid without a horizon cutoff.

## Reproduction, scope and next discriminating test

Run `python3 VERIFY_EC49FFJ_TRIE.py --hmin 2 --hmax 8 --out EXACT_REPORT_REGENERATED.json`, then `python3 VERIFY_EC49FFJ_BRUTE_SMALL.py EXACT_REPORT_EC49FFJ.json`. All standard-library Python, deterministic exact integer/tuple computation. The local original model has been embedded alongside the verifier. Evidence: 130 exact key rows, 156,832 legal words, 1,333,554 native prefix-trie nodes, and 3,389,185 independent brute-force selections. A full rerun gave byte-equal row data to the stored report.

This is an exact finite result about the specified original one-window, one-full-key, four-low-signature model, and an infinite explicit **upper-bound construction**. It neither substitutes for a 22-path multi-window search nor changes P000 or the protected ACTIVE worldview. The parent still seeks <=5 full keys and <=93 native signed-prefix edges.

**EC49FFK:** complete the 70 original-key configurations at h=9, where the new infinite family supplies a 52-edge construction, or establish a stronger analytic key-independent lower bound. A bounded h=9 trie attempt did not complete; no unconditional finite h=9 minimum is claimed. Then adapt grouped signature masks and certified subtree bounds to multiwindow, multikey 22-path systems.

Provenance: preceding author frontier EC49FFI `53e1f6f452d57a2500da33949807093088b2e123`; current canonical rule reads GLOBAL_KNOWLEDGE_V1 main `a04a4db2931658bd0c44d7a51fdb1df29dbce6c7` and Enterprise Math main `639a491b38cfd969c5a0604206ca2a562a390cbf`. Status: `AUTHOR_EXACT_FINITE_THEOREM / EXACT_TRIE_DP_PASS / INDEPENDENT_SMALL_BRUTE_PASS / NOT_ADMITTED`; native Researcher-ID/RA are separate from formal Owner/CLAIM/Driver admission.
