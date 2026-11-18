# X6 Unit124 — exact triadic-block versus signed-native shortest BRC interface

**Research date:** 2026-11-18. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; author `EM-X6-FB6990`, logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`. **Status:** AUTHOR-PROVED / EXACT FINITE PYTHON EXECUTED / UNREVIEWED / NOT_ADMITTED. The R063 six-blob 512-case C3/C4 native benchmark has not been re-executed here.

## Actual source and precise consumer

Read the current-main `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py`, Git blob `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`. Lines 8–16 select 20 underlying axis triples and 160 signed event types. Lines 19–35 define the number `U(D)` of **ordered three-distinct-axis macro-event sequences**. Lines 91–95 derive the signed event-incidence count `U(D) prod_i C(D_i,d_(i,+))`. The original source and `research_notes/X6_SIGNED_TRIADIC_DECOMPOSITION_BRC_V2_20260906.md` are correctly explicit about their macro-event/Path-formal meaning; the latter's section 7 names an additional atomic Cell-path layer without a universal counting equality to native shortest-path BRC.

The present unit supplies that missing *typed comparison* for a declared, independently inspectable micro-expansion; it does not reinterpret the original macro counts as native endpoint BRC. Scientific premises remain P000 V5 and the signed `Z^6` primitive spatial steps pinned at `59538f585d037d09ef687b28715c4bc1a3f9fe03`, with historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. No claim is made that every order of the three steps inside a physical triadic force event is dynamically admissible: this is a *free 3!-order signed spatial-word expansion* of that event alphabet, a separately typed combinatorial interface.

## Theorem: exact full-native shortest-word coverage

Fix a six-component unsigned incidence vector `D in N_0^6` with `sum D_i=3m`, `0<=D_i<=m`, and let each underlying triad event select three **distinct** named axes. Assume sign coherence: every occurrence of a given axis has the same native spatial sign. Expand each ordered triad event into any of the six permutations of its three signed unit steps, keeping its event's three steps contiguous, and concatenate the `m` events. The resulting words are genuine native shortest words for the signed endpoint displacement.

Let `U(D)` be the actual current-source macro-event count, `T(D)` be the number of these expanded, block-constrained primitive words, and `B(D)` the total native shortest N-BRC word multiplicity. Then for every `m>=0`,

```
T(D) = 6^m U(D),
B(D) = (3m)! / prod_i D_i!,
0 <= T(D) <= B(D).
```

For any feasible `D`, equality `T(D)=B(D)` holds **if and only if** `max_i D_i<=1`. In particular, nonempty equality cases occur only at `m=1` and `m=2`; at `m=2`, equality is the unique degree vector `D=(1,1,1,1,1,1)`.

**Proof of formula and injectivity:** an ordered macro-event sequence has six distinct spatial micro-orders per triad. Every resulting primitive word is recoverable as exactly those consecutive three-letter blocks and, within each block, its named underlying triple; hence two choices never collapse to the same word. Sign coherence makes the total length `3m=sum_i |delta_i|`, precisely the signed-native shortest word length. The usual multinomial count of all such shortest words gives `B(D)`.

**Proof of equality criterion:** if `max_i D_i<=1`, all primitive letters have distinct axes globally, so **every** shortest word automatically has three distinct axes in each consecutive length-three block. Conversely if some `D_i>=2`, the native shortest word beginning with two copies of axis `i` is valid and cannot be represented by any triadic block with distinct underlying axes. Therefore `T(D)<B(D)`. The zero case is the empty word, with `T=B=1`.

An explicit quantitative strictness bound holds for `m>=1`:

```
T(D)/B(D) <= 1 - [sum_i D_i(D_i-1)] / [(3m)(3m-1)].
```

Indeed, under the uniform distribution on all native shortest words, the disjoint events that the *first two positions* have the same axis have combined probability exactly the subtracted rational term. Each such word violates the first triadic block constraint. This bound is exact arithmetic; it need not be attained.

## Native-BRC counterexamples at the actual consumer boundary

- `m=2, D=(1,1,1,1,1,1)`: `U(D)=20`, `T=20*36=720`, `B=6!=720`. Full coverage holds at the unique nontrivial two-triad all-distinct configuration.
- `m=2, D=(2,2,2,0,0,0)`: `U(D)=1`, `T=36`, `B=6!/(2!)^3=90`, **coverage `2/5`**. The other 54 native shortest paths interleave axes across event-block boundaries.
- `m=3, D=(3,3,3,0,0,0)`: `U(D)=1`, `T=216`, `B=9!/(3!)^3=1680`, coverage `9/70`.
- `m=3, D=(2,2,2,1,1,1)`: `U(D)=93`, `T=20,088`, `B=45,360`, coverage `31/70`.

**Opposite-sign provenance case:** for `d_(0,+)=d_(0,-)=1`, `d_(1,+)=d_(2,+)=2` and all other signed degrees zero, the macro signed count is `U(2,2,2,0,0,0)*C(2,1)=2`; its free triadic-block expansion has `2*6^2=72` length-six primitive words. Their net displacement is `(0,2,2,0,0,0)`, shortest native length **4**, native shortest N-BRC count **6**. Thus exactly **zero** of these 72 length-six block words is a shortest native word. The natural counts count different path populations and must not be subtracted to fabricate a signed N-BRC cancellation.

## Actually executed exact certificate

The independent self-contained Python checker `research_checks/X6_UNIT124_TRIADIC_BLOCK_VS_NATIVE_BRC_20261118.py` was executed under CPython ordinary, `-O` and `-OO`. All three completed with exit 0 and byte-identical UTF-8 JSON; their actual stdout SHA256 is `c1dd74b24bf7e11f3b16bea05323c54687b835731de920b8026c27f5e1d3ae7a`. The program uses always-on explicit mathematical checks, not optimized-away `assert`.

Finite coverage: exact DP over all feasible six-axis degree vectors for `m=0,1,2,3` (respectively **1,20,141,580** vectors), verifying `T<=B`, the equality classification and rational collision bound. Among the `m=2` vectors **140** are strict, and all **580** `m=3` vectors are strict. An independent enumerator traversed **all distinct primitive words** for each of the 141 `m=2` configurations and all four stated examples (the latter including two with `m=3`), comparing direct block acceptance against `6^m U(D)`.

The certificate `research_checks/X6_UNIT124_TRIADIC_BLOCK_VS_NATIVE_BRC_RESULTS_20261118.json` preserves each exact example and census. The universal statement follows from the proof, not the finite search. This is source-grounded comparison of the actual triadic macro-event consumer and the pinned signed-native shortest-word interface; it is not an original-module integration run.

## LP019 / LP020 / LP023 / LP026 downstream disposition

For this **newly inspected current-main consumer**, the macro-event coefficient code is **PRESERVE_PATH_BRC_AT_MACRO_EVENT_TYPE**. Any current or later importer requiring *all* signed-native shortest primitive words must either compute `B(D)` from raw signed endpoint degrees, or carry the exact event-block restriction and disclose `T(D)`, not silently equate the two. Mixed-sign `d` requires provenance-preserving length/type separation before any shortest-path inference. This supplies an explicit source-location, operator/type boundary and exact numerical tests toward the 28-LP downstream ledger. No incorrect original caller is attributed to this correctly scoped script; LP011 and the originally alleged LP019 signed subtraction source remain `UNRESOLVED_PROVENANCE` pending exact historical commit:path:line.

Mother-objective remaining items: complete the original 28-LP claim-to-current-consumer crosswalk; consume independent Driver `REQUEST_REVISION`; obtain independent R063 original C3/C4 512-case verification/admission on existing Issue #2416. Preserve signed P000 and both frozen scientific pins, prior Unit118 original integration, and all earlier Source-published checkpoints.
