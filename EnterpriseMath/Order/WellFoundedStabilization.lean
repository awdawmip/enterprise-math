import Mathlib.Logic.Function.Iterate
import Mathlib.Order.WellFounded

namespace EnterpriseMath.WellFoundedStabilization

variable {α : Type*} [PartialOrder α] [WellFoundedLT α]

/--
A monotone reductive endomap on a well-founded partial order reaches, after finitely
many ordinary iterations, the greatest fixed point below the initial state.
-/
theorem exists_iterate_isGreatest (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : ∃ n : ℕ, IsGreatest {y : α | F y = y ∧ y ≤ x} (F^[n] x) := by
  induction x using WellFoundedLT.induction with
  | ind x ih =>
      by_cases hfix : F x = x
      · refine ⟨0, ?_⟩
        change IsGreatest {y : α | F y = y ∧ y ≤ x} x
        refine ⟨⟨hfix, le_rfl⟩, ?_⟩
        intro y hy
        exact hy.2
      · have hlt : F x < x := lt_of_le_of_ne (hred x) hfix
        obtain ⟨n, hn⟩ := ih (F x) hlt
        refine ⟨n.succ, ?_⟩
        change IsGreatest {y : α | F y = y ∧ y ≤ x} (F^[n] (F x))
        refine ⟨⟨hn.1.1, hn.1.2.trans (hred x)⟩, ?_⟩
        intro y hy
        apply hn.2
        refine ⟨hy.1, ?_⟩
        calc
          y = F y := hy.1.symm
          _ ≤ F x := hmono hy.2

/-- A canonical finite iteration count reaching the greatest fixed point below `x`. -/
noncomputable def stabilizationSteps (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : ℕ :=
  Classical.choose (exists_iterate_isGreatest F hmono hred x)

/-- The canonical stabilized state selected by finite iteration. -/
noncomputable def stabilize (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : α :=
  F^[stabilizationSteps F hmono hred x] x

/-- The selected finite iterate is the greatest fixed point below the initial state. -/
theorem stabilizationSteps_spec (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) :
    IsGreatest {y : α | F y = y ∧ y ≤ x}
      (F^[stabilizationSteps F hmono hred x] x) :=
  Classical.choose_spec (exists_iterate_isGreatest F hmono hred x)

/-- `stabilize` is reached by the canonical finite number of ordinary `F`-iterations. -/
theorem stabilize_eq_iterate (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) :
    stabilize F hmono hred x = F^[stabilizationSteps F hmono hred x] x :=
  rfl

/-- The stabilized state is the greatest original fixed point below the initial state. -/
theorem stabilize_isGreatest (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : IsGreatest {y : α | F y = y ∧ y ≤ x} (stabilize F hmono hred x) := by
  simpa [stabilize] using stabilizationSteps_spec F hmono hred x

/-- Stabilization always lands at an original `F`-fixed point. -/
theorem stabilize_fixed (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : F (stabilize F hmono hred x) = stabilize F hmono hred x :=
  (stabilize_isGreatest F hmono hred x).1.1

/-- Stabilization never moves upward. -/
theorem stabilize_le (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : stabilize F hmono hred x ≤ x :=
  (stabilize_isGreatest F hmono hred x).1.2

/-- Every original fixed point below `x` lies below the stabilized state. -/
theorem fixed_le_stabilize (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    {y x : α} (hyfix : F y = y) (hyx : y ≤ x) : y ≤ stabilize F hmono hred x :=
  (stabilize_isGreatest F hmono hred x).2 ⟨hyfix, hyx⟩

/-- An original fixed point is unchanged by stabilization. -/
theorem stabilize_eq_of_fixed (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    {x : α} (hfix : F x = x) : stabilize F hmono hred x = x := by
  apply le_antisymm (stabilize_le F hmono hred x)
  exact fixed_le_stabilize F hmono hred hfix le_rfl

/-- The stabilization operator is idempotent. -/
theorem stabilize_idempotent (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) :
    stabilize F hmono hred (stabilize F hmono hred x) = stabilize F hmono hred x := by
  exact stabilize_eq_of_fixed F hmono hred (stabilize_fixed F hmono hred x)

/-- Stabilization preserves monotonicity. -/
theorem stabilize_mono (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) :
    Monotone (stabilize F hmono hred) := by
  intro x y hxy
  apply fixed_le_stabilize F hmono hred (stabilize_fixed F hmono hred x)
  exact (stabilize_le F hmono hred x).trans hxy

/-- Stabilization has exactly the same fixed points as the original endomap. -/
theorem stabilize_eq_self_iff (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x)
    (x : α) : stabilize F hmono hred x = x ↔ F x = x := by
  constructor
  · intro h
    rw [← h]
    exact stabilize_fixed F hmono hred x
  · exact stabilize_eq_of_fixed F hmono hred

/--
On a well-founded partial order, finite stabilization completes a monotone reductive
endomap into a monotone, reductive, idempotent endomap with the same fixed points.
-/
theorem stabilized_is_interior_like (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) :
    Monotone (stabilize F hmono hred) ∧
      (∀ x, stabilize F hmono hred x ≤ x) ∧
      (∀ x, stabilize F hmono hred (stabilize F hmono hred x) = stabilize F hmono hred x) := by
  exact ⟨stabilize_mono F hmono hred, stabilize_le F hmono hred,
    stabilize_idempotent F hmono hred⟩

end EnterpriseMath.WellFoundedStabilization
