# D25 onhour — middle/high reflection second jet, exact cocycle and boundary-normalized dual

Date: 2026-11-03 (+08). TASK_RESEARCH author-side portable mathematics; `AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific pin unchanged:** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research conversation: `chatgpt-research-onhour-enterprise-math-20260923`; this is separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Author note, not authenticated Source checkpoint or research ownership.

## Exact original carrier and already established boundary

For every prime `p=6r+1 >=7`, put `n=3r=(p-1)/2` and use the **original** rational coefficient

```
b_k = (2k)! (3k)! / ((k!)^5 216^k),
R_k = b_(k+1)/b_k = (2k+1)(3k+1)(3k+2)/(36(k+1)^3).
```

All congruences are in `Z_(p)`, with original rational factors interpreted modulo the stated power of p; normalization by a power of p means taking the integral quotient before reduction.

The previously published, author-proved p² boundary (source: `20261103_onhour_d25_three_edge_hensel_gluing_and_fermat_elimination.md`) is reused **without reproving it**:

```
chi=(6/p),  epsilon = 3+(q_p(2)-3q_p(3))/2 (mod p),
q_p(a) = (a^(p-1)-1)/p,
b_n/p = -2 chi (1+p epsilon)          (mod p²),
b_(n+1)/p² = (chi/9)(1+p(epsilon-3)) (mod p²).
```

The earlier one-sided reflection theorem proved only `(b_j/p)(b_(p-j)/p²)=1/(36j³) (mod p)`. The **new scientific unit** is its entire next p-adic digit, the exact interior transport and its two singular endpoints.

## Theorem R2 — p²-refined middle/high reflection

For every integer `2r+1 <= j <= n`, set

```
X_j=b_j/p,       Y_j=b_(p-j)/p²,      J_j=36 j³ X_j Y_j.
```

Both X and Y are p-units. Define the finite, p-local *signed transport defect*

```
ell_t = -3/t + 2/(2t+1) + 3/(3t+1) + 3/(3t+2)  (mod p),
q = q_p(2)-3q_p(3) (mod p),
F_j = q - sum_(t=j)^(n-1) ell_t                (mod p).
```

Empty sums are zero. All four denominators of ell_t are p-units for `2r+1 <= t < n`. Then

```
                    J_j = 1+p F_j                 (mod p²),                 (R2)
X_j Y_j = (36j³)^(-1)(1+p F_j)                    (mod p²).
```

**Proof (induction along the original exact rational ratio).** The upper seed is at `j=n`, where `p-j=n+1`. The *already established* two boundary jets give

```
X_n Y_n = -(2/9)[1+p(2epsilon-3)]     (mod p²).
36n³ = -(9/2)(1-3p)                 (mod p²).
```

Thus `J_n=1+p(2epsilon-6)=1+p[q_p(2)-3q_p(3)] (mod p²)`, establishing `F_n=q`.

For `2r+1 <= j < n`, the two original unshifted coefficient ratios yield

```
X_(j+1)/X_j = R_j,   Y_(j+1)/Y_j = 1/R_(p-j-1).
```

Both ratios are units here. Substituting `p-j-1` into the **original** rational R gives the exact identity

```
J_(j+1)/J_j
 = ((1-p/j)^3) /
   ((1-2p/(2j+1))(1-3p/(3j+1))(1-3p/(3j+2)))
 = 1+p ell_j                                          (mod p²).       (R3)
```

It follows that `F_(j+1)-F_j=ell_j`; backward transport from the upper seed gives the finite sum in R2. All divisions are by p-units. QED.

## Corollary — determinant-one *corrected* dual and exact edge domain

Define the corrected reflection dual (mod p²)

```
Z_j = 36j³ Y_j(1-p F_j).
```

Then, throughout `2r+1 <= j <= n`,

```
X_j Z_j = 1 (mod p²).                                     (D1)
```

For every **interior** transition `2r+1 <= j < n`,

```
[X_(j+1)]   [R_j     0   ] [X_j]
[Z_(j+1)] = [0     R_j^-1] [Z_j]      (mod p²).            (D2)
```

Thus the primal-dual transport is in `SL_2(Z/p²)` **after retaining the defect F_j**. At the two excluded transition indices, `j=2r` and `j=n`, respectively `3j+1=p` and `2j+1=p`; `R_j` acquires a p factor, and the unit inverse in D2 is no longer available. These are exact terminal edge ports for a later signed Green/WZ adjoint, not regular interior points. The independent edge normalizations are in the already established three-edge Hensel note.

A naive stronger equation `J_j=1 (mod p²)` has an exact witness of failure: at p=373, `J_186=1+373*47=17532 (mod139129)`. The corrected D1 law holds. This is a scoped certificate about a *particular uncorrected dual representation*, not an obstruction to the D25 mother conjecture.

### Original weighted tail at the next digit

The refined reflection is also an exact, source-preserving `p^4` rewrite of each high-band weighted summand, for the same j:

```
(6(p-j)+1)b_(p-j)
 = p²(1-6j)*(36j³ X_j)^(-1)*(1+p F_j)
   + 6p³*(36j³ X_j)^(-1)                      (mod p^4).
