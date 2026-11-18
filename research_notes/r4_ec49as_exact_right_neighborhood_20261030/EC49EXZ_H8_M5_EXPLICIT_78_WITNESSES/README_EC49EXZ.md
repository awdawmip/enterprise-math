# EC49EXZ — Explicit 78-edge native signed BRC witnesses for H8/M5/S<=6

**Research date:** 2026-11-04. **Status:** AUTHOR_EXPLICIT_CONSTRUCTION / INDEPENDENT_EXACT_OBSERVER_AND_PREFIX_VERIFICATION_PASS / AUTHOR_INTEGER_DP_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Parent: EC49EXY at immutable `a3fd0ca831e5974204288f8e1b44129088acbd9f`, existing Draft PR #1730. Frozen scientific pins: Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, EM `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral rules are read separately; P000/ACTIVE Heartbeat World unchanged.

## Result: improved **constructive upper bound**

In the existing finite seven-operation model, let `E` be the number of distinct **nonempty ordered signed primitive-X6 prefixes** across all seven horizons h=2..8. Require each horizon's words to have total signed displacement `(+2,0,0,0,0,0)`, one complete six-axis positive-step key, and a nine-history observer of full rational rank nine. Let `M` be the number of distinct complete keys and `S` the total number of distinct transfer signatures. Then two explicit legal constructions prove

`E*(H8, M5, S<=6) <= 78 < 80.`

The previously published global lower bound remains `E*>=63`. Thus the current proven interval is **63 <= E* <= 78**. A finite schedule's exact minimum is not asserted to be the global optimum.

The two witnesses' complete operation words are in `EC49EXZ_EXPLICIT_WITNESSES.json`. They require only the original primitive signed-axis operations `a,b,c,d,e,f,g`. Their seven-horizon key schedules are:
- EXZ-A: (3,1,1), (3,1,1), (3,3,1), (3,3,1), (3,4,1), (3,5,1), (3,6,1);
- EXZ-B: (3,1,1), (3,1,1), (5,1,1), (5,1,1), (6,1,1), (7,1,1), (8,1,1).

Each key implicitly extends to the full native six-axis key `(u,v,w,0,0,0)`; these are restricted supports *inside* X6, not a replacement for the six-axis universe. In both witnesses, the cumulative distinct signed primitive prefixes at horizons h=2..8 are exactly `(28,42,58,66,70,74,78)`.

## Exact proof by concrete construction

Define the signed primitive expansions `a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`. The signs denote signed native axis indices, not ordinary 2D coordinates. For each listed word, expanding every operation into its signed steps and counting positive occurrences yields precisely its declared six-component key; counting signed net occurrences yields `(+2,0,0,0,0,0)`. All horizon-h words contain exactly h operation letters.

For each horizon, compute each candidate's complete nine-history five-bucket transfer signature as the base-five integer of the nine bucket outputs. The required frozen minimal observer family is T4=`{1836687,1867942,1872656,1873981}` where r=u+v-h-1>=1, else T2=`{1836425,1866380}`. Both explicit witnesses contain each required signature exactly once per horizon. The exact rank test constructs the 9-by-(5*|T|) integer matrix `A[j,(s,b)] = 1` iff history j under signature s reaches bucket b. Rational Gaussian elimination gives **rank 9 at every horizon**. The union of distinct transfer signatures over the full run is precisely T4 union T2: S=6. Exactly five distinct full BRC keys occur.

Finally, form every nonempty signed-prefix tuple of each selected primitive path; the union has 78 elements. The h2 core `ce,de,ec,ed` already has 28 elements; the staged counts displayed above are checked independently from the explicit words. This is an exact constructive upper-bound proof, requiring neither numerical approximation nor solver completeness.

## Additional exact finite DP evidence

EC49EXY enumerated **12,356** lower-bound survivor double-collision schedules. A reproducible first batch ranks schedules by total eligible frozen native word count (ties: descending EXY bound, then stable original source order). The first 200 schedules were actually run through the unchanged EC49EXJ exact OR-mask prefix-trie DP with integer cutoff 80. **198** returned `BOUND_PASS minimum_total_at_least=80`; the two source-ranked cases 14 and 15 returned `PASS min_extra=50 total=78 nodes=617 colors=18`. A separate traceback implementation recovered their 18 specific words, and the standalone exact verifier rechecked rank, six-axis keys, net displacement and complete prefix unions. Original DP input SHA256 identifiers for the two cases are included in the witness JSON. The complete population, ordering, original frozen generator and exact solver are reusable through `REPRO_EC49EXZ_BATCH.py` and its sibling EC49EXJ/EXY source files.

The exact DP recurrence is `DP_v[mask]`, the minimum number of unprepaid edges in the node v subtree needed to realize observer mask; combine child masks by OR and add one for an active child edge absent from the h2 prepaid base. Cutoff discards only costs >=52 extra, which cannot later decrease. The two root results 50 extra give the exact minimum 78 for **their fixed schedules**; the concrete word lists provide a separate direct validity witness regardless of any DP calculation.

## Verification and provenance

Run `python3 VERIFY_EC49EXZ_INDEPENDENT.py` from this directory (Python stdlib only). It reconstructs paths, full keys, T2/T4 signatures, each nine-history rational rank, and exact signed primitive prefix cost **without importing the original generator or DP solver**. To replay the batch, compile the existing sibling `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/EXACT_OR_MASK_DP.cpp` as `exact_or_mask_dp`; run `python3 REPRO_EC49EXZ_BATCH.py /path/to/exact_or_mask_dp 200` from this directory. The latter needs the already published EC49EXY complete survivor TSV and frozen EC49EXJ generator. Frozen inputs and task authority are preserved.

**Next EC49FAA:** now optimize the *global* minimum below the newly established 78 upper bound, scanning the remaining 12,156 schedules not excluded/resolved by the first 200 exact case tests. Establish a feasible E<78 construction, or exact cutoff-78 exclusion; use observer-preserving suffix sharing and prefix-DP deduplication. A candidate may have E=78; a failure at cutoff 78 excludes only E<78, not equality. Preserve case IDs, native paths, timeout status and per-case reproducibility; do not infer an 78-edge global lower bound from the two fixed-schedule minima.

**Authority:** Published as author-side portable research in the existing PR; GitHub identity does not grant Source-native CLAIM or Driver admission. At this run, the Enterprise Math Sites connection reports `research_authority_granted=false` and owner listing returned `CONTROL_QUOTA`. No canonical Source CLAIM/Result or independent mathematical review is asserted.
