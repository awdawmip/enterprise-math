import EnterpriseMath.Quotient.RootQuotientMixedOverheadDecomposition
import EnterpriseMath.Quotient.RootQuotientExactMixedDirectionPhase
import EnterpriseMath.Quotient.RootQuotientTwoMacroHorizonTwo
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

private theorem rPowerFree_five_of_pos_le_eighteen
    {b : ℕ} (hb : 1 ≤ b) (hbN : b ≤ 18) :
    RPowerFree 5 b := by
  apply rPowerFree_of_lt_two_pow_rootOrder hb
  norm_num
  omega

private theorem rPowerFree_five_of_pos_le_twentySeven
    {b : ℕ} (hb : 1 ≤ b) (hbN : b ≤ 27) :
    RPowerFree 5 b := by
  apply rPowerFree_of_lt_two_pow_rootOrder hb
  norm_num
  omega

private theorem primeHard_eight_mem_5_18_2 :
    8 ∈ RootQuotientPrimeHardSemanticTargetFinset 5 18 2 := by
  apply (mem_primeHardSemanticTargetFinset_iff).2
  have hCount : rootQuotientPrimeFactorCount 8 = 3 := by
    simpa using rootQuotientPrimeFactorCount_two_pow 3
  exact ⟨⟨by norm_num, by norm_num,
    rPowerFree_five_of_pos_le_eighteen (by norm_num) (by norm_num)⟩,
    by omega⟩

private theorem primeHard_eighteen_mem_5_18_2 :
    18 ∈ RootQuotientPrimeHardSemanticTargetFinset 5 18 2 := by
  apply (mem_primeHardSemanticTargetFinset_iff).2
  have hCount : rootQuotientPrimeFactorCount 18 = 3 := by
    have h2 : rootQuotientPrimeFactorCount 2 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_two]
      simp
    have h3 : rootQuotientPrimeFactorCount 3 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_three]
      simp
    calc
      rootQuotientPrimeFactorCount 18 =
          rootQuotientPrimeFactorCount (2 * (3 ^ 2)) := by norm_num
      _ = rootQuotientPrimeFactorCount 2 +
          rootQuotientPrimeFactorCount (3 ^ 2) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 1 + 2 * 1 := by
        rw [h2, rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le, h3]
      _ = 3 := by norm_num
  exact ⟨⟨by norm_num, by norm_num,
    rPowerFree_five_of_pos_le_eighteen (by norm_num) (by norm_num)⟩,
    by omega⟩

/-- At `(r,N,h)=(5,18,2)`, no singleton semantic-composite divisor family can
cover both hard targets `8` and `18`. -/
theorem two_le_globalRepairDivisorCoverNumber_5_18_2 :
    2 ≤ rootQuotientGlobalRepairDivisorCoverNumber 5 18 2 := by
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset 5 18 2)
        (RootQuotientSemanticCompositeCandidates 5 18)
        S :=
    ⟨RootQuotientSemanticCompositeCandidates 5 18,
      semanticCompositeCandidates_finite 5 18,
      semanticCompositeCandidates_cover_primeHardTargets (by omega)⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  by_contra hNot
  have hCardOne : S.ncard ≤ 1 := by
    rw [hSCard]
    omega
  obtain ⟨g8, hg8S, hg8Dvd⟩ := hCover.2 8 primeHard_eight_mem_5_18_2
  obtain ⟨g18, hg18S, hg18Dvd⟩ := hCover.2 18 primeHard_eighteen_mem_5_18_2
  have hEq : g8 = g18 :=
    (Set.ncard_le_one hSFinite).1 hCardOne g8 hg8S g18 hg18S
  have hgCommon : g8 ∣ Nat.gcd 8 18 := by
    apply Nat.dvd_gcd
    · exact hg8Dvd
    · simpa [hEq] using hg18Dvd
  have hgDvdTwo : g8 ∣ 2 := by norm_num at hgCommon ⊢; exact hgCommon
  have hgCandidate := hCover.1 hg8S
  have hgTwo : 2 ≤ g8 := hgCandidate.1.1
  have hgLeTwo : g8 ≤ 2 := Nat.le_of_dvd (by norm_num) hgDvdTwo
  have hgEqTwo : g8 = 2 := by omega
  have hTwoPrimeBasis : 2 ∈ RootQuotientPrimeBasis 18 :=
    ⟨Nat.prime_two, by norm_num⟩
  exact hgCandidate.2 (by simpa [hgEqTwo] using hTwoPrimeBasis)

/-- Exact global divisor-cover number at the first mixed-cover witness. -/
theorem globalRepairDivisorCoverNumber_5_18_2_eq_two :
    rootQuotientGlobalRepairDivisorCoverNumber 5 18 2 = 2 := by
  have hMu : rootQuotientMinimumCompositeMacroCount 5 18 2 = 2 :=
    minimumCompositeMacroCount_eq_two_of_two_three_wedge
      (r := 5) (N := 18) (h := 2)
      (by norm_num) (by norm_num) (by norm_num)
      (by norm_num) (by norm_num)
  have hUpper := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := 5) (N := 18) (h := 2) (by norm_num) (by norm_num)
  rw [hMu] at hUpper
  exact Nat.le_antisymm hUpper two_le_globalRepairDivisorCoverNumber_5_18_2

