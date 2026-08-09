import Mathlib.Tactic

namespace EnterpriseMath.CriticalGrid

/-- Compose adjacent endpoint pairs. The equality proof records that the
intermediate endpoint really is shared; the resulting comparison remembers only
its two outer endpoints. -/
def composeAdjacent {α : Type} (p q : α × α) (_h : p.2 = q.1) : α × α :=
  (p.1, q.2)

/-- Historical P018 critical-grid result: composition of three successive
endpoints forgets only the intermediate point and returns the outer pair. -/
@[simp] theorem composeAdjacent_mk {α : Type} (a b c : α) :
    composeAdjacent (a, b) (b, c) rfl = (a, c) := rfl

/-- Historical P018 critical-grid result: the two decompositions of a
deterministic 2x2 rectangle have exactly the same outer endpoint pair. No
additive, order, metric, or topological structure is required. -/
theorem rectangle_pair_interchange
    {α β γ : Type}
    (F₀ F₁ : α → β) (G₀ G₁ : β → γ) (x : α) :
    composeAdjacent
        (G₀ (F₀ x), G₀ (F₁ x))
        (G₀ (F₁ x), G₁ (F₁ x))
        rfl
      =
    composeAdjacent
        (G₀ (F₀ x), G₁ (F₀ x))
        (G₁ (F₀ x), G₁ (F₁ x))
        rfl := by
  rfl

/-- Integer-coordinate shadow of the same rectangle: both edge decompositions
are exact telescoping decompositions of the outer difference. -/
theorem rectangle_difference_interchange (a b c d : ℤ) :
    d - a = (b - a) + (d - b) ∧
    d - a = (c - a) + (d - c) := by
  constructor <;> omega

/-- The finite rectangle-variation identity obtained by subtracting the two
exact decompositions. -/
theorem rectangle_variation_identity (a b c d : ℤ) :
    (d - b) - (c - a) = (d - c) - (b - a) := by
  omega

end EnterpriseMath.CriticalGrid
