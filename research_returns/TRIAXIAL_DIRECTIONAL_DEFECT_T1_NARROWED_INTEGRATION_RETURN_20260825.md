# TRIAXIAL DIRECTIONAL DEFECT T1 NARROWED INTEGRATION — RETURN

Researcher-ID: `EM-TDINT-AD7201`

Task-ID: `GS-TRIAXIAL-DIRECTIONAL-DEFECT-T1-NARROWED-INTEGRATION`

Primary disposition:

`T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_INTEGRATED`

## Frozen integration head

`11d8b33ff0e9fbe13256ec0f51ac7ef984723cc7`

The PR merge candidate tested this integration head against current-main base
`bca280964a67853ed272b56ab255e00186d59aab` as merge head
`7c5e70f756cb95ba43d901a5b15cd000f422f2a3`.

Pull request: `#645`.

This was a `NO NEW MATHEMATICS` integration. The mathematical authority remained:

- taskbook source `9c9358159111e7f29c9fe6e5860a330589654c0e`;
- controlling Driver review `f364c75d55e8018bcea80bdf00fc025f2ad7dd02`;
- independently verified implementation head `b1f79d2314de2d1ae1511a693cdf37e7c7812cf8`.

## Integrated narrowed interface

The independently verified operator implementation was transplanted unchanged as:

`src/enterprise_math/_triaxial_directional_defect_core.py`

with Git blob:

`5261da8b9e7848ac5cce935f81d7e7e0381b210b`.

The public narrowed T1 adapter is:

`src/enterprise_math/triaxial_directional_defect.py`

with Git blob:

`570088fb2a8dc1a19ada303d55ea1cb93718a0c7`.

The exposed integration surface includes typed equivalents of:

- `DECLARE_FRAME`;
- `DIFF1`;
- `RHOMBUS2`;
- `TRIPLE_DEFECT`;
- `XRAY_KERNEL_CERT`;
- `FRAME_WIDTH`;
- `MULTIFRAME_UNIQUENESS`;
- `EXPOSED_AUGMENT`;
- `FULL_ADJOINT` / `CHIRALITY_ADJOINT`;
- `COMPRESSED_GRAM` / `GRAM_FACTOR`.

## Mandatory semantic split

The Driver-required split is explicit and executable:

`FULL_ADJOINT / CHIRALITY_ADJOINT`

is a full sparse-field adjoint surface, while

`COMPRESSED_GRAM / GRAM_FACTOR`

is a finite native-hex compressed `G*G` / factorization diagnostic surface.

They are separate result types with distinct domain semantics. The integration does not identify the two objects.

## Preserved boundaries

The adapter requires canonical primitive frames where the width/census interface requires them, constructs an explicit canonical unoriented-ray key, and deduplicates multi-frame input through that key.

The width/uniqueness interface is explicitly scoped by `NativeHexDomain`; no arbitrary-domain width theorem was added.

The integrated coefficient-domain diagnostic is frozen to the independently exercised characteristics `0,2,3,5,7`. The small-characteristic singularity cases remain executable negative controls rather than being silently coerced into a field-universal claim.

The six-point endpoint stencil remains distinct from the eight typed trace states. Endpoint coalescence is not treated as trace identity.

The same operator core supplies tomography and the Hive/rhombus bridge. No duplicate rhombus/triple-defect implementation was introduced.

The exposed-vertex augmentation path retains the unimodular/full-rank certificate behavior in the verified characteristics.

Y–Delta is not exported by the narrowed public API. No Y–Delta theorem, binary/nonlinear tomography result, Foundation edit, width-theorem enlargement, or new top-level tool family was introduced.

## Toolbox and inventory integration

The method is registered as a `GLOBAL_SUBTOOL` under:

`T1_SCALE_ENUMERATION_VALUATION`

rather than as a new top-level family.

Machine registry artifact:

`enterprise_toolbox_registry.json`

Git blob:

`41d4ee9c5f2124be9905dce8ff5f1ca55f11fe94`.

Method inventory addendum:

`research_method_inventory_addenda/20260825_triaxial_directional_defect_t1.json`

Git blob:

`422562255c3c6a64e8fc1d263f4ccbbf0d253959`.

Human toolbox mirror:

`docs/ENTERPRISE_TOOLBOX_REGISTRY.md`

Git blob:

`3a3f7daf968e41472dc1bb3a0ac1e83d84c6bd73`.

## Regression evidence

Exact quality command executed by CI:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

Result:

```text
Ran 1431 tests in 476.150s
OK
```

Quality workflow run: `32861520263`.

Quality job: `97846697091`.

All 13 new integration regressions passed. They cover:

1. cyclic covariance / reversal sign behavior;
2. primitive/canonical frame validation and unoriented-key exposure;
3. shared-core second-to-third defect bridge;
4. six-point endpoint stencil versus eight-state trace-cube typing;
5. native-hex single-frame uniqueness boundary;
6. native-hex multi-frame uniqueness and explicit unoriented dedup;
7. constructive X-ray kernel certificate;
8. Euler-phi primitive frame census;
9. exposed-vertex unimodular augmentation in characteristics `0,2,3,5,7`;
10. typed full-adjoint versus compressed-Gram separation;
11. Gram factorization plus small-characteristic failure guards;
12. Hive/rhombus reuse through the same core;
13. Y–Delta API absence plus the finite-support left-inverse negative guard.

The whole-repository suite, not merely the new test file, passed.

## Governance/current-main reconciliation

During execution, the repository task-publication cutover became active after the original taskbook was distributed. The taskbook therefore required a publication-only migration before CI would accept it.

The migration added only the current publication/registry metadata and retained the original taskbook source as provenance:

`research_tasks/TRIAXIAL_DIRECTIONAL_DEFECT_T1_NARROWED_INTEGRATION_20260825.md@9c9358159111e7f29c9fe6e5860a330589654c0e`.

It did not alter the mathematical body or widen the task.

At frozen integration head `11d8b33ff0e9fbe13256ec0f51ac7ef984723cc7`, the reference-integrity workflow passed:

- citation/lineage: PASS;
- shared tool routing: PASS;
- canonical task registry/orphan prevention: PASS;
- legacy scheduler cutover: PASS;
- bilingual sync: PASS.

The full PR merge candidate against `main@bca280964a67853ed272b56ab255e00186d59aab` also passed the complete quality suite. No current-main mathematical or structural conflict remains.

## Evidence freeze

Evidence manifest:

`research_output/evidence/TRIAXIAL_DIRECTIONAL_DEFECT_T1_NARROWED_INTEGRATION_MANIFEST_20260825.json`

The terminal task-registry record is frozen as `DONE` with no successor mathematics opened by this integration task.

No research residue was created because no new mathematical gap was required to close the integration.

## Final disposition

`T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_INTEGRATED`
