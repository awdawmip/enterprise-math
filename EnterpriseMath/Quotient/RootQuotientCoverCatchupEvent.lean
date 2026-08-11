import EnterpriseMath.Quotient.RootQuotientResourceFlow
import EnterpriseMath.Quotient.RootQuotientThreeMacroStableOptimality
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- From horizon ten onward, the two-type divisor-cover threshold occurs strictly
before the globally optimal three-macro q=7 threshold. -/
theorem six_mul_five_pow_lt_threeMacroStableThreshold_of_ten_le
    {h : ℕ}
    (hTen : 10 ≤ h) :
    6 * 5 ^ (h - 1) < rootQuotientThreeMacroStableThreshold h := by
  obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hTen
  have hPow : 5 ^ n ≤ 7 ^ n := Nat.pow_le_pow_left (by omega) n
  calc
    6 * 5 ^ (10 + n - 1) = 11718750 * 5 ^ n := by
      simp [pow_add]
      norm_num
    _ < 49412580 * 7 ^ n := by
      nlinarith [show 0 < 7 ^ n by positivity]
    _ = rootQuotientThreeMacroStableThreshold (10 + n) := by
      simp [rootQuotientThreeMacroStableThreshold, pow_add]
      norm_num

/-- Resource values immediately before the two-type divisor-cover threshold in
the stable budget-three range. -/
theorem resources_before_twoCoverThreshold_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    rootQuotientPrimeDirectionDemand (6 * 5 ^ (h - 1) - 1) h = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber
        r (6 * 5 ^ (h - 1) - 1) h = 2 ∧
    rootQuotientMinimumCompositeMacroCount
        r (6 * 5 ^ (h - 1) - 1) h = 3 := by
  have hh : 3 ≤ h := by omega
  have hChain := threeLayerThresholdChain hh
  have hLower : rootQuotientTwoMacroFullThreshold h ≤
      6 * 5 ^ (h - 1) - 1 := by
    have hStrict := hChain.2.2.2.1
    omega
  have hUpper : 6 * 5 ^ (h - 1) - 1 < 6 * 5 ^ (h - 1) := by
    positivity
  have hPhase := threeLayer_phase_pure_residual_depth
    (r := r) (N := 6 * 5 ^ (h - 1) - 1) (h := h)
    hr hh (by omega) hLower hUpper
  exact ⟨hPhase.1, hPhase.2.1, hPhase.2.2.1⟩

/-- Resource values at the two-type divisor-cover threshold once the stable
budget-three theorem is available. -/
theorem resources_at_twoCoverThreshold_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    rootQuotientPrimeDirectionDemand (6 * 5 ^ (h - 1)) h = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber
        r (6 * 5 ^ (h - 1)) h = 3 ∧
    rootQuotientMinimumCompositeMacroCount
        r (6 * 5 ^ (h - 1)) h = 3 := by
  let C := 6 * 5 ^ (h - 1)
  have hh : 3 ≤ h := by omega
  have hChain := threeLayerThresholdChain hh
  have hThreeLower : 3 ^ (h + 1) ≤ C := by
    have hB2Le : 3 ^ (h + 1) < rootQuotientTwoMacroFullThreshold h :=
      hChain.2.2.1
    have hB2C : rootQuotientTwoMacroFullThreshold h < C := by
      exact hChain.2.2.2.1
    omega
  have hFiveUpper : C < 5 ^ (h + 1) := hChain.2.2.2.2
  have hDir : rootQuotientPrimeDirectionDemand C h = 2 :=
    primeDirectionDemand_eq_two_of_three_pow_le_of_lt_five_pow
      hThreeLower hFiveUpper
  have hCoverLower : 3 ≤ rootQuotientGlobalRepairDivisorCoverNumber r C h :=
    three_le_globalRepairDivisorCoverNumber_of_six_mul_five_pow_le
      hr hh (by simpa [C] using hBinary) (by simp [C])
  have hBefore := resources_before_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hCoverStep := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := C - 1) (h := h) (by omega)
  have hCSucc : (C - 1) + 1 = C := by
    have hCPos : 0 < C := by dsimp [C]; positivity
    omega
  have hCoverUpper : rootQuotientGlobalRepairDivisorCoverNumber r C h ≤ 3 := by
    rw [← hCSucc]
    have := hCoverStep.2
    rw [hBefore.2.1] at this
    omega
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r C h = 3 := by omega
  have hStableUpper : C < rootQuotientThreeMacroStableThreshold h :=
    six_mul_five_pow_lt_threeMacroStableThreshold_of_ten_le hTen
  have hMuUpper : rootQuotientMinimumCompositeMacroCount r C h ≤ 3 :=
    (minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
      (r := r) (N := C) (h := h)
      hr hTen (by dsimp [C]; positivity) (by simpa [C] using hBinary)).2
      hStableUpper
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := C) (h := h) hr (by omega)
  have hMu : rootQuotientMinimumCompositeMacroCount r C h = 3 := by omega
  exact ⟨hDir, hCover, hMu⟩

/-- Event type `(0,1,0)`: the divisor-cover layer catches up with exact storage,
absorbing one unit of residual-depth overhead. -/
def rootQuotientCoverCatchupEvent : RootQuotientResourceEvent :=
  ⟨0, 1, 0⟩

/-- **Fifth exact universal resource event.**

For every stable budget-three horizon `h>=10`, the state
`6*5^(h-1)` triggers a pure cover catch-up event: direction demand stays two,
the divisor-cover minimum rises from two to three, and exact storage remains
three. -/
theorem resourceEvent_at_twoCoverThreshold_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    rootQuotientResourceEvent r (6 * 5 ^ (h - 1) - 1) h =
      rootQuotientCoverCatchupEvent := by
  let C := 6 * 5 ^ (h - 1)
  have hBefore := resources_before_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hAt := resources_at_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hSucc : (C - 1) + 1 = C := by
    have hCPos : 0 < C := by dsimp [C]; positivity
    omega
  dsimp [rootQuotientResourceEvent, rootQuotientCoverCatchupEvent]
  rw [show 6 * 5 ^ (h - 1) = C by rfl, hSucc,
    hBefore.1, hBefore.2.1, hBefore.2.2,
    hAt.1, hAt.2.1, hAt.2.2]
  rfl

/-- At the cover-catchup event, mixed-cover gap increases by one while the
residual-depth gap decreases by one. -/
theorem gapFlow_at_twoCoverThreshold_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    rootQuotientMixedCoverGapInt r (6 * 5 ^ (h - 1)) h -
        rootQuotientMixedCoverGapInt r (6 * 5 ^ (h - 1) - 1) h = 1 ∧
    rootQuotientResidualDepthGapInt r (6 * 5 ^ (h - 1)) h -
        rootQuotientResidualDepthGapInt r (6 * 5 ^ (h - 1) - 1) h = -1 := by
  have hBefore := resources_before_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hAt := resources_at_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  dsimp [rootQuotientMixedCoverGapInt, rootQuotientResidualDepthGapInt]
  rw [hBefore.1, hBefore.2.1, hBefore.2.2,
    hAt.1, hAt.2.1, hAt.2.2]
  norm_num

end EnterpriseMath.Quotient
