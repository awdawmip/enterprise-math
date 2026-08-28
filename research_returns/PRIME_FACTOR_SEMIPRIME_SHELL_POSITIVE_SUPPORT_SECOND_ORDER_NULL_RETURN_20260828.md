# Prime-Factor Semiprime Shell Positive-Support Second-Order Null — Research Return

Status: `FROZEN_RETURN / SECOND_ORDER_DENSITY_ARTIFACT / HOLDOUTS_UNTOUCHED`

Date: `2026-08-28`

Researcher-ID: `EM-PFSS2R-C60E73`

Task: `RS-PRIME-FACTOR-SEMIPRIME-SHELL-POSITIVE-SUPPORT-SECOND-ORDER-NULL`

Publication: `TP2-D8A51502065004783B7B`

Execution: `ER-BED2B498BDA67D045479`

Claim: `chatgpt-pfss2r-20260828-1340-c60e73`

## 1. Terminal disposition

`TERMINAL_CLASS = SECOND_ORDER_DENSITY_ARTIFACT`.

`ELIGIBLE_DISCOVERY_CELLS = 60`.

`CELLS_CLEARING_BOTH_99_PERCENT_FAMILYWISE_GATES = 0`.

`SECOND_ORDER_RESIDUAL_CANDIDATE = NONE`.

`NEW_HOLDOUT_ACCESS = NONE`.

After repairing the prior singleton-stratum degeneracy with an exact positive-support rule, both corrected null families have positive empirical variance on every feature admitted to the cross-scale test. The corrected test is therefore identifiable.

The result is negative: no pre-eligible discovery feature reaches the 99% family-wise threshold under both corrected null families. Under the registered rule the task terminates at discovery and the untouched holdouts are not spent.

## 2. Exact positive-support freeze

The corrected generation freezes the same factor-shell observable, factor trim, 32-bin density-flattened coordinate, and square exclusion.

Corrected Null A uses full wheel-block cells with

\[
s_A(k)=2^{\max(3,k-10)}
\]

complete 210-blocks, with exact prime count preserved independently in every residue class modulo 210.

Corrected Null B uses full wheel-gap bands with

\[
s_B(k)=2^{\max(4,k-6)}
\]

complete 210-blocks and cyclically translates the observed prime indicator by whole 210-blocks.

Before any corrected residual z-score was inspected, exact support was computed from the null geometry and feature-weight function. The number of supported registered features at each discovery scale was

| \(X\) | Null A | Null B |
|---:|---:|---:|
| \(10^6\) | 78 | 60 |
| \(3\cdot10^6\) | 96 | 81 |
| \(10^7\) | 96 | 96 |
| \(3\cdot10^7\) | 96 | 96 |
| \(10^8\) | 96 | 96 |

The exact all-five-scale intersection contains 60 \((\eta,b)\) cells. For each of the three shell widths, the eligible zero-based bins are

\[
\{1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21\}.
\]

The eligible set is frozen in

`research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_POSITIVE_SUPPORT_SECOND_ORDER_NULL/support_freeze.json`.

## 3. Exact discovery counts

The primary semiprime factor-pair totals, after the registered \(p^4>X\) trim and square exclusion, are:

| \(X\) | \(\eta=1/100\) | \(\eta=3/1000\) | \(\eta=1/1000\) |
|---:|---:|---:|---:|
| \(10^6\) | 683 | 203 | 69 |
| \(3\cdot10^6\) | 2,125 | 628 | 209 |
| \(10^7\) | 6,519 | 1,948 | 659 |
| \(3\cdot10^7\) | 18,133 | 5,409 | 1,804 |
| \(10^8\) | 58,530 | 17,462 | 5,818 |

These are discovery data only.

## 4. 4096-replicate corrected null results

Both corrected null families were run for exactly 4,096 discovery replicates using the pre-frozen seeds. Every one of the 60 eligible cells had strictly positive empirical standard deviation under both null families.

Deterministic array SHA-256 values:

- corrected Null A: `c1c67979aa5d5c23dfaecafa92e788579513f244301cc0a02c9b159dc1cae610`;
- corrected Null B: `df42c9a95f360f539b51f6fc6e176b950c4270332d295cee0d913edb348aed73`.

A second replay with the same seeds was bit-identical.

The registered family-wise max statistic gives:

