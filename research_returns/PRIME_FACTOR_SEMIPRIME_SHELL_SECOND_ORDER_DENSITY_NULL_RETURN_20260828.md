# Prime-Factor Semiprime Shell Second-Order Density/Covariance Null — Research Return

Status: `FROZEN_RETURN / NULL_MODEL_MISSPECIFICATION / NEW_HOLDOUTS_UNTOUCHED`

Date: `2026-08-28`

Researcher-ID: `EM-PFSS2-A927C4`

Task: `RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL`

Publication: `TP2-D44C166C4C87CEC167E7`

Execution: `ER-DC1E66CD6CE300BD1A65`

Claim: `chatgpt-pfss2-20260828-1305-a927c4`

## 1. Terminal disposition

`TERMINAL_CLASS = NULL_MODEL_MISSPECIFICATION`.

`REGISTERED_STATISTIC = UNDEFINED_UNDER_NULL_A`.

`SECOND_ORDER_RESIDUAL_CANDIDATE = NOT_EVALUABLE_AND_NOT_CLAIMED`.

`NEW_HOLDOUT_ACCESS = NONE`.

The task terminates at the discovery stage. The registered conditional microcell/wheel null overconditions the first three discovery scales so strongly that every relevant conditioned stratum is a singleton. Consequently the Null-A variance is exactly zero for every registered occupancy cell at those scales. The frozen statistic

\[
z_{X,\eta,b}=\frac{O_{X,\eta,b}-\mu_{X,\eta,b}}{\sigma_{X,\eta,b}}
\]

is therefore undefined for three of the five discovery scales, and the cross-scale statistic

\[
C_{\eta,b}=5^{-1/2}\sum_X z_{X,\eta,b}
\]

cannot be evaluated as registered.

No epsilon regularizer, cell dropping, scale dropping, or coarsening is introduced after seeing this failure. Those would be post-hoc changes prohibited by the taskbook.

## 2. Exact structural obstruction

Null A freezes the microcell label

\[
(k,j),\qquad
k=\lfloor\log_2 q\rfloor,\qquad
j=\left\lfloor
\frac{1024(q-2^k)}{2^k}
\right\rfloor,
\]

and also freezes `q mod 210`.

For `q<2^18`, one has `k<=17`. A fixed microcell then has diameter strictly less than

\[
\frac{2^k}{1024}\le 128<210.
\]

Two distinct integers in the same residue class modulo 210 differ by a nonzero multiple of 210. Hence a fixed `(k,j,q mod 210)` stratum contains at most one integer whenever `q<2^18`.

Therefore conditional resampling within such a stratum is the identity map.

Under the registered factor trim `p^4>X`, the largest relevant `q` in the discovery data is:

| X | max relevant q |
|---:|---:|
| 1,000,000 | 27,297 |
| 3,000,000 | 70,465 |
| 10,000,000 | 171,186 |
| 30,000,000 | 383,544 |
| 100,000,000 | 1,000,000 |

The first three are all below `262,144=2^18`. Thus Null A has exact zero variance at every registered `(eta,xi-bin)` feature for `X=10^6,3*10^6,10^7`.

This is an exact combinatorial obstruction, not a Monte-Carlo accident.

## 3. Exact Null-B contrast witness

Null B is not identically frozen on the same data.

At

- `X=1,000,000`,
- `eta=1/100`,
- zero-based `xi` bin `1`,
- band block indices `t in [128,130)`, corresponding to `q in [26,880,27,299]`,

the exact aggregate contribution of that band to the registered cell is:

- cyclic shift by zero 210-blocks: `25`;
- cyclic shift by one 210-block: `31`.

So the registered two null families have materially different support/covariance structure already at the first discovery scale: Null A is structurally degenerate, while Null B admits a nontrivial shift.

## 4. Exact discovery counts

Square pairs are excluded from the primary statistic as registered.

The exact primary semiprime-pair totals are:

