# PREFIX-859 — Exact two-read odd-modulus Pareto frontier and a non-Mersenne arithmetic family

Date: 2026-11-17. Scientific status: AUTHOR_PROVED (algebraic criterion and orbit family); EXACT_FINITE_EXHAUSTION (p=3..11); NOT_INDEPENDENTLY_REVIEWED; NOT_ADMITTED.

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (same line as PREFIX-858). Predecessor: `2026-11-17_r6_prefix858_arithmetic_orbit_coldstart_family.md`. This note concerns an auxiliary, named, positive BRC integer-residue observer; it makes no claim of an admitted physical X6 Cell/Link/Port time-event correspondence.

## Exact problem and nontrivial two-read regime

Let the named state be `x in {0,1}^p`, `U(x)=sum_i 2^i x_i`, `N=2^p`. One physical heartbeat permits either no change or a flip of one named bit. At two successive heartbeats observe `c_t(S+U_t) mod q1` and `c_(t+1)(S+U_(t+1)) mod q2`. The known `S` and power-of-two multipliers `c_t` can be inverted for odd `q1,q2`; hence the informative readings are `U_t mod q1` and `U_(t+1) mod q2`. The initial state is wholly unknown; only the *terminal complete named state* must be recoverable, not the path.

This optimization deliberately restricts `q1,q2` to odd integers `3 <= qi < N`. Both individual readings are thus noninjective on all N states. Without that constraint, an odd modulus `N+1` alone identifies U in `p+1` bits, rendering minimization of two-read *total bits* a different and often trivial objective. We optimize separately (i) `ceil(log2(q1))+ceil(log2(q2))`, (ii) `max(ceil(log2(q1)),ceil(log2(q2)))`, and (iii) the coordinatewise Pareto frontier. These are **raw port widths**, not entropy-coded average message lengths.

## Theorem 859-A: exact collision-distance criterion for arbitrary ordered moduli

For each possible terminal integer `v in {0,...,N-1}`, define its legal immediate predecessor set

`P_p(v)={v} union {v XOR 2^i : 0<=i<p}`.

For any first modulus `q1`, define the **forbidden terminal distance set**

`F_p(q1)={w-v:0<=v<w<N, (P_p(v) mod q1) intersects (P_p(w) mod q1)}.`

Then the ordered two-read protocol `(q1,q2)` recovers *every terminal complete named state* if and only if

`F_p(q1) intersect {q2,2q2,...,floor((N-1)/q2)q2} = empty.`

**Proof.** Different terminal states `v,w` produce an identical second observation exactly when `q2 | (w-v)`. Each can be reached in one legal step from precisely the elements of its predecessor set. Their first observations coincide exactly when those two sets have a common residue modulo `q1`. Both equalities are necessary and sufficient for an indistinguishable pair of legal two-heartbeat histories. A pair exists precisely when `w-v` is in both displayed sets. If none exists, the two observed residues determine the terminal state uniquely. Multiplication by a unit and subtraction of the known S do not change these fibers. QED.

This is a **complete finite decision algorithm** for arbitrary ordered `q1,q2`, and does not require `q2=N-1` as in PREFIX-858.

**Corollary 859-B (a time-varying observer is essential in this regime).** Identical moduli `q1=q2=q<N` never succeed: take terminal states 0 and q with unchanged (no-op) predecessors, whose readings are both 0 modulo q at both steps.

## Theorem 859-C: a new non-Mersenne infinite orbit family

For all integers `p>=9` with `p congruent 3 (mod 6)`, the ordered protocol

`(q1,q2)=(21,2^p-1)`

recovers every terminal state. The first observer always costs **5 bits** and the second costs **p bits**.

**Proof.** The multiplicative orbit of 2 modulo 21 has length 6 and is `{1,2,4,8,16,11}`. Since `p>=9`, the precursor-residue set of terminal 0 is exactly
`A={0,1,2,4,8,11,16}`. Its modular sumset is all residues `0..20` except `7,14`: enumerate the 49 ordered sums (or use the independent short checker). Since `p=6m+3`, `(2^p-1) mod 21=7`. As in PREFIX-858 theorem A, the only possible collision under `q2=2^p-1` is between terminal 0 and terminal `2^p-1`. The first precursor residues are `A` and `7-A`, which are disjoint because `7 notin A+A`. QED.

This supplies a distinct non-Mersenne constant-width family. It is not a universal minimum over all moduli, and the five-bit first read has a different arithmetic period from the previously exhibited four-bit Mersenne family.

## Theorem 859-D: finite exact resource frontier

