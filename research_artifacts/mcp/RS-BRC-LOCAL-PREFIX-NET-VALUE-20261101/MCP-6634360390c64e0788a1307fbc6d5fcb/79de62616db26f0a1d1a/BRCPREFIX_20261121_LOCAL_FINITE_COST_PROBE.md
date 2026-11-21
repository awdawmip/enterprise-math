# BRC prefix net-value: exact local trial (2026-11-21)
Status: LOCAL_FINITE_EXPERIMENT / NOT_REVIEWED. Formal Task: RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101.
Scientific inputs: enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14, src/enterprise_math/brc_opportunistic_shortcuts.py, src/enterprise_math/brc_multiplier_priority_jump.py, experiments/brc_squarefree_kernel_compression_probe.py.

## Experiment
Fixed M=1000; retain the exact same 625 odd-N scan-irreducible multipliers (residues 0,1,3,5,7 mod 8). Compare the existing structural order, 13-kernel prefix (98 multipliers) followed by structural fallback, learned fixed-20 prefix followed by structural fallback, and learned-20 + 13-kernel prefixes followed by structural fallback. The latter three de-duplicate before appending, so all four have identical candidate sets.

The test evaluator is the exact immediate multiplier-Fermat witness of the preexisting reference experiment, using integer isqrt and gcd: t=m*N; x=ceil(sqrt(t)); delta=x*x-t; y=isqrt(delta); success iff y*y=delta and 1<gcd(x-y,N)<N. This standalone Python source-aligned reproduction does NOT import or time native BRC direct-jump transport. Each trial stops on success or after all 625 candidates.

Generation: Python random.Random(20261121), Eratosthenes primes and two groups, 220 unique semiprimes each, conditioned on N.bit_length() in {31,32}. Balanced: distinct primes from [40009,60013]; imbalanced: one prime [20011,26003] and one [80021,120011]. Group generation uses balanced first, then imbalanced, both sorted by N. Factor labels are generation/ground truth only, never algorithm input. Bit ranges and factor distributions were declared prior to these evaluations.

| Complete order | Balanced mean candidate tests | Imbalanced mean candidate tests | Hits balanced / imbalanced |
|---|---:|---:|---|
| structural | 250.136364 | 222.272727 | 150/220 ; 178/220 |
| learned20 + fallback | 254.854545 | 230.636364 | 150/220 ; 178/220 |
| kernel13 + fallback | 275.059091 | 241.681818 | 150/220 ; 178/220 |
| learned20 + kernel13 + fallback | 272.995455 | 244.500000 | 150/220 ; 178/220 |

Each complete order has the same hit/miss set: 70 balanced misses, 42 imbalanced misses. Every miss executes 625 tests, so p90 including misses = 625 for both populations under every order. Relative to structural baseline, learned20 changes mean test count by +1.89% balanced and +3.76% imbalanced; kernel13 by +9.96%, +8.73%; combined by +9.14%, +10.00%.

## Scope and cost
Within the specified fixed immediate-Fermat evaluator and candidate-count cost, none of these three prefixed complete orders reduces mean evaluations on the two test populations. This is a local NO_GAIN-in-candidate-count finding, not a result about all bit lengths, regimes or implementations. It does not overturn historical training/validation results at M=100 or claims about useful specialist orders elsewhere.

The one-pass timing measurements were not relied on (non-interleaved run order and processor variation). Candidate schedules were precomputed outside the timed loop. No conclusion is drawn yet about native direct-jump backend speed, per-input setup, correction counts, cache, peak memory or tail wall time. For any complete scan, a failed input cannot reduce candidate tests by reordering; benefits on hit cases must compensate dispatch/setup costs and any variable per-candidate expense.

Reproduction details: generate primes inclusively with the standard sieve; choose unique factor products by Random.sample(prime_pool,2) for balanced and Random.choice(small_pool), Random.choice(large_pool) for imbalanced; reject bit lengths outside 31..32; use factor_pair_count(m)=sum(1 for a in 1..isqrt(m) if m%a==0); structural score is that count for odd m and count for m//4 when m divisible by four; sort all other representatives by decreasing score then m, keeping m=1 first. Kernel prefix selects m with squarefree_kernel(m) in (1,13,14,3,15,2,5,6,30,22,105,33,7); learned prefix is (1,48,96,8,15,80,21,16,56,45,35,3,72,7,99,88,40,55,9,24). Append unseen structural-order candidates.

Next scientific test: run the ACTUAL existing BRC direct-jump backend and existing RegimeShortcutLedger on matched N, with predeclared per-input work/setup, correction, gcd, fallback and tail measurements. Retain historical prefix evidence and owner boundaries; independent review remains separate.