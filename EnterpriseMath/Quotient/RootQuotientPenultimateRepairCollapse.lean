import EnterpriseMath.Quotient.RootQuotientMacroRepairEquivalence
import EnterpriseMath.Quotient.RootQuotientMacroPareto
import EnterpriseMath.Quotient.RootQuotientPenultimateStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Finite maximal-rank semantic target family at the penultimate prime
horizon. -/
noncomputable def RootQuotientMaximalPrimeRankBoundaryFinset
    (r N : ℕ) : Finset ℕ :=
  (RootQuotientSemanticTargetFinset r N).filter
    (fun b =>
      rootQuotientPrimeFactorCount b = rootQuotientPrimeHorizon r N)

/-- Membership in the finite maximal-rank target family is exactly the existing
maximal-boundary predicate once the prime horizon is nontrivial. -/
theorem mem_maximalPrimeRankBoundaryFinset_iff
    {r N b : ℕ}
    (hHorizon : 1 ≤ rootQuotientPrimeHorizon r N) :
    b ∈ RootQuotientMaximalPrimeRankBoundaryFinset r N ↔
      RootQuotientMaximalPrimeRankBoundary r N b := by
  constructor
  · intro hb
    have hbFilter := Finset.mem_filter.1 hb
    have hbSemantic : b ∈ RootQuotientNontrivialPowerFreeBasis r N :=
      (mem_rootQuotientSemanticTargetFinset_iff).1 hbFilter.1
    exact ⟨by omega, hbSemantic.2.1, hbSemantic.2.2, hbFilter.2⟩
  · intro hbMax
    have hbTwo : 2 ≤ b := by
      by_contra hNot
      have hbOne : b = 1 := by omega
      have hCountEq := hbMax.2.2.2
      rw [hbOne] at hCountEq
      have hCountOne : rootQuotientPrimeFactorCount 1 = 0 := by
        simp [rootQuotientPrimeFactorCount]
      rw [hCountOne] at hCountEq
      omega
    apply Finset.mem_filter.2
    exact ⟨
      (mem_rootQuotientSemanticTargetFinset_iff).2
        ⟨hbTwo, hbMax.2.1, hbMax.2.2.1⟩,
      hbMax.2.2.2⟩

/-- Every semantic-semiprime penultimate cover is also a cover in the general
semantic-composite repair relaxation. -/
theorem semiprimeCover_is_semanticComposite_repairDivisorCover
    {r N : ℕ} {S : Set ℕ}
    (hHorizon : 1 ≤ rootQuotientPrimeHorizon r N)
    (hSemi : RootQuotientPenultimateSemiprimeFamily r N S)
    (hCover : RootQuotientPenultimateDivisorCover r N S) :
    RootQuotientRepairDivisorCover
      (RootQuotientMaximalPrimeRankBoundaryFinset r N)
      (RootQuotientSemanticCompositeCandidates r N)
      S := by
  constructor
  · intro g hgS
    have hgSemantic := hSemi.1 hgS
    refine ⟨hgSemantic, ?_⟩
    intro hgPrime
    have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hgPrime.1]
      simp
    have hSemiCount := hSemi.2 g hgS
    omega
  · intro b hbFin
    have hbMax :=
      (mem_maximalPrimeRankBoundaryFinset_iff hHorizon).1 hbFin
    exact hCover b hbMax

