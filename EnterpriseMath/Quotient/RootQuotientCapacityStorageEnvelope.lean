import EnterpriseMath.Quotient.RootQuotientCompilerAsymmetry
import EnterpriseMath.Quotient.RootQuotientCompilerDistance
import EnterpriseMath.Quotient.RootQuotientMinimumStoragePhase
import EnterpriseMath.Quotient.RootQuotientPenultimateCoverGeometry
import Mathlib.Algebra.Order.Floor.Div
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Smallest per-instruction `Omega` capacity in the canonical complete
filtration that can meet execution horizon `h`. -/
def rootQuotientCanonicalCapacityForHorizon
    (r N h : ℕ) : ℕ :=
  rootQuotientPrimeHorizon r N ⌈/⌉ h

/-- For positive exact prime horizon and positive execution budget, the
canonical capacity selected by ceiling division is itself positive. -/
theorem rootQuotientCanonicalCapacityForHorizon_pos
    {r N h : ℕ}
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    1 ≤ rootQuotientCanonicalCapacityForHorizon r N h := by
  by_contra hNot
  have hZero : rootQuotientCanonicalCapacityForHorizon r N h = 0 := by omega
  have hBound :
      rootQuotientPrimeHorizon r N ≤ h * 0 := by
    have hCeil :
        rootQuotientPrimeHorizon r N ⌈/⌉ h ≤ 0 := by
      simpa [rootQuotientCanonicalCapacityForHorizon, hZero]
    exact (ceilDiv_le_iff_le_mul (by omega)).1 hCeil
  omega

/-- The canonical capacity envelope always gives a valid finite presentation
at the requested positive horizon. -/
theorem rootQuotientCanonicalCapacityBasis_separates
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h)) := by
  let k := rootQuotientCanonicalCapacityForHorizon r N h
  have hkPos : 1 ≤ k :=
    rootQuotientCanonicalCapacityForHorizon_pos hLPos hh
  apply (rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
    (r := r) (N := N) (k := k) (h := h) hr hkPos).2
  have hCeil : rootQuotientPrimeHorizon r N ⌈/⌉ h ≤ k := by
    rfl
  have hBound : rootQuotientPrimeHorizon r N ≤ h * k :=
    (ceilDiv_le_iff_le_mul (by omega)).1 hCeil
  simpa [Nat.mul_comm] using hBound

/-- True minimum storage is bounded above by the complete canonical
capacity-filtered dictionary selected for the same horizon. -/
theorem rootQuotientMinimumStorageSize_le_canonicalCapacityEnvelope
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    rootQuotientMinimumStorageSize r N h ≤
      (RootQuotientOmegaFilteredBasis
        r N (rootQuotientCanonicalCapacityForHorizon r N h)).ncard := by
  let k := rootQuotientCanonicalCapacityForHorizon r N h
  have hSemantic :
      RootQuotientOmegaFilteredBasis r N k ⊆
        RootQuotientNontrivialPowerFreeBasis r N := by
    intro g hg
    exact ⟨hg.1, hg.2.1, hg.2.2.1⟩
  have hFinite : (RootQuotientOmegaFilteredBasis r N k).Finite :=
    rootQuotientOmegaFilteredBasis_finite
  have hPos : PositiveRootQuotientGenerators
      (RootQuotientOmegaFilteredBasis r N k) :=
    rootQuotientOmegaFilteredBasis_positive
  have hSep : SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis r N k) := by
    dsimp [k]
    exact rootQuotientCanonicalCapacityBasis_separates
      (by omega) hLPos hh
  exact rootQuotientMinimumStorageSize_le_normalized
    ⟨hSemantic, hFinite, hPos, hSep⟩

/-- At one step, the canonical capacity envelope is exactly the full semantic
basis. -/
theorem rootQuotientCanonicalCapacityForHorizon_one
    {r N : ℕ} :
    rootQuotientCanonicalCapacityForHorizon r N 1 =
      rootQuotientPrimeHorizon r N := by
  simp [rootQuotientCanonicalCapacityForHorizon, Nat.ceilDiv_eq_add_pred_div]

/-- At the exact prime horizon, the canonical required capacity is one whenever
that horizon is positive. -/
theorem rootQuotientCanonicalCapacityForHorizon_exactPrimeHorizon_eq_one
    {r N : ℕ}
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientCanonicalCapacityForHorizon
      r N (rootQuotientPrimeHorizon r N) = 1 := by
  let L := rootQuotientPrimeHorizon r N
  apply Nat.le_antisymm
  · have hBound : L ≤ L * 1 := by simp
    have hCeil : L ⌈/⌉ L ≤ 1 :=
      (ceilDiv_le_iff_le_mul (by omega)).2 hBound
    simpa [L, rootQuotientCanonicalCapacityForHorizon] using hCeil
  · exact rootQuotientCanonicalCapacityForHorizon_pos hLPos hLPos

