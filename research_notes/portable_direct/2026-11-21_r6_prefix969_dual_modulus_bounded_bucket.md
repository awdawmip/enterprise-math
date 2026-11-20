# PREFIX-969 — Dual-modulus interval filter for named XOR collisions

Date: 2026-11-21 (Asia/Shanghai). Scope: independent auxiliary named integer observer, frozen scientific input `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED. Historical provenance `EM-DIRECT-58C410` is not asserted as a live session capability.

## Defined problem

Let p≥4, H=2^(p−1), L=H+1, U=2H−1, Q_p={L,L+2,...,U}. Let k≥1 be odd with k+2<H, and m>0 odd (tested m=1,3,5). For a,b in Q_p, a≠b, 1≤t≤2k, and 0≤i,j,I,J<p, solve both named equations:

```text
((k*a) XOR (1<<j)) - (1<<i) = t*b
(((k+2)*a) XOR (1<<J)) - (1<<I) = (t+m)*b
```

Represent their numerical residuals c=2^i−s·2^j, C=2^I−S·2^J using actual source-bit signs s=1−2 bit_j(ka), S=1−2 bit_J((k+2)a). Each numeric residual retains ALL of its named source slots; duplicate values are never treated as duplicate-free histories.

## Theorem 969.1 (dual determinant inversion)

Define d=2t−km, necessarily odd and nonzero. Then the collision equations imply

```text
d*b = k*C-(k+2)*c,                         (1)
d*a = t*C-(t+m)*c,                         (2)
2*[t*C-(t+m)*c] = m*[k*C-(k+2)*c] + d*(C-c).  (3)
```

Once the modular bucket condition kC≡(k+2)c (mod |d|) holds, BOTH quotients (1),(2) are integers: (1) is divisible by d; (3) gives d dividing twice the numerator of (2); d odd implies d divides its numerator.

Proof: Write ka−tb=c and (k+2)a−(t+m)b=C. Eliminate a to obtain (1), eliminate b to obtain (2). Direct expansion proves (3). The integrality inference follows since gcd(d,2)=1. QED.

## Theorem 969.2 (exact simultaneous modulus interval)

Write D_lo=min(dL,dU), D_hi=max(dL,dU), and for a fixed residual c define

```text
C_lo(c) = max(ceil(((k+2)c+D_lo)/k), ceil(((t+m)c+D_lo)/t))
C_hi(c) = min(floor(((k+2)c+D_hi)/k), floor(((t+m)c+D_hi)/t))
```

For a residual C satisfying the above bucket congruence, the two reconstructed integer values a,b lie in [L,U] IF AND ONLY IF C_lo(c)≤C≤C_hi(c). This includes d<0, |d|=1, and any noncoprimality of k,d.

Proof: For either z/d and d≠0, L≤z/d≤U iff min(dL,dU)≤z≤max(dL,dU). Apply separately to (1) and (2), divide each linear inequality by the positive coefficients k and t, take ceilings/floors and intersect. The congruence makes the quotients integers by Theorem 969.1. QED.

Algorithm: for each fixed t build a hash of sorted full-fiber numeric C entries keyed by kC mod |d|. For each eligible c, find the bucket keyed by (k+2)c mod |d|; binary-search its inclusive [C_lo,C_hi] subsequence. Recover a,b, keep odd non-diagonal pairs and check the actual target-side bit signs for EVERY stored named slot. The congruence and range filter are exact; re-expansion retains the declared final named-history observer. This safe-quotient statement is scoped to these output histories, not to arbitrary future BRC/native operations.

## Exact Q19 experiment (p=19, k=21)

| gap m | congruence-bucket numeric pairs | range-filtered numeric pairs | non-diagonal modulus pairs | named histories |
|---:|---:|---:|---:|---:|
| 1 | 132661 | 1420 | 442 | 614 |
| 3 | 134077 | 2826 | 839 | 1286 |
| 5 | 24996 | 15 | 3 | 3 |
| **sum** | **291734** | **4261** | **1284** | **1903** |

The range filter eliminates 287473/291734 = 98.5394% of numerical candidate quotient reconstructions, a 68.47× reduction in that operation relative to PREFIX-968. Bucket construction (31437 insertions), probing (31437 lookups), and final source sign checking (11596 slot tests) remain in the end-to-end cost. The remaining arithmetic pairs are 1419, 2825 and 15; the other two range candidates are diagonal pairs.

All Q19 named tuple hashes match the PREFIX-966/967/968 independent earlier lists:

```
m=1 ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71
m=3 1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3
m=5 c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b
```

Independent raw XOR endpoint enumeration matched the complete named tuple multisets at all 168 cases p=4..7, all eligible odd k, m=1,3,5 (p group witness totals 48,210,1007,3233). Canonical compact list SHA-256: `493d98b86bb0393586dbc02185d740b6b09c9ebcae26c69162e5e994ab9bd4f6`.

Measured in one local CPython run, 12 alternating-order repetitions per method, median full-generator seconds:

| m | old unbounded bucket | bounded bucket | old/new |
|---:|---:|---:|---:|
|1|0.032723|0.011780|2.778|
|3|0.037504|0.014092|2.661|
|5|0.010525|0.010113|1.041|

Times include constructing source dictionaries and residue buckets, reconstructing all moduli, checking all source signs and validating original XOR equations. Performance is implementation/environment specific, with range-bisect overhead relevant when buckets are already sparse. These are not asymptotic or native BRC speedup claims.

## Reproducibility and continuation

Run `python PREFIX969_R6_DUAL_MODULUS_INTERVAL_JOIN.py --small --benchmark` (stdlib only), which checks 168 direct XOR cases, all Q19 hashes, and prints exact operation counts. Determinant arithmetic uses exact Python integers. Companion `PREFIX969_R6_EXACT_RESULTS.json` records the exact counts and local median observations.

Predecessor: `awdawmip/enterprise-math@04b94145705fc0425fb1563adeadcabef7cbb1c5:research_notes/portable_direct/2026-11-21_r6_prefix968_modular_bucket_quotient_join.md`. Frozen scientific pin remains unchanged. P000 V4, Source P000 V5, current ACTIVE worldview, and joint observer-preservation rules were read without reinterpreting the auxiliary two-core integer model as a native X6 carrier.

Next: compare adaptive sparse/full-bucket traversal and cross-t or cross-m bucket reuse with full preprocessing/memory cost, retaining every signed source fiber. The mother question B_fix,odd(32)∈{19,20} remains OPEN. No X6 CLAIM/PROGRESS, formal Result, Review or Foundation promotion is asserted.
