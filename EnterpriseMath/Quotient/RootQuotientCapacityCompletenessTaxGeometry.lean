import EnterpriseMath.Quotient.RootQuotientCapacityCompletenessTax
import EnterpriseMath.Quotient.RootQuotientMacroEndpoints
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Composite part of the complete canonical capacity-filtered dictionary
selected for execution horizon `h`. -/
def RootQuotientCanonicalCapacityCompositePart
    (r N h : ℕ) : Set ℕ :=
  RootQuotientOmegaFilteredBasis
      r N (rootQuotientCanonicalCapacityForHorizon r N h) \
    RootQuotientPrimeBasis N

/-- The selected complete capacity dictionary contains the forced prime core
whenever the selected capacity is positive. -/
theorem rootQuotientPrimeBasis_subset_canonicalCapacityBasis
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    RootQuotientPrimeBasis N ⊆
      RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h) := by
  have hkPos : 1 ≤ rootQuotientCanonicalCapacityForHorizon r N h :=
    rootQuotientCanonicalCapacityForHorizon_pos hLPos hh
  intro p hp
  have hCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hp.1]
    simp
  exact ⟨hp.1.two_le, hp.2, prime_rPowerFree hr hp.1, by omega⟩

/-- The selected complete capacity dictionary decomposes into forced primes and
its composite remainder. -/
theorem canonicalCapacityBasis_eq_prime_union_compositePart
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h) =
      RootQuotientPrimeBasis N ∪
        RootQuotientCanonicalCapacityCompositePart r N h := by
  have hPrimeSub :=
    rootQuotientPrimeBasis_subset_canonicalCapacityBasis hr hLPos hh
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

/-- Exact cardinal decomposition of the selected complete capacity dictionary. -/
theorem canonicalCapacityBasis_ncard_eq_prime_add_compositePart
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    (RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h)).ncard =
      (RootQuotientPrimeBasis N).ncard +
        (RootQuotientCanonicalCapacityCompositePart r N h).ncard := by
  have hPrimeSub :=
    rootQuotientPrimeBasis_subset_canonicalCapacityBasis hr hLPos hh
  have hFinite :
      (RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h)).Finite :=
    rootQuotientOmegaFilteredBasis_finite
  have hDecomp :
      (RootQuotientCanonicalCapacityCompositePart r N h).ncard +
        (RootQuotientPrimeBasis N).ncard =
      (RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h)).ncard := by
    exact Set.ncard_sdiff_add_ncard_of_subset hPrimeSub hFinite
  omega

/-- The complete selected composite macro family always contains at least as
many macro types as a true minimum macro presentation at the same horizon. -/
theorem minimumCompositeMacroCount_le_canonicalCapacityCompositePart_ncard
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h ≤
      (RootQuotientCanonicalCapacityCompositePart r N h).ncard := by
  have hStorageUpper :=
    rootQuotientMinimumStorageSize_le_canonicalCapacityEnvelope
      hr hLPos hh
  have hTrueDecomp :=
    rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      (r := r) (N := N) (h := h) hr hh
  have hCanonicalDecomp :=
    canonicalCapacityBasis_ncard_eq_prime_add_compositePart
      (r := r) (N := N) (h := h) hr hLPos hh
  rw [hTrueDecomp, hCanonicalDecomp] at hStorageUpper
  omega

/-- General exact interpretation of capacity-completeness storage tax.

After removing the common forced prime core, the tax is precisely the number of
extra composite macro types stored by the complete capacity-filtered dictionary
beyond a true minimum macro presentation. -/
theorem rootQuotientCapacityCompletenessStorageTax_eq_compositeRedundancy
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    rootQuotientCapacityCompletenessStorageTax r N h =
      (RootQuotientCanonicalCapacityCompositePart r N h).ncard -
        rootQuotientMinimumCompositeMacroCount r N h := by
  rw [rootQuotientCapacityCompletenessStorageTax]
  rw [canonicalCapacityBasis_ncard_eq_prime_add_compositePart
    hr hLPos hh]
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  have hLe :=
    minimumCompositeMacroCount_le_canonicalCapacityCompositePart_ncard
      hr hLPos hh
  omega

/-- The complete capacity envelope is storage-optimal exactly when its
composite part already has minimum possible cardinality. -/
theorem rootQuotientCapacityCompletenessStorageTax_eq_zero_iff_compositeOptimal
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    rootQuotientCapacityCompletenessStorageTax r N h = 0 ↔
      (RootQuotientCanonicalCapacityCompositePart r N h).ncard =
        rootQuotientMinimumCompositeMacroCount r N h := by
  rw [rootQuotientCapacityCompletenessStorageTax_eq_compositeRedundancy
    hr hLPos hh]
  have hLe :=
    minimumCompositeMacroCount_le_canonicalCapacityCompositePart_ncard
      hr hLPos hh
  omega

/-- Strict positive completeness tax is exactly strict composite-macro
over-storage. -/
theorem rootQuotientCapacityCompletenessStorageTax_pos_iff_compositeOverstored
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    0 < rootQuotientCapacityCompletenessStorageTax r N h ↔
      rootQuotientMinimumCompositeMacroCount r N h <
        (RootQuotientCanonicalCapacityCompositePart r N h).ncard := by
  rw [rootQuotientCapacityCompletenessStorageTax_eq_compositeRedundancy
    hr hLPos hh]
  have hLe :=
    minimumCompositeMacroCount_le_canonicalCapacityCompositePart_ncard
      hr hLPos hh
  omega

end EnterpriseMath.Quotient
