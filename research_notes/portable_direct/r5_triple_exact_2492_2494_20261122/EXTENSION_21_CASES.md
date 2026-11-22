# R5 exact triple-cancellation extension: all 21 thresholds below 20,000

Date 2026-11-22. Status: AUTHOR_EXACT_FINITE_PROOF / EXACT_MODULAR_JET_CHECKED / NOT_REVIEWED. Frozen five-event scalar input remains enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. This is an independent portable-research extension of the proof in this directory's RESEARCH.md and of the earlier primitive-root characteristic-zero phase theorems at 74c74c94d7971bdd8594824b734e574f85d43fd2 and c9329abecc9963667647a2774b351a33c0456b0a.

## Finite-domain theorem

For **every** positive integer m<20,000 satisfying simultaneously the published primitive 29/32/43 zero-phase congruences, the strict minimum period of the quasipolynomial terms of degree at least two is

    M_m(O_m(N)) = 229746052653717600 / (29*2*43)
                = 92119507880400.

This quantification is exhaustive **only in 1<=m<20000**. No all-m minimum-period claim is made.

The complete 21 thresholds are:
2492, 2493, 2494, 4988, 6144, 8638, 8639, 8640,
11132, 11133, 11134, 11135, 11136, 13628, 13629, 13630,
16124, 17280, 19774, 19775, 19776.

## Exact proof and verification scope

The previously proved all-threshold characteristic-zero cancellation identities ensure root orders 29, 32, 43 vanish for every one of these thresholds, yielding the same upper bound L/(29*2*43).

For each threshold the new independent rational generating-function first-jet evaluator in VERIFY_EXTENDED.cpp computes the full signed, joint-event-correct numerator in F_p at primitive d-th roots for

    d = 7,9,11,13,16,17,19,23,25,27,29,31,32,37,43.

It finds **exactly** d=29,32,43 have pole-witness=false, with all other 12 roots having a provably nonzero value R_m or first derivative at pole order >=4. In each case the 12 surviving orders have LCM equal to L/(29*2*43). Modular **nonzero** evaluations certify characteristic-zero nonzero and hence the required high-order poles; modular zero evaluations are NOT used to prove characteristic-zero cancellations. The upper/lower bounds coincide. d16 has nonzero R_m at all 21 thresholds, verifying 2^4 retention.

The target list in VERIFY_EXTENDED.cpp is the same as the earlier verified algorithm VERIFY_TRIPLE.cpp with the 21 actual thresholds plus 17 unchanged small regression targets. Both compile from standalone C++17 source with:

    g++ -std=c++17 -O2 -Wall -Wextra -Werror -fsanitize=undefined -fno-sanitize-recover=all VERIFY_EXTENDED.cpp -o verify_extended
    ./verify_extended > EXTENDED_OUTPUT.csv 2> EXTENDED_LOG.txt

Actual local execution: completed all 15 primitive orders with 13 original integer-DP anchor checks passing and no undefined-behavior sanitizer errors; output includes **570 data rows** (38 target thresholds x 15 orders), 571 lines with header. The local full output SHA256 is `9c1049391c673822009d2420ef650050cddafeb4843332110fcdcfa0e0656954`, the local C++ SHA256 is `9e5f0b366b80b88af5c4bcf95a5e07cb5bb2899c298573b0bbe3327c4427c03d`, and the Git blob of the tested source is `f53fc501139ca03bce36fd6a565c3a0cdc850981`. The complete output is regenerable exactly from this source; the corresponding binary/CSV can be retained locally but is not required for the mathematical proof.

As an independent finite enumeration, the congruence intersections are exactly the list above for 1<=m<20000. Across **all** positive integers these triple-zero classes occur in 91 residue classes mod 79808, a statement about root cancellations only. The present minimum-period equality is proved for the 21 listed cases.

### Selected order-16 first-jet evidence

Every listed pair below is (R_m, q*dR_m/dq) mod 10177 at primitive order 16 root 1750; R_m is nonzero throughout:

| m | R_m mod 10177 | Euler derivative |
|---:|---:|---:|
| 2492 | 132 | 2757 |
| 2493 | 5899 | 275 |
| 2494 | 794 | 1453 |
| 4988 | 264 | 6832 |
| 6144 | 5375 | 3304 |
| 8638 | 5097 | 4114 |
| 8639 | 881 | 5642 |
| 8640 | 1516 | 5353 |
| 11132 | 5286 | 8748 |
| 11133 | 9096 | 6922 |
| 11134 | 5891 | 4187 |
| 11135 | 4754 | 3551 |
| 11136 | 7834 | 2948 |
| 13628 | 5418 | 8774 |
| 13629 | 4818 | 6869 |
| 13630 | 6685 | 469 |
| 16124 | 5550 | 10118 |
| 17280 | 3032 | 7379 |
| 19774 | 811 | 7624 |
| 19775 | 5635 | 3004 |
| 19776 | 9350 | 1299 |

## Next scientific problem

The all-positive-m exact least-period function remains open. Find symbolic root-phase classifications for the other survivor orders, or derive a threshold-generating-function recurrence to prove the 12-order nonzero property on all 91 triple-zero classes, or find exact counterexamples. Do not repeat the already checked 21 cases or change the frozen input, P000, or the control Task/owner.
