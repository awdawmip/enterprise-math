import EnterpriseMath.Quotient.RootQuotientRepairHierarchyStrict
import EnterpriseMath.Quotient.RootQuotientPenultimateRepairCollapse
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Storage gap between exact bounded-depth residual-word repair and the coarser
candidate-restricted divisor-hitting relaxation. -/
noncomputable def rootQuotientRepairRelaxationGap
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) : ℕ :=
  rootQuotientMinimumRelativeRepairStorage G h T C -
    rootQuotientRepairDivisorCoverNumber T C

/-- Under the natural base-hardness and feasibility hypotheses, exact repair
storage decomposes into divisor-cover storage plus the residual-depth gap. -/
theorem minimumRelativeRepairStorage_eq_divisorCover_add_relaxationGap
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t)
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    rootQuotientMinimumRelativeRepairStorage G h T C =
      rootQuotientRepairDivisorCoverNumber T C +
        rootQuotientRepairRelaxationGap G h T C := by
  have hLe := repairDivisorCoverNumber_le_minimumRelativeRepairStorage
    hNoBase hFeasible
  dsimp [rootQuotientRepairRelaxationGap]
  omega

/-- The repair relaxation is exact precisely when the gap vanishes. -/
theorem repairRelaxationGap_eq_zero_iff
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t)
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    rootQuotientRepairRelaxationGap G h T C = 0 ↔
      rootQuotientMinimumRelativeRepairStorage G h T C =
        rootQuotientRepairDivisorCoverNumber T C := by
  have hLe := repairDivisorCoverNumber_le_minimumRelativeRepairStorage
    hNoBase hFeasible
  dsimp [rootQuotientRepairRelaxationGap]
  omega

/-- Exact repair storage of the strict two-target example is two. -/
theorem minimumRelativeRepairStorage_strictExample_eq_two :
    rootQuotientMinimumRelativeRepairStorage
      (∅ : Set ℕ)
      1
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates = 2 := by
  have hWitness := twelve_twenty_is_exactRepair_strictExample
  have hUpper := rootQuotientMinimumRelativeRepairStorage_le hWitness
  have hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (∅ : Set ℕ)
        1
        RootQuotientStrictRepairTargets
        RootQuotientStrictRepairCandidates
        S :=
    ⟨({12, 20} : Set ℕ), hWitness⟩
  obtain ⟨S, hS, hSCard⟩ :=
    exists_minimumRelativeRepairPresentation hFeasible
  have hLowerS := two_le_ncard_of_exactRepair_strictExample hS
  rw [hSCard] at hLowerS
  have hWitnessCard : ({12, 20} : Set ℕ).ncard = 2 := by norm_num
  rw [hWitnessCard] at hUpper
  omega

/-- The divisor-cover relaxation in the strict example uses at most one type. -/
theorem repairDivisorCoverNumber_strictExample_le_one :
    rootQuotientRepairDivisorCoverNumber
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates ≤ 1 := by
  have hLe := rootQuotientRepairDivisorCoverNumber_le
    (S := ({4} : Set ℕ))
    (by simp)
    singleton_four_is_divisorCover_strictExample
  simpa using hLe

/-- **Strict positive repair-relaxation gap.**

The divisor-hitting relaxation can miss a genuine bounded-depth storage cost:
the minimal two-target example has gap at least one. -/
theorem one_le_repairRelaxationGap_strictExample :
    1 ≤ rootQuotientRepairRelaxationGap
      (∅ : Set ℕ)
      1
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates := by
  have hExact := minimumRelativeRepairStorage_strictExample_eq_two
  have hCover := repairDivisorCoverNumber_strictExample_le_one
  dsimp [rootQuotientRepairRelaxationGap]
  rw [hExact]
  omega

