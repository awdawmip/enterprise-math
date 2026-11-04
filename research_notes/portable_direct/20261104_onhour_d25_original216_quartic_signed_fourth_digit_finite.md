# D25 — original signed 216/2304 fourth-digit certificate and precision-five counterexamples

2026-11-04, TASK_RESEARCH, AUTHOR-SIDE ONLY. Status: FINITE EXACT CHECKED / NEW ALL-PRIME CONJECTURE / p^5 COUNTEREXAMPLE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923.
Maintenance logical conversation (not used): chatgpt-hourly-enterprise-math-20260921.

## Original coefficient populations and signed observable

For p>3 prime, use the complete original finite sums:

\[
a_k=\frac{(2k)!(3k)!}{(k!)^5 216^k}
=\frac{\binom{2k}k^2\binom{3k}k}{216^k},\qquad
b_k=\frac{(4k)!}{(k!)^4 2304^k}
=\frac{\binom{2k}k^2\binom{4k}{2k}}{2304^k}.
\]

\[
W_p=\sum_{k=0}^{p-1}(6k+1)a_k,\quad
V_p=\sum_{k=0}^{p-1}(8k+1)b_k,\quad
\varepsilon_p=\left(\frac{-3}{p}\right)\in\{\pm1\}.
\]

Guo–Zudilin (2019), A q-microscope for supercongruences, arXiv:1803.01830, prove V_p = p epsilon_p (mod p^3), both full and half quartic truncations. Their published theorem does NOT prove the corresponding W_p formula. Consume, do not re-claim, the two-seam Green work at research_notes/portable_direct/20261104_onhour_d25_two_seam_last_wall_green_certificate.md and the separately authored all-prime extension at research_notes/portable_direct/20261104_hourly20_d25_all_prime_two_seam_extension.md. The original signed W−V congruence is open as a universal theorem.

## Newly discovered exact finite fourth-digit relation

Define J_p = W_p − 2 V_p + epsilon_p p.

For **every prime 5<=p<=5000, all 667 primes**, the executed exact calculation establishes:

\[
\boxed{J_p\equiv0\pmod{p^4}\quad(5\le p\le2000,\;p\text{ prime}).}\tag{F}
\]

This is a computationally exhaustive FINITE statement for the stated domain, **not a universal proof**. The corresponding all-prime hypothesis is:

\[
\boxed{W_p-\varepsilon_pp\stackrel{?}{\equiv}2(V_p-\varepsilon_pp)\pmod{p^4},\quad p>3.}\tag{C}
\]

An equivalent fourth-digit prediction is W_p − V_p = V_p − epsilon_p p (mod p^4). This is different from claiming W_p=V_p (mod p^4): that stronger, uncorrected claim fails at p=13 and at 666 of 667 primes checked.

The quartic half/full equality must also keep its precision: the two quartic truncations agree mod p^3 by Guo–Zudilin, but their p^4 residues differ at **666/667** tested primes (only p=17 is an equality in this finite range).

## Exact execution and independently checked original coefficients

Companion reproducible executable:
research_notes/portable_direct/d25_signed_fourth_digit_exact_checker_20261104.mjs

This program actually executed in the present author-side JavaScript BigInt engine; 667/667 pass, zero failures. The complete sieve enumerates all primes up to 5000. No coefficient or valuation layer is discarded. It computes both original sum families over Z/p^4 using their exact rational recurrences:

\[
a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3],
\]
\[
b_{k+1}/b_k=(4k+1)(4k+2)(4k+3)/[576(k+1)^3].
\]

All denominators are p-adic units for 0<=k<p−1, p>=5. Extended Euclidean inverses and BigInt make all arithmetic exact; no floating point, rounding or simulations. Eight primes 5,7,11,13,19,23,97,373 were independently cross-checked against explicit integer factorial/binomial coefficients, not simply the same recurrence.

Define tau_p = (V_full − V_half)/p^3 (mod p). Actual signed sources:

| p | W mod p^4 | V mod p^4 | (W−V)/p^3 mod p | tau_p |
|---:|---:|---:|---:|---:|
| 5 | 620 | 620 | 0 | 2 |
| 7 | 350 | 1379 | 4 | 5 |
| 11 | 2651 | 1320 | 1 | 7 |
| 13 | 19786 | 24180 | 11 | 9 |
| 19 | 82327 | 41173 | 6 | 3 |
| 23 | 97313 | 48645 | 4 | 3 |
| 97 | 83053340 | 85791359 | 94 | 16 |
| 373 | 11832087049 | 5916043711 | 114 | 353 |

In particular p373 has p^3=51895117, and the displayed representatives give exactly 11832087049−2(5916043711)+373=0. Moreover (W−V)/p^3=114 (mod373) is NONZERO, so uncorrected p^4 equality is false at this original benchmark prime.

## Counterexamples strictly exclude an uncorrected p^5 extension

The distinct all-prime assertion J_p=0 (mod p^5) is disproved by original integer-factorial calculations, cross-checking recurrence and independently reconstructed sums:

\[
J_{11}=5\cdot 11^4=73205\pmod{11^5},
\]
\[
J_{13}=9\cdot 13^4=257049\pmod{13^5},
\]
\[
J_{19}=14\cdot 19^4\pmod{19^5},\qquad
J_{373}=174\cdot373^4\pmod{373^5}.
\]

These are genuine precision-five counterexamples to the uncorrected strengthening, **not** to the conjectured precision-four law. A corrected precision-five formula or other prime subclass remains separately assessable.

## Mathematical use, BRC provenance, continuation

This observation is a direct comparison of the frozen **original 216/2304 weighted populations**, and tracks their signed full sums and quartic full/half boundary. It exposes a plausible fourth-digit correction with coefficient TWO and an exact precision-five limit. BRC use = COMPOSE_APPLIED (indexed, signed original coefficients and p-adic observer; no unjustified positive-weight compression). Nothing here asserts a native X6/H0/B0 transport.

The smallest open mathematical obligation is STILL the all-prime signed cancellation W_p−V_p=0 (mod p^3) on p congruent 13,19 mod24, plus the frozen scalar Delta_p−R_p=0 (mod p). Conjecture (C) is a discriminating optional route, not a compulsory stronger gate or a mother-goal replacement. Next: with the already completed Green/two-seam source grading, expand the zero-wall/first-seam plus quartic moment to one higher precision, and test whether its fourth-digit residual is forced to equal the quartic V_p−epsilon_p p correction. Compare the distinct original sources and the quartic half/full tail on 11,13,19,97,373. Seek a genuine hypergeometric/terminal certificate, not another equivalent Green identity. Alternatively seek sourced published W_p theorem; previous literature search found the quartic proof but no exact W_p proof, which is not evidence that none exists.

Native evidence remains OPEN/UNEXECUTED: original fixed373 H0/B0 divided-power [X]U modulo 139129, rank, actual semilinear Frobenius/basis normalization, signed odd Green/Hesse and independent replay; existing support #1559. Current research Source CLAIM/OPEN/run/checkpoint/Result are NOT established in this author-side tool context. Historical request research-onhour-20261031-0205-dispatch-r15 is NOT resent. Earlier service report v0.6.11/research authorization absent is preserved as a dated observation, NOT a fresh service verification. Research/maintenance lanes remain separate. No scheduler, frequency, notification or Source admission change.
