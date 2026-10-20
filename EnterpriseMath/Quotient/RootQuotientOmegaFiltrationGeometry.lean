import EnterpriseMath.Quotient.RootQuotientOmegaFiltration
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The canonical `Omega`-filtered alphabets are nested by instruction
capacity. -/
theorem rootQuotientOmegaFilteredBasis_mono
    {r N k j : ℕ}
    (hkj : k ≤ j) :
    RootQuotientOmegaFilteredBasis r N k ⊆
      RootQuotientOmegaFilteredBasis r N j := by
  intro g hg
  exact ⟨hg.1, hg.2.1, hg.2.2.1, hg.2.2.2.trans hkj⟩

/-- Every nontrivial bounded power-free semantic denominator belongs to the
`Omega`-filtered alphabet at the exact prime-only horizon. -/
theorem rootQuotientNontrivialPowerFreeBasis_subset_omegaFiltered_exactHorizon
    {r N : ℕ} :
    RootQuotientNontrivialPowerFreeBasis r N ⊆
      RootQuotientOmegaFilteredBasis
        r N (rootQuotientPrimeHorizon r N) := by
  intro b hb
  have hBound :=
    (rootQuotientPrimeHorizon_le_iff
      (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
  exact ⟨hb.1, hb.2.1, hb.2.2,
    hBound b (by omega) hb.2.1 hb.2.2⟩

/-- The exact-horizon endpoint of the canonical `Omega` filtration is exactly
the complete nontrivial one-step semantic action basis. -/
theorem rootQuotientOmegaFilteredBasis_exactHorizon_eq_semanticBasis
    {r N : ℕ} :
    RootQuotientOmegaFilteredBasis
      r N (rootQuotientPrimeHorizon r N) =
      RootQuotientNontrivialPowerFreeBasis r N := by
  apply Set.Subset.antisymm
  · intro g hg
    exact ⟨hg.1, hg.2.1, hg.2.2.1⟩
  · exact
      rootQuotientNontrivialPowerFreeBasis_subset_omegaFiltered_exactHorizon

/-- A nontrivial natural number has positive project prime-factor count. -/
theorem rootQuotientPrimeFactorCount_pos_of_two_le
    {g : ℕ}
    (hgTwo : 2 ≤ g) :
    0 < rootQuotientPrimeFactorCount g := by
  have hNeNil : g.primeFactorsList ≠ [] :=
    (Nat.primeFactorsList_ne_nil g).2 (by omega)
  have hLenPos : 0 < g.primeFactorsList.length :=
    List.length_pos_iff.mpr hNeNil
  simpa [rootQuotientPrimeFactorCount] using hLenPos

/-- Prime-factor count one is exactly primality for nontrivial naturals. -/
theorem rootQuotientPrimeFactorCount_eq_one_iff_prime
    {g : ℕ}
    (hgTwo : 2 ≤ g) :
    rootQuotientPrimeFactorCount g = 1 ↔ g.Prime := by
  simpa [rootQuotientPrimeFactorCount,
    ArithmeticFunction.cardFactors_apply] using
    (ArithmeticFunction.cardFactors_eq_one_iff_prime (n := g))

/-- For root order at least two, capacity one is exactly the bounded prime
primitive alphabet. -/
theorem rootQuotientOmegaFilteredBasis_one_eq_primeBasis
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientOmegaFilteredBasis r N 1 = RootQuotientPrimeBasis N := by
  apply Set.Subset.antisymm
  · intro g hg
    have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hg.1
    have hCountOne : rootQuotientPrimeFactorCount g = 1 := by
      omega
    exact ⟨
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hg.1).1 hCountOne,
      hg.2.1⟩
  · intro p hp
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hp.1]
      simp
    exact ⟨hp.1.two_le, hp.2, prime_rPowerFree hr hp.1, by omega⟩

/-- Filtration summary: for `r≥2`, capacity one starts at primes, the family
is nested, and capacity `L_r(N)` reaches the complete one-step semantic basis. -/
theorem rootQuotientOmegaFiltration_endpoints
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientOmegaFilteredBasis r N 1 = RootQuotientPrimeBasis N ∧
    RootQuotientOmegaFilteredBasis
      r N (rootQuotientPrimeHorizon r N) =
      RootQuotientNontrivialPowerFreeBasis r N := by
  exact ⟨rootQuotientOmegaFilteredBasis_one_eq_primeBasis hr,
    rootQuotientOmegaFilteredBasis_exactHorizon_eq_semanticBasis⟩

end EnterpriseMath.Quotient
