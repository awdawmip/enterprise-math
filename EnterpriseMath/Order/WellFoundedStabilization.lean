import Mathlib.Order.WellFounded

namespace EnterpriseMath.WellFoundedStabilization

variable {α : Type*} [PartialOrder α] [WellFoundedLT α]

/--
Finite stabilization of a reductive endomap on a well-founded partial order.

If `F x = x`, stop. Otherwise `F x < x`, so well-founded recursion continues below `x`.
-/
noncomputable def stabilize (F : α → α) (hred : ∀ x, F x ≤ x) (x : α) : α :=
  if h : F x = x then x else stabilize F hred (F x)
termination_by x
decreasing_by
  exact lt_of_le_of_ne (hred x) h

/-- A fixed point is unchanged by stabilization. -/
theorem stabilize_eq_of_fixed (F : α → α) (hred : ∀ x, F x ≤ x) {x : α}
    (hfix : F x = x) : stabilize F hred x = x := by
  rw [stabilize]
  simp [hfix]

/-- Stabilization always lands at an `F`-fixed point. -/
theorem stabilize_fixed (F : α → α) (hred : ∀ x, F x ≤ x) (x : α) :
    F (stabilize F hred x) = stabilize F hred x := by
  induction x using WellFoundedLT.induction with
  | h x ih =>
      rw [stabilize]
      split
      next hfix => exact hfix
      next hnot =>
        exact ih (F x) (lt_of_le_of_ne (hred x) hnot)

/-- Stabilization never moves upward. -/
theorem stabilize_le (F : α → α) (hred : ∀ x, F x ≤ x) (x : α) :
    stabilize F hred x ≤ x := by
  induction x using WellFoundedLT.induction with
  | h x ih =>
      rw [stabilize]
      split
      next => exact le_rfl
      next hnot =>
        exact (ih (F x) (lt_of_le_of_ne (hred x) hnot)).trans (hred x)

/-- Every `F`-fixed point below `x` remains below the stabilized state. -/
theorem fixed_le_stabilize (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    {y x : α} (hyfix : F y = y) (hyx : y ≤ x) : y ≤ stabilize F hred x := by
  revert hyx
  induction x using WellFoundedLT.induction with
  | h x ih =>
      intro hyx
      rw [stabilize]
      split
      next => exact hyx
      next hnot =>
        have hlt : F x < x := lt_of_le_of_ne (hred x) hnot
        apply ih (F x) hlt
        calc
          y = F y := hyfix.symm
          _ ≤ F x := hmono hyx

/-- The stabilized state is the greatest `F`-fixed point below the initial state. -/
theorem stabilize_isGreatest (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : IsGreatest {y : α | F y = y ∧ y ≤ x} (stabilize F hred x) := by
  refine ⟨⟨stabilize_fixed F hred x, stabilize_le F hred x⟩, ?_⟩
  intro y hy
  exact fixed_le_stabilize F hmono hred hy.1 hy.2

/-- The stabilization operator is idempotent. -/
theorem stabilize_idempotent (F : α → α) (hred : ∀ x, F x ≤ x) (x : α) :
    stabilize F hred (stabilize F hred x) = stabilize F hred x := by
  exact stabilize_eq_of_fixed F hred (stabilize_fixed F hred x)

/-- If `F` is monotone, then its stabilization operator is monotone. -/
theorem stabilize_mono (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) :
    Monotone (stabilize F hred) := by
  intro x y hxy
  apply fixed_le_stabilize F hmono hred (stabilize_fixed F hred x)
  exact (stabilize_le F hred x).trans hxy

/-- Stabilization has exactly the same fixed points as the original endomap. -/
theorem stabilize_eq_self_iff (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : stabilize F hred x = x ↔ F x = x := by
  constructor
  · intro h
    rw [← h]
    exact stabilize_fixed F hred x
  · exact stabilize_eq_of_fixed F hred

/--
On a well-founded partial order, stabilizing a monotone reductive endomap produces a
monotone, reductive, idempotent endomap with the same fixed points.
-/
theorem stabilized_is_interior_like (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) :
    Monotone (stabilize F hred) ∧
      (∀ x, stabilize F hred x ≤ x) ∧
      (∀ x, stabilize F hred (stabilize F hred x) = stabilize F hred x) := by
  exact ⟨stabilize_mono F hmono hred, stabilize_le F hred, stabilize_idempotent F hred⟩

end EnterpriseMath.WellFoundedStabilization
