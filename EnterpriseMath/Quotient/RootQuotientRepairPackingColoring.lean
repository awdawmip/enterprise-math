import EnterpriseMath.Quotient.RootQuotientRepairPackingStaircase
import Mathlib.Data.Fin.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A coloring of a finite target family by `k` compatibility classes.

Targets assigned the same color are either equal or share some admissible
candidate divisor.  Therefore a divisor-incompatibility packing can contain at
most one target of each color. -/
def RootQuotientRepairCompatibilityColoring
    (C : Set ℕ) (U : Finset ℕ) (k : ℕ) (color : ℕ → Fin k) : Prop :=
  ∀ t ∈ U, ∀ u ∈ U,
    color t = color u →
      t = u ∨ ∃ g : ℕ, g ∈ C ∧ g ∣ t ∧ g ∣ u

/-- A compatibility coloring is injective on every divisor-incompatibility
packing contained in the colored target family. -/
theorem repairPacking_color_injective
    {C : Set ℕ} {T U : Finset ℕ} {k : ℕ} {color : ℕ → Fin k}
    (hUT : U ⊆ T)
    (hPack : RootQuotientRepairDivisorPacking C U)
    (hColor : RootQuotientRepairCompatibilityColoring C T k color) :
    Set.InjOn color (U : Set ℕ) := by
  intro t ht u hu hEq
  have htU : t ∈ U := by simpa using ht
  have huU : u ∈ U := by simpa using hu
  have htT : t ∈ T := hUT htU
  have huT : u ∈ T := hUT huU
  rcases hColor t htT u huT hEq with hTU | ⟨g, hgC, hgT, hgU⟩
  · exact hTU
  · exact hPack g hgC t htU u huU hgT hgU

/-- **Compatibility-coloring upper bound on packing size.**

If all targets admit `k` compatibility colors, every divisor-incompatibility
packing has cardinality at most `k`. -/
theorem repairPacking_card_le_of_compatibilityColoring
    {C : Set ℕ} {T U : Finset ℕ} {k : ℕ} {color : ℕ → Fin k}
    (hUT : U ⊆ T)
    (hPack : RootQuotientRepairDivisorPacking C U)
    (hColor : RootQuotientRepairCompatibilityColoring C T k color) :
    U.card ≤ k := by
  have hInj := repairPacking_color_injective hUT hPack hColor
  have hCard := Set.ncard_le_ncard_of_injOn color
    (fun t ht => by simp) hInj (Set.toFinite (Set.univ : Set (Fin k)))
  simpa using hCard

/-- A compatibility coloring of the complete target family immediately bounds
the maximum repair packing number. -/
theorem repairDivisorPackingNumber_le_of_compatibilityColoring
    {T : Finset ℕ} {C : Set ℕ} {k : ℕ} {color : ℕ → Fin k}
    (hColor : RootQuotientRepairCompatibilityColoring C T k color) :
    rootQuotientRepairDivisorPackingNumber T C ≤ k := by
  obtain ⟨U, hUT, hPack, hUCard⟩ :=
    exists_maximumRepairDivisorPacking T C
  have hLe := repairPacking_card_le_of_compatibilityColoring hUT hPack hColor
  rw [hUCard] at hLe
  exact hLe

end EnterpriseMath.Quotient
