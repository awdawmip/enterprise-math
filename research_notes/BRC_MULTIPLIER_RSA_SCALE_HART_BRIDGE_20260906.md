# BRC multiplier scaling / Hart-OLF bridge — Round 7

Status: `PRIOR-ART BRIDGE + RSA-SCALE BOUNDARY + FINITE PERFORMANCE EVIDENCE / NO NEW FACTORIZATION COMPLEXITY CLAIM`
Date: `2026-09-06`
Parent tools: `t0.brc_multiplier_basin`, `t0.brc_multiplier_transition`, `t0.brc_square_gap_prefilter`, `t0.brc_multiplier_priority_jump`

## 1. Why this round exists

The previous rounds showed real constant-factor gains for scanning a fixed small multiplier set: exact BRC root/remainder transport removes repeated integer roots, the mod-4032 table rejects most impossible square gaps, and a mod-4 feasibility rule removes 25% of odd-N multipliers.

This round asks whether those finite gains can be extrapolated to RSA-like balanced semiprimes.

The answer is **no for a fixed ceiling such as m<=100**. The relevant multiplier scale grows with N, and the mechanism is classical Hart/Lehman multiplier-Fermat mathematics.

## 2. Immediate-square bridge is Hart OLF prior art

For a multiplier k and odd N, let

`x = ceil(sqrt(kN))`, `g = x^2-kN`.

If `g=b^2`, then

`kN=(x-b)(x+b)`

and `gcd(x-b,N)` can expose a factor. This is exactly the one-line-factor / multiplier-Fermat surface studied by William B. Hart (2012), itself connected to Lehman.

Hart's published OLF loops over multipliers and tests the ceiling gap for squarehood. His practical optimization also premultiplies N by `M=480`. Current FLINT exposes `n_factor_one_line` and its implementation still recomputes an integer square root for every loop iteration.

External prior-art references:

- W. B. Hart, *A One Line Factoring Algorithm*, J. Aust. Math. Soc. 92 (2012), 61-69, DOI 10.1017/S1446788712000146.
- FLINT `src/ulong_extras/factor_one_line.c`, current implementation with `FLINT_ONE_LINE_MULTIPLIER 480`.
- FLINT `n_factor_lehman`, separate classical Lehman implementation.

The Enterprise contribution claimed here is **only** the typed BRC implementation bridge: retain `(root,remainder)` and transport it between multipliers instead of rematerializing each root. No novelty is claimed for the factorization principle, multiplier 480, or the N^(1/3) search scale.

## 3. RSA-style failure of m<=100

Balanced random semiprimes were generated from two independent same-bit primes. For each N we tested every mod-4-feasible `1<=m<=100` using the exact immediate ceiling-square condition.

Observed bounded hit counts:

- 5000 semiprimes from 32-bit primes (roughly 64-bit N): only 5 had any hit with m<=100.
- 3000 semiprimes from 64-bit primes (roughly 128-bit N): no hits were observed in the run.

Therefore the excellent small-number coverage in earlier rounds was a small-factor diagnostic and must not be extrapolated to cryptographic balanced semiprimes.

## 4. Why the multiplier scale is N^(1/3)

Write `N=pq`, `p<q`, and a same-parity multiplier split `k=uv` so a successful representation may be arranged as

`x-b=up`, `x+b=vq`.

Immediate ceiling success requires

`(vq-up)^2 < 4(up+vq-1)`.

Let `r=q/p`. Then

`|vq-up| = p v |r-u/v|`.

For balanced factors `p,q ~ sqrt(N)` and balanced multiplier splits `u,v ~ sqrt(k)`, the right-hand side of the ceiling condition has square-root scale `N^(1/4) k^(1/4)`. A generic best rational approximation with denominator v has error scale `|r-u/v| ~ 1/v^2 ~ 1/k`, giving left-hand scale `N^(1/2) k^(-1/2)`.

Balancing the two scales gives

`N^(1/2) k^(-1/2) ~ N^(1/4) k^(1/4)`

hence

`k ~ N^(1/3)`.

This is a heuristic scaling derivation, not a new theorem. It matches Hart's OLF heuristic `O(N^(1/3+eps))` and the classical Lehman search scale.

Finite balanced-prime scans support the exponent. Across prime bit sizes 10..26, the fitted slope of `log2(first_hit_multiplier)` against approximate `log2(N)` was about `0.322`, close to `1/3`. Median `m/N^(1/3)` stayed on an O(1) scale (roughly 0.27..0.39 in these runs).

## 5. Structural score helps constants, not the exponent

For moderate balanced semiprimes we scanned up to `M=2*floor(N^(1/3))`.

Sorting feasible multipliers by the existing same-parity factor-pair score reduced first-hit ranks materially, e.g.:

| prime bits | median M | increasing feasible median rank | structural median rank |
|---:|---:|---:|---:|
| 18 | ~6.8k | 694 | 342.5 |
| 20 | ~16.8k | 1692.5 | 844 |
| 22 | ~43.1k | 2874 | 949.5 |
| 24 | ~109k | 13475 | 3086.5 |