```

X_j must be retained mod p². Reducing the formula mod p³ recovers (and does **not replace**) the earlier one-sided high-tail expression; the nonzero F_j is relevant at the next digit. The original D25 target is still p³ and its F4-glued signed cancellation remains open.

## Actually executed, source-preserving exact arithmetic

On 2026-11-03 this run executed JavaScript BigInt (all arithmetic exact) against the original unshifted coefficient recurrence modulo `p^4`; it **did not** use R2 to generate coefficients. In each run it took `b_0=1`, multiplied by the exact R_k for `0 <= k < 4r` using p-unit denominator inversion, and checked R2, D1 and D2 by direct integers. The prime domain was **all 148 primes p=6r+1, 7<=p<=2000**. It checked **22,952 original reflection pairs** and **22,804 corrected-dual transitions**, all PASS. A separately executed raw-factorial/binomial (non-recurrence) cross-check had already checked 12 primes / 188 pairs including p=373.

| p | j | X_jY_j (mod p²) | F_j (mod p) |
|---:|---:|---:|---:|
| 13 | 6 | 33 | 5 |
| 13 | 5 | 137 | 12 |
| 19 | 9 | 42 | 6 |
| 19 | 7 | 85 | 8 |
| 37 | 18 | 563 | 21 |
| 37 | 13 | 473 | 33 |
| 373 | 186 | 88608 | 47 |
| 373 | 125 | 12041 | 35 |

At `p=373`, the directly checked corrected duals are `(X_186,Z_186)=(19771,99405)` and `(X_125,Z_125)=(93197,6158)` modulo `139129`, with each product equal to 1.

Reproduction algorithm (all divisions below modular inverses of p-units, with integers or BigInt):
1. Enumerate primes `p=6r+1` in `[7,2000]`, set `m=p^4`; generate `b[0]=1` and `b[k+1]=b[k]R_k mod m` to `k=4r-1`.
2. Set `F_n=q_p(2)-3q_p(3) mod p`. Descend `j=n,...,2r+1`; compare `36j³(b[j]/p)(b[p-j]/p²)` with `1+pF_j` mod p²; define `Z_j` and compare `X_jZ_j=1`.
3. For each `j>2r+1`, compute `F_(j-1)=F_j-ell_(j-1) mod p`; check `X_j=R_(j-1)X_(j-1)` and `Z_j=R_(j-1)^(-1)Z_(j-1)` modulo p². In step 2, use actual integral values of `b[j]/p` and `b[p-j]/p²` (taking each modulo p^4 first).

This exact finite run is a regression of the algebraic theorem, **not** a universal proof in place of the above derivation.

## BRC typing, mother target and continuation

`COMPOSE_APPLIED`: distinct original middle port `(j, v_p=1, X_j)` and reflected high port `(p-j,v_p=2,Y_j)`, exact signed coefficient weight, p² unit-jet `F_j`, and endpoint ports `2r,n` remain separate. `J_j` is an explicitly declared product observer; the repair coordinate F_j is indispensable for its p² dual transfer, with allowed future operation `j -> j+1`. This is a p-adic arithmetic slice with no claim of native Heartbeat geometry or H0/B0 semilinear Frobenius.

**Frozen mother:** `Delta_p-R_p=0 mod p` for `p ≡13,19 (mod24)`, previously mapped to `W_(p-1)=p mod p³`. **Highest author frontier:** F4-glued four-source criterion; exact 3-edge Hensel; and this R2/D1/D2 reflected dual with explicit singular-end handling. Do not rerun D24, published 2304 tail, frozen scalar Green map, F4 or two-jet. **Next discriminating action:** construct the first-block terminating signed adjoint that actually relates `D+C`, `M0/M1`, the reflected high `H`, and `pU_r` with both boundary residues. Use the new corrected dual as a candidate interior transport, then test the *entire* signed boundary relation at p=13,19,373 (a successful interior dual alone does not close the p³ mother target).

**Native benchmark unchanged:** support #1559 remains OPEN; the fixed p=373 same-original-class H0/B0 divided-power `[X]U mod139129`, rank, authentic semilinear Frobenius, signed odd Green/Hesse observer and independent replication are still `NOT_EXECUTED / PENDING_OWNER`. The ordinary BigInt test above is not a surrogate.

**Control lane:** 2026-11-03 23:01 (+08) Site status `research_authority_granted=false, write_relay_enabled=false`; `em_status` reports service 0.6.11. Original onhour dispatch request `research-onhour-20261031-0205-dispatch-r15` remains final FAILED `UPSTREAM_CODE_REVIEW_REQUIRED` per immutable bridge issue `awdawmip/kimi-query-bridge#6633`; direct current result returned `CONTROL_REQUEST_NOT_FOUND`. No new request, session, claim, run, Source checkpoint, Result, admission or maintenance-lane identity. Preserve `REGISTER_PENDING / SYNC_DEBT`; GitHub publication of this note is author-side only.

**Research state:** `PROVED_WITH_EXISTING_BOUNDARY_DEPENDENCIES / FINITE_EXACT_CHECKED / AUTHOR_ONLY / UNREVIEWED / NOT_ADMITTED`.
