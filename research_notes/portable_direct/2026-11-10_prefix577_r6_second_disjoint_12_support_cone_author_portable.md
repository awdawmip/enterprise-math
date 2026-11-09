# BRC-X6: second distinct fixed 12-policy support and positive 11D compression region

Date 2026-11-10, Asia/Hong_Kong. Scientific source pin SHA-256 f42f2906d77f24085c123f3ccfe9667d41caa96d. Status AUTHOR_PROVED / EXACT_SYMBOLIC_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is author-portable mathematics; there is no claim of native Source checkpoint, Result or Driver acceptance.

## Model and new support

Retain all 96 original native ports, six labeled actions, nine original joint signed seven-variable next-port/reward roots, source ports (6,7,28,29), signs (+,-,-,+) and all 38 legal deterministic policies. Let C be the exact 24x38 source/action integer incidence matrix. Keep inherited 13-policy chart I=(2,8,15,21,24,28,29,31,37,0,1,3,5), with independent columns.

Consider a second fixed 12-policy set S2=(1,3,4,5,11,14,17,18,23,27,29,36), distinct from the first set S=(1,5,8,12,21,23,28,30,31,33,36,37). For w=(w0,...,w12), define v=L2*w with the ordered formulas

v0=-w3+w4+w7+w9+w10
v1=w0+w1-w4-w5-w7-w8+w11
v2=w3+w5+w8; v3=w12-w1
v4=w1; v5=w0+w1
v6=w4+w9; v7=w3-w4-w9
v8=w1+w7; v9=w4+w5
v10=w6-w1-w7; v11=w7+w8.

Write r2(w)=w2-w0-w1, n2=(-1,-1,1,0,0,0,0,0,0,0,0,0,0), and delta2=e2+e8+e16+e22 in Z^24. The **exact integer matrix identity** is

C[:,I] - C[:,S2]*L2 = delta2 * n2.

Rank(C[:,I])=13, rank(C[:,S2])=12. In original independent rows R=(0,1,2,3,4,5,18,19,20,21,22,6,10), det C[R,I]=-1. Pull back S2 to this chart: its unique left-null relation is n2.

Thus, for every real w, the same 24 original native coordinates admit a nonnegative mixture using *this particular* fixed 12-policy support S2 **if and only if** r2(w)=0 and L2*w>=0 coordinatewise. The representation is unique and has the same total normalization, because L2 is integer and C_S2 has rank 12. If all 13 entries of w are strictly positive, positivity of all 12 v entries is equivalent to

w2=w0+w1,
w4+w7+w9+w10>w3,
w0+w1+w11>w4+w5+w7+w8,
w12>w1,
w3>w4+w9,
w6>w1+w7.

These conditions define a strict relative cone of dimension 12 in w-space; restricting to a feasible fixed sum D leaves a positive **11-dimensional** section. The statement is confined to S2, not a universal 12-support classification.

## Small exact integer example and non-nesting

w=(1,1,2,3,1,1,3,1,1,1,1,3,2), sum=21.
v=(1,1,5,1,1,2,2,1,2,2,1,2), sum=21.

The common original numerator matrix is

[8,1,2,3,5,2]
[7,3,2,3,2,4]
[5,2,3,1,5,5]
[2,4,2,3,5,5].

Every one of the 24 coordinates is positive; every source row sums to 21. Complete nine-root signed native joint observations were verified for the original 13 and the new 12 policies.

For this example r2=0 but the previous cone's r1=w6-w9-w11=-1. The previous D=18 example, w=(1,1,1,1,1,1,2,4,2,1,1,1,1), satisfies r1=0 and r2=-1. Therefore these are two genuinely distinct 11-dimensional positive slices, each with integer points outside the other. Neither example is claimed to have **minimum** support exactly 12.

## Proof reproduction, reuse and remaining research

The complete 24-by-13 integer identity, exact ranks and native 13-row determinant, all 38 permitted policies, all nine frozen joint roots, and the D21 / inherited D18 distinguishing points were recalculated by exact Python/SymPy verifier verify_native_cone2.py with the source-frozen native kernel. JSON exact certificate SHA-256: 57d240f2a9bd9568b8f0caf0d8732266b057c9ac63b3f0831f95cd82ebf2c7b8. The author-side local package is separate from canonical Source execution and review.

Next: combine these two precise fixed-support residual screens with additional *distinct* support cones to avoid duplicate D<=511 candidate searches; any putative minimum-support-13 result must still have a target-specific complete nonnegative 12-support exclusion certificate. Do not reuse target-dependent candidate-mask enumerations across different weight vectors as if they were global.

The original canonical D25 mother task still requires native H0/B0 divided-power module, [X]U mod p², Frobenius/eta/kappa evidence, original signed Hesse/Green observers and independent review; the mathematical claim above is static portable work. Current session/CLAIM is not verified. UR V2 four-file original 94,687-byte artifact with SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unlocated, so only genuine source recovery and eventual authorized provenance repair are pending.
