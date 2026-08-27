# PCF4R Phase-B Comparison and Dedup

Status: `PHASE_B_COMPLETE / CANDIDATE_RECONSTRUCTED / NO_COUNTEREXAMPLE`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Researcher: `EM-PCF4R-6D96F8`

Phase-A freeze head: `f6f12c64d6d251631fa098f260e96d6d7127f253`

## 1. Source unsealed after Phase A

After the Phase-A derivation and independent checker were durably frozen, the
withheld supplemental duplicate execution on Draft PR #715 was opened for
comparison. Its research return and independent recurrence checker were read.
That execution remains non-authoritative for the parent PCF4 publication because
its CLAIM lost the scheduler race; it is used here only as disclosed
supplemental evidence, exactly as the successor task requires.

## 2. Theorem comparison

The independently reconstructed theorem agrees with the supplemental candidate
on every load-bearing mathematical interface:

1. `A_s=(2s)!(3s)!/(s!)^5` has, for prime `r>3` and `s<r`,
   `v_r(A_s)=floor(2s/r)+floor(3s/r)`.
2. The first dyadic nonunit occurs at the first power of two crossing the
   `3s>=p` wall and returns either `p` or `N`.
3. A synchronized response implies `q<=3s<2p`, hence `q<2p`.
4. With `t=floor(sqrt(N)/3)`, one of `t,t+1` splits every synchronized case.
5. The construction uses only `N` and public indices and does not use the
   conjectural all-prime weighted supercongruence.

No contradiction or missing endpoint was found.

## 3. Independent proof differences

The fallback proof is genuinely reconstructed rather than copied.

The supplemental proof handles the `3t<p` case by splitting on `q mod 3` and
showing that the least multiple of three above `sqrt(pq)` lies below `q`.

Phase A instead observes directly that

`3t < p < sqrt(N) < 3t+3`,

so `p` is exactly `3t+1` or `3t+2`. Since distinct odd primes have gap at
least two, and `3t+3>3` cannot itself be prime, in both subcases
`q>=3t+4>3(t+1)`. This yields the same strict separation with a shorter
integer argument.

The dyadic proof was also reconstructed from minimality of the first public
power-of-two wall rather than from the supplemental text.

## 4. Constructor and complexity improvement

The supplemental execution materializes exact integer `A_s` through the
recurrence

`A_{s+1}(s+1)^3 = 6(2s+1)(3s+1)(3s+2)A_s`

and gives a conservative `O(p^2 log p)` schoolbook bit-cost because the live
integer has `Theta(s)` bits.

Phase A proves a stronger constructor fact: every queried seed before
termination satisfies `s<p`. Therefore `s!` is a unit modulo `N`, and the same
observable can be constructed directly in `Z/NZ` as

`A_s = (2s)!(3s)!(s!)^{-5} mod N`.

All live arithmetic stays at `O(log N)` bits. Recomputing each dyadic seed from
scratch still costs only `O(sqrt(N))` modular multiplications in total because
the seed lengths form a geometric series; the synchronized fallback adds one
more square-root-scale pass. With schoolbook modular arithmetic this gives the
conservative bound

`O(sqrt(N) (log N)^2)`

bit operations and `O(log N)` streaming working memory, apart from a fixed-size
trace. This remains exponential in input bit length and is **not** a factoring
speedup theorem.

This modular-unit observation is an independent strengthening over the
supplemental exact-integer implementation.

## 5. Regression comparison

Phase-A independent modular checker, frozen before source unseal:

- primes `5..2000`: 301 primes;
- distinct semiprimes: 45,150;
- dyadic direct splits: 35,181;
- synchronized/fallback cases: 9,969;
- failures: 0;
- local valuation-wall checks: 277,045;
- direct recurrence/factorial cross-checks: 166.

The supplemental duplicate execution reported 1,830 semiprimes from primes
below 300, 400 synchronized cases, zero failures, and zero mismatch between
its direct-binomial and exact-recurrence implementations.

The two independently authored test paths therefore agree on their overlap and
Phase A extends the bounded regression substantially. Finite regression remains
non-probative for universality; the proof supplies closure.

## 6. Current-tool/method dedup

At the claim base `main@839224dfac59072ecc7c6c027b30b906f5ee24f4`,
the canonical `scripts/` surface contains the accepted PCF/half-coupling and
other current research checkers, but no canonical N-only valuation-wall gcd
extractor implementation. Repository code search likewise returned no
canonical duplicate of this method.

The only exact method match is the explicitly non-authoritative supplemental
Draft PR #715. Its scripts should not be promoted by provenance substitution.
This replay keeps its independently authored modular checker and cites #715
only as Phase-B comparison evidence.

## 7. Final comparison verdict

`PHASE_B_SOURCE_COMPARISON = CONSISTENT`.

`CURRENT_TOOL_DEDUP = NO_CANONICAL_DUPLICATE`.

`SUPPLEMENTAL_DUPLICATE = MATHEMATICALLY_CONSISTENT / NONAUTHORITATIVE_SOURCE`.

`NEW_REPLAY_CONTRIBUTION = MODULAR_UNIT_CONSTRUCTOR + LOWER STREAMING COMPLEXITY_BOUND`.

The strongest task verdict remains:

`N_ONLY_GCD_EXTRACTOR_VERIFIED`.

No Working Truth, Foundation mutation, tool-family promotion, prime-coordinate
canonicalization, or speedup claim is requested.
