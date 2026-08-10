import EnterpriseMath.Quotient.RootQuotientPenultimateStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The penultimate semiprime cover number is positive whenever the prime-only
horizon is at least two. -/
theorem rootQuotientPenultimateSemiprimeCoverNumber_pos
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    1 ≤ rootQuotientPenultimateSemiprimeCoverNumber r N := by
  obtain ⟨S, hSFinite, _hSemi, hCover, hSCard⟩ :=
    exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
  by_contra hNot
  have hTauZero : rootQuotientPenultimateSemiprimeCoverNumber r N = 0 := by
    omega
  have hSZero : S.ncard = 0 := by
    rw [hSCard, hTauZero]
  have hSEmpty : S = ∅ :=
    (Set.ncard_eq_zero hSFinite).1 hSZero
  have hHorizonPos : 0 < rootQuotientPrimeHorizon r N := by omega
  obtain ⟨b, hbPos, hbN, hbFree, hbCount⟩ :=
    exists_powerFree_boundary_at_rootQuotientPrimeHorizon hHorizonPos
  have hbMax : RootQuotientMaximalPrimeRankBoundary r N b :=
    ⟨hbPos, hbN, hbFree, hbCount⟩
  obtain ⟨g, hgS, _hgDvd⟩ := hCover b hbMax
  rw [hSEmpty] at hgS
  exact hgS

/-- A single semantic semiprime covers all maximal-rank boundaries exactly when
it is a common divisor of every such boundary. -/
def RootQuotientCommonMaximalSemiprimeDivisor
    (r N d : ℕ) : Prop :=
  d ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
  rootQuotientPrimeFactorCount d = 2 ∧
  ∀ b : ℕ, RootQuotientMaximalPrimeRankBoundary r N b → d ∣ b

/-- A common maximal semiprime divisor gives a singleton divisor cover. -/
theorem singleton_semiprime_divisorCover_of_common
    {r N d : ℕ}
    (hd : RootQuotientCommonMaximalSemiprimeDivisor r N d) :
    RootQuotientPenultimateSemiprimeFamily r N ({d} : Set ℕ) ∧
    RootQuotientPenultimateDivisorCover r N ({d} : Set ℕ) := by
  constructor
  · constructor
    · intro g hg
      have hgd : g = d := by simpa using hg
      subst g
      exact hd.1
    · intro g hg
      have hgd : g = d := by simpa using hg
      subst g
      exact hd.2.1
  · intro b hbMax
    exact ⟨d, by simp, hd.2.2 b hbMax⟩

/-- Exact singleton-cover criterion.

The minimum penultimate macro count is one iff all maximal-rank boundaries
share one bounded semantic semiprime divisor. -/
theorem rootQuotientPenultimateSemiprimeCoverNumber_eq_one_iff_common
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientPenultimateSemiprimeCoverNumber r N = 1 ↔
      ∃ d : ℕ, RootQuotientCommonMaximalSemiprimeDivisor r N d := by
  constructor
  · intro hTauOne
    obtain ⟨S, _hSFinite, hSemi, hCover, hSCard⟩ :=
      exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
    have hSOne : S.ncard = 1 := by
      rw [hSCard, hTauOne]
    obtain ⟨d, hSEq⟩ := (Set.ncard_eq_one).1 hSOne
    refine ⟨d, ?_⟩
    have hdS : d ∈ S := by
      rw [hSEq]
      simp
    refine ⟨hSemi.1 hdS, hSemi.2 d hdS, ?_⟩
    intro b hbMax
    obtain ⟨g, hgS, hgDvd⟩ := hCover b hbMax
    have hgd : g = d := by
      rw [hSEq] at hgS
      simpa using hgS
    simpa [hgd] using hgDvd
  · rintro ⟨d, hd⟩
    obtain ⟨hSemi, hCover⟩ := singleton_semiprime_divisorCover_of_common hd
    have hUpper :
        rootQuotientPenultimateSemiprimeCoverNumber r N ≤ 1 := by
      have hFinite : ({d} : Set ℕ).Finite := Set.finite_singleton d
      have hLe :=
        rootQuotientPenultimateSemiprimeCoverNumber_le
          hFinite hSemi hCover
      simpa using hLe
    have hLower := rootQuotientPenultimateSemiprimeCoverNumber_pos hHorizon
    omega

/-- The penultimate minimum-storage gap above primes is exactly one iff a
common maximal semantic semiprime divisor exists. -/
theorem rootQuotientMinimumStorageSize_penultimate_eq_prime_add_one_iff_common
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumStorageSize
        r N (rootQuotientPrimeHorizon r N - 1) =
        (RootQuotientPrimeBasis N).ncard + 1 ↔
      ∃ d : ℕ, RootQuotientCommonMaximalSemiprimeDivisor r N d := by
  rw [rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    hr hHorizon]
  have hTauPos := rootQuotientPenultimateSemiprimeCoverNumber_pos hHorizon
  constructor
  · intro hEq
    have hTauOne : rootQuotientPenultimateSemiprimeCoverNumber r N = 1 := by
      omega
    exact
      (rootQuotientPenultimateSemiprimeCoverNumber_eq_one_iff_common
        hHorizon).1 hTauOne
  · intro hCommon
    have hTauOne :=
      (rootQuotientPenultimateSemiprimeCoverNumber_eq_one_iff_common
        hHorizon).2 hCommon
    rw [hTauOne]

end EnterpriseMath.Quotient
