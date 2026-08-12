import EnterpriseMath.Quotient.RootQuotientPrimeHardRepair
import EnterpriseMath.Quotient.RootQuotientHardDirectionRepair
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every hard pure-prime target is a member of the full prime-hard semantic
target family in the high-root regime. -/
theorem hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    RootQuotientHardPrimeTargetFinset N h ⊆
      RootQuotientPrimeHardSemanticTargetFinset r N h := by
  intro t ht
  obtain ⟨p, hpHard, htEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
  have htPos : 1 ≤ t := by rw [htEq]; positivity
  have htN : t ≤ N := by rw [htEq]; exact hpHard.2
  have htFree : RPowerFree r t :=
    rPowerFree_of_lt_two_pow_rootOrder htPos (htN.trans_lt hBinary)
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hpHard.1]
    simp
  have htCount : rootQuotientPrimeFactorCount t = h + 1 := by
    rw [htEq, rootQuotientPrimeFactorCount_pow hpHard.1.one_le, hpCount]
    simp
  apply (mem_primeHardSemanticTargetFinset_iff).2
  exact ⟨⟨by omega, htN, htFree⟩, by omega⟩

/-- The full semantic-composite candidate set is finite. -/
theorem semanticCompositeCandidates_finite
    (r N : ℕ) :
    (RootQuotientSemanticCompositeCandidates r N).Finite := by
  exact rootQuotientNontrivialPowerFreeBasis_finite.sdiff

/-- Every prime-hard semantic target is itself an admissible composite candidate
and hence the full candidate set gives a trivial finite divisor cover. -/
theorem semanticCompositeCandidates_cover_primeHardTargets
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
      (RootQuotientSemanticCompositeCandidates r N) := by
  constructor
  · exact Set.Subset.rfl
  · intro t ht
    have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
    have htSemantic := htMem.1
    have htComposite : t ∉ RootQuotientPrimeBasis N := by
      intro htPrime
      have hPrimeCount : rootQuotientPrimeFactorCount t = 1 := by
        rw [rootQuotientPrimeFactorCount,
          Nat.primeFactorsList_prime htPrime.1]
        simp
      omega
    exact ⟨t, ⟨htSemantic, htComposite⟩, dvd_rfl⟩

/-- The pure-direction demand is a lower bound on the global divisor-cover
relaxation. -/
theorem primeDirectionDemand_le_globalRepairDivisorCoverNumber
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r N h := by
  have hGlobalFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
    ⟨RootQuotientSemanticCompositeCandidates r N,
      semanticCompositeCandidates_finite r N,
      semanticCompositeCandidates_cover_primeHardTargets hh⟩
  obtain ⟨S, hSFinite, hGlobalCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hGlobalFeasible
  have hPureCover : RootQuotientRepairDivisorCover
      (RootQuotientHardPrimeTargetFinset N h)
      (RootQuotientSemanticCompositeCandidates r N)
      S := by
    constructor
    · exact hGlobalCover.1
    · intro t ht
      exact hGlobalCover.2 t
        (hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
          hr hh hBinary ht)
  have hPureLe := rootQuotientRepairDivisorCoverNumber_le
    hSFinite hPureCover
  rw [hSCard] at hPureLe
  have hPureEq := hardTargetRepairCoverNumber_eq_direction_ncard
    (r := r) (N := N) (h := h) hr hh hBinary
  have hDirEq := hardPrimeDirections_ncard_eq_primeDirectionDemand N h
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  rw [hPureEq, hDirEq] at hPureLe
  exact hPureLe

/-- Extra first-order divisor-cover storage caused by mixed semantic targets,
beyond the pure-prime-direction floor. -/
noncomputable def rootQuotientMixedDivisorCoverOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientGlobalRepairDivisorCoverNumber r N h -
    rootQuotientPrimeDirectionDemand N h

/-- Residual bounded-depth storage not visible to divisor hitting alone. -/
noncomputable def rootQuotientResidualDepthStorageOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientGlobalRepairRelaxationGap r N h

/-- Global divisor-cover storage decomposes into the pure-direction floor plus
mixed divisibility pressure. -/
theorem globalRepairDivisorCoverNumber_eq_directionDemand_add_mixedDivisorOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h =
      rootQuotientPrimeDirectionDemand N h +
        rootQuotientMixedDivisorCoverOverhead r N h := by
  have hLe := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    hr hh hBinary
  dsimp [rootQuotientMixedDivisorCoverOverhead]
  omega

/-- **Mixed-overhead two-stage decomposition.**

Mixed-direction storage pressure has two mathematically distinct sources:

1. extra divisor-hitting storage already forced by adding mixed semantic targets;
2. extra residual-depth storage because divisor hitting alone need not satisfy
   the bounded word metric.

Their sum is exactly the previously defined mixed-direction macro overhead. -/
theorem mixedDirectionMacroOverhead_eq_mixedDivisor_add_residualDepth
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMixedDirectionMacroOverhead r N h =
      rootQuotientMixedDivisorCoverOverhead r N h +
        rootQuotientResidualDepthStorageOverhead r N h := by
  have hMu := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  have hCover := globalRepairDivisorCoverNumber_eq_directionDemand_add_mixedDivisorOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  have hGlobal := minimumCompositeMacroCount_eq_globalDivisorCover_add_gap
    (r := r) (N := N) (h := h) hr hh
  dsimp [rootQuotientResidualDepthStorageOverhead] at hGlobal ⊢
  omega

/-- **Three-source optional-macro storage decomposition.**

True optional-macro storage splits into a pure-direction floor, mixed
first-order divisor-cover pressure, and residual bounded-depth pressure. -/
theorem minimumCompositeMacroCount_eq_direction_add_cover_add_depth
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientPrimeDirectionDemand N h +
        rootQuotientMixedDivisorCoverOverhead r N h +
          rootQuotientResidualDepthStorageOverhead r N h := by
  have hMu := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    (r := r) (N := N) (h := h) hr hh hBinary
  have hMix := mixedDirectionMacroOverhead_eq_mixedDivisor_add_residualDepth
    (r := r) (N := N) (h := h) hr hh hBinary
  omega

/-- **Four-source total primitive-storage decomposition.**

Total stored primitive types consist of the mandatory bounded-prime backend plus
three optional-macro resource components. -/
theorem minimumStorage_eq_prime_add_direction_add_cover_add_depth
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard +
        rootQuotientPrimeDirectionDemand N h +
          rootQuotientMixedDivisorCoverOverhead r N h +
            rootQuotientResidualDepthStorageOverhead r N h := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  rw [minimumCompositeMacroCount_eq_direction_add_cover_add_depth
    hr hh hBinary]
  omega

/-- If the global divisor relaxation is exact, all mixed overhead is already
visible at the divisor-cover level. -/
theorem mixedDirectionMacroOverhead_eq_mixedDivisorOverhead_of_globalGap_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hGap : rootQuotientGlobalRepairRelaxationGap r N h = 0) :
    rootQuotientMixedDirectionMacroOverhead r N h =
      rootQuotientMixedDivisorCoverOverhead r N h := by
  have hSplit := mixedDirectionMacroOverhead_eq_mixedDivisor_add_residualDepth
    (r := r) (N := N) (h := h) hr hh hBinary
  simp [rootQuotientResidualDepthStorageOverhead, hGap] at hSplit
  exact hSplit

end EnterpriseMath.Quotient
