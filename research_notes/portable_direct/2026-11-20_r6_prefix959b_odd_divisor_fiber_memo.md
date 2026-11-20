# PREFIX-959B — Cached odd-divisor fibers for adjacent-core named XOR witnesses

**Date:** 2026-11-20. **Frozen input pin:** f42f2906d77f24085c123f3ccfe9667d41caa96d. Historical source: EM-DIRECT-58C410 / MCP-31edc522830749ad8775ca012e02ef30 (not a current CLAIM). **Evidence:** mathematical proof plus independently checked exact finite computation; NOT_REVIEWED. This is the auxiliary named-XOR observer, not a native 6D X6/BRC dynamics result.

## Exact model

Let p≥4, H=2^(p−1), Qp={H+1,H+3,...,2H−1}. Fix positive odd k with k+2<H. A named joint witness for off-diagonal (a,b) in Qp² consists of named 0≤i,j,I,J<p and integers t,T≥1 satisfying:

    (k*a XOR 2^j)-2^i=t*b
    ((k+2)*a XOR 2^J)-2^I=T*b

The actual signs s=1−2bit_j(ka) and S=1−2bit_J((k+2)a) define c=2^i−s2^j and C=2^I−S2^J, with full lists of named source triples retained for every numeric residual. Set m=T−t, Delta=C−c, N=k*C−(k+2)*c and D=2*t−k*m.

PREFIX-958 proved Delta=2a−mb and N=Db. Its Q19 generator used 538,183 candidate signed-D divisibility tests. The question here is whether repeated tests can be removed without quotienting away source histories.

## Theorem 959B.1 — Odd-part divisor-fiber bijection

For N≠0, uniquely write |N|=2^h*n, with h=v2(N)≥0 and n positive odd. Every original witness determines exactly one positive odd divisor q|n and co-divisor b=n/q in Qp, satisfying

    D=sign(N)*2^h*q
    t=(D+k*m)/2
    T=t+m
    a=(m*b+Delta)/2.

Conversely choose any odd divisor q|n with ceil(n/(2H−1))≤q≤floor(n/(H+1)). Retain the reconstructed quantities if t,T≥1, t≤2k, a is an odd Qp member different from b, and both actual signed-source bit predicates hold. This reconstructs all non-resonant named witnesses and their exact multiplicities. Each valid numerical residual pair contributes the product of its two permitted named-source triple counts.

**Proof.** Because b is positive odd, N=Db implies v2(D)=v2(N)=h and sign(D)=sign(N). Cancelling 2^h in N=Db gives n=qb, hence the unique odd q and its exact interval. The inverse formulas are integer identities. Back substitution yields k*a−t*b=c from k*Delta−N=2c; adding Delta yields (k+2)*a−T*b=C. The explicit source bit predicates recover both original XOR equations. Conversely any original tuple determines its unique m,c,C,D,q; preserving the named triple lists prevents loss or multiplication of distinct histories. QED.

For N=0 retain the separate PREFIX-958 resonance case D=0. The only possible positive quotient gaps are m=2 or m=4, with t=km/2 and a=(m/2)b+c/k, subject to every original source predicate. This branch is evaluated independently, without division by zero.

## Corollary 959B.2 — Dyadic progression sieve

If m is odd, the condition that a=(mb+Delta)/2 be odd is equivalent to mb+Delta≡2 (mod 4). Since m and b are odd and b^(-1)≡b (mod 4),

    b≡m*(2−Delta) (mod 4)
    D≡N*b (mod 4).

Thus among odd D values only one residue class mod 4 can contribute. If m is even, the earlier Delta modulo-4 sieve (Delta≡2 for m≡0; Delta≡0 for m≡2) already forces odd a for odd b. The additional exact condition v2(D)=v2(N)=h gives D≡2^h (mod 2^(h+1)). The divisor-fiber form incorporates both conditions.

## Theorem 959B.3 — Cache equivalence

For fixed p, the fiber Fp(n)={(b,q): b∈Qp, q≥1 odd, bq=n} depends solely on odd n; it is independent of m,c,C, sign(N) and v2(N). It can be computed **once per distinct odd part** of |N|, by enumerating odd q in the exact divisor interval, testing n mod q=0, and retaining the corresponding b. On each cache hit no new modular divisor test is necessary. Reconstruct D,t,T,a and check the source predicates separately. The proof is immediate from Theorem 959B.1 and preservation of the reconstruction map. This gives an exact algorithmic equivalence; no general polynomial bit-complexity claim is made.

## Strict Q19 experiment, source pin unchanged

Here p=19, k=21, next core 23, and the previously verified Q19 gap range 0≤m≤6 is reused. The code constructs candidates without consulting the prior pair certificate.

| Stage | Exact count |
|---|---:|
| Residual/gap entries after modulo-4 filter | 545,278 |
| Nonzero numerator entries | 545,276 |
| Distinct cached odd parts (including empty fibers) | 36,208 |
| Cache hits | 509,068 |
| **New modular divisor probes across all cache misses** | **59,138** |
| Eligible b divisor candidates before a-domain screen | 43,941 |
| In-domain numeric residual candidates | 17,719 |
| **Distinct ordered off-diagonal pairs** | **6,203** |
| **Named joint histories** | **8,649** |

This is an 89.0115444% reduction from the 538,183 modular-division probes in PREFIX-958, measured at that specific stage. The independent dyadic-congruence-progression variant performed 134,582 probes. Total wall-clock time did not reliably improve (cached Python approximately 0.67 seconds on one local run); there is no end-to-end performance claim.

By gap m=0,...,6, pair memberships are [6,442,4724,839,190,3,0] and named joint histories [6,614,6509,1286,231,3,0]. One pair belongs to two gap fibers and remains multiply tagged. The resulting 49,624-byte sorted little-endian uint64 pair-ID sequence has SHA-256:

    1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75

This matches the independent PREFIX-955/957B/958 certificates; it does not add distinct-pair coverage.

### Independent verification

For every odd k with k+2<2^(p−1) and each p=4,5,6,7 (56 cases total), the new algorithm used the **full admissible quotient-gap range** and was compared against raw original XOR enumeration of every off-diagonal (a,b), all named source index pairs, and exact gap-tagged witness multiplicities. All 56 comparisons passed, including resonance cases. The general bijection is proved algebraically; the Q19 numbers are an exact finite computation relying on the previously pinned Q19 gap bound.

Run: python3 PREFIX959B_R6_ODD_FIBER_MEMO.py --prefix PREFIX959B_R6 (Python 3.10+). This creates the exact-results JSON and binary pair-ID certificate and tests all the stated assertions. The repository publication provides this complete note, runnable program and JSON; the binary certificate is reproducible from the program. A local ZIP handoff additionally preserves the original source, an independent dyadic-progression program, binary and SHA-256 manifest.

## Scientific scope and next question

This exact identity concerns the auxiliary named XOR observation fiber. Under ACTIVE P000 and the residual-faithfulness discipline, identical numeric c or C does not permit discarding the source triple's identity when future source-sensitive observations are still in scope. The algorithm caches only the exact integer divisor fiber, preserving named lists and checking actual source-bit predicates. No native BRC/Heartbeat X6 transfer is asserted without a typed observer and allowed-operation preservation map.

Next: derive a weighted arithmetic sum over the shared Fp(n) fibers that counts named histories without constructing every output pair; investigate which named-source equivalences remain sound after sequential BRC port/path composition. Research status remains NOT_REVIEWED; the historical identity and Source Git publication do not constitute formal task execution authority.