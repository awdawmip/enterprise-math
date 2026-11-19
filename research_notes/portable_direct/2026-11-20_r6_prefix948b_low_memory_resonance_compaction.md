# PREFIX-948B — Low-memory resonance-aware pair generation

Date: 2026-11-20. Scope: a computational continuation of PREFIX-948 on the **same frozen scientific input** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`, the same auxiliary named-XOR observer, and the complete Q19 odd modulus population. This addendum creates no new claims about native X6/BRC dynamics, independent Review, formal acceptance or new coverage.

PREFIX-948 proved a complete determinant split for k=21 and 23. The exhaustive 722-choice signed-bit check established that the zero-determinant branch in this domain yields precisely the diagonal family \`(a,a)\` except the single admissible exception \`a=274627\`, because 21*a has every low 19-bit position equal to 1 there. The earlier primary determinant implementation stored 10,541,739 repeated resonance witness combinations in memory prior to deduplication.

The new C++17 implementation \`PREFIX948_R6_LOWMEM_DETERMINANT.cpp\` uses the same *proved* finite resonance classification but generates these 131,071 diagonal pair IDs directly once each. It still exhaustively checks every nonzero-determinant signed-index/t/m configuration and retains exact integer quotient, bit-sign and odd interval checks.

The observed standalone local process results, for the exact same population on the same execution environment, are:

| Path | Elapsed execution | Peak RSS | Full intersection |
|---|---:|---:|---:|
| Original determinant enumerator | 1.03 s | 132,824 KiB | 137,274 |
| Low-memory determinant enumerator | **0.38 s** | **2,688 KiB** | **137,274** |

The low-memory result contains 8,711 nonresonant witness configurations, 131,071 resonance-generated diagonal pairs and one excluded all-ones diagonal. It produces **byte-for-byte identical** sorted 1,098,192-byte pair IDs to both earlier independent complete computations, with SHA-256 \`54c35a06874167484f0028443be45d3b03e69bc3bdf0e64fc97cf371522f6223\`. This is an exact result, not a sampling test. The observed time/RSS exclude compilation and other preparation and do not imply universal speedups for arbitrary core pairs.

This method reduces memory by avoiding repeated indistinguishable *pair* IDs while preserving the distinct source-labeled witness counts separately as evidence in PREFIX-948. The broader question is whether a general resonance class can be represented compactly without losing its named-source witness multiplicities. Mother \`B_fix,odd(32) in {19,20}\` remains open.

Status: AUTHOR_PROVED / THREE_EXACT_FULL_DOMAIN_IMPLEMENTATIONS_AGREE / NOT_REVIEWED / NOT_ADMITTED. No protected Activity write or shared CLAIM is asserted.
