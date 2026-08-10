import EnterpriseMath.Quotient.RootQuotientAlphabetNormalization
import EnterpriseMath.Quotient.RootQuotientOmegaFiltrationGeometry
import EnterpriseMath.Quotient.RootQuotientPrimeHorizonGeometry
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Reachable denominator products are monotone in the primitive alphabet. -/
theorem rootQuotientProductReachableWithin_mono_generators
    {h d : ℕ} {G H : Set ℕ}
    (hGH : G ⊆ H)
    (hReach : RootQuotientProductReachableWithin h G d) :
    RootQuotientProductReachableWithin h H d := by
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  refine ⟨w, hwLen, ?_, hProd⟩
  intro g hg
  exact hGH (hwG g hg)

/-- Required bounded semantic boundaries attaining the exact prime-only rank. -/
def RootQuotientMaximalPrimeRankBoundary
    (r N : ℕ) (b : ℕ) : Prop :=
  1 ≤ b ∧ b ≤ N ∧ RPowerFree r b ∧
    rootQuotientPrimeFactorCount b = rootQuotientPrimeHorizon r N

/-- A semantic macro family suitable for a one-step saving: every selected
macro is a bounded nontrivial power-free denominator with at least two prime
factor tokens. -/
def RootQuotientPenultimateMacroFamily
    (r N : ℕ) (S : Set ℕ) : Prop :=
  S ⊆ RootQuotientNontrivialPowerFreeBasis r N ∧
  ∀ g : ℕ, g ∈ S → 2 ≤ rootQuotientPrimeFactorCount g

/-- A macro family covers every maximal-rank semantic boundary by divisibility. -/
def RootQuotientPenultimateDivisorCover
    (r N : ℕ) (S : Set ℕ) : Prop :=
  ∀ b : ℕ,
    RootQuotientMaximalPrimeRankBoundary r N b →
    ∃ g : ℕ, g ∈ S ∧ g ∣ b

/-- Every positive separator at the penultimate prime horizon supplies a
composite semantic divisor for every maximal-rank boundary.

Identity and irrelevant instructions are first removed by semantic
normalization.  If the normalized compiling word contained only primes, unique
factorization would force its length to be the full prime horizon rather than
one less. -/
theorem exists_composite_semantic_divisor_of_penultimate_separator
    {r N b : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N - 1) G)
    (hbMax : RootQuotientMaximalPrimeRankBoundary r N b) :
    ∃ g : ℕ,
      g ∈ G ∧
      g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      2 ≤ rootQuotientPrimeFactorCount g ∧
      g ∣ b := by
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N)
      (h := rootQuotientPrimeHorizon r N - 1) (G := G)
      (by omega) hGPos).1 hSep
      b hbMax.1 hbMax.2.1 hbMax.2.2.1
  have hNormReach :=
    rootQuotient_reachable_normalize_to_semanticBasis
      hGPos hbMax.1 hbMax.2.1 hbMax.2.2.1 hReach
  obtain ⟨w, hwLen, hwNorm, hProd⟩ := hNormReach
  by_contra hNoComposite
  have hAllPrime : ∀ g : ℕ, g ∈ w → g.Prime := by
    intro g hg
    have hgNorm := hwNorm g hg
    by_contra hgNotPrime
    have hgCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hgNorm.2.1
    have hgNotTwo : ¬2 ≤ rootQuotientPrimeFactorCount g := by
      intro hgTwo
      exact hNoComposite ⟨g, hgNorm.1, hgNorm.2, hgTwo,
        word_member_dvd_compiled_product hg hProd⟩
    have hgOne : rootQuotientPrimeFactorCount g = 1 := by omega
    exact hgNotPrime
      ((rootQuotientPrimeFactorCount_eq_one_iff_prime hgNorm.2.1).1 hgOne)
  have hwPrimeBasis : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro p hp
    have hpPrime : p.Prime := hAllPrime p hp
    have hpDvd : p ∣ b := word_member_dvd_compiled_product hp hProd
    have hpN : p ≤ N :=
      (Nat.le_of_dvd (by omega) hpDvd).trans hbMax.2.1
    exact ⟨hpPrime, hpN⟩
  have hExact : w.length = rootQuotientPrimeFactorCount b :=
    prime_word_length_eq_primeFactorCount hwPrimeBasis hProd.symm
  rw [hbMax.2.2.2] at hExact
  omega

