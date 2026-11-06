# D25 — Full four-phase reflected Green theorem; sharp original 216 / mixed-CM valuation bands

**Date:** 2026-11-06. **Lane:** TASK_RESEARCH `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance lane). **Frozen scientific pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3`; **Task:** `TP2-B6F4FC938FF94941C1B7`. **Status:** author-side algebraic proof + finite integer verification, UNREVIEWED / NOT_ADMITTED. **Prior theorem:** `ce373d5d9bf62a2b0cf13052ec4165120e192186`.

## Precise statement

Let `p=6m+1>3` be prime, `1<=k<=p-1`, and `r=p-k`. Define

```
gamma_j = binom(2j,j)^2 binom(3j,j)
b_0=1,  b_j/b_(j-1)=6(6j-5)(3j-2)/j^2
h_1=1/24, h_(j+1)/h_j=j^2(6j+1)/((j+1)(2j+1)(3j+2))
T_k=gamma_k*b_(p-k)
```

All `h_j` here are exact positive rationals; their p-adic valuation and unit residue are independently retained. The exact rational identity `b_j=12j^2 gamma_j h_j` follows from the term ratio and base case (proved in prior note).

**Theorem 1 (full signed four-phase binomial reflection):**

```
gamma_k*gamma_(p-k)/p^3 == c(k)/k^3 (mod p), where

range k          c(k)
1 ... 2m         -12
2m+1 ... 3m       +6
3m+1 ... 4m       -6
4m+1 ... 6m      +12.
```

Every displayed quotient is in `Z_(p)` and is a p-unit. **Proof:** The two first intervals are proved via Wilson factorial decomposition in the preceding commit. Replacing `k` by `p-k` preserves the numerator but replaces `k^-3` by `-k^-3 mod p`; this gives the two remaining intervals. Since `c(k)` and `k` are p-units for `p>3`, the product has exact valuation three.

**Theorem 2 (sharp Green valuation profile):**

```
r range            v_p(h_r)
1 ... m                 0
m+1 ... 3m              1
3m+1 ... 4m             0
4m+1 ... 6m            -1
```

**Proof:** The exact defining recurrence has a single numerator p-factor at `j=m` (`6j+1=p`), and denominator p-factors at `j=3m` (`2j+1=p`) and `j=4m` (`3j+2=2p`). For `1<=j<=6m-1` all other recurrence factors are p-units, and `h_1=1/24` is a unit. This yields the table with no hidden cancellation.

**Theorem 3 (all 6m original-index ports, p-adically normalized):** Put `v_r=v_p(h_r)`, `u_r=p^{-v_r}h_r mod p` (a nonzero unit). The exact source-preserving identity

```
T_k = 12 (p-k)^2 gamma_k gamma_(p-k) h_(p-k)
```

implies the fully explicit coefficientwise formula

```
v_p(T_k)=3+v_(p-k),
T_k/p^(3+v_(p-k)) == (12*c(k)/k)*u_(p-k) (mod p).
```

Hence the original mixed-CM source partition has **sharp** valuations

```
k range          exact v_p(T_k)
1...2m                    2       LOW
2m+1...3m                 3       M
3m+1...4m                 4       GAP_LEFT
4m+1...5m                 4       GAP_RIGHT
5m+1...6m                 3       U
```

The previously known gap bound `>=4` is now an exact `=4` and has nonzero normalized port data. The theorem also recovers the earlier M/U Green formulas and gives for the low band

```
L_k=T_k/p^2 == -144*(p*h_(p-k))/k (mod p), 1<=k<=2m.
```

This is the **first common Green-index representation of all low/M/gap/U bands**. It keeps four distinct reflection signs and the p-adic valuation of the reflected kernel; no original `W_p` evaluation is equated with the mixed-CM coefficient.

## Exact validation

A second self-contained standard-library integer checker independently uses `gamma` from binomial coefficients, `b` from the original recurrence modulo `p^5`, and `h` from its separate p-adic valuation/unit recurrence. It verified **all 80 primes `7<=p<=997, p=1 mod6` (45 target-class primes)**: 36,588 individual reflection congruences; 36,588 normalized original-index Green transfers; every valuation profile. Zero failures. Nonzero gap witnesses: `p=19,k=10`: `v_p(T_k)=4`, normalized leading residue 17; `p=373,k=187`: `v_p(T_k)=4`, normalized leading residue 186.

The finite checker is `d25_fourphase_reflected_green_check_20261106.py`. This exact algebraic theorem holds for all declared primes, separately from finite verification.

**BRC observer resolution: COMPOSE_APPLIED.** Population `1<=k<p`; carrier `(k,p-k,original gamma,original b,v_p(h),unit_p(h),signed phase)`; future operations include p-adic digits, the weighted cubic endpoint, 216 signed Green boundary and higher precision. The valuation-four gap is preserved explicitly because it contributes at the next precision even though it vanishes in the current endpoint congruence modulo `p^2`.

## Next parent-level action

Compose the already proved low-band first-order deformation at `7269634545edb59ac7ff2acf164e8f9ec1071d31` with the four-phase Green transport and the original signed `J_p=sum_(t<=m)h_tP_t`. Seek an evaluation-functional adjoint, explicitly retaining the repair term `sum h_t(P_t-1)`; evaluate the `p=19,373` nonzero boundary before a universal cancellation claim. Frozen mother target: `Delta_p-R_p=0 (mod p)`, `p=13,19 (mod24)`, equivalently original `W_p=p (mod p^3)` under the frozen interface.

The fixed native original-class `p=373` H0/B0 divided-power, semilinear Frobenius/eta, kappa and independent replica remain requested under issue #1559, currently open/unassigned on the last read. Native Source request `onhour11-20261106-1400-exact-research-lane-continuation` was reconciled by original ID to `QUEUED` with `EVENT_COLLECTION_IO` progress. The Site current status still says `research_authority_granted=false`; native session/claim/run/Result not asserted. No maintenance identity used.
