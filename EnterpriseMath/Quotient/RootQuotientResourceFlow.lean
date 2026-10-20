import EnterpriseMath.Quotient.RootQuotientResourceEvents
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Signed first-order mixed-cover gap `tau_global - d_dir`. -/
def rootQuotientMixedCoverGapInt
    (r N h : ℕ) : ℤ :=
  (rootQuotientGlobalRepairDivisorCoverNumber r N h : ℤ) -
    (rootQuotientPrimeDirectionDemand N h : ℤ)

/-- Signed residual-depth gap `mu - tau_global`. -/
def rootQuotientResidualDepthGapInt
    (r N h : ℕ) : ℤ :=
  (rootQuotientMinimumCompositeMacroCount r N h : ℤ) -
    (rootQuotientGlobalRepairDivisorCoverNumber r N h : ℤ)

/-- Signed resource increment at `N -> N+1`. -/
structure RootQuotientSignedResourceEvent where
  direction : ℤ
  divisorCover : ℤ
  exactStorage : ℤ
  deriving DecidableEq, Repr

noncomputable def rootQuotientSignedResourceEvent
    (r N h : ℕ) : RootQuotientSignedResourceEvent where
  direction :=
    (rootQuotientPrimeDirectionDemand (N + 1) h : ℤ) -
      (rootQuotientPrimeDirectionDemand N h : ℤ)
  divisorCover :=
    (rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h : ℤ) -
      (rootQuotientGlobalRepairDivisorCoverNumber r N h : ℤ)
  exactStorage :=
    (rootQuotientMinimumCompositeMacroCount r (N + 1) h : ℤ) -
      (rootQuotientMinimumCompositeMacroCount r N h : ℤ)

/-- In the high-root regime the signed mixed-cover gap is nonnegative. -/
theorem mixedCoverGapInt_nonneg
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    0 ≤ rootQuotientMixedCoverGapInt r N h := by
  have hLe := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    (r := r) (N := N) (h := h) hr hh hBinary
  dsimp [rootQuotientMixedCoverGapInt]
  exact_mod_cast hLe

/-- The signed residual-depth gap is always nonnegative at positive horizon. -/
theorem residualDepthGapInt_nonneg
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    0 ≤ rootQuotientResidualDepthGapInt r N h := by
  have hLe := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr hh
  dsimp [rootQuotientResidualDepthGapInt]
  exact_mod_cast hLe

/-- **Exact mixed-cover flow law.**

The change of the cover-over-direction gap is the difference between the cover
and direction event components. -/
theorem mixedCoverGapInt_succ_sub_eq_event_difference
    (r N h : ℕ) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h =
      (rootQuotientSignedResourceEvent r N h).divisorCover -
        (rootQuotientSignedResourceEvent r N h).direction := by
  dsimp [rootQuotientMixedCoverGapInt,
    rootQuotientSignedResourceEvent]
  ring

/-- **Exact residual-depth flow law.**

The change of the exact-over-cover gap is the difference between exact-storage
and divisor-cover event components. -/
theorem residualDepthGapInt_succ_sub_eq_event_difference
    (r N h : ℕ) :
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h =
      (rootQuotientSignedResourceEvent r N h).exactStorage -
        (rootQuotientSignedResourceEvent r N h).divisorCover := by
  dsimp [rootQuotientResidualDepthGapInt,
    rootQuotientSignedResourceEvent]
  ring

/-- Total optional storage flow is the sum of direction flow plus both signed
gap flows. -/
theorem exactStorageEvent_eq_direction_add_gapFlows
    (r N h : ℕ) :
    (rootQuotientSignedResourceEvent r N h).exactStorage =
      (rootQuotientSignedResourceEvent r N h).direction +
      (rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h) +
      (rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h) := by
  rw [mixedCoverGapInt_succ_sub_eq_event_difference,
    residualDepthGapInt_succ_sub_eq_event_difference]
  ring

/-- At the first mixed-cover event, the cover gap increases by one while the
depth gap stays unchanged. -/
theorem gapFlow_at_first_mixed_cover_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 2 * 3 ^ h < 2 ^ r) :
    rootQuotientMixedCoverGapInt r (2 * 3 ^ h) h -
        rootQuotientMixedCoverGapInt r (2 * 3 ^ h - 1) h = 1 ∧
    rootQuotientResidualDepthGapInt r (2 * 3 ^ h) h -
        rootQuotientResidualDepthGapInt r (2 * 3 ^ h - 1) h = 0 := by
  let T := 2 * 3 ^ h
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_one_direction_only
    (r := r) (N := T - 1) (h := h)
    hr hh (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega)
  have hRight := threeLayer_phase_mixed_cover_only
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.1)
  dsimp [rootQuotientMixedCoverGapInt,
    rootQuotientResidualDepthGapInt]
  rw [show T = 2 * 3 ^ h by rfl,
    hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  norm_num

/-- At the second pure-direction birth, one unit of cover overhead is absorbed
without changing cover or exact storage. -/
theorem gapFlow_at_second_direction_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 3 ^ (h + 1) < 2 ^ r) :
    rootQuotientMixedCoverGapInt r (3 ^ (h + 1)) h -
        rootQuotientMixedCoverGapInt r (3 ^ (h + 1) - 1) h = -1 ∧
    rootQuotientResidualDepthGapInt r (3 ^ (h + 1)) h -
        rootQuotientResidualDepthGapInt r (3 ^ (h + 1) - 1) h = 0 := by
  let T := 3 ^ (h + 1)
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_mixed_cover_only
    (r := r) (N := T - 1) (h := h)
    hr hh (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega)
  have hRight := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.1)
  dsimp [rootQuotientMixedCoverGapInt,
    rootQuotientResidualDepthGapInt]
  rw [show T = 3 ^ (h + 1) by rfl,
    hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  norm_num

/-- At the budget-two exact compiler threshold, divisibility geometry is
unchanged while the residual-depth gap increases by one. -/
theorem gapFlow_at_budgetTwo_exact_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : rootQuotientTwoMacroFullThreshold h < 2 ^ r) :
    rootQuotientMixedCoverGapInt r
        (rootQuotientTwoMacroFullThreshold h) h -
        rootQuotientMixedCoverGapInt r
          (rootQuotientTwoMacroFullThreshold h - 1) h = 0 ∧
    rootQuotientResidualDepthGapInt r
        (rootQuotientTwoMacroFullThreshold h) h -
        rootQuotientResidualDepthGapInt r
          (rootQuotientTwoMacroFullThreshold h - 1) h = 1 := by
  let T := rootQuotientTwoMacroFullThreshold h
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T - 1) (h := h)
    hr hh (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega) (by
      dsimp [T]
      omega)
  have hRight := threeLayer_phase_pure_residual_depth
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.2.1)
  dsimp [rootQuotientMixedCoverGapInt,
    rootQuotientResidualDepthGapInt]
  rw [show T = rootQuotientTwoMacroFullThreshold h by rfl,
    hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  norm_num

end EnterpriseMath.Quotient
