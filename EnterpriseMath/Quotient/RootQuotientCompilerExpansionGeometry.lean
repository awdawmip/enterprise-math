import EnterpriseMath.Quotient.RootQuotientCompilerOrder
import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import Mathlib.Data.ENat.Basic
import Mathlib.Data.Nat.Find
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Infinite-valued compiler expansion factor between arbitrary quotient
presentations.

If `H` can implement every instruction of `G`, take the least implementation
depth, but floor the expansion factor at one so that literal identity/inclusion
has multiplicative unit cost `1`.  If `G` is not implementable from `H`, the
cost is `∞`.

This normalization avoids the pathological `0 * ∞ = 0` interaction that would
arise from using raw zero-step depths as multiplicative path lengths. -/
noncomputable def rootQuotientCompilerExpansion
    (H G : Set ℕ) : ℕ∞ :=
  if hExists : ∃ h : ℕ, RootQuotientAlphabetCompilesWithin h H G then
    (max 1 (Nat.find hExists) : ℕ)
  else
    ⊤

/-- Every compiler expansion factor is at least the multiplicative identity. -/
theorem one_le_rootQuotientCompilerExpansion
    {H G : Set ℕ} :
    1 ≤ rootQuotientCompilerExpansion H G := by
  classical
  unfold rootQuotientCompilerExpansion
  split_ifs with hExists
  · exact_mod_cast Nat.le_max_left 1 (Nat.find hExists)
  · exact le_top

/-- Finite compiler expansion is equivalent to eventual implementability. -/
theorem rootQuotientCompilerExpansion_ne_top_iff
    {H G : Set ℕ} :
    rootQuotientCompilerExpansion H G ≠ ⊤ ↔
      ∃ h : ℕ, RootQuotientAlphabetCompilesWithin h H G := by
  classical
  unfold rootQuotientCompilerExpansion
  split_ifs with hExists
  · exact ⟨fun _ => hExists, fun _ => ENat.natCast_ne_top _⟩
  · simp [hExists]

/-- Exact finite-budget characterization of the infinite-valued expansion
factor.

