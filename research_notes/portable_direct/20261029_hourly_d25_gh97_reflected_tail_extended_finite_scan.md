# D25/LIFT GH-97 — independent finite-range reflected-tail exception audit below 100,000

2026-10-29. Author: TASK_RESEARCH lane `chatgpt-research-hourly-enterprise-math-20260923`. **AUTHOR-EXACT-COMPUTED / BOUNDED_FINITE_RANGE / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is a finite observation and algorithmic completeness certificate, **not** a new universal theorem, native Source CLAIM/checkpoint, Result or independent review. Parent D25/LIFT/JT2 remains OPEN. Scientific freeze `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

## Precisely bounded statement

For primes `p=4d+3>=7` let `h_0=1`,
`h_(j+1)=h_j (4j+3)^3/[(4j+4)(4j+5)(4j+6)]`, `j<d`,
and the **reflected** (not original GH-3) tail
`R_p(9)=sum_(j=0)^d (8j+5)h_j 9^(d+1+j)/(d+1+j)` in `F_p`.

An independently implemented exact C++17 integer-arithmetic enumeration of **every** prime in the stated range returns:

`{p : 7<=p<100000, p prime, p%4=3, R_p(9)=0 mod p} = {3347}`.

Complete population: **4,807 primes**. The first range `7<=p<30000` has **1,632 primes**, zero set `{3347}`, matching the previous GH-95 Python implementation; the new range `30000<=p<100000` has **3,175 primes**, **no** additional exception. This extends, but never implies, global uniqueness or a density law.

## Exact algorithm and completeness scope

Program: `d25_gh97_reflected_tail_extended_scan.cpp`. Standard Eratosthenes sieve enumerates all primes below `100000` with `p%4=3`. For each prime, integer inverse table
`inv[1]=1; inv[k]=p-floor(p/k)*inv[p%k] mod p` for `2<=k<p`
is correct by the Euclidean identity `p=qk+r`, since `r=-qk mod p`.
Every denominator in `h_j` for `j<d` belongs to `[1,p-1]`; every tail denominator `d+1+j` belongs to `[1,(p-1)/2]`. Thus all modular divisions are well defined and the loop evaluates exactly all `d+1` terms, with no truncation or floating point.

The C++ `int64_t` multiplication chain reduces modulo `p` after each multiplication; with `p<100000` each un-reduced two-factor product is below `10^10`, safely within signed 64-bit range. The integer powers `(4j+3)^3` are also computed modulo `p` within the same bounds.

Command actually executed: `g++ -O2 -std=c++17 -Wall -Wextra d25_gh97_reflected_tail_extended_scan.cpp -o d25_gh97_scan && ./d25_gh97_scan`. Output: `old_range_count 1632 zeros 3347` and `new_range_count 3175 zeros`.

As an implementation-independence spot check, six primes were re-evaluated using Python's independently written `pow(a,-1,p)` per denominator rather than the C++ recurrence table. Both implementations returned exactly:

| p | R_p(9) mod p |
|---:|---:|
| 7 | 1 |
| 3347 | 0 |
| 30011 | 823 |
| 40031 | 28279 |
| 65519 | 16888 |
| 99991 | 91259 |

This is an author implementation check of a declared finite enumeration, not an independent mathematical admission or a claim about untested primes.

## Source-observer and next action

BRC decision `COMPOSE_APPLIED` to GH-95/GH-96 source-labelled p-adic carrier: prime p, reflected index j, operator=recurrence/finite source sum, observer `R_p(9) mod p`, with original target `T_(p,9)` strictly separate. This new bounded result supplies an adversarial test for any conjectured CM/Jacobi/WZ classification: it must predict the zero at 3347 and the observed absence of additional zeros in the 3,175 newly checked primes, without upgrading a finite scan to an all-prime proof.

**Next smallest theoretical unit:** derive a *noncircular arithmetic criterion* for `R_p(9) mod p` via finite-field character sums or WZ telescoping; test whether the GH-96 nonliftable stationary-root mechanism is structural or accidental. Original GH-3 `T_(p,9)=0 mod p`, GH-83 Laurent `B_0L`, GH-20/21 second digit, W/S, six Hasse ports, R23/R36 and native p=373 remain separate. No native CLAIM, OPEN, Source checkpoint, reviewer disposition or P000/worldview change follows from this portable calculation. Control/old service sessions remain protected under #1558.

Executed program SHA256: `70b9ea6c6db0dca56b701617e5c7827ed05e68668ccc3d9c5173638a3d58bf38`. C++ Git blob expected `004964bb6929d635cecda498e4089fbd3d45031a`.
