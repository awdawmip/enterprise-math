# R284BD — A uniform low-height control ray for exact and adversarial-noise-resilient three-channel Port identification

Date: 2026-11-20. Status: **AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED**.

**Science lineage:** R284AT → R284AX → R284AZ → R284BA → R284BB. Inherited R284AT frozen scientific blob SHA-1: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This note treats the *auxiliary named directed-Port determinant observer*; a 3×3 coefficient matrix does not define a native three-dimensional Enterprise slice or change P000. These exact integer calculations do not claim an actual native Heartbeat/BRC operation.

## Exact problem and control ray

Let C range over all 512 strictly positive matrices in {1,2}^{3×3}, with its nine entries independently chosen. Set E_ij to the named matrix unit (zero-based indices), and define

    Y_C(d0,d1,d2,z1,z2)
      = det(diag(d0,d1,d2) - C - z1 E_01 - z2 E_02).

Fix the **common, nonadaptive, nonnegative integer direction**

    v = (40,47,53,55,45)

in the order (d0,d1,d2,z1,z2). Use a single scalar reading with controls `t v`, where t is a positive integer.

**BD1 (uniform quadratic-coefficient separation).** For every candidate C,

    Y_C(t v) = 99640 t^3 + A_C t^2 + B_C t + C_C,

where A_C,B_C,C_C are integers. Across the complete set of 512 matrices, the ordered pairs (A_C,B_C) are all distinct. More specifically:

    -23042 <= A_C <= -11521
       -620 <= B_C <= 532
         -5 <= C_C <= 5,

and whenever C != C' but A_C=A_C', one has |B_C-B_C'| >= 3.

These are exact finite statements established by exhaustive integer enumeration and the independently readable complete 512-row certificate; they are not asserted for general n,H. The common cubic coefficient follows directly from determinant multilinearity: it is d0*d1*d2=40*47*53=99640. For every C, the remaining coefficients can be recovered *without interpolation error* from Y_C at t=0,1,-1:

    C_C = Y_C(0),
    A_C = (Y_C(1)+Y_C(-1)-2Y_C(0))/2,
    B_C = (Y_C(1)-Y_C(-1)-2*99640)/2.

The checker enumerates the 512 matrices in lexicographic product((1,2),repeat=9) order and evaluates each determinant using the explicit integer 3×3 formula. It verifies the coefficient identity at eleven signed and positive values of t; uniqueness of all 512 (A,B) pairs, all coefficient ranges, exactly 3,840 same-A unordered matrix pairs and minimum corresponding |Delta B|=3 are checked by complete enumeration. The companion JSON preserves every coefficient row and the exact output at t=4667. This constitutes a finite exhaustive certificate with an auditable total enumeration algorithm, not a black-box random claim.

**BD2 (a rigorous *uniform*, unbounded-noise scaling law for this finite candidate alphabet).** For every integer t>=1155, all 512 outputs are pairwise different, and their minimum absolute separation obeys

    min_{C!=C'} |Y_C(t v)-Y_C'(t v)| >= 3t-10.        (BD2)

**Proof.** Given C != C', the cubic terms cancel. Denote coefficient differences by Delta A, Delta B, Delta C. The enumerated ranges give |Delta B|<=1152 and |Delta C|<=10. If Delta A !=0, its integer magnitude is at least 1, so the reverse triangle inequality gives

    |Delta A t² + Delta B t + Delta C| >= t²-1152t-10.

If Delta A=0, BD1 ensures |Delta B|>=3 and the analogous bound is >=3t-10. For t>=1155, t²-1152t-10 >=3t-10, which is positive. Both cases prove BD2 for *all integer t in the stated unbounded range*, with no need to rerun a candidate search at each t. QED.

For adversarial real readout noise |epsilon|<=delta, with any predeclared finite delta>=0, choose

    integer t >= max(1155, floor((2delta+10)/3)+1).

Then BD2 supplies pairwise output gaps strictly greater than 2delta, hence nearest-candidate decoding from a 512-entry exact integer table recovers C after **one fixed reading**. This is a constructive, fixed-alphabet scaling result. Decoder computation/storage is finite but table-based; this claim is neither a general n/H theorem nor a polynomial-time algorithm across growing input sizes.

## Smaller explicit high-noise fixture (stronger than the uniform bound)

Exact enumeration finds an even smaller useful setting for delta=7000:

    t=4667
    (d0,d1,d2,z1,z2) = (186680,219349,247351,256685,210015)
    maximum actuator magnitude K=256685.

All 512 integer determinant outputs are distinct; the exact *minimum* adjacent gap is **14001**. Hence closed adversarial error intervals with delta=7000 are disjoint. The minimum and maximum noiseless integers are

    10128044513828982
    10128295451451151

and the maximum absolute reading width is **54 bits**. The witness pair in the lexicographic 512-matrix list has indices 268 and 452. In contrast, the earlier R284BB published one-read delta=7000 finite fixture used maximum actuator magnitude 789900; this new certified fixture uses approximately 3.08 times smaller maximum control. This is a comparison of two **specified finite fixtures**, not a claim of globally minimal actuator height.

At t=1, even the small controls (40,47,53,55,45) distinguish all 512 matrices exactly with minimum gap 1; for the uniform guarantee at t=4671, the certified lower bound is 3*4671-10=14003, and actual enumerated gap is 14013.

## Exact reproducibility

- `R284BD_star_ray_quadratic_certificate_checker.py`: Python 3 standard-library checker with an integer-only 3×3 determinant, 512 complete candidates, coefficient extraction at t=0,1,-1, eleven-value polynomial consistency checks, exact pairwise signature analysis and bounded-noise checks.
- `R284BD_star_ray_exact_verification.json`: full 512-row (A,B,C,output at t=4667) certificate, coefficient/response bounds, closest-output witness indices and the five explicit scaling results; independently recomputed using a second BigInt implementation.
- These materials use only integer arithmetic, with no floating-point tolerance or sampling. The finite certificate is as strong as its exhaustive enumeration scope; BD2 is a proof from the verified finite signature facts.
- Native Activity is separate from scientific publication. The historical researcher lineage is EM-DIRECT-E6B1DD, existing session MCP-8487128c846440d1952bfc6fa44aeb86, Activity RA-DD7D715E42D8874661313886. No formal CLAIM, native PROGRESS, Result, independent review, Working Truth or P000 change is asserted.

## Follow-up

1. Find a sparse analytic (non-enumerative) proof of distinct (A,B) for this ray, or a smaller ray; distinguish local precision improvements from a uniform dynamic-range theorem.
2. Determine the true minimal K for n=3,H=2 and delta=7000, using structured certificates rather than unbounded brute force; the observed K=256685 is a sufficient witness.
3. Combine R284BC output-diameter lower bounds with explicit ray optimization and resource-accurate table decoding; compare bits, number of simultaneous Port controls, robustness and cost.
