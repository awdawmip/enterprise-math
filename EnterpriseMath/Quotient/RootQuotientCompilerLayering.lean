import EnterpriseMath.Quotient.RootQuotientLeastPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- For root order at least two, every bounded prime instruction is itself a
nontrivial bounded power-free semantic action. -/
theorem rootQuotientPrimeBasis_subset_semanticBasis
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientPrimeBasis N ⊆
      RootQuotientNontrivialPowerFreeBasis r N := by
  intro p hp
  exact ⟨hp.1.two_le, hp.2, prime_rPowerFree hr hp.1⟩

/-- Exact criterion for when the semantic one-step basis and the primitive
prime instruction basis coincide.

They coincide exactly when the prime compiler already executes every required
semantic action in one primitive step, equivalently when the exact prime-only
horizon is at most one. -/
theorem rootQuotient_semanticBasis_eq_primeBasis_iff_horizon_le_one
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientNontrivialPowerFreeBasis r N = RootQuotientPrimeBasis N ↔
      rootQuotientPrimeHorizon r N ≤ 1 := by
  constructor
  · intro hEq
    have hSemanticSep :=
      rootQuotientNontrivialPowerFreeBasis_separates_at_one
        (r := r) (N := N) (by omega)
    rw [hEq] at hSemanticSep
    exact rootQuotientPrimeHorizon_minimal_of_separates
      (r := r) (N := N) (h := 1) (by omega) hSemanticSep
  · intro hHorizon
    apply Set.Subset.antisymm
    · have hPrimeSep :
          SeparatesRootQuotientWordsUpTo r N 1 (RootQuotientPrimeBasis N) :=
        (rootQuotientPrimeBasis_separates_iff_horizon_le
          (r := r) (N := N) (h := 1) (by omega)).2 hHorizon
      exact
        rootQuotientNontrivialPowerFreeBasis_subset_of_one_step_separates
          (r := r) (N := N) (G := RootQuotientPrimeBasis N)
          (by omega) rootQuotientPrimeBasis_positive hPrimeSep
    · exact rootQuotientPrimeBasis_subset_semanticBasis hr

/-- Composition gives a genuine strict presentation compression exactly after
the semantic/primitive layers have separated, i.e. when the prime-only exact
horizon exceeds one. -/
theorem rootQuotient_primeBasis_strictly_smaller_than_semantic_of_one_lt_horizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hDepth : 1 < rootQuotientPrimeHorizon r N) :
    RootQuotientPrimeBasis N ⊆
        RootQuotientNontrivialPowerFreeBasis r N ∧
      RootQuotientPrimeBasis N ≠
        RootQuotientNontrivialPowerFreeBasis r N := by
  refine ⟨rootQuotientPrimeBasis_subset_semanticBasis hr, ?_⟩
  intro hEq
  have hCollapse :
      rootQuotientPrimeHorizon r N ≤ 1 :=
    (rootQuotient_semanticBasis_eq_primeBasis_iff_horizon_le_one hr).1 hEq.symm
  omega

/-- Layering summary at the two extreme execution models.

* one-step semantics owns the nontrivial power-free basis;
* unrestricted-enough primitive compilation owns the prime basis;
* the two bases differ precisely when more than one prime instruction is
  required for some semantic denominator. -/
theorem rootQuotient_semantic_primitive_layering
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientPrimeBasis N ⊆
      RootQuotientNontrivialPowerFreeBasis r N ∧
    (RootQuotientNontrivialPowerFreeBasis r N = RootQuotientPrimeBasis N ↔
      rootQuotientPrimeHorizon r N ≤ 1) := by
  exact ⟨rootQuotientPrimeBasis_subset_semanticBasis hr,
    rootQuotient_semanticBasis_eq_primeBasis_iff_horizon_le_one hr⟩

end EnterpriseMath.Quotient
