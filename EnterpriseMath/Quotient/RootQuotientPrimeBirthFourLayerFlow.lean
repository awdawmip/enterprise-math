import EnterpriseMath.Quotient.RootQuotientRepairPackingExtension
import EnterpriseMath.Quotient.RootQuotientPrimeBirthPreinvestmentPenalty
import EnterpriseMath.Quotient.RootQuotientPrimeBirthPenaltyFlow
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Complete four-layer hard-prime-birth event formula.**

At `N+1=p^(h+1)`:

* direction demand always rises by one;
* packing rises exactly when the new target extends an old maximum packing;
* cover rises exactly by the cover preinvestment penalty;
* exact storage rises exactly by the exact preinvestment penalty.
-/
theorem fourLayerResourceEvent_at_prime_birth_eq_indicators
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientFourLayerResourceEvent r N h =
      { direction := 1
        packing := rootQuotientPackingExtensionIndicator r N h
        divisorCover :=
          rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p
        exactStorage :=
          rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p } := by
  have hNewHard := prime_birth_mem_primeHardSemanticTargetFinset
    hr hh hp hBirth hBinaryNext
  have hDirection := directionEvent_eq_one_at_prime_birth
    (r := r) hp hBirth
  have hPacking := packingEvent_eq_packingExtensionIndicator_of_newHard hNewHard
  have hThree := resourceEvent_at_prime_birth_eq_preinvestmentPenalties
    hr hh hp hBirth hBinaryNext
  apply RootQuotientFourLayerResourceEvent.ext
  · exact hDirection
  · exact hPacking
  · exact congrArg RootQuotientResourceEvent.divisorCover hThree
  · exact congrArg RootQuotientResourceEvent.exactStorage hThree

/-- Prime-birth packing-over-direction gap flow. -/
theorem mixedPackingGapFlow_at_prime_birth
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientMixedPackingGapInt r (N + 1) h -
        rootQuotientMixedPackingGapInt r N h =
      (rootQuotientPackingExtensionIndicator r N h : ℤ) - 1 := by
  rw [mixedPackingGapInt_succ_sub_eq_event_difference]
  have hEvent := fourLayerResourceEvent_at_prime_birth_eq_indicators
    hr hh hp hBirth hBinaryNext
  rw [hEvent]
  rfl

/-- Prime-birth packing-to-cover coordination flow. -/
theorem packingToCoverGapFlow_at_prime_birth
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientPackingToCoverGapInt r (N + 1) h -
        rootQuotientPackingToCoverGapInt r N h =
      (rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p : ℤ) -
        (rootQuotientPackingExtensionIndicator r N h : ℤ) := by
  rw [packingToCoverGapInt_succ_sub_eq_event_difference hh]
  have hEvent := fourLayerResourceEvent_at_prime_birth_eq_indicators
    hr hh hp hBirth hBinaryNext
  rw [hEvent]
  rfl

/-- Prime-birth residual-depth flow. -/
theorem residualDepthGapFlow_at_prime_birth_fourLayer
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h =
      (rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p : ℤ) -
        (rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p : ℤ) := by
  rw [residualDepthGapInt_succ_sub_eq_fourLayer_event_difference hr hh]
  have hEvent := fourLayerResourceEvent_at_prime_birth_eq_indicators
    hr hh hp hBirth hBinaryNext
  rw [hEvent]
  rfl

/-- The three internal prime-birth flows telescope to the old total mixed-gap
law. -/
theorem primeBirth_fourLayerGapFlows_telescope
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    (rootQuotientMixedPackingGapInt r (N + 1) h -
        rootQuotientMixedPackingGapInt r N h) +
    (rootQuotientPackingToCoverGapInt r (N + 1) h -
        rootQuotientPackingToCoverGapInt r N h) +
    (rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h) =
      (rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p : ℤ) - 1 := by
  rw [mixedPackingGapFlow_at_prime_birth hr hh hp hBirth hBinaryNext,
    packingToCoverGapFlow_at_prime_birth hr hh hp hBirth hBinaryNext,
    residualDepthGapFlow_at_prime_birth_fourLayer hr hh hp hBirth hBinaryNext]
  ring

end EnterpriseMath.Quotient
