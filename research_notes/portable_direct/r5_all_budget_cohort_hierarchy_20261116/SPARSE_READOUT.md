# R5 — 512-coefficient sparse representation of 25,856 exact count observations

Date: 2026-11-16. Frozen input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Status: AUTHOR_PROVED / EXACT_FINITE_RECOMPUTABLE / NOT_REVIEWED.

## Result

For the derived 954-event, radius-two indexed-center observer with eight effective closure switches, in the 101-budget window `214<=K<=314`, the complete table of `101 * 256 = 25,856` closure-mask optimal-path counts is exactly recoverable from **512 nonzero integer cohort coefficients** together with their budget/requirement-mask indices.

Let `A_T(K)` be the number of full-closed optimal paths with exact requirement union `T`. The prior common-cost theorem gives

`N_b(K) = sum_{T: (T & b)==T} A_T(K)`.

Across the frozen 101 budget instances the exact number of nonzero coefficient entries is 512 and the total union of requirement-mask indices contains only 25 possibilities; any one budget contains at most 20 positive coefficients. Therefore a *single requested observation* `N_b(K)` can be answered with at most 20 mask-containment tests and integer additions, after the 512-coefficient representation has been constructed.

The ratio between a dense count table and sparse coefficient **entry counts**, `25856/512 = 50.5`, is exact. It is a logical-value count, not a guaranteed byte/memory or runtime speedup: coefficients and count integers may have different lengths, and a dense table offers constant-time indexed lookups.

## Proof

Each optimal full-closed path belongs to exactly one exact requirement-union class `T`. The mask `b` admits that path precisely when `T subseteq b`. Sum class multiplicities to obtain the readout. The exact cohort sweep in `VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py` visits all 101 budgets, emits every positive class count and gives the 512-entry total. The independent `VERIFY_R5_SPARSE_READOUT.py` consumes that JSON, checks all 101 rows and all 256 masks, and compares the direct sparse subset sum against an independently implemented dense Boolean zeta transform. All 25,856 comparisons agree.

## Reproduction

From a checkout of the Draft PR branch:

```sh
python research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py |
python research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_SPARSE_READOUT.py
```

Actual run: `PASS_R5_SPARSE_READOUT_ALL_25856`, `stored_nonzero_integer_coefficients=512`, `total_distinct_requirement_masks=25`, `dense_count_values=25856`. The independent sparse-readout script's verified Git Blob is `7e0ad39cf5a67af0177d92522147deb24a128df4`. Full 101-budget coefficients are deterministically emitted by the first program.

## Next

Determine whether the nine budget support-pattern intervals and their 512 coefficients admit a smaller local transfer description derived from the gap geometry rather than enumerated optimizers. Preserve the distinct unresolved `max-new/min-old` optimal-center recourse question on K214..291.
