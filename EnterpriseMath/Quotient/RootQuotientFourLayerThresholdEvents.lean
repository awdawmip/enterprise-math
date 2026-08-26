import EnterpriseMath.Quotient.RootQuotientPackingThresholdEvents
import EnterpriseMath.Quotient.RootQuotientCoverCatchupEvent
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- First hard-direction birth: all four resource layers rise together. -/
def rootQuotientFourLayerDirectionBirthEvent : RootQuotientFourLayerResourceEvent :=
  ⟨1, 1, 1, 1⟩

/-- First mixed incompatibility birth: packing, cover, and exact storage rise
while pure-direction demand stays fixed. -/
def rootQuotientFourLayerMixedPackingBirthEvent : RootQuotientFourLayerResourceEvent :=
  ⟨0, 1, 1, 1⟩

/-- Pure-direction catch-up: only direction demand rises. -/
def rootQuotientFourLayerDirectionCatchupEvent : RootQuotientFourLayerResourceEvent :=
  ⟨1, 0, 0, 0⟩

/-- Pure residual-depth birth: only exact storage rises. -/
def rootQuotientFourLayerResidualDepthBirthEvent : RootQuotientFourLayerResourceEvent :=
  ⟨0, 0, 0, 1⟩

/-- Packing-certified cover catch-up: packing and cover rise together while
exact storage is already one level ahead. -/
def rootQuotientFourLayerPackingCoverCatchupEvent : RootQuotientFourLayerResourceEvent :=
  ⟨0, 1, 1, 0⟩

/-- Helper: when pure-direction demand and divisor-cover number coincide, the
intermediate packing number has the same value. -/
theorem globalRepairPacking_eq_of_direction_eq_cover
    {r N h k : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hDir : rootQuotientPrimeDirectionDemand N h = k)
    (hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = k) :
    rootQuotientGlobalRepairDivisorPackingNumber r N h = k := by
  have hHierarchy := canonicalRepairFourLayerHierarchy hr hh hBinary
  omega

/-- **Four-layer first mixed event.**

At `N=2*3^h`, a mixed target enters that is divisor-incompatible with the
existing pure-2 hard target.  Packing, cover, and exact storage therefore rise
together: `(0,1,1,1)`. -/
theorem fourLayerResourceEvent_at_firstMixedThreshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 2 * 3 ^ h < 2 ^ r) :
    rootQuotientFourLayerResourceEvent r (2 * 3 ^ h - 1) h =
      rootQuotientFourLayerMixedPackingBirthEvent := by
  let T := 2 * 3 ^ h
  have hChain := threeLayerThresholdChain hh
  have hPrevBinary : T - 1 < 2 ^ r := by omega
  have hPrev := threeLayer_phase_one_direction_only
    (r := r) (N := T - 1) (h := h)
    hr hh hPrevBinary (by
      dsimp [T]
      have hStrict := hChain.1
      omega) (by dsimp [T]; omega)
  have hPrevPack := globalRepairPacking_eq_of_direction_eq_cover
    hr (by omega) hPrevBinary hPrev.1 hPrev.2.1
  have hAt := threeLayer_phase_mixed_cover_only
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.1)
  have hPackLower := two_le_globalRepairPacking_at_firstMixedThreshold
    (r := r) (h := h) hr (by omega) hBinary
  have hPackUpper :
      rootQuotientGlobalRepairDivisorPackingNumber r T h ≤ 2 := by
    have hHierarchy := canonicalRepairFourLayerHierarchy
      (r := r) (N := T) (h := h) hr (by omega) (by simpa [T] using hBinary)
    rw [hAt.2.1] at hHierarchy
    exact hHierarchy.2.1
  have hAtPack : rootQuotientGlobalRepairDivisorPackingNumber r T h = 2 := by omega
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by dsimp [T]; positivity
    omega
  dsimp [rootQuotientFourLayerResourceEvent,
    rootQuotientFourLayerMixedPackingBirthEvent]
  rw [show 2 * 3 ^ h = T by rfl, hSucc,
    hPrev.1, hPrevPack, hPrev.2.1, hPrev.2.2.1,
    hAt.1, hAtPack, hAt.2.1, hAt.2.2.1]
  rfl

/-- **Four-layer second prime-direction birth.**

