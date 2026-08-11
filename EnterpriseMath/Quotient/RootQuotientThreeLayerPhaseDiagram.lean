import EnterpriseMath.Quotient.RootQuotientDivisorCoverFrontier
import EnterpriseMath.Quotient.RootQuotientTwoMacroHorizonTwo
import EnterpriseMath.Quotient.RootQuotientPrimeFourEightNineMetric
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- First arithmetic threshold: the pure-2 hard direction is born before the
first mixed divisor-cover obstruction. -/
theorem two_pow_succ_lt_two_mul_three_pow
    {h : ℕ}
    (hh : 1 ≤ h) :
    2 ^ (h + 1) < 2 * 3 ^ h := by
  have hPow : 2 ^ h < 3 ^ h :=
    pow_lt_pow_left' (by omega : h ≠ 0) (by omega : (2 : ℕ) < 3)
  rw [pow_succ]
  nlinarith

/-- The second pure-prime direction is born before the exact budget-two
compiler frontier for every horizon `h>=3`. -/
theorem three_pow_succ_lt_twoMacroFullThreshold_of_three_le
    {h : ℕ}
    (hh : 3 ≤ h) :
    3 ^ (h + 1) < rootQuotientTwoMacroFullThreshold h := by
  have hTwo : h ≠ 2 := by omega
  by_cases hFive : h ≤ 5
  · have hCases : h = 3 ∨ h = 4 ∨ h = 5 := by omega
    rcases hCases with rfl | rfl | rfl <;>
      norm_num [rootQuotientTwoMacroFullThreshold,
        rootQuotientTwoMacroOptimalThreshold,
        rootQuotientFourNineThreshold]
  · have hSix : 6 ≤ h := by omega
    obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hSix
    have hPow : 3 ^ n ≤ 5 ^ n := Nat.pow_le_pow_left (by omega) n
    calc
      3 ^ (6 + n + 1) = 2187 * 3 ^ n := by
        simp [pow_add]
        norm_num
      _ < 7500 * 5 ^ n := by
        nlinarith [show 0 < 5 ^ n by positivity]
      _ = rootQuotientTwoMacroFullThreshold (6 + n) := by
        simp [rootQuotientTwoMacroFullThreshold,
          rootQuotientTwoMacroOptimalThreshold,
          rootQuotientEightNineThreshold, pow_add]
        norm_num

/-- The exact budget-two compiler frontier lies strictly before the two-type
divisor-cover frontier. -/
theorem twoMacroFullThreshold_lt_six_mul_five_pow
    {h : ℕ}
    (hh : 3 ≤ h) :
    rootQuotientTwoMacroFullThreshold h < 6 * 5 ^ (h - 1) := by
  have hTwo : h ≠ 2 := by omega
  by_cases hFive : h ≤ 5
  · have hCases : h = 3 ∨ h = 4 ∨ h = 5 := by omega
    rcases hCases with rfl | rfl | rfl <;>
      norm_num [rootQuotientTwoMacroFullThreshold,
        rootQuotientTwoMacroOptimalThreshold,
        rootQuotientFourNineThreshold]
  · have hSix : 6 ≤ h := by omega
    obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hSix
    simp [rootQuotientTwoMacroFullThreshold,
      rootQuotientTwoMacroOptimalThreshold,
      rootQuotientEightNineThreshold, pow_add]
    norm_num
    nlinarith [show 0 < 5 ^ n by positivity]

/-- The two-type divisor-cover frontier lies before the third hard pure-prime
direction. -/
theorem six_mul_five_pow_lt_five_pow_succ
    {h : ℕ}
    (hh : 1 ≤ h) :
    6 * 5 ^ (h - 1) < 5 ^ (h + 1) := by
  rw [show h + 1 = (h - 1) + 2 by omega, pow_add]
  norm_num
  nlinarith [show 0 < 5 ^ (h - 1) by positivity]

/-- **Ordered threshold chain for the first three storage layers.**

For every horizon `h>=3`, pure-direction, mixed divisor-cover, exact budget-two,
and next pure-direction thresholds interlace strictly. -/
theorem threeLayerThresholdChain
    {h : ℕ}
    (hh : 3 ≤ h) :
    2 ^ (h + 1) < 2 * 3 ^ h ∧
    2 * 3 ^ h < 3 ^ (h + 1) ∧
    3 ^ (h + 1) < rootQuotientTwoMacroFullThreshold h ∧
    rootQuotientTwoMacroFullThreshold h < 6 * 5 ^ (h - 1) ∧
    6 * 5 ^ (h - 1) < 5 ^ (h + 1) := by
  exact ⟨
    two_pow_succ_lt_two_mul_three_pow (by omega),
    two_mul_three_pow_lt_three_pow_succ,
    three_pow_succ_lt_twoMacroFullThreshold_of_three_le hh,
    twoMacroFullThreshold_lt_six_mul_five_pow hh,
    six_mul_five_pow_lt_five_pow_succ (by omega)⟩

/-- Exact pure-direction demand in the band between the second and third prime
hard-direction births. -/
theorem primeDirectionDemand_eq_two_of_three_pow_le_of_lt_five_pow
    {N h : ℕ}
    (hLower : 3 ^ (h + 1) ≤ N)
    (hUpper : N < 5 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 2 := by
  have hLeTwo : rootQuotientPrimeDirectionDemand N h ≤ 2 :=
    (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
      (N := N) (h := h) (s := 2)).2 (by
        simpa [rootQuotientStablePrimeBase] using hUpper)
  have hNotLeOne : ¬rootQuotientPrimeDirectionDemand N h ≤ 1 := by
    intro hLe
    have hState :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 1)).1 hLe
    have : N < 3 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase] using hState
    omega
  omega

/-- The explicit transient dictionary `{4,8,9}` is a valid normalized
three-macro presentation below the two-type divisor-cover shell. -/
theorem four_eight_nine_is_compositeMacroPresentation_below_coverThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hN : 9 ≤ N)
    (hBinary : N < 2 ^ r)
    (hBound : N < 6 * 5 ^ (h - 1)) :
    RootQuotientCompositeMacroPresentation
      r N h ({4, 8, 9} : Set ℕ) := by
  have hFourFree : RPowerFree r 4 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 4 ≤ N).trans_lt hBinary)
  have hEightFree : RPowerFree r 8 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 8 ≤ N).trans_lt hBinary)
  have hNineFree : RPowerFree r 9 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hN.trans_lt hBinary)
  refine ⟨by simp, ?_, ?_⟩
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl | rfl
    · exact ⟨⟨by omega, by omega, hFourFree⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by omega, by omega, hEightFree⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by omega, hN, hNineFree⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
  · simpa [RootQuotientPrimeFourEightNineBasis] using
      (primeFourEightNineBasis_separates_iff_stateBound_lt_shell
        (r := r) (N := N) (h := h)
        hr (by omega) hh hBinary).2 hBound

/-- Phase 0: below the first hard prime direction, all three optional-storage
layers vanish. -/
theorem threeLayer_phase_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hUpper : N < 2 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 0 ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h = 0 ∧
    rootQuotientMinimumCompositeMacroCount r N h = 0 ∧
    rootQuotientMixedDivisorCoverOverhead r N h = 0 ∧
    rootQuotientResidualDepthStorageOverhead r N h = 0 := by
  have hMu := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
    hr hN hBinary hUpper
  have hDirLe := primeDirectionDemand_le_minimumCompositeMacroCount
    hr (by omega) hBinary
  have hCoverLe := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hDir : rootQuotientPrimeDirectionDemand N h = 0 := by omega
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 0 := by omega
  refine ⟨hDir, hCover, hMu, ?_, ?_⟩
  · simp [rootQuotientMixedDivisorCoverOverhead, hDir, hCover]
  · simp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap, hMu, hCover]

/-- Phase 1: one hard prime direction and one exact macro type, with no mixed
or residual-depth overhead. -/
theorem threeLayer_phase_one_direction_only
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 ^ (h + 1) ≤ N)
    (hUpper : N < 2 * 3 ^ h) :
    rootQuotientPrimeDirectionDemand N h = 1 ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h = 1 ∧
    rootQuotientMinimumCompositeMacroCount r N h = 1 ∧
    rootQuotientMixedDivisorCoverOverhead r N h = 0 ∧
    rootQuotientResidualDepthStorageOverhead r N h = 0 := by
  have hTri : N < 3 ^ (h + 1) :=
    hUpper.trans (two_mul_three_pow_lt_three_pow_succ)
  have hDir := primeDirectionDemand_eq_one_of_two_pow_le_of_lt_three_pow
    hLower hTri
  have hMu := minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
    hr (by omega) hBinary hLower hUpper
  have hDirLeCover := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    hr (by omega) hBinary
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 1 := by omega
  refine ⟨hDir, hCover, hMu, ?_, ?_⟩
  · simp [rootQuotientMixedDivisorCoverOverhead, hDir, hCover]
  · simp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap, hMu, hCover]

/-- Phase 2: pure direction demand remains one, but mixed divisibility forces a
second macro type.  Divisor cover is already exact, so all mixed overhead is
cover geometry. -/
theorem threeLayer_phase_mixed_cover_only
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 1 ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 ∧
    rootQuotientMinimumCompositeMacroCount r N h = 2 ∧
    rootQuotientMixedDivisorCoverOverhead r N h = 1 ∧
    rootQuotientResidualDepthStorageOverhead r N h = 0 := by
  have hDir := primeDirectionDemand_eq_one_of_two_three_wedge
    (by omega) hLower hUpper
  have hMu := minimumCompositeMacroCount_eq_two_of_two_three_wedge
    hr (by omega) hBinary hLower hUpper
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hNotOne : ¬rootQuotientGlobalRepairDivisorCoverNumber r N h ≤ 1 := by
    intro hOne
    have hBound :=
      (globalRepairDivisorCoverNumber_le_one_iff_stateBound_lt_two_mul_three_pow
        (r := r) (N := N) (h := h)
        hr (by omega) (by omega) hBinary).1 hOne
    omega
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 := by omega
  refine ⟨hDir, hCover, hMu, ?_, ?_⟩
  · simp [rootQuotientMixedDivisorCoverOverhead, hDir, hCover]
  · simp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap, hMu, hCover]

