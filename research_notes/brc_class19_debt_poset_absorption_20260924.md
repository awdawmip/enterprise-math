# BRC class-19 debt poset and absorbing dirty steps

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note continues the quantitative cancellation-debt theorem. It identifies the exact order structure behind the class-19 obstruction and proves that a dirty class-13 cancellation step cannot be bypassed indirectly by a different class-19-neutral suppressor.

## 1. Debt as a function of the cancellation step

For a class-19 target prime r, put

`h_r=(r-1)/2`

and for any positive odd integer s define

`d_r(s)=1_{h_r|s}+v_r(s)`.

For a class-13 prime q with `ord_q(4)=2s_q`, this is exactly the q-to-r cancellation-debt coefficient from the previous unit.

### Theorem 1.1 — divisibility monotonicity

If `s|t`, then for every class-19 r,

`d_r(t)>=d_r(s)`.

### Proof

If `h_r|s`, then `h_r|t`, so the endpoint indicator cannot decrease. Also `s|t` gives `v_r(t)>=v_r(s)`. Add the two inequalities.

Thus the vector map

`Debt_19(s)=(d_r(s))_r`

is coordinatewise monotone on the divisibility poset of odd cancellation steps.

## 2. Dirty is an upward-closed divisibility property

Fix a target horizon p and call an odd step s **19-dirty below p** when `d_r(s)>0` for at least one class-19 target `r<p`; otherwise call it **19-clean below p**.

Theorem 1.1 immediately gives:

### Corollary 2.1

- the dirty steps form an upward-closed set under divisibility;
- the clean steps form a divisor-downward set.

In particular, if a class-13 q is dirty and another class-13 cancellation step `s_Q` is a multiple of `s_q`, then Q is dirty as well and inherits at least the same class-19 debt vector on every already-active coordinate.

This is stronger than a finite list of dirty primes: it is an order invariant of the cancellation-step lattice.

## 3. Absorbing dirty rows in the large-prime signature cone

Consume the exact large-prime signature column for a class-13 generator Q:

- at a class-13 row q, the column is negative exactly when `s_q|s_Q`, in which case it equals `-c_q`;
- otherwise its q-entry is nonnegative;
- its class-19 coordinates are the nonnegative debt vector `Debt_19(s_Q)`.

Suppose q is 19-dirty. Any signature column capable of lowering row q must satisfy `s_q|s_Q`. By Corollary 2.1, such a Q is necessarily 19-dirty too. Therefore:

### Theorem 3.1 — absorbing dirty row

After restricting to signature generators that are exactly neutral on every earlier class-19 branch, every 19-dirty class-13 row has **no negative incoming column**.

Consequently its defect can only stay fixed or increase under any class-19-neutral combination of large-prime signature generators.

So a positive dirty class-13 blocker is an immediate infeasibility certificate for p-neutral/class-19-neutral repair inside the full signature cone. There is no indirect route through another clean class-13 suppressor.

This closes a loophole left by a q-specific construction: one might have hoped to suppress dirty q using a different Q whose cancellation progression contains q's. Divisibility monotonicity proves that every such Q inherits q's class-19 debt and is therefore forbidden by the same neutrality constraint.

## 4. Arbitrary-port strengthening

The same conclusion is not merely an artifact of the large-prime quotient.

Any port j that contributes negatively to a dirty class-13 q must lie on q's cancellation progression, hence `s_q|j` with odd quotient. For every class-19 r witnessing q's dirtiness, either `h_r|s_q` or `r|s_q`, and therefore the same positive endpoint/denominator event occurs at j. Since class 19 has no negative channel, a cloud that is exactly class-19-neutral cannot occupy such a port at all.

Thus the dirty-row absorption theorem holds before the large-prime quotient as well: class-19 neutrality removes every negative q carrier from the admissible support.

## 5. Finite regression

Checker:

`research_checks/check_brc_class19_debt_poset_absorption_20260924.py`.

Checker publication commit:

`9dbedfb45e5c484d7668103e8062880ffb604c08`.

Below 5000 it verified:

- higher class-13 targets: `82`;
- clean q: `38`;
- dirty q: `44`;
- realized nested cancellation-step pairs `s_q|s_Q`: `103`;
- debt-vector monotonicity failures on all nested pairs: `0`;
- horizon-wise clean-downset failures: `0`;
- clean-generator / dirty-row absorption checks: `44,944`;
- negative incoming clean-generator failures: `0`.

Finite computation is falsification/regression only. The proof is Theorem 1.1 plus the exact signature law and the no-negative-channel property of class 19.

## 6. BRC meaning

The residual state has an order structure: once a cancellation step carries an irreversible class-19 debt, every multiple step carries at least that debt. A quotient that remembers only “this branch can cancel q” but drops the cancellation-step divisibility relation would incorrectly suggest bypasses that do not exist.

For p-neutral repair, the minimal sufficient structural state therefore includes the cancellation-step poset together with the vector debt label on each step.

## 7. Do not repeat / next

Do not search for an indirect class-19-neutral suppressor of a dirty q through a larger cancellation step; the dirty set is upward closed and the row is absorbing.

The next nonredundant auxiliary unit, only while formal D24 remains blocked, is to exploit this absorbing-set theorem to reduce the arbitrary initial-defect repair problem to its clean-step subcone and derive the exact remaining repair budget there.

If the canonical lossless session rollover becomes live, stop auxiliary work and return to the Source-native D24 continuation immediately.
