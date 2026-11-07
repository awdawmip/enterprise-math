# EC49EXT — 173 further exact H8/M5/S≤6 signed-X6 BRC three-key-collision exclusions

**Research date:** 2026-11-03 Asia/Shanghai. **Status:** AUTHOR-SIDE EXACT FINITE CERTIFICATE / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED. **Predecessors:** EC49EXS, EC49EXR (Draft PR #1730). **Frozen scientific inputs:** Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (neither changed). P000 and ACTIVE worldview unchanged.

## Result EXT-1

In the frozen symbolic signed-native X6 seven-operation model, consider H=8 windows h=2,...,8, exactly M=5 distinct complete positive BRC keys, S≤6 nine-history transfer types and primitive signed prefix-edge cost E. Let `C` be the 946 three-window common-key schedules from EC49EXS with its certified per-depth lower bound below 80. For schedule x let `N(x)` denote the total number of all *eligible operation words* over its seven windows that realize the mandatory T4 (four) or T2 (two) observer signatures and its exact full six-component BRC positive-count key.

**Finite theorem.** For all x in C with `400 < N(x) ≤ 575`, the exact minimum prefix cost satisfies `E_min(x) ≥ 80`. The subset has **173** schedules. Together with EC49EXR's 92 schedules with `N(x)≤400`, all **265** x in C with `N(x)≤575` have this threshold certificate.

Proof uses the complete EC49EXJ signed-native generator: for each fixed x, enumerate all legitimate operation words, expand each to the original *ordered signed primitive X6 steps*, and store the terminal `(h,observation_signature)` coverage colors in a complete prefix trie. The h2 fixed four words `{ce,de,ec,ed}` require exactly 28 prepaid prefix edges. EC49EXJ's `EXACT_OR_MASK_DP.cpp` computes exact minimum additional costs using a subtree union-mask integer DP. Its cutoff 80 discards only states with additional cost ≥52; all subsequent edge costs are nonnegative. Every one of the 173 trees returned `BOUND_PASS minimum_total_at_least=80`. This is a finite exact proof for the declared subset, retaining full six native spatial coordinates in each original signed primitive axis label.

**Executed scope:** 173 cases ordered by (total eligible words, largest per-window eligible count, original EXS row index), with `N` from 409 to 575, trie nodes from 2,047 to 3,751, and 20/22/24 distinct coverage colors. The `EC49EXT_COMPACT_EXECUTED.json.gz.b64` file is a lossless gzip+base64 record containing `[EXS_row_index,eligible_word_count,trie_node_count,color_count,80]` for every actually checked case; for each row, the solver receipt is exactly `BOUND_PASS minimum_total_at_least=80 nodes=<trie_node_count> colors=<color_count>`. The complete locally executed per-case JSON (also including input SHA256) is available in the task's full evidence archive. The existing EC49EXJ generator/DP is reused unchanged.

**Updated frontier:** EC49EXS 946 triple-collision survivors minus 265 exact certificates = **681** triple-collision schedules. EC49EXS leaves 44,234 double-collision schedules; combined remaining **44,915**. The global optimum retains the previously proved `63≤E*≤80`, with an E=80 witness in EC49EXK.

## Reproduction and evidence

Use the pinned same-PR sibling files `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/{ANALYTIC_EC49EXJ.py,SCREEN_H5_EC49EXJ.py,EXACT_OR_MASK_DP.cpp}` and `EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH/EC49EXS_TRIPLE_CANDIDATES.tsv`. Run `python3 VERIFY_EC49EXT.py > reproduced.json` with Python 3 and g++ C++17. The verifier asserts the full 946-row candidate catalogue, checks the 92+173 word-count partition, rebuilds all 173 signed native prefix trees and requires exact `BOUND_PASS` receipts. It reuses the author-side generator and solver; a later independent Driver may review their completeness.

Decode the text-safe evidence file with `base64 -d | gzip -d`. SHA256 of decoded UTF-8 report: `0be9891c0f378721aeba4b506d88fe08f0d185b31a59548e8c482f6bf9f63263`; SHA256 of EXS input TSV: `847e83ed59209902076c1d22cdda176e30218bc8d0f573fbcc11a0e69ae67ca4`. Publication is author-side scientific storage, not native CLAIM/Result/Driver admission.

## Next precise question EC49EXU

Test `575 < N(x) ≤ 700` within the 681 remaining triple-collision schedules, respecting bounded exact solver time and recording each completed cutoff receipt. For difficult cases strengthen the necessary native prefix bound. Then move to 44,234 double-collision schedules. Any claimed E<80 witness must be checked for all mandatory nine-history signatures, five full keys and true signed-native trie cost.
