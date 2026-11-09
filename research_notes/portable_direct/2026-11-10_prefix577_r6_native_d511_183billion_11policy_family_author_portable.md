# BRC-X6 original-native: 183,121,078,608 distinct nine-bit mixtures with one fixed eleven-policy compression

Date 2026-11-10 (Asia/Hong_Kong). Frozen scientific SHA256 `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Author-portable status: **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. No native Source CLAIM, Result, acceptance or independent Driver review is asserted.

## Reuse and exact claim

Preserve the original 96 native ports, six labeled actions, source ports (6,7,28,29) with signs (+,-,-,+), and all nine signed seven-variable joint next-port/reward roots. Exhaustively check 1296 four-source action tuples; exactly 38 deterministic policies pass all nine frozen roots. Let C be the corresponding exact 24×38 original source/action incidence matrix. The inherited rank-thirteen policy chart is I=(2,8,15,21,24,28,29,31,37,0,1,3,5).

The **previously verified 199-candidate D=511 reductions** include cases 145 and 153, both represented by one fixed eleven-policy support S4=(0,1,3,6,8,12,17,28,29,30,31). Those two exact reductions are historical inputs, **not new results** in this turn. This theorem identifies and proves a complete five-dimensional parameter family on that fixed S4, with vastly more distinct valid reductions.

Choose positive integers a,b,c,d,e,f such that

    a>=1, b>=1, c>=5, d>=13, e>=5, f>=4,
    a+b+c+d+e+f = 492.

Assign the ordered weights

    v = (a,b,c,4,2,4,8,d,e,1,f)                    (support S4)
    w = (1,2,4,8,16,d-12,e-4,f-3,4,a,b+4,c-4,3)   (chart I).

All 24 source/action probabilities are strictly positive and all mixture weights on both supports are positive. Their common integer weight sum is 511 = 2^9−1, and **the following exact native identity holds for every admissible six-tuple**:

    C[:,I] * w = C[:,S4] * v    in Z^24.

Consequently all these X have minimum support at most eleven and preserve all nine original fully signed native joint observations under both representations. This is a fixed-support constructive upper bound, **not** a claim of universal nine-bit impossibility or of minimum support exactly eleven.

## Exact proof and fixed-support structure

Use the original row order R=(0,1,2,3,4,5,18,19,20,21,22,6,10). The actual native integer matrix B=C[R,I] has det(B)=−1, hence J=B^(-1) C[R,S4] is integral. Its full original 24-row lift was checked exactly:

    C[:,I] * J = C[:,S4].

In zero-based components the **complete** eleven-to-thirteen map w=Jv is

    w0=v9; w1=v4; w2=v5; w3=v6; w4=2*v3+v6;
    w5=-v3-v6+v7; w6=-v3+v8; w7=-v3+v9+v10;
    w8=v3; w9=v0-v3+v5; w10=v1+v3;
    w11=v2-v5; w12=v3-v9.

The exact ranks are rank C[:,I]=13 and rank C[:,S4]=11. S4's image in the chart lies on two independent integer hyperplanes:

    w3−w4+2*w8=0;
    2*w0+w3−w4+2*w12=0.

Substitution of the six parameters in the complete integer map proves all 24 affine coordinate identities coefficientwise. Every column of C is individually native nine-root compliant, so exact equality of mixture coordinates before projection also preserves the original complete signed joint observation.

## Exact count and distinctness

The six integer lower bounds sum to 29. Subtracting them leaves six nonnegative integers with total 492−29=463. The elementary stars-and-bars identity gives

    binomial(463+5,5) = binomial(468,5) = 183,121,078,608.

This count is a **symbolic exact family count**; it is not a claim that 183 billion independent calculations were executed. Different parameter tuples give distinct w (recover a,b,c,d,e,f from w9,w10,w11,w5,w6,w7), and C[:,I] has rank13, so their 24-component probability vectors X are genuinely distinct as well.

## Explicit checkable interior witness

Parameters (a,b,c,d,e,f)=(100,60,70,90,100,72) yield

    w=(1,2,4,8,16,78,96,69,4,100,64,66,3)
    v=(100,60,70,4,2,4,8,90,100,1,72)

and the exactly equal native four-source six-action numerator matrix 511*X is

    234   2   4   8  190   73
    233  72   4   8   94  100
    212 133   4   2   70   90
    116 160   3  72   70   90.

All 24 coordinates are strictly positive, each row sums to 511, and all nine signed joint-root checks pass. Boundary sample (1,1,5,13,5,467) also passes, including strict positivity.

## Reproduction, authorship and next unit

Independent exact integer and SymPy verification re-enumerated the original 1296 action tuples and 38 legal policies; checked original frozen nine roots, det/rank, the 24×11 matrix identity, the six affine coefficient identities, the prior 199 historical ancestor entries (index145,153), both positive examples, the complete normalization and unique-count argument. All checks PASS from a freshly extracted portable archive containing the frozen kernel, full 199 earlier certificate with prior author provenance, exact verifier, full Chinese proof, JSON certificate and hashes. The original frozen kernel is not repinned or modified.

Next independent task: classify further valid fixed supports by their *actual intersection* with this D511 chart and seek candidate-specific complete exclusion of every ≤12 support to establish a new nine-bit minimum-thirteen example. This result shows that one eleven-policy support alone compresses an enormous exact subfamily, not that 13-minimality is impossible.

Canonical D25 still requires original-class native H0/B0 divided-power [X]U mod p² and Frobenius/eta/kappa/odd Hesse-Green experiment with genuine Source owner/CLAIM. Historical UR V2 four-file original target remains 94,687 bytes and SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; original bytes were not verified in this turn. This author-side note does not promote unpublished UR materials or reprove completed UR mathematics.


## Exact all-parameter native numerators and three previous-support exclusion screens

With the six parameters as above, the **entire exact 4×6 numerator matrix** (no per-point enumeration needed) is

    [a+b+c+4, 2,     4, 8, d+e,   f+1]
    [a+b+c+3, f,     4, 8, d+4,   e  ]
    [a+e+12,  b+f+1, 4, 2, c,     d  ]
    [a+16,    b+e,   3, f, c,     d  ].

Every entry is strictly positive under the displayed parameter bounds, and every row sums to 511. In particular the first-row action-1 numerator is exactly 2, so gcd(2,511)=1: the common denominator **cannot be reduced below 511**, and nine bits are intrinsic to these exact probability values, not just to the chosen display weights.

For the three previously proved fixed twelve-policy supports on the same chart I, the exact prior residuals were r1=w6−w9−w11, r2=w2−w0−w1 and r3=−w3+w4+w7+w9+w10. The present five-dimensional family has

    r1=e−a−c,  r2=1,  r3=a+b+f+9 (>0).

Thus no family member belongs to the complete S2 or S3 fixed-support cone. For the remaining S1, its unique candidate coefficient L1(w) at index 11 is w8−w4=4−16=−12 for **every** parameter tuple. Hence **none** of the 183,121,078,608 family members belongs to the earlier three particular fixed twelve-policy cones S1/S2/S3, while each has its explicit positive eleven-policy S4 representation. This is a support-specific separation, not a global exclusion of alternate supports.