A conjectural sparse mode keeping only multipliers with at least three same-parity factor pairs used about 42-51% of candidates in these windows while retaining about 97-100% of the bounded hits. This is **not safe** and is not promoted to the production router; it is only evidence for a future conjectural fast mode with fallback.

Nothing here proves an exponent improvement over N^(1/3).

## 6. Hart-480 as a natural bridge

Hart's empirical premultiplier `480` has many small factor splits. Under the Enterprise structural score, `480/4=120` has 8 unordered factor pairs, substantially more than the best m<=100 score from the earlier experiment. This explains why the earlier score naturally points toward the same high-divisor multiplier class, but it also downgrades novelty: the high-divisor premultiplier idea is classical/prior art.

The useful new composition is computational:

`K=480*N`

then Hart iterations `i=1,2,...` are exactly the BRC multiplier-root sequence for base K. The existing BRC recurrence can therefore replace

`isqrt(i*K)` at every i

with one initial root and exact `(J_i,R_i)->(J_(i+1),R_(i+1))` transport, followed by the existing mod-4032 gap prefilter.

## 7. Finite Hart-480 transport benchmarks

For fixed iteration counts, direct Hart-style scanning (fresh target `isqrt` each iteration) was compared with BRC consecutive transport plus the same mod-4032 square-gap filter.

Representative whole-scan Python timings showed:

- single-word/small-integer region: no reliable gain; at 64 bits BRC overhead can lose.
- 256 bits: about 1.1-1.2x in tested windows.
- 512 bits: about 1.2-1.35x.
- 1024 bits: about 1.3-1.45x.
- 2048 bits: about 1.15-1.4x.

For 10,000 iterations, tested full-scan speedups were approximately 1.13x (256 bit), 1.29x (512 bit), 1.28x (1024 bit), and 1.40x (2048 bit).

These are implementation-level finite timings, not complexity results. Hart/FLINT's intended single-word domain already has very cheap integer roots, so the BRC transport is most interesting as a multiword/batch implementation experiment, not as a claim of improving FLINT's current single-word factorer.

## 8. Coverage versus iteration count

With Hart premultiplier 480 and balanced random semiprimes:

- 100 iterations: hit rate fell rapidly with factor size (about 19.5% at 20-bit factors, 3.3% at 24-bit factors, zero observed at 28/32 bits in the cited bounded runs).
- 1,000 iterations: about 60.5% at 20-bit factors, 17.3% at 24-bit, 5% at 28-bit, zero observed at 32-bit.
- 10,000 iterations: about 99.5% at 20-bit factors, 81.3% at 24-bit, 16.3% at 28-bit, 8% at 32-bit.
- 100,000 iterations: about 85% at 28-bit factors and 40% at 32-bit factors in small validation samples.

This is consistent with the growing N^(1/3) search horizon.

## 9. Predictor-table scaling boundary

The current production BRC transition table stores high-precision dyadic predictors through 100 multipliers. Extending the same representation linearly gives, for a 4096-bit-N static precision near 2058 fraction bits:

- 1,000 transitions: about 0.26 MB raw constants;
- 10,000 transitions: about 2.58 MB;
- 100,000 transitions: about 25.8 MB.

Exact runtime generation of those constants in the current Python environment took roughly 0.012 s, 0.093 s, and 0.91 s respectively, but this cost is only attractive when amortized across many N values or cached. A giant checked-in table therefore does not solve the asymptotic candidate-count problem; it merely trades compute for linear storage.

**Decision:** do not expand the production static table to 100k merely to chase Hart coverage. Future work should seek a block/analytic predictor or batch reuse before making a large static-table commitment.

## 10. Adaptive N-visible routing result

Initial-root phase bins and small N-visible residue features were tested as routers for the m<=100 ordering. They can improve rank relative to the purely structural order on some distributions, but they did not robustly beat a globally learned fixed order and did not produce a stable wall-clock gain across distribution shifts.

**Decision:** no adaptive phase router is promoted from this round. This negative result should prevent reintroducing an overfit N-visible heuristic without stronger evidence.

## 11. Strategic frontier

The multiplier program now has a clean separation:

1. **Exact BRC implementation gains:** retained `(J,R)`, consecutive/direct transport, mod-4 skip, square-gap residue filtering.
2. **Classical factorization layer:** Fermat/Hart/Lehman multiplier principle, premultiplier 480, N^(1/3) scale.
3. **Heuristic layer:** factor-pair priority and possible sparse high-divisor modes.

The next worthwhile attack is not another small m<=100 ordering tweak. It is one of:

- a table-free/block predictor for long Hart-style multiplier streams;
- batch-many-N reuse of one predictor table;
- a rigorously bounded sparse multiplier family that reduces candidate count below a constant fraction without losing the Hart/Lehman coverage guarantee.

Until one of those succeeds, no RSA-breaking or asymptotic speedup claim is justified.
