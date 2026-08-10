import EnterpriseMath.Quotient.RootQuotientCapacityStorageEnvelope
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Storage overhead of insisting on the complete canonical capacity-filtered
instruction dictionary, compared with a true minimum-cardinality presentation
at the same execution horizon. -/
def rootQuotientCapacityCompletenessStorageTax
    (r N h : ℕ) : ℕ :=
  (RootQuotientOmegaFilteredBasis
      r N (rootQuotientCanonicalCapacityForHorizon r N h)).ncard -
    rootQuotientMinimumStorageSize r N h

/-- At one execution step the complete capacity dictionary is exactly the
canonical semantic basis, so the completeness tax is zero. -/
theorem rootQuotientCapacityCompletenessStorageTax_one_eq_zero
    {r N : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientCapacityCompletenessStorageTax r N 1 = 0 := by
  rw [rootQuotientCapacityCompletenessStorageTax]
  rw [rootQuotientCanonicalCapacityForHorizon_one]
  rw [rootQuotientOmegaFilteredBasis_exactHorizon_eq_semanticBasis]
  rw [rootQuotientMinimumStorageSize_one_eq_semanticBasis_ncard
    (r := r) (N := N) (by omega)]
  simp

/-- At the exact prime horizon the complete capacity dictionary has collapsed
to the prime core, again matching true minimum storage exactly. -/
theorem rootQuotientCapacityCompletenessStorageTax_exactPrimeHorizon_eq_zero
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientCapacityCompletenessStorageTax
      r N (rootQuotientPrimeHorizon r N) = 0 := by
  rw [rootQuotientCapacityCompletenessStorageTax]
  rw [rootQuotientCanonicalCapacityForHorizon_exactPrimeHorizon_eq_one hLPos]
  rw [rootQuotientOmegaFilteredBasis_one_eq_primeBasis hr]
  rw [rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
    hr hLPos le_rfl]
  simp

/-- At the penultimate prime horizon, completeness tax is exactly the number of
semantic semiprime macro types discarded by a minimum divisor cover. -/
theorem rootQuotientCapacityCompletenessStorageTax_penultimate_eq_semiprimeRedundancy
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientCapacityCompletenessStorageTax
        r N (rootQuotientPrimeHorizon r N - 1) =
      (RootQuotientAllSemanticSemiprimes r N).ncard -
        rootQuotientPenultimateSemiprimeCoverNumber r N := by
  rw [rootQuotientCapacityCompletenessStorageTax]
  rw [rootQuotientCanonicalCapacityForHorizon_penultimate_eq_two hHorizon]
  exact rootQuotientOmegaFilteredBasis_two_ncard_sub_minimumStorage_penultimate
    hr hHorizon

/-- The complete capacity-two dictionary is storage-optimal at the penultimate
horizon iff every semantic semiprime type is required by a minimum cover. -/
theorem rootQuotientOmegaFilteredBasis_two_storageOptimal_penultimate_iff
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    (RootQuotientOmegaFilteredBasis r N 2).ncard =
        rootQuotientMinimumStorageSize
          r N (rootQuotientPrimeHorizon r N - 1) ↔
      rootQuotientPenultimateSemiprimeCoverNumber r N =
        (RootQuotientAllSemanticSemiprimes r N).ncard := by
  rw [rootQuotientOmegaFilteredBasis_two_ncard_eq_prime_add_allSemiprimes hr]
  rw [rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    hr hHorizon]
  omega

/-- Whenever a strict subset of semantic semiprime types covers all maximal
rank boundaries, the complete capacity-two dictionary strictly overstores at
the penultimate horizon. -/
theorem rootQuotientMinimumStorageSize_lt_omegaFilteredBasis_two_of_coverNumber_lt
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hSparse :
      rootQuotientPenultimateSemiprimeCoverNumber r N <
        (RootQuotientAllSemanticSemiprimes r N).ncard) :
    rootQuotientMinimumStorageSize
        r N (rootQuotientPrimeHorizon r N - 1) <
      (RootQuotientOmegaFilteredBasis r N 2).ncard := by
  rw [rootQuotientOmegaFilteredBasis_two_ncard_eq_prime_add_allSemiprimes hr]
  rw [rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    hr hHorizon]
  omega

end EnterpriseMath.Quotient
