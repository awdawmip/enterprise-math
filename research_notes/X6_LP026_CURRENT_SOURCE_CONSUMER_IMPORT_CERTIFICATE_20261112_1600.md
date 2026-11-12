# X6 LP026 actual current-consumer import closure — exact Source-byte regression

Date: 2026-11-12, Research lane on-hour. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. State: **EXECUTED EXACT SOURCE CONSUMER REGRESSION / NONBLIND / UNREVIEWED / NOT_ADMITTED**. Research evidence only; not a native TASK CLAIM/open, admitted Result or independent review.

## Scope and immutable inputs

- Mathematical task pins retained: centered signed-X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparator `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Actual current main `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py`: Git blob `ac32f6d82a91db99297e587cf63b0df95cece514`, imported Python function `relative_endpoint_multiplicity`.
- Actual current main `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`: Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, imported `endpoint_multiplicity` and `endpoint_weight`.
- Existing published Laurent checker `research_checks/X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER_CHECK_20261112_ONHOUR.py`: Git blob `e2bc083f1832b8eae2d8887095912da0e0e8984f`. Existing mathematical derivation `research_notes/X6_LP026_SIGNED_LAURENT_BRC_AND_CONSUMER_20261112_ONHOUR.md`.
- New targeted integration regression `research_checks/X6_LP026_CURRENT_SOURCE_CONSUMER_IMPORT_20261112_1600.py`: commit `d0ed9ee16490face014dfa0624acb949078ad5f9`, Git blob `769a7b6801436bc3b14a8f810f9caae4edd9ba2a`, content SHA256 `503dd130665ba2e8b011e58f1443d84f1a9d16534f7402730724298b6be0fb86`. Full GitHub readback matched the executed bytes.

The three previously published Python source/checker files were obtained through the authorized GitHub connector, reproduced *byte-for-byte* inside an isolated Python source layout and independently checked against their Git blob object hashes **before import**. This is an actual import/execution of those exact source bytes; it is **not** a claim of cloning or executing all tests in the complete repository or of deploying a new production interface.

## Commands and exact executed output

1. `python research_checks/X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER_CHECK_20261112_ONHOUR.py` in the isolated faithful source layout: the previously conditional `current_source_positive_consumer` branch actually ran and printed:

```text
PASS X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER
unweighted_state_length_cases 31065
weighted_depth_multinomial_cases 1205
signed_relative_n6_zero 21360
signed_relative_n8_011235 4200
legacy_positive_n6_zero 720
weighted_n2_zero 143/6
current_repo_positive_consumer PASS
```

2. `python research_checks/X6_LP026_CURRENT_SOURCE_CONSUMER_IMPORT_20261112_1600.py` performed an additional independent dynamic test: **5,005** positive path-length / relative-endpoint states at lengths 0..9 were compared to the actual current `x6_signed.relative_endpoint_multiplicity`, and **7,588** signed relative states at lengths 0..6 were compared with depth-fiber sums of the actual `signed_brc.endpoint_multiplicity`. It passed, printed:

```text
PASS X6_LP026_CURRENT_SOURCE_CONSUMER_IMPORT
source_blob_pins {'x6_signed.py': 'ac32f6d82a91db99297e587cf63b0df95cece514', 'signed_brc.py': '300a96e3dc24bf6fff73743037a0347a8bc83176'}
positive_actual_consumer_state_length_tests 5005
signed_actual_native_fiber_state_length_tests 7588
observer_n6:positive,signed,native_zero 720 21360 19920
signed_relative_n8_median_witness 4200
weighted_native_n2_zero 143/6
```

All arithmetic was exact `int` or `Fraction`. The finite coverage is not a universal correctness proof; the previously published Laurent coefficient theorem supplies the all-`N` mathematical argument in its stated domain.

## Precise consumer decision and next action

**LP026 — KEEP / RETYPE:** `relative_endpoint_multiplicity` is a validated **positive-only six-generator relative observer** within its declared argument contract, not the full signed X6 native endpoint BRC. At length six and relative zero it returns **720**, while the signed relative quotient has **21,360** words and the exact native zero endpoint has **19,920** words. The signed native kernel's depth-fiber aggregate matches the Laurent quotient in the tested range. Do **not** overwrite the positive-only function or silently reassign its output type.

This completes the previously unexecuted imported-current-consumer check in the prior LP026 research note (for the exact inspected two Git blobs). The remaining material dependency is **source-level call-site reachability and type propagation**, not another proof of the completed Laurent lemma: inspect current callers of `relative_endpoint_multiplicity`, `endpoint_multiplicity` and min-zero quotient outside these verified kernels, distinguish positive vs signed semantics, and write the minimal typed adapter/guard only if a verified caller requires it. Preserve the Driver `REQUEST_REVISION` on the 28-claim corpus until the remaining actual caller/old-provenance obligations are discharged.

Control boundary: Source research can be recorded on GitHub, but this run did not verify a winning X6 Research-lane CLAIM/open. The earlier lane SID `MCP-de3e5bafb24f43f4a5e6285e7601676a` is historical provenance, not an available Sites session capability. Current Sites subject recovery of that SID returned `OWN_SESSION_REGISTRATION_NOT_FOUND`; it is not evidence that the GitHub Chat lane is terminated. The native continuation read request `onhour-20261112-1604-x6-current-continuation` was QUEUED at last read and must be polled under its **original request ID**, not resubmitted. Exact typed progress artifact repair remains tracked by #2141.

**Unchanged**: frozen science, P000, canonical task publication, owner/CLAIM, R063 accepted results, existing live code, review, and scheduler. No full-project or native benchmark is claimed.