At `3^(h+1)` the new pure direction catches up with already-present mixed
packing pressure.  Packing, cover, and exact storage stay fixed: `(1,0,0,0)`. -/
theorem fourLayerResourceEvent_at_secondDirectionThreshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 3 ^ (h + 1) < 2 ^ r) :
    rootQuotientFourLayerResourceEvent r (3 ^ (h + 1) - 1) h =
      rootQuotientFourLayerDirectionCatchupEvent := by
  let T := 3 ^ (h + 1)
  let M := 2 * 3 ^ h
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_mixed_cover_only
    (r := r) (N := T - 1) (h := h)
    hr hh (by dsimp [T]; omega) (by
      dsimp [T, M]
      have hStrict := hChain.2.1
      omega) (by dsimp [T]; omega)
  have hMPack : 2 ≤ rootQuotientGlobalRepairDivisorPackingNumber r M h :=
    two_le_globalRepairPacking_at_firstMixedThreshold
      (r := r) (h := h) hr (by omega) (by
        dsimp [M]
        exact (hChain.2.1.trans_lt hBinary))
  have hMLePrev : M ≤ T - 1 := by
    dsimp [M, T]
    have hStrict := hChain.2.1
    omega
  have hPrevPackLower : 2 ≤
      rootQuotientGlobalRepairDivisorPackingNumber r (T - 1) h :=
    hMPack.trans (globalRepairDivisorPackingNumber_mono_stateBound hMLePrev)
  have hPrevPackUpper :
      rootQuotientGlobalRepairDivisorPackingNumber r (T - 1) h ≤ 2 := by
    have hHierarchy := canonicalRepairFourLayerHierarchy
      (r := r) (N := T - 1) (h := h)
      hr (by omega) (by dsimp [T]; omega)
    rw [hPrev.2.1] at hHierarchy
    exact hHierarchy.2.1
  have hPrevPack : rootQuotientGlobalRepairDivisorPackingNumber r (T - 1) h = 2 := by
    omega
  have hAt := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.1)
  have hAtPack := globalRepairPacking_eq_of_direction_eq_cover
    hr (by omega) (by simpa [T] using hBinary) hAt.1 hAt.2.1
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by dsimp [T]; positivity
    omega
  dsimp [rootQuotientFourLayerResourceEvent,
    rootQuotientFourLayerDirectionCatchupEvent]
  rw [show 3 ^ (h + 1) = T by rfl, hSucc,
    hPrev.1, hPrevPack, hPrev.2.1, hPrev.2.2.1,
    hAt.1, hAtPack, hAt.2.1, hAt.2.2.1]
  rfl

/-- **Four-layer exact compiler birth.**

At the global budget-two exact threshold, direction, packing, and divisor-cover
layers stay at two while exact storage rises to three: `(0,0,0,1)`. -/
theorem fourLayerResourceEvent_at_budgetTwoExactThreshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : rootQuotientTwoMacroFullThreshold h < 2 ^ r) :
    rootQuotientFourLayerResourceEvent r
        (rootQuotientTwoMacroFullThreshold h - 1) h =
      rootQuotientFourLayerResidualDepthBirthEvent := by
  let T := rootQuotientTwoMacroFullThreshold h
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T - 1) (h := h)
    hr hh (by dsimp [T]; omega) (by
      dsimp [T]
      have hStrict := hChain.2.2.1
      omega) (by dsimp [T]; omega)
  have hPrevPack := globalRepairPacking_eq_of_direction_eq_cover
    hr (by omega) (by dsimp [T]; omega) hPrev.1 hPrev.2.1
  have hAt := threeLayer_phase_pure_residual_depth
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.2.1)
  have hAtPack := globalRepairPacking_eq_of_direction_eq_cover
    hr (by omega) (by simpa [T] using hBinary) hAt.1 hAt.2.1
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by
      dsimp [T]
      have hLower := hChain.2.2.1
      omega
    omega
  dsimp [rootQuotientFourLayerResourceEvent,
    rootQuotientFourLayerResidualDepthBirthEvent]
  rw [hSucc,
    hPrev.1, hPrevPack, hPrev.2.1, hPrev.2.2.1,
    hAt.1, hAtPack, hAt.2.1, hAt.2.2.1]
  rfl

/-- **Four-layer stable cover catch-up.**

At `6*5^(h-1)` in the proved stable budget-three regime, a third pairwise
incompatible hard target appears.  Packing and cover rise together while exact
storage remains three: `(0,1,1,0)`. -/
theorem fourLayerResourceEvent_at_twoCoverThreshold_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    rootQuotientFourLayerResourceEvent r (6 * 5 ^ (h - 1) - 1) h =
      rootQuotientFourLayerPackingCoverCatchupEvent := by
  let T := 6 * 5 ^ (h - 1)
  have hh : 3 ≤ h := by omega
  have hBefore := resources_before_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hBeforePack := globalRepairPacking_eq_of_direction_eq_cover
    hr (by omega) (by dsimp [T]; omega) hBefore.1 hBefore.2.1
  have hAt := resources_at_twoCoverThreshold_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hPackLower := three_le_globalRepairPacking_at_twoCoverThreshold
    (r := r) (h := h) hr hh hBinary
  have hPackUpper : rootQuotientGlobalRepairDivisorPackingNumber r T h ≤ 3 := by
    have hHierarchy := canonicalRepairFourLayerHierarchy
      (r := r) (N := T) (h := h)
      hr (by omega) (by simpa [T] using hBinary)
    rw [hAt.2.1] at hHierarchy
    exact hHierarchy.2.1
  have hAtPack : rootQuotientGlobalRepairDivisorPackingNumber r T h = 3 := by
    omega
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by dsimp [T]; positivity
    omega
  dsimp [rootQuotientFourLayerResourceEvent,
    rootQuotientFourLayerPackingCoverCatchupEvent]
  rw [show 6 * 5 ^ (h - 1) = T by rfl, hSucc,
    hBefore.1, hBeforePack, hBefore.2.1, hBefore.2.2,
    hAt.1, hAtPack, hAt.2.1, hAt.2.2]
  rfl

end EnterpriseMath.Quotient
