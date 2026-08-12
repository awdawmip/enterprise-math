import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every instruction of a nontrivial alphabet is at least two. -/
def NontrivialRootQuotientGenerators (G : Set ℕ) : Prop :=
  ∀ g : ℕ, g ∈ G → 2 ≤ g

/-- A one-step implementation of a nontrivial target instruction must be the
literal singleton word containing that same instruction. -/
theorem mem_of_reachableWithin_one_of_two_le
    {H : Set ℕ} {g : ℕ}
    (hgTwo : 2 ≤ g)
    (hReach : RootQuotientProductReachableWithin 1 H g) :
    g ∈ H := by
  obtain ⟨w, hwLen, hwH, hProd⟩ := hReach
  cases w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
      omega
  | cons a w =>
      have hwNil : w = [] := by
        cases w with
        | nil => rfl
        | cons b w' =>
            simp at hwLen
      subst w
      have haH : a ∈ H := hwH a (by simp)
      simp [rootQuotientWordProduct] at hProd
      simpa [hProd] using haH

/-- Depth-one compilation exactly recovers reverse set inclusion on
nontrivial primitive alphabets.

Thus the ordinary presentation inclusion order is literally the depth-one
slice of the graded compiler relation; depths greater than one are the new
resource-sensitive refinement. -/
theorem rootQuotientAlphabetCompilesWithin_one_iff_subset
    {H G : Set ℕ}
    (hGTwo : NontrivialRootQuotientGenerators G) :
    RootQuotientAlphabetCompilesWithin 1 H G ↔ G ⊆ H := by
  constructor
  · intro hCompile g hgG
    exact mem_of_reachableWithin_one_of_two_le
      (hGTwo g hgG) (hCompile g hgG)
  · exact rootQuotientAlphabetCompilesWithin_of_subset

/-- Compiler depth is monotone: once every higher-level instruction can be
implemented within `h` steps, any larger budget remains valid. -/
theorem rootQuotientAlphabetCompilesWithin_mono_depth
    {H G : Set ℕ} {h j : ℕ}
    (hhj : h ≤ j)
    (hCompile : RootQuotientAlphabetCompilesWithin h H G) :
    RootQuotientAlphabetCompilesWithin j H G := by
  intro g hg
  obtain ⟨w, hwLen, hwH, hProd⟩ := hCompile g hg
  exact ⟨w, hwLen.trans hhj, hwH, hProd⟩

/-- Every alphabet compiles itself literally within one step. -/
theorem rootQuotientAlphabetCompilesWithin_refl_one
    {G : Set ℕ} :
    RootQuotientAlphabetCompilesWithin 1 G G :=
  rootQuotientAlphabetCompilesWithin_of_subset Set.Subset.rfl

/-- The graded compiler relation is a multiplicative enrichment of the ordinary
inclusion preorder: identity costs one, composition multiplies costs, and
larger allowed costs preserve feasibility. -/
theorem rootQuotientCompilerOrder_laws
    {K H G : Set ℕ} {j k m : ℕ}
    (hHG : RootQuotientAlphabetCompilesWithin j H G)
    (hKH : RootQuotientAlphabetCompilesWithin k K H)
    (hJKM : j * k ≤ m) :
    RootQuotientAlphabetCompilesWithin 1 G G ∧
      RootQuotientAlphabetCompilesWithin m K G := by
  exact ⟨rootQuotientAlphabetCompilesWithin_refl_one,
    rootQuotientAlphabetCompilesWithin_mono_depth hJKM
      (rootQuotientAlphabetCompilesWithin_trans hHG hKH)⟩

/-- Canonical semantic and `Omega`-filtered alphabets are nontrivial in the
sense required by the depth-one/inclusion equivalence. -/
theorem rootQuotientNontrivialPowerFreeBasis_nontrivialGenerators
    {r N : ℕ} :
    NontrivialRootQuotientGenerators
      (RootQuotientNontrivialPowerFreeBasis r N) := by
  intro g hg
  exact hg.1

end EnterpriseMath.Quotient
