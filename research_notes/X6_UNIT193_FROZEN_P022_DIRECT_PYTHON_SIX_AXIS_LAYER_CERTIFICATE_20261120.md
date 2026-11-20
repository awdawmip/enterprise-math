# X6 Unit193 — direct execution of the immutable P022 six-axis geodesic producer

Date: 2026-11-20. Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.
Frozen science pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; frozen historical source pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
Source status: **AUTHOR_EXACT_PYTHON_EXECUTED / SOURCE_BLOB_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Native semantic PROGRESS separate and not submitted by this unit.

## Why this is a new experimental unit

Unit173 examined the actual P022 producer and importing tests. Unit192 established the six-signed-axis geodesic-layer BRC split identity and tested a source-equivalent independent JavaScript implementation, rather than importing the historical Python producer. **Unit193 closes the direct-source execution gap**: the actual, frozen, unchanged Python source `src/enterprise_math/p022_geodesic_multiplicity.py` was imported with `importlib` after verifying its exact Git blob **`46373050168d2430b6cb3952aa763f3081284632`** and byte SHA256 **`3e920f21b9ed4124323dbc4d982e2df43381b573f43fcc5ca84952a51bb19237`**.

Direct calls to the original functions `sc_graph_radius`, `sc_geodesic_path_count`, `sc_geodesic_interval_profile`, and `sc_shell_total_geodesic_paths` were independently compared against, respectively, signed L1 endpoint length, recursive predecessor-word BRC, explicit midpoint-layer integer enumeration, and all-endpoint shell BRC mass. For every midpoint `y` on a shortest signed-axis path from 0 to `z`, exact producer `sc_geodesic_path_count(y)*sc_geodesic_path_count(z-y)` was summed and compared with the producer's end-state BRC. Independent bounded-polynomial integer convolution verified each producer interval profile. Four malformed-input rejections were also checked.

This is **actual import and execution of the historical Python producer**, not just transcription of its equations. The exact module copy is byte-identical to the immutable published Git object. The X6↔P022 relation remains an explicitly typed signed-axis graph adapter; no new existing production import or native R063 benchmark run is asserted.

## Executed six-axis shell and layer certificate

| Radius | Exact endpoints | Direct source total shortest-path BRC |
| ---: | ---: | ---: |
| 0 | 1 | 1 |
| 1 | 12 | 12 |
| 2 | 72 | 132 |
| 3 | 292 | 1,332 |
| 4 | 912 | 12,372 |
| 5 | 2,364 | 106,452 |
| 6 | 5,336 | 856,212 |

Total **8,989 endpoints**, **57,505 endpoint/layer equalities**, **235,705 explicit midpoint instances** including **173,980 on shell 6**, **4 malformed-input cases**, and **0 mismatches**. All shell masses sum to **976,513**. The Python checker was executed under default, `-O` and `-OO` modes; each output JSON SHA256 was `eae5dda23f452d74c638ae5489060d41e347a0265da1f49a757120e10c80195c`. The checker uses explicit `require` rather than optimization-removable `assert`.

The source module itself is from `fd2bcff10ca6e147348b6c1236027fc0d2877df3` and remains unmodified. The independently executed checker should be saved at `research_checks/X6_UNIT193_PINNED_P022_PYTHON_DIRECT_SIX_AXIS_CHECK_20261120.py`, with the complete machine certificate at `research_checks/X6_UNIT193_PINNED_P022_PYTHON_DIRECT_SIX_AXIS_RESULTS_20261120.json`.

## Interpretation and continuation

This newly certifies the frozen **Python producer's actual six-dimensional behavior** at all signed L1 endpoints through radius 6 and its BRC midpoint conservation. It is a direct historical implementation test, while the general identity retains Unit192's proof status. The source's test file `tests/test_p022_geodesic_multiplicity.py` historically exercised dimensions 1–3 for small radii; that established test scope is not silently expanded.

The unresolved parent obligations remain: real LP011 native signed-argmax and LP019 positive-path subtraction *offending* `commit:path:line` and typed caller, if such historical callers exist; actual native X6 production order-sensitive integration rather than merely typed graph adapters; original Units149–152 and later author Units175 onward native semantic links under current legitimate same-lane CLAIM/RUN; independent Driver review.

No R063 benchmark rerun, no task/owner takeover, no new dispatch or scheduler operation. Research conversation provenance `chatgpt-research-onhour-enterprise-math-20260923`; exclude maintenance `chatgpt-hourly-enterprise-math-20260921`. Existing RA `RA-5E3FE1E761E4963EC461A892` is only an activity source record, not protected writer authority.
