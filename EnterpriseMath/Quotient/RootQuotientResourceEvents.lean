import EnterpriseMath.Quotient.RootQuotientMacroStorageStaircase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Unit state-bound increment of the three nested optional-storage frontiers. -/
structure RootQuotientResourceEvent where
  direction : ℕ
  divisorCover : ℕ
  exactStorage : ℕ
  deriving DecidableEq, Repr

/-- Resource-event vector at the transition `N -> N+1`. -/
noncomputable def rootQuotientResourceEvent
    (r N h : ℕ) : RootQuotientResourceEvent where
  direction :=
    rootQuotientPrimeDirectionDemand (N + 1) h -
      rootQuotientPrimeDirectionDemand N h
  divisorCover :=
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h -
      rootQuotientGlobalRepairDivisorCoverNumber r N h
  exactStorage :=
    rootQuotientMinimumCompositeMacroCount r (N + 1) h -
      rootQuotientMinimumCompositeMacroCount r N h

/-- Every resource-event component is binary. -/
theorem rootQuotientResourceEvent_components_le_one
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    (rootQuotientResourceEvent r N h).direction ≤ 1 ∧
    (rootQuotientResourceEvent r N h).divisorCover ≤ 1 ∧
    (rootQuotientResourceEvent r N h).exactStorage ≤ 1 := by
  have hD := primeDirectionDemand_succ_staircase N h
  have hC := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := N) (h := h) hh
  have hM := minimumCompositeMacroCount_succ_staircase
    (r := r) (N := N) (h := h) hr hh
  dsimp [rootQuotientResourceEvent]
  omega

/-- Each component is literally zero or one. -/
theorem rootQuotientResourceEvent_components_zero_or_one
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    ((rootQuotientResourceEvent r N h).direction = 0 ∨
      (rootQuotientResourceEvent r N h).direction = 1) ∧
    ((rootQuotientResourceEvent r N h).divisorCover = 0 ∨
      (rootQuotientResourceEvent r N h).divisorCover = 1) ∧
    ((rootQuotientResourceEvent r N h).exactStorage = 0 ∨
      (rootQuotientResourceEvent r N h).exactStorage = 1) := by
  have h := rootQuotientResourceEvent_components_le_one hr hh
  omega

/-- Event type `(1,1,1)`: a new hard pure-prime direction is born and all three
storage layers rise together. -/
def rootQuotientDirectionBirthEvent : RootQuotientResourceEvent :=
  ⟨1, 1, 1⟩

/-- Event type `(0,1,1)`: no new pure direction, but a mixed divisor obstruction
forces one more cover type and exact storage follows it. -/
def rootQuotientMixedCoverBirthEvent : RootQuotientResourceEvent :=
  ⟨0, 1, 1⟩

/-- Event type `(1,0,0)`: a new pure direction is born while upper storage stays
fixed, absorbing one unit of previously mixed cover overhead. -/
def rootQuotientDirectionCatchupEvent : RootQuotientResourceEvent :=
  ⟨1, 0, 0⟩

/-- Event type `(0,0,1)`: divisibility geometry is unchanged, but bounded-depth
execution forces one extra stored type. -/
def rootQuotientResidualDepthBirthEvent : RootQuotientResourceEvent :=
  ⟨0, 0, 1⟩

