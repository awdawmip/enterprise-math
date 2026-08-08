import Mathlib.Order.GaloisConnection.Defs

open Function

namespace EnterpriseMath.OrderAdjoint

universe u v

variable {α : Type u} {β : Type v}

/-- The lower-after-upper projection induced by a Galois connection.

Enterprise Math calls this shape a collapse when it is instantiated by a power map and
`Nat.nthRoot`. The order-theoretic construction itself is standard mathlib mathematics. -/
def collapse [Preorder α] [Preorder β] {l : α → β} {u : β → α}
    (_gc : GaloisConnection l u) : β → β :=
  l ∘ u

@[simp]
theorem collapse_apply [Preorder α] [Preorder β] {l : α → β} {u : β → α}
    (gc : GaloisConnection l u) (b : β) : collapse gc b = l (u b) :=
  rfl

/-- A Galois lower-after-upper projection is reductive. -/
theorem collapse_le [Preorder α] [Preorder β] {l : α → β} {u : β → α}
    (gc : GaloisConnection l u) (b : β) : collapse gc b ≤ b := by
  simpa [collapse] using gc.l_u_le b

/-- A Galois lower-after-upper projection is monotone. -/
theorem collapse_monotone [Preorder α] [Preorder β] {l : α → β} {u : β → α}
    (gc : GaloisConnection l u) : Monotone (collapse gc) := by
  simpa [collapse] using gc.monotone_l_comp_u

/-- A Galois lower-after-upper projection is idempotent. -/
theorem collapse_idempotent [Preorder α] [PartialOrder β] {l : α → β} {u : β → α}
    (gc : GaloisConnection l u) (b : β) :
    collapse gc (collapse gc b) = collapse gc b := by
  simpa [collapse] using gc.l_u_l_eq_l (u b)

/-- Fixed points of the lower-after-upper projection are exactly elements in the range
of the lower adjoint. -/
theorem collapse_eq_self_iff_mem_range [Preorder α] [PartialOrder β]
    {l : α → β} {u : β → α} (gc : GaloisConnection l u) (b : β) :
    collapse gc b = b ↔ b ∈ Set.range l := by
  constructor
  · intro h
    refine ⟨u b, ?_⟩
    simpa [collapse] using h
  · rintro ⟨a, rfl⟩
    simpa [collapse] using gc.l_u_l_eq_l a

end EnterpriseMath.OrderAdjoint
