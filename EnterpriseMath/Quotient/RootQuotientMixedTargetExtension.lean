import EnterpriseMath.Quotient.RootQuotientHardDirectionRepair
import EnterpriseMath.Quotient.RootQuotientMacroRepairEquivalence
import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact storage overhead caused by extending the repair target family from the
hard pure-prime directions to the complete bounded semantic target family,
keeping the forced prime backend and semantic-composite candidate set fixed. -/
noncomputable def rootQuotientMixedTargetExtensionOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientSemanticTargetFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) -
    rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientHardPrimeTargetFinset N h)
      (RootQuotientSemanticCompositeCandidates r N)

/-- Hard-direction count is exactly the existing pure-direction demand. -/
theorem hardPrimeDirections_ncard_eq_primeDirectionDemand
    (N h : ℕ) :
    (RootQuotientHardPrimeDirections N h).ncard =
      rootQuotientPrimeDirectionDemand N h := by
  rw [rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff]
  rfl

/-- **Mixed-direction overhead = target-extension repair overhead.**

In the high-root regime, the previously defined mixed-direction macro overhead
has an exact task-extension meaning: it is the additional minimum dictionary
cardinality required when one enlarges the repair specification from the hard
pure-prime targets to all bounded semantic targets. -/
theorem mixedTargetExtensionOverhead_eq_mixedDirectionMacroOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMixedTargetExtensionOverhead r N h =
      rootQuotientMixedDirectionMacroOverhead r N h := by
  have hFull := minimumCompositeMacroCount_eq_minimumRelativeRepairStorage
    (r := r) (N := N) (h := h) hr hh
  have hPure := hardTargetMinimumRelativeRepairStorage_eq_direction_ncard
    (r := r) (N := N) (h := h) hr hh hBinary
  have hDir := hardPrimeDirections_ncard_eq_primeDirectionDemand N h
  dsimp [rootQuotientMixedTargetExtensionOverhead,
    rootQuotientMixedDirectionMacroOverhead]
  rw [← hFull, hPure, hDir]

/-- Full semantic repair storage decomposes into pure-direction repair storage
plus the mixed target-extension overhead. -/
theorem fullSemanticRepairStorage_eq_pureDirectionRepair_add_mixedExtension
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) +
      rootQuotientMixedTargetExtensionOverhead r N h := by
  have hFull := minimumCompositeMacroCount_eq_minimumRelativeRepairStorage
    (r := r) (N := N) (h := h) hr hh
  have hPure := hardTargetMinimumRelativeRepairStorage_eq_direction_ncard
    (r := r) (N := N) (h := h) hr hh hBinary
  have hDir := hardPrimeDirections_ncard_eq_primeDirectionDemand N h
  have hDecomp := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  have hMix := mixedTargetExtensionOverhead_eq_mixedDirectionMacroOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  rw [← hFull, hPure, hDir, hMix]
  exact hDecomp

/-- Mixed overhead vanishes exactly when extending from the pure-direction
repair task to the full semantic repair task costs no extra stored macro type. -/
theorem mixedDirectionMacroOverhead_eq_zero_iff_fullRepair_eq_pureRepair
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMixedDirectionMacroOverhead r N h = 0 ↔
      rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) := by
  have hDecomp := fullSemanticRepairStorage_eq_pureDirectionRepair_add_mixedExtension
    (r := r) (N := N) (h := h) hr hh hBinary
  have hMix := mixedTargetExtensionOverhead_eq_mixedDirectionMacroOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  rw [hMix] at hDecomp
  omega

end EnterpriseMath.Quotient
