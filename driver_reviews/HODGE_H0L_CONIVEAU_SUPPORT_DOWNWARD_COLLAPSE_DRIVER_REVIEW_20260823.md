# HODGE H0L — Driver Review

Date: `2026-08-23`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task: `RS-HODGE-H0L-CONIVEAU-SUPPORT-DOWNWARD-COLLAPSE`
Taskbook source: `e74eeb9966f0adb7deb74408b74336c2aa20c542`
Owner branch: `research/hodge-h0l-coniveau-support-collapse`
Researcher-ID: `EM-HODGE-H0L-8D4C27`

## Driver disposition

`H0L_SUPPORT_FIRST_EQUALS_CYCLE_GYSIN_NORMAL_FORM_R1`

is **ACCEPTED** as a valid negative Hodge-special result.

Hard prerequisite A:

`DEGREE_2P_ALGEBRAICITY_CONIVEAU_EQUIVALENCE_TYPED_WITHOUT_OVERCLAIM = PASS`.

Primary hard target B:

`SOURCE_DERIVED_CONIVEAU_DOWNWARD_COLLAPSE_ADDS_ROBUST_ATTRIBUTED_LEVERAGE = NOT_ESTABLISHED`.

Preferred target C:

`CONIVEAU_SUPPORT_COLLAPSE_ENTERPRISE_R3_PRESEED = NOT_ESTABLISHED`.

`H1_ADMISSIBLE = false`.

The canonical owner branch is exactly one commit ahead of the taskbook source with only H0L return/checker artifacts added. Freeze the returned payload by owner branch plus:

- semantic core SHA-256: `eaef510d5d1439a0658618bb91745f4a140bfca66a79120f6ef63614da6f550d`;
- manifest blob SHA: `676a53424a26e6fe846e9823ee5ccd34361e1cb6`;
- checker: `83528/83528 PASS`.

## Accepted load-bearing mathematics

1. At rational degree `2p` on a smooth projective complex variety, geometric coniveau `N^p H^{2p}` is correctly typed as the rational span of codimension-`p` algebraic cycle classes. Localization identifies the support kernel, and purity/Gysin plus resolution/stratification and top Borel-Moore homology identify the degree-`2p` support generators. No generalized-Hodge-conjecture statement is asserted.
2. For the Fermat cubic fourfold, the full rational control is independently regenerated as
   `H^4(X_F,Q)=V_Hdg,Q direct_sum V_nonHdg,Q`
   with dimensions `21+2`, where the non-Hodge block has types `(3,1)+(1,3)`.
3. Phase A passes the anti-leakage firewall: the H0K final cycle lift and plane class matrix were not used to generate the H0L support rule.
4. The complete source-generated 405-plane support has exact Gysin rank `21`, and
   `ker[H^4(X_F,Q)->H^4(X_F-Z_all,Q)] = V_Hdg,Q`.
   The two-dimensional non-Hodge block has zero false positives.
5. A source-only 21-plane pivot support `Z_21` has principal Gram determinant `27` and the same restriction kernel. Under the declared component-count notion, 21 irreducible codimension-2 surface components are necessary and sufficient to support the whole 21-dimensional Hodge carrier at once.
6. The stratified support presentation admits exact reductions
   `36855 -> 405 -> 21`:
   pair-incidence presentation -> top local-cohomology/Borel-Moore generators -> independent Gysin image basis.
7. Class-sensitive supports are also available: each rational Hodge block admits source-only support selection, while `V_nonHdg,Q` admits none. Negative and denominator-bearing rational inputs remain correctly Q-linear and are not retyped as effective cycles.

## Attribution verdict

The support-first formulation is mathematically correct and theorem-relevant, but it does not earn Enterprise attribution against the fair standard baseline.

- `36855 -> 405` is exactly the ordinary top-degree local-cohomology / purity / Cousin collapse;
- `405 -> 21` is ordinary Gysin-image rank and exact linear algebra;
- class-sensitive support transport is finite-group representation plus localization/Gysin source mathematics.

Thus all H0L positive candidates are:

`SOURCE_INHERITED_LEVERAGE`.

Freeze:

`ROBUST_TRANSFORM_ATTRIBUTED_CANDIDATE_COUNT = 0`.

This is stronger than saying support-first failed. Support-first **succeeds exactly**, but at degree `2p` its successful operational normal form is already the classical cycle/Gysin normal form.

## Route closure

Freeze:

`CONIVEAU_SUPPORT_FIRST_FORMULATION_IS_SOURCE_COMPLETE_AT_AUDITED_FERMAT_SCOPE__DO_NOT_SCALE_KNOWN_POSITIVE_BENCHMARKS`.

Do not rerun H0L with more Fermat planes, larger support unions, alternate pivots, weakened baselines, or a different known-positive homogeneous/Fermat example while preserving the same localization/Gysin mechanism.

H0D remains the abstract transform-attributed R2 control. H0E–H0L now show that future quotients, algebraic normal forms, filtered recognition, Picard/divisor lifting, vector-bundle/Chern lifting, algebraic correspondences, character interaction, and coniveau support-lowering all become source-inherited on the audited known-positive Hodge benchmarks.

## Successor routing principle

The next stage must stop using a benchmark whose algebraicity is already available as checker mathematics. It should move to a genuine unresolved algebraicity frontier with:

1. an exact rational Hodge input frozen before cycle search;
2. no known target cycle available to seed the construction;
3. a mechanism genuinely different from future quotient / DFT / Gysin support rank;
4. a hard stop if the candidate simply reproduces standard deformation, derived, or semiregularity normal forms.

No H1 stage opens from H0L.