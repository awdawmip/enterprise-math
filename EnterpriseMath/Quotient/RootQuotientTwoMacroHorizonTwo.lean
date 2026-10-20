import EnterpriseMath.Quotient.RootQuotientTwoMacroOptimalPhase
import EnterpriseMath.Quotient.RootQuotientExactMixedDirectionPhase
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- At horizon two, any two-macro presentation that reaches state `27` must
use one composite pure `2`-power and one composite pure `3`-power. -/
theorem minimum_two_macro_family_at_horizon_two_is_two_three_pure_powers
    {r N : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (h27 : 27 ≤ N)
    (h125 : N < 125)
    (hS : RootQuotientCompositeMacroPresentation r N 2 S)
    (hSCard : S.ncard = 2) :
    ∃ g₂ g₃ a b : ℕ,
      S = ({g₂, g₃} : Set ℕ) ∧
      2 ≤ a ∧ 2 ≤ b ∧
      g₂ = 2 ^ a ∧ g₃ = 3 ^ b := by
  have hTwoHard : 2 ∈ RootQuotientHardPrimeDirections N 2 := by
    norm_num [RootQuotientHardPrimeDirections]
    omega
  have hThreeHard : 3 ∈ RootQuotientHardPrimeDirections N 2 := by
    norm_num [RootQuotientHardPrimeDirections]
    omega
  obtain ⟨g₂, hg₂S, hg₂Serve⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hTwoHard
  obtain ⟨g₃, hg₃S, hg₃Serve⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hThreeHard
  have hgNe : g₂ ≠ g₃ := by
    intro hEq
    have hDirEq := primeDirection_eq_of_macro_serves_both
      Nat.prime_two Nat.prime_three hg₂Serve (hEq ▸ hg₃Serve)
    omega
  have hPairSub : ({g₂, g₃} : Set ℕ) ⊆ S := by
    intro g hg
    simp at hg
    rcases hg with rfl | rfl <;> assumption
  have hPairCard : ({g₂, g₃} : Set ℕ).ncard = 2 := by
    simp [hgNe]
  have hCardLe : S.ncard ≤ ({g₂, g₃} : Set ℕ).ncard := by
    rw [hSCard, hPairCard]
  have hPairEq : ({g₂, g₃} : Set ℕ) = S :=
    Set.eq_of_subset_of_ncard_le hPairSub hCardLe hS.1
  obtain ⟨a, haPos, hg₂Eq⟩ := hg₂Serve
  obtain ⟨b, hbPos, hg₃Eq⟩ := hg₃Serve
  have haTwo : 2 ≤ a := by
    by_contra hNot
    have haOne : a = 1 := by omega
    have hg₂PrimeBasis : g₂ ∈ RootQuotientPrimeBasis N := by
      rw [hg₂Eq, haOne]
      simp [RootQuotientPrimeBasis, Nat.prime_two]
      omega
    exact (hS.2.1 hg₂S).2 hg₂PrimeBasis
  have hbTwo : 2 ≤ b := by
    by_contra hNot
    have hbOne : b = 1 := by omega
    have hg₃PrimeBasis : g₃ ∈ RootQuotientPrimeBasis N := by
      rw [hg₃Eq, hbOne]
      simp [RootQuotientPrimeBasis, Nat.prime_three]
      omega
    exact (hS.2.1 hg₃S).2 hg₃PrimeBasis
  exact ⟨g₂, g₃, a, b, hPairEq.symm, haTwo, hbTwo, hg₂Eq, hg₃Eq⟩

/-- No two optional macros can separate state `27` at horizon two. -/
theorem three_le_minimumCompositeMacroCount_of_twentySeven_le_at_horizon_two
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (h27 : 27 ≤ N) :
    3 ≤ rootQuotientMinimumCompositeMacroCount r N 2 := by
  by_contra hNot
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N 2 ≤ 2 := by omega
  by_cases h125Hard : 125 ≤ N
  · have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
      hr (by omega) hBinary
    have hDirLeTwo : rootQuotientPrimeDirectionDemand N 2 ≤ 2 :=
      hDirLeMu.trans hMuLe
    have hStateLt :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := 2) (s := 2)).1 hDirLeTwo
    have hBelow : N < 125 := by
      norm_num [rootQuotientStablePrimeBase] at hStateLt ⊢
      exact hStateLt
    omega
  · have h125 : N < 125 := by omega
    obtain ⟨S, hS, hSCardMin⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr (by omega)
    have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
      hr (by omega) hBinary
    have hDirNotOne : ¬rootQuotientPrimeDirectionDemand N 2 ≤ 1 := by
      intro hLe
      have hStateLt :=
        (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
          (N := N) (h := 2) (s := 1)).1 hLe
      have hBelow : N < 27 := by
        norm_num [rootQuotientStablePrimeBase] at hStateLt ⊢
        exact hStateLt
      omega
    have hMuGe : 2 ≤ rootQuotientMinimumCompositeMacroCount r N 2 := by omega
    have hMu : rootQuotientMinimumCompositeMacroCount r N 2 = 2 := by omega
    have hSCard : S.ncard = 2 := by rw [hSCardMin, hMu]
    obtain ⟨g₂, g₃, a, b, hSEq, haTwo, hbTwo, hg₂Eq, hg₃Eq⟩ :=
      minimum_two_macro_family_at_horizon_two_is_two_three_pure_powers
        hr hBinary h27 h125 hS hSCard
    have hSepPair : SeparatesRootQuotientWordsUpTo
        r N 2 (RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ)) := by
      simpa [hSEq] using hS.2.2
    by_cases haEq : a = 2
    · let t := 24
      have htN : t ≤ N := by dsimp [t]; omega
      have htPos : 1 ≤ t := by norm_num [t]
      have htFree : RPowerFree r t :=
        rPowerFree_of_lt_two_pow_rootOrder htPos (htN.trans_lt hBinary)
      have hReach :=
        (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
          (r := r) (N := N) (h := 2)
          (G := RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ))
          (by omega) (by
            intro g hg
            rcases hg with hgPrime | hgMacro
            · exact hgPrime.1.one_le
            · simp at hgMacro
              rcases hgMacro with rfl | rfl
              · rw [hg₂Eq]; positivity
              · rw [hg₃Eq]; positivity)).1 hSepPair
          t htPos htN htFree
      obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
      have hFact3 : t.factorization 3 = 1 := by
        simpa [t, rootQuotientFourNineThreshold] using
          (factorization_three_fourNineThreshold (h := 2) (by omega))
      have hw49 : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w := by
        intro g hgWord
        have hg := hwG g hgWord
        rcases hg with hgPrime | hgMacro
        · exact Or.inl hgPrime
        · simp at hgMacro
          rcases hgMacro with hG2 | hG3
          · subst g
            rw [hg₂Eq, haEq]
            exact Or.inr (by simp)
          · subst g
            have hgDvd : g₃ ∣ t := word_member_dvd_compiled_product hgWord hProd
            rw [hg₃Eq] at hgDvd
            have htZero : t ≠ 0 := by norm_num [t]
            have hbLeFact : b ≤ t.factorization 3 :=
              (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvd
            omega
      have hCostLe := rootQuotientPrimeFourNineCost_le_word_length
        htPos hw49 hProd
      have hCostEq : rootQuotientPrimeFourNineCost t = 3 := by
        simpa [t, rootQuotientFourNineThreshold] using
          (rootQuotientPrimeFourNineCost_six_mul_four_pow (k := 3) (by omega))
      rw [hCostEq] at hCostLe
      omega
    · have haThree : 3 ≤ a := by omega
      let t := 12
      have htN : t ≤ N := by dsimp [t]; omega
      have htPos : 1 ≤ t := by norm_num [t]
      have htFree : RPowerFree r t :=
        rPowerFree_of_lt_two_pow_rootOrder htPos (htN.trans_lt hBinary)
      have hReach :=
        (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
          (r := r) (N := N) (h := 2)
          (G := RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ))
          (by omega) (by
            intro g hg
            rcases hg with hgPrime | hgMacro
            · exact hgPrime.1.one_le
            · simp at hgMacro
              rcases hgMacro with rfl | rfl
              · rw [hg₂Eq]; positivity
              · rw [hg₃Eq]; positivity)).1 hSepPair
          t htPos htN htFree
      obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
      have hFact2 : t.factorization 2 = 2 := by
        simpa [t, rootQuotientEightNineThreshold] using
          (factorization_two_eightNineThreshold (h := 2) (by omega))
      have hFact3 : t.factorization 3 = 1 := by
        simpa [t, rootQuotientEightNineThreshold] using
          (factorization_three_eightNineThreshold (h := 2) (by omega))
      have hw89 : RootQuotientWordOver (RootQuotientPrimeEightNineBasis N) w := by
        intro g hgWord
        have hg := hwG g hgWord
        rcases hg with hgPrime | hgMacro
        · exact Or.inl hgPrime
        · simp at hgMacro
          rcases hgMacro with hG2 | hG3
          · subst g
            have hgDvd : g₂ ∣ t := word_member_dvd_compiled_product hgWord hProd
            rw [hg₂Eq] at hgDvd
            have htZero : t ≠ 0 := by norm_num [t]
            have haLeFact : a ≤ t.factorization 2 :=
              (Nat.prime_two.pow_dvd_iff_le_factorization htZero).1 hgDvd
            omega
          · subst g
            have hgDvd : g₃ ∣ t := word_member_dvd_compiled_product hgWord hProd
            rw [hg₃Eq] at hgDvd
            have htZero : t ≠ 0 := by norm_num [t]
            have hbLeFact : b ≤ t.factorization 3 :=
              (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvd
            omega
      have hCostLe := rootQuotientPrimeEightNineCost_le_word_length
        htPos hw89 hProd
      have hCostEq : rootQuotientPrimeEightNineCost t = 3 := by
        simpa [t, rootQuotientEightNineThreshold] using
          (rootQuotientPrimeEightNineCost_twelve_mul_five_pow
            (k := 3) (by omega))
      rw [hCostEq] at hCostLe
      omega

/-- Exact global state threshold for optional macro budget two at horizon two. -/
theorem minimumCompositeMacroCount_le_two_iff_stateBound_lt_twentySeven_at_horizon_two
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N 2 ≤ 2 ↔ N < 27 := by
  constructor
  · intro hMuLe
    by_contra hNot
    have hThree :=
      three_le_minimumCompositeMacroCount_of_twentySeven_le_at_horizon_two
        hr hBinary (by omega)
    omega
  · intro hBelow
    by_cases hEight : N < 8
    · have hZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
        (r := r) (N := N) (h := 2) hr hN hBinary (by simpa using hEight)
      rw [hZero]
      omega
    · by_cases hEighteen : N < 18
      · have hOne :=
          minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
            (r := r) (N := N) (h := 2)
            hr (by omega) hBinary (by norm_num; omega) (by norm_num; omega)
        rw [hOne]
        omega
      · have hTwo := minimumCompositeMacroCount_eq_two_of_two_three_wedge
          (r := r) (N := N) (h := 2)
          hr (by omega) hBinary (by norm_num; omega) (by norm_num; omega)
        rw [hTwo]

/-- Full optional-macro-budget-two state threshold for every horizon `h>=2`. -/
def rootQuotientTwoMacroFullThreshold (h : ℕ) : ℕ :=
  if h = 2 then 27 else rootQuotientTwoMacroOptimalThreshold h

/-- Complete global budget-two code-design law from horizon two onward. -/
theorem minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ 2 ↔
      N < rootQuotientTwoMacroFullThreshold h := by
  by_cases hTwo : h = 2
  · subst h
    simpa [rootQuotientTwoMacroFullThreshold] using
      (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twentySeven_at_horizon_two
        (r := r) (N := N) hr hN hBinary)
  · have hThree : 3 ≤ h := by omega
    simpa [rootQuotientTwoMacroFullThreshold, hTwo] using
      (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroThreshold
        (r := r) (N := N) (h := h) hr hThree hN hBinary)

end EnterpriseMath.Quotient
