# R284BY — A 34-bit single-read star-Port code with exact circular gap 41

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / COMPLETE_FINITE_EXHAUSTIVE_CERTIFICATE / NOT_REVIEWED.
Mode: independent portable auxiliary algebra; no native X6/BRC physical inference or formal Task CLAIM.

## Frozen model and scientific input

Continue the verified R284BX source, without changing its matrix population or frozen leaf controls:
- Predecessor: \`research_notes/portable_direct/R284BX_EXACT_28_TO_34_BIT_STAR_PORT_CODE_FRONTIER_20261120.md\` at Git blob \`dd2d8e941ff5fdfb295af76f5d721eb35054699a\` (read from canonical main 2026-11-20).
- For each row-major binary matrix C in {1,2}^{4x4}, define
  F_C = det(diag(d0,6,13,d3) - C - z1 E01 - z2 E02 - z3 E03) mod p.
- Exactly one non-adaptive circular observation is obtained, with adversarial real error of radius rho on R/pZ. Every candidate C must decode.

The new fixed parameters are:

| value | exact integer |
|---|---:|
| p (prime, 34 bits) | 17179869143 |
| d0 | 1120822 |
| d3 | 1651130 |
| z1 | 390139 |
| z2 | 394465 |
| z3 | 1497642 |

Only these five free controls differ from the frozen predecessor. The modulus p is the same as R284BX's original 34-bit instance.

## Exact finite theorem

The above fixed mapping has 65536 pairwise distinct residues with exact minimum circular gap **41**. Thus a nearest-center decoder recovers every C for every real circular error \`0 <= rho < 41/2 = 20.5\`; the same fixed mapping fails uniform recovery for \`rho >= 20.5\`. For integral measurement errors the maximum symmetric correctable range is **±20**.

One pair attaining the exact minimum is

- A = [2,2,2,2, 1,1,2,2, 2,1,2,1, 1,1,2,2], F_A = 11862732159.
- B = [2,1,1,1, 1,2,1,1, 2,1,1,2, 2,1,2,1], F_B = 11862732200.

Their difference is 41. All other pairs are at circular distance at least 41 by complete sorted-neighbor enumeration, including the wraparound gap.

Relative to the R284BX certified 34-bit instance (gap 34 and integer errors ±16), this is an exact gain of seven units of minimum circular separation and four units of symmetric integral error tolerance at unchanged bit length. Relative to the 35-bit R284BW witness (gap 59), it remains a lower-gap, lower-bit alternative. No global 34-bit optimum or 27-bit impossibility is asserted.

## Proof, computation and observation fidelity

The determinant is evaluated using the predecessor's exact nine-coefficient integer polynomial (U,V,p1,p2,q1,q2,q3,J,K):

  F = d0(U*d3+V)-z1(p1*d3+q1)-z2(p2*d3+q2)-z3*q3+J*d3+K.

The identity follows by ordinary 4x4 cofactor expansion. The independent checker also calculates a signed 24-permutation Leibniz determinant for 256 regularly spaced matrices to cross-check coefficient indexing and implementation. Python arbitrary-precision integers are used in the saved checker; there is no floating-point arithmetic.

Exhaustive proof certificate: enumerate the Cartesian product {1,2}^16 in lexicographic row-major order, compute the exact residue for each of the 65536 matrices, sort residues together with matrix indices, and take the minimum of the 65535 consecutive differences plus the circular wrap gap \`p-last+first\`. The returned minimum is exactly 41 with multiplicity one and no duplicates. Sorting's neighbor principle proves this covers every unordered pair, not just sampled pairs. A complete nearest-center decoder test at errors -20, 0, +20 for all 65536 matrices returned the original candidate 196608/196608 times. A direct triangle inequality on the circle proves the real-radius guarantee for any nonintegral error as well.

The checker independently confirms p is prime by trial dividing all odd divisors up to floor(sqrt(p)), reports the witness pair above and the SHA-256 of row-major 8-byte big-endian residues:
\`d003d4087695d3e38fcc044d0a49385fd59d5f633c44421c0989e3c0c65961de\`.

Reproduction:
\`python research_notes/portable_direct/R284BY_34bit_gap41_checker.py\`
produces \`R284BY_34bit_gap41_verification.json\` in the same directory.

This result certifies the *specified* finite star-Port observation code and noise model, not a lower bound across all possible controls. The complete source-to-observer residual is retained: distinguishing codewords may share the preceding nonconstant signature while differing in the hidden C03 coordinate; the full residue decoding (rather than only the signature quotient) is what yields invertibility.

## Remaining scientific questions and control state

1. Search for a 34-bit code with gap >= 42 or the frozen-pair maximum 59, or prove an upper bound by an exact certificate; a bounded unsuccessful search would not establish impossibility.
2. Find a 27-bit lossless code, or derive a genuine impossibility bound. Incorporate search/verification time, the 65536-entry decoder table and preprocessing into any complexity claim.
3. Study branch/port residual preservation when compressing the table, without claiming a native six-axis mapping until an explicit embedding and observer interface are proved.

The R284BX source was read and its scientific pin retained. Historical provenance: the prior portable line was recorded as EM-DIRECT-E6B1DD; this run did not acquire a new authenticated Researcher SID, winning CLAIM or Result authority. Native owner check \`r1-20261120-1856-owner-inventory\` was WAITING_RESOURCE (GitHub primary rate limit, automatic same-request recovery) when this note was prepared; it grants no owner permission. Research Activity semantic association and independent review remain pending.
