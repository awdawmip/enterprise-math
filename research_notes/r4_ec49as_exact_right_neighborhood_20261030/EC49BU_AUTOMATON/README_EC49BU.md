# EC49BU — signed-X6 weighted BRC finite automaton and eventual saturation

**Date:** 2026-10-31 (Asia/Shanghai). **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_AUTOMATON_AND_WITNESS_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Author context is not an independent review.

At signed-X6 zero-displacement length n, fixed positive weights wp=(2,3,3,2,1,1), wm=(1,1,1,1,1,1), fixed-instrument H={id, swap E1/E2}, first/last ordered steps and substring filters A=(+E1,+E2), B=(+E2,+E1), the exact minimum **rational-linear additive** observer ranks are:

| even length | native ordered closed words | base | separate A/B | conjunction-complete | with count |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 396 | 156 | 166 | 166 | 167 |
| 6 | 19,920 | 288 | 444 | 458 | 459 |
| 8 | 1,281,420 | 288 | 718 | 860 | 861 |
| 10 | 96,807,312 | 288 | 864 | 1152 | 1153 |
| **all even n≥10** | native exact formula | **288** | **864** | **1152** | **1153** |

**Theorem and exact certificate.** A pattern automaton over the signed-step histogram computes every weighted observation fiber without raw word enumeration. At length 10, an explicit 576-fiber certificate supplies two closed words per fiber with nonzero determinant of the two fixed-instrument weight channels (minimum absolute determinant 1). Inserting the native ordered adjacent loop (+E3,-E3) at a boundary outside the A/B patterns preserves all filters and zero displacement and multiplies the two weight channels by 3, proving full rank for every even n≥10. A triple of concrete words has augmented (weight_id, weight_swap, unweighted count) determinant 36, proving the extra count coordinate. The result concerns additive state dimension, not general bit encoding or physical heartbeat evolution.

**Actual checks.** Two byte-identical runs of the exact Fraction/DP verifier, native signed_brc.py unchanged (Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176), full direct check of 1,155 certificate words and 576 nonzero minors, and independent direct enumeration of all 1,281,420 length-8 closed words with separate-filter rank 718 modulo two primes. The n=10 DP used 680,434 memoized states rather than 96,807,312 native paths. All unfiltered totals match native endpoint_multiplicity and endpoint_weight.

**Full original sources.** Four neighboring EC49BU_full_sources.tar.xz.b64.part01 … part04 text files reconstruct the 18,916-byte xz tarball (16 full files: proof, actual executed Python scripts, direct witness JSON, complete per-fiber JSON report, independent brute script, original native source, stdout, manifest, sources/handoff). Concatenate parts in number order, then decode with base64 -d and unpack with tar -xJf -.

**Archive SHA-256:** 9112a8df1fac6b8d2cdcf8bd7c83381b242f7be8b8f46546ce1952fe42bc4ecc.

**Git blob readback for four parts (in order):** c25876f0f98c8e490177c80033335d3a4d672544; 28d62d792cd4fd21af4e8c2dc2af4f34d367f68e; dfeb2a7e816c1a11ed61f62f6f80723f84e7098d; 81a7f25f009e9f5da1e30d5142b9785a01c3805f. All four matched exact original bytes in immutable source commit.

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 main@de204c329a38a544872aa156dcc1f2c7a0442e47; Enterprise Math main@61c7e9a043a4b1daa49f8d07989f9f1fa4decf88; predecessor EC49BT branch@3c57c82f6ece117098863f8ee79f97e9d6098c8f. P000 and ACTIVE worldview unchanged.

**Authority:** Native service 0.6.11 reports research_authority_granted=false; current owner query returned CONTROL_QUOTA. This author-side portable artifact has no Source-native CLAIM, Result, independently approved Driver review or canonical math admission.

**Next EC49BV:** implement arbitrary declared finite H≤S6 and finite substring-pattern DFAs with fixed/covariant weight semantics, explicit complexity bounds and two independent exact checks; bridge no-filter aggregate to native endpoint_weight, preserving signed order and provenance.
