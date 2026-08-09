import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic

namespace EnterpriseMath.HistoryMerge

/-- The finite fiber of `F` through the history starting at `x`. -/
def fiberFinset {α β : Type*} [Fintype α] [DecidableEq β]
    (F : α → β) (x : α) : Finset α :=
  Finset.univ.filter fun y => F y = F x

/-- Membership in a finite history fiber is exactly equality of current images. -/
theorem mem_fiberFinset_iff {α β : Type*} [Fintype α] [DecidableEq β]
    (F : α → β) (x y : α) :
    y ∈ fiberFinset F x ↔ F y = F x := by
  simp [fiberFinset]

/-- T012 core: deterministic postcomposition cannot split histories that have already merged. -/
theorem merged_never_split {α β γ : Type*}
    (F : α → β) (T : β → γ) {x y : α}
    (hxy : F x = F y) :
    (T ∘ F) x = (T ∘ F) y := by
  exact congrArg T hxy

/-- Under deterministic postcomposition, each old history fiber is contained in the new fiber. -/
theorem fiberFinset_subset_postcompose {α β γ : Type*}
    [Fintype α] [DecidableEq β] [DecidableEq γ]
    (F : α → β) (T : β → γ) (x : α) :
    fiberFinset F x ⊆ fiberFinset (T ∘ F) x := by
  intro y hy
  apply (mem_fiberFinset_iff (F := T ∘ F) x y).2
  apply merged_never_split F T
  exact (mem_fiberFinset_iff F x y).1 hy

/-- T012 finite form: merged-history multiplicity is nondecreasing under deterministic postcomposition. -/
theorem fiberCard_mono_postcompose {α β γ : Type*}
    [Fintype α] [DecidableEq β] [DecidableEq γ]
    (F : α → β) (T : β → γ) (x : α) :
    (fiberFinset F x).card ≤ (fiberFinset (T ∘ F) x).card := by
  exact Finset.card_le_card (fiberFinset_subset_postcompose F T x)

end EnterpriseMath.HistoryMerge
