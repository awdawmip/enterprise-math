import Mathlib.Data.Set.Card

namespace EnterpriseMath.History

universe u v w

variable {X : Type u} {Y : Type v} {Z : Type w}

/-- Initial states that have merged with `x` under the forward map `F`. -/
def mergedClass (F : X → Y) (x : X) : Set X :=
  {y | F y = F x}

/-- Once two histories have merged, deterministic forward composition cannot split them again. -/
theorem mergedClass_subset_next (F : X → Y) (T : Y → Z) (x : X) :
    mergedClass F x ⊆ mergedClass (T ∘ F) x := by
  intro y hy
  change F y = F x at hy
  change T (F y) = T (F x)
  exact congrArg T hy

/-- On a finite state domain, merged-history multiplicity is nondecreasing under deterministic
forward composition. This is the finite-cardinality part of T012. -/
theorem mergedMultiplicity_mono [Finite X] (F : X → Y) (T : Y → Z) (x : X) :
    (mergedClass F x).ncard ≤ (mergedClass (T ∘ F) x).ncard :=
  Set.ncard_le_ncard (mergedClass_subset_next F T x)

end EnterpriseMath.History
