# X6 Unit180 — frozen test-consumer source audit: 24 new exact callers

**Observation date:** 2026-11-20. **Author lane:** TASK_RESEARCH, logical conversation `chatgpt-research-onhour-enterprise-math-20260923`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, mother objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`.
**Frozen scientific input:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`. **Frozen historical source:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. **Status:** AUTHOR_SOURCE_AUDIT / IMMUTABLE_BLOBS_READ / UNREVIEWED / NOT_ADMITTED.

## Source-backed increment

Read the actual complete text of **24 targeted frozen `tests/*.py` files** via the connected GitHub `fetch_file` at the exact historical commit. All 24 yielded Git blob SHA1s (manifest below). No new test execution, no new native R063 benchmark, no claim that these tests are the entirety of historical consumers.

The exact-name source check across these 24 bodies found zero occurrences of `diagonal_quotient`, `canonical_min_zero`, `same_diagonal_class`, `diagonal_chart`, `compose_canonical`, `inverse_canonical`, `argmax` or `argmin`. This is a precisely scoped textual absence test for these spellings, **not** a determination about equivalent formulas, dynamically discovered consumers or other original sources. Unit179 already covered 31 other tests; these 24 are a semantic-inspection subset of the **312/312** complete frozen test corpus already published by Unit180's canonical census. No remaining 257-file read gap is asserted by this supplemental note. Keep Unit178's separate 225 top-level production and Unit179's separate 110 experiment Python inventories unchanged.

## Positive exact producer–consumer observations and type boundary

- `tests/test_euler_fcc_chirality_connectivity.py:5–26,29–96` imports both `euler_fcc_chirality` and `euler_fcc_chirality_connectivity`, and exercises `cover_neighbors`, `cover_components`, `cover_diameter`, `gauge_cover_relabel` and `verify_connectivity_classification`. This is the already-typed derived 8-state K4 covering graph used in Unit172, not an invocation of a six-axis native Cell BRC subtraction.
- `tests/test_tetrahedral_endpoint_sum.py:4–20,40–82` imports and calls `endpoint_sum`, `residual_code`, `canonical_decomposition`, `lift_difference` and `affine_support`. Its torsion and residual code are the derived K4 carriers from Unit170, not native positive N-BRC.
- `tests/test_weighted_relation_field.py:4–28,45–96` calls `weighted_relation_field`, `coarsen_weighted_relation_field`, `merge_weighted_relation_field`, and `split_two_block_totals_from_internal_relation`; the tests retain signed integer relation-field entries, with coarse-graining and reconstruction tested as distinct operations. They support the source/type chain used in Unit176, but do not themselves transfer an X6 signed-axis dominant selector.
- `tests/test_p022_barlow_growth.py:3–25,35–48,120–166` cross-checks Barlow shell path formulas and recurrence across short period patterns; `tests/test_p022_barlow_precision.py:3–22,24–125` separately checks prefix imbalance and selected-layer witnesses. These are P022 derived path consumers; neither is a demonstrated LP019 cancellation of positive native endpoint multiplicity. Their bare Python `assert` statements are not an optimized-mode assurance certificate; the generic validation hazard was already established and repaired in a different LP019 checker by Unit111, and is not claimed as a new finding here.
- `tests/test_relation_observable_composition.py:3–12,17–84,129–169` includes a concrete hidden-branch example and an intermediate-undefinedness example; `tests/test_p023_composition_safe_collapse.py:6–21,24–75` tests that a coarse observer must be constant on fibers before an induced operation is valid. These are positive evidence that the checked derived APIs distinguish fiber information from terminal-only observation, not an actual raw Cell address conversion.
- `tests/test_relation_lattice.py:4–14,17–65` imports `weighted_relation_field` and compares field-preserving shifts with source data. It is not a caller of R061's `diagonal_quotient.py` despite the different algebraic use of equivalence classes.

These observed callsites contribute exact provenance and non-conflation to the 28-LP crosswalk. No specific historical erroneous LP011 native signed argmax or LP019 native positive N-BRC cancellation caller has been established in this 24-file scope. Retain both as `UNRESOLVED_PROVENANCE` until a true `commit:path:line` is found. Preserve correctly typed producer/consumer code rather than patching it on an allegation.

## File-by-file immutable source inventory

