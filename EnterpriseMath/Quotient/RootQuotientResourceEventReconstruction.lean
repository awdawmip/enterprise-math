import EnterpriseMath.Quotient.RootQuotientDirectionDepthTransferEvent
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Absolute three-layer optional-storage state at one bounded state range. -/
structure RootQuotientResourceState where
  direction : ℕ
  divisorCover : ℕ
  exactStorage : ℕ
  deriving DecidableEq, Repr

noncomputable def rootQuotientResourceState
    (r N h : ℕ) : RootQuotientResourceState where
  direction := rootQuotientPrimeDirectionDemand N h
  divisorCover := rootQuotientGlobalRepairDivisorCoverNumber r N h
  exactStorage := rootQuotientMinimumCompositeMacroCount r N h

/-- The direction component is reconstructed exactly by adding the unit event. -/
theorem direction_state_succ_eq_add_event
    (r N h : ℕ) :
    (rootQuotientResourceState r (N + 1) h).direction =
      (rootQuotientResourceState r N h).direction +
        (rootQuotientResourceEvent r N h).direction := by
  have hMono := primeDirectionDemand_succ_staircase N h
  dsimp [rootQuotientResourceState, rootQuotientResourceEvent]
  omega

/-- The divisor-cover component is reconstructed exactly by adding its event
component. -/
theorem divisorCover_state_succ_eq_add_event
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    (rootQuotientResourceState r (N + 1) h).divisorCover =
      (rootQuotientResourceState r N h).divisorCover +
        (rootQuotientResourceEvent r N h).divisorCover := by
  have hMono := globalRepairDivisorCoverNumber_succ_staircase
    (r := r) (N := N) (h := h) hh
  dsimp [rootQuotientResourceState, rootQuotientResourceEvent]
  omega

/-- The exact optional-macro component is reconstructed exactly by adding its
event component. -/
theorem exactStorage_state_succ_eq_add_event
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    (rootQuotientResourceState r (N + 1) h).exactStorage =
      (rootQuotientResourceState r N h).exactStorage +
        (rootQuotientResourceEvent r N h).exactStorage := by
  have hMono := minimumCompositeMacroCount_succ_staircase
    (r := r) (N := N) (h := h) hr hh
  dsimp [rootQuotientResourceState, rootQuotientResourceEvent]
  omega

/-- **Resource event = exact discrete derivative.**

All three resource coordinates reconstruct simultaneously from the previous
state plus the event vector. -/
theorem resourceState_succ_reconstructs_from_event
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientResourceState r (N + 1) h =
      { direction :=
          (rootQuotientResourceState r N h).direction +
            (rootQuotientResourceEvent r N h).direction
        divisorCover :=
          (rootQuotientResourceState r N h).divisorCover +
            (rootQuotientResourceEvent r N h).divisorCover
        exactStorage :=
          (rootQuotientResourceState r N h).exactStorage +
            (rootQuotientResourceEvent r N h).exactStorage } := by
  apply RootQuotientResourceState.ext
  · exact direction_state_succ_eq_add_event r N h
  · exact divisorCover_state_succ_eq_add_event hh
  · exact exactStorage_state_succ_eq_add_event hr hh

/-- Cumulative direction event count reconstructs the direction demand from an
arbitrary starting state. -/
theorem direction_state_add_eq_start_add_event_sum
    (r N m h : ℕ) :
    (rootQuotientResourceState r (N + m) h).direction =
      (rootQuotientResourceState r N h).direction +
        ∑ j in Finset.range m,
          (rootQuotientResourceEvent r (N + j) h).direction := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [show N + (m + 1) = (N + m) + 1 by omega,
        direction_state_succ_eq_add_event, ih]
      simp [Finset.sum_range_succ]
      omega

/-- Cumulative divisor-cover events reconstruct the cover frontier from an
arbitrary starting state. -/
theorem divisorCover_state_add_eq_start_add_event_sum
    {r N m h : ℕ}
    (hh : 1 ≤ h) :
    (rootQuotientResourceState r (N + m) h).divisorCover =
      (rootQuotientResourceState r N h).divisorCover +
        ∑ j in Finset.range m,
          (rootQuotientResourceEvent r (N + j) h).divisorCover := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [show N + (m + 1) = (N + m) + 1 by omega,
        divisorCover_state_succ_eq_add_event hh, ih]
      simp [Finset.sum_range_succ]
      omega

/-- Cumulative exact-storage events reconstruct the true macro frontier from an
arbitrary starting state. -/
theorem exactStorage_state_add_eq_start_add_event_sum
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    (rootQuotientResourceState r (N + m) h).exactStorage =
      (rootQuotientResourceState r N h).exactStorage +
        ∑ j in Finset.range m,
          (rootQuotientResourceEvent r (N + j) h).exactStorage := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [show N + (m + 1) = (N + m) + 1 by omega,
        exactStorage_state_succ_eq_add_event hr hh, ih]
      simp [Finset.sum_range_succ]
      omega

/-- **Lossless event-stream reconstruction.**

The event stream is a complete discrete derivative of the three-layer storage
frontier: summing each event coordinate exactly recovers the corresponding
resource curve from any starting state. -/
theorem resourceEventStream_reconstructs_frontier
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientResourceState r (N + m) h =
      { direction :=
          (rootQuotientResourceState r N h).direction +
            ∑ j in Finset.range m,
              (rootQuotientResourceEvent r (N + j) h).direction
        divisorCover :=
          (rootQuotientResourceState r N h).divisorCover +
            ∑ j in Finset.range m,
              (rootQuotientResourceEvent r (N + j) h).divisorCover
        exactStorage :=
          (rootQuotientResourceState r N h).exactStorage +
            ∑ j in Finset.range m,
              (rootQuotientResourceEvent r (N + j) h).exactStorage } := by
  apply RootQuotientResourceState.ext
  · exact direction_state_add_eq_start_add_event_sum r N m h
  · exact divisorCover_state_add_eq_start_add_event_sum hh
  · exact exactStorage_state_add_eq_start_add_event_sum hr hh

end EnterpriseMath.Quotient
