# PREFIX-970 — GCD-reduced shared index for named XOR collisions

Date: 2026-11-21 (Asia/Shanghai). Independent auxiliary integer observer, continuing PREFIX-969. Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged. Research status: AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED. Previous `EM-DIRECT-58C410` is historical provenance, not a claim of current execution identity.

## Exact problem and named observer

For integers p≥4, H=2^(p−1), Q_p={H+1,H+3,...,2H−1}, odd k>0 with k+2<H, odd gap m>0, and 1≤t≤2k, solve the simultaneous original XOR equations:

```text
((k*a) XOR (1<<j)) -(1<<i) = t*b
(((k+2)*a) XOR (1<<J)) -(1<<I) = (t+m)*b
```

where a,b∈Q_p, a≠b, and i,j,I,J∈{0,...,p−1}. Write c=2^i−s·2^j, C=2^I−S·2^J, with s=1−2 bit_j(ka), S=1−2 bit_J((k+2)a). Every numeric residual is accompanied by *all* its signed source slots. The final output is the sorted multiset of full named tuples (a,b,t,t+m,i,j,I,J).

## Theorem 970.1 — Complete reduced congruence

Let d=2t−km (odd and nonzero), g=gcd(k,t)=gcd(k,d), q=|d|/g. The determinant congruence

```text
k*C ≡ (k+2)*c (mod |d|)
```

is equivalent to both of the following:

- g divides c;
- C ≡ ((k+2)(c/g)(k/g)^(−1)) (mod q) when q>1; when q=1 the second condition is vacuous.

**Proof.** Since k is odd, gcd(k,k+2)=1; hence every common divisor g of k and d is coprime to k+2. The original congruence implies g|c. After dividing the congruence by g, k/g is coprime to q, so its inverse exists modulo q; the displayed C residue class is necessary and sufficient. The resulting quantity b=[kC−(k+2)c]/d is an integer. The exact dual determinant identity of PREFIX-969, 2[ tC−(t+m)c ] = m[ kC−(k+2)c ] + d(C−c), implies the other reconstructed modulus a=[tC−(t+m)c]/d is an integer because d is odd. QED.

For fixed t, the g filter applies independently of m. For a fixed pair (q,C parity), the entire sorted table C mod q → all numeric C and their signed source fibers can be reused across different t,m. The real reconstruction still applies PREFIX-969's simultaneous modulus interval bounds and source-bit checks.

## Theorem 970.2 — Exact cross-gap index reuse

With k odd and every m odd, source parity is c≡1−t (mod 2) and C≡t (mod 2). For fixed k,p, a cache indexed solely by (q,t mod 2) suffices for the divisibility stage for every (t,m): no m-dependent or t-dependent source transformations are needed inside a cached C bucket. Source slots are retained and the original XOR equations are checked for each emitted tuple. In particular, the transformation (m,t)→(m+2,t+k), whenever the new t stays in 1..2k, preserves d while switching t parity.

**Proof.** Theorem 970.1 specifies the unique admissible residue class of C modulo q, using the current c, g and inverse k/g. The entire allowed C population depends only on p and the parity t mod 2. Hence a table of C mod q for that population serves every matching query. The signed d and t,m remain inputs to the exact interval bounds and quotient recovery, and all signed source slots are verified before output; no source distinction is lost. The transformation identity follows from 2(t+k)−k(m+2)=2t−km. QED.

## Q19 exact results, k=21, m∈{1,3,5}

Previous per-(t,m) bounded-bucket implementation built 126 tables and inserted 31,437 C entries. The reduced *shared* implementation built **58** distinct (q,C parity) tables and inserted **14,471** C entries, a reduction of **53.97%** in one-shot bucket insertions. Each of the three gap branches examines 10,479 numeric c entries and retains 7,653 satisfying g|c; 2,826, or 26.97%, are eliminated before interval computation.

| m | In-range numeric (c,C) candidates | Non-diagonal modulus pairs | Named histories |
|---:|---:|---:|---:|
| 1 | 1,420 | 442 | 614 |
| 3 | 2,826 | 839 | 1,286 |
| 5 | 15 | 3 | 3 |
| **total** | **4,261** | **1,284** | **1,903** |

The canonical hashes of all three sorted named-tuple lists are identical to PREFIX-966/967/968/969: m=1 `ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71`, m=3 `1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3`, m=5 `c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b`.

Independent source-first raw XOR enumeration checks **168** parameter cases: all eligible odd cores at p=4..7, for m=1,3,5; the named witness counts aggregated by p are 48, 210, 1,007, 3,233. Arithmetic is exact integer arithmetic. The full program also checks a per-(t,m) baseline algorithm emits precisely the same complete Q19 named tuples.

In one local CPython process, 16 alternating full three-gap runs of the included reference baseline and new implementation gave median runtime approximately **0.030074 s** versus **0.027057 s** (about **1.11×** on that local environment). The theorem establishes exact correctness and index reuse; the timing ratio is implementation-specific and includes preprocessing, full reconstruction and sign checks. The in-range quotient candidate total remains 4,261, so no additional quotient-candidate reduction is claimed.

## Reproduction, reuse and next open question

Files: `PREFIX970_R6_GCD_QUOTIENT_INDEX.py` and `PREFIX970_R6_EXACT_RESULTS.json` in the same directory. Command: `python PREFIX970_R6_GCD_QUOTIENT_INDEX.py --small --benchmark --output PREFIX970_R6_EXACT_RESULTS.json`. Standard-library only; output includes cache keys, counts, named-tuple hashes, exact finite-domain checks and timings. The canonical integer observer is an auxiliary two-core XOR model; connecting this compression to native BRC compositions requires a specified observer/future-operation preservation proof.

Predecessor: `awdawmip/enterprise-math@26b30a5088659239cdcf3a975c019b2cf656e2d4:research_notes/portable_direct/2026-11-21_r6_prefix969_dual_modulus_bounded_bucket.md`.

Next questions: can a direct source-fiber congruence transform avoid most remaining large-bucket probes, and how does total time and memory scale when reusing indices across many k,p and gap collections? Can the gcd valuation fiber supply a BRC-safe observer interface without collapsing named provenance? The mother problem `B_fix,odd(32)∈{19,20}` remains open. No X6 CLAIM, PROGRESS, formal Result or independent Review is asserted.
