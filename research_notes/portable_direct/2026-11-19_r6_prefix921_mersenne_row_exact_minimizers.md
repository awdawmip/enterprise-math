# PREFIX-921 — Mersenne-row exact minimum of named-XOR collision mass

Date: 2026-11-19 (Asia/Shanghai), 进取数论研究6. Scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`, reusing PREFIX-917/918/919/920. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / DIRECT_WITNESSES_AUDITED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model and theorem

Let (N=2^{32}) and consider **named** traces (Z_x=(x,x)) and (F_x^i=(x,x\oplus2^i)), for (0\le x<N), (0\le i<32). Observe (Phi_{a,b}(u,v)=(u\bmod a,v\bmod b)), retaining the trace type and source-bit label in the underlying domain. A collision is an unordered pair of distinct named traces having the same observation.

**Theorem.** Fix the odd second-port modulus (b=2^{19}-1=524287). Among all (131072) odd (a\in[262145,524287]), the least number of colliding unordered trace pairs is exactly
[
\boxed{13\cdot 2^{31}=27,917,287,424}.
]
Its complete minimizer set is exactly
[
\boxed{\{518271,521279,522783,523535,523911,524099,524193\}}.
]
For these seven moduli all collisions have equal starting states; every other (a) has at least one additional **different-start** collision. Consequently this entire (b=524287) row is noninjective, including its seven minima.

## A. Exact universal equal-start contribution

When starts agree, a zero trace and a flip cannot collide: the endpoint difference is a power of 2, not divisible by odd (b>1). For two distinct flips at bits (i,j), the endpoint difference is one of (pm2^i\pm2^j). Since (2\) has multiplicative order (19) modulo (2^{19}-1) (19 is prime, (2^{19}\equiv1) and (2\not\equiv1)), the only possible distinct-source congruences with (0\le i,j<32) are (j=i+19) with matching XOR signs; the opposite-sign congruences are impossible because the order is odd. There are 13 unordered bit pairs ((i,i+19)), and each has exactly (N/2) starting states with matching bit values. Hence equal-start mass is exactly (13N/2), independent of (a).

For example (F_0^0=(0,1)) and (F_0^{19}=(0,524288)) collide at every (a). This also shows why a failure to find different-start collisions is **not** an injectivity certificate.

## B. A sharp modular obstruction to different-start collisions

For different starts, order them (x<y). First-port congruence forces (y-x=ka) with (1\le k\le K(a)=\lfloor(N-1)/a\rfloor). Whatever zero-or-one-flip types are used, endpoint congruence requires
[
ka\bmod b\in S_b,qquad
S_b=\{0\}\cup\{\pm2^i\bmod b\}\cup\{\pm2^i\pm2^j\bmod b:0\le i,j<32\}.
]
This necessary condition covers zero/zero, zero/flip and two-flip, with no assumptions about XOR carry windows.

At (b=524287), the powers (2^0,\ldots,2^{31}\bmod b) cover all 19 elements of the doubling orbit. The exact finite set contains 38 signed single-power residues and 647 signed two-power residues; the union (including zero) has 647 elements and is closed under multiplication by (2\bmod b).

Define (a_t=b-94\cdot2^t) for (0\le t\le11). Here (gcd(94,b)=1), so
[
ka_t\bmod b\in S_b\iff -94k\bmod b\in S_b
]
by doubling invariance. Exact enumeration of the 647 residue values followed by multiplication by ((-94)^{-1}\bmod b) gives
[
\boxed{\min\{k\ge1:-94k\bmod b\in S_b\}=8369}.
]
An independent direct loop verifies the absence of intersections for (1\le k<8369). For (0\le t\le6), (K(a_t)\le K(518271)=8287<8369), ruling out **all different-start collisions**, regardless of their trace types. These are precisely the seven moduli listed in the theorem.

The bound is sharp within this family. At (t=7), (a=512255), the pair
[
F_0^6=(0,64),\quad F_{4287062095}^{15}=(4287062095,4287094863)
]
is a valid different-start collision: its start difference is (8369a) and its endpoint difference is (8177b). All state endpoints lie in ([0,N)), with legal XOR source bits.

## C. Uniqueness of the seven minimizers in the entire row

For each of the (131072) strict-19-bit odd (a), a C++17 generator searches first for zero/zero and zero/flip witnesses and then for two-flip witnesses using the previously published PREFIX-918 exact bit-window kernel. Every candidate returned by the kernel is **directly checked** by recomputing the real named XOR endpoints and both moduli; the proof of positive coverage requires only the actual checked witness, not an assumption that all negative searches were complete.

The complete row at (b=524287) returned:

| First verified witness type | Number of first-port moduli |
| --- | ---: |
| Zero/zero, distinct starts | 1 |
| Zero/flip, distinct starts | 48,723 |
| Two-flip, distinct starts | 82,341 |
| No distinct-start collision | 7 |
| **Total** | **131,072** |

All (131065) positive witnesses were independently audited in Python against exact integer state bounds, source labels and both modular equalities, with zero invalid witnesses. The seven omitted cases were independently ruled out by Part B. The locally audited row file SHA-256 is `a5011ac4b433bf15394212b7550c84dd582f69c74fcf8d0d1e0853f70ad0c05b`. Therefore every other (a) has at least one additional collision, proving uniqueness of the seven global row minimizers.

## Replication and scientific boundary

`PREFIX921_R6_MERSENNE_GAP_MINIMUM_CHECK.py` recomputes the independent finite set obstruction and the sharp (t=7) witness using Python exact integers. `PREFIX921_R6_DISTINCT_START_ROW.cpp` is derived from the frozen PREFIX-920 generator with a positional (b) parameter and an explicitly renamed `NO_DISTINCT_START_COLLISION` status; compile with `g++ -O3 -std=c++17`, then run `./row 524287 > witnesses.txt`. Its output contains a fully checked valid named witness for every positive row. The separate independent audit recomputes (x\oplus2^i) and (y\oplus2^j) for each `W a,b,type,x,y,i,j` line (negative bit index means zero step). No floating-point arithmetic is involved.

The result belongs to the auxiliary two-port observer at the frozen input pin and does not assert equivalence to native six-axis Heartbeat World dynamics. The central (B_{\mathrm{fix,odd}}(32)\in\{19,20\}) problem remains open.

**Next discriminating research unit:** investigate odd (b) with no equal-start collisions ((W_{32}(b)=0)). Seek a fully collision-free 19-bit observer or a general noninjectivity theorem, retaining source labels and exact modular witnesses. No shared X6 CLAIM or formal theorem admission is claimed.
