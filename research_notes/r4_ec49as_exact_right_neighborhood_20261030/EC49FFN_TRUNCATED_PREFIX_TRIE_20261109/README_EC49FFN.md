# EC49FFN — Exact three-microstep terminal truncation for native signed BRC prefix optimization

Date: 2026-11-09. Author-side analytic algorithm and exact finite audit. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source is the original six-operation, nine-state DFA, ordered native signed-X6 kernel in `../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/BRC_ORIGINAL_MODEL_EC49FFJ.py`, Git Blob `6350340fbe869f17b5a50bd1ba30640db44a3a99`.

## Exact terminal truncation theorem

For a fixed observation window h, a fixed admissible COMPLETE BRC key K, and four ordered operation words with terminal signatures 1,2,4,8, every word has the same native signed-X6 length L. Let P be the union of their nonempty signed native microstep prefixes, and let P_{<=L-3} retain only depths 1 through L-3.

The EC49FFM terminal-determinacy lemma proves that two such words of *different* low terminal signatures cannot have identical signed native prefixes of length L-3. Every selected witness therefore has its own, disjoint last THREE native edges. No one of these final three prefixes can equal another selected word's prefix at the same depth; different depths are distinct by construction.

Consequently, for **every** legal selected quadruple,

```text
|P| = |P_{<=L-3}| + 4*3 = |P_{<=L-3}| + 12.
```

The additive constant is independent of the four choices. Thus the global optimum over fixed (h,K) obeys the exact identity

```text
OPT_full_native_signed_prefix(h,K)
  = OPT_truncated_native_signed_prefix(h,K;depth<=L-3) + 12.
```

The truncated terminal nodes retain their original DFA colours 1,2,4,8; no path identity is forgotten in the original witness set. Reuse the proven EC49FFJ 16-mask exact rooted-trie DP on the shorter tree, adding 12 to its optimum. Recover each original operation word and fully expand and count its signed-X6 prefixes when returning a witness to the mother problem.

**Scope of safe compression:** this proves preservation of one-key, one-window, four-distinct-low-readout cost and feasibility at this fixed terminal horizon. If another future operation or another window/key is later added, do not reuse the truncated quotient without a new exact future-observer/fibre certificate. This is consistent with joint relation/observer-preservation rules.

## Exact computational audit

A standalone reproducible Python 3 implementation is `VERIFY_EC49FFN.py`. It imports the frozen EC49FFJ model and exact 16-mask merge algebra, reconstructs every legal complete key for h=2,...,9, constructs the truncated signed-X6 trie directly, and checks terminal colour collisions. All 200 legal keys and all 781,882 retained low-signature operation words were covered.

Rows: h=2: 1 key, 4 words, 17 truncated nodes, global best 28; h=3: 3 keys, 30 words, 145 nodes, best 34; h=4: 7 keys, 176 words, 923 nodes, best 32; h=5: 13 keys, 950 words, 5,133 nodes, best 36; h=6: 22 keys, 4,932 words, 26,974 nodes, best 40; h=7: 34 keys, 25,060 words, 137,722 nodes, best 44; h=8: 50 keys, 125,680 words, 692,144 nodes, best 48; h=9: 70 keys, 625,050 words, 3,445,408 nodes, best 52.

An additional full-model comparison (executed separately with the existing source solver and archived EC49FFJ/EC49FFK complete-key reports) matched **all 200 per-key exact optimum values**. Summing unique trie nodes per key over H2-H9, full signed tries had 6,654,112 nodes whereas truncated signed tries had 4,308,466: **2,345,646 fewer (35.25%)**. These counts measure materialized trie states in this specific finite enumeration, not CPU speedup, end-to-end complexity, or the multiwindow objective.

The complete 200-row report is stored without loss as gzip-base64 `EXACT_REPORT_EC49FFN.json.gz.b64`. Decode using `base64 -d | gzip -d` and compare with `VERIFY_EC49FFN.py` output. Original execution summary: `RUN_EC49FFN.txt`. Report text and checker are public project research material; no service credentials or platform/session keys are included.

## Reuse

This exact reduction removes terminal branching from every fixed-key trie instance without changing the EC49FFM cost optimum or its minimizing keys. The mother objective (`<=5` complete BRC keys and `<=93` distinct native signed prefixes across multiple windows) is still open, because cross-key sharing and observation constraints require separate treatment.

**Next science unit:** identify a certificate for safe terminal-subtree peeling over multiple full keys and multiple observation windows, including distinct native lengths and shared prefixes; test on a new feasible quota/observer pattern not already covered by earlier 22-24-path exclusions.

**Authority:** author-side proof, not independent Driver acceptance or native Source Result; P000 and ACTIVE worldview unchanged.
