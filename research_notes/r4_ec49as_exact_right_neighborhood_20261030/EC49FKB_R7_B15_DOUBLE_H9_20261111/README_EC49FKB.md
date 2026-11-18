# EC49FKB — Radius-seven retained-key B=15 double-H9 exact obstruction (2026-11-11)

**Research status:** author-side exact finite calculation; two local implementations executed; independent Driver mathematical review pending.  
**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.  
**Continuation:** EC49FKA (B=14) at `fd0effc4810bb0569fd315b2e980493afb3dc68f`.  
**Model:** nine-state BRC generator, full raw keys, signed ordered native-X6 microstep prefixes, two frozen seven-key/94-prefix witnesses A and B.

## Exact local theorem

For either profile A or B, choose a seven-position replacement set `Q` among the 24 labeled witness words, fixing the remaining seventeen original operation words. Let `F(Q)` be the full literal nonempty signed-prefix union of the fixed words. The original seven words use exactly seven complete raw cache keys.

Among the `C(24,7)=346104` choices per profile, precisely 4336 retain the seven raw keys and have `|F(Q)|=78` (hence the hypothetical 93-prefix incremental budget is `B=15`). These yield 67 distinct fixed-prefix backgrounds. **Exactly one background per profile occurs for 1762 different Q.** Every one of those Q omits the two observation demands `(window=9, signature=16)` and `(window=9, signature=32)`.

For that common fixed-prefix background `F`, define `D(w)=P(w)\\F`, with `P(w)` the literal ordered/signed native microstep prefixes. Since all seven raw keys are already used by the fixed seventeen words, every permitted completion word must use one of those keys. The frozen 178850-word legal catalogue contains 280 words per missing H9 label using those keys. Exactly 35 words per label have `|D(w)|<=15`.

The exact pairwise finite enumeration of the `35 * 35 = 1225` qualifying pairs gives

```text
min_{w16,w32} |D(w16) union D(w32)| = 16.
```

Thus any purported seven-word completion of total cost at most 93 would, in particular, include both H9 labels with at most 15 new prefixes, contradicting this exact bound. The frozen original witness is itself a valid 94-prefix completion for every Q. Therefore **all 1762 positions per profile, 3524 distinct labeled fixed-background subproblems in total, have exact optimum 94**.

This is a new finite local optimum under the pinned generator; it is not a proof that the unrestricted seven-key mother problem has global minimum 94.

## Executed cross-check and numerical witnesses

| Item | Profile A | Profile B |
| --- | ---: | ---: |
| All seven-position choices | 346104 | 346104 |
| Retained-key B15 contexts | 4336 | 4336 |
| Different B15 prefix backgrounds | 67 | 67 |
| Contexts in common double-H9 background | 1762 | 1762 |
| Fixed prefixes | 78 | 78 |
| Eligible H9 words per label | 35 | 35 |
| Enumerated pair candidates | 1225 | 1225 |
| Exact minimum joint new prefixes | 16 | 16 |
| **Exact total optimum** | **94** | **94** |

An example omitted Q is `(2,4,5,6,7,22,23)` (zero-based positions of the sorted 24 demand words). A minimum-16-prefix H9 pair is `fegfgffgg` with `gefgfffgg` for A, and `fegfgffgg` with `geffgffgg` for B.

Two locally executed verifiers agreed: the source-based prefix-set enumeration `EC49FKB_B15_SHARED_H9_EXACT.py` and an independently implemented signed-prefix/complete-key parser `EC49FKB_B15_H9_DIRECT_CHECK.py` reading the existing frozen TSV catalogue. Both printed a `3524_PASS` sentinel. The adjacent published `VERIFY_EC49FKB.py` is a **third executed portable reproduction**, using the frozen generator but an independently coded literal signed-prefix and complete-key builder. Its actual local output was `EC49FKB_B15_H9_EXACT_3524_PASS`; its precise counts and witness words are also in `EXACT_RESULT_EC49FKB.json`.

## Complete rerun inputs and instructions

The published portable verifier reads the original source files already in this PR under sibling directory `EC49FJD_RELEASE_B11_COMPLETE_20261111/`: `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`. From this directory run `python VERIFY_EC49FKB.py` in Python 3.10+; no external package is required. Full word enumeration, full Q enumeration, admissible key filtering and exact H9 pair unions occur inside the script. An optional `EC49FKB_INPUT_DIR` is supported for a separate exact frozen-input checkout. The input generator and witness blobs in this PR are `e3663682afe80bdcbbc90c442cb2daaccc0dee66` and `6e54f83f9d39bf932d7f36addf4b1987ca88b077`, respectively.

**Precisely open B15 scope:** `(4336 - 1762) * 2 = 5148` other retained-key seven-path contexts remain outside this particular certificate. Earlier subset-obstruction exploration suggests additional reducible background classes but has not been promoted into this theorem. Next choose a remaining B15 background and prove a 4–7-label union obstruction or perform complete exact trie optimization; then examine released-key seven-path contexts and the independent unrestricted 93-prefix construction route. Preserve the exact frozen observation semantics and the original seven-key constraint.

**Authority:** no current immutable EC49AS task publication was found by the native task query on 2026-11-11. Material is stored as GitHub author evidence on the existing Draft PR; it is not a formal CLAIM/Result/independent Driver admission. P000/ACTIVE worldview unchanged.
