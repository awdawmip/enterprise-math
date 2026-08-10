import EnterpriseMath.Quotient.RootQuotientCollectiveNecessity
import EnterpriseMath.Quotient.RootQuotientMinimumStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The bounded prime primitive alphabet is finite. -/
theorem rootQuotientPrimeBasis_finite
    {N : ℕ} :
    (RootQuotientPrimeBasis N).Finite := by
  apply Set.finite_Icc.subset
  intro p hp
  exact ⟨hp.1.two_le, hp.2⟩

/-- At horizon one, the normalized finite storage optimizer is exactly the
canonical nontrivial power-free semantic basis. -/
theorem rootQuotientMinimumStorageSize_one_eq_semanticBasis_ncard
    {r N : ℕ}
    (hr : 1 ≤ r) :
    rootQuotientMinimumStorageSize r N 1 =
      (RootQuotientNontrivialPowerFreeBasis r N).ncard := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := 1) hr (by omega)
  have hSemanticSubG :
      RootQuotientNontrivialPowerFreeBasis r N ⊆ G :=
    rootQuotientNontrivialPowerFreeBasis_subset_of_one_step_separates
      hr hG.2.2.1 hG.2.2.2
  have hGSubSemantic :
      G ⊆ RootQuotientNontrivialPowerFreeBasis r N := hG.1
  have hEq : G = RootQuotientNontrivialPowerFreeBasis r N :=
    Set.Subset.antisymm hGSubSemantic hSemanticSubG
  rw [← hGCard, hEq]

/-- Once the execution horizon reaches the exact prime-only horizon, minimum
storage is exactly the bounded prime-core cardinality. -/
theorem rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hHorizon : rootQuotientPrimeHorizon r N ≤ h) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard := by
  have hPrimeStorage :
      RootQuotientFiniteStorageSeparator r N h (RootQuotientPrimeBasis N) := by
    refine ⟨rootQuotientPrimeBasis_subset_semanticBasis hr,
      rootQuotientPrimeBasis_finite,
      rootQuotientPrimeBasis_positive, ?_⟩
    exact (rootQuotientPrimeBasis_separates_iff_horizon_le
      (r := r) (N := N) (h := h) (by omega)).2 hHorizon
  have hUpper :
      rootQuotientMinimumStorageSize r N h ≤
        (RootQuotientPrimeBasis N).ncard :=
    rootQuotientMinimumStorageSize_le_normalized hPrimeStorage
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) (by omega) hh
  have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates
      hr hG.2.2.1 hG.2.2.2
  have hLower : (RootQuotientPrimeBasis N).ncard ≤ G.ncard :=
    Set.ncard_le_ncard hPrimeSubG hG.2.1
  rw [hGCard] at hLower
  exact Nat.le_antisymm hUpper hLower

/-- In the intermediate no-least phase, minimum finite storage is strictly
larger than the forced prime core: at least one additional composite semantic
primitive type is unavoidable. -/
theorem primeBasis_ncard_lt_rootQuotientMinimumStorageSize_of_intermediate
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    (RootQuotientPrimeBasis N).ncard <
      rootQuotientMinimumStorageSize r N h := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) (by omega) (by omega)
  have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates
      hr hG.2.2.1 hG.2.2.2
  obtain ⟨g, hgG, _hgSemantic, hgNotPrime⟩ :=
    exists_composite_semantic_generator_of_intermediate_separator
      hr hh hBelow hG.2.2.1 hG.2.2.2
  have hgNotPrimeBasis : g ∉ RootQuotientPrimeBasis N := by
    intro hgPrime
    exact hgNotPrime hgPrime.1
  have hStrict : RootQuotientPrimeBasis N ⊂ G := by
    exact Set.ssubset_iff_subset_ne.mpr
      ⟨hPrimeSubG, by
        intro hEq
        have hgPrimeBasis : g ∈ RootQuotientPrimeBasis N := by
          rw [hEq]
          exact hgG
        exact hgNotPrimeBasis hgPrimeBasis⟩
  have hCardStrict :
      (RootQuotientPrimeBasis N).ncard < G.ncard :=
    Set.ncard_lt_ncard hStrict hG.2.1
  simpa [hGCard] using hCardStrict

/-- Quantitative intermediate storage lower bound: at least one primitive type
beyond the forced prime core is required. -/
theorem primeBasis_ncard_add_one_le_rootQuotientMinimumStorageSize_of_intermediate
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    (RootQuotientPrimeBasis N).ncard + 1 ≤
      rootQuotientMinimumStorageSize r N h := by
  exact Nat.succ_le_iff.mpr
    (primeBasis_ncard_lt_rootQuotientMinimumStorageSize_of_intermediate
      hr hh hBelow)

/-- Storage phase summary: semantic-cardinality endpoint at one step, prime
cardinality endpoint after the exact prime horizon, and a strict gap above the
prime core throughout the intermediate phase. -/
theorem rootQuotientMinimumStorage_phase_summary
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (h < rootQuotientPrimeHorizon r N →
      (RootQuotientPrimeBasis N).ncard + 1 ≤
        rootQuotientMinimumStorageSize r N h) ∧
    (rootQuotientPrimeHorizon r N ≤ h →
      rootQuotientMinimumStorageSize r N h =
        (RootQuotientPrimeBasis N).ncard) := by
  constructor
  · intro hBelow
    exact primeBasis_ncard_add_one_le_rootQuotientMinimumStorageSize_of_intermediate
      hr hh hBelow
  · intro hHorizon
    exact rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
      hr (by omega) hHorizon

end EnterpriseMath.Quotient
