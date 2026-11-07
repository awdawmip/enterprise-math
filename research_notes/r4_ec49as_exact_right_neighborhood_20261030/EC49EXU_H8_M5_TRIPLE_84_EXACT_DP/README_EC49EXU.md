# EC49EXU — 84 additional exact signed-native H8/M5/S≤6 BRC triple-collision exclusions

**Research date:** 2026-11-03 Asia/Shanghai. **Status:** AUTHOR-SIDE EXACT FINITE THRESHOLD CERTIFICATES / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED. **Predecessor:** EC49EXT in Draft PR #1730. **Frozen scientific pins:** Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE worldview unchanged.

## Precise theorem U1 and scope

Work in the frozen EC49EXJ symbolic model: seven legal operation encodings, ordered signed native six-axis primitive steps, complete six-component positive BRC cache keys, nine-history observer signatures, windows h=2,...,8, exactly five distinct full BRC keys, no more than six observer-transfer types, and E equal to the number of distinct edges in the union of the selected original signed-step prefixes.

Let C denote the **946** three-window common-key schedules surviving the verified EC49EXS necessary bound. For each x in C, let N(x) be the total count of eligible original operation words satisfying its per-window complete BRC key and required T4/T2 observation signature. EC49EXR and EC49EXT have exact threshold certificates for all **265** schedules in C with N≤575.

This unit enumerated all **102** schedules in C with 575<N≤700, built each signed-native candidate trie, and completed a cutoff-80 exact integer subset-OR calculation for **84** schedules. For each of those 84 schedules x,

\[
\boxed{E_{\min}(x)\ge80.}
\]

The 84 indices are exactly the P rows in `EC49EXU_RECEIPTS.txt`, indexed by the original EC49EXS 946-row TSV (zero-based index). All 18 T rows have actual candidate tries and word counts, but their exact integer solver run exceeded the bounded per-case runtime; they remain **unresolved**.

## Exact finite proof

1. Use the original, ordered, signed X6 operation expansion and nine-history signature evaluator from sibling `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/SCREEN_H5_EC49EXJ.py`. Generate all eligible operation words for each schedule in `EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH/EC49EXS_TRIPLE_CANDIDATES.tsv`. The size-sorted catalogue has exactly 946 entries; 265 have N≤575, and exactly 102 satisfy 575<N≤700. Every executed instance regenerates its full trie and checks N against the catalogue count and each of seven per-window word counts.
2. Every trie terminal carries its precise `(h,signature)` coverage bit. The four mandatory h2 words `ce,de,ec,ed` contribute 28 pre-paid signed-native prefix edges. All remaining trie edges have nonnegative integer costs, 1 when used and 0 when already pre-paid. There are 20, 22 or 24 required coverage colors for these instances.
3. At each trie node v, the original EC49EXJ `EXACT_OR_MASK_DP.cpp` computes a map of reachable coverage bitmasks to the smallest extra-edge cost, combining child subtrees by OR and addition. A nonempty child selection adds the child's incoming edge cost; the terminal color may be selected at zero local cost. This is an exact subtree induction because each child subtree shares no further edges with any other child.
4. Run at full-cost cutoff E<80, i.e. extra edge cost <52, pruning any partial cost at least 52 (all future increments nonnegative). When no full coverage mask is reachable after this pruning, `BOUND_PASS minimum_total_at_least=80` is a sound and complete *threshold exclusion* for that particular full candidate universe.
5. The 84 P rows returned precisely that certificate. The 18 T rows are identified by index and time limit; no mathematical lower-bound improvement is claimed for those rows. This proof preserves the whole signed primitive sequence (not a projected coordinate histogram) and all full BRC key/observer-fiber conditions.

## Executed evidence and reproduction

`EC49EXU_RECEIPTS.txt` contains **all 102** per-instance index, eligible-word count, trie node count, required color count and actual solver status. P stands for the exact source solver's output `BOUND_PASS minimum_total_at_least=80 nodes=<nodes> colors=<colors>`; T means time limit reached. Reproduction program `VERIFY_EC49EXU.py` references the *unchanged* sibling EC49EXJ generator/DP and EC49EXT catalogue; no ad hoc shortening of the signed-native word model is used.

Actual executed machine environment: Python 3, g++ C++17 `-O3`, bounded subprocess per-case cutoff of 80, case timeout 3–8 seconds (different bounded batches, reported as such rather than as a uniform 8 seconds). Complete local JSONL contains per-instance input SHA256, solver stdout, subprocess status, durations and errors: SHA256 `32dd7cf541f9616b2c598a8a41259c2b051ed919581d30c0ccd9fb12c7310222`. Compact receipt TSV SHA256 `56f92bb2bd1b8903ecc1f2a6fa12ea916f8ad502e6e2158f7b72b1d7084ba3c3`. Scope is author-side reproducible finite computation; independent Driver review is pending.

**Frontier update:** EC49EXT left 681 three-collision plus 44,234 double-collision schedules. This run disjointly excludes 84 additional triple schedules, giving **597 triple + 44,234 double = 44,831** not-yet-excluded schedules. Within the 597 triple schedules, 18 have N in (575,700] but timed out, and 579 have N>700. The global proved bound stays `63≤E*≤80`, with E=80 signed-native construction from EC49EXK.

## Open next unit EC49EXV

Focus first on the **18 timeout cases** using a stronger exact branch/observer-compatible lower bound or improved exact OR-mask DP state dominance, retaining the cutoff and mandatory color semantics; every completed exclusion must carry a verifiable receipt. In parallel test an independently chosen small subset of the 579 triple cases with N>700, and then the 44,234 double-collision cases. Do not infer impossibility from timeout or extend local certificates beyond their fixed instances. Native Owner/CLAIM/Result/Driver rights require actual authenticated current authority; GitHub source storage is author-side and does not confer them.