/-- First universal event: at state `2^(h+1)` all three resource layers jump
from zero to one. -/
theorem resourceEvent_at_first_direction_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 2 ^ (h + 1) < 2 ^ r) :
    rootQuotientResourceEvent r (2 ^ (h + 1) - 1) h =
      rootQuotientDirectionBirthEvent := by
  let T := 2 ^ (h + 1)
  have hT : T = 2 ^ (h + 1) := rfl
  have hTTwo : 2 ≤ T := by
    dsimp [T]
    have hBase : 2 ≤ 2 ^ (h + 1) := le_self_pow (by omega) (by omega)
    exact hBase
  have hPrevTwo : 2 ≤ T - 1 := by
    dsimp [T]
    have h16 : 16 ≤ 2 ^ (h + 1) := by
      have hPow : 2 ^ 4 ≤ 2 ^ (h + 1) :=
        pow_le_pow_right' (by omega : (1 : ℕ) ≤ 2) (by omega)
      norm_num at hPow
      exact hPow
    omega
  have hPrevBinary : T - 1 < 2 ^ r := by omega
  have hPrev := threeLayer_phase_zero
    (r := r) (N := T - 1) (h := h)
    hr hh hPrevTwo hPrevBinary (by omega)
  have hChain := threeLayerThresholdChain hh
  have hRight := threeLayer_phase_one_direction_only
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.1)
  have hSucc : (T - 1) + 1 = T := by omega
  dsimp [rootQuotientResourceEvent,
    rootQuotientDirectionBirthEvent]
  rw [hSucc, hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  rfl

/-- Second universal event: the first mixed divisor obstruction raises cover and
exact storage while pure-direction demand remains one. -/
theorem resourceEvent_at_first_mixed_cover_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 2 * 3 ^ h < 2 ^ r) :
    rootQuotientResourceEvent r (2 * 3 ^ h - 1) h =
      rootQuotientMixedCoverBirthEvent := by
  let T := 2 * 3 ^ h
  have hChain := threeLayerThresholdChain hh
  have hPrevBinary : T - 1 < 2 ^ r := by omega
  have hPrev := threeLayer_phase_one_direction_only
    (r := r) (N := T - 1) (h := h)
    hr hh hPrevBinary (by
      dsimp [T]
      omega) (by omega)
  have hRight := threeLayer_phase_mixed_cover_only
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.1)
  have hSucc : (T - 1) + 1 = T := by
    dsimp [T]
    positivity
  dsimp [rootQuotientResourceEvent,
    rootQuotientMixedCoverBirthEvent]
  rw [hSucc, hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  rfl

/-- Third universal event: at `3^(h+1)` the second pure direction is born but
cover/exact storage stay at two, so one unit of mixed-cover overhead is
absorbed. -/
theorem resourceEvent_at_second_direction_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 3 ^ (h + 1) < 2 ^ r) :
    rootQuotientResourceEvent r (3 ^ (h + 1) - 1) h =
      rootQuotientDirectionCatchupEvent := by
  let T := 3 ^ (h + 1)
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_mixed_cover_only
    (r := r) (N := T - 1) (h := h)
    hr hh (by omega) (by
      dsimp [T]
      omega) (by omega)
  have hRight := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.1)
  have hSucc : (T - 1) + 1 = T := by
    dsimp [T]
    positivity
  dsimp [rootQuotientResourceEvent,
    rootQuotientDirectionCatchupEvent]
  rw [hSucc, hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  rfl

/-- Fourth universal event: at the exact budget-two compiler threshold, only
exact storage jumps; the directional and divisor-cover layers remain two. -/
theorem resourceEvent_at_budgetTwo_exact_threshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : rootQuotientTwoMacroFullThreshold h < 2 ^ r) :
    rootQuotientResourceEvent r
        (rootQuotientTwoMacroFullThreshold h - 1) h =
      rootQuotientResidualDepthBirthEvent := by
  let T := rootQuotientTwoMacroFullThreshold h
  have hChain := threeLayerThresholdChain hh
  have hPrev := threeLayer_phase_second_direction_absorbs_cover
    (r := r) (N := T - 1) (h := h)
    hr hh (by omega) (by
      dsimp [T]
      omega) (by omega)
  have hRight := threeLayer_phase_pure_residual_depth
    (r := r) (N := T) (h := h)
    hr hh (by simpa [T] using hBinary) (by simp [T]) (by
      dsimp [T]
      exact hChain.2.2.2.1)
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by
      dsimp [T]
      have hLower := hChain.2.2.1
      positivity
    omega
  dsimp [rootQuotientResourceEvent,
    rootQuotientResidualDepthBirthEvent]
  rw [hSucc, hPrev.1, hPrev.2.1, hPrev.2.2.1,
    hRight.1, hRight.2.1, hRight.2.2.1]
  rfl

end EnterpriseMath.Quotient
