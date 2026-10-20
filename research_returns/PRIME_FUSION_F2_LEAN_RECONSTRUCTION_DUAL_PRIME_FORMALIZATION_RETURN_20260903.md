# Prime Fusion F2 Lean Reconstruction / Dual-Prime Formalization — Same-Task Revision Return

- Task: `RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION`
- Publication: `TP2-7C31E9A4D5B6082F14CE`
- Researcher-ID: `EM-PFF2-711F6F`
- Claim: `chatgpt-pff2-revision-20260903-1011-ec63243d`
- Execution record: `ER-4F66816516093ADD279C`
- Execution branch: `formalization/prime-fusion-f2-revision-em-pff2-711f6f`
- PR: `#1135`
- Revision baseline: frozen head `5fe2e3c3212cca23ee588cb058016d2a6688cf36`
- Prior frozen Result under revision: `RR-800F535F2CD7966AB03E`
- Task hard target: `PRIME_FUSION_T7_T8_ACCEPTED_MATHEMATICS_LEAN_FORMALIZED_NO_SORRY_WITH_PINNED_BUILD_PASS`
- Research verdict: **FORMALIZED / SAME-TASK DRIVER DEFECT REPAIRED / HARD TARGET MET**

## 1. Why this revision exists

The previous F2 execution had a valid T7/T8 arithmetic layer, a passing warnings-fatal Lean build, and a clean standard-axiom audit, but Driver returned the same Task-ID because F2-L04 was definitionally circular.

The rejected encoding defined `FixedChannelPrimeFieldPair a b` by already storing `(Nmodulus a b).Prime` and `(Cmodulus a b).Prime`; the alleged converse to dual primality therefore recovered exactly what the certificate had assumed. Driver required an independently typed fixed-channel field predicate, a genuine field-to-prime converse, explicit edge conditions, and preservation of the Gaussian/Eisenstein labels.

This execution changes only that theorem-spec defect and its regression guard. The already-accepted T7 reconstruction layer, T8 semiprime arithmetic, fixed CRT/channel interfaces, and negative controls are preserved. No T9 or T12–T15 scope was absorbed.

## 2. Preserved F2-L01 / F2-L02 — T7 reconstruction layer

`EnterpriseMath/PrimeFusion/Reconstruction.lean` is preserved from the reviewed frozen frontier, including:

- `idempotent_universal_channel_split`;
- `channels_isCoprime_implies_primitive`;
- `positive_cell_channel_orientation`;
- `reconstruction_square_gate_necessary`;
- `no_reconstruction_if_U_not_square`;
- `no_positive_reconstruction_if_not_oriented`;
- `reconstruct_positive_cell_of_diagonal_roots`;
- `reconstruct_positive_primitive_cell_of_diagonal_roots`;
- `reconstructed_strict_interior_gate`.

Thus the accepted T7 behavior remains: universal idempotent splitting, exact diagonal-square reconstruction, derived parity, derived primitivity from channel coprimality, preservation of the positive diagonal case, and a separate strict-interior gate.

## 3. Preserved F2-L03 — dual-prime arithmetic equivalence

`EnterpriseMath/PrimeFusion/DualPrime.lean` preserves:

- `SquarefreeSemiprime`;
- `dualPrime_iff_squarefreeSemiprime_mul`;
- `fixed_channels_dualPrime_iff_squarefreeSemiprime`.

For fixed nontrivial distinct factors, the arithmetic theorem remains

`(N.Prime ∧ C.Prime) ↔ SquarefreeSemiprime (N*C)`,

and the cell specialization still uses `Hmodulus_eq_mul` without forgetting the fixed Gaussian/Eisenstein channel attachment on the dual-prime side.

## 4. Repaired F2-L04 — structural fieldness really forces primality

### 4.1 The certificate no longer contains the conclusion

The revised definition is:

```lean
def FixedChannelPrimeFieldPair (a b : ℤ) : Prop :=
  IsField (ZMod (Nmodulus a b)) ∧
    IsField (ZMod (Cmodulus a b)) ∧
      Nmodulus a b ≠ Cmodulus a b
```

There is no `Nat.Prime` field in this predicate. It talks about the already-fixed quotient ring operations themselves and retains the ordered Gaussian/Eisenstein channel labels.

### 4.2 Prime -> field remains the forward construction

`zmod_isField_of_prime` converts a modulus-primality proof into `IsField (ZMod n)` using the canonical `ZMod` prime-field instance. This is used only in the forward dual-prime-to-field direction.

### 4.3 Field -> prime is now a genuine theorem

The new load-bearing converse is:

```lean
theorem zmod_prime_of_isField {n : ℕ} (hn1 : 1 < n)
    (hfield : IsField (ZMod n)) : n.Prime
```

Its proof installs from `hfield` the nontrivial/domain structure of the existing `ZMod n`, obtains `NeZero n` from the explicit edge condition `1 < n`, uses finiteness of `ZMod n`, and applies `CharP.char_is_prime (ZMod n) n`.

Therefore modulus primality is *derived from structural fieldness* rather than stored in the certificate.

### 4.4 Fixed-channel converse and exact edge conditions

The revision adds:

- `fixedChannelPrimeFieldPair_dualPrime`;
- repaired `fixedChannelPrimeFieldPair_iff_dualPrime`.