/-- Penultimate-cover necessity: the useful composite semantic generators of
any penultimate separator cover all maximal-rank boundaries by divisibility. -/
theorem penultimate_separator_induces_composite_divisor_cover
    {r N : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N - 1) G) :
    ∀ b : ℕ,
      RootQuotientMaximalPrimeRankBoundary r N b →
      ∃ g : ℕ,
        g ∈ G ∧
        g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
        2 ≤ rootQuotientPrimeFactorCount g ∧
        g ∣ b := by
  intro b hbMax
  exact exists_composite_semantic_divisor_of_penultimate_separator
    hr hHorizon hGPos hSep hbMax

/-- Conversely, a semantic composite-divisor cover of all maximal-rank
boundaries is sufficient together with the forced primes at the penultimate
horizon. -/
theorem prime_union_penultimateMacroCover_separates
    {r N : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hMacro : RootQuotientPenultimateMacroFamily r N S)
    (hCover : RootQuotientPenultimateDivisorCover r N S) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientPrimeBasis N ∪ S) := by
  have hPos :
      PositiveRootQuotientGenerators (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · exact (hMacro.1 hgS).1.trans (by omega)
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N)
    (h := rootQuotientPrimeHorizon r N - 1)
    (G := RootQuotientPrimeBasis N ∪ S)
    (by omega) hPos).2
  intro b hbPos hbN hbFree
  have hBound :=
    (rootQuotientPrimeHorizon_le_iff
      (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
      b hbPos hbN hbFree
  by_cases hLow :
      rootQuotientPrimeFactorCount b ≤ rootQuotientPrimeHorizon r N - 1
  · have hPrimeReach :
        RootQuotientProductReachableWithin
          (rootQuotientPrimeHorizon r N - 1)
          (RootQuotientPrimeBasis N) b :=
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le hbPos hbN).2
        hLow
    exact rootQuotientProductReachableWithin_mono_generators
      (Set.subset_union_left) hPrimeReach
  · have hbMaxCount :
        rootQuotientPrimeFactorCount b = rootQuotientPrimeHorizon r N := by
      omega
    have hbMax : RootQuotientMaximalPrimeRankBoundary r N b :=
      ⟨hbPos, hbN, hbFree, hbMaxCount⟩
    obtain ⟨g, hgS, hgDvd⟩ := hCover b hbMax
    have hgSemantic := hMacro.1 hgS
    have hgCount : 2 ≤ rootQuotientPrimeFactorCount g := hMacro.2 g hgS
    rcases hgDvd with ⟨c, hbc⟩
    have hgPos : 1 ≤ g := by omega
    have hcPos : 1 ≤ c := by
      by_contra hNot
      have hcZero : c = 0 := by omega
      subst c
      simp at hbc
      omega
    have hcN : c ≤ N := by
      have hcDvd : c ∣ b := by
        refine ⟨g, ?_⟩
        simpa [Nat.mul_comm] using hbc
      exact (Nat.le_of_dvd (by omega) hcDvd).trans hbN
    have hCountMul := rootQuotientPrimeFactorCount_mul hgPos hcPos
    have hcCount :
        rootQuotientPrimeFactorCount c ≤
          rootQuotientPrimeHorizon r N - 2 := by
      rw [hbc] at hbMaxCount
      rw [hCountMul] at hbMaxCount
      omega
    have hTailReach :
        RootQuotientProductReachableWithin
          (rootQuotientPrimeHorizon r N - 2)
          (RootQuotientPrimeBasis N) c :=
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le hcPos hcN).2
        hcCount
    obtain ⟨w, hwLen, hwPrime, hProd⟩ := hTailReach
    refine ⟨g :: w, ?_, ?_, ?_⟩
    · simp only [List.length_cons]
      omega
    · intro a ha
      simp at ha
      rcases ha with rfl | haTail
      · exact Or.inr hgS
      · exact Or.inl (hwPrime a haTail)
    · calc
        b = g * c := hbc
        _ = g * rootQuotientWordProduct w := by rw [← hProd]
        _ = rootQuotientWordProduct (g :: w) := by rfl

end EnterpriseMath.Quotient
