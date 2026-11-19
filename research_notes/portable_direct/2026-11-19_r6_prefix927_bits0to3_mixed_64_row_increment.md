# PREFIX-927 — Four named XOR source bits, exact union and new collision certificates

Date: 2026-11-19. Lane: 进取数论研究6. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. Exact dependency: PREFIX-919/920 (mixed zero-flip), PREFIX-923/924/925 (bucket/zero-zero/same-start) and PREFIX-926 (bit-0 64-row certificate). Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_ENUMERATION_AGREEMENT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model and goal

Let p=32, N=2^32, Q={262145,262147,...,524287}, M=|Q|=131072. Named traces are Z_x=(x,x) and F_x^i=(x,x XOR 2^i) with source i retained, 0<=x<N, 0<=i<32. Two-port observer: Phi_(a,b)(u,v)=(u mod a,v mod b), (a,b) in Q^2. This is an auxiliary discrete BRC/provenance-aware observation model, NOT an X6-native dynamical embedding.

Let B be PREFIX-923's two-sided bucket-capacity collision set, Z the zero-zero set (lcm(a,b)<N), and S the same-start source-collision set (some 1<=d<=31 satisfies 2^d = +/-1 mod b). PREFIX-925 independently counted |B union Z union S| = 7,462,508,971.

Let R={400001,400003,...,400127}, with 64 odd second-port moduli. PREFIX-926 counted the source-bit-0 constructive family T_0 and its time reversals outside B union Z union S: 437,560 ordered pairs, with sorted little-endian uint64 index SHA256 f8e594257de9a99aa6de4be42d9dde79ba0427a5105c60bfa715d92bd25a60e4.

## Theorem 1 — Named source-bit-i witnesses and reversible orientation

For any 0<=i<32 put H=2^i and A=ka for k>=1.

(a) If A<N and b divides (A-H), then the distinct named trajectories F_0^i=(0,H) and Z_A=(A,A) collide under Phi_(a,b).

(b) If A+H<N and b divides (A+H), then F_H^i=(H,0) and Z_(A+H)=(A+H,A+H) collide.

Both are valid because 0,H,A,A+H lie in [0,N) under their respective hypotheses; start differences are multiples of a, while endpoint differences are multiples of b. Reversing a named trace exchanges start/end and preserves its bit label; hence (a,b) also certifies the transpose (b,a) in the swapped-port observer. No zero-difference or source-unlabeled inference is used.

## Theorem 2 — Exhaustive constructive enumeration for bits i=0,1,2,3

Fix b in R, i in {0,1,2,3}, and k in [1, floor((N-1)/262145)]=[1,16383]. Since b is odd, any solution of ka = +/-2^i mod b implies gcd(k,b)=1. Let v=k^-1 mod b.

The complete possible a values in Q satisfy:
- case (a): a = (2^i*v) mod b;
- case (b): a = (-2^i*v) mod b.

Because width(Q)=262142<b for all b in R, each residue class has at most one a in Q; adding b once if the least residue is below 262145 locates it. Check odd parity, Q bounds, the exact A+H<N cutoff for case (b), and the actual divisibility. No candidate for these two explicit witness forms is omitted.

For bit i, collect these pairs, transpose them, and keep each orientation only when outside B union Z union S, with S tested against that orientation's second modulus. Encode (a,b) as the 64-bit integer ((a-262145)/2)*131072+(b-262145)/2. Duplicate parameter witnesses and orientation overlaps are removed by exact integer sets, never by addition of aggregate counts.

## Exact census and independent check

The full 64-row domain is explored for each of four source bits. Two distinct algorithms agree:
- Python iterates b,k, inverts k modulo b, constructs the actual named trajectories and checks both observed residues.
- C++17 iterates b,a, inverts a modulo b, solves the two unique k residues, directly checks both observed residues, and deduplicates sorted integer pair indices.

| bit i | valid (b,k,sign) witnesses | distinct ordered pairs outside B/Z/S | progressive union through i |
|---|---:|---:|---:|
| 0 | 386,923 | 437,560 | 437,560 |
| 1 | 385,892 | 435,589 | 654,668 |
| 2 | 385,639 | 436,510 | 873,058 |
| 3 | 387,049 | 437,287 | 1,091,862 |

The source-bit increments beyond preceding bits are 217,108 (i=1), 218,390 (i=2), 218,804 (i=3). Relative to the already published PREFIX-926 bit-0 certificate, the exact new increment is 654,302 ordered pairs. Consequently:

|B union Z union S union T_0 union T_1 union T_2 union T_3| = 7,463,600,833;
complement in Q^2 = 17,179,869,184 - 7,463,600,833 = 9,716,268,351.

Python and independent C++17 compute the same sorted little-endian uint64 final-union digest:
SHA256 2f03e83c1df067b926ed075e2bf641bdedfc12480590994ede45691d37aa7ad0.
The Python bit-0 standalone digest equals PREFIX-926's immutable published digest f8e594257de9a99aa6de4be42d9dde79ba0427a5105c60bfa715d92bd25a60e4, an exact backward compatibility check.

An explicit first new bit-1 witness outside B/Z/S and the old bit-0 union is (a,b)=(354267,400123), i=1, k=3403, A=1,205,570,601: F_0^1=(0,2) and Z_A=(1205570601,1205570601). Here A-2=1,205,570,599=3013*400123, while A=3403*354267. Both observed pairs are (0,2). Other new examples: i=2 at (354257,400127), k=11497, and i=3 at (354257,400095), k=8711, using the plus branch.

## Scope, reproducibility and open next step

The theorem exhausts precisely these 4 source-bit witness templates over the stated 64 b rows and their transposes, relative to the three indicated old certificate families, with exact integer arithmetic. It does not deduplicate against every other historic signed-power, mixed, double-flip or complete-row certificate. The global mother question B_fix,odd(32) in {19,20} remains open; no native X6 statement follows without a typed embedding/readout and residual-provenance preservation proof.

Reproduce with Python 3 standard library script PREFIX927_R6_BITS0TO3_ROW_CHECK.py and independent C++17 -O3 script PREFIX927_R6_INDEPENDENT.cpp. The C++ program writes the final sorted pair IDs as little-endian uint64; compare its sha256sum with the result JSON. No floating point or stochastic input is used.

Next discriminating work: extend the four-bit scan to all 32 sources and/or other b rows, then intersect the resulting actual ordered-pair set with earlier complete-row/double-flip witness sets; retain explicit orientations and named-source identity rather than interpreting aggregate coverage as a fully global union.
