# JT2 UR — exact finite norm–jet sweep on all 575 admissible primes up to 20,000

Date: 2026-11-16. Scientific status: **EXACT FINITE COMPUTATION / AUTHOR-SIDE REPRODUCIBLE EVIDENCE**. Original UR reduction and the full target belong to `EM-JT2-EF9380`; the original limited-stage review belongs to `EM-DVR-57CCCE`. This expanded scan is a source-exposed Driver `EM-DVR-DEBB5E` finite audit, not an independent current Native Result review.

## Fixed model and arithmetic

For prime `p > 3`, `p mod 24 in {13,19}`, set `n=(p-1)/3=2m`, `P_n(X)=Q_m(X^2)` (ordinary Legendre, `P_n(1)=1`). Define `J_m(Y)=sum_r ([Y^r] Q_m(Y)^2)*Y^r/(2r+1)`. At the frozen rational port `Y=1/2`, compute

```
CM0 = Q_m(1/2) mod p
u = Q_m(1/2) / p mod p       [only after CM0=0]
d = Q_m'(1/2) mod p
J = J_m(1/2) mod p
epsilon = (18*u*d - 2*J - 3) mod p
```

All arithmetic is exact in `Z/(p^2)` or `F_p`. The polynomial coefficients are calculated using

```
[Y^j]Q_m = (-1)^(m-j) (2m+2j)! /
            (2^(2m) (m-j)! (m+j)! (2j)!),  0<=j<=m.
```

Every factorial index is at most `4m=2n<p`; each `2r+1` in `J` is at most `4m+1<p`. Thus all listed modular divisions are by units. The C++ program enumerates the entire declared finite prime domain, reduces the coefficient formula modulo `p^2`, squares `Q_m` coefficientwise modulo `p`, and evaluates the displayed residue. It checks CM0 rather than assuming it.

## Exact computation, output and independent check

Run on Debian with `g++ (Debian 14.2.0-19) 14.2.0`:

```sh
g++ -O3 -std=c++17 experiments/jt2_ur_norm_jet_exact_scan_to_20000_20261116.cpp -o /tmp/jt2_ur_scan
/tmp/jt2_ur_scan 20000 > /tmp/jt2_ur_20000.csv
```

Observed terminal summary:

```
SUMMARY hi=20000 total=575 cm0=575 cmfails=0 e_nonzero=0
```

These are **575 exact finite cases** in the stated domain; the previously saved 45 primes `p<=997` are included, and **530 additional primes** `997<p<=20000` were checked. In all 575, `Q_m(1/2)=0 mod p` and `epsilon_p=0 mod p`. Sample CSV records `(p,m,CM0,J,u,d,epsilon)`:

```
(13,2,0,0,2,12,0)
(19,3,0,12,4,17,0)
(397,66,0,65,102,127,0)
(997,166,0,609,473,460,0)
(3019,503,0,952,306,754,0)
(10093,1682,0,2563,2675,1624,0)
(19963,3327,0,19482,16609,6367,0)
```

For `p=13,19,43,109,163,397,733,997,3019,10093`, a separate Python implementation built `P_n(X)` by the **three-term Legendre polynomial recurrence** rather than the factorial formula; its `Q_m`, convolution, `J_m`, `u`, and `epsilon` outputs matched the C++ calculation. This avoids relying on the same coefficient-construction algorithm for the cross-check.

The run produced 575 data rows plus one header (16,433 UTF-8 bytes in the local full CSV). The submitted C++ program regenerates every row without an external dependency or floating-point arithmetic.

## Scientific contribution and next discriminating step

This extends the exact observation window, supporting the conjectured fixed-port `epsilon_p=0` without changing its logical status: the uniform congruence for **every** admissible prime remains the open UR task. The earlier Driver proof of automatic SIMPLE and the unique balanced p-adic Hensel root is available at `research_notes/driver/2026-11-16_jt2_ur_legendre_automatic_simple_all_order_balanced_hensel.md`. An all-prime proof must still establish that the fixed rational port `1/2` coincides modulo `p^2` with that balanced root.

Primary frozen source: `research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md` at `969846f1d451b3e086f34a19b217e333c8a90c8d`; original accepted limited norm-jet stage review: `driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md`. Earlier 45-prime audit: `research_notes/driver/2026-11-16_jt2_ur_eps_norm_jet_exact_45_prime_audit.md` at `4f4ad7227b6003e00b835ab5802c20c6a9edf67e`.

New experimental source: `experiments/jt2_ur_norm_jet_exact_scan_to_20000_20261116.cpp` at `972772b1a9782035c26e19e9f1a28460c66371ab`, Git blob `d1713a41eacaf4a989958c9d2a7c6f66beae9679`. No Native Result admission or task closure is asserted.