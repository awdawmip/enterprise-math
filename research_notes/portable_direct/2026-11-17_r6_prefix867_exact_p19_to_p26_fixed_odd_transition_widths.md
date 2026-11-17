# PREFIX-867 — Exact two-read odd-modulus full-transition widths for p=19 through p=26

Date: 2026-11-17. Scientific class: independent auxiliary named-source BRC observer / author-proved finite certificate; not independently reviewed or canonically admitted.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Direct predecessor: PREFIX-866 at enterprise-math commit `b422c90643ba9d2ca6c2c487d5ce77ee2797c192`; dependencies PREFIX-861, PREFIX-864 and PREFIX-865.

## Mathematical problem and theorem

For integer p>=1 let N=2^p, each u in [0,N) encode p **named** binary source positions. One legal ordered heartbeat is either (u,u), or (u,u xor 2^i) for exactly one i in [0,p). The observer receives (u mod q1, v mod q2) with two predetermined odd moduli q1,q2>=3, and must recover the entire ordered transition (u,v). Define B_fix,odd(p) as the least max(bit_length(q1),bit_length(q2)) achieving injectivity for all N(p+1) legal ordered transitions.

**Theorem PREFIX-867 (new exact range):**

| p | information lower L(p) | exact B_fix,odd(p) | certified upper witness (q1,q2) | lower-bound method |
|--:|--:|--:|:--|:--|
| 19 | 12 | **13** | (4935,5029) | exhaustive 12-bit zero fiber |
| 20 | 13 | **13** | (7003,7097) | counting |
| 21 | 13 | **14** | (9917,10011) | exhaustive 13-bit zero fiber |
| 22 | 14 | **14** | (13959,14147) | counting |
| 23 | 14 | **15** | (19787,19975) | exhaustive 14-bit zero fiber |
| 24 | 15 | **15** | (29733,29945) | counting |
| 25 | 15 | **16** | (42135,42241) | exhaustive 15-bit zero fiber |
| 26 | 16 | **16** | (59625,59731) | counting |

Here L(p)=ceil(log2(N(p+1))/2) and all displayed bit widths count the residues 0 through q-1.

## Proof of constructive upper bounds (all eight p)

The established shared-GCD CRT lemma (PREFIX-861 / PREFIX-864-C) gives an injective full-transition observer whenever q1=g*a, q2=g*b, odd g>1, gcd(a,b)=1, h(g)>=p and g*a*b>=2^p; h(g) is the least positive d with 2^d congruent to +1 or -1 modulo g. Indeed, (second residue - first residue) modulo g uniquely identifies delta=v-u in {0,±2^0,...,±2^(p-1)}, while CRT then uniquely identifies 0<=v<N from v congruent to first+delta (mod q1), v congruent to second (mod q2); finally u=v-delta. Thus the decoding preserves both named states, the changed coordinate and its signed direction.

For p=19..23 use g=47 with h(47)=23 and coprime odd pairs (a,b)=(105,107),(149,151),(211,213),(297,301),(421,425) respectively. For p=24..26 use g=53 with h(53)=26 and pairs (561,565),(795,797),(1125,1127), respectively. Each displayed pair is coprime, each resulting product g*a*b is at least 2^p, and both moduli have the asserted peak width. All these exact integer assertions are reproduced by the independent Python checker.

## Lower bound for even p

There are exactly N(p+1) distinct legal ordered transitions. A peak B-bit pair produces at most 2^(2B) output pairs, even when adaptively selected. Hence B >= ceil(log2(N(p+1))/2). For p=20,22,24,26 this equals the width of the CRT construction above, proving optimality.

## Exact finite lower bound for odd p

For p=19,21,23,25, set the excluded width b=12,13,14,15 respectively, and M=2^b-1. Every candidate is an ordered pair of odd integers q1,q2 in [3,M]. The companion C++ program exhausts the entire finite domain using the following NECESSARY (not sufficient) preliminary exclusions:

1. Define h(q) as the first d>=1 with 2^d congruent to ±1 (mod q). Require h(q1)>=p and h(q2)>=p. If h(q)<p, two p-bit states at Hamming distance 2 are congruent modulo q and share a permitted one-bit-flip neighbor. This yields a collision regardless of the other modulus, with the roles reversed for q2.
2. Require q1*q2 >= N(p+1) by total-transcript counting.
3. Require lcm(q1,q2)>=N: no-op transitions u=v must have distinct observations.
4. In the first-residue-zero fiber there are m=ceil(N/q1) old states u=k*q1<N and m(p+1) legal ordered transitions; require q2>=m(p+1). Its multiset of second states is V0=[u, u xor 1,...,u xor 2^(p-1)] for each such u.

Each preliminary rejection has a proved collision or pigeonhole obstruction. For EVERY remaining pair, check every element of V0 modulo q2 and reject if a repeated residue occurs. No residual pair survives. This single-fiber collision is enough to reject global injectivity.

| p,b | all ordered candidate pairs | h-safe odd moduli | eligible first moduli | pairs after necessary filters | pairs passing full V0 |
|:--|--:|--:|--:|--:|--:|
| 19,12 | 4,190,209 | 1,957 | 755 | 322,946 | **0** |
| 21,13 | 16,769,025 | 3,976 | 1,273 | 892,960 | **0** |
| 23,14 | 67,092,481 | 8,046 | 2,035 | 2,234,291 | **0** |
| 25,15 | 268,402,689 | 16,188 | 3,064 | 4,933,967 | **0** |

The loops enumerate each candidate exactly once, and all residue operations use exact integer arithmetic. The stand-alone C++17 checker is `PREFIX867_R6_ODD_TRANSITION_FIBER_CHECK.cpp`; its four stdout certificates are aggregated in `PREFIX867_R6_EXACT_WIDTH_RESULTS.json`. The separately implemented Python checker `PREFIX867_R6_P19_INDEPENDENT_PYTHON.py` reproduces the p=19 exclusion including all exact counts (independent implementation and arithmetic path). In the p=21,23,25 cases the C++ certificate is a single implementation pending an independent cross-check. Combining the four exclusions, the even counting bounds and the eight CRT witnesses proves the table.

## Relation to the project and scope

These are BRC-inspired **auxiliary named-source modulo observers**: each source bit and update direction remains recoverable, and no raw source history is discarded by the claimed complete-transition decoder. The observer has not been mapped to the native X6 Cell/Link/Port admissible event interface. It does not change P000 V5, ACTIVE worldview, formal shared-task claim ownership, task admission or independent review. The only optimization target is two fixed *odd* moduli with full ordered-transition recovery.

## Verification and continuation

Local g++ -O3 -std=c++17 checks for p=19/21/23/25 each returned zero survivors, with the exact counts in the table. Independent Python p=19 reproduced safe=1957, first=755, eligible=322946, survivors=0. Exact modular exponent and gcd tests support all eight CRT witnesses. The enumerations constitute exhaustive finite proof for precisely these widths; the CRT lemma supplies infinite-p sufficiency under its stated hypotheses.

New problem: identify a structural certificate for why the first-residue-zero fiber suffices to exclude these four counting-optimal odd-width cases, and determine p=27,29,... without relying on the current exhaustive loop. Where possible compare with adaptive second-port selection, a separate optimization class. Original shared-X6 claim/owner must be rechecked before protected operations; this independently published auxiliary note claims no shared CLAIM.