The converse requires the transparent edge conditions

- `1 < Nmodulus a b`;
- `1 < Cmodulus a b`;

and the biconditional additionally fixes

- `Nmodulus a b ≠ Cmodulus a b`.

The final channel-labelled theorem is therefore noncircular:

`FixedChannelPrimeFieldPair a b ↔ (Nmodulus a b).Prime ∧ (Cmodulus a b).Prime`

under the explicit nondegenerate/distinct-channel hypotheses.

### 4.5 Product/quotient attachment remains fixed and labelled

`fixed_channel_prime_fields_and_orders` now upgrades each structural `IsField` proof to actual `Field` data on exactly the existing `ZMod N` and `ZMod C` operations and preserves their exact cardinalities.

`fixed_channel_prime_field_product` still combines those labelled field carriers with the pre-existing `pointedCRT` equivalence

`ZMod H ≃+* ZMod N × ZMod C`.

The codomain order continues to encode Gaussian channel first and Eisenstein channel second; no unordered abstract-product shortcut replaces the fixed projections.

## 5. F2-L05 — integration, regression guard, proof integrity

`EnterpriseMath/PrimeFusion.lean` imports the F2 modules and explicitly prints axioms for the repaired load-bearing declarations, including:

- `zmod_prime_of_isField`;
- `fixedChannelPrimeFieldPair_dualPrime`;
- `fixedChannelPrimeFieldPair_iff_dualPrime`.

A new deterministic guard was added at:

`research_checks/PRIME_FUSION_F2_LEAN_RECONSTRUCTION_DUAL_PRIME_FORMALIZATION_CHECK_20260903.py`.

It rejects `sorry`, `admit`, explicit custom `axiom`, and `unsafe` declarations in the F2 source; it also parses `FixedChannelPrimeFieldPair` and fails if `.Prime` / `Nat.Prime` is reintroduced into that certificate. It requires the structural `IsField -> IsDomain -> CharP.char_is_prime` converse surface and the repaired axiom-audit declarations.

The module intentionally uses proposition-valued instances through typeclass synthesis. The pinned `--wfail` build initially rejected the otherwise elaborated module only because the style linter recommends ordinary `let` over `letI` for proposition-valued declarations. Because ordinary `let` would not register those values for typeclass synthesis, the final module explicitly disables only `linter.style.haveILetI` for this file and documents why; no theorem statement or proof obligation is weakened.

## 6. Pinned machine-check evidence

### 6.1 Diagnostic run

- Workflow: `lean`
- Run: `33707240057`
- Job: `100498947756`
- Owner head: `f35b0a9070bfe0451d1f1d9f24d6e6bddf3323a2`
- Outcome: **FAIL only because warnings are fatal**
- Diagnostic: five `linter.style.haveILetI` warnings in `DualPrime.lean`.
- Important: `DualPrime.lean` elaborated and the top-level `#print axioms` output was produced; there was no theorem/type error.

### 6.2 Authoritative successful build

- GitHub Actions workflow: `lean`
- Run: `33707604969`
- Job: `100500020046`
- Tested owner head: `a413be9df26c0b2093c2048fa8e50ce27db1fdf1`
- PR merge ref tested by Actions: `1f8ea121d03556ec634aecb664d13e3100b27b99`
- Integrated base in that merge ref: `6f8f53230f6e36e0b55c873a72052176dd40b673`
- Toolchain: `leanprover/lean4:v4.33.0-rc2`
- Lean commit reported by runner: `d8b18978322de05a8f3dba51ef03cf5461676c17`
- mathlib revision: `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`
- Command: `lake build --wfail -KCI EnterpriseMath`
- Result: **PASS — `Build completed successfully (8733 jobs).`**

The successful run compiled:

- `EnterpriseMath.PrimeFusion.Reconstruction`;
- `EnterpriseMath.PrimeFusion.DualPrime`;
- `EnterpriseMath.PrimeFusion`;
- top-level `EnterpriseMath`.

The repaired load-bearing declarations report only repository-accepted standard Lean axioms:

- `propext`;
- `Classical.choice`;
- `Quot.sound`.

No custom axiom, `sorry`, or `admit` is present.

## 7. Repository-wide non-task CI status

The broad `quality` and `reference-integrity` workflows remain red and are not claimed as passing evidence for this task. At least one current `quality` failure is demonstrably an upstream control-plane import fault:

`tests/test_research_dispatch_cohort_overlay.py: ImportError: cannot import name 'research_scheduler' from 'tools'`.

That failure occurs in the generic Python unit-test shard and is unrelated to the F2 Lean source. The taskbook's explicit hard gate is the pinned warnings-fatal Lean build plus proof-integrity/axiom checks; that gate passes on the tested PR merge ref.

## 8. Residue and next control-plane action

F2 mathematical/formalization residue after the Driver-requested same-task repair: **NONE**.

The only remaining action is Driver review of PR #1135 and the replacement frozen Result. Driver should check that the new `IsField (ZMod ...)` certificate and characteristic argument satisfy the requested F2-L04 theorem-spec fidelity, then accept/integrate or return a new concrete theorem-level defect.

No F3 successor is authorized by this return.
