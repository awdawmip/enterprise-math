# R5 primitive-29/32 phase and surviving-order evidence

Frozen input: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15; no formal CLAIM; independent author check, NOT_REVIEWED.

## Exact characteristic-zero phase output
```text
order=29 zero phases: 54 55 56 57 58
order=32 zero phases: 60 61 62 63 64
```
Algorithm: `VERIFY_PHASES.cpp`, exact integer quotient rings Z[x]/(x^29-1), Z[x]/(x^16+1), full inclusion-exclusion preserving joint original-event counts. Periodicity is proved by the symbolic generating-function derivation in RESEARCH.md; only base phases are enumerated. Sanitizer execution returned zero diagnostics.

## Matching lower-bound modular coverage

Program `CHECK_SURVIVORS.cpp` evaluates complete signed event numerator and Euler jet over split prime fields with primitive d-th root, for every m=112..116 and 124..128 and d in {7,9,11,13,16,17,19,23,25,27,29,31,32,37,43}. This includes 150 selected m,d rows, plus 5 d=16 regression rows at m=60..64; full original local CSV contains 155 data rows, SHA256 cf8ed8c223898a809205821903195d5f8bb255e186f5a4d69b15d5f5033c55b9.

Every m=112..116: only d29 has a zero witness; all other 13 necessary orders have nonzero R or, with denominator pole order >=4, nonzero first Euler jet.

Every m=124..128: only d32 and d43 have zero witnesses; every other necessary d has a nonzero witness. Primitive d16 separately has nonzero witness (retains factor 16).

The full modular zero rows are not used for characteristic-zero vanishing: that is independently proved by Theorem A and the prior exact d43 theorem. Each modular **nonzero** witness is a sufficient characteristic-zero nonvanishing certificate.

For m=124..128, the primitive d43 evaluation gives R0=0 and first jet respectively 8367,4222,3602,5112,7663 modulo 10321; its denominator pole order is 3, so the first jet is not enough to retain d43. Other modulus/root parameters are emitted deterministically by the verifier.

The source code and numeric summary support strict least periods L/29 at 112..116 and L/86 at 124..128. Neither future range nor the triple-contraction large-m upper bound has a matching lower-bound proof.

## Verification record
`VERIFY_PHASES.cpp`: local tested SHA256 670bd356b97dd139e0744ac85f0784b238d2e0eb41629b86c8c5ccd0047c120e; `CHECK_SURVIVORS.cpp`: 7851e447341f931d544c994fd61ab8fcc41658ded8558d69833db98abab177a1. C++17, exact integer and modular arithmetic; UBSan checked `VERIFY_PHASES`. Independent review: NOT_REVIEWED.
