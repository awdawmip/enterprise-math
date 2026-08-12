import EnterpriseMath.Quotient.RootQuotientMixedTargetExtension
import EnterpriseMath.Quotient.RootQuotientPenultimateRepairCollapse
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Semantic targets that remain outside the horizon-`h` ball of the forced
prime backend.  These, and only these, create optional-macro repair pressure. -/
noncomputable def RootQuotientPrimeHardSemanticTargetFinset
    (r N h : ℕ) : Finset ℕ :=
  (RootQuotientSemanticTargetFinset r N).filter
    (fun b => h < rootQuotientPrimeFactorCount b)

@[simp]
theorem mem_primeHardSemanticTargetFinset_iff
    {r N h b : ℕ} :
    b ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ↔
      b ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      h < rootQuotientPrimeFactorCount b := by
  simp [RootQuotientPrimeHardSemanticTargetFinset]

/-- Membership in the prime-hard semantic family is exactly failure of the
forced prime backend at the declared horizon. -/
theorem mem_primeHardSemanticTargetFinset_iff_not_prime_reachable
    {r N h b : ℕ} :
    b ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ↔
      b ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) b := by
  constructor
  · intro hb
    have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hb
    refine ⟨hbMem.1, ?_⟩
    intro hReach
    have hCountLe :=
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
        (by omega) hbMem.1.2.1).1 hReach
    omega
  · rintro ⟨hbSemantic, hNoReach⟩
    apply (mem_primeHardSemanticTargetFinset_iff).2
    refine ⟨hbSemantic, ?_⟩
    by_contra hNot
    have hCountLe : rootQuotientPrimeFactorCount b ≤ h := by omega
    have hReach :=
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
        (by omega) hbSemantic.2.1).2 hCountLe
    exact hNoReach hReach

/-- Repairing all semantic targets is equivalent to repairing only the targets
that are horizon-hard for the forced prime backend.  Prime-easy targets require
no optional macro at all. -/
theorem relativeRepairPresentation_fullSemantic_iff_primeHard
    {r N h : ℕ} {S : Set ℕ} :
    RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientSemanticTargetFinset r N)
      (RootQuotientSemanticCompositeCandidates r N)
      S ↔
    RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
      S := by
  constructor
  · rintro ⟨hFinite, hSC, hFull⟩
    refine ⟨hFinite, hSC, ?_⟩
    intro t ht
    have htSemantic : t ∈ RootQuotientSemanticTargetFinset r N := by
      have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
      exact (mem_rootQuotientSemanticTargetFinset_iff).2 htMem.1
    exact hFull t htSemantic
  · rintro ⟨hFinite, hSC, hHard⟩
    refine ⟨hFinite, hSC, ?_⟩
    intro t ht
    have htSemantic :=
      (mem_rootQuotientSemanticTargetFinset_iff).1 ht
    by_cases hCount : h < rootQuotientPrimeFactorCount t
    · exact hHard t
        (mem_primeHardSemanticTargetFinset_iff).2 ⟨htSemantic, hCount⟩
    · have hPrimeReach : RootQuotientProductReachableWithin h
          (RootQuotientPrimeBasis N) t :=
        (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
          (by omega) htSemantic.2.1).2 (by omega)
      exact rootQuotientProductReachableWithin_mono_generators
        Set.subset_union_left hPrimeReach

/-- Full semantic and prime-hard relative repair cardinality sets coincide. -/
theorem relativeRepairCardinalities_fullSemantic_eq_primeHard
    (r N h : ℕ) :
    RootQuotientRelativeRepairCardinalities
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientSemanticTargetFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) =
    RootQuotientRelativeRepairCardinalities
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) := by
  ext m
  constructor
  · rintro ⟨S, hS, hCard⟩
    exact ⟨S,
      (relativeRepairPresentation_fullSemantic_iff_primeHard).1 hS,
      hCard⟩
  · rintro ⟨S, hS, hCard⟩
    exact ⟨S,
      (relativeRepairPresentation_fullSemantic_iff_primeHard).2 hS,
      hCard⟩

/-- Exact minimum storage is unchanged after dropping all prime-easy semantic
targets. -/
theorem minimumRelativeRepairStorage_fullSemantic_eq_primeHard
    (r N h : ℕ) :
    rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientSemanticTargetFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) =
    rootQuotientMinimumRelativeRepairStorage
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) := by
  unfold rootQuotientMinimumRelativeRepairStorage
  rw [relativeRepairCardinalities_fullSemantic_eq_primeHard]

