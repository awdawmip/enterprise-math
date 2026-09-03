# Research Return — R005-A deficit-shadow executable binding correction

Task: `RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION`  
Publication: `TP2-ADD82532ACD19FC01D53`  
Researcher: `EM-R005AFIX-754384`  
Claim: `chatgpt-r005a-fix-20260904-0746`  
Execution branch: `research/r005a-fix-chatgpt-20260904-754384`  
Execution base: `746be8ced2bbc3ffa89b601f881e9cf86a2d7a43`  
Frozen mathematical source: `f9e2a611b45631c43effce36b7300c6f9a56b77b`

## Terminal disposition requested

`NO_MATH_DELTA_EXECUTABLE_BINDING_REPAIRED`

This is an integrity/executable repair only. It does not strengthen, weaken, or otherwise alter DSI1, DSI2, DSI3, the q=78553 constants, the certified endpoint, the external catalogue obligation, or the gap-shadow search semantics frozen at the source commit.

## Exact repair

The source scanner could not execute the declared positive catalogue-validation path because two exact-byte defects were present:

1. `max_gap_bound_end` was read from misspelled `metada` instead of `metadata`;
2. the required-band coverage diagnostic contained a malformed f-string split.

The corrected scanner preserves all mathematical expressions and only repairs those two executable defects.

The focused regression was extended to close the evidence hole that allowed the defect to escape the original validation:

- a `completeness_attestation=true` synthetic catalogue now reaches the positive `validate_catalog_for_seam` path successfully;
- a catalogue whose `max_gap_bound_end` is exactly one unit below `required_gap_start_max` is rejected with `max-gap bound does not cover the required gap-start band`;
- the existing false-attestation fail-closed test remains and still rejects correctly.

## Exact-byte validation

Final scanner:

- path: `experiments/r005a_p2_gap_shadow_inversion.py`
- bytes: `12289`
- Git blob SHA-1: `sha1:1d3d19adc13652bf343972c5eb3ac95684bb8c8a`
- SHA-256: `sha256:6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5`

Final regression:

- path: `experiments/r005a_p2_gap_shadow_inversion_regression.py`
- bytes: `8145`
- Git blob SHA-1: `sha1:ece824a71c884b09033f1666581a71afe86822a0`
- SHA-256: `sha256:3286c62f6ac7ab3a14c214e462ef8a8e3ad19f780873253ff906f46d8ba394be`

Validation transcript:

- path: `research_artifacts/RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION_20260904/validation_transcript.txt`
- bytes: `3552`
- Git blob SHA-1: `sha1:fc929d83bc57a4068ef8786c5e66520c9ae3756d`
- SHA-256: `sha256:30fa91f56a21a2a677486375a3386fef4459f55a00794fac1c8b6904f00f540e`

Focused regression output:

- path: `research_artifacts/RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION_20260904/focused_regression_output.json`
- bytes: `734`
- Git blob SHA-1: `sha1:4bf7d82b52185f1ffc8bf357d719c29c00406768`
- SHA-256: `sha256:5a9fe4f053df4b886a3b0d2e1a26b9c2ec25ef592840220f2ccffc0773d4b6f8`

The scanner/regression Git blob identities above were independently recomputed from the locally executed bytes and match the GitHub branch blob IDs exactly.

Commands on those exact bytes:

```text
python3 -m py_compile r005a_p2_gap_shadow_inversion.py r005a_p2_gap_shadow_inversion_regression.py
# exit 0

python3 r005a_p2_gap_shadow_inversion_regression.py
# exit 0 / status PASS
```

Regression coverage includes `54165` exact gap-shadow equivalence checks, `1008` deficit-formula checks, exact synthetic scanner agreement on `963` failures, the new true-attestation positive path, the new max-gap-bound coverage rejection, and the retained false-attestation rejection.

## Frozen mathematical boundary

The q=78553 data remains exactly:

- `d_max_bound = 2`;
- required gap-start interval: `[1291005053866735,1294364244470160]`;
- required complete-gap threshold: `916`;
- certified frontier remains `k <= 2822453183433`.

The q=78553 seam is **not closed** by this task. It remains blocked on a complete, independently auditable exact-916-gap catalogue for starts `[1291005053866735,1294364244470160]`.

## Control-plane recommendation

Freeze this return as a `PASS` result for Driver review with hard target disposition `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED`. If Driver accepts, the prior executable/evidence-binding objection can be closed at the same mathematical strength. Do not infer any q=78553 frontier extension, Working Truth promotion, Foundation authority, or canonical promotion from this Researcher return alone.
