# BRC-X6: third independent fixed twelve-policy compression cone (2026-11-10)

Evidence: AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-portable TASK_RESEARCH H40, not a Source-native checkpoint or accepted Result. Scientific pin SHA256 f42f2906d77f24085c123f3ccfe9667d41caa96d is unchanged.

## Native data, theorem

Use all 96 original ports, six labeled actions and nine original signed seven-variable next-port/reward joint roots. Four source ports are (6,7,28,29), with signs (+,-,-,+). Enumerating the original 1296 labeled four-source choices under all nine joint roots gives 38 legal deterministic policies, indexed 0..37 lexicographically. C is the resulting original 24-by-38 integer incidence matrix. It retains source-action labels; full joint signed balance is checked rather than inferred from scalar totals.

Reuse the rank-13 policy chart
I=(2,8,15,21,24,28,29,31,37,0,1,3,5).
Its original row minor R=(0,1,2,3,4,5,18,19,20,21,22,6,10) has determinant -1.

Define the new twelve-policy support
S3=(2,4,5,11,14,15,17,18,23,26,29,36).
For any real chart weights w0,...,w12, define v=L3 w by:

    v0  = w0+w1-w3-w5-w8+w9+w10+w11
    v1  = w3+w5+w8
    v2  = w12-w1
    v3  = w1
    v4  = w7+w8-w11
    v5  = w2-w7-w8+w11
    v6  = w3-w7-w10
    v7  = w7+w10
    v8  = w1+w7
    v9  = w3+w5-w7-w9-w10
    v10 = w6-w1-w7
    v11 = w7+w8.

Set n3=(0,0,0,-1,1,0,0,1,0,1,1,0,0) and r3(w)=n3·w=-w3+w4+w7+w9+w10. The following **24-by-13 exact integer identity** holds:

    C[:,I] - C[:,S3] * L3 = C[:,I[4]] * transpose(n3).

Both rank(C[:,I])=13 and rank(C[:,S3])=12 are exact (also independently verified modulo 101). The fixed-support representation C_I w=C_S3 v, v>=0 exists **if and only if** r3(w)=0 and L3 w>=0; in that case v=L3 w is unique. On w>0, v>0 the feasible chart cone is relatively open and dimension 12; a fixed positive total D cuts it in dimension 11. This iff applies to S3 only, not to all twelve-policy supports.

## Small strictly positive exact witness

w=(3,1,2,4,1,1,3,1,1,1,1,1,2), sum 22;
v=(1,6,1,1,1,1,2,2,2,2,1,2), sum 22.

They satisfy r3(w)=0, v=L3 w and C_I w=C_S3 v. The exact four-by-six original numerators 22X, source order (6,7,28,29), are:

    8  1  2  4  5  2
    7  3  2  4  2  4
    5  2  5  1  3  6
    2  4  4  3  3  6

Every one of the 24 entries is strictly positive, and every row sums to 22. The 13-term chart and 12-term alternative are exact and preserve all nine original native signed full-joint observations, so minSupport(X)<=12. No minimum-support-equals-12 claim follows.

## Non-nesting relative to preceding two positive cones

Prior exact fixed-support screens on the same I are r1(w)=w6-w9-w11 and r2(w)=w2-w0-w1. For the new w, r1=1, r2=-2, r3=0, so S3's positive cone is contained in neither previous cone. Conversely, the prior S1 D18 positive example (1,1,1,1,1,1,2,4,2,1,1,1,1) has r3=6; the S2 D21 example (1,1,2,3,1,1,3,1,1,1,1,3,2) has r3=1. Neither of those positive cones is contained in S3. This supplies a third genuinely distinct eleven-dimensional compression section and a concrete small integer point outside both existing sections.

## Reproduction and boundaries

This turn ran an exact SymPy derivation on the source-frozen kernel plus a separate pure-integer reconstruction of all 38 original legal deterministic policies and nine signed joint roots. The integer verifier checked all 312 coordinates of the displayed matrix identity, ranks mod 101, weights, the four source rows and nonnesting; all checks PASS. The local reproducibility bundle also contains the unchanged source kernel, L3 matrix/certificate, exact proof text and verifier. The unchanged native kernel SHA256 is d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0.

Next: test further distinct S4 fixed-support sections or find a target-specific complete D<=511 minimum-support-13 infeasibility certificate. Retain all prior D511 reductions and Research1 J1/J2 provenance. This author-portable progress is separate from the canonical D25 original-class H0/B0 [X]U mod p² Frobenius/eta/kappa experiment. The original UR V2 four-file bundle remains unlocated: historical 94,687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. No native session, CLAIM, checkpoint, Result, review or mathematical admission is asserted here.