/-- Exact pure-direction demand at `N=18,h=2`. -/
theorem primeDirectionDemand_18_2_eq_one :
    rootQuotientPrimeDirectionDemand 18 2 = 1 := by
  have hPhase := directionDemand_eq_one_and_mixedOverhead_eq_one_of_two_three_wedge
    (r := 5) (N := 18) (h := 2)
    (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num)
  exact hPhase.1

/-- **Pure mixed-divisor mode.**

At `(r,N,h)=(5,18,2)`, all mixed storage overhead is already visible at the
divisor-cover level; no residual-depth gap remains. -/
theorem mixedOverhead_5_18_2_is_cover_only :
    rootQuotientMixedDivisorCoverOverhead 5 18 2 = 1 ∧
    rootQuotientResidualDepthStorageOverhead 5 18 2 = 0 := by
  have hCover := globalRepairDivisorCoverNumber_5_18_2_eq_two
  have hDir := primeDirectionDemand_18_2_eq_one
  have hMu : rootQuotientMinimumCompositeMacroCount 5 18 2 = 2 :=
    minimumCompositeMacroCount_eq_two_of_two_three_wedge
      (r := 5) (N := 18) (h := 2)
      (by norm_num) (by norm_num) (by norm_num)
      (by norm_num) (by norm_num)
  constructor
  · dsimp [rootQuotientMixedDivisorCoverOverhead]
    rw [hCover, hDir]
    norm_num
  · dsimp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap]
    rw [hMu, hCover]
    norm_num

/-- Finite arithmetic classification used by the `N=27,h=2` divisor cover. -/
theorem dvd_four_or_nine_of_primeHard_5_27_2
    {b : ℕ}
    (hb : b ∈ RootQuotientPrimeHardSemanticTargetFinset 5 27 2) :
    4 ∣ b ∨ 9 ∣ b := by
  have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hb
  have hbTwo : 2 ≤ b := hbMem.1.1
  have hbN : b ≤ 27 := hbMem.1.2.1
  have hCount : 2 < rootQuotientPrimeFactorCount b := hbMem.2
  interval_cases b <;>
    norm_num [rootQuotientPrimeFactorCount] at hCount ⊢

/-- The pair `{4,9}` is a divisor cover of every prime-hard semantic target at
`(r,N,h)=(5,27,2)`. -/
theorem four_nine_is_globalRepairDivisorCover_5_27_2 :
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset 5 27 2)
      (RootQuotientSemanticCompositeCandidates 5 27)
      ({4, 9} : Set ℕ) := by
  have h4Free : RPowerFree 5 4 :=
    rPowerFree_five_of_pos_le_twentySeven (by norm_num) (by norm_num)
  have h9Free : RPowerFree 5 9 :=
    rPowerFree_five_of_pos_le_twentySeven (by norm_num) (by norm_num)
  constructor
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl
    · exact ⟨⟨by norm_num, by norm_num, h4Free⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by norm_num, by norm_num, h9Free⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
  · intro b hb
    rcases dvd_four_or_nine_of_primeHard_5_27_2 hb with h4 | h9
    · exact ⟨4, by simp, h4⟩
    · exact ⟨9, by simp, h9⟩

/-- Exact pure-direction demand at `N=27,h=2`. -/
theorem primeDirectionDemand_27_2_eq_two :
    rootQuotientPrimeDirectionDemand 27 2 = 2 := by
  have hLeTwo : rootQuotientPrimeDirectionDemand 27 2 ≤ 2 :=
    (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
      (N := 27) (h := 2) (s := 2)).2 (by
        norm_num [rootQuotientStablePrimeBase])
  have hNotLeOne : ¬rootQuotientPrimeDirectionDemand 27 2 ≤ 1 := by
    intro hLe
    have hState :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := 27) (h := 2) (s := 1)).1 hLe
    norm_num [rootQuotientStablePrimeBase] at hState
  omega

/-- Exact global divisor-cover number at `N=27,h=2`. -/
theorem globalRepairDivisorCoverNumber_5_27_2_eq_two :
    rootQuotientGlobalRepairDivisorCoverNumber 5 27 2 = 2 := by
  have hUpper : rootQuotientGlobalRepairDivisorCoverNumber 5 27 2 ≤ 2 := by
    unfold rootQuotientGlobalRepairDivisorCoverNumber
    have hLe := rootQuotientRepairDivisorCoverNumber_le
      (S := ({4, 9} : Set ℕ)) (by simp)
      four_nine_is_globalRepairDivisorCover_5_27_2
    norm_num at hLe ⊢
    exact hLe
  have hLower := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    (r := 5) (N := 27) (h := 2)
    (by norm_num) (by norm_num) (by norm_num)
  rw [primeDirectionDemand_27_2_eq_two] at hLower
  exact Nat.le_antisymm hUpper hLower

