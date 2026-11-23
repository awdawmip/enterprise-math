# T6 exact v17=1 cancellation: five moments suffice with at most ten atoms per side

Date: 2026-11-23 Asia/Taipei. Scientific contributor: continuing Driver `EM-DVR-DEBB5E`. This is a finite-exhaustion mathematical subresult, not a native Result or an independent formal review.

## Proposition

Let `A,B` be finite multisets of positive integers `e`. Independently for each side `sum(e)<=2331`. Define `d=e+1`, `H_k(X)=sum_{e in X}(e/(e+1))^k` and `m_X(d)`. Assume `H_k(A)=H_k(B)` for `k=0,1,...,5`. If each side has at most ten denominators (counting repetitions) with exact `v_17(d)=1`, then

```
m_A(17u)=m_B(17u) for every positive integer u with 17 ∤ u.
```

Consequently this applies under the original T6 `H_0,...,H_6` hypothesis.

## Reduction from full rational identities

As before, `S_k=sum d^{-k}=sum_{i=0}^k(-1)^i binom(k,i)H_i`. Reuse the [existing universal 17² cancellation theorem](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md). Subtract the equal contributions of all denominators divisible by 17² from each full rational moment. Multiply the remaining k-th identity by `17^k` and reduce mod `17^k`: terms of 17-coprime denominators vanish, leaving necessary congruences for exact-valuation-one cofactor multisets

```
sum_{u∈U_A} u^{-k} ≡ sum_{u∈U_B} u^{-k} (mod 17^k),  k=1,...,5.
```

Here `u>=1`, `17∤u`, `d=17u`, `e=17u-1`, so the complete permissible domain consists of nondecreasing profiles `U=(u_1,...,u_n)` with `0<=n<=10`, `u_i<=137` and `sum(17u_i-1)<=2331`.

## Exact injection certificate

The C++17 verifier independently enumerates all such profiles by multiset recursion and counts them by a separate unbounded-coin integer dynamic program. For each profile it computes five modular inverse-power sums under `17,289,4913,83521,1419857`. The full mixed-radix signature fits in `uint64_t` because the exact key range is `17^15=2862423051509815793<2^64`. No lossy hash is used.

It writes each signature into exactly one of 256 binary files by its low eight bits. Four nonoverlapping passes independently sorted and exhaustively compared **all** adjacent keys within buckets 0–63, 64–127, 128–191 and 192–255. Every cross-profile equality would fall into one bucket.

| Number of atoms | All admissible profiles |
|---:|---:|
| 0 | 1 |
| 1 | 129 |
| 2 | 4,220 |
| 3 | 62,225 |
| 4 | 531,399 |
| 5 | 3,017,496 |
| 6 | 12,469,599 |
| 7 | 39,974,384 |
| 8 | 104,260,287 |
| 9 | 229,524,497 |
| 10 | 439,058,783 |
| **Total** | **828,903,020** |

Observed independent recursion and DP counts match at every cardinality.

| Bucket range | Exact keys checked | Collisions |
|---|---:|---:|
| 0–63 | 207,227,328 | 0 |
| 64–127 | 207,228,012 | 0 |
| 128–191 | 207,225,006 | 0 |
| 192–255 | 207,222,674 | 0 |
| **All 256** | **828,903,020** | **0** |

The complete source is in `research_checks/T6_P17_V1_UPTO_TEN_FIVE_MOMENT_BUCKET_EXACT_20261123.cpp`. It was built with `g++ -std=c++17 -O3 -Wall -Wextra` and executed; emitted 828,903,020 exact signature records and separately checked the entire disjoint bucket partition. The compilation issued only several indentation warnings in compact CLI code; no mathematical computation assertion failed. Four checker processes operated on disjoint bucket ranges and all returned successfully with the exact totals shown above.

Thus the five-coordinate map is injective across **all** 0–10-atom profiles and the proposition follows.

## Scope, provenance, next

This extends the prior up-to-eight and up-to-nine results and reuses their exact original hypotheses; the 17² prerequisite and original T6 contributors retain their existing attribution. The global T6=2332 minimum and unrestricted populations remain open. Source publication is separate from Activity linkage, native review, Result admission and official Task completion.

Next mathematical discriminator: test whether 11-atom and 12-atom profiles preserve five-moment injectivity, and if a collision occurs reconstruct explicit profiles and inspect the sixth moment rather than misreporting a counterexample to full rational moment equality.