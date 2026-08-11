import EnterpriseMath.Quotient.RootQuotientRepairPackingStaircase
import EnterpriseMath.Quotient.RootQuotientResourceEvents
import EnterpriseMath.Quotient.RootQuotientFourLayerStorageDecomposition
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Four-layer state-bound resource increment:

`direction -> packing -> divisor cover -> exact storage`.
-/
structure RootQuotientFourLayerResourceEvent where
  direction : ℕ
  packing : ℕ
  divisorCover : ℕ
  exactStorage : ℕ
  deriving DecidableEq, Repr

noncomputable def rootQuotientFourLayerResourceEvent
    (r N h : ℕ) : RootQuotientFourLayerResourceEvent where
  direction :=
    rootQuotientPrimeDirectionDemand (N + 1) h -
      rootQuotientPrimeDirectionDemand N h
  packing :=
    rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h -
      rootQuotientGlobalRepairDivisorPackingNumber r N h
  divisorCover :=
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h -
      rootQuotientGlobalRepairDivisorCoverNumber r N h
  exactStorage :=
    rootQuotientMinimumCompositeMacroCount r (N + 1) h -
      rootQuotientMinimumCompositeMacroCount r N h

/-- Forgetting the packing coordinate recovers the existing three-layer event. -/
def RootQuotientFourLayerResourceEvent.toThreeLayer
    (e : RootQuotientFourLayerResourceEvent) : RootQuotientResourceEvent :=
  ⟨e.direction, e.divisorCover, e.exactStorage⟩

@[simp]
theorem fourLayerResourceEvent_toThreeLayer
    (r N h : ℕ) :
    (rootQuotientFourLayerResourceEvent r N h).toThreeLayer =
      rootQuotientResourceEvent r N h := rfl

/-- **Every four-layer resource coordinate is binary.**

Each fixed-horizon resource frontier is a unit-step staircase in state bound,
so every increment belongs to `{0,1}`. -/
theorem fourLayerResourceEvent_components_zero_or_one
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    ((rootQuotientFourLayerResourceEvent r N h).direction = 0 ∨
      (rootQuotientFourLayerResourceEvent r N h).direction = 1) ∧
    ((rootQuotientFourLayerResourceEvent r N h).packing = 0 ∨
      (rootQuotientFourLayerResourceEvent r N h).packing = 1) ∧
    ((rootQuotientFourLayerResourceEvent r N h).divisorCover = 0 ∨
      (rootQuotientFourLayerResourceEvent r N h).divisorCover = 1) ∧
    ((rootQuotientFourLayerResourceEvent r N h).exactStorage = 0 ∨
      (rootQuotientFourLayerResourceEvent r N h).exactStorage = 1) := by
  have hD := primeDirectionDemand_succ_staircase N h
  have hP := globalRepairDivisorPackingNumber_succ_staircase r N h
  have hC := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := N) (h := h) hh
  have hM := minimumCompositeMacroCount_succ_staircase
    (r := r) (N := N) (h := h) hr hh
  dsimp [rootQuotientFourLayerResourceEvent]
  constructor <;> omega

/-- Signed packing-over-direction gap. -/
def rootQuotientMixedPackingGapInt
    (r N h : ℕ) : ℤ :=
  (rootQuotientGlobalRepairDivisorPackingNumber r N h : ℤ) -
    (rootQuotientPrimeDirectionDemand N h : ℤ)

/-- Signed cover-over-packing coordination gap. -/
def rootQuotientPackingToCoverGapInt
    (r N h : ℕ) : ℤ :=
  (rootQuotientGlobalRepairDivisorCoverNumber r N h : ℤ) -
    (rootQuotientGlobalRepairDivisorPackingNumber r N h : ℤ)

/-- Signed exact-over-cover residual-depth gap, reusing the existing quantity. -/
@[simp]
theorem residualDepthGapInt_eq_fourthGap
    (r N h : ℕ) :
    rootQuotientResidualDepthGapInt r N h =
      (rootQuotientMinimumCompositeMacroCount r N h : ℤ) -
        (rootQuotientGlobalRepairDivisorCoverNumber r N h : ℤ) := rfl

/-- Packing-gap flow is packing event minus direction event. -/
theorem mixedPackingGapInt_succ_sub_eq_event_difference
    (r N h : ℕ) :
    rootQuotientMixedPackingGapInt r (N + 1) h -
        rootQuotientMixedPackingGapInt r N h =
      ((rootQuotientFourLayerResourceEvent r N h).packing : ℤ) -
        ((rootQuotientFourLayerResourceEvent r N h).direction : ℤ) := by
  dsimp [rootQuotientMixedPackingGapInt,
    rootQuotientFourLayerResourceEvent]
  have hD := primeDirectionDemand_succ_staircase N h
  have hP := globalRepairDivisorPackingNumber_succ_staircase r N h
  omega

/-- Cover-coordination gap flow is cover event minus packing event. -/
theorem packingToCoverGapInt_succ_sub_eq_event_difference
    (r N h : ℕ) :
    rootQuotientPackingToCoverGapInt r (N + 1) h -
        rootQuotientPackingToCoverGapInt r N h =
      ((rootQuotientFourLayerResourceEvent r N h).divisorCover : ℤ) -
        ((rootQuotientFourLayerResourceEvent r N h).packing : ℤ) := by
  dsimp [rootQuotientPackingToCoverGapInt,
    rootQuotientFourLayerResourceEvent]
  have hP := globalRepairDivisorPackingNumber_succ_staircase r N h
  have hCMono := globalRepairDivisorCoverNumber_mono_succ
    (r := r) (N := N) (h := h) (by omega)
  have hCStep := globalRepairDivisorCoverNumber_succ_le_add_one
    (r := r) (N := N) (h := h) (by omega)
  omega

/-- Residual-depth gap flow is exact event minus cover event. -/
theorem residualDepthGapInt_succ_sub_eq_fourLayer_event_difference
    (r N h : ℕ) :
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h =
      ((rootQuotientFourLayerResourceEvent r N h).exactStorage : ℤ) -
        ((rootQuotientFourLayerResourceEvent r N h).divisorCover : ℤ) := by
  dsimp [rootQuotientResidualDepthGapInt,
    rootQuotientFourLayerResourceEvent]
  have hCMono := globalRepairDivisorCoverNumber_mono_succ
    (r := r) (N := N) (h := h) (by omega)
  have hCStep := globalRepairDivisorCoverNumber_succ_le_add_one
    (r := r) (N := N) (h := h) (by omega)
  have hMMono := minimumCompositeMacroCount_mono_succ
    (r := r) (N := N) (h := h) (by omega) (by omega)
  have hMStep := minimumCompositeMacroCount_succ_le_add_one
    (r := r) (N := N) (h := h) (by omega) (by omega)
  omega

/-- The old mixed-cover gap is exactly packing pressure plus cover coordination. -/
theorem mixedCoverGapInt_eq_mixedPacking_add_packingToCover
    (r N h : ℕ) :
    rootQuotientMixedCoverGapInt r N h =
      rootQuotientMixedPackingGapInt r N h +
        rootQuotientPackingToCoverGapInt r N h := by
  dsimp [rootQuotientMixedCoverGapInt,
    rootQuotientMixedPackingGapInt,
    rootQuotientPackingToCoverGapInt]
  ring

/-- Total exact optional storage flow is direction flow plus the three internal
gap flows. -/
theorem exactStorageEvent_eq_direction_add_fourLayerGapFlows
    (r N h : ℕ) :
    ((rootQuotientFourLayerResourceEvent r N h).exactStorage : ℤ) =
      ((rootQuotientFourLayerResourceEvent r N h).direction : ℤ) +
      (rootQuotientMixedPackingGapInt r (N + 1) h -
        rootQuotientMixedPackingGapInt r N h) +
      (rootQuotientPackingToCoverGapInt r (N + 1) h -
        rootQuotientPackingToCoverGapInt r N h) +
      (rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h) := by
  rw [mixedPackingGapInt_succ_sub_eq_event_difference,
    packingToCoverGapInt_succ_sub_eq_event_difference,
    residualDepthGapInt_succ_sub_eq_fourLayer_event_difference]
  ring

end EnterpriseMath.Quotient
