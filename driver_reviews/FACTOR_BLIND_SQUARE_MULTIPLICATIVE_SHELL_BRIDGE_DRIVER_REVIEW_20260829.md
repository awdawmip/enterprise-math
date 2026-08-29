# Driver Review — Factor-Blind Square–Multiplicative Shell Bridge

Driver-ID: `EM-DVR-P8H4Q2`
Task: `RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE`
Publication: `TP2-A712090E5314373E5447`
Canonical Result: `RR-C5769D6B237D02BFF025`
Canonical Claim: `chatgpt-smsb1-20260829-1645-73d4c2`
Researcher: `EM-SMSB1-73D4C2`
Verdict: `ACCEPTED / NEGATIVE_BOUNDARY`

## 1. Duplicate-claim resolution

This task is not a declared cohort. Under the runtime invariant `FIRST_VALID_CLAIM_WINS`, the operational claim is determined by GitHub server comment order. Claim comment `5461383212` (`EM-SMSB1-73D4C2`, created `2026-08-29T08:47:53Z`) precedes duplicate claim comment `5461388441` (`EM-SMSB1-4A7E2C`, created `2026-08-29T08:49:14Z`). Therefore `EM-SMSB1-73D4C2` is the canonical execution lineage. The later branch/result may be retained as corroborating audit evidence but has no competing runtime authority.

## 2. Accepted exact result

The exact periodic-filter obstruction is accepted at the stated restricted strength.

Let a factor-blind Fermat-offset filter be periodic with fixed finite period `M` and suppose it retains the true Fermat offset `T`. Periodicity forces every nonnegative congruent predecessor

`T - jM`,  `0 <= j <= floor(T/M)`,

to be retained as well. Hence the number of retained candidates through `T` is at least

`floor(T/M) + 1`.

Therefore every such fixed-finite periodic filter has retained-candidate complexity `Omega(T)` and cannot provide `o(T)` candidate count. This is an exact no-go for that mechanism class; it is not a universal no-go for all `N`-derived factor-blind mechanisms.

The bridge identity `B^2 = b + T(2c+T)` is accepted as the Fermat conic identity / reparameterization boundary, not as a new factor oracle.

## 3. Accepted empirical boundary

The frozen `SHELL_RESIDUE_QR_CONDITIONAL_V1` family is accepted as empirically negative under the task's dual-compartment factor-blind contract:

- 800 primary cases and 600 adversarial challenge cases;
- 24/32/40/48/64-bit bands;
- no serialized factor labels in worker-visible public corpus;
- independent stdlib checker reproduces the high-recall collapse on the adversarial challenge;
- at 99% recall, the independently replayed KNN requires all 10 buckets for the p-rank, q/M2-proxy, and T targets, so the corresponding compression ratio is 1.

The authoring random-forest metrics and exact operation-count ratios are retained as supporting implementation evidence, but they are not promoted to independently replayed theorem-level facts because the independent checker does not reproduce those sklearn models or all wrapper cost counters.

## 4. Factorization-gain disposition

`NO_S1 / NO_S2 / NO_S3` is accepted.

The exact-search wrapper did not establish a competitive factorization gain outside the near-twin regime. Apparent near-twin advantage is not admitted as S2 because matched Fermat already has `T=0` or negligible displacement and is the stronger comparator. No Working Truth, Foundation mutation, canonical promotion, or factorization-algorithm claim is granted.

## 5. Scope exclusions

This review explicitly does **not** establish any of the following:

1. a universal impossibility theorem for every factor-blind function of `N`;
2. a no-go for nonperiodic, adaptive, or algebraic mechanisms;
3. exact full-M2 localization from the q-bucket proxy;
4. novelty merely from re-encoding `(L,D)` or finite multi-k signatures;
5. permission to reopen the same periodic-residue family by retuning model class, bucket count, or finite multiplier list.

## 6. Method harvest and successor policy

Harvest:

`RESULT_ONLY / EXACT_PERIODIC_SIEVE_NO_GO_REUSABLE / TESTED_CONDITIONAL_FAMILY_NEGATIVE / NO_GENERAL_FACTOR_BLIND_BRIDGE`

No automatic successor is authorized. A future task is justified only if it introduces a genuinely different mechanism class—nonperiodic, adaptive, algebraic, or another explicitly non-equivalent factor-blind construction—with a frozen leakage contract and exact total-cost comparator. The existing residual-priority/Hart streaming-cost task remains separate and should not be republished here.

## 7. Driver disposition

`RR-C5769D6B237D02BFF025` is **ACCEPTED as a NEGATIVE_BOUNDARY at the restricted strength above**.

The later duplicate execution `EM-SMSB1-4A7E2C` is classified `AUDIT_ONLY / NONOPERATIONAL_DUPLICATE_CLAIM`; its mathematical observations may corroborate the accepted boundary but do not replace or compete with the canonical result lineage.
