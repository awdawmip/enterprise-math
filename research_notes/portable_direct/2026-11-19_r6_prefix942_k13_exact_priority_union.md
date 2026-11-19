# PREFIX-942 — k=13 named-XOR exact certified union after modular floor-sum census

Date 2026-11-19; frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Parent: PREFIX-941, PREFIX-940. Scope: auxiliary named XOR two-port observer, **not** native X6.
Status: AUTHOR_PROVED / FULL_INTEGER_COMPUTED / TWO_INDEPENDENT_ENUMERATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Constructive theorem

For Q={262145,262147,...,524287} (131072 odd moduli), define W13 as the distinct ordered (a,b) for which 0<=i,j<=18 and integer t>0 satisfy

    ((13*a) XOR 2^j)-2^i = t*b.

Then the legal named trajectories F_0^i=(0,2^i) and F_(13a)^j=(13a,(13a XOR 2^j)) have identical two-port readout Phi_(a,b)(u,v)=(u mod a,v mod b) and distinct original starts.

Proof: 13a=0 mod a and the defining equation gives equal endpoints modulo b. The endpoints lie in [0,2^32) because 13*524287+2^18<2^32. Moreover

    13*262145 - 2^19 <= D <= 13*524287 + 2^18 - 1
    2,883,597 <= D <= 7,077,874 < 27*262145.

Thus all positive quotients satisfy 1<=t<=26; the finite enumeration of Q, all 361 source-bit pairs and t=1..26 is complete. QED.

## Exact new evidence

A scalar C++17 implementation and independently written vectorized NumPy implementation exhaust this finite domain, sort unique 64-bit pair IDs and subtract the earlier B/Z/S, U, V, W2, W3, D4, W5, D6, W7, D8, W9, D10 and W11 families in this exact priority order. The old B/Z/S and V closed predicates and the ten older sorted input sets come from the pinned PREFIX-940 context. The W11 set is regenerated from original published PREFIX-940 executable code and matches its published SHA-256.

Pair encoding:

    ID(a,b) = ((a-262145)/2)*131072 + ((b-262145)/2),

stored as strictly increasing little-endian unsigned 64-bit integers.

| Priority-exclusive category | Exact W13 pair count |
|---|---:|
| B/Z/S | 6,526,046 |
| U | 2,242 |
| V | 25,712 |
| W2 | 501,872 |
| W3 | 104,480 |
| D4 | 123 |
| W5 | 846 |
| D6 | 728 |
| W7 | 1,268 |
| D8 | 168 |
| W9 | 1,706 |
| D10 | 262 |
| W11 | 1,394 |
| **NEW13, not in prior union** | **5,826,892** |

Raw (a,i,j,t) witnesses: 16,796,156, agreeing exactly per t with the PREFIX-941 modular floor-sum algorithm.
Unique ordered W13 pairs: 12,993,739.

**New certified pair union = 7,558,699,988 + 5,826,892 = 7,564,526,880.**
Complement not covered by these specific certificates = 131072^2 - 7,564,526,880 = **9,615,342,304**, not established injective.

First lexicographic NEW13 example:

    a=271267, b=522505, i=3, j=17, t=7
    13a = 3526471
    (3526471 XOR 131072) = 3657543
    3657543 - 8 = 3657535 = 7*522505
    Phi_(a,b)(0,8) = Phi_(a,b)(3526471,3657543) = (0,8)

## Independent exact validation / frozen inputs

Both implementations produced byte-identical full W13.bin (12,993,739 IDs, 103,949,912 bytes, SHA-256 cca46c6869592a231c694d2d221f91ace3ec8043873c29cfbc5a1a1029dd7adc) and NEW13.bin (5,826,892 IDs, 46,615,136 bytes, SHA-256 7bf2c2654405ffe78029a3958c8679923f3f3a576fd9f30755b30c5cee355d37).

The ten older input files were extracted from the existing user-provided PREFIX939_R6_full_reproduction_bundle.zip and independently SHA-256 checked against the immutable PREFIX-940 source manifest. Exact W11 regenerated locally using original PREFIX-940 source: SHA-256 8212f0472ebe72ae93db8a205c8631f5eb96abbe952588cc08a5eb4087aeecf5. All category counts, all quotient witness counts and both binary sets agree across the two independent implementations.

Original executable sources: PREFIX942_R6_K13_EXACT_UNION_CPP.cpp, PREFIX942_R6_K13_INDEPENDENT_NUMPY.py. Full executed-source and binary-result package: PREFIX942_R6_K13_REPRODUCTION_BUNDLE.zip, with a SHA-256 manifest. Evidence is author-computed; independent mathematics review, formal Result admission, Activity linking and native X6 CLAIM are separate.

## Next mathematical question

Combine PREFIX-941's exact modular-lattice witness formula with source-preserving deduplicated (a,b) counting to avoid materializing large pair sets, and rigorously determine any transferable observer interface to native six-dimensional X6 instead of presuming one. Mother question B_fix,odd(32) in {19,20} remains OPEN.