Applying theorem 859-A exhaustively to **every ordered odd pair** `3<=q1,q2<2^p` for each `p=3,...,11` gives the following results. The witness format is `(q1,q2)`; displayed Pareto pairs are `(bits1,bits2)`. The complete counters and witnesses reside in `PREFIX859_R6_TWO_READ_ODD_PARETO_RESULTS.json`.

| p | successful ordered pairs | minimum total bits | minimum peak bits | Pareto widths (witness moduli) |
|---|---:|---:|---:|---|
| 3 | 0 | — | — | none |
| 4 | 0 | — | — | none |
| 5 | 1 | 10 | 5 | (5,5):(17,31) |
| 6 | 22 | 11 | 6 | (5,6):(25,63); (6,5):(63,25) |
| 7 | 334 | 11 | 6 | (4,7):(15,127); (6,6):(33,55); (7,5):(127,27) |
| 8 | 2927 | 13 | 7 | (5,8):(29,253); (6,7):(33,121); (7,6):(95,57); (8,5):(253,29) |
| 9 | 19961 | 14 | 7 | (5,9):(21,511); (6,8):(33,187); (7,7):(65,117); (8,6):(209,57) |
| 10 | 113991 | 15 | 8 | (6,9):(33,385); (7,8):(65,221); (8,7):(207,115); (10,6):(893,61) |
| 11 | 586424 | 15 | 8 | (4,11):(15,2047); (6,10):(33,715); (7,9):(65,429); (8,8):(171,247); (9,7):(437,115); (11,6):(1991,61) |

In particular, for `p=7` the minimum **total** is 11 bits using `(15,127)`, whereas the minimum **maximum per-read port width** is 6 bits using `(33,55)` (12 raw bits total). This realizes a nontrivial latency/bandwidth balancing tradeoff in the exact BRC source observer. At `p=11` the peak optimum is 8 bits `(171,247)`, while the minimum-total design is a 4-bit plus 11-bit observer `(15,2047)`.

No inference is made beyond `3<=p<=11` from the finite exact table; the orbit family above has its independent infinite proof.

## Execution, audit and reproducibility

- `PREFIX859_R6_TWO_READ_ODD_PARETO_CHECK.cpp`, C++17 standard library, enumerates every first modulus, every terminal state and all p+1 legal predecessor possibilities; it records forbidden terminal differences and scans *every* second odd modulus and every nonzero multiple below N. It then calculates exact widths and undominated width classes. Run `g++ -O3 -std=c++17 -o check PREFIX859_R6_TWO_READ_ODD_PARETO_CHECK.cpp && ./check > reproduced.json`.
- `PREFIX859_R6_TWO_READ_ODD_PARETO_RESULTS.json` records the full nine-case summary with count, minimum widths and bounded witness lists. `-1` means no admissible pair in the restricted search space. Compare reproduced JSON exactly against the committed file.
- `PREFIX859_R6_INDEPENDENT_CROSSCHECK.py` independently enumerates the *trajectory-to-observation map*, checks all reported frontier/optimal witnesses and exhaustively recounts valid odd pairs for `p=3,...,7`. Run `python3 PREFIX859_R6_INDEPENDENT_CROSSCHECK.py PREFIX859_R6_TWO_READ_ODD_PARETO_RESULTS.json`. This check does not reuse the forbidden-distance procedure.

Local execution for this run: compiled the C++17 exhaustive checker, obtained the nine-case results (through p=11); an independent Python direct-trajectory implementation agreed on the earlier p=3..7 counts and checked selected valid witnesses across p=3..11. The independent checker provided here is a reproducible version of that method; its GitHub upload/readback alone is not represented as remote execution. The closed-form orbit complement calculation is exact.

## Scope, limitations, and next science

This observer retains all p named provenance bits as its scientific state and only compresses readings, with the usual freedom to keep observers/decoders. The count does not include retaining or computing the old state, decoder complexity, or an X6 native dynamics realization. Oddness ensures the time multiplier `c_t` is invertible; using even q at early times may produce other limited-horizon protocols but cannot be silently treated as permanently valid under the power-of-two heartbeat weighting.

Next: prove analytic upper/lower peak-bit bounds for growing p (rather than extrapolating the nine-case table), and determine whether nonperiodic or feedback-controlled observers yield a better long-time **sliding-window** frontier. A genuinely native X6 Cell/Link/Port claim additionally needs source/target permission, triadic incident event and preserved source-provenance evidence.

Ownership: this is separately persisted auxiliary BRC mathematics, not an authenticated CLAIM or a checkpoint on `RS-X6-NATIVE-TIME-DYNAMICS`. Keep its verified native task frontier and its active-owner semantics separate. No mathematical admission/review is claimed.
