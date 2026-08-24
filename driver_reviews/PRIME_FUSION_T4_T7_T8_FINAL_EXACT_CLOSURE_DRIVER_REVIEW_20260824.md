# Driver Review — Prime Fusion T4/T7/T8 Final Exact Closure

Status: `DRIVER_ACCEPTED / EXACT_CLOSURE_VERIFIED / STRONGER_THEOREMS_RETAINED`
Date: `2026-08-24`
Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`
Task: `RS-PRIME-FUSION-T4-T7-T8-FINAL-EXACT-CLOSURE`
Taskbook source: `522d1f9847b087eff380d79b506cb6924f5fa7cd`
Owner branch: `research/prime-fusion-t4-t7-t8-final-exact-closure`
Frozen owner head: `5723685c3ef3b43b5fb826af3b185f142a60d0ec`
Checker commit before return freeze: `e203f6b9b298532345a7d5209cb35c564b5d3e89`
Return: `research_returns/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_RETURN_20260823.md`
Checker: `experiments/prime_fusion_t4_t7_t8_final_exact_closure_checker.py`

## 1. Branch and evidence audit

Relative to taskbook source `522d1f9847b087eff380d79b506cb6924f5fa7cd`, the owner branch is `ahead 3 / behind 0` and changes only two output paths:

1. the independently authored exact checker;
2. the frozen return.

The extra commit count reflects checker strengthening before freeze, not unrelated branch mutation.

The return declares `STATEMENT-EXPOSED INDEPENDENT EXACT VERIFICATION / PASS`. Before freeze, its mathematical inputs were limited to the controlling taskbook and the statement-only packet at `d8e3df5e2ceb61e63fe12ad38524fa5f5968f5cf`; withheld source proofs/checker/narrative and downstream reconciliation were not used.

Verdict:

`EVIDENCE_BOUNDARY = ACCEPTED`.

## 2. T4 — accepted and strengthened

Source-scope theorem:

`R/(a+b xi) ~= Z/NZ x Z/CZ ~= Z/HZ`

for a positive primitive cell, with pointed residue

`r == -a*b^{-1} (mod H)`.

The independent closure constructs the quotient maps and kernels explicitly; it does not rely on cardinality alone.

Stronger result retained:

For `d=gcd(a,b)`, the Gaussian and Eisenstein component additive quotients have Smith invariant factors

`(d,N/d)` and `(d,C/d)`.

Hence component cyclicity holds iff `d=1`.

Therefore primitivity is the exact cyclicity criterion, not merely a sufficient condition.

Driver classification:

`T4 = INDEPENDENTLY_VERIFIED_AT_EXACT_POINTED_RING_STRENGTH / STRENGTHENED_SNF_CYCLICITY_THEOREM`.

## 3. T7 — accepted and strengthened

For every idempotent `e mod H`, defining

`N=gcd(e,H)`, `C=gcd(e-1,H)`

automatically gives

`NC=H`, `gcd(N,C)=1`.

Thus those two source assumptions are redundant once idempotence is known.

For positive primitive unordered cells, the exact reconstruction gate is:

`N>C`

and

`U=3N-2C`, `V=2C-N`

are perfect squares.

Strict interiority away from the positive diagonal is exactly the additional condition `V>0`, equivalently `N<2C`.

The return supplies exact negative controls showing both the square gate and the orientation condition are theorem-critical.

Driver classification:

`T7 = INDEPENDENTLY_VERIFIED_AT_EXACT_SOURCE_STRENGTH / MINIMAL_HYPOTHESES_IDENTIFIED`.

## 4. T8 — accepted and strengthened

The source equivalence for an interior primitive cell survives:

`dual-prime <=> R/(a+b xi) ~= F_p x F_q`

with distinct channel primes `p=N`, `q=C`, equivalently total norm `H=NC` square-free semiprime with canonical channel attachment.

The independent closure proves the algebraic equivalence on the larger nonzero nonnegative cell family:

`N,C both prime <=> H=NC is a square-free semiprime`.

Boundary and nonprimitive controls were included. The abstract product `F_p x F_q` does not by itself remember which factor is Gaussian versus Eisenstein; canonical channel labels are extra structure supplied by the fixed product projections / central idempotents.

Driver classification:

`T8 = INDEPENDENTLY_VERIFIED_AT_EXACT_SOURCE_STRENGTH / STRONGER_CELL_FAMILY_EQUIVALENCE_AVAILABLE`.

## 5. Executable evidence

The independently authored checker returned:

`PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_CHECKER: PASS`.

Recorded finite audit includes:

- T4 SNF/cyclicity over `0<=a,b<=64`, excluding `(0,0)`, with explicit primitive/nonprimitive controls;
- T7 every idempotent for every modulus `1<=H<=1000` (`4,987` idempotents), plus exact reconstruction witnesses and negative controls;
- T8 all nonzero nonnegative cells with `0<=a,b<=100` (`10,200` cells), including `460` dual-prime cells and boundary/nonprimitive/prime-power/composite controls.

Finite checks are audit evidence; acceptance rests on the written exact proofs.

## 6. Final task verdict

Researcher final classification:

`T4_T7_T8_EXACT_CLOSURE_VERIFIED`.

Driver accepts it.

Hard target:

`PRIME_FUSION_T4_T7_T8_EXACT_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED = SATISFIED`.

No theorem-critical source statement among T4/T7/T8 requires weakening.

This closes the last three rows that previously had only `PARTIAL` independent coverage.