| X | eta=1/100 | eta=3/1000 | eta=1/1000 |
|---:|---:|---:|---:|
| 1,000,000 | 683 | 203 | 69 |
| 3,000,000 | 2,125 | 628 | 209 |
| 10,000,000 | 6,519 | 1,948 | 659 |
| 30,000,000 | 18,133 | 5,409 | 1,804 |
| 100,000,000 | 58,530 | 17,462 | 5,818 |

These counts are discovery data only.

## 5. Frozen 4096-replicate diagnostics

Both registered null generators were executed for exactly 4,096 discovery replicates using the manifest seeds, then rerun deterministically a second time.

Array SHA-256:

- Null A: `adffaf6ee4e3098caf53d0ee2c3c63bcfb8dd1c218d654341a57c4794b5175a9`;
- Null B: `a2d3ef1315397c97c3dcc0ba3ef4aabec532dc307aecd6909d173cd312f86577`.

The second replay was bit-identical.

Number of nonzero-variance registered features by discovery scale:

| X | Null A | Null B |
|---:|---:|---:|
| 1,000,000 | 0 | 3 |
| 3,000,000 | 0 | 29 |
| 10,000,000 | 0 | 50 |
| 30,000,000 | 12 | 65 |
| 100,000,000 | 33 | 78 |

Number of `(eta,bin)` cells with nonzero variance at all five discovery scales:

- Null A: `0`;
- Null B: `3`.

Thus no registered cross-scale `C_{eta,b}` exists under Null A.

## 6. Holdout firewall

The new holdouts

\[
X=3\cdot10^8,\qquad X=10^9
\]

were not enumerated, queried, or used in any statistic.

They remain untouched and may be reused only by a separately published corrected generation whose nuisance-conditioning rule is frozen before access.

## 7. Parent-result authority

The parent result `RR-3287C6124F8D8A1F0901` was still awaiting Driver review at task start.

No parent empirical interpretation was used as Working Truth. The present terminal result depends only on:

1. this task's registered null definitions;
2. exact integer discovery enumeration;
3. the exact microcell/residue capacity argument;
4. the deterministic Null-B contrast witness and replay diagnostics.

## 8. Hard-target disposition

Hard target:

`SEMIPRIME_FACTOR_SHELL_SECOND_ORDER_NULL_SURVIVOR_CLASSIFIED`.

Disposition:

`NULL_MODEL_MISSPECIFICATION`.

This does **not** show that a second-order arithmetic residual exists or does not exist. It shows that the present registered Null-A conditioning makes the proposed second-order test non-identifiable at three discovery scales.

The smallest legitimate next frontier is to publish a corrected null generation with a predeclared minimum conditional-support / positive-variance rule. Candidate repairs include coarser q microcells or an adaptive support floor, but no repair is selected inside this task.

## 9. Reproducibility

Artifacts:

- `research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_SECOND_ORDER_DENSITY_NULL/experiment_manifest.json`;
- `research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_SECOND_ORDER_DENSITY_NULL/result_summary.json`;
- `scripts/check_prime_factor_semiprime_shell_second_order_density_null.py`.

Checker:

```bash
python scripts/check_prime_factor_semiprime_shell_second_order_density_null.py
```

proves the structural obstruction and exact Null-B witness without holdout access.

When `numpy` and `numba` are available,

```bash
python scripts/check_prime_factor_semiprime_shell_second_order_density_null.py --full
```

also regenerates the 4,096-replicate discovery arrays and checks their frozen SHA-256 values.

## 10. Final freeze

`NULL_A_FIRST_THREE_DISCOVERY_SCALES = EXACT_ZERO_VARIANCE`.

`REGISTERED_CROSS_SCALE_STATISTIC = UNDEFINED`.

`HOLDOUTS_3E8_AND_1E9 = UNTOUCHED`.

`RESULT = NULL_MODEL_MISSPECIFICATION`.

`UNRESOLVED_RESIDUE = CORRECTED_POSITIVE_SUPPORT_NULL_REQUIRES_NEW_PUBLICATION`.