/-- `{4,6,9}` is a valid horizon-two presentation through state 27. -/
theorem four_six_nine_is_compositeMacroPresentation_5_27_2 :
    RootQuotientCompositeMacroPresentation
      5 27 2 ({4, 6, 9} : Set ℕ) := by
  have h4Free : RPowerFree 5 4 :=
    rPowerFree_five_of_pos_le_twentySeven (by norm_num) (by norm_num)
  have h6Free : RPowerFree 5 6 :=
    rPowerFree_five_of_pos_le_twentySeven (by norm_num) (by norm_num)
  have h9Free : RPowerFree 5 9 :=
    rPowerFree_five_of_pos_le_twentySeven (by norm_num) (by norm_num)
  refine ⟨by simp, ?_, ?_⟩
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl | rfl
    · exact ⟨⟨by norm_num, by norm_num, h4Free⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by norm_num, by norm_num, h6Free⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by norm_num, by norm_num, h9Free⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
  · have hSep26 : SeparatesRootQuotientWordsUpTo
        5 26 2 (RootQuotientPrimeFourSixBasis 26) :=
      (primeFourSixBasis_separates_iff_stateBound_lt_three_pow_succ
        (r := 5) (N := 26) (h := 2)
        (by norm_num) (by norm_num) (by norm_num) (by norm_num)).2 (by norm_num)
    have hPos : PositiveRootQuotientGenerators
        (RootQuotientPrimeBasis 27 ∪ ({4, 6, 9} : Set ℕ)) := by
      intro g hg
      rcases hg with hgPrime | hgMacro
      · exact hgPrime.1.one_le
      · simp at hgMacro
        rcases hgMacro with rfl | rfl | rfl <;> omega
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := 5) (N := 27) (h := 2)
      (G := RootQuotientPrimeBasis 27 ∪ ({4, 6, 9} : Set ℕ))
      (by norm_num) hPos).2
    intro b hbPos hbN hbFree
    by_cases hb27 : b = 27
    · subst b
      refine ⟨[9, 3], by norm_num, ?_, ?_⟩
      · intro g hg
        simp at hg
        rcases hg with rfl | rfl
        · exact Or.inr (by simp)
        · exact Or.inl ⟨Nat.prime_three, by norm_num⟩
      · norm_num [rootQuotientWordProduct]
    · have hb26 : b ≤ 26 := by omega
      have hReach26 :=
        (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
          (r := 5) (N := 26) (h := 2)
          (G := RootQuotientPrimeFourSixBasis 26)
          (by norm_num) rootQuotientPrimeFourSixBasis_positive).1 hSep26
          b hbPos hb26 hbFree
      apply rootQuotientProductReachableWithin_mono_generators ?_ hReach26
      intro g hg
      change g ∈ RootQuotientPrimeBasis 26 ∪ ({4, 6} : Set ℕ) at hg
      rcases hg with hgPrime | hgMacro
      · exact Or.inl ⟨hgPrime.1, by omega⟩
      · exact Or.inr (by
          simp at hgMacro ⊢
          tauto)

/-- Exact true optional-macro storage at `N=27,h=2`. -/
theorem minimumCompositeMacroCount_5_27_2_eq_three :
    rootQuotientMinimumCompositeMacroCount 5 27 2 = 3 := by
  have hLower :=
    three_le_minimumCompositeMacroCount_of_twentySeven_le_at_horizon_two
      (r := 5) (N := 27) (by norm_num) (by norm_num) (by norm_num)
  have hUpper := rootQuotientMinimumCompositeMacroCount_le
    four_six_nine_is_compositeMacroPresentation_5_27_2
  have hCard : ({4, 6, 9} : Set ℕ).ncard = 3 := by norm_num
  rw [hCard] at hUpper
  omega

/-- **Pure residual-depth mode.**

At `(r,N,h)=(5,27,2)`, the divisor-cover relaxation needs no storage beyond the
pure-direction floor, but exact bounded-depth repair needs one extra type. -/
theorem mixedOverhead_5_27_2_is_depth_only :
    rootQuotientMixedDivisorCoverOverhead 5 27 2 = 0 ∧
    rootQuotientResidualDepthStorageOverhead 5 27 2 = 1 := by
  have hCover := globalRepairDivisorCoverNumber_5_27_2_eq_two
  have hDir := primeDirectionDemand_27_2_eq_two
  have hMu := minimumCompositeMacroCount_5_27_2_eq_three
  constructor
  · dsimp [rootQuotientMixedDivisorCoverOverhead]
    rw [hCover, hDir]
  · dsimp [rootQuotientResidualDepthStorageOverhead,
      rootQuotientGlobalRepairRelaxationGap]
    rw [hMu, hCover]
    norm_num

end EnterpriseMath.Quotient