| family | empirical 99% threshold | observed max \(T\) | empirical tail rank |
|---|---:|---:|---:|
| corrected Null A | 3.6953790239 | 1.8196292851 | 0.9768123017 |
| corrected Null B | 3.6931766084 | 2.1614452450 | 0.8057114962 |

Thus the observed global maximum is comfortably below the family-wise threshold under each null family.

No eligible cell clears both thresholds.

## 5. Strongest remaining cells

The strongest joint-margin cell is

- \(\eta=1/1000\);
- zero-based bin \(b=6\);
- \(C_A=-1.8097545288\);
- \(C_B=-1.8574064828\).

Its sign is negative on all five discovery scales under both standardizations, but it remains far below both 99% family-wise thresholds. Its smaller threshold margin is

\[
-1.8856244951.
\]

The largest absolute corrected-Null-A cross-scale statistic occurs at \(\eta=1/1000,b=19\):

\[
C_A=-1.8196292851,\qquad C_B=-1.7017588626.
\]

The largest absolute corrected-Null-B cross-scale statistic occurs at \(\eta=1/100,b=14\):

\[
C_A=0.9831398449,\qquad C_B=2.1614452450.
\]

Neither is close to passing both gates.

## 6. Holdout firewall

The registered new holdouts

\[
X=3\cdot10^8,\qquad X=10^9
\]

were not enumerated, queried, or used in any statistic.

Because no discovery candidate exists, the taskbook requires termination without holdout evaluation. The holdouts remain available for a genuinely different future hypothesis; they are not consumed to rescue this failed global occupancy observable.

## 7. Authority and interpretation

The preceding semiprime-shell results were not used as Working Truth. This result depends on the current taskbook, exact discovery enumeration, the pre-residual support freeze, and the two corrected null generators.

The strongest justified interpretation is:

\[
\boxed{\text{GLOBAL SEMIPRIME FACTOR-SHELL OCCUPANCY}
\;\text{shows no stable second-order residual at the tested scales.}}
\]

More precisely, once the nuisance model preserves local wheel-conditioned density, exact shell-overlap covariance, and circular short-gap structure while retaining positive conditional support, the previously interesting global occupancy phase does not exceed corrected family-wise null fluctuations.

This is **not** a theorem that every prime/semiprime coordinate observable is structure-free. It closes only the naive global occupancy observable at the registered second-order density/covariance strength.

## 8. Hard-target disposition

Hard target:

`SEMIPRIME_FACTOR_SHELL_POSITIVE_SUPPORT_SECOND_ORDER_SURVIVOR_CLASSIFIED`.

Disposition:

`SECOND_ORDER_DENSITY_ARTIFACT`.

There is no unresolved global occupancy candidate within this task.

A future task would need a genuinely different, independently motivated observable or a predeclared local arithmetic stratum. Adding such a variable here after the global occupancy failure would be post-hoc rescue and is not allowed.

## 9. Reproducibility

Artifacts:

- `research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_POSITIVE_SUPPORT_SECOND_ORDER_NULL/support_freeze.json`;
- `research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_POSITIVE_SUPPORT_SECOND_ORDER_NULL/result_summary.json`;
- `scripts/check_prime_factor_semiprime_shell_positive_support_second_order_null.py`.

Checker:

```bash
python scripts/check_prime_factor_semiprime_shell_positive_support_second_order_null.py
```

reconstructs exact discovery counts and the exact positive-support set without holdout access.

With `numpy` and `numba` available,

```bash
python scripts/check_prime_factor_semiprime_shell_positive_support_second_order_null.py --full
```

also regenerates both 4,096-replicate discovery arrays and verifies their frozen SHA-256 values, thresholds, observed max statistics, and zero-candidate decision.

## 10. Final freeze

`POSITIVE_SUPPORT_ELIGIBLE_CELLS = 60`.

`CORRECTED_NULL_A_99 = 3.6953790238805664`.

`CORRECTED_NULL_B_99 = 3.6931766083545967`.

`OBSERVED_MAX_T_A = 1.8196292851063531`.

`OBSERVED_MAX_T_B = 2.1614452449762354`.

`DISCOVERY_CANDIDATES = 0`.

`HOLDOUTS_3E8_AND_1E9 = UNTOUCHED`.

`RESULT = SECOND_ORDER_DENSITY_ARTIFACT`.

`UNRESOLVED_GLOBAL_OCCUPANCY_RESIDUE = NONE`.