/-- **Global macro frontier = exact repair of the prime-hard semantic family.** -/
theorem minimumCompositeMacroCount_eq_primeHardRelativeRepairStorage
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) := by
  calc
    rootQuotientMinimumCompositeMacroCount r N h =
        rootQuotientMinimumRelativeRepairStorage
          (RootQuotientPrimeBasis N)
          h
          (RootQuotientSemanticTargetFinset r N)
          (RootQuotientSemanticCompositeCandidates r N) :=
      minimumCompositeMacroCount_eq_minimumRelativeRepairStorage hr hh
    _ = rootQuotientMinimumRelativeRepairStorage
          (RootQuotientPrimeBasis N)
          h
          (RootQuotientPrimeHardSemanticTargetFinset r N h)
          (RootQuotientSemanticCompositeCandidates r N) :=
      minimumRelativeRepairStorage_fullSemantic_eq_primeHard r N h

/-- First-order global divisor relaxation: cover every prime-hard semantic target
by at least one admissible composite divisor. -/
noncomputable def rootQuotientGlobalRepairDivisorCoverNumber
    (r N h : ℕ) : ℕ :=
  rootQuotientRepairDivisorCoverNumber
    (RootQuotientPrimeHardSemanticTargetFinset r N h)
    (RootQuotientSemanticCompositeCandidates r N)

/-- The global divisor relaxation is a lower bound on the true optional-macro
frontier. -/
theorem globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  apply repairDivisorCoverNumber_le_minimumCompositeMacroCount hr hh
  · intro t ht
    exact (mem_primeHardSemanticTargetFinset_iff).1 ht |>.1
  · intro t ht
    exact
      (mem_primeHardSemanticTargetFinset_iff_not_prime_reachable).1 ht |>.2

/-- Global repair-relaxation gap after all prime-easy targets have been removed. -/
noncomputable def rootQuotientGlobalRepairRelaxationGap
    (r N h : ℕ) : ℕ :=
  rootQuotientMinimumCompositeMacroCount r N h -
    rootQuotientGlobalRepairDivisorCoverNumber r N h

/-- The true macro frontier decomposes into global divisor-cover pressure plus
the residual bounded-depth repair gap. -/
theorem minimumCompositeMacroCount_eq_globalDivisorCover_add_gap
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientGlobalRepairDivisorCoverNumber r N h +
        rootQuotientGlobalRepairRelaxationGap r N h := by
  have hLe := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount hr hh
  dsimp [rootQuotientGlobalRepairRelaxationGap]
  omega

/-- At the penultimate prime horizon, prime-hard semantic targets are exactly the
maximal-prime-rank boundaries. -/
theorem primeHardSemanticTargetFinset_penultimate_eq_maximalRank
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientPrimeHardSemanticTargetFinset
        r N (rootQuotientPrimeHorizon r N - 1) =
      RootQuotientMaximalPrimeRankBoundaryFinset r N := by
  ext b
  constructor
  · intro hb
    have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hb
    have hBound :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
        b (by omega) hbMem.1.2.1 hbMem.1.2.2
    have hEq : rootQuotientPrimeFactorCount b =
        rootQuotientPrimeHorizon r N := by omega
    apply (mem_maximalPrimeRankBoundaryFinset_iff (by omega)).2
    exact ⟨by omega, hbMem.1.2.1, hbMem.1.2.2, hEq⟩
  · intro hb
    have hbMax :=
      (mem_maximalPrimeRankBoundaryFinset_iff (by omega)).1 hb
    apply (mem_primeHardSemanticTargetFinset_iff).2
    refine ⟨⟨by omega, hbMax.2.1, hbMax.2.2.1⟩, ?_⟩
    rw [hbMax.2.2.2]
    omega

/-- **Global repair relaxation collapses at the penultimate horizon.** -/
theorem globalRepairRelaxationGap_penultimate_eq_zero
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientGlobalRepairRelaxationGap
      r N (rootQuotientPrimeHorizon r N - 1) = 0 := by
  have hCollapse := penultimate_repairHierarchy_collapse
    (r := r) (N := N) hr hHorizon
  dsimp [rootQuotientGlobalRepairRelaxationGap,
    rootQuotientGlobalRepairDivisorCoverNumber]
  rw [primeHardSemanticTargetFinset_penultimate_eq_maximalRank hHorizon]
  omega

end EnterpriseMath.Quotient
