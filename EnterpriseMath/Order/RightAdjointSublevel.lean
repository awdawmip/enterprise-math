import Mathlib.Order.GaloisConnection.Basic
import Mathlib.Order.Bounds.Basic

namespace EnterpriseMath.Order

variable {α β : Type*} [PartialOrder α] [PartialOrder β]

/-- A monotone map admits a right adjoint exactly when each of its principal
sublevel sets has a greatest element. -/
theorem exists_rightAdjoint_iff_sublevel_hasGreatest (l : α → β) (hl : Monotone l) :
    (∃ u : β → α, GaloisConnection l u) ↔
      ∀ b : β, ∃ m : α, IsGreatest {a : α | l a ≤ b} m := by
  constructor
  · rintro ⟨u, h⟩ b
    refine ⟨u b, (h (u b) b).2 le_rfl, ?_⟩
    intro a ha
    exact (h a b).1 ha
  · intro h
    let u (b : β) : α := Classical.choose (h b)
    have hu (b : β) : IsGreatest {a : α | l a ≤ b} (u b) :=
      Classical.choose_spec (h b)
    refine ⟨u, ?_⟩
    intro a b
    exact ⟨fun ha => (hu b).2 ha, fun ha => (hl ha).trans (hu b).1⟩

end EnterpriseMath.Order
