# T6: exact cancellation of the 17-adic valuation-one layer with at most nine atoms on each side

Date: 2026-11-23 (Asia/Taipei). Scientific contributor: continuing control-plane Driver `EM-DVR-DEBB5E`. Status: independently computed finite mathematical subresult; not a Native Review, Result admission or mother-goal closure.

## Precise proposition

Let `A,B` be finite multisets of positive integers `e`, each independently satisfying `sum(e) <= 2331`. Define `d=e+1`, `H_k(X)=sum_{e in X}(e/(e+1))^k`, and `m_X(d)` as multiplicity. Suppose `H_k(A)=H_k(B)` for `0<=k<=5`. If **each side** has at most nine denominators of exact 17-adic valuation one (counting repetitions), then

```
m_A(17u)=m_B(17u) for every u>=1 with 17 ∤ u.
```

This strengthens the prior up-to-eight-atoms theorem without requiring the sixth-degree observation. It therefore applies to the original T6 equality `H_0,...,H_6`.

## Necessary congruences from the full rational moments

The binomial identity `S_k(X)=sum_{i=0}^k (-1)^i binom(k,i) H_i(X)`, with `S_k(X)=sum (e+1)^(-k)`, gives equality of `S_1,...,S_5`. Reuse the earlier [universal 17² cancellation theorem](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md), valid under `H_0,...,H_3`. Cancel matching terms of denominators divisible by `17²`, multiply each remaining k-th identity by `17^k` and reduce in the 17-adic localization modulo `17^k`. Terms with 17-coprime denominators vanish. Thus the exact-valuation-one denominator profiles satisfy

```
F(U_A)=F(U_B),  F(U)=(sum_{u in U} u^{-k} mod 17^k)_{k=1..5}.
```

This is deduced from the original full identities rather than assumed for prime components.

## Exact finite proof by complete injection test

Allowed atoms have `d=17u`, `1<=u<=137`, `17 ∤ u`, exponent cost `17u-1`. Enumerate every nondecreasing (repetitions permitted) profile of size `0<=n<=9` with total cost `sum(17u_i-1)<=2331`.

The checked implementation uses exact extended-Euclidean modular inverses, integer residues modulo `17,289,4913,83521,1419857`, and a mixed-radix 64-bit key; its key space is `17^(1+2+3+4+5)=2862423051509815793<2^64`. It writes each full signature key to one of 256 disjoint buckets chosen by the low eight key bits. Within every bucket, all keys are sorted and every adjacent equality is tested. This is a lossless partition of the entire key space, so all global equalities are caught within one bucket.

A separate integer generating-function/unbounded-coin dynamic program counts the same profiles by exact `n` and total cost, independently of the signature recursion.

| Number of atoms n | Exact lawful profiles |
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
| **9** | **229,524,497** |
| **Total** | **389,844,237** |

**Observed: 389,844,237 exact legal profiles; zero collisions of the five-coordinate signature across the entire joint 0–9 domain.**

Computation record: the full emission and initial bucket-check run established independent recursion/DP equality for every `n`, and checked buckets 0–190; the execution hit a time limit after completing bucket 190, before the final summary print. The remaining persisted binary buckets 191–255 were each subsequently fully sorted and checked, with `98,974,913` keys and zero collisions. To independently confirm the interrupted 160–190 segment, a second bounded execution reenumerated the entire profile universe, emitted and sorted exactly buckets 160–190, again finding zero collisions and the same independent `n` counts. The first uninterrupted progress report recorded zero collisions through bucket 159. These three verified disjoint intervals collectively cover all 256 buckets without relying on a nonexistent single-run success exit. The available source checker can be run without a short timeout to obtain a single-run conclusion.

As `F` is injective over every admissible profile with 0–9 atoms, equality of the necessary 17-adic signatures forces equality of the exact profiles, proving the scoped statement.

## Limits, authorship and next question

This proves only the at-most-nine-per-side subcase. Arbitrary populations above nine, and full T6 global optimality, remain open. The prior 17² theorem is used at its original scope; its author/provenance remains unchanged. The executable checker is a direct continuation of the earlier eight-atom procedure; no independent review or method novelty is claimed. Project Activity association, Native Review/Result and task ownership remain governed by their real current contracts.

Next discriminating work: establish an exact structural collision threshold or extend the signature-injection window beyond nine with a memory-efficient calculation or modular argument.