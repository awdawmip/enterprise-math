# BRC-X6 original native 11-bit, 13-term-minimal full-positive witness — 2026-11-10

**Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED; author-portable proof only. Neither a current Source Task CLAIM nor Driver acceptance is asserted.

**Scientific input:** SHA256 f42f2906d77f24085c123f3ccfe9667d41caa96d. Original 96 ports, six labeled actions, all nine frozen roots and full signed seven-variable next-port/reward joint observations. Source ports (6,7,28,29), signs (+,-,-,+). Exactly 38 of the 1296 original deterministic policy tuples are legal across all nine roots.

## New explicit 11-bit theorem

The following probability matrix has minimum deterministic support **exactly 13 among the original 38 legal native policies**:

    X = (1/2023) * [
      [1513,  2,   4,   8, 112, 384],
      [1265,378,   4,   8,  48, 320],
      [ 592,728, 251,   2, 154, 296],
      [ 528,664,   3, 378, 154, 296]
    ]

All 24 numerators are positive; every row sums to 2023, which uses **11 binary bits**. The 13 legal policy IDs (zero-based original frozen enumeration) are

    I=(2,8,15,21,24,28,29,31,37,0,1,3,5).

Their respective integer convex coefficients, divided by 2023, are

    w=(1,2,4,8,16,32,64,128,256,512,600,150,250).

Direct exact integer reconstruction reproduces all 24 source-action marginals and all nine signed full-joint root observations. Therefore minimum support is at most 13.

## Exact exclusion of 12-term representations

Let C be the 24x38 binary native source/action incidence matrix. Select chart rows R=(0,1,2,3,4,5,18,19,20,21,22,6,10), set A=C[R,:], B=A[:,I] and Q=B^{-1}A. Exact integer/rational reconstruction gives rank(C)=rank(A)=13, det(B)=-1, integral Q and max |Q_ij|=2. The target has B-coordinates w.

**Inherited (not recredited) theorem:** every 13x13 minor of A has absolute value at most 3; independently archived exact author proof is commit e38d623754636b3e2c2d31935752295e12a27023. This is a stated dependency of the new result.

Suppose a nonnegative representation used at most 12 native policies. Extend their span to 12 independent native columns T. For i=0,...,12 define the integer cofactor d_i=det([A[:,T], B[:,i]]). Nonzero d belongs to {-3,...,3}^13 by the sharp minor bound; since A[:,I] w lies in span(T), we have d·w=0. All T-columns lie in the zero-column mask Z(d)={j:d^T Q[:,j]=0}; hence rank(Q[:,Z(d)])>=12.

Two independently coded exact C++17 MITM enumerators with different 6+7 / 7+6 radix-seven splits exhaust every bounded d satisfying d·w=0 and produce byte-identical sorted masks. Integer counts:

- 17,663,255 relations including d=0; 17,663,254 nonzero.
- 105,124 eligible nonzero relations with at least 12 orthogonal legal columns.
- 40,191 distinct eligible masks, with ranks 6:93, 7:1644, 8:13397, 9:17068, 10:7229, 11:756, 12:**4**.
- SHA256 of both byte-identical mask files: 6d742c17c79faca73de82063e8ba90fc3e3137c9b5967cc5c63a9bb4a2ed469b.

Ranks are determined modulo p=2^61-1, and four rank-12 cases were independently rechecked using exact rational SymPy. The nonzero d implies rational rank <=12. Because max|Q_ij|<=2, Hadamard bounds each 12x12 minor by 48^6=12,230,590,464 < p; therefore a rational rank-12 case cannot disappear modulo p.

Four small **integer Farkas separators** y are explicitly certified below. In each row, y^T Q[:,j]>=0 for every legal column j of the listed rank-12 zero-mask but y·w<0. Every inequality was checked in exact integer arithmetic:

| Rank-12 zero mask | Integer y, 13 components | y·w |
| --- | --- | ---: |
| 35740265513 | (1,1,1,-1,1,0,-1,-1,-1,0,-1,0,0) | -1033 |
| 45508472261 | (0,0,0,0,1,0,-1,0,-1,0,-1,-1,1) | -804 |
| 79082381590 | (0,0,-1,0,0,1,1,0,1,-1,0,-1,-1) | -564 |
| 210571785383 | (0,-1,-1,-1,0,-1,-1,-1,0,0,0,-1,0) | -388 |

Every rank-12 mask's nonnegative cone is separated from w, and lower-rank masks cannot contain 12 independent T-columns. All possible 12-term decompositions are excluded. Combining exact upper and lower bounds gives:

**minSupport(X)=13, common denominator D=2023 (<2048), binary length=11.**

## Scientific reproduction, lineage and remaining work

The complete 13-file author-portable ZIP includes frozen native kernel, exact chart, two independent C++ enumerators, modular rank checker, byte-identical mask lists, exact SymPy/nine-root verifier, JSON certificate and expanded derivation. Archive SHA256: 331c516fbcd109a36674da2302e8f70b41a6e8d16647ca31b89da83ff7f8bc5b. Deterministic JSON certificate SHA256: 6d186301819829c32831cf921384daf080a37b6492f06d14e1f338dc03cc7d0b. The full clean-unzip compilation/exhaustive enumeration/exact verifier passed.

This advances the prior 12-bit D=3523 result (commit 6ef530dd55b956789503019fb109fd53c88fe081) without repeating credit for the inherited 38-policy original classification, native minor-3 theorem or the D25 Source frontier. A numerical mixed-integer solver was used only to select candidate weights; it is not the proof of optimality.

The Source D25 native task still requires authenticated original-class H0/B0 divided-power evidence and valid execution authority. Historical UR V2 four-file authentic source remains unlocated: target 94,687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. Next portable question: search for a full-positive ten-bit or shorter exact 13-minimal native certificate or establish an explicit bounded obstruction, preserving all original observation and author provenance.
