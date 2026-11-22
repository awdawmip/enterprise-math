# R5 extension: order-17/19 root-jet survival for every positive threshold

Date: 2026-11-22. Frozen five-event scalar scientific pin: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Status: AUTHOR_EXACT_CONDITIONAL_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED. This extends the independently saved order-23 proof in RESEARCH.md; no native P000 or X6 transfer is asserted.

## Theorems

Let R_m(q)=1-(1-A_m(q))(1-B_m(q))(1-C_m(q)) retain the original three overlapping short-block events (supports E0,E1,E2 in VERIFY_D17_D19.cpp), the long V={223,...,290}, Z={296,...,312}. Let z_d denote any primitive dth root, and dot R=q dR/dq.

1. For every positive m, R_m(z_19) ≠ 0.
2. For every positive m, (R_m(z_17), dot R_m(z_17)) ≠ (0,0).
3. In the previously archived 91 short-Q progressions, the conditional total bound on possible exceptional nonnegative k decreases from 1375 to 1168.

## Proof of infinity

At a primitive19th root, V contains 228,247,266,285 and Z contains304, so B=C=0 and R=A. At a primitive17th root, V contains238,255,272,289 and Z contains306; hence B=dot B=C=0. Therefore R=A and dot R=dot A+(1-A)dot C at d=17, with dot R=dot A+dot C whenever A=0.

Reuse the exact six-integer-cone rational threshold generating function for A_m(q) archived at enterprise-math@e0176cd68a434192899a5a1de746c2c66b5946dc:research_notes/portable_direct/r5_q_pole_collision_20261122/RESEARCH.md. Direct enumeration of its six denominator-root collisions gives maximum threshold pole order μ17=μ19=2, and all t-poles are 2dth roots. The rational function has no finite polynomial part. Thus for 1≤r≤2d, h≥0, A_{r+2dh}(z_d)=U_r+hV_r exactly, with coefficients in the degree-(d-1) integer cyclotomic ring. The Euler derivative increases threshold pole order at most one: its value on such progressions is a polynomial of degree≤2 in h. C'_m(z_17), computed explicitly from ∏_{p=296}^{312}(1-q^{mp}), is affine in h at fixed m mod34.

All needed finite evaluations use the seven nonempty signed overlap-subset DP. In the integer group ring of d cyclic exponents, a p-shift sends coefficient j to j+p mod d; q derivative of a shift carries p times the original coefficient. Subtracting the coefficient at q^(d-1) from the first d-1 positions yields the canonical basis in Z[q]/Φ_d(q), as Φ_d(q)=1+...+q^(d-1) for these primes.

For d=19, compute A_r and A_{r+38} for r=1,...,38. In each row of D17_D19.csv the indicated coefficient of U_r and V_r is strictly same-sign or has a nonzero U_r and zero V_r. Therefore every affine A_{r+38h} has a nonzero coefficient at all h≥0, proving theorem 1.

For d=17, 24 of the 34 base residues have nonzero A_r. Their indicated canonical coefficient of U_r and V_r likewise maintains a fixed nonzero sign at h≥0. The ten base residues r=13,...,17 and 30,...,34 have A_r=A_{r+34}=0, so the affine zero-order function vanishes identically for each such residue. For these ten, the exact DP and independent C derivative produce dot R at r, r+34 and r+68. The second forward difference is the zero cyclotomic vector in each case. As degree(dot R)≤2, this forces dot R_{r+34h}=U'_r+hV'_r for every h≥0. The CSV displays a canonical coordinate with U'_r nonzero and V'_r the same sign (or zero), proving theorem 2.

Every certificate is a characteristic-zero integer-cyclotomic calculation; no modulo-prime zero is treated as a complex zero. The finite 38 and 34 phase enumerations are exhaustive for the rational-period theorem, not an extrapolation from an unbounded numerical search.

## Conditional consequence for the 91 progressions

Previously fixed L=229746052653717600, Q=2L and K=L/(29·2·43). The previous 91 progressions contain, for order17, 66 bases in the nonzero R0 class and 25 in the identically-zero R0 class; the old bounds allotted one and two possible k roots respectively, totaling 66+25·2=116. All 91 have nonzero order19 R0 at k=0 and the old bound allotted at most one possible k each, totaling 91. New theorems eliminate all 116+91=207 such theoretical possibilities. Existing independent order23 reduction had already reduced the total bound to 1375, so the new sum is 1375−207=1168. This is a bound on potentially exceptional k across 91 distinct progressions, not a count of actual failures. The other root hypotheses, earlier 29/32/43 cancellation results, and project Result/Review status remain unaltered.

## Execution evidence, source and next question

Source: VERIFY_D17_D19.cpp; complete 72-row coefficient certificate D17_D19.csv. Both g++ -O2 -std=c++17 and g++ -O1 -std=c++17 -fsanitize=undefined -fno-sanitize-recover=all completed, CSVs matched byte for byte, and printed:
D17_D19: order19=38/38 order17_R0=24/34 order17_dot=10/34 S=91 S17dot=25 eliminated=207 remaining=1168 failures=0.

Executed source SHA256: 7bc2793facd282016c88a27b7df50c4134c99ee8c4120cc7bedb20e38aa10d36.
Executed CSV SHA256: d6e915249e3912ab305e53c7ab368e88a2f093873e234ca430b48aa10ef25106.

Future work: order37 R0 linear progression and root classification; then order25 and the remaining compound cyclotomic jets. Use the existing 91×12 frozen certificate and preserve full event provenance. This remains portable independent research; formal CLAIM/Result/review and Activity observation-sidecar audit are distinct operations.
