# D25 — One-field cross-grade second-digit certificate after accepted first-digit UR

Date: 2026-11-09 (Asia/Hong_Kong). **AUTHOR_SIDE_DERIVED / EXACT_18_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** Same Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3; Research logical lane chatgpt-research-onhour-enterprise-math-20260923.

## 1. Exact inherited facts

For all target primes p≡13,19 (mod 24), let p=6m+1. The accepted first-digit result includes original W216≡p (mod p²); Guo–Zudilin's V2304 half/full result gives V_half≡p (mod p³) for these prime classes. The already derived cross-grade decomposition (see the previous D25 grade1 first-jet note) is

W_full−V_full ≡ W0−V_half + p K1 (S0+pS1)+p² K2 S2 (mod p³),

where W0 retains indices 0..2m at p³ precision; V_half retains indices 0..3m at p³ precision; K1,S0 are p²-precision p-units/sums; S1, K2, S2 are mod-p data. For complete definitions and proof of the first jet, read `research_notes/portable_direct/20261109_onhour_d25_w216_grade1_first_jet_cross_grade_certificate.md`. This note consumes that result, not its proof again.

## 2. Exact mod-p target (new lower-precision terminal observer)

The already established first-digit equality W_full≡V_full (mod p²) and the cross-grade formula show

W0−V_half+p K1 S0 ≡0 (mod p²).

Define the following *well-defined element* of F_p:

B_p = (W0−V_half+p K1 S0)/p² modulo p,

where the numerator is evaluated as a p-adic integer and all lower-precision representatives give the same quotient residue (changes to K1 or S0 by multiples of p² change the numerator by multiples of p³).

**The exact reduced second-digit certificate is**

Theta_p := B_p + (K1 mod p) S1 + K2 S2 (mod p).

Then, for every prime p≡13 or19 (mod24),

**Theta_p = 0 in F_p if and only if W_full=V_full modulo p³.**

By the previously established source port/crosswalk, this is also an equivalent *vanishing criterion* for the frozen LIFT statement Delta_p−R_p=0 (mod p); we do not identify the numerical values Theta_p and Delta_p−R_p without an explicit unit/comparison map.

### Proof

Subtract V from W in the exact grade decomposition. The grade-0 plus p K1 S0 block is divisible by p² by the accepted first-digit result. After dividing the difference by p² and reducing modulo p, the surviving contributions are exactly B_p, (K1 mod p)S1, and K2 S2. The equivalence follows because p² times a p-adic residue vanishes modulo p³ precisely when that residue vanishes modulo p. No p^0 or p^1 information was discarded before establishing divisibility.

This strictly isolates the *one remaining divided second digit* as three explicitly sourced F_p coordinates. It does not assume that any one coordinate vanishes separately and does not solve the all-prime cancellation.

## 3. Independent exact 18-prime check

The original full binomial sums and independent grade-jet recurrence were run in `d25_w216_grade1_jet_cross_grade_20261109.py`. This second projection was separately evaluated from the saved full integer data, verifying p²-divisibility of the B numerator and Theta=0 for the 18 checked primes. Each row gives (B_p, (K1 mod p)S1, K2 S2) in F_p:

| p | B | jet | grade2 |
|---:|---:|---:|---:|
| 7 | 5 | 4 | 5 |
| 13 | 4 | 12 | 10 |
| 19 | 2 | 8 | 9 |
| 31 | 1 | 7 | 23 |
| 37 | 31 | 23 | 20 |
| 43 | 5 | 3 | 35 |
| 61 | 31 | 13 | 17 |
| 67 | 3 | 6 | 58 |
| 73 | 38 | 4 | 31 |
| 97 | 40 | 32 | 25 |
| 109 | 67 | 26 | 16 |
| 127 | 85 | 124 | 45 |
| 157 | 3 | 56 | 98 |
| 163 | 45 | 95 | 23 |
| 193 | 121 | 11 | 61 |
| 211 | 130 | 90 | 202 |
| 229 | 152 | 99 | 207 |
| **373** | **190** | **290** | **266** |

In each row the displayed three integers sum to 0 modulo its indicated p. For p=373, the pre-division numerator W0−V_half+pK1S0 is 26434510 modulo 51895117 = 190·139129, and 190+290+266=746=2·373.

This is a finite verifier for the reduced theorem and the earlier p373 original W/V congruence, not proof of Theta_p=0 for arbitrary target primes.

## 4. BRC and future scientific action

Retained carrier: three **source-labelled** coordinates B_p, jet_p and grade2_p and the precise p²-divided second-digit observer; separate p-adic grades are not individually forced to vanish. The map (original p³ total)->(F_p triple) is proved well-defined under accepted first-digit divisibility and preserves the final zero test, with original signed weights and source equations preserved. This is a direct application of BRC information-preservation and coordinate recovery to the exact D25 certificate (REUSE_APPLIED).

Next decisive route is a finite-field/creative-telescoping cancellation across the **combined** triple (B_p, jet_p, grade2_p), aiming at an all-prime Theta_p=0 identity in both target classes. Direct single-grade annihilation is already refuted by the p373 value grade2_p=266.

Native benchmark #1559 still requires original p373 H0/B0 divided-power [X]U mod 139129 with real rank, semilinear Frobenius orientation/eta, signed kappa, Delta-R and independent reproducer. A native executor is unconfirmed; this proof is only author-side evidence. Historical Source Researcher EM-ENTERPRISE-4DEB43 is preserved as provenance, not claimed as an authenticated current session.

Status: AUTHOR_SIDE_EXACT_EQUIVALENCE / FINITE_18_PRIME_PROJECTION_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
