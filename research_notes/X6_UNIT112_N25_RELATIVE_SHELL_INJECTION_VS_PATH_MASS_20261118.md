# X6 Unit112 — a fixed N=25 signed shell is faithfully observed but NOT BRC-homomorphically counted

**Date:** 2026-11-18. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; canonical Task `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`.

**Status:** `AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED`. This is a new scoped observer/path-semantics adjudication for LP015, LP017, LP019 and LP023. It neither changes the P000 V5 frozen scientific baseline nor executes the original R063/Helly C3/C4 benchmark.

## Precise proposition and hypotheses

Work only in a **selected signed three-axis affine sub-torsor** of the six-axis native X6 space from P000 V5 at immutable `59538f585d037d09ef687b28715c4bc1a3f9fe03`, with integer displacement `z=(a,b,c)`, squared native component readout `G(z)=a²+b²+c²`, and native shortest signed-word count `B(z)=T!/ (|a|!|b|!|c|!)`, `T=|a|+|b|+|c|`. Define the **relative/min-zero observer** `rho(z)=z-min(a,b,c)(1,1,1)`; this observer's integers are not native Cell identity and do not preserve native distance or path labels by declaration.

Let `Sigma_25 = {z in Z³ : G(z)=25}`. Then:

1. `|Sigma_25|=30`, and **the restriction** `rho|Sigma_25` is injective, so `|rho(Sigma_25)|=30`. This does **not** assert global injectivity of `rho: Z³ -> A_E`.
2. The nonnegative min-zero square-25 **section** `P_25 = {q in N_0³:min(q)=0, G(q)=25}` has exactly **nine** elements and equals `rho(Sigma_25) intersect {q:G(q)=25}`, not the full image `rho(Sigma_25)`.
3. Signed shell native shortest-path mass `sum_{z in Sigma_25} B(z)=846`; section-local mass `sum_{q in P_25} B(q)=213`; **naively reinterpreting all 30 relative image addresses as primitive native displacements** gives `sum_{q in rho(Sigma_25)} B(q)=3699`. All three integers count different typed populations/operations.
4. The observer images' *observer-coordinate* squared-length distribution is exactly `{17:6,25:9,50:3,58:6,65:6}` and hence cannot be treated as a norm-25 native shell.

### Exact short proof

The integer solutions of `a²+b²+c²=25` are precisely all signed permutations of `(5,0,0)` and `(4,3,0)`. There are `6+24=30`. Their coordinate sums belong to `{-7,-5,-1,1,5,7}`; none is divisible by 3.

If `rho(x)=rho(y)`, then `y=x+k(1,1,1)` for some integer `k`. Equal squared norms yield
`0=G(y)-G(x)=2k(a+b+c)+3k²=k(2 S(x)+3k)`.
For `k≠0`, `3` must divide `S(x)`, contradicting the displayed possible sums. Thus `k=0`, proving injectivity **on this shell** without assuming observer data preserve operations.

There are three ordered positive one-support solutions and six ordered positive two-support `(3,4,0)` solutions in `P_25`. Their natural path masses are `3*1+6*binomial(7,3)=213`; the full signed shell has `6*1+24*binomial(7,3)=846`.

For a particularly small typed counterexample, `z=(-3,-4,0)` is native norm-square `25`, with `B(z)=35`. Its min-zero readout is `rho(z)=(1,0,4)`, observer gauge-square `17`, and using the *wrong native formula on that readout* gives `B(rho(z))=5`. Thus **injectivity on a fixed shell is not preservation of the original labeled primitive-path count**. Recovery is possible only with the declared shell constraint and exact inverse, not by silently applying the native BRC formula to the observer representative.

The other observer-image squared-norm classes and the naively summed mass `3699` follow by the finite explicit enumerator below. In particular the number nine is the *separately cut* nonnegative norm-25 section, not the number of observer images of the native signed shell.

## Executed exact certificate and evidence scope

The actual executed checker is `research_checks/X6_UNIT112_N25_SIGNED_SHELL_RELATIVE_OBSERVER_FIBER_CHECK_20261118.py` (source SHA256 `1946243a22506de4a34b4f118de0329cca8499dbb1b4fa9d59585959069f4163`, Git blob `6d3ae8ead5ce96c9d6b090769be3dee75dd39c65`). It exhaustively enumerates `[-5,5]^3`, filters squared norm 25, and makes **900** explicit pairwise observer-equality checks in addition to exact integer path and image statistics. CPython ordinary, `-O`, and `-OO` were **actually run**, all exited successfully, with byte-identical JSON output SHA256 `a0fbee481efe687703d2074b2f455af47909018d20164ac44ce7343c5144e219`; all conditions use always-on `require`, not optimizable bare `assert`. Result JSON has Git blob `5402b25b0fa3f4694b16e69bab13fd71cda4aab4`.

Proposition 1 and the shell counts have a finite self-contained proof above; results 3/4 have complete stated finite executable coverage. This does not assert anything for arbitrary squared norms, arbitrary observers, a fourth/fifth/sixth axis outside the selected signed slice, or future-operation descent.

**Scoped source provenance:** frozen task `RS_X6_LEGACY_PLANE_RECONCILIATION_20260905.md` blob `9cbefbb8886a0ce4f312b1a52cde0990d55aa7eb`; original 28-row author ledger `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json` at `a0bfa8eace20b061f5b228c733acdc46221388d7` blob `5881055c0801ca5bb0970756d500daa0114d36b0`; existing 28-row typed crosswalk `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md` blob `2c7c4794a90df294cf3d158cb63ba29886c7babd`. In this run, 14 additional small pre-rebase early definitions and 7 selected dated frozen research notes were read for source provenance; the seven selected notes did not provide the old original 9/213 claim locus under the targeted textual predicates. These bounded reads do not prove original LP015/017 historical locations absent across all 231 notes. Existing Unit97–111 source/read/validation results are consumed, not replayed.

**Typed mother-task implication:** keep `LP015=positive_section_only`, `LP017=section_mass_213_only`, `LP019=positive_path_counts_are_nonnegative`, `LP023=relative_observer_requires_declared_inverse_for_native_BRC`. Correcting a consumer requires an actual source:line that equates `rho(Sigma_25)` with the nine-element section or computes native counts on relative representatives. No such erroneous live caller was established in this unit, so no active module is patched. Alleged frozen LP011 wrong `argmax` / LP019 positive-path sign subtraction remain `UNRESOLVED_PROVENANCE`, not newly asserted source faults.

**Next exact unit:** trace remaining active LP015/017/023 concrete source call sites that count `rho(Sigma_25)`, and classify any real section-vs-image or BRC native-vs-observer misuse by immutable `file:line`. Deliver the scoped negative historical source findings to the independent Driver's existing `REQUEST_REVISION` route; no new Driver identity or review acceptance. Keep original R063 C3/C4 benchmark support Issue #2416 open with its unchanged original object and acceptance gates.
