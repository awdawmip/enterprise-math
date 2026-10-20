import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Complete bounded semantic composite family: the canonical semantic ISA
minus the forced bounded-prime core. -/
def RootQuotientAllSemanticComposites
    (r N : ℕ) : Set ℕ :=
  RootQuotientNontrivialPowerFreeBasis r N \ RootQuotientPrimeBasis N

/-- The complete semantic composite family is finite. -/
theorem rootQuotientAllSemanticComposites_finite
    {r N : ℕ} :
    (RootQuotientAllSemanticComposites r N).Finite :=
  rootQuotientNontrivialPowerFreeBasis_finite.sdiff

/-- The canonical semantic basis decomposes into disjoint forced primes and
semantic composites. -/
theorem semanticBasis_eq_prime_union_allSemanticComposites
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientNontrivialPowerFreeBasis r N =
      RootQuotientPrimeBasis N ∪ RootQuotientAllSemanticComposites r N := by
  have hPrimeSub : RootQuotientPrimeBasis N ⊆
      RootQuotientNontrivialPowerFreeBasis r N :=
    rootQuotientPrimeBasis_subset_semanticBasis hr
  ext g
  constructor
  · intro hg
    by_cases hgPrime : g ∈ RootQuotientPrimeBasis N
    · exact Or.inl hgPrime
    · exact Or.inr ⟨hg, hgPrime⟩
  · intro hg
    rcases hg with hgPrime | hgComp
    · exact hPrimeSub hgPrime
    · exact hgComp.1

/-- At one execution step every semantic composite action must be stored
literally, so the optional macro frontier begins at the full semantic-composite
cardinality. -/
theorem rootQuotientMinimumCompositeMacroCount_one_eq_allSemanticComposites_ncard
    {r N : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientMinimumCompositeMacroCount r N 1 =
      (RootQuotientAllSemanticComposites r N).ncard := by
  have hStorageOne :=
    rootQuotientMinimumStorageSize_one_eq_semanticBasis_ncard
      (r := r) (N := N) (by omega)
  have hDecomp :=
    rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      (r := r) (N := N) (h := 1) hr (by omega)
  have hPrimeSub : RootQuotientPrimeBasis N ⊆
      RootQuotientNontrivialPowerFreeBasis r N :=
    rootQuotientPrimeBasis_subset_semanticBasis hr
  have hSemanticCard :
      (RootQuotientAllSemanticComposites r N).ncard +
        (RootQuotientPrimeBasis N).ncard =
      (RootQuotientNontrivialPowerFreeBasis r N).ncard := by
    exact Set.ncard_sdiff_add_ncard_of_subset
      hPrimeSub rootQuotientNontrivialPowerFreeBasis_finite
  rw [hStorageOne] at hDecomp
  omega

/-- At the exact positive prime compiler horizon no optional composite macro is
needed. -/
theorem rootQuotientMinimumCompositeMacroCount_exactPrimeHorizon_eq_zero
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount
      r N (rootQuotientPrimeHorizon r N) = 0 :=
  rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
    hr hLPos le_rfl

/-- Full macro-frontier endpoint summary. -/
theorem rootQuotientCompositeMacroFrontier_endpoints
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount r N 1 =
        (RootQuotientAllSemanticComposites r N).ncard ∧
      rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeHorizon r N) = 0 :=
  ⟨rootQuotientMinimumCompositeMacroCount_one_eq_allSemanticComposites_ncard hr,
    rootQuotientMinimumCompositeMacroCount_exactPrimeHorizon_eq_zero hr hLPos⟩

end EnterpriseMath.Quotient
