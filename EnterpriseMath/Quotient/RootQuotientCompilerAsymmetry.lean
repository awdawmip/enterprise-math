import EnterpriseMath.Quotient.RootQuotientCompilerDistance
import EnterpriseMath.Quotient.RootQuotientOmegaFiltrationGeometry
import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every bounded `Omega`-filtered presentation is finite. -/
theorem rootQuotientOmegaFilteredBasis_finite
    {r N k : ℕ} :
    (RootQuotientOmegaFilteredBasis r N k).Finite := by
  apply Set.finite_Icc.subset
  intro g hg
  exact ⟨hg.1, hg.2.1⟩

/-- Before semantic saturation, increasing the `Omega` capacity strictly adds
primitive instruction types.

The witness is the minimum bounded rank-`j` power-free shell element. -/
theorem rootQuotientOmegaFilteredBasis_ssubset_of_lt_of_le_horizon
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hkj : k < j)
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientOmegaFilteredBasis r N k ⊂
      RootQuotientOmegaFilteredBasis r N j := by
  have hSubset :
      RootQuotientOmegaFilteredBasis r N k ⊆
        RootQuotientOmegaFilteredBasis r N j :=
    rootQuotientOmegaFilteredBasis_mono (Nat.le_of_lt hkj)
  let b := rootQuotientPrimeShellMinimum r j
  have hbShell : b ∈ RootQuotientPrimeShell r j := by
    dsimp [b]
    exact rootQuotientPrimeShellMinimum_mem hr
  have hbN : b ≤ N := by
    dsimp [b]
    exact
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := j) hr hN).2 hjL
  have hbTwo : 2 ≤ b := by
    by_contra hNot
    have hbOne : b = 1 := by omega
    have hCountZero : rootQuotientPrimeFactorCount b = 0 := by
      simp [hbOne, rootQuotientPrimeFactorCount]
    have hCountJ : rootQuotientPrimeFactorCount b = j := hbShell.2.2
    omega
  have hbJ : b ∈ RootQuotientOmegaFilteredBasis r N j :=
    ⟨hbTwo, hbN, hbShell.2.1, by rw [hbShell.2.2]⟩
  have hbNotK : b ∉ RootQuotientOmegaFilteredBasis r N k := by
    intro hbK
    have hCountK : rootQuotientPrimeFactorCount b ≤ k := hbK.2.2.2
    rw [hbShell.2.2] at hCountK
    omega
  exact Set.ssubset_iff_subset_ne.mpr
    ⟨hSubset, by
      intro hEq
      have hbK : b ∈ RootQuotientOmegaFilteredBasis r N k := by
        rw [hEq]
        exact hbJ
      exact hbNotK hbK⟩

/-- Strict filtration growth is strict storage-cardinality growth. -/
theorem rootQuotientOmegaFilteredBasis_ncard_lt_of_lt_of_le_horizon
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hkj : k < j)
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    (RootQuotientOmegaFilteredBasis r N k).ncard <
      (RootQuotientOmegaFilteredBasis r N j).ncard := by
  exact Set.ncard_lt_ncard
    (rootQuotientOmegaFilteredBasis_ssubset_of_lt_of_le_horizon
      hr hN hkPos hkj hjL)
    rootQuotientOmegaFilteredBasis_finite

/-- The exposed rank of an unsaturated filtration layer is exactly its raw
capacity index. -/
theorem rootQuotientOmegaFiltrationExposedRank_eq_index_of_le_horizon
    {r N j : ℕ}
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientOmegaFiltrationExposedRank r N j = j := by
  simp [rootQuotientOmegaFiltrationExposedRank, hjL]

