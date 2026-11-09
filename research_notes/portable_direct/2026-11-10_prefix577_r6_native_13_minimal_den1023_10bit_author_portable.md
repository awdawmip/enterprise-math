# BRC-X6: 10-bit, full-positive, original-native 13-term-minimal strategy (2026-11-10)

**Status:** AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-portable only; no native Source CLAIM, checkpoint, Result or independent Driver review.

**Frozen scientific input** SHA256 f42f2906d77f24085c123f3ccfe9667d41caa96d: the original 96 ports, six labeled actions, nine frozen roots and signed seven-variable full next-port/reward joint observation. Source ports (6,7,28,29), signs (+,-,-,+). Rebuilding all 6^4=1296 candidate action tuples gives exactly 38 legal deterministic policies, all verified over all nine roots.

## New theorem and explicit witness

The following 24 positive source/action probabilities have **minimum deterministic support exactly 13 among the original 38 admissible policies**:

    X = 1/1023 * [
      [513,   2,  4,   8, 112, 384],
      [419, 224,  4,   8,  48, 320],
      [208, 320, 97,   2, 100, 296],
      [144, 256,  3, 224, 100, 296]
    ]

Every row totals **1023**, which has exactly **10 binary bits**. The 13 original admissible policy IDs

    I=(2,8,15,21,24,28,29,31,37,0,1,3,5)

have exact positive integer weights

    w=(1,2,4,8,16,32,64,128,256,128,192,96,96),

whose total is 1023. Exact reconstruction of the 24 source/action marginals and all nine signed full-joint root observations passes; hence minSupport(X)≤13.

## Exhaustive 12-term exclusion

Let C be the 24x38 original-native binary incidence matrix. Take R=(0,1,2,3,4,5,18,19,20,21,22,6,10), A=C[R,:], B=A[:,I], Q=B^{-1}A. Symbolic exact calculations give rank(C)=rank(A)=13, det(B)=-1, integral Q and max|Q_ij|=2, with Q[:,I]=I_13.

**Inherited exact author theorem (no new credit):** every 13x13 minor of A has absolute value at most 3; previously published exact proof at commit e38d623754636b3e2c2d31935752295e12a27023.

If X had a nonnegative representation using ≤12 original legal policies, extend its column span to twelve independent native columns T. The nonzero integer cofactor d_i=det([A[:,T],B[:,i]]) belongs to [-3,3]^13 by the inherited minor bound, satisfies d·w=0, and has at least 12 independent legal columns in zero mask Z(d)={j:dᵀQ[:,j]=0}. Therefore rank(Q[:,Z(d)])≥12 is necessary.

Two separately coded C++17 exact exhaustive meet-in-the-middle enumerators split the thirteen coefficients 6+7 and 7+6, respectively. They enumerate every bounded d with d·w=0 and produce **byte-identical** mask lists, SHA256 3dcb544d26d8058d12dad85c192a2f4928a0cd5d46b02dc113c422ea97bd5361.

| Exhaustive object | Exact count |
| --- | ---: |
| Relations, including d=0 | 42,364,049 |
| Nonzero relations | 42,364,048 |
| Nonzero relations with at least 12 zero columns | 232,470 |
| Distinct eligible masks | 77,267 |
| Mask ranks 6,7,8,9,10,11,12 | 86; 1,989; 21,934; 35,397; 16,126; 1,723; **12** |

Ranks were computed modulo p=2^61-1 and all twelve rank-12 cases rechecked by exact-rational SymPy. Every nonzero d bounds rational rank by 12. Because |Q_ij|≤2, each nonzero 12x12 minor is at most 48^6=12,230,590,464 < p by Hadamard, so rational rank 12 cannot fall below 12 mod p.

For the **only twelve rank-12 masks**, the following small integer Farkas separators y have yᵀQ[:,j]≥0 for **every** column j of that mask, but y·w<0. Every dot product is verified exactly by the reproducible Python verifier:

| Mask | 13-component integer y | y·w |
| --- | --- | ---: |
| 10881109462 | (0,0,0,0,1,0,-1,0,-1,1,0,0,1) | -80 |
| 42815993880 | (0,1,1,0,0,1,0,0,0,-1,0,0,-1) | -186 |
| 45375335877 | (0,0,0,0,1,0,-1,0,-1,0,-1,-1,1) | -496 |
| 70473775696 | (1,1,1,0,0,1,0,-1,0,-1,-1,0,0) | -409 |
| 75301418640 | (1,0,1,0,0,1,-1,0,0,-1,-1,0,1) | -251 |
| 80610872338 | (-1,2,2,1,2,1,-1,0,-1,1,0,1,-2) | -205 |
| 145627318119 | (0,0,0,-1,1,-1,0,0,0,0,0,-1,0) | -120 |
| 146865844206 | (0,0,0,0,0,0,1,-1,0,0,0,0,0) | -64 |
| 173044616225 | (1,1,-1,0,1,1,-1,-1,0,0,-1,-1,0) | -433 |
| 173045718049 | (1,1,-1,1,1,1,-1,-1,0,0,-1,-1,0) | -425 |
| 206828572647 | (0,0,0,0,0,-1,1,0,0,0,0,-1,0) | -64 |
| 216790176006 | (0,0,0,0,0,0,1,0,0,-1,0,-1,-1) | -256 |

Every rank-12 masked nonnegative cone is separated from the target; rank≤11 masks cannot contain twelve independent columns. Thus no ≤12-policy nonnegative representation exists, proving **minSupport(X)=13, D=1023, 10 bits**.

## Exact reproduction and provenance

The complete clean-unzipped **14-file** research package includes the frozen original kernel, exact 13x38 chart, two differently split C++17 enumerators, modular rank checker, both byte-identical sorted mask files, exact rational/nine-root verifier, twelve dual certificates, JSON certificate and full mathematical proof. It was freshly compiled and rerun from a clean ZIP extraction. Research ZIP SHA256 c89c2a67ff65364613ed72eacdec886fb9a0bacdab7acc4205d0bdf4325c673c; exact JSON certificate SHA256 4e401da4395f817fdfd15f82ef09a83276afa8b91fc85eabac6cbfdbc6cecd9c. The earlier numerical MILP was only a candidate finder, not an infeasibility proof.

This is the new 10-bit increment over prior 11-bit D2023 author evidence at commit 7afb2c106aa7ad282d60b52ef99a57c055889fcf; earlier minor-3 and native policy-discovery evidence retain their authorship. Current canonical Source D25/H0-B0 fixed native frontier remains separate and requires actual own execution session and winning CLAIM for formal writes. Historical genuine UR V2 four-file bundle remains unresolved: 94,687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. Next portable inquiry: a ≤9-bit explicit native witness with exact completeness certificate, or a scoped lower-bound lemma.
