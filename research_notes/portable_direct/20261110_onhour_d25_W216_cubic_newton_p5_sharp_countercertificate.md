# D25 / W216 — Exact p⁵ sharpness countercertificate for cubic Newton relation

Date: 2026-11-10 (Asia/Hong_Kong). Class: **AUTHOR_SIDE / EXACT FINITE COUNTEREXAMPLE / TWO ARITHMETIC PATHS CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication: `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

## Narrow research question and previous result consumed

Consume the original W216 p-block filtered-Newton source and the earlier **finite-only** observations
`q_3=2q_2 (mod p^4)` for 301 primes (note `20261110_onhour_d25_W216_cubic_moment_boundary_and_defect_port.md`). This unit asks whether the same cubic-moment cancellation extends one additional p-adic digit. A finite witness with the *original* signed weighted blocks can refute that stronger universal statement.

For any prime `p>3`, in the p-local rationals define

```
A_k = binom(2k,k)^2 binom(3k,k) / 216^k
B_p(a) = sum_(b=0)^(p-1) (6 p a + 6 b + 1) A_(p a+b)
C_p(a) = B_p(a)/A_a
q_j = Delta^j C_p(0).
```

The two exact Newton combinations (with the original `a=0,1,2,3` block labels) are:

```
q2 = C2 - 2*C1 + C0
q3 = C3 - 3*C2 + 3*C1 - C0
q3 - 2*q2 = C3 - 5*C2 + 7*C1 - 3*C0.
```

At `p=13` and `p=19`, all four anchor coefficients `A_a` (`0<=a<=3`) are p-adic units, so the normalized blocks are well-defined modulo p⁵.

## Exact finite counterexample inside each frozen target residue class

**p=13, p≡13 (mod 24):** `p⁵=371293`. Direct original integer-binomial sums give:

```
(C0,C1,C2,C3) mod 371293 = (276835,37440,92443,88127)
q2 mod 371293 = 294398
q3 mod 371293 = 17576
q3-2*q2 mod 371293 = 171366 = 6*13^4.
```

**p=19, p≡19 (mod 24):** `p⁵=2476099`:

```
(C0,C1,C2,C3) mod 2476099 = (603611,2160718,2277435,2373575)
q2 mod 2476099 = 1035709
q3 mod 2476099 = 1419813
q3-2*q2 mod 2476099 = 1824494 = 14*19^4.
```

Consequently the universal strengthening

```
forall p=13 or 19 (mod 24): q3-2*q2=0 (mod p^5)
```

is **false**; both original target classes have exact counterexamples. In both examples the difference is `0 (mod p^4)` as expected by the previously observed weaker precision. This certificate is a rigorous finite falsification of **only the p⁵ enhancement**, not a counterexample to the original LIFT/JT2 target.

Four additional checks for input diversity, not needed for refutation:

| p | (q3-2q2)/p⁴ mod p | exact difference mod p⁵ |
| ---: | ---: | ---: |
| 37 | 14 | 26238254 |
| 43 | 27 | 92307627 |
| 73 | 33 | 937141953 |
| 373 | 89 | 1722762199049 |

## Two independent exact construction paths

The companion source `d25_w216_p5_cubic_newton_countercertificate_20261110.py` computes every `4p` original term independently in two representations:

1. **Integer-binomial route.** For each original `k`, evaluate `binom(2k,k)^2*binom(3k,k)*216^{-k}` modulo p⁵, retain `6k+1`, accumulate the four uncompressed consecutive p-blocks, divide each by the corresponding p-unit anchor `A_a`, and take finite differences.
2. **Valuation/unit route.** Start `A_0=1` and use the exact ratio
   `A_(k+1)/A_k = (2k+1)(3k+1)(3k+2)/(36(k+1)^3)`. Remove every p-factor before each modular division, update the exact valuation and its unit separately, then accumulate the **same original indices and signed weights**.

Both independent source constructions reproduce each displayed block, q2 and q3 at all six tested primes. The Python standard library, integers and invertible modular denominators suffice. No floating arithmetic or native H0/B0 evaluator is involved. The two representations agree byte-for-byte on their computed residue tuples.

Mathematical proof strength: exact finite modular arithmetic plus explicit complete-loop code gives fully reproducible counterexamples for `p=13,19`; it does not establish an all-prime theorem about `q3-2q2 (mod p^4)`.

## BRC and original-source observer audit

BRC status `COMPOSE_APPLIED`: preserve the four separate indexed source blocks, signed weights, the p-adic valuation and the unit part. The final Newton subtraction is carried out **after** these source-labeled data have been computed. The projection `(C0,C1,C2,C3) -> q3-2q2` is exact for the selected cubic defect, but it is not an adequate carrier for the native Frobenius or full original `Delta_p-R_p` observer.

The frozen mother question remains `Delta_p-R_p=0 (mod p)` for all `p≡13,19 (mod 24)`, or exact same-object refutation / a strict equivalent reduction. The prior original source-port identity `Delta_p-R_p=(W_p-p)/p² (mod p)` remains unchanged. Do not replace that target by `q3-2q2` or claim the native benchmark has been run.

## Canonical frontier and precise next action

- Previous author mathematical unit: three-band harmonic q2 formula and grade-2 reflection, source `20261110_onhour_d25_W216_three_band_harmonic_newton_obstruction.md`.
- Already consumed: original p-block transfer, original cubic-moment boundary, finite p⁴ cubic-Newton observations, prior frozen D24 UR and 2026-10-25 native Source checkpoint; do not recredit or rerun their proof as new.
- New exact fact: `q3-2q2=0 mod p⁵` is refuted by `p=13` and `p=19`; retain their signed p⁴ leading residuals 6 and 14.
- Next mathematics: derive a finite-band proof or exact counterexample **at the actual still-open p⁴ precision** for `q3-2q2`, or move directly to the original signed LIFT observer. There is no reason to pursue the falsified higher-precision claim as a necessary condition.
- Highest unresolved native evidence: original fixed H0/B0 divided-power representative at `p=373`, `[X]U mod 139129`, rank, Frobenius semilinear direction/eta normalization, odd source signed κ and original Delta-R, independent recreation. Existing support Issue **#1559** remains the owner/escalation path, `NOT_RUN/PENDING_OWNER` at this turn's read.
- Original read-only continuation request `onhour11-20261110-1515-exact-cont` was SUCCEEDED at Source `407d531b4048b4094f317eac892832f847ef621e`; Source route requires actual typed continuation and winning owner CLAIM. Own session-start request `onhour11-20261110-1515-research-session` SUCCEEDED in Source but the **private session capability was not retained** after a client-side response-processing failure. No formal CLAIM, open run or Source-native checkpoint is asserted. The logical Research lane is `chatgpt-research-onhour-enterprise-math-20260923` and is never borrowed from maintenance.