/-- At the penultimate prime horizon, the complete canonical capacity envelope
uses capacity two. -/
theorem rootQuotientCanonicalCapacityForHorizon_penultimate_eq_two
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientCanonicalCapacityForHorizon
      r N (rootQuotientPrimeHorizon r N - 1) = 2 := by
  let L := rootQuotientPrimeHorizon r N
  let h := L - 1
  have hh : 1 ≤ h := by omega
  have hUpperBudget : L ≤ h * 2 := by
    dsimp [h]
    omega
  have hUpper : L ⌈/⌉ h ≤ 2 :=
    (ceilDiv_le_iff_le_mul (by omega)).2 hUpperBudget
  have hNotOne : ¬L ⌈/⌉ h ≤ 1 := by
    intro hOne
    have hBad : L ≤ h * 1 :=
      (ceilDiv_le_iff_le_mul (by omega)).1 hOne
    dsimp [h] at hBad
    omega
  have hEq : L ⌈/⌉ h = 2 := by omega
  simpa [L, h, rootQuotientCanonicalCapacityForHorizon] using hEq

/-- Capacity-two semantic dictionary decomposes exactly into bounded primes and
all bounded semantic semiprimes. -/
theorem rootQuotientOmegaFilteredBasis_two_eq_prime_union_allSemanticSemiprimes
    {r N : ℕ}
    (hr : 2 ≤ r) :
    RootQuotientOmegaFilteredBasis r N 2 =
      RootQuotientPrimeBasis N ∪ RootQuotientAllSemanticSemiprimes r N := by
  apply Set.Subset.antisymm
  · intro g hg
    have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hg.1
    have hCountCases :
        rootQuotientPrimeFactorCount g = 1 ∨
          rootQuotientPrimeFactorCount g = 2 := by omega
    rcases hCountCases with hOne | hTwo
    · left
      exact ⟨
        (rootQuotientPrimeFactorCount_eq_one_iff_prime hg.1).1 hOne,
        hg.2.1⟩
    · right
      exact ⟨⟨hg.1, hg.2.1, hg.2.2.1⟩, hTwo⟩
  · intro g hg
    rcases hg with hgPrime | hgSemi
    · have hCount : rootQuotientPrimeFactorCount g = 1 := by
        rw [rootQuotientPrimeFactorCount,
          Nat.primeFactorsList_prime hgPrime.1]
        simp
      exact ⟨hgPrime.1.two_le, hgPrime.2,
        prime_rPowerFree hr hgPrime.1, by omega⟩
    · exact ⟨hgSemi.1.1, hgSemi.1.2.1, hgSemi.1.2.2, by rw [hgSemi.2]⟩

/-- Exact storage size of the complete capacity-two dictionary. -/
theorem rootQuotientOmegaFilteredBasis_two_ncard_eq_prime_add_allSemiprimes
    {r N : ℕ}
    (hr : 2 ≤ r) :
    (RootQuotientOmegaFilteredBasis r N 2).ncard =
      (RootQuotientPrimeBasis N).ncard +
        (RootQuotientAllSemanticSemiprimes r N).ncard := by
  rw [rootQuotientOmegaFilteredBasis_two_eq_prime_union_allSemanticSemiprimes hr]
  have hSemi : RootQuotientPenultimateSemiprimeFamily
      r N (RootQuotientAllSemanticSemiprimes r N) :=
    allSemanticSemiprimes_is_family
  exact Set.ncard_union_eq
    (rootQuotientPrimeBasis_disjoint_semiprimeFamily hSemi)
    rootQuotientPrimeBasis_finite
    (rootQuotientNontrivialPowerFreeBasis_finite.subset fun d hd => hd.1)

/-- At the penultimate horizon, the over-storage of the complete capacity-two
filtration dictionary over the true optimum is exactly the redundancy of
storing every semantic semiprime rather than a minimum divisor cover. -/
theorem rootQuotientOmegaFilteredBasis_two_ncard_sub_minimumStorage_penultimate
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    (RootQuotientOmegaFilteredBasis r N 2).ncard -
      rootQuotientMinimumStorageSize
        r N (rootQuotientPrimeHorizon r N - 1) =
      (RootQuotientAllSemanticSemiprimes r N).ncard -
        rootQuotientPenultimateSemiprimeCoverNumber r N := by
  rw [rootQuotientOmegaFilteredBasis_two_ncard_eq_prime_add_allSemiprimes hr]
  rw [rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    hr hHorizon]
  have hTauLe :
      rootQuotientPenultimateSemiprimeCoverNumber r N ≤
        (RootQuotientAllSemanticSemiprimes r N).ncard := by
    exact rootQuotientPenultimateSemiprimeCoverNumber_le
      (rootQuotientNontrivialPowerFreeBasis_finite.subset fun d hd => hd.1)
      allSemanticSemiprimes_is_family
      (allSemanticSemiprimes_cover_maximalBoundaries hHorizon)
  omega

end EnterpriseMath.Quotient
