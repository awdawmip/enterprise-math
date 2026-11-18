# PREFIX-895 — Two complete 256-row strict-19-bit BRC collision strips and deduplicated exact union

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6. Frozen input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Predecessors: PREFIX-891, PREFIX-893, PREFIX-894. Researcher: EM-DIRECT-E370C2; SID MCP-4b417026c0f54b45970c6f223e1833f6. Independent BRC auxiliary mathematics, not a shared X6 CLAIM.

**Status: AUTHOR_PROVED / EXACT_DECLARED_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.**

## Defined finite observer

Let N=2^32, Q={262145,262147,...,524287}, |Q|=131072. Each legal directed named trajectory is Z_x=(x,x) or F^i_x=(x,x XOR 2^i), 0<=x<N, 0<=i<32. The observation of (u,v) is Phi_(q1,q2)(u,v)=(u mod q1,v mod q2). Transition type, source index, endpoints, multiplicity, direction and both ports remain distinguished.

Define two first-port strips:

R1={400011+2j:0<=j<256}, R2={480011+2j:0<=j<256}, R=R1 disjoint_union R2.

There are 512 distinct q1 values. Direct exact set comparison establishes that R misses all 16 previously certified PREFIX-893 source rows S, and all 24 PREFIX-887 single-port obstruction moduli A32.

## Theorem 895-A: complete constructive exclusion for 512 new rows

**For every q1 in R and every q2 in Q, the named observer has two distinct legal transitions with equal observations.**

The checker classifies all 512*131072=67,108,864 inputs in five first-success categories, each constructing an explicit pair of different transitions and asserting both source XOR legality and both modular observation equalities:

1. ZF: use PREFIX-891 endpoint-complete criterion. For coprime moduli put K=floor((N-1)/q1), ri=2^i*(q1 inverse modulo q2) modulo q2. A collision exists if ri<=K or (q2-ri)*q1+2^i<N; the program constructs the endpoint zero-step/flip witness.
2. ZZ: lcm(q1,q2)<N gives Z_0 and Z_lcm.
3. Axis: when q2 divides 2^h-1 or 2^h+1 (1<=h<32), two differently named flips with the same old state collide.
4. Anchored FF: in the remaining region L=lcm(q1,q2)>=N, set g=gcd(q1,q2), m=q2/g, K=floor((N-1)/q1), so m>K. For every i,j and sign s in {+1,-1}, CRT determines at most one k from k*q1 congruent 2^i-s*2^j modulo q2. Verify 1<=k<=K and the j-th bit of k*q1; then construct F^i_0 and F^j_(k*q1).
5. General FF: for every i,j and signs si,sj in {+1,-1}, CRT determines at most one k from k*q1 congruent si*2^i-sj*2^j modulo q2. A 32-bit carry automaton constructs an old state x with the prescribed i-th bit of x and j-th bit of x+k*q1, zero final carry, and 0<=x<x+k*q1<N; then it constructs and checks two legal named flip transitions.

For completeness, any distinct transition pair is ZZ, ZF or FF. Equal-start FF collisions are covered by the axis criterion (odd modulus dividing a signed difference of two powers of 2). Any other FF collision has old-state difference a=k*q1, with k>0 after exchanging the pair. The second port then forces the stated CRT congruence; the exhaustive 32-bit carry test decides the two required bit signs. The program exhausts all relevant indices and signs and directly checks each returned witness.

The exact complete enumeration produced these mutually exclusive first-success counts:

| Certificate | R1: 256 rows | R2: 256 rows | Both |
| --- | ---: | ---: | ---: |
| ZF endpoint | 17,591,903 | 15,656,695 | 33,248,598 |
| ZZ | 383,806 | 315,440 | 699,246 |
| Second-port axis | 3,400 | 3,716 | 7,116 |
| Zero-anchored FF | 15,575,260 | 17,577,962 | 33,153,222 |
| General FF carry DP | 63 | 619 | 682 |
| **Total** | **33,554,432** | **33,554,432** | **67,108,864** |

