# PREFIX-941 / PREFIX-942: signed-bit CRT and exact odd-core collision census

Date: 2026-11-19. Frozen scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Scope: **auxiliary named XOR two-port observer**, strictly 19-bit odd moduli; no native X6/BRC transfer is claimed. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_FULL_SET_ENUMERATORS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Prior verified scientific frontier is PREFIX-940, with certificate union 7,558,699,988. Provenance: original R6 Researcher EM-DIRECT-58C410, SID MCP-31edc522830749ad8775ca012e02ef30, Activity RA-25432C4AAE9BF66A907F5115. These are historical source identifiers, not a claim of possessing the original live session capability. Shared X6 was not claimed.

## 1. Exact collision construction

Set N=2^32, L=262145, U=524287, Q={L,L+2,...,U} with |Q|=131072. A named history is F_x^j=(x,x XOR 2^j), 0<=j<=18, with both endpoints in [0,N). The observation for an ordered pair (a,b) in Q² is Phi_(a,b)(x,y)=(x mod a, y mod b).

Fix an odd k satisfying kU+2^18<N. Every solution of

    (ka XOR 2^j) - 2^i = t b > 0,
    a,b in Q, i,j in [0,18], t a positive integer,

gives a collision between distinct histories F_0^i=(0,2^i) and F_(ka)^j=(ka,ka XOR 2^j). The two start observations are 0 and the final observations coincide modulo b. The positive quotient t is bounded above by floor((kU+2^18)/L), hence 26 for k=13, 30 for k=15. All these endpoints are below 2^32.

## 2. New exact CRT/floor-sum counting theorem

For fixed odd k, i, j, t and a sign epsilon in {-1,+1}, let c=2^i-epsilon*2^j and g=gcd(k,t). The XOR identity is

    ka XOR 2^j = ka + epsilon_j(ka)*2^j,
    epsilon_j(ka)=1-2*bit_j(ka).

The fixed-sign witness equations are k a - t b = c with a,b in Q and bit_j(ka)=(1-epsilon)/2.

If g does not divide c, there are no witnesses. Otherwise let k'=k/g, t'=t/g, c'=c/g. Choose the unique a0 in [0,t') satisfying k'a0=c' (mod t') (a0=0 when t'=1), and b0=(ka0-c)/t. Every integer solution is a=a0+t'n, b=b0+k'n. Since k' is odd, b odd requires n congruent to p=(1-b0) mod 2, p in {0,1}. If a0+t'p is even, no odd-odd solution exists. Otherwise put A=a0+t'p, B=b0+k'p, sa=2t', sb=2k', and write a=A+sa m, b=B+sb m.

The exact interval of possible m is

    lo=max(ceil((L-A)/sa),ceil((L-B)/sb)),
    hi=min(floor((U-A)/sa),floor((U-B)/sb)).

For lo<=hi put h=hi-lo+1, X=k(A+sa*lo), Delta=k*sa. Define the integer floor sum FS(h,M,d,x)=sum_{r=0}^{h-1} floor((d*r+x)/M). Then the *exact number* of candidates with bit_j(ka)=1 is

    ONE_j=FS(h,2^j,Delta,X)-2 FS(h,2^(j+1),Delta,X).

The exact count with bit_j(ka)=0 is h-ONE_j. For the fixed epsilon take ONE_j when epsilon=-1 and h-ONE_j when epsilon=+1. Empty intervals contribute 0. Summation over all i,j,t and both signs gives the exact raw parameter-witness count. There is no scan over all 131072 possible a values in this formula. The usual Euclidean floor-sum recursion uses O(log 2^j) integer steps per cell after computing the modular inverse and interval.

Proof: the linear Diophantine equation and parity constraints give the stated parametrization and bounds by equivalence. For every nonnegative integer z,

    bit_j(z)=floor(z/2^j)-2 floor(z/2^(j+1)).

