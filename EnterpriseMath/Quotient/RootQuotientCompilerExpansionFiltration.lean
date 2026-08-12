import EnterpriseMath.Quotient.RootQuotientCompilerDistance
import EnterpriseMath.Quotient.RootQuotientCompilerExpansionGeometry
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- On the canonical `Omega` filtration, the arbitrary-presentation expansion
factor has the exact closed form obtained earlier from ceiling division.

The outer `max 1` is precisely the multiplicative-unit normalization used by
the general infinite-valued geometry. -/
theorem rootQuotientCompilerExpansion_omegaFiltered_eq
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    rootQuotientCompilerExpansion
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) =
      ((max 1
        (rootQuotientOmegaFiltrationCompilerDepth r N k j) : ℕ) : ℕ∞) := by
  classical
  let d := rootQuotientOmegaFiltrationCompilerDepth r N k j
  have hCompileD : RootQuotientAlphabetCompilesWithin
      d
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j) := by
    dsimp [d]
    exact rootQuotientOmegaFilteredBasis_compiles_at_exact_compilerDepth
      hr hN hkPos
  let hExists : ∃ h : ℕ,
      RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) :=
    ⟨d, hCompileD⟩
  have hFindLe : Nat.find hExists ≤ d :=
    Nat.find_min' hExists hCompileD
  have hFindCompile : RootQuotientAlphabetCompilesWithin
      (Nat.find hExists)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j) :=
    Nat.find_spec hExists
  have hDLeFind : d ≤ Nat.find hExists := by
    dsimp [d]
    exact rootQuotientOmegaFiltrationCompilerDepth_minimal
      hr hN hkPos hFindCompile
  have hFindEq : Nat.find hExists = d :=
    Nat.le_antisymm hFindLe hDLeFind
  unfold rootQuotientCompilerExpansion
  rw [dif_pos hExists]
  rw [hFindEq]

/-- The same identification for compilation all the way to the canonical
semantic ISA. -/
theorem rootQuotientCompilerExpansion_omegaFiltered_to_semantic_eq
    {r N k : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    rootQuotientCompilerExpansion
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientNontrivialPowerFreeBasis r N) =
      ((max 1 (rootQuotientSemanticCompilerDepth r N k) : ℕ) : ℕ∞) := by
  classical
  let d := rootQuotientSemanticCompilerDepth r N k
  have hCompileD : RootQuotientAlphabetCompilesWithin
      d
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
    dsimp [d]
    exact rootQuotientOmegaFilteredBasis_compiles_semantic_at_exact_depth
      hr hkPos
  let hExists : ∃ h : ℕ,
      RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientNontrivialPowerFreeBasis r N) :=
    ⟨d, hCompileD⟩
  have hFindLe : Nat.find hExists ≤ d :=
    Nat.find_min' hExists hCompileD
  have hFindCompile : RootQuotientAlphabetCompilesWithin
      (Nat.find hExists)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientNontrivialPowerFreeBasis r N) :=
    Nat.find_spec hExists
  have hDLeFind : d ≤ Nat.find hExists := by
    have hMin :=
      (rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff_compilerDepth_le
        (r := r) (N := N) (k := k) (h := Nat.find hExists)
        hr hkPos).1 hFindCompile
    exact hMin
  have hFindEq : Nat.find hExists = d :=
    Nat.le_antisymm hFindLe hDLeFind
  unfold rootQuotientCompilerExpansion
  rw [dif_pos hExists]
  rw [hFindEq]

/-- Explicit ceiling-division form of the arbitrary-presentation expansion on
the `Omega` filtration. -/
theorem rootQuotientCompilerExpansion_omegaFiltered_closedForm
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    rootQuotientCompilerExpansion
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) =
      ((max 1
        (rootQuotientOmegaFiltrationExposedRank r N j ⌈/⌉ k) : ℕ) : ℕ∞) := by
  simpa [rootQuotientOmegaFiltrationCompilerDepth] using
    rootQuotientCompilerExpansion_omegaFiltered_eq
      (r := r) (N := N) (k := k) (j := j) hr hN hkPos

/-- Prime-to-semantic expansion factor is the exact prime horizon whenever that
horizon is positive. -/
theorem rootQuotientCompilerExpansion_prime_to_semantic_eq_horizon
    {r N : ℕ}
    (hr : 1 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientCompilerExpansion
        (RootQuotientOmegaFilteredBasis r N 1)
        (RootQuotientNontrivialPowerFreeBasis r N) =
      (rootQuotientPrimeHorizon r N : ℕ∞) := by
  rw [rootQuotientCompilerExpansion_omegaFiltered_to_semantic_eq
    (r := r) (N := N) (k := 1) hr (by omega)]
  rw [rootQuotientSemanticCompilerDepth_one]
  have hMax : max 1 (rootQuotientPrimeHorizon r N) =
      rootQuotientPrimeHorizon r N := max_eq_right hLPos
  rw [hMax]

end EnterpriseMath.Quotient