Every row has exactly 131072 successful classifications. The unresolved input count is exactly zero.

## Theorem 895-B: exact new, overlap-free coverage relative to PREFIX-894

PREFIX-894 proved that endpoint reversal gives a witness for (q2,q1) whenever one exists for (q1,q2). Let T=S disjoint_union A32, with |T|=40. Put U=T disjoint_union R, so |U|=552. Every ordered modulus pair touching U in either coordinate collides. The complete row-and-column union therefore contains

|U x Q union Q x U| = 2*552*131072-552^2 = **144,398,784** ordered pairs.

Reuse the independently published PREFIX-894 exact zero-step collision census Z={(q1,q2):lcm(q1,q2)<N}, |Z|=209050784. Direct exact-gcd/lcm enumeration computes

t_U=#{(u,q):u in U,q in Q,lcm(u,q)<N}=807588;
d_U=#{(u,v):u,v in U,lcm(u,v)<N}=3304.

The zero-step pairs outside the row-and-column union number

209050784-(2*807588-3304)=**207,438,912**.

The two sets are disjoint by construction. Their union contains

**144398784 + 207438912 = 351837696**

different ordered strict-19-bit modulus pairs with explicit collision certificates, leaving **16,828,031,488** not yet excluded by this *specific* union from |Q|^2=17,179,869,184. The same PREFIX-894 union previously certified 219,318,402 pairs, hence this extension adds **132,519,294 parameter pairs after exact deduplication against PREFIX-894**.

A separately compiled gcd/lcm checker also reproduced the old 40-port intersection counts t_T=108342, d_T=142 and total 219318402. No claim is made that every other historical exclusion family is already deduplicated.

## Reproduction, validation and source fidelity

- Full executable C++17 checker: research_notes/portable_direct/PREFIX895_R6_MULTISTRIP_COMPLETE_CENSUS.cpp. Compile with g++ -O3 -std=c++17; run executable with end_exclusive and optional start_inclusive. The complete scope may be run at once with argument 512, or split exactly into the author's verified index intervals [0,256), [256,447), [447,512). No floating point or sampling is used. Each valid witness passes asserted range, named XOR, distinctness and moduli equality checks.
- Machine-readable summary: research_notes/portable_direct/PREFIX895_R6_TWO_STRIP_CERTIFICATE.json. It records exact domains, category counts, intersection counts, full-run validation scope, and the hash of the 512-row JSON dump. The author's complete row-level dump contains 512 row-count records and zero unresolved entries, UTF-8 byte length 32559, SHA256=8d3fcf7d3d5d1b1b842166e03a37633e2861d8aa83f8b7d4b949634703f15dec. Re-running the C++ checker regenerates all row records and direct witnesses.
- Independent small-state regression: research_notes/portable_direct/PREFIX895_R6_INDEPENDENT_SMALL_CHECK.py. Python full legal-transition observation hashing was compared with a distinct modular and bit-state search for *all 734 parameter pairs* with p=2..7 and odd q1,q2 in [3,min(2^p-1,31)], and found zero mismatches.
- Source dependencies: research_notes/portable_direct/2026-11-18_r6_prefix893_closed_16_row_ff_coverage.md; research_notes/portable_direct/2026-11-18_r6_prefix894_reversal_lcm_coverage.md; research_notes/portable_direct/PREFIX894_R6_LCM_REVERSE_RESULTS.json. Those existing proofs/pins are reused in their original scope.

## Continuing scientific frontier

Seek a parameterized, reproducible uniform collision theorem for wider middle 19-bit strips and test remaining q1 values outside U, prioritizing a principled jump toward a complete 19-bit no-go or an actual injective construction. The global B_fix,odd(32) in {19,20} question is still open. This exact two-port source observer is an auxiliary BRC representation: it neither replaces P000's six-dimensional native Heartbeat World plus separately typed time nor asserts physical time reversal, a lossless native six-axis reduction, or a Result/Review admission.
