# EC49FIN — six-path B=11 exact pair/triple exclusion

Date: 2026-11-11. Role: independent author research, native Researcher-ID `EM-DIRECT-04BDD4`, activity `RA-CE8B3AFDDE628F1874926EF9`. Scientific input is frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Historical 94-edge witnesses: EC49FGJ A/B, blob `e65c1598ad9fa2680558046ed1e59d83806536b8`. Predecessor: PR #1730 at `f665586316c5d3c47ae424ec5cf6bf449a1e02f6`.

## Exact finite proposition

For either 24-demand, seven-key, 94-edge witness A or B, choose six demand labels `Q`, keep the remaining 18 original words, require that those fixed words still occupy all **seven original complete cache keys**, and require exactly 12 original native prefixes to be removed by deleting the six chosen paths. This means fixed-background cardinality 82 and a 93-edge target leaves **B=11** new prefixes. For **all 6,284 such Q per witness**, the cost of any legal six-word completion with at most seven complete keys is at least 94. The original six words provide a completion of cost 94; hence the exact optimum for each of the 12,568 fixed-background subproblems is 94.

The universe is the complete frozen nine-state BRC legal-word catalog of 178,850 words, with 9,838 words using the seven original keys of either witness. Raw keys are complete `(count(+E1),count(+E2),count(+E3))` tuples in the frozen native model, and path cost counts **distinct nonempty ordered signed six-axis native prefixes**. The fixed 18 paths already use seven keys, so every admissible replacement word necessarily belongs to the seven-key subcatalog.

## Exact dynamic-programming lemma

Construct a rooted trie containing the native ordered signed prefixes of all 9,838 permitted words. The edge into trie node `v` costs zero if its prefix belongs to the retained background `F(Q)`, and one otherwise. For a nonempty demand subset `S` of size at most three, let `d_v(S)` denote the minimum cost of a rooted prefix subtree below `v` that reaches a word terminal for each label in `S`. Terminal states are initialized at zero, and children are merged by the disjoint subset convolution

```
(d * g)(S) = min_{T subset S} [d(S\T) + g(T) + edge_cost * 1_{T != empty}].
```

Every selected word induces a root-to-terminal path, whose new-prefix cost is exactly the sum of its selected trie edges. A union of paths is a rooted subtree; the recurrence covers every partition across children and pays a shared edge once. Thus the recurrence is exact. Any pair or triple `S` with `d_root(S)>11` is a rigorous necessary-condition exclusion for all six labels, independent of the remaining choices.

The executed C++ program computes all six singleton, 15 pair, and 20 triple optimum values at each node, by descending node ID in the prefix-first trie. Original seven-key restriction is enforced by input generation, and the actual support bit mask encodes retained background edges exactly.

## Full enumeration results

|Profile|B=11 Q|Pair exclusion|New triple exclusion|Pair/triple survivors|
|:--|--:|--:|--:|--:|
|A|6,284|1,100|5,184|0|
|B|6,284|1,100|5,184|0|
|Both|12,568|2,200|10,368|0|

Both tries contain 42,735 nodes and 9,838 legal terminal words. The cases are all six-label combinations among 24 labels satisfying the stated removal and key condition. Counts are exact integer arithmetic; no floating point or approximation is involved in the proof (elapsed-time metadata is not a mathematical input).

## Reproduction and independent checks

Re-use the frozen predecessor `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py` and its EC49FGJ witness JSON. Run `python MAKE_INPUT_EC49FIN.py` to regenerate both `TRIE_*.txt` and `QS_*_11.txt`. Compile `g++ -O3 -std=c++17 VERIFY_EC49FIN.cpp -o ec49fin`. For each `X` in `A B`, run `./ec49fin TRIE_X.txt QS_X_11.txt 0`. Each output's first line must report `checked=6284`, `pair_excluded=1100`, `triple_new_excluded=5184`, `triple_survivors=0`.

The source generator was executed independently of earlier locally generated data and reproduced identical input SHA256 digests (see `EXACT_REPORT_EC49FIN.json`). A separate literal set-union enumeration, not using trie DP, checked the first 20 pair-surviving Q for each profile and found a three-demand minimum **12** for each; another independent subset-trie recurrence agreed with direct enumeration on eight small-candidate triples per profile. The local evidence archive includes actual source, full deterministic input lists, all execution chunks and their logs, independent verification programs, the predecessor frozen word/witness generator, and SHA256 manifest.

## Next research unit

Extend to B=13 fixed-key six-path cases (2,498 Q per profile). Also address the genuinely released/reallocated-key cases by extending the trie state to include complete key selection. This is an author-side exact finite result, pending independent Driver mathematical review and formal Result admission. It does not change P000, the frozen scientific input or an existing task claim.