For any positive budget `h`, `Δ(H,G)≤h` iff `H` actually implements `G` within
`h` primitive instructions. -/
theorem rootQuotientCompilerExpansion_le_natCast_iff
    {H G : Set ℕ} {h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientCompilerExpansion H G ≤ (h : ℕ∞) ↔
      RootQuotientAlphabetCompilesWithin h H G := by
  classical
  unfold rootQuotientCompilerExpansion
  split_ifs with hExists
  · let m := Nat.find hExists
    have hmCompile : RootQuotientAlphabetCompilesWithin m H G :=
      Nat.find_spec hExists
    constructor
    · intro hLe
      have hMaxLe : max 1 m ≤ h := by
        exact_mod_cast hLe
      have hmLe : m ≤ h :=
        (Nat.le_max_right 1 m).trans hMaxLe
      exact rootQuotientAlphabetCompilesWithin_mono_depth hmLe hmCompile
    · intro hCompile
      have hmLe : m ≤ h := Nat.find_min' hExists hCompile
      have hMaxLe : max 1 m ≤ h := max_le hh hmLe
      exact_mod_cast hMaxLe
  · constructor
    · intro hLe
      have hEqTop : (h : ℕ∞) = ⊤ := top_unique hLe
      exact (ENat.natCast_ne_top h hEqTop).elim
    · intro hCompile
      exact (hExists ⟨h, hCompile⟩).elim

/-- Literal identity has expansion factor exactly one. -/
theorem rootQuotientCompilerExpansion_self
    {G : Set ℕ} :
    rootQuotientCompilerExpansion G G = 1 := by
  apply le_antisymm
  · exact
      (rootQuotientCompilerExpansion_le_natCast_iff (H := G) (G := G)
        (h := 1) (by omega)).2
        rootQuotientAlphabetCompilesWithin_refl_one
  · exact one_le_rootQuotientCompilerExpansion

/-- Multiplicative triangle inequality on arbitrary presentations.

Compiler expansion factors compose as path expansion bounds; unreachable legs
have cost `∞`, which is absorbing because every expansion factor is at least
one. -/
theorem rootQuotientCompilerExpansion_triangle
    {K H G : Set ℕ} :
    rootQuotientCompilerExpansion K G ≤
      rootQuotientCompilerExpansion H G *
        rootQuotientCompilerExpansion K H := by
  classical
  by_cases hHG : ∃ a : ℕ, RootQuotientAlphabetCompilesWithin a H G
  · by_cases hKH : ∃ b : ℕ, RootQuotientAlphabetCompilesWithin b K H
    · let a := max 1 (Nat.find hHG)
      let b := max 1 (Nat.find hKH)
      have haCompile : RootQuotientAlphabetCompilesWithin a H G := by
        apply rootQuotientAlphabetCompilesWithin_mono_depth
          (Nat.le_max_right 1 (Nat.find hHG))
        exact Nat.find_spec hHG
      have hbCompile : RootQuotientAlphabetCompilesWithin b K H := by
        apply rootQuotientAlphabetCompilesWithin_mono_depth
          (Nat.le_max_right 1 (Nat.find hKH))
        exact Nat.find_spec hKH
      have habCompile : RootQuotientAlphabetCompilesWithin (a * b) K G :=
        rootQuotientAlphabetCompilesWithin_trans haCompile hbCompile
      have habPos : 1 ≤ a * b := by
        have haPos : 1 ≤ a := by exact Nat.le_max_left _ _
        have hbPos : 1 ≤ b := by exact Nat.le_max_left _ _
        exact Nat.one_le_mul haPos hbPos
      have hLe : rootQuotientCompilerExpansion K G ≤ ((a * b : ℕ) : ℕ∞) :=
        (rootQuotientCompilerExpansion_le_natCast_iff habPos).2 habCompile
      have hHGCost : rootQuotientCompilerExpansion H G = (a : ℕ∞) := by
        simp [rootQuotientCompilerExpansion, hHG, a]
      have hKHCost : rootQuotientCompilerExpansion K H = (b : ℕ∞) := by
        simp [rootQuotientCompilerExpansion, hKH, b]
      rw [hHGCost, hKHCost, ← ENat.natCast_mul]
      exact hLe
    · have hKHtop : rootQuotientCompilerExpansion K H = ⊤ := by
        simp [rootQuotientCompilerExpansion, hKH]
      have hHGNonzero : rootQuotientCompilerExpansion H G ≠ 0 := by
        have hOne := one_le_rootQuotientCompilerExpansion (H := H) (G := G)
        omega
      rw [hKHtop, ENat.mul_top hHGNonzero]
      exact le_top
  · have hHGtop : rootQuotientCompilerExpansion H G = ⊤ := by
      simp [rootQuotientCompilerExpansion, hHG]
    have hKHNonzero : rootQuotientCompilerExpansion K H ≠ 0 := by
      have hOne := one_le_rootQuotientCompilerExpansion (H := K) (G := H)
      omega
    rw [hHGtop, ENat.top_mul hKHNonzero]
    exact le_top

/-- For nontrivial target instructions, expansion factor at most one is exactly
reverse set inclusion.  Thus ordinary presentation inclusion is the unit-cost
slice of the infinite-valued compiler geometry. -/
theorem rootQuotientCompilerExpansion_le_one_iff_subset
    {H G : Set ℕ}
    (hGTwo : NontrivialRootQuotientGenerators G) :
    rootQuotientCompilerExpansion H G ≤ 1 ↔ G ⊆ H := by
  rw [rootQuotientCompilerExpansion_le_natCast_iff (h := 1) (by omega)]
  exact rootQuotientAlphabetCompilesWithin_one_iff_subset hGTwo

/-- Equivalent equality-one form of the inclusion slice. -/
theorem rootQuotientCompilerExpansion_eq_one_iff_subset
    {H G : Set ℕ}
    (hGTwo : NontrivialRootQuotientGenerators G) :
    rootQuotientCompilerExpansion H G = 1 ↔ G ⊆ H := by
  constructor
  · intro hEq
    exact
      (rootQuotientCompilerExpansion_le_one_iff_subset hGTwo).1 hEq.le
  · intro hSubset
    apply le_antisymm
    · exact
        (rootQuotientCompilerExpansion_le_one_iff_subset hGTwo).2 hSubset
    · exact one_le_rootQuotientCompilerExpansion

/-- Task correctness is a finite-radius ball around the canonical semantic
specification in compiler expansion geometry. -/
theorem rootQuotientCompilerExpansion_to_semanticBasis_le_iff_separates
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h)
    (hGPos : PositiveRootQuotientGenerators G) :
    rootQuotientCompilerExpansion
        G (RootQuotientNontrivialPowerFreeBasis r N) ≤ (h : ℕ∞) ↔
      SeparatesRootQuotientWordsUpTo r N h G := by
  rw [rootQuotientCompilerExpansion_le_natCast_iff hh]
  exact (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
    hr hGPos).symm

end EnterpriseMath.Quotient