| Frozen file at `fd2bcff10ca6…` | Git blob SHA1 |
|---|---|
| `tests/test_equivariant_section.py` | `bdc3c76070182698b39f7dea38f2312b9f9c07b6` |
| `tests/test_euler_rotation_refinement.py` | `b1bfd336a4c4955752ebf44c6d185d27672f94e2` |
| `tests/test_finite_symmetry.py` | `41fedf9ece09a62caba518a7f47a55e0ffbb2840` |
| `tests/test_lattice_geometry.py` | `304ff8e769f93fa0e96a03c1ffe89960ea5dd622` |
| `tests/test_p022_barlow_growth.py` | `8e8418a87a1fbbdad9ba5ff03cbe532af0f6f224` |
| `tests/test_p022_barlow_stacking.py` | `e0b6e3c4df5db0db0f8d238d527df72a3e4ca510` |
| `tests/test_p023_borrow_cocycle.py` | `d08ad45b7dac725253df25408844907014344b5e` |
| `tests/test_p023_composition_safe_collapse.py` | `6ad6792fe895ebdb36e12e187a0195c0f1742521` |
| `tests/test_p023_minimal_repair.py` | `d81492a8a1bcc0013704c1d9ad0a79dbb50270fb` |
| `tests/test_relation_future_powerset.py` | `f471c4efe8e46e16c123304c478b4f6cfd097f0e` |
| `tests/test_relation_lattice.py` | `07ba3cafbbed67e522cbe441aec7a3fff8f82b0f` |
| `tests/test_relation_observable_composition.py` | `496672442cb81e8fa114c07959ec150784e02c31` |
| `tests/test_c3_chiral_complex_structure.py` | `a8846720f22247b25d78e8705e17a36792125fc9` |
| `tests/test_euler_fcc_chirality_connectivity.py` | `794037b5d2f2a58b79b0054814d6e7a69b3fe7f1` |
| `tests/test_p022_barlow_precision.py` | `1bf1cfb09b0f16b1964dc9c62011f9cf85bd415e` |
| `tests/test_p022_hcp_geometry.py` | `8bd7e37736d3eb001e22f6dde19d91ca2e0d5235` |
| `tests/test_p023_safe_precision_interior.py` | `5bed9d83d5160e4d4c32a0b30418738dea866455` |
| `tests/test_p023_selector_semigroup.py` | `7555ac85612146e72eceae8479f121f8e2f74578` |
| `tests/test_relation_observable_signature.py` | `fb96b54b3eb61324ac398e0e3dcf6ec3d91fab2b` |
| `tests/test_relational_spectrum.py` | `3a968d396fa52e9873f936463aa18bee28b00373` |
| `tests/test_safe_operation_algebra.py` | `6a1f94746458e07a781d1f4abefdadcfc1c8e103` |
| `tests/test_state_pair.py` | `34ac4a031c72dc1a79f1699b513ca169786a0b30` |
| `tests/test_tetrahedral_endpoint_sum.py` | `d5cf7d4fa1405eca8245baa143334e282ee8fb26` |
| `tests/test_weighted_relation_field.py` | `51748dfe340c385907c4f2218fa1ae5ae2260522` |

## Control provenance and next exact action

Author-only source audit; no formal native checkpoint or independent Driver review claimed. Source-pinned predecessor: `research_notes/X6_UNIT179_FROZEN_EXPERIMENT_CONSUMER_AUTHOR_CONTINUATION_20261120.json` (blob `cdf911cbab56b78e60d5036d31d8fc1c84a08319`), in which Native was authenticated through Unit174 and Units175–179 were outstanding. Old original recovery requests and associated statuses are preserved in that source; no request was replayed here. Current same-lane winning claim/RUN authority has not been established from the presently read-only material.

Continue reading the remaining 257 frozen test bodies only where evidence value warrants, join actual producer–consumer edges against 28-LP claims and exact old/current `commit:path:line` allegations; distinguish derived K4/P022/finite-operation carriers from six-axis signed BRC. Also retain Units149–152 historical association, Units175–180 Native semantic association, existing original R063 benchmark, and independent review as distinct tasks.

## Canonical same-lane reconciliation (2026-11-20)

The canonical Unit180 proof and manifest at `research_notes/X6_UNIT180_FROZEN_ALL312_TEST_DIRECT_CONSUMER_CENSUS_20261120.md` and `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/unit180_frozen_all_312_test_python_manifest.json` already establish all 312/312 exact frozen tests read. This 24-file supplemental note documents **deeper semantic producer/consumer classification within those 312** and must not be used to reopen the completed 281-file read debt. Unit181 independently completed the 60 August-dated note/definition corpus. The separate Unit182 signed return-fiber theorem consumes that existing frontier.
