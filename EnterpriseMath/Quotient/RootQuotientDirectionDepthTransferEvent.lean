import EnterpriseMath.Quotient.RootQuotientResourceEventLegality
import EnterpriseMath.Quotient.RootQuotientOrthogonalMixedOverheads
import EnterpriseMath.Quotient.RootQuotientDivisorCoverFrontier
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Event type `(1,0,1)`: a new pure direction is born, the divisor-cover layer
stays fixed, and exact storage rises.  One unit of mixed-cover overhead is
therefore converted into residual-depth overhead. -/
def rootQuotientDirectionDepthTransferEvent : RootQuotientResourceEvent :=
  ⟨1, 0, 1⟩

/-- Resource state immediately before the `N=27,h=2` transfer event. -/
theorem resources_5_26_2_eq_one_two_two :
    rootQuotientPrimeDirectionDemand 26 2 = 1 ∧
    rootQuotientGlobalRepairDivisorCoverNumber 5 26 2 = 2 ∧
    rootQuotientMinimumCompositeMacroCount 5 26 2 = 2 := by
  have hDir := primeDirectionDemand_eq_one_of_two_three_wedge
    (by norm_num : (2 : ℕ) ≥ 2)
    (by norm_num : 2 * 3 ^ 2 ≤ 26)
    (by norm_num : 26 < 3 ^ (2 + 1))
  have hMu := minimumCompositeMacroCount_eq_two_of_two_three_wedge
    (r := 5) (N := 26) (h := 2)
    (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num)
  have hCoverLe := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := 5) (N := 26) (h := 2) (by norm_num) (by norm_num)
  have hCoverNotOne :
      ¬rootQuotientGlobalRepairDivisorCoverNumber 5 26 2 ≤ 1 := by
    intro hLe
    have hBound :=
      (globalRepairDivisorCoverNumber_le_one_iff_stateBound_lt_two_mul_three_pow
        (r := 5) (N := 26) (h := 2)
        (by norm_num) (by norm_num) (by norm_num) (by norm_num)).1 hLe
    norm_num at hBound
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber 5 26 2 = 2 := by
    rw [hMu] at hCoverLe
    omega
  exact ⟨hDir, hCover, hMu⟩

/-- Resource state at `N=27,h=2`, already identified as the pure residual-depth
strict witness. -/
theorem resources_5_27_2_eq_two_two_three :
    rootQuotientPrimeDirectionDemand 27 2 = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber 5 27 2 = 2 ∧
    rootQuotientMinimumCompositeMacroCount 5 27 2 = 3 :=
  ⟨primeDirectionDemand_27_2_eq_two,
    globalRepairDivisorCoverNumber_5_27_2_eq_two,
    minimumCompositeMacroCount_5_27_2_eq_three⟩

/-- **Concrete sixth nontrivial resource event.**

At `(r,h,N->N+1)=(5,2,26->27)` the event is `(1,0,1)`: a new hard 3-direction
appears, divisor-cover storage stays at two, and exact storage rises to three. -/
theorem resourceEvent_5_26_2_eq_directionDepthTransfer :
    rootQuotientResourceEvent 5 26 2 =
      rootQuotientDirectionDepthTransferEvent := by
  have hBefore := resources_5_26_2_eq_one_two_two
  have hAfter := resources_5_27_2_eq_two_two_three
  dsimp [rootQuotientResourceEvent,
    rootQuotientDirectionDepthTransferEvent]
  norm_num
  rw [hBefore.1, hBefore.2.1, hBefore.2.2,
    hAfter.1, hAfter.2.1, hAfter.2.2]
  rfl

/-- At the `(1,0,1)` event, one unit of cover overhead is converted into one
unit of residual-depth overhead. -/
theorem gapFlow_5_26_2_directionDepthTransfer :
    rootQuotientMixedCoverGapInt 5 27 2 -
        rootQuotientMixedCoverGapInt 5 26 2 = -1 ∧
    rootQuotientResidualDepthGapInt 5 27 2 -
        rootQuotientResidualDepthGapInt 5 26 2 = 1 := by
  have hEvent := resourceEvent_5_26_2_eq_directionDepthTransfer
  have hCast := signedResourceEvent_eq_cast_resourceEvent
    (r := 5) (N := 26) (h := 2) (by norm_num) (by norm_num)
  have hCoverFlow := mixedCoverGapInt_succ_sub_eq_event_difference 5 26 2
  have hDepthFlow := residualDepthGapInt_succ_sub_eq_event_difference 5 26 2
  have hDirNat : (rootQuotientResourceEvent 5 26 2).direction = 1 := by
    rw [hEvent]
    rfl
  have hCoverNat : (rootQuotientResourceEvent 5 26 2).divisorCover = 0 := by
    rw [hEvent]
    rfl
  have hExactNat : (rootQuotientResourceEvent 5 26 2).exactStorage = 1 := by
    rw [hEvent]
    rfl
  have hDir : (rootQuotientSignedResourceEvent 5 26 2).direction = 1 := by
    rw [hCast.1, hDirNat]
    norm_num
  have hCover : (rootQuotientSignedResourceEvent 5 26 2).divisorCover = 0 := by
    rw [hCast.2.1, hCoverNat]
    norm_num
  have hExact : (rootQuotientSignedResourceEvent 5 26 2).exactStorage = 1 := by
    rw [hCast.2.2, hExactNat]
    norm_num
  rw [hDir, hCover] at hCoverFlow
  rw [hCover, hExact] at hDepthFlow
  norm_num at hCoverFlow hDepthFlow ⊢
  exact ⟨hCoverFlow, hDepthFlow⟩

end EnterpriseMath.Quotient
