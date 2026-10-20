import EnterpriseMath.Quotient.RootQuotientCoverCatchupEvent
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A direction-only catch-up (`direction=1`, `cover=0`) can happen only when
there is already at least one unit of mixed-cover gap available to absorb. -/
theorem one_le_mixedDivisorCoverOverhead_of_direction_event_one_cover_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinaryNext : N + 1 < 2 ^ r)
    (hDirEvent : (rootQuotientResourceEvent r N h).direction = 1)
    (hCoverEvent : (rootQuotientResourceEvent r N h).divisorCover = 0) :
    1 ≤ rootQuotientMixedDivisorCoverOverhead r N h := by
  have hDMono := primeDirectionDemand_succ_staircase N h
  have hCMono := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := N) (h := h) hh
  have hNestNext := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    (r := r) (N := N + 1) (h := h) hr hh hBinaryNext
  dsimp [rootQuotientResourceEvent] at hDirEvent hCoverEvent
  dsimp [rootQuotientMixedDivisorCoverOverhead]
  omega

/-- A cover-only catch-up (`cover=1`, `exact=0`) can happen only when there is
already at least one unit of residual-depth gap available to absorb. -/
theorem one_le_residualDepthStorageOverhead_of_cover_event_one_exact_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hCoverEvent : (rootQuotientResourceEvent r N h).divisorCover = 1)
    (hExactEvent : (rootQuotientResourceEvent r N h).exactStorage = 0) :
    1 ≤ rootQuotientResidualDepthStorageOverhead r N h := by
  have hCMono := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := N) (h := h) hh
  have hMM := minimumCompositeMacroCount_succ_staircase
    (r := r) (N := N) (h := h) hr hh
  have hNestNext := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N + 1) (h := h) hr hh
  dsimp [rootQuotientResourceEvent] at hCoverEvent hExactEvent
  dsimp [rootQuotientResidualDepthStorageOverhead,
    rootQuotientGlobalRepairRelaxationGap]
  omega

/-- Event `(1,0,0)` consumes exactly one unit of mixed-cover gap and leaves the
residual-depth gap unchanged. -/
theorem gapFlow_of_directionCatchupEvent
    {r N h : ℕ}
    (hEvent : rootQuotientResourceEvent r N h =
      rootQuotientDirectionCatchupEvent) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h = -1 ∧
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h = 0 := by
  have hCoverFlow := mixedCoverGapInt_succ_sub_eq_event_difference r N h
  have hDepthFlow := residualDepthGapInt_succ_sub_eq_event_difference r N h
  have hDir : (rootQuotientSignedResourceEvent r N h).direction = 1 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hDMono := primeDirectionDemand_succ_staircase N h
    have hComp : (rootQuotientResourceEvent r N h).direction = 1 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hCover : (rootQuotientSignedResourceEvent r N h).divisorCover = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hCMono := globalRepairDivisorCoverNumber_succ_staircase
      (r := r) (N := N) (h := h) (by omega)
    have hComp : (rootQuotientResourceEvent r N h).divisorCover = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hExact : (rootQuotientSignedResourceEvent r N h).exactStorage = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).exactStorage = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  rw [hDir, hCover] at hCoverFlow
  rw [hCover, hExact] at hDepthFlow
  norm_num at hCoverFlow hDepthFlow ⊢
  exact ⟨hCoverFlow, hDepthFlow⟩

/-- Event `(0,1,0)` transfers one unit from residual-depth gap into mixed-cover
gap without changing total exact storage. -/
theorem gapFlow_of_coverCatchupEvent
    {r N h : ℕ}
    (hEvent : rootQuotientResourceEvent r N h =
      rootQuotientCoverCatchupEvent) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h = 1 ∧
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h = -1 := by
  have hCoverFlow := mixedCoverGapInt_succ_sub_eq_event_difference r N h
  have hDepthFlow := residualDepthGapInt_succ_sub_eq_event_difference r N h
  have hDir : (rootQuotientSignedResourceEvent r N h).direction = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hDMono := primeDirectionDemand_succ_staircase N h
    have hComp : (rootQuotientResourceEvent r N h).direction = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hCover : (rootQuotientSignedResourceEvent r N h).divisorCover = 1 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hCMono := globalRepairDivisorCoverNumber_succ_staircase
      (r := r) (N := N) (h := h) (by omega)
    have hComp : (rootQuotientResourceEvent r N h).divisorCover = 1 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hExact : (rootQuotientSignedResourceEvent r N h).exactStorage = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).exactStorage = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  rw [hDir, hCover] at hCoverFlow
  rw [hCover, hExact] at hDepthFlow
  norm_num at hCoverFlow hDepthFlow ⊢
  exact ⟨hCoverFlow, hDepthFlow⟩

/-- Event `(0,1,1)` creates one unit of mixed-cover gap and leaves the depth gap
unchanged. -/
theorem gapFlow_of_mixedCoverBirthEvent
    {r N h : ℕ}
    (hEvent : rootQuotientResourceEvent r N h =
      rootQuotientMixedCoverBirthEvent) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h = 1 ∧
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h = 0 := by
  have hCoverFlow := mixedCoverGapInt_succ_sub_eq_event_difference r N h
  have hDepthFlow := residualDepthGapInt_succ_sub_eq_event_difference r N h
  have hDir : (rootQuotientSignedResourceEvent r N h).direction = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).direction = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hCover : (rootQuotientSignedResourceEvent r N h).divisorCover = 1 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).divisorCover = 1 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hExact : (rootQuotientSignedResourceEvent r N h).exactStorage = 1 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).exactStorage = 1 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  rw [hDir, hCover] at hCoverFlow
  rw [hCover, hExact] at hDepthFlow
  norm_num at hCoverFlow hDepthFlow ⊢
  exact ⟨hCoverFlow, hDepthFlow⟩

/-- Event `(0,0,1)` creates one unit of residual-depth gap and leaves the cover
gap unchanged. -/
theorem gapFlow_of_residualDepthBirthEvent
    {r N h : ℕ}
    (hEvent : rootQuotientResourceEvent r N h =
      rootQuotientResidualDepthBirthEvent) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h = 0 ∧
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h = 1 := by
  have hCoverFlow := mixedCoverGapInt_succ_sub_eq_event_difference r N h
  have hDepthFlow := residualDepthGapInt_succ_sub_eq_event_difference r N h
  have hDir : (rootQuotientSignedResourceEvent r N h).direction = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).direction = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hCover : (rootQuotientSignedResourceEvent r N h).divisorCover = 0 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).divisorCover = 0 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  have hExact : (rootQuotientSignedResourceEvent r N h).exactStorage = 1 := by
    dsimp [rootQuotientSignedResourceEvent]
    have hComp : (rootQuotientResourceEvent r N h).exactStorage = 1 := by
      rw [hEvent]
      rfl
    dsimp [rootQuotientResourceEvent] at hComp
    omega
  rw [hDir, hCover] at hCoverFlow
  rw [hCover, hExact] at hDepthFlow
  norm_num at hCoverFlow hDepthFlow ⊢
  exact ⟨hCoverFlow, hDepthFlow⟩

end EnterpriseMath.Quotient
