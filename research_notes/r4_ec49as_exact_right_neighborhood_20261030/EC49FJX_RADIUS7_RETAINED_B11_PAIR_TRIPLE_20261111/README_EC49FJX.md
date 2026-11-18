# EC49FJX — Exact native BRC radius-seven B=11 pair/triple classification

Date: **2026-11-11**. Frozen scientific input: **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. Scientific status: **author-side finite exact theorem; independent mathematical Driver review and formal Result admission pending**. Strict continuation of EC49FJU–FJW in PR #1730.

## Theorem: 31,472 new sharp 94-prefix local optima

Fix either EC49FGJ seven-complete-key, 94-distinct-native-prefix BRC witness profile A or B. Each witness has 24 distinct labeled BRC observation demands with valid nine-state operation words. Choose seven distinct labeled positions Q, keep the other 17 original operation words fixed, and replace the seven chosen words by any seven full-catalog legal words respecting the original demands and at-most-seven *complete raw cache-key identities*.

Consider exactly those Q satisfying (i) the 17 fixed words already use all original seven raw key identities and (ii) their union F(Q) consists of 82 literal *ordered and signed native-X6 microstep prefixes*. Thus reaching 93 total prefixes permits **at most 11 newly added prefixes**, denoted B(Q)=11.

There are **15,736** such Q for A and separately **15,736** for B, distributed over **36** different fixed-prefix background classes per witness. The following exact classification exhausts them:

| Disjoint certificate class | A | B |
| :-- | --: | --: |
| Pair-of-demand union impossibility at budget 11 | 2,640 | 2,640 |
| Additional triple-of-demand union impossibility at budget 11 | 13,096 | 13,096 |
| Surviving B=11 fixed-background Q | **0** | **0** |
| **New exact local optima 94** | **15,736** | **15,736** |

Therefore **31,472 new finite local 94-prefix optima** are established across A and B. Adding the earlier disjoint EC49FJU–FJW classes gives **105,296** certified retained-key seven-replacement Q per witness (**210,592 combined**), with **48,112** retained-key cases per witness still open. Independently, **192,696** seven-position cases per witness release at least one old key and require complete-key selection.

## Complete finite necessary-condition proof

For a legal signed ordered BRC word w, P(w) is the exact set of nonempty native-X6 signed microstep prefixes. For each original fixed-background F, for every omitted label ell, and for B=11, enumerate **every** frozen legal word satisfying ell and using one of the seven already-occupied raw full keys. Retain its incremental prefix set A = P(w) minus F only when |A| <= 11. Thus each label gets a finite complete family A_F(ell,11).

If there existed a seven-word completion with total prefix cost at most 93, each omitted label would necessarily choose a member of its A_F(ell,11); its seven incremental prefix sets would have union size at most 11. Consequently for **every** subset of the seven labels, the minimum union size over the corresponding eligible candidate families would be <=11.

Contraposition: if even one pair or one triple of omitted labels has **no** eligible union with size <=11, the seven-label completion cannot achieve 93. This is an exact necessary condition: each word omitted from A_F individually introduces more than the total remaining budget and is therefore irrelevant to any counterexample.

The algorithm computes pair and triple unions of the *complete* filtered candidate families, compressing via only one rigorous domination rule: if A is a subset of A', A' can be omitted from a minimum-union search for any future label, because for any further set S, |A union S| <= |A' union S|. The antichain reduction does not merge ordered native paths into endpoints or identify distinct full cache keys.

Each witness has 36 distinct B=11 prefix-background classes. For 4 classes of 660 contexts each, the pair screen finds a violating pair for **2,640** contexts. The other **13,096** contexts fall in the remaining 32 classes; the triple screen processes all, finds a violating triple in every case, and leaves zero survivors. Every raw complete cache key is preserved by the 17 fixed words, so no eighth key may be introduced. Original EC49FGJ witness words provide a 94-prefix completion for each Q. Hence the sharp optimum for each target Q equals 94.

**Scope nuance:** a minimum **after removing candidate words that individually cost >11** is an obstruction threshold test, not necessarily the unrestricted pair/triple minimum. The proof establishes the impossibility of **<=11** additional prefixes and uses the existing 12-added-prefix original witness for the exact optimum; it does not assert an unrestricted pair minimum of 12/13.

## Actual execution and portable reproduction

Exact signed nine-state BRC input: 178,850 legal words with 94 complete raw cache keys, of which 9,838 have one witness's seven allowed key identities. Input generator and immutable A/B witness JSON come from the prior EC49FGW and EC49FGJ evidence on this same Draft PR. No classical trigonometric or non-BRC propagation model was used; these are exact finite set, word and bitmask operations on typed BRC words.

Three actual executed scripts published here:

1. **EC49FJX_RADIUS7_B11_PAIR.py** — all retained-key seven-subset positions, exact 36 B11 groups, pair obstructions and the 13,096 remaining Q per witness.
2. **EC49FJX_RADIUS7_B11_TRIPLE.py** — full triple antichain search for **all** pair survivors under B11, returning zero triple survivors.
3. **EC49FJX_DIRECT_CROSSCHECK.py** — separately written literal signed-step word enumeration without antichain or profile-support optimization, checking 128 certificates: 16 pair and 48 triple cases in each of A and B. All pass.

Reproduce by placing **EC49FGW_RADIUS5_SCREEN.py** and **EC49FGJ_SEVEN_KEY_94_WITNESSES.json** from sibling **EC49FGW_RADIUS5_EXACT_SCREENS_20261110/** into an **EC49FJR/** directory beside these three scripts (or expose that source directory on PYTHONPATH). Run the three scripts in the order above with Python 3. They write the full case reports: EC49FJX_B11_PAIR_REPORT.json, EC49FJX_B11_TRIPLE_REPORT.json, EC49FJX_DIRECT_CHECK_REPORT.json. The GitHub **EXACT_SUMMARY_EC49FJX.json** gives SHA256 for all three actual scripts, frozen inputs, complete original reports and logs.

The complete original author evidence, 4,472,343-byte pair report, 12,858,339-byte triple report, 54,127-byte direct check report, source inputs, logs and hash ledger are in the **separately delivered conversation archive** EC49FJX_R7_B11_31472_COMPLETE_EVIDENCE_20261111.tar.xz. Archive length **93,824 bytes**, SHA256 **ff1c9951a1f5a13d6b02515525f694a2f31f5a50bc3688e07f12eecb966829c8**. The tar archive and all internally listed SHA256 values were locally read back and matched. **This large evidence archive is a conversation attachment, not a Github file; the exact scripts on GitHub regenerate its reports.**

## Unresolved scope and authority

The mother objective remains determining whether the **global** seven-full-key BRC optimum is 94 or whether any 93-prefix construction exists. The present theorem fixes 17 of 24 original words and only addresses the B11 retained-key seven-replacement class. Next: retained-key B12 class (8,020 per witness in EC49FJU), the 48,112 remaining retained-key Q per witness, and key-releasing Q through key-aware trie optimization. Continue independent constructive 93-prefix search.

Native session and formal TASK/CLAIM status must be established by actual current service receipts; ordinary author-side GitHub commits and a PR comment **do not** create a formal Result or mathematical admission.
