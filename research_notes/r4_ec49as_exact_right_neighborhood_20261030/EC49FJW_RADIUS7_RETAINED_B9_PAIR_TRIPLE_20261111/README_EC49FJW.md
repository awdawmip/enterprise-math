# EC49FJW — exact radius-seven retained-key B=9 classification by two-/three-demand native-prefix certificates

**Date:** 2026-11-11. **Frozen BRC scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** author-side finite exact computation/proof, not independently Driver-reviewed, not an admitted Result. This is a strict continuation of EC49FJU–FJV in Draft PR #1730.

## Mathematical statement

Use the two pinned EC49FGJ witnesses A and B, each consisting of 24 *distinct labeled* observation demands ((h,sigma)), 24 legal nine-state BRC words, exactly seven original **complete raw cache keys**, and 94 distinct **literal signed ordered native X6 microstep prefixes**. For every seven-element subset (Q) of the 24 original labeled positions, preserve the other 17 original words unchanged. Let (F(Q)) be the prefix union of these 17 words and (K_F) their complete raw cache-key set.

This theorem concerns precisely the cases where (i) (K_F) already equals the original seven complete keys, and (ii) (|F(Q)|=84), equivalently the 93-prefix target has an additional-prefix budget (B(Q)=9). There are **17,424** such cases per witness, organized into exactly **24** different fixed-prefix backgrounds. **Every one has exact optimal total prefix cost 94, even when the seven omitted words are replaced by arbitrary legal BRC words from the entire frozen native-word catalog subject to the original full-key budget.** Thus **34,848 new fixed-background subproblems** across witnesses A/B are closed.

| Per witness | A | B |
|---|---:|---:|
| Radius-seven cases with fixed 17 still retaining all seven keys and (B=9) | 17,424 | 17,424 |
| Exact two-demand obstructions | 16,776 | 16,776 |
| Further exact three-demand obstructions (disjoint from pairs) | 648 | 648 |
| Remaining in this B=9 class | **0** | **0** |
| Certified minimum total prefixes | **94** | **94** |

Combining this new, disjoint B=9 class with the previously saved 72,136 retained-key certificates per witness from EC49FJV yields **89,560** exact local 94-prefix certificates per witness (**179,120** across both). Of the 153,408 seven-position retained-key cases per witness, **63,848** remain unclassified. Another 192,696 seven-position cases per witness release at least one original key and are a separate key-selection problem.

## Why two/three demands certify all seven

Write (P(w)) for the complete literal signed native-prefix set of a legal word (w). For fixed prefix-closed (F) and one demand label (ell), form
[
 A_F(ell,B) = {,P(w)\setminus F : w 	ext{ is legal}, operatorname{key}(w)in K_F, wmodelsell, |P(w)\setminus F|le B,}.
]
Every seven-word completion with at most (B=9) additional prefixes necessarily supplies one member of this finite family for every omitted label. All other legal words have >9 individual added prefixes and cannot participate in such a completion.

For any two or three omitted distinct labels (ell_1,ldots,ell_t), compute the complete exact disjoint-demand union obstruction:
[
min_{A_iin A_F(ell_i,9)}
  igl|A_1cupcdotscup A_tigr| > 9,qquad tin{2,3}.
]
If this holds for *one* pair/triple, no assignment to the remaining omitted labels can satisfy the 93-prefix target. The fixed 17 already use seven full key identities; a legal seven-key solution cannot introduce an eighth. The original omitted seven legal words give a feasible cost of 94, so the optimal cost is exactly 94. These claims refer to the full frozen BRC legal catalog, not a selected witness-only subcatalog.

A set-inclusion antichain is an exact speedup: for one demand, if (Asubseteq A'), replacing (A') with (A) cannot raise the size of its union with any later candidate. After union of two demand families, the same antichain reduction preserves whether an at-most-nine union exists. For all 17,424 cases, the two-demand screen gives 16,776 exclusions per witness; the remaining 648 per witness all have a violating triple. All 648 triple certificates per witness arise from 12 fixed-prefix-background classes of 54 contexts each. The complete count includes every one of the ({24choose7}=346104) labeled-seven-position subsets, filtered by exact raw-key retention and (|F|=84); no random search is used.

**Subtle proof-scope point:** candidate pair/triple unions are evaluated after the individually >9 alternatives have been discarded. A recorded candidate-union cost of 10 or 11 means **the at-most-nine completion is impossible**, not that the unrestricted two-/three-demand optimum exceeds 10. The *full seven-demand* optimum equals 10 additional prefixes by the original 94-edge witness.

## Exact execution and independent audit

Reused the pinned EC49FGW nine-state typed BRC generator and immutable EC49FGJ witness JSON. The legal catalog is **178,850** BRC words on 94 raw complete keys; filtering by each witness's original seven keys retains **9,838** words. Prefixes are native ordered signed X6 microsteps, encoded injectively as bytes ((d+4)) for signed axis (d), not displaced endpoints or unsigned multisets. The only numerical operations used for this BRC model computation are finite exact word enumeration, set union, bitmask/inclusion tests and integer counting.

Executed `EC49FJW_RADIUS7_B9_PAIR.py` for the complete case partition and pair certificate, then `EC49FJW_RADIUS7_B9_TRIPLE.py` for all 1,296 remaining cases across A/B. A separately written direct literal signed-prefix word-enumeration checker `EC49FJW_DIRECT_CROSSCHECK.py`, without the antichain or profile-support optimization, verified **192 cases**: 48 pair obstructions and 48 triple obstructions for each profile. The complete reports, actual scripts, frozen source inputs and execution logs are in `EC49FJW_COMPLETE_EVIDENCE.tar.xz.b64`, a base64-encoded xz tarball. All source files have a SHA256 manifest in `EC49FJW_SUMMARY.json` inside the archive.

Reproduce with:
```bash
base64 -d EC49FJW_COMPLETE_EVIDENCE.tar.xz.b64 > EC49FJW_COMPLETE_EVIDENCE.tar.xz
tar -xJf EC49FJW_COMPLETE_EVIDENCE.tar.xz
cd EC49FJW_R7_B9
python EC49FJW_RADIUS7_B9_PAIR.py
python EC49FJW_RADIUS7_B9_TRIPLE.py
python EC49FJW_DIRECT_CROSSCHECK.py
```

Archive byte SHA256: `661a71e0f749fd2c7e4914ea14e0aaa43cf30d646e9a652186e25d2650a856bb`; decompressed contents include case-complete reports and real execution logs. Freeze-pinned inputs are unchanged. This new result does **not** prove the global seven-key minimum (C_{\min}(7)=94).

**Next mathematics:** take the unclassified retained-key radius-seven (B=11) class (15,736 per witness in EC49FJU), run pair/triple screens then seven-demand native-trie DP; separately study the 192,696 key-releasing seven-position contexts per witness via full-key-selection-aware DP; independently search for any globally valid 93-prefix construction.

**Authority:** no active EC49AS task CLAIM or Driver mathematical admission asserted; native session/owner queries are tracked separately, and ordinary GitHub author-side publication is not a formal Result.
