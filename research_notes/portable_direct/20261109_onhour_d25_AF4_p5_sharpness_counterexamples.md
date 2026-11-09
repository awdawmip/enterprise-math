# D25 AF4: fifth-digit sharpness on both frozen residue classes

Date: 2026-11-09. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance. Author-side arithmetic / exact counterexample / bounded experiment, **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

## The original signed full-cutoff quantities

For primes p>3 set
[
A_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\quad
C_n=\frac{\binom{4n}{2n}\binom{2n}{n}^2}{2304^n},
]
[
W_p=\sum_{n=0}^{p-1}(6n+1)A_n,\quad
V_p=\sum_{n=0}^{p-1}(8n+1)C_n,\quad
E_p=W_p-2V_p+p\left(\frac{-3}{p}\right).
]
Prior author-side AF4 conjecture is `E_p=0 mod p^4`. Define the fifth-digit residual only when E_p is divisible by p^4:
[
q_p=(E_p/p^4)\bmod p\in\mathbf F_p.
]
Thus a proposed universal improvement to modulo p^5 would require q_p=0 for every target p.

## Exact counterexamples, one in each frozen residue class

The original binomial sums, evaluated modulo p^5 with complete original cutoffs, give:

| p | residue mod 24 | p^5 | W_p mod p^5 | V_p mod p^5 | chi=(-3/p) | E_p mod p^5 | q_p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 371293 | 276835 | 195546 | +1 | 257049 = 9*13^4 | 9 |
| 19 | 19 | 2476099 | 603611 | 1865667 | +1 | 1824494 = 14*19^4 | 14 |
| 373 | 13 | 7220115733093 | 2934720761840 | 3393369805886 | +1 | 3368096883534 = 174*373^4 | 174 |

All integers in the table are exact residues, not floating approximations. For p=13 and p=19 the nonzero q_p provides **two strict counterexamples** to `E_p=0 mod p^5`, covering both frozen classes. Consequently the modulus p^4 in AF4, if proved, is sharp as a **uniform** claim separately on each of these two residue classes. No claim is made that every prime has exact valuation 4.

## Independent exact arithmetic and observer/operation provenance

Program: `research_notes/portable_direct/d25_AF4_p5_sharpness_20261109.py`.

Path A evaluates the original hypergeometric factorial ratio recursively in Z/p^5Z:
[
A_{n+1}/A_n=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3},\qquad
C_{n+1}/C_n=\frac{(4n+1)(4n+3)(2n+1)}{288(n+1)^3}.
]
The recurrences follow exactly from the original factorial definitions; n+1<p and p>3 ensure unit denominators. Path B evaluates the independent **unbounded integer** binomial numerators term-by-term, multiplying by inverse powers of 216 and 2304 modulo p^5. Paths A/B coincide for p=5,7,13,19,37,43,73,373 (complete W/V/chi/E, not merely quotient).

A fresh bounded scan tested **all 548 primes in 5<=p<=4000**. All 548 have E_p=0 mod p^4 by exact calculation. Exactly two have q_p=0 within this finite window: p=5 and 7. The frozen 13/19 mod24 classes contain **139** tested primes, all with q_p nonzero. Finite observation only; the two exact p=13/19 counterexamples already suffice to refute uniform p^5 strengthening.

BRC-style residual typing retains the original full weighted coefficient provenance and the noncollapsed tuple `(p, p mod24, chi, v_p(E_p) at bounded precision, q_p mod p, method)`. The fifth-digit quotient cannot be inferred from the previously computed AF4 zero alone.

## Consequence for the live mother objective

The frozen mother objective remains `Delta_p-R_p=0 mod p` for p=13,19 mod24, equivalent at its established source interface to original full `W216-V2304=0 mod p^3`. AF4 modulo p^4 is still unproved, and its next **load-bearing** proof unit remains:
[
E_{<=2,p}/p^3+L_p=0\pmod p,
]
preserving original weights, grade-zero through grade-three contributions and the real cutoff.

The completed p^5 falsification prevents the stronger fifth-digit target from silently becoming an AF4 prerequisite. Next try a finite WZ/Fricke or explicit boundary-transfer certificate on the p^4 expression, starting with exact p=13,19,373 residues and retaining the two source observables. The native p=373 H0/B0 `[X]U mod139129`, rank, normalization, signed kappa and independent validation remain separately unexecuted (#1559); this author-side computation is not that benchmark. Source recovery of historical Researcher `EM-ENTERPRISE-4DEB43` returned `SESSION_CAPABILITY_REQUIRED`, so no live CLAIM/run or native checkpoint is asserted.