/-- Any finite semantic-composite divisor cover of the maximal-rank boundary
family can be projected to a semantic-semiprime cover without increasing the
number of stored types. -/
theorem exists_semiprimeCover_ncard_le_of_semanticComposite_repairCover
    {r N : ℕ} {S : Set ℕ}
    (hHorizon : 1 ≤ rootQuotientPrimeHorizon r N)
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover
      (RootQuotientMaximalPrimeRankBoundaryFinset r N)
      (RootQuotientSemanticCompositeCandidates r N)
      S) :
    ∃ S' : Set ℕ,
      S'.Finite ∧
      RootQuotientPenultimateSemiprimeFamily r N S' ∧
      RootQuotientPenultimateDivisorCover r N S' ∧
      S'.ncard ≤ S.ncard := by
  classical
  let f : ℕ → ℕ := rootQuotientChosenSemiprimeDivisor r N
  let S' : Set ℕ := f '' S
  have hRank : ∀ g : ℕ, g ∈ S →
      2 ≤ rootQuotientPrimeFactorCount g := by
    intro g hgS
    have hgC := hCover.1 hgS
    have hgSemantic := hgC.1
    have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hgSemantic.1
    by_contra hNot
    have hCountOne : rootQuotientPrimeFactorCount g = 1 := by omega
    have hgPrime : g.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hgSemantic.1).1 hCountOne
    exact hgC.2 ⟨hgPrime, hgSemantic.2.1⟩
  have hS'Finite : S'.Finite := hSFinite.image f
  have hSemi : RootQuotientPenultimateSemiprimeFamily r N S' := by
    constructor
    · intro d hd
      rcases hd with ⟨g, hgS, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec
        (hCover.1 hgS).1 (hRank g hgS)).1
    · intro d hd
      rcases hd with ⟨g, hgS, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec
        (hCover.1 hgS).1 (hRank g hgS)).2.1
  have hPenCover : RootQuotientPenultimateDivisorCover r N S' := by
    intro b hbMax
    have hbFin : b ∈ RootQuotientMaximalPrimeRankBoundaryFinset r N :=
      (mem_maximalPrimeRankBoundaryFinset_iff hHorizon).2 hbMax
    obtain ⟨g, hgS, hgDvd⟩ := hCover.2 b hbFin
    have hSpec := rootQuotientChosenSemiprimeDivisor_spec
      (hCover.1 hgS).1 (hRank g hgS)
    exact ⟨f g, ⟨g, hgS, rfl⟩, hSpec.2.2.trans hgDvd⟩
  have hCard : S'.ncard ≤ S.ncard := by
    dsimp [S']
    exact Set.ncard_image_le hSFinite
  exact ⟨S', hS'Finite, hSemi, hPenCover, hCard⟩

/-- **Penultimate divisor-cover collapse.**

The first-order semantic-composite divisor-cover relaxation has exactly the same
minimum cardinality as the semantic-semiprime cover problem at the penultimate
prime horizon. -/
theorem penultimateRepairDivisorCoverNumber_eq_semiprimeCoverNumber
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientRepairDivisorCoverNumber
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientPenultimateSemiprimeCoverNumber r N := by
  apply Nat.le_antisymm
  · obtain ⟨S, hSFinite, hSemi, hPenCover, hSCard⟩ :=
      exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
    have hGeneric : RootQuotientRepairDivisorCover
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
      semiprimeCover_is_semanticComposite_repairDivisorCover
        (by omega) hSemi hPenCover
    have hLe := rootQuotientRepairDivisorCoverNumber_le hSFinite hGeneric
    rw [hSCard] at hLe
    exact hLe
  · obtain ⟨S₀, hS₀Finite, hSemi₀, hPenCover₀, _hS₀Card⟩ :=
      exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
    have hGeneric₀ : RootQuotientRepairDivisorCover
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S₀ :=
      semiprimeCover_is_semanticComposite_repairDivisorCover
        (by omega) hSemi₀ hPenCover₀
    have hFeasible : ∃ S : Set ℕ,
        S.Finite ∧
        RootQuotientRepairDivisorCover
          (RootQuotientMaximalPrimeRankBoundaryFinset r N)
          (RootQuotientSemanticCompositeCandidates r N)
          S :=
      ⟨S₀, hS₀Finite, hGeneric₀⟩
    obtain ⟨S, hSFinite, hGeneric, hSCard⟩ :=
      exists_minimumRepairDivisorCover hFeasible
    obtain ⟨S', hS'Finite, hSemi, hPenCover, hS'Le⟩ :=
      exists_semiprimeCover_ncard_le_of_semanticComposite_repairCover
        (by omega) hSFinite hGeneric
    have hTauLe := rootQuotientPenultimateSemiprimeCoverNumber_le
      hS'Finite hSemi hPenCover
    rw [hSCard] at hS'Le
    exact hTauLe.trans hS'Le

/-- **Penultimate repair-hierarchy collapse theorem.**

At horizon `L_r(N)-1`, the coarse divisor-hitting relaxation, the exact global
optional-macro storage, and the semiprime set-cover number all coincide.  This
is the precise sense in which the general residual-word repair hypergraph
collapses to ordinary divisor set cover at the penultimate layer. -/
theorem penultimate_repairHierarchy_collapse
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientRepairDivisorCoverNumber
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeHorizon r N - 1) ∧
    rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeHorizon r N - 1) =
      rootQuotientPenultimateSemiprimeCoverNumber r N := by
  have hCoverEq :=
    penultimateRepairDivisorCoverNumber_eq_semiprimeCoverNumber
      (r := r) (N := N) hHorizon
  have hMuEq :=
    rootQuotientMinimumCompositeMacroCount_penultimate_eq_tau
      (r := r) (N := N) hr hHorizon
  exact ⟨hCoverEq.trans hMuEq.symm, hMuEq⟩

end EnterpriseMath.Quotient