/-- Richer-to-poorer compilation costs exactly one literal instruction in the
strict unsaturated region. -/
theorem rootQuotientOmegaFiltrationCompilerDepth_richer_to_poorer_eq_one
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hkj : k < j)
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientOmegaFiltrationCompilerDepth r N j k = 1 := by
  have hjPos : 1 ≤ j := by omega
  have hkL : k ≤ rootQuotientPrimeHorizon r N :=
    (Nat.le_of_lt hkj).trans hjL
  have hSubset :
      RootQuotientOmegaFilteredBasis r N k ⊆
        RootQuotientOmegaFilteredBasis r N j :=
    rootQuotientOmegaFilteredBasis_mono (Nat.le_of_lt hkj)
  have hCompileOne : RootQuotientAlphabetCompilesWithin
      1
      (RootQuotientOmegaFilteredBasis r N j)
      (RootQuotientOmegaFilteredBasis r N k) :=
    rootQuotientAlphabetCompilesWithin_of_subset hSubset
  have hUpper :
      rootQuotientOmegaFiltrationCompilerDepth r N j k ≤ 1 :=
    rootQuotientOmegaFiltrationCompilerDepth_minimal
      hr hN hjPos hCompileOne
  have hPositive :
      0 < rootQuotientOmegaFiltrationCompilerDepth r N j k := by
    by_contra hNot
    have hZero : rootQuotientOmegaFiltrationCompilerDepth r N j k = 0 := by
      omega
    have hCompileZero : RootQuotientAlphabetCompilesWithin
        0
        (RootQuotientOmegaFilteredBasis r N j)
        (RootQuotientOmegaFilteredBasis r N k) :=
      (rootQuotientOmegaFilteredBasis_compilesWithin_iff_compilerDepth_le
        (r := r) (N := N) (k := j) (j := k) (h := 0)
        hr hN hjPos).2 (by omega)
    have hBudget :=
      (rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
        (r := r) (N := N) (k := j) (j := k) (h := 0)
        hr hN hjPos).1 hCompileZero
    rw [rootQuotientOmegaFiltrationExposedRank_eq_index_of_le_horizon hkL] at hBudget
    omega
  omega

/-- Poorer-to-richer compilation cannot be done in one instruction in the
strict unsaturated region. -/
theorem two_le_rootQuotientOmegaFiltrationCompilerDepth_poorer_to_richer
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hkj : k < j)
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    2 ≤ rootQuotientOmegaFiltrationCompilerDepth r N k j := by
  by_contra hNot
  have hDepthLeOne :
      rootQuotientOmegaFiltrationCompilerDepth r N k j ≤ 1 := by omega
  have hCompileOne : RootQuotientAlphabetCompilesWithin
      1
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j) :=
    (rootQuotientOmegaFilteredBasis_compilesWithin_iff_compilerDepth_le
      (r := r) (N := N) (k := k) (j := j) (h := 1)
      hr hN hkPos).2 hDepthLeOne
  have hBudget :=
    (rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
      (r := r) (N := N) (k := k) (j := j) (h := 1)
      hr hN hkPos).1 hCompileOne
  rw [rootQuotientOmegaFiltrationExposedRank_eq_index_of_le_horizon hjL] at hBudget
  omega

/-- Strict storage-depth Pareto asymmetry before semantic saturation.

Moving from capacity `k` to a strictly richer capacity `j` increases stored
primitive types and strictly decreases the reverse compiler cost: the richer
ISA can express the poorer one literally in one step, whereas the poorer ISA
needs at least two steps to recover the richer one. -/
theorem rootQuotientOmegaFiltration_strict_storage_depth_asymmetry
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hkj : k < j)
    (hjL : j ≤ rootQuotientPrimeHorizon r N) :
    (RootQuotientOmegaFilteredBasis r N k).ncard <
        (RootQuotientOmegaFilteredBasis r N j).ncard ∧
      rootQuotientOmegaFiltrationCompilerDepth r N j k = 1 ∧
      2 ≤ rootQuotientOmegaFiltrationCompilerDepth r N k j := by
  exact ⟨
    rootQuotientOmegaFilteredBasis_ncard_lt_of_lt_of_le_horizon
      hr hN hkPos hkj hjL,
    rootQuotientOmegaFiltrationCompilerDepth_richer_to_poorer_eq_one
      hr hN hkPos hkj hjL,
    two_le_rootQuotientOmegaFiltrationCompilerDepth_poorer_to_richer
      hr hN hkPos hkj hjL⟩

end EnterpriseMath.Quotient
