import EnterpriseMath.Quotient.RootQuotientPenultimateCover
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A bounded semantic semiprime family: every selected macro carries exactly
two prime-factor tokens. -/
def RootQuotientPenultimateSemiprimeFamily
    (r N : ℕ) (S : Set ℕ) : Prop :=
  S ⊆ RootQuotientNontrivialPowerFreeBasis r N ∧
  ∀ g : ℕ, g ∈ S → rootQuotientPrimeFactorCount g = 2

/-- Every semantic semiprime family is a valid penultimate macro family. -/
theorem penultimateSemiprimeFamily_is_macroFamily
    {r N : ℕ} {S : Set ℕ}
    (hSemi : RootQuotientPenultimateSemiprimeFamily r N S) :
    RootQuotientPenultimateMacroFamily r N S := by
  refine ⟨hSemi.1, ?_⟩
  intro g hg
  rw [hSemi.2 g hg]

/-- Exact semiprime divisor-cover criterion at the penultimate prime horizon.

Once the bounded primes are included, a semantic semiprime set separates at
horizon `L_r(N)-1` iff its divisibility neighborhoods cover every required
boundary of maximal prime-factor rank. -/
theorem prime_union_semiprimeFamily_separates_penultimate_iff_divisorCover
    {r N : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hSemi : RootQuotientPenultimateSemiprimeFamily r N S) :
    SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientPrimeBasis N ∪ S) ↔
      RootQuotientPenultimateDivisorCover r N S := by
  constructor
  · intro hSep b hbMax
    have hPos :
        PositiveRootQuotientGenerators (RootQuotientPrimeBasis N ∪ S) := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · exact (hSemi.1 hgS).1.trans (by omega)
    obtain ⟨g, hgUnion, _hgSemantic, hgCount, hgDvd⟩ :=
      exists_composite_semantic_divisor_of_penultimate_separator
        hr hHorizon hPos hSep hbMax
    have hgS : g ∈ S := by
      rcases hgUnion with hgPrime | hgS
      · have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime hgPrime.1]
          simp
        omega
      · exact hgS
    exact ⟨g, hgS, hgDvd⟩
  · intro hCover
    exact prime_union_penultimateMacroCover_separates
      hr hHorizon (penultimateSemiprimeFamily_is_macroFamily hSemi) hCover

/-- Every semantic composite macro contains a semantic semiprime divisor. -/
theorem exists_semiprime_semantic_divisor
    {r N g : ℕ}
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgCompositeRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    ∃ d : ℕ,
      d ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      rootQuotientPrimeFactorCount d = 2 ∧
      d ∣ g := by
  by_cases hEq : rootQuotientPrimeFactorCount g = 2
  · exact ⟨g, hgSemantic, hEq, dvd_rfl⟩
  · have hTwoLt : 2 < rootQuotientPrimeFactorCount g := by omega
    obtain ⟨d, _c, hdTwo, _hcTwo, hdDvd, _hcDvd,
        hdFree, _hcFree, _hProd, hdCount, _hcCount⟩ :=
      exists_rPowerFree_factor_split_at_primeFactorCount
        (by omega) hgSemantic.2.2 (by omega) hTwoLt
    have hdN : d ≤ N :=
      (Nat.le_of_dvd (by omega) hdDvd).trans hgSemantic.2.1
    exact ⟨d, ⟨hdTwo, hdN, hdFree⟩, hdCount, hdDvd⟩

/-- The complete semantic semiprime family always covers the maximal-rank
boundaries when the exact prime horizon is at least two. -/
def RootQuotientAllSemanticSemiprimes (r N : ℕ) : Set ℕ :=
  {d : ℕ |
    d ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
    rootQuotientPrimeFactorCount d = 2}

/-- The complete bounded semantic semiprime family is a valid semiprime family. -/
theorem allSemanticSemiprimes_is_family
    {r N : ℕ} :
    RootQuotientPenultimateSemiprimeFamily
      r N (RootQuotientAllSemanticSemiprimes r N) := by
  constructor
  · intro d hd
    exact hd.1
  · intro d hd
    exact hd.2

/-- Every maximal-rank boundary is divisible by some bounded semantic
semiprime whenever `L_r(N)>=2`. -/
theorem allSemanticSemiprimes_cover_maximalBoundaries
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientPenultimateDivisorCover
      r N (RootQuotientAllSemanticSemiprimes r N) := by
  intro b hbMax
  have hRank : 2 ≤ rootQuotientPrimeFactorCount b := by
    rw [hbMax.2.2.2]
    exact hHorizon
  obtain ⟨d, hdSemantic, hdCount, hdDvd⟩ :=
    exists_semiprime_semantic_divisor
      ⟨by
        have hbTwo : 2 ≤ b := by
          have hCountPos : 0 < rootQuotientPrimeFactorCount b := by omega
          by_contra hNot
          have hbOne : b = 1 := by omega
          subst b
          simp [rootQuotientPrimeFactorCount] at hCountPos
        exact hbTwo,
        hbMax.2.1,
        hbMax.2.2.1⟩
      hRank
  exact ⟨d, ⟨hdSemantic, hdCount⟩, hdDvd⟩

end EnterpriseMath.Quotient
