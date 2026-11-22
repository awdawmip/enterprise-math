# R5 O(N) finite-field certificate: exact first contraction

Frozen science: \`enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`.
Local computation (Python 3, arbitrary-precision integer modular arithmetic; no external packages): for **each** m=1,...,37, 14 witness orders \`[7,9,11,13,17,19,23,25,27,29,31,32,37,43]\`. All 518 ordered pairs \`(R_m(w), wR'_m(w))\` were computed, including the correct simultaneous count constraints for E0/E1/E2. Every root is verified to have exact order d in its finite field.

* m=1,...,36: **14/14** orders supply a certificate for a pole of order >=3; strict minimum period is 229746052653717600.
* m=37: **13/14** supply the nonzero lower-bound certificate. Order 43 has residue R=0 at the selected finite-field root. Its **actual characteristic-zero cancellation** is separately proved by the exact threshold generating-function identity in RESEARCH.md, giving strict minimum period 5342931457063200.
* 40 denominator orders have pole multiplicity >=3, with lcm 229746052653717600. Among them, only order 43 is divisible by 43.

The complete local JSON produced by \`VERIFY_MODULAR.py\` was 81079 bytes, SHA-256:
\`2ae805b37e1022de3c72e75e944a7be028b66c19048309f08939c5ba722a39ef\`.

The verifier writes the full reproducible JSON table. The hash fixes the precise author-executed version; it is not a mathematical proof or a replacement for the deterministic generator.

## All order witnesses at m=37

| d | Finite prime P | primitive root w | denominator order | R(w) mod P | D R(w) mod P |
|---:|---:|---:|---:|---:|---:|
| 7 | 10039 | 5580 | 14 | 0 | 2138 |
| 9 | 10009 | 5783 | 11 | 0 | 413 |
| 11 | 10099 | 792 | 9 | 9431 | 6391 |
| 13 | 10037 | 5992 | 8 | 0 | 44 |
| 17 | 10099 | 4343 | 6 | 8167 | 8055 |
| 19 | 10223 | 2301 | 5 | 3368 | 2404 |
| 23 | 10259 | 4778 | 4 | 8729 | 4462 |
| 25 | 10151 | 7216 | 4 | 3493 | 6380 |
| 27 | 10099 | 2017 | 4 | 0 | 2059 |
| 29 | 10093 | 7218 | 3 | 5232 | 9924 |
| 31 | 10169 | 1836 | 4 | 0 | 4053 |
| 32 | 10177 | 7318 | 3 | 7329 | 8217 |
| 37 | 10139 | 1802 | 3 | 1888 | 9411 |
| 43 | 10321 | 3215 | 3 | 0 | 6843 |

When denominator order is 3, the displayed nonzero zero-jet establishes a third-order pole. At denominator order >=4, nonzero zero-jet or first-jet suffices. The d=43 row at m=37 does **not** establish zero over characteristic zero; that is why the separate rational generating-function proof is essential.

## Independent check of the two previous finite gaps

| m | d=43 field/root | R(w) mod 10321 | D R(w) mod 10321 | Passing witness orders |
|---:|---|---:|---:|---:|
| 18 | 10321 / 3215 | 7382 | 6624 | 14/14 |
| 19 | 10321 / 3215 | 4154 | 3531 | 14/14 |

These two thresholds had been explicitly left outside the parent finite range. The new computation also establishes all other m=21,...,36, closing the whole prefix through 36.

## Reproduce

Run \`python3 VERIFY_MODULAR.py\` next to this file. Its complete 518-row JSON and assertions regenerate the finite-field data using the true five-event model. The 43 vanishing step and the upper/lower period argument are stated in RESEARCH.md.

Status: AUTHOR_EXACT_PROOF / FINITE_FIELD_EXACT_CHECK / NOT_REVIEWED. Native Researcher/Activity bookkeeping, shared owner authorization and formal Source Result remain separate.
