import EnterpriseMath.Quotient.RootQuotientResourceEventReconstruction
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Signed total mixed overhead: exact optional-macro storage minus the hard
pure-direction floor. -/
def rootQuotientTotalMixedGapInt
    (r N h : ℕ) : ℤ :=
  (rootQuotientMinimumCompositeMacroCount r N h : ℤ) -
    (rootQuotientPrimeDirectionDemand N h : ℤ)

/-- Total mixed overhead is the sum of mixed-cover and residual-depth gaps. -/
theorem totalMixedGapInt_eq_coverGap_add_depthGap
    (r N h : ℕ) :
    rootQuotientTotalMixedGapInt r N h =
      rootQuotientMixedCoverGapInt r N h +
        rootQuotientResidualDepthGapInt r N h := by
  dsimp [rootQuotientTotalMixedGapInt,
    rootQuotientMixedCoverGapInt,
    rootQuotientResidualDepthGapInt]
  ring

/-- In the high-root regime, the signed total gap is exactly the integer cast of
the natural mixed-direction macro overhead. -/
theorem totalMixedGapInt_eq_mixedDirectionMacroOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientTotalMixedGapInt r N h =
      (rootQuotientMixedDirectionMacroOverhead r N h : ℤ) := by
  have hDecomp := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  dsimp [rootQuotientTotalMixedGapInt]
  omega

/-- **Total mixed-overhead flow law.**

The intermediate divisor-cover layer cancels: total mixed overhead changes only
by the difference between exact-storage and pure-direction event components. -/
theorem totalMixedGapInt_succ_sub_eq_exactEvent_sub_directionEvent
    (r N h : ℕ) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
        rootQuotientTotalMixedGapInt r N h =
      (rootQuotientSignedResourceEvent r N h).exactStorage -
        (rootQuotientSignedResourceEvent r N h).direction := by
  dsimp [rootQuotientTotalMixedGapInt,
    rootQuotientSignedResourceEvent]
  ring

/-- Same flow law expressed through the natural binary event vector under the
staircase hypotheses. -/
theorem totalMixedGapInt_succ_sub_eq_cast_event_difference
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
        rootQuotientTotalMixedGapInt r N h =
      ((rootQuotientResourceEvent r N h).exactStorage : ℤ) -
        ((rootQuotientResourceEvent r N h).direction : ℤ) := by
  rw [totalMixedGapInt_succ_sub_eq_exactEvent_sub_directionEvent]
  have hCast := signedResourceEvent_eq_cast_resourceEvent hr hh
  rw [hCast.1, hCast.2.2]

/-- No-change event. -/
def rootQuotientNoChangeEvent : RootQuotientResourceEvent :=
  ⟨0, 0, 0⟩

/-- Event `(1,1,0)`: both lower layers catch up while exact storage stays
fixed.  If it occurs, one unit of residual-depth overhead is absorbed. -/
def rootQuotientDualCatchupEvent : RootQuotientResourceEvent :=
  ⟨1, 1, 0⟩

/-- The eight binary event vectors are the complete algebraic event alphabet. -/
theorem resourceEvent_eq_one_of_eight
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientResourceEvent r N h = rootQuotientNoChangeEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientResidualDepthBirthEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientCoverCatchupEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientMixedCoverBirthEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientDirectionCatchupEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientDirectionDepthTransferEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent ∨
    rootQuotientResourceEvent r N h = rootQuotientDirectionBirthEvent := by
  have hBits := rootQuotientResourceEvent_components_zero_or_one hr hh
  rcases hBits.1 with hD0 | hD1 <;>
    rcases hBits.2.1 with hC0 | hC1 <;>
      rcases hBits.2.2 with hM0 | hM1
  all_goals
    first
    | left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; right; right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; right; right; right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; right; right; right; right; left
      apply RootQuotientResourceEvent.ext <;> assumption
    | right; right; right; right; right; right; right
      apply RootQuotientResourceEvent.ext <;> assumption

/-- Total mixed overhead is preserved by synchronized direction birth `(1,1,1)`. -/
theorem totalMixedGapFlow_of_directionBirthEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientDirectionBirthEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 0 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientDirectionBirthEvent]

/-- Mixed-cover birth `(0,1,1)` creates one unit of total mixed overhead. -/
theorem totalMixedGapFlow_of_mixedCoverBirthEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientMixedCoverBirthEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 1 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientMixedCoverBirthEvent]

/-- Residual-depth birth `(0,0,1)` also creates one unit of total mixed overhead. -/
theorem totalMixedGapFlow_of_residualDepthBirthEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientResidualDepthBirthEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 1 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientResidualDepthBirthEvent]

/-- Direction catch-up `(1,0,0)` absorbs one unit of total mixed overhead. -/
theorem totalMixedGapFlow_of_directionCatchupEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientDirectionCatchupEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = -1 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientDirectionCatchupEvent]

/-- Cover catch-up `(0,1,0)` preserves total mixed overhead while transferring
one unit from depth gap into cover gap. -/
theorem totalMixedGapFlow_of_coverCatchupEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientCoverCatchupEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 0 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientCoverCatchupEvent]

/-- Direction-to-depth transfer `(1,0,1)` preserves total mixed overhead while
moving one unit from cover gap into depth gap. -/
theorem totalMixedGapFlow_of_directionDepthTransferEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h =
      rootQuotientDirectionDepthTransferEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 0 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientDirectionDepthTransferEvent]

/-- Dual catch-up `(1,1,0)`, if realized, absorbs one unit of total mixed
overhead. -/
theorem totalMixedGapFlow_of_dualCatchupEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = -1 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientDualCatchupEvent]

/-- No-change event preserves total mixed overhead. -/
theorem totalMixedGapFlow_of_noChangeEvent
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientNoChangeEvent) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
      rootQuotientTotalMixedGapInt r N h = 0 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh, hEvent]
  norm_num [rootQuotientNoChangeEvent]

end EnterpriseMath.Quotient
