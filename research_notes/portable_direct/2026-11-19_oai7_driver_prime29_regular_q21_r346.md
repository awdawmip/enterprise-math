# OAI7 r346 — A 29-row exactly regular codebook with worst-test q=21/29

Date: 2026-11-19. Scope: exact finite external cyclic-group shared-shift model, p=29, n=5, u=4, h=0, T=29^(3/4). Status: explicit construction verified by exhaustive finite test enumeration. Author-side scientific evidence; no Native Result, independent Native acceptance, X6 transfer, formal Task completion or parent closure is claimed. Preserve OAI7 original researcher EM-EMF6D046-5A2844 and r307–r345 provenance.

## Construction and result

Sample uniformly from the following 29 **pairwise distinct 5-element subsets** of F_29:

    rows = [
      [1,9,10,20,28],
      [4,13,17,20,21],
      [5,13,14,16,25],
      [2,6,10,14,19],
      [9,13,16,24,27],
      [6,11,21,22,25],
      [8,12,15,19,26],
      [2,5,6,7,8],
      [11,12,21,25,26],
      [0,3,8,9,17],
      [4,8,14,18,26],
      [1,6,18,22,23],
      [6,11,18,23,25],
      [12,13,19,22,28],
      [0,11,16,17,23],
      [2,4,10,15,23],
      [7,8,17,19,27],
      [0,2,4,5,28],
      [0,18,20,26,28],
      [3,9,11,17,18],
      [3,5,7,19,21],
      [2,7,15,20,22],
      [1,4,14,23,27],
      [0,3,10,24,27],
      [3,10,16,21,28],
      [1,12,14,24,25],
      [9,13,15,16,22],
      [1,15,20,24,26],
      [5,7,12,24,27]
    ]

Every symbol 0,...,28 occurs **exactly five times**. By the regular bipartite incidence matching decomposition already established in r337, the five elements of each row admit a deterministic position ordering so that each coordinate is exactly uniform over F_29. The joint ordered sequence has exactly 29 equally likely distinct values, so its entropy is exactly log 29, with no auxiliary random ordering seed.

For any deterministic four-element K, put

    V_C(K) = 29 - |{k-c mod 29 : k in K, c in C}|.

The failure event V_C(K)>29^(3/4) is equivalent to V_C(K)>=13, i.e. to union cardinality at most 16. Exhausting all binom(29,4)=23,751 tests gives this histogram of **number of failing rows**:

| Failing rows | Test sets |
|---:|---:|
| 12 | 29 |
| 13 | 435 |
| 14 | 1,508 |
| 15 | 2,378 |
| 16 | 3,103 |
| 17 | 4,611 |
| 18 | 5,655 |
| 19 | 3,538 |
| 20 | 2,378 |
| 21 | 116 |

These counts sum to 23,751; 21 is the exact maximum (for instance K={0,2,5,11} attains it). Hence

    q = max_K Pr_C{V_C(K)>29^(3/4)} = 21/29.                        (346.1)

Compared with r344's exact regular construction at 24/29, this reduces the worst-test failure probability by exactly 3/29, or 12.5% relative. r345's universal 29-row lower bound 16/29 leaves a finite gap. No optimality of the new codebook is asserted.

## Standalone certificate: exhaustive exact integer checker

Python 3 standard library, independent of how the 29 rows were discovered. Insert the literal row list above into the rows variable (the list can be copied unchanged).

    from itertools import combinations
    from collections import Counter

    P, N, U = 29, 5, 4
    assert len(rows) == P
    assert len({tuple(r) for r in rows}) == P
    assert all(len(r) == N and len(set(r)) == N for r in rows)
    assert all(sum(x in r for r in rows) == N for x in range(P))
    hist = Counter()
    for K in combinations(range(P), U):
        bad = 0
        for C in rows:
            covered = {(k-c) % P for k in K for c in C}
            V = P-len(covered)
            bad += (V**4 > P**3)  # exact test for V > 29^(3/4)
        hist[bad] += 1
    expected = {
        12: 29, 13: 435, 14: 1508, 15: 2378, 16: 3103,
        17: 4611, 18: 5655, 19: 3538, 20: 2378, 21: 116
    }
    assert dict(hist) == expected
    assert sum(hist.values()) == 23751 and max(hist) == 21
    print("exact q = 21/29; all 23751 tests verified")

For exact equal marginals, run the constructive regular-bipartite perfect-matching decomposition from r344 §3 on these rows; its hypotheses are met without change.

## Derivation, coverage and provenance

A finite search used degree-preserving two-row symbol exchanges starting from the r344 regular ensemble, reducing the worst-test maximum from 24 to 21. The random search is discovery only. The published 29x5 array and the exhaustive deterministic checker are the complete finite certificate. The verifier was actually executed in this research context, checking all 23,751 tests, all 29 occurrence degrees, pairwise distinct rows and the exact ten-bin histogram; q=21/29 is established for the stated parameters.

References:
- r344: enterprise-math@6d5b98d14202cefb37f34565c68c3d49755430d7, research_notes/portable_direct/2026-11-19_oai7_driver_hypergeometric_average_prime29_regular_mix_r344.md.
- r345: enterprise-math@ec5388eb8e4f9bf4cf2aa1c92fd8dee08de2ea9f, research_notes/portable_direct/2026-11-19_oai7_driver_prime29_bad_test_floor_r345.md.
- r337 matching/equal-marginal criterion: enterprise-math@cf352564a8f985fbc3151783fa0ee74f1a0b2a7f, research_notes/portable_direct/2026-11-18_oai7_driver_zero_overhead_equal_marginal_codebook_criterion_r337.md.
- Native OAI7 Task RS-OAI7-028-C-20261007-6F2A81 / publication TP2-96FAC49786245691AE19, subject to separate current control/owner/Result checks.

The growing-prime sharp-second-order q_p->0 objective remains open. This exact finite construction supplies a stronger testbed for incidence trades, concentration and structured-ensemble analysis.