/-- Every maximal-rank boundary is prime-hard at the penultimate horizon. -/
theorem maximalPrimeRankBoundary_not_reachable_prime_penultimate
    {r N t : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (ht : t ∈ RootQuotientMaximalPrimeRankBoundaryFinset r N) :
    ¬RootQuotientProductReachableWithin
      (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientPrimeBasis N)
      t := by
  have htMax :=
    (mem_maximalPrimeRankBoundaryFinset_iff (by omega)).1 ht
  intro hReach
  have hCostLe :=
    (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
      htMax.1 htMax.2.1).1 hReach
  rw [htMax.2.2.2] at hCostLe
  omega

/-- A minimum penultimate semiprime cover gives an exact relative repair
presentation of the maximal-rank boundary family. -/
theorem exists_penultimate_maximal_relativeRepairPresentation
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S := by
  obtain ⟨S, hSFinite, hSemi, hCover, _hSCard⟩ :=
    exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
  have hSep :=
    (prime_union_semiprimeFamily_separates_penultimate_iff_divisorCover
      hr hHorizon hSemi).2 hCover
  have hSC : S ⊆ RootQuotientSemanticCompositeCandidates r N := by
    intro g hg
    have hgSemantic := hSemi.1 hg
    refine ⟨hgSemantic, ?_⟩
    intro hgPrime
    have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hgPrime.1]
      simp
    have hSemiCount := hSemi.2 g hg
    omega
  refine ⟨S, hSFinite, hSC, ?_⟩
  intro t ht
  have htMax :=
    (mem_maximalPrimeRankBoundaryFinset_iff (by omega)).1 ht
  have hPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := hSemi.1 hgS
      omega
  exact
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N)
      (h := rootQuotientPrimeHorizon r N - 1)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hPos).1 hSep
      t htMax.1 htMax.2.1 htMax.2.2.1

/-- **Penultimate repair-relaxation gap vanishes.**

For the maximal-rank target family, ordinary candidate-restricted divisor
cover is already exact bounded-depth repair at the penultimate horizon. -/
theorem penultimate_repairRelaxationGap_eq_zero
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientRepairRelaxationGap
      (RootQuotientPrimeBasis N)
      (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientMaximalPrimeRankBoundaryFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) = 0 := by
  have hNoBase : ∀ t ∈ RootQuotientMaximalPrimeRankBoundaryFinset r N,
      ¬RootQuotientProductReachableWithin
        (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientPrimeBasis N) t := by
    intro t ht
    exact maximalPrimeRankBoundary_not_reachable_prime_penultimate hHorizon ht
  have hFeasible := exists_penultimate_maximal_relativeRepairPresentation
    hr hHorizon
  have hCoverEq :=
    penultimateRepairDivisorCoverNumber_eq_semiprimeCoverNumber
      (r := r) (N := N) hHorizon
  have hExactLe : rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientMaximalPrimeRankBoundaryFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) ≤
      rootQuotientPenultimateSemiprimeCoverNumber r N := by
    obtain ⟨S, hSFinite, hSemi, hCover, hSCard⟩ :=
      exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
    have hSep :=
      (prime_union_semiprimeFamily_separates_penultimate_iff_divisorCover
        hr hHorizon hSemi).2 hCover
    have hSC : S ⊆ RootQuotientSemanticCompositeCandidates r N := by
      intro g hg
      have hgSemantic := hSemi.1 hg
      refine ⟨hgSemantic, ?_⟩
      intro hgPrime
      have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
        rw [rootQuotientPrimeFactorCount,
          Nat.primeFactorsList_prime hgPrime.1]
        simp
      have hSemiCount := hSemi.2 g hg
      omega
    have hRel : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S := by
      refine ⟨hSFinite, hSC, ?_⟩
      intro t ht
      have htMax :=
        (mem_maximalPrimeRankBoundaryFinset_iff (by omega)).1 ht
      have hPos : PositiveRootQuotientGenerators
          (RootQuotientPrimeBasis N ∪ S) := by
        intro g hg
        rcases hg with hgPrime | hgS
        · exact hgPrime.1.one_le
        · have hgSemantic := hSemi.1 hgS
          omega
      exact
        (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
          (r := r) (N := N)
          (h := rootQuotientPrimeHorizon r N - 1)
          (G := RootQuotientPrimeBasis N ∪ S)
          (by omega) hPos).1 hSep
          t htMax.1 htMax.2.1 htMax.2.2.1
    have hLe := rootQuotientMinimumRelativeRepairStorage_le hRel
    rw [hSCard] at hLe
    exact hLe
  have hCoverLeExact :=
    repairDivisorCoverNumber_le_minimumRelativeRepairStorage
      hNoBase hFeasible
  have hExactEqCover : rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientMaximalPrimeRankBoundaryFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientRepairDivisorCoverNumber
        (RootQuotientMaximalPrimeRankBoundaryFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) := by
    rw [hCoverEq]
    exact Nat.le_antisymm hExactLe (by simpa [hCoverEq] using hCoverLeExact)
  exact
    (repairRelaxationGap_eq_zero_iff hNoBase hFeasible).2 hExactEqCover

end EnterpriseMath.Quotient
