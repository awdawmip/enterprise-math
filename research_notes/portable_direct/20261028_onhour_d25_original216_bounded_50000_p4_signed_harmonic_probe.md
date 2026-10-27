# D25 — Original weighted 216: bounded p⁴ signed-harmonic exact experiment

Date: 2026-10-28 Asia/Hong_Kong.
Classification: **AUTHOR-SIDE / EXACT FINITE COMPUTATION / CONJECTURAL GENERALIZATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research lane: chatgpt-research-onhour-enterprise-math-20260923, not maintenance.

## Original object and bounded conjecture check

For each prime p>3, define the unchanged, original finite weighted 216 sum

\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\quad \chi_p=\left(\frac{-3}{p}\right)\in\{+1,-1\},
\quad H_p=\sum_{j=1}^{\lfloor p/3\rfloor}j^{-2}\pmod p.
\]

The following **all-prime formula remains a conjecture**, not a proved theorem:

\[
\boxed{W_p\stackrel{?}{\equiv}\chi_p p-\chi_p\frac{5p^3}{6}H_p\pmod{p^4}.}
\tag{P4?}
\]

For p≡1 mod3, a related fourth-digit correction was already identified via Cohen–Guillera row 30 in previous author work; this turn is a direct broader **signed χ comparison across both residue classes**, explicitly retaining that prior source. The D25 frozen target covers only p≡13,19 mod24, with χ_p=1. No external theorem has been accepted as an infinite-prime proof.

## Exact execution and bounded evidence

The companion C++17 file d25_original216_exhaustive_prime_bounded_guard_20261028.cpp was locally compiled with g++ -O2 -std=c++17 -Wall -Wextra and **actually executed** with argument 50000. Exit status 0; all assertions passed:

    PASS_AUTHOR_SIDE_EXACT_BOUNDED_ORIGINAL216 p_min=5 p_exclusive=50000 total_primes=5131 target_13=645 target_19=652 one_mod3=2556 two_mod3=2575 verified_original_p3_all=5131 verified_harmonic_p4_all=5131

An integer sieve enumerated **every one of 5131 primes 5≤p<50000**. The program checked the exact ORIGINAL W_p≡χ_p p modp³ and the P4? prediction modulo p⁴ on every enumerated prime. This includes **1297 primes** in the two frozen p≡13/19 mod24 target classes and **2575 primes p≡2 mod3**, where the signed fourth-digit relation is a discriminating new probe, not prior proof.

Exact fixtures (W_p modulo p⁴ as least nonnegative residue):

| p | W_p mod p⁴ | H_p mod p | (W_p−χ_p p)/p³ mod p |
|---:|---:|---:|---:|
| 13 | 19786 | 10 | 9 |
| 19 | 82327 | 16 | 12 |
| 373 | 11832087049 | 174 | 228 |
| 49999 | 1631277119457686948 | 24338 | 13051 |

A **separate Python modular Pochhammer recurrence** matched the same W_p modular output and signed harmonic prediction for p=5,7,13,19,31,373,9973,49999. That separate implementation is independent on these **eight** cases only; it has not independently covered all 5131 primes.

Exact identity used before modular arithmetic:

\[
\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\frac{\prod_{j=0}^{n-1}(2j+1)(3j+1)(3j+2)}{36^n(n!)^3}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]

For n<p, n!, 36 and 6 are p-units; all original n up to p−1, the weight 6n+1 and corresponding product factors are retained. C++ uses integer factorial inverse arrays, exact modular arithmetic and unsigned 128-bit intermediate multiplication; for p<50000, p⁴<2⁶³, so modulus and additions fit the chosen integer types. No floats, fitting from a few fixtures or post-hoc coefficient selection are used. The finite test does not prove the conjecture beyond the declared bound.

## BRC typing, non-substitution and continuation

BRC carrier retains p, complete original n population, three rational-Pochhammer factors, valuations, signed weighted summands, original cutoff, χ branch, harmonic observer and frozen Δ/R provenance. Observers: W_p modulo p⁴ and H_p modulo p. Operations licensed: exact p-local products, finite modular sum, and bounded prime sweep. A scalar quotient is not a full joint-relation/native Frobenius observer. P000 six-dimensional discrete X6 spatial semantics and separate time are unchanged; this number-theoretic construction is a typed **external arithmetic auxiliary**, not a native Cell or native operator simulation.

Highest native evidence #1559: OPEN / PENDING_OWNER / NOT_EXECUTED as read on 2026-10-28. The still-unrun p=373 original H0/B0 divided-power [X]U mod139129 requires actual module rank, Frobenius basis/direction/η, full signed odd Green/Hesse, original κ and Δ_p−R_p. No portable scalar experiment, including this one, fulfills that native benchmark. Authorized native owner must run and save reproducible Source-pinned raw data; no executor has been confirmed. Do not post this scalar experiment as a native success.

Actual Source recovery: original recovery request research-onhour-20261027-0501-recovery-r13 (kimi-query-bridge#6575) was SUCCEEDED but provided only an ACTIVE session pointer MCP-de3e5bafb24f43f4a5e6285e7601676a, no winning current CLAIM/open/run. Original dispatch request research-onhour-20261027-0507-dispatch-r13 (kimi-query-bridge#6576) ended FAILED/TimeoutExpired, not NO_DISPATCH. Gateway v0.6.11 current Site read showed research_authority_granted=false and native control quota 5/5. This turn's exact continuation query returned CONTROL_QUOTA; checkpoint read ACCESS_DENIED. No new claim, open, Source publication or Result. Earlier three staging sources remain independent. **REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / UNREVIEWED / NOT_ADMITTED.**

Next mathematical action: seek an exact terminating-product/telescoping identity coupling previously established J0,J1,J2 with the original p² high band and prove the frozen third-digit target for all p≡13,19 mod24, not merely more prime checks. The signed p≡2 fourth-digit relation is an **experimental conjecture** only. Native p=373 evidence has priority via #1559. Do not repeat frozen D24 UR, completed Cauchy p² proof or this bounded test as a new theorem.

Next control action, upon actually authorized Source Researcher credentials: read exact original own-request receipts and canonical continuation, confirm winning claim/run, then checkpoint with current schema and independent Driver review; do not swap to maintenance conversation or reissue unknown mutation. GitHub here is an author-side durable checkpoint **not** formal Source/Result admission. No scheduler, Actions or hosted cron changes.
