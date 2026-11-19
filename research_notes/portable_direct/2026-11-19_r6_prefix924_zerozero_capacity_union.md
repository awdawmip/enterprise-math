# PREFIX-924 — Exact zero-step collisions outside the two-sided bucket-capacity certificate

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_IMPLEMENTATIONS / 128_DIRECT_GCD_ROW_AUDITS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Immediate frontier: PREFIX-923, research_notes/portable_direct/2026-11-19_r6_prefix923_sharp_bucket_capacity_and_highband_census.md; earlier exact named source trace framework PREFIX-917/918/920.

## Domain and theorem

Let p=32, N=2^p, c=p+1=33 and Q={262145,262147,...,524287}, |Q|=131072. For each ordered (a,b) in Q^2, the auxiliary two-port observer maps each typed named trajectory Z_x=(x,x), F_x^i=(x,x XOR 2^i) to (start mod a, end mod b), where 0<=x<N and 0<=i<p. Preserve the type/start/source-bit labels.

Let B be the set of modulus pairs failing at least one necessary PREFIX-923 bucket-capacity inequality:
b>=c*ceil(N/a), a>=c*ceil(N/b).
Let Z be the set for which the observer has a zero-step/zero-step collision.

**Theorem (exact finite cardinality):**
|Z| = 209,050,784;
|Z\B| = 95,349,218;
|B| = 7,365,546,244;
|B union Z| = **7,460,895,462**;
|Q^2\(B union Z)| = **9,718,973,722**.

These counts concern **ordered (a,b)**. This is an exact deduplication of two certificate families only, not a claimed increment to the complete PREFIX-912/914/920/922/923 multi-family collision ledger.

### Lemma 1: exact zero-zero support

Two distinct zero-step traces Z_x,Z_y collide iff
x-y is a nonzero multiple of both a and b. Thus
(a,b) in Z iff lcm(a,b)<N.
Sufficiency uses Z_0 and Z_lcm(a,b); necessity follows because |x-y|<N.

### Lemma 2: exact capacity-safe lower cutoff

For any a in Q, the pair avoids both bucket obstructions iff b in Q and b>=T(a), where

T(a)=max(262145, 33*ceil(N/a), ceil(N/floor(a/33))).

Proof: ceil(N/b)<=floor(a/33) is equivalent to b>=ceil(N/floor(a/33)), because a/33 is positive and all quantities are integers. The other inequality is b>=33*ceil(N/a). Q's lower bound supplies the first maximum term. This avoids floating point comparisons and gives a monotone b interval for each a.

### Lemma 3: complete divisor/Möbius count, preserving oddness

For fixed odd a and any odd-domain lower cutoff T, uniquely write
g=gcd(a,b), q=a/g, t=b/g.
Then g|a, b=g*t, gcd(q,t)=1, t is odd, and
lcm(a,b)=a*t.

Consequently, for each g|a, the permitted t interval is
lo(g)=ceil(T/g), hi(g)=min(floor(524287/g),floor((N-1)/a)).
The number of odd integers t in this interval coprime to q is exactly

C(q,lo,hi)=sum_{d|q} mu(d) [
 floor((floor(hi/d)+1)/2)
 -
 floor((floor((lo-1)/d)+1)/2)
],

with C=0 when lo>hi. All divisors d of q are odd. The extra odd-integer restriction is indispensable: merely counting gcd(q,t)=1 admits even t and doubles some terms.

The exact row count is sum_{g|a} C(a/g,lo(g),hi(g)).
Sum it over all 131072 values of a with T=262145 to obtain |Z|; use T=T(a) to obtain |Z\B|. Since (a,b) is uniquely partitioned by gcd(a,b), no double counting occurs.

## Exact results and numerical certificates

| Quantity | Ordered modulus pairs |
| --- | ---: |
| Complete Q^2 | 17,179,869,184 |
| PREFIX-923 two-sided capacity obstruction B | 7,365,546,244 |
| Capacity-safe pairs | 9,814,322,940 |
| Zero-zero support Z | 209,050,784 |
| Z inside B | 113,701,566 |
| **Z outside B (new capacity-relative exclusions)** | **95,349,218** |
| **B union Z** | **7,460,895,462** |
| Remaining after this *two-family* union | 9,718,973,722 |

Of the Z\B pairs, 73,900 lie on the diagonal a=b, and 95,275,318 lie off diagonal; the latter is even, as required by (a,b) interchange symmetry. This is a structural sanity check on the cardinality.

Exact sample rows (a, capacity-safe cutoff T(a), all Z row pairs, Z outside B):
- (262145, 540724, 6657, 0)
- (262147, 540724, 1, 0)
- (321651, 440649, 8339, 1782)
- (440665, 321651, 1405, 687)
- (524287, 270369, 1, 1)

**Verification:** A Python 3 factorization/divisor enumeration computes both complete 131072-row totals; separately implemented C++17 uses a sieved Möbius function, precomputed odd divisors and identical exact mathematical predicates, obtaining all totals exactly. C++17 independently performs a literal gcd/lcm check of every b in Q for 128 deterministically spaced a rows (16,777,216 unique ordered (a,b) positions, evaluated at both cutoffs) with zero mismatches. No floating point or probabilistic selection is involved. The first internal prototype omitted the required condition t odd and was rejected by the direct-GCD row check; the published two programs include the correction and expected-count assertions.

Reproduction:
1. python3 research_notes/portable_direct/PREFIX924_R6_CAPACITY_ZEROZERO_INCLUSION.py
2. g++ -O2 -std=c++17 research_notes/portable_direct/PREFIX924_R6_ZEROZERO_CAPACITY_UNION.cpp -o prefix924 && ./prefix924
3. Compare with research_notes/portable_direct/PREFIX924_R6_CAPACITY_ZEROZERO_RESULTS.json.

These programs use only standard Python/C++ integer arithmetic. The JSON lists the exact domain, counts and direct-GCD verification coverage.

## Interpretation and next discriminating unit

This result gives a **fully deduplicated, proved obstruction** for the union of bucket overflow and zero/zero traces, without enumerating all 17,179,869,184 pairs. The auxiliary observer is a provenance-aware BRC support/collision proxy; these zero-zero and bucket counts do not assert native X6 injectivity or theorem admission.

Further progress: intersect this exact two-family union with established signed-power / mixed-flip / complete-row certificate sources and their exact source labels, then classify the residual Q^2 domain. A valuable alternative is to derive a symbolic range bound for *mixed zero/flip* collisions on the remaining capacity-safe, zero-zero-safe pairs. Preserve the mother objective B_fix,odd(32) in {19,20} without promoting this auxiliary result.
