# X6 Unit199 — Frozen weighted signed-BRC caller boundary and exact method-level execution

Status: AUTHOR_SOURCE_AUDIT / EXACT_SOURCE_PYTHON_EXECUTED / UNREVIEWED / NOT_ADMITTED
Date: 2026-11-21
Task: RS-X6-LEGACY-PLANE-RECONCILIATION; TP2-B4A441B23DA3159232C2
Mother objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905
Research lane: chatgpt-research-onhour-enterprise-math-20260923
Historical Source author: EM-X6-FB6990; author Activity RA-5E3FE1E761E4963EC461A892 (separate CAS update).

## Source, target and actual reuse

Unit198 proved the exact equality between the original six-variable weak-composition sum and its six-factor Fraction coefficient convolution for signed-X6 weighted endpoint mass. Unit199 does not repeat this proof. It determines (a) which historical caller can actually be established, and (b) the complete Python function-call performance of the original frozen function against the existing Unit198 algorithm, under identical exact inputs.

Original frozen source:
- Repo: awdawmip/enterprise-math
- Commit: fd2bcff10ca6e147348b6c1236027fc0d2877df3
- File: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py
- Git blob SHA-1: 300a96e3dc24bf6fff73743037a0347a8bc83176
- File SHA-256: 6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4
- Exact local bytes imported: 2,852 (both hashes matched the GitHub read).

P000 retains six signed native spatial axes and independent time ordering. This unit changes neither that ontology nor the frozen source.

## Source-backed producer → consumer boundary

The **confirmed direct caller** in the producer's frozen experiment directory is experiments/x6_signed_native_spatial_v16_20260905/check_signed_brc.py at the same commit. Lines 6–9 import endpoint_weight from signed_brc; lines 56–63 call it with equal weights on three selected endpoints over a short length window, comparing with endpoint_multiplicity.

The frozen .github/workflows/x6-signed-spatial-v16.yml at lines 20–24 executes that checker script, and does not directly import the weighted function.

GitHub's exact directory listing contains only signed_brc.py, check_signed_brc.py, x6_signed.py and check_x6_signed.py. Additional historical source bodies inspected at the same commit: src/enterprise_math/p022_geodesic_multiplicity.py, p022_barlow_growth.py, p022_barlow_stacking.py, p022_barlow_precision.py and tests/test_p022_geodesic_multiplicity.py. None of those inspected bodies directly references endpoint_weight or signed_brc. The separate frozen V7 check_x6_coordinate.py uses its own brc_endpoint_multiplicity and is not a signed weighted caller.

**Conclusion with exact search scope:** a regression-test caller is established; an actual production endpoint_weight workload is not established by these inspected paths. The tree listing itself contains 5,014 entries, which were not all source-body searched. Absence in the inspected subset is not a repository-wide absence certificate. The original production consumer's commit:path:line, observed K distribution and production acceptance object remain evidence debt.

## New actual experiment: frozen Python function vs Unit198 coefficient DP

The original function was directly executed from a SHA-verified copy of the pinned Python source, and its exact Fraction output was compared against the existing Unit198 coefficient convolution. This is a **new function-level method comparison, not the six-file R063 native benchmark**.

Domain:
- Two exact weight profiles: all integer weights 1; rational u=(1/2,2/3,3/5,1,2,3), v=(3/2,5/4,1,7/3,1,2).
- Two endpoints: z=(0,0,0,0,0,0) and z=(2,-1,0,1,-1,0).
- K=4,8,12,16 and length = sum_i |z_i| + 2K.
- 16 exact input cases; 0 disagreements. Three timed calls for each implementation per case (48 original, 48 coefficient DP). Each timed result was again checked for exact equality.
- Python perf_counter_ns measured total function-call time including Fraction operations, factorial work and coefficient setup. The medians depend on host and inputs; they are not a universal speedup or a replacement for R063 acceptance.

| K | Frozen original median, representative equal-weight zero endpoint | Coefficient DP median, same input | Ratio |
|---:|---:|---:|---:|
| 4 | 2.524 ms | 0.169 ms | 14.924× |
| 8 | 23.273 ms | 0.367 ms | 63.489× |
| 12 | 133.511 ms | 0.623 ms | 214.284× |
| 16 | 382.304 ms | 1.099 ms | 347.831× |

Across all 16 cases, observed ratios range **9.830×–347.831×**; at K=16 across all four weight/endpoint combinations they range 264.227×–347.831×. The complete 16-case summary in research_checks/X6_UNIT199_PINNED_WEIGHTED_BRC_METHOD_PROFILE_RESULTS_20261121.json stores all median nanoseconds and SHA256 fingerprints of each exact rational answer. The original six-variable composition count at K=16 is C(21,5)=20,349; the already-proved Unit198 coefficient method uses O(K²) exact Fraction arithmetic operations for fixed six axes. Measurement and arithmetic asymptotics remain separately typed.

The original local raw experiment output, including the three actual timings of each method per case, has SHA256 953ce5192dbe4395ecab9cacc50a7bc6358fd3f62211214eaad8c88db50fc563 and remains an execution-local artifact, not itself published as a GitHub file. The repository companion JSON is a compact summary, not a byte-for-byte copy of that raw result. The new repository reproduction checker X6_UNIT199_PINNED_WEIGHTED_BRC_METHOD_PROFILE_REPRO_20261121.py imports the published Unit198 code and checks the original historical Git blob before reproducing the cases. The local measured harness used the same frozen Python function and same Unit198 coefficient function body.

## Remaining scientific and engineering obligations

1. Continue precise historical caller provenance research, especially LP011/LP019, preserving distinct path, observed output and computation type. Do not invent a production integration from the test-only caller evidence.
2. For any confirmed production consumer, collect actual input shape, K distribution and native validation object; only then evaluate a possible compatible replacement and its full overhead, without altering the frozen benchmark.
3. Consume original queued/unknown continuation by the original request ID. Existing GitHub evidence and Activity checkpoint are not a new Native CLAIM/RUN/PROGRESS or an independent review.
4. Pending Native semantic links: Units175–199 and historical Units149–152. Independent Driver evaluation remains UNREVIEWED / NOT_ADMITTED.

This unit is AUTHOR_SOURCE_AUDITED / EXACT_PYTHON_EXECUTED / NOT_ADMITTED. No scheduler, claimant identity, original Source, or P000 modification.