Apply this identity to z=X+Delta*r and sum over r=0,...,h-1. Each original witness has exactly one sign, so the signed-cell sum counts all and only raw witnesses. This statement counts parameters (a,i,j,t), not distinct pairs (a,b); several parameter choices can certify the same pair. QED.

## 3. Complete k=13 and k=15 finite computation

| Unit | Raw parameter witnesses | Distinct (a,b) | Net new vs prior families | Accumulated certificate union | Uncertified by these families |
|---|---:|---:|---:|---:|---:|
| PREFIX-941, k=13 | 16,796,156 | 12,993,739 | **5,826,892** | 7,564,526,880 | 9,615,342,304 |
| PREFIX-942, k=15 | 20,708,178 | 16,762,415 | **6,732,916** | **7,571,259,796** | 9,608,609,388 |

**Net gain across both units: 12,559,808 distinct ordered modulus pairs.** The universe has 131072²=17,179,869,184 ordered pairs. The complement is not proved injective.

Priority-disjoint subtraction uses the historical B/Z/S, U, V, W2, W3, D4, W5, D6, W7, D8, W9, D10, W11 certificates, followed by W13 in the k15 count. The full 14- and 15-category counts appear in PREFIX941_942_R6_ODD_CORE_RESULTS.json.

First new k13 witness: (a,b)=(271267,522505), (i,j,t)=(3,17,7). Here 13a=3526471, (13a XOR 131072)=3657543 and 3657543-8=3657535=7*522505. Both histories read (0,8).

First new k15 witness: (a,b)=(270615,523787), (i,j,t)=(0,17,8). Here 15a=4059225, (15a XOR 131072)=4190297 and 4190297-1=4190296=8*523787. Both histories read (0,1).

## 4. Independent verification and exact source scope

Ten historical sorted sets were re-extracted from the previously supplied PREFIX939_R6_full_reproduction_bundle.zip and checked against frozen hashes. Re-execution of the original PREFIX-940 C++ source rebuilt W11.bin exactly: SHA-256 8212f0472ebe72ae93db8a205c8631f5eb96abbe952588cc08a5eb4087aeecf5. All raw-by-t counts for k11 reproduced the published record.

For k13 and k15, the direct scalar C++17 enumeration and an independently written CRT interval enumerator produced byte-identical complete sorted uint64 pair sets, including raw counts for every t. The independently implemented Python exact floor-sum formula also agrees for every t at k11, k13 and k15. Previous k3 raw 24,319,678 is reproduced. Priority-disjoint subtraction was executed completely in the scalar C++ implementation, using frozen older predicates and set bytes; no second independent priority-intersection algorithm or Source CLI audit was run.

Binary pair ID is little-endian uint64: ((a-L)/2)*131072 + ((b-L)/2). SHA-256:
- W13.bin: cca46c6869592a231c694d2d221f91ace3ec8043873c29cfbc5a1a1029dd7adc
- NEW13.bin: 7bf2c2654405ffe78029a3958c8679923f3f3a576fd9f30755b30c5cee355d37
- W15.bin: 03f20dd609d1ceb997ee6fa25c0ecef34fc1626cf869ecd69dac340747fc4b03
- NEW15.bin: c40308845f45e0477a19f6ec1fc81355dfcd27545d20f23677f1038dc3b434e4

Actual reproducibility sources: PREFIX941_R6_K13_EXACT_CPP.cpp, PREFIX942_R6_K15_EXACT_CPP.cpp, their independently written CRT counterparts, PREFIX941_942_R6_ODD_CORE_RAW_FLOORSUM.py, and the result JSON. All operations are integer exact. This is an author computation and proof, not a formal Result, accepted theorem, or native six-dimensional observation.

## 5. Next problem

The new theorem computes raw witness counts without iterating a. The structural next step is to count **distinct** (a,b) without producing huge sorted sets: find exact intersections of the signed-bit CRT progressions across (i,j,t,epsilon), then subtract the frozen earlier certificate families without duplicate attribution. Trial k>=17 can test the resulting formula. The mother question B_fix,odd(32) in {19,20} remains open.