/-- Phase 3: the second pure-prime direction is born and absorbs the preceding
mixed cover overhead.  Both coarse and exact repair frontiers equal two. -/
theorem threeLayer_phase_second_direction_absorbs_cover
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 3 ^ (h + 1) ≤ N)
    (hUpper : N < rootQuotientTwoMacroFullThreshold h) :
    rootQuotientPrimeDirectionDemand N h = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 ∧
    rootQuotientMinimumCompositeMacroCount r N h = 2 ∧
    rootQuotientMixedDivisorCoverOverhead r N h = 0 ∧
    rootQuotientResidualDepthStorageOverhead r N h = 0 := by
  have hChain := threeLayerThresholdChain hh
  have hFiveUpper : N < 5 ^ (h + 1) :=
    hUpper.trans (hChain.2.2.2.2.1.trans hChain.2.2.2.2.2)
  have hDir := primeDirectionDemand_eq_two_of_three_pow_le_of_lt_five_pow
    hLower hFiveUpper
  have hN : 2 ≤ N := by positivity
  have hMuLe :=
    (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
      (r := r) (N := N) (h := h)
      hr (by omega) hN hBinary).2 hUpper
  have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
    hr (by omega) hBinary
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 2 := by omega
  have hDirLeCover := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    hr (by omega) hBinary
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 := by omega
  refine ⟨hDir, hCover, hMu, ?_, ?_⟩
  · simp [rootQuotientMixedDivisorCoverOverhead, hDir, hCover]
  · simp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap, hMu, hCover]

/-- Phase 4: **pure residual-depth strip.**

Two macro types are still sufficient as a divisor hitting set, but no
horizon-`h` compiler can realize the full repair task with only two types.
Exactly one additional type is required purely because of bounded execution
depth. -/
theorem threeLayer_phase_pure_residual_depth
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : rootQuotientTwoMacroFullThreshold h ≤ N)
    (hUpper : N < 6 * 5 ^ (h - 1)) :
    rootQuotientPrimeDirectionDemand N h = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 ∧
    rootQuotientMinimumCompositeMacroCount r N h = 3 ∧
    rootQuotientMixedDivisorCoverOverhead r N h = 0 ∧
    rootQuotientResidualDepthStorageOverhead r N h = 1 := by
  have hChain := threeLayerThresholdChain hh
  have hThreeLower : 3 ^ (h + 1) ≤ N := by
    exact (Nat.le_of_lt hChain.2.2.1).trans hLower
  have hFiveUpper : N < 5 ^ (h + 1) :=
    hUpper.trans hChain.2.2.2.2.2
  have hDir := primeDirectionDemand_eq_two_of_three_pow_le_of_lt_five_pow
    hThreeLower hFiveUpper
  have hCoverLe : rootQuotientGlobalRepairDivisorCoverNumber r N h ≤ 2 :=
    (globalRepairDivisorCoverNumber_le_two_iff_stateBound_lt_six_mul_five_pow
      (r := r) (N := N) (h := h)
      hr hh (by omega) hBinary).2 hUpper
  have hDirLeCover := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    hr (by omega) hBinary
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 2 := by omega
  have hMuNotTwo : ¬rootQuotientMinimumCompositeMacroCount r N h ≤ 2 := by
    intro hMuLe
    have hBelow :=
      (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
        (r := r) (N := N) (h := h)
        hr (by omega) (by omega) hBinary).1 hMuLe
    omega
  have hN9 : 9 ≤ N := by
    have h81 : 81 ≤ 3 ^ (h + 1) := by
      have hPow : 3 ^ 4 ≤ 3 ^ (h + 1) :=
        pow_le_pow_right' (by omega : (1 : ℕ) ≤ 3) (by omega)
      norm_num at hPow ⊢
      exact hPow
    omega
  have hPresentation :=
    four_eight_nine_is_compositeMacroPresentation_below_coverThreshold
      (r := r) (N := N) (h := h)
      hr (by omega) hN9 hBinary hUpper
  have hMuLeThree := rootQuotientMinimumCompositeMacroCount_le hPresentation
  have hCard : ({4, 8, 9} : Set ℕ).ncard = 3 := by norm_num
  rw [hCard] at hMuLeThree
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 3 := by omega
  refine ⟨hDir, hCover, hMu, ?_, ?_⟩
  · simp [rootQuotientMixedDivisorCoverOverhead, hDir, hCover]
  · simp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap, hMu, hCover]

/-- At the next cover threshold the first-order divisor relaxation itself must
jump to at least three types. -/
theorem threeLayer_cover_jumps_at_six_mul_five_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 6 * 5 ^ (h - 1) ≤ N) :
    3 ≤ rootQuotientGlobalRepairDivisorCoverNumber r N h :=
  three_le_globalRepairDivisorCoverNumber_of_six_mul_five_pow_le
    hr hh hBinary hLower

end EnterpriseMath.Quotient
