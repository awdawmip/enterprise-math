import EnterpriseMath.Quotient.RootQuotientPrimeEightNineTwentyFiveMetric
import EnterpriseMath.Quotient.RootQuotientTwoMacroOptimalPhase
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Stable next-prime-seven state threshold for optional macro budget three. -/
def rootQuotientThreeMacroStableThreshold (h : ℕ) : ℕ :=
  60 * 7 ^ (h - 3)

/-- From horizon ten onward, the stable q=7 threshold already contains the
three hard pure-prime directions `2,3,5`. -/
theorem five_pow_succ_le_threeMacroStableThreshold_of_ten_le
    {h : ℕ}
    (hTen : 10 ≤ h) :
    5 ^ (h + 1) ≤ rootQuotientThreeMacroStableThreshold h := by
  obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hTen
  have hPow : 5 ^ n ≤ 7 ^ n := Nat.pow_le_pow_left (by omega) n
  calc
    5 ^ (10 + n + 1) = 48828125 * 5 ^ n := by
      simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num
    _ ≤ 49412580 * 7 ^ n :=
      Nat.mul_le_mul (by norm_num) hPow
    _ = rootQuotientThreeMacroStableThreshold (10 + n) := by
      simp [rootQuotientThreeMacroStableThreshold, pow_add,
        Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num

/-- The stable threshold always lies below the next hard pure-prime direction
`7^(h+1)`. -/
theorem threeMacroStableThreshold_lt_seven_pow_succ
    {h : ℕ}
    (hh : 3 ≤ h) :
    rootQuotientThreeMacroStableThreshold h < 7 ^ (h + 1) := by
  rw [show h + 1 = (h - 3) + 4 by omega, pow_add]
  dsimp [rootQuotientThreeMacroStableThreshold]
  nlinarith [show 0 < 7 ^ (h - 3) by positivity]

/-- The older `4,9` adversarial shell is below the stable q=7 threshold once
horizon six is reached. -/
theorem fourNineThreshold_le_threeMacroStableThreshold_of_six_le
    {h : ℕ}
    (hSix : 6 ≤ h) :
    rootQuotientFourNineThreshold h ≤ rootQuotientThreeMacroStableThreshold h := by
  obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hSix
  have hPow : 4 ^ n ≤ 7 ^ n := Nat.pow_le_pow_left (by omega) n
  calc
    rootQuotientFourNineThreshold (6 + n) = 6144 * 4 ^ n := by
      simp [rootQuotientFourNineThreshold, pow_add,
        Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num
    _ ≤ 20580 * 7 ^ n := Nat.mul_le_mul (by norm_num) hPow
    _ = rootQuotientThreeMacroStableThreshold (6 + n) := by
      simp [rootQuotientThreeMacroStableThreshold, pow_add,
        Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num

/-- If hard directions `2,3,5` are all present and a separating composite
family has exactly three members, then all three slots are forced: the family
is one composite pure power in each of those directions. -/
theorem minimum_three_macro_family_is_two_three_five_pure_powers
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hFiveHard : 5 ^ (h + 1) ≤ N)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = 3) :
    ∃ g₂ g₃ g₅ a b c : ℕ,
      S = ({g₂, g₃, g₅} : Set ℕ) ∧
      2 ≤ a ∧ 2 ≤ b ∧ 2 ≤ c ∧
      g₂ = 2 ^ a ∧ g₃ = 3 ^ b ∧ g₅ = 5 ^ c := by
  have hTwoHard : 2 ∈ RootQuotientHardPrimeDirections N h := by
    refine ⟨Nat.prime_two, ?_⟩
    exact (Nat.pow_le_pow_left (by omega) (h + 1)).trans hFiveHard
  have hThreeHard : 3 ∈ RootQuotientHardPrimeDirections N h := by
    refine ⟨Nat.prime_three, ?_⟩
    exact (Nat.pow_le_pow_left (by omega) (h + 1)).trans hFiveHard
  have hFiveHardMem : 5 ∈ RootQuotientHardPrimeDirections N h :=
    ⟨by norm_num, hFiveHard⟩
  obtain ⟨g₂, hg₂S, hg₂Serve⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hTwoHard
  obtain ⟨g₃, hg₃S, hg₃Serve⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hThreeHard
  obtain ⟨g₅, hg₅S, hg₅Serve⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hFiveHardMem
  have hg₂₃ : g₂ ≠ g₃ := by
    intro hEq
    have := primeDirection_eq_of_macro_serves_both
      Nat.prime_two Nat.prime_three hg₂Serve (hEq ▸ hg₃Serve)
    omega
  have hg₂₅ : g₂ ≠ g₅ := by
    intro hEq
    have := primeDirection_eq_of_macro_serves_both
      Nat.prime_two (by norm_num : Nat.Prime 5) hg₂Serve (hEq ▸ hg₅Serve)
    omega
  have hg₃₅ : g₃ ≠ g₅ := by
    intro hEq
    have := primeDirection_eq_of_macro_serves_both
      Nat.prime_three (by norm_num : Nat.Prime 5) hg₃Serve (hEq ▸ hg₅Serve)
    omega
  have hTripleSub : ({g₂, g₃, g₅} : Set ℕ) ⊆ S := by
    intro g hg
    simp at hg
    rcases hg with rfl | rfl | rfl <;> assumption
  have hTripleCard : ({g₂, g₃, g₅} : Set ℕ).ncard = 3 := by
    simp [hg₂₃, hg₂₅, hg₃₅]
  have hCardLe : S.ncard ≤ ({g₂, g₃, g₅} : Set ℕ).ncard := by
    rw [hSCard, hTripleCard]
  have hTripleEq : ({g₂, g₃, g₅} : Set ℕ) = S :=
    Set.eq_of_subset_of_ncard_le hTripleSub hCardLe hS.1
  obtain ⟨a, haPos, hg₂Eq⟩ := hg₂Serve
  obtain ⟨b, hbPos, hg₃Eq⟩ := hg₃Serve
  obtain ⟨c, hcPos, hg₅Eq⟩ := hg₅Serve
  have hpLeN {p : ℕ} (hp : p.Prime) (hpHard : p ^ (h + 1) ≤ N) : p ≤ N := by
    have hpLePow : p ≤ p ^ (h + 1) := by
      calc
        p = p ^ 1 := by simp
        _ ≤ p ^ (h + 1) := Nat.pow_le_pow_right hp.one_le (by omega)
    exact hpLePow.trans hpHard
  have haTwo : 2 ≤ a := by
    by_contra hNot
    have haOne : a = 1 := by omega
    have hgPrimeBasis : g₂ ∈ RootQuotientPrimeBasis N := by
      rw [hg₂Eq, haOne]
      exact ⟨Nat.prime_two, hpLeN Nat.prime_two hTwoHard.2⟩
    exact (hS.2.1 hg₂S).2 hgPrimeBasis
  have hbTwo : 2 ≤ b := by
    by_contra hNot
    have hbOne : b = 1 := by omega
    have hgPrimeBasis : g₃ ∈ RootQuotientPrimeBasis N := by
      rw [hg₃Eq, hbOne]
      exact ⟨Nat.prime_three, hpLeN Nat.prime_three hThreeHard.2⟩
    exact (hS.2.1 hg₃S).2 hgPrimeBasis
  have hcTwo : 2 ≤ c := by
    by_contra hNot
    have hcOne : c = 1 := by omega
    have hgPrimeBasis : g₅ ∈ RootQuotientPrimeBasis N := by
      rw [hg₅Eq, hcOne]
      exact ⟨by norm_num, hpLeN (by norm_num) hFiveHardMem.2⟩
    exact (hS.2.1 hg₅S).2 hgPrimeBasis
  exact ⟨g₂, g₃, g₅, a, b, c, hTripleEq.symm,
    haTwo, hbTwo, hcTwo, hg₂Eq, hg₃Eq, hg₅Eq⟩

/-- The `4,9` adversarial target contains no factor five. -/
theorem factorization_five_fourNineThreshold
    {h : ℕ}
    (hh : 1 ≤ h) :
    (rootQuotientFourNineThreshold h).factorization 5 = 0 := by
  let n := h - 1
  have hSixFive : (6 : ℕ).factorization 5 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  have hFourFive : (4 : ℕ).factorization 5 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientFourNineThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [hSixFive, hFourFive]

/-- With `4` occupying the two-direction slot, the transient `4,9` shell is an
unavoidable target even if the third macro is an arbitrary composite pure
five-power. -/
theorem three_macro_family_with_four_fails_at_fourNineThreshold
    {r N h g₃ g₅ b c : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hN : rootQuotientFourNineThreshold h ≤ N)
    (hbTwo : 2 ≤ b)
    (hcTwo : 2 ≤ c)
    (hg₃Eq : g₃ = 3 ^ b)
    (hg₅Eq : g₅ = 5 ^ c)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ ({4, g₃, g₅} : Set ℕ))) :
    False := by
  let t := rootQuotientFourNineThreshold h
  have htPos : 1 ≤ t := by dsimp [t, rootQuotientFourNineThreshold]; positivity
  have htFree : RPowerFree r t :=
    rPowerFree_of_lt_two_pow_rootOrder htPos (hN.trans_lt hBinary)
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ ({4, g₃, g₅} : Set ℕ))
      (by omega) (by
        intro g hg
        rcases hg with hgPrime | hgMacro
        · exact hgPrime.1.one_le
        · simp at hgMacro
          rcases hgMacro with rfl | rfl | rfl
          · omega
          · rw [hg₃Eq]; positivity
          · rw [hg₅Eq]; positivity)).1 hSep
      t htPos hN htFree
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  have hFact3 : t.factorization 3 = 1 :=
    factorization_three_fourNineThreshold (by omega)
  have hFact5 : t.factorization 5 = 0 :=
    factorization_five_fourNineThreshold (by omega)
  have hw49 : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w := by
    intro g hgWord
    have hg := hwG g hgWord
    rcases hg with hgPrime | hgMacro
    · exact Or.inl hgPrime
    · simp at hgMacro
      rcases hgMacro with hFour | hG3 | hG5
      · subst g
        exact Or.inr (by simp)
      · subst g
        have hgDvd : g₃ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₃Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have hbLeFact : b ≤ t.factorization 3 :=
          (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
      · subst g
        have hgDvd : g₅ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₅Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have hcLeFact : c ≤ t.factorization 5 :=
          ((by norm_num : Nat.Prime 5).pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
  have hCostLe := rootQuotientPrimeFourNineCost_le_word_length
    htPos hw49 hProd
  have hCostEq : rootQuotientPrimeFourNineCost t = h + 1 := by
    dsimp [t, rootQuotientFourNineThreshold]
    simpa [show h + 1 - 2 = h - 1 by omega] using
      (rootQuotientPrimeFourNineCost_six_mul_four_pow (k := h + 1) (by omega))
  rw [hCostEq] at hCostLe
  omega

/-- Stable threshold valuations at the three hard directions. -/
theorem factorization_two_threeMacroStableThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    (rootQuotientThreeMacroStableThreshold h).factorization 2 = 2 := by
  let n := h - 3
  have h60 : (60 : ℕ).factorization 2 = 2 := by
    rw [show (60 : ℕ) = 4 * 15 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have h4 : (4 : ℕ).factorization 2 = 2 := by
      simpa [show (4 : ℕ) = 2 ^ 2 by norm_num] using
        (Nat.factorization_pow_self (n := 2) Nat.prime_two)
    have h15 : (15 : ℕ).factorization 2 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [h4, h15]
  have h7 : (7 : ℕ).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientThreeMacroStableThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [h60, h7]

theorem factorization_three_threeMacroStableThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    (rootQuotientThreeMacroStableThreshold h).factorization 3 = 1 := by
  let n := h - 3
  have h60 : (60 : ℕ).factorization 3 = 1 := by
    rw [show (60 : ℕ) = 3 * 20 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have h20 : (20 : ℕ).factorization 3 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [Nat.Prime.factorization, h20]
  have h7 : (7 : ℕ).factorization 3 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientThreeMacroStableThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [h60, h7]

theorem factorization_five_threeMacroStableThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    (rootQuotientThreeMacroStableThreshold h).factorization 5 = 1 := by
  let n := h - 3
  have h60 : (60 : ℕ).factorization 5 = 1 := by
    rw [show (60 : ℕ) = 5 * 12 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have h12 : (12 : ℕ).factorization 5 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [Nat.Prime.factorization, h12]
  have h7 : (7 : ℕ).factorization 5 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientThreeMacroStableThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [h60, h7]

/-- If all three hard directions are occupied by pure-power macros and the
2-direction exponent is at least three, the stable q=7 shell itself remains
unreachable within the claimed horizon. -/
theorem three_macro_pure_power_family_fails_at_stableThreshold_of_three_le_twoExponent
    {r N h g₂ g₃ g₅ a b c : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hN : rootQuotientThreeMacroStableThreshold h ≤ N)
    (haThree : 3 ≤ a)
    (hbTwo : 2 ≤ b)
    (hcTwo : 2 ≤ c)
    (hg₂Eq : g₂ = 2 ^ a)
    (hg₃Eq : g₃ = 3 ^ b)
    (hg₅Eq : g₅ = 5 ^ c)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ ({g₂, g₃, g₅} : Set ℕ))) :
    False := by
  let t := rootQuotientThreeMacroStableThreshold h
  have htPos : 1 ≤ t := by dsimp [t, rootQuotientThreeMacroStableThreshold]; positivity
  have htFree : RPowerFree r t :=
    rPowerFree_of_lt_two_pow_rootOrder htPos (hN.trans_lt hBinary)
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ ({g₂, g₃, g₅} : Set ℕ))
      (by omega) (by
        intro g hg
        rcases hg with hgPrime | hgMacro
        · exact hgPrime.1.one_le
        · simp at hgMacro
          rcases hgMacro with rfl | rfl | rfl
          · rw [hg₂Eq]; positivity
          · rw [hg₃Eq]; positivity
          · rw [hg₅Eq]; positivity)).1 hSep
      t htPos hN htFree
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  have hFact2 : t.factorization 2 = 2 :=
    factorization_two_threeMacroStableThreshold hh
  have hFact3 : t.factorization 3 = 1 :=
    factorization_three_threeMacroStableThreshold hh
  have hFact5 : t.factorization 5 = 1 :=
    factorization_five_threeMacroStableThreshold hh
  have hwStable : RootQuotientWordOver
      (RootQuotientPrimeEightNineTwentyFiveBasis N) w := by
    intro g hgWord
    have hg := hwG g hgWord
    rcases hg with hgPrime | hgMacro
    · exact Or.inl hgPrime
    · simp at hgMacro
      rcases hgMacro with hG2 | hG3 | hG5
      · subst g
        have hgDvd : g₂ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₂Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have haLeFact : a ≤ t.factorization 2 :=
          (Nat.prime_two.pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
      · subst g
        have hgDvd : g₃ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₃Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have hbLeFact : b ≤ t.factorization 3 :=
          (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
      · subst g
        have hgDvd : g₅ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₅Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have hcLeFact : c ≤ t.factorization 5 :=
          ((by norm_num : Nat.Prime 5).pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
  have hCostLe := rootQuotientPrimeEightNineTwentyFiveCost_le_word_length
    htPos hwStable hProd
  have hCostEq : rootQuotientPrimeEightNineTwentyFiveCost t = h + 1 := by
    dsimp [t, rootQuotientThreeMacroStableThreshold]
    simpa [show h + 1 - 4 = h - 3 by omega] using
      (rootQuotientPrimeEightNineTwentyFiveCost_sixty_mul_seven_pow
        (k := h + 1) (by omega))
  rw [hCostEq] at hCostLe
  omega

/-- Universal arbitrary-three-macro lower obstruction in the stable tail.

The threshold itself makes `2,3,5` hard from horizon ten onward.  Three macro
slots are therefore completely saturated by those pure-prime directions.  If
the 2-direction macro is `4`, the older `4,9` adversary defeats the code; if its
exponent is at least three, the q=7 stable shell defeats it. -/
theorem four_le_minimumCompositeMacroCount_of_threeMacroStableThreshold_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : N < 2 ^ r)
    (hThreshold : rootQuotientThreeMacroStableThreshold h ≤ N) :
    4 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  by_contra hNot
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ 3 := by omega
  by_cases hBelowSeven : N < 7 ^ (h + 1)
  · have hFiveHard : 5 ^ (h + 1) ≤ N :=
      (five_pow_succ_le_threeMacroStableThreshold_of_ten_le hTen).trans hThreshold
    obtain ⟨S, hS, hSCardMin⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr (by omega)
    have hMuGe : 3 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
      have hNotDirTwo : ¬rootQuotientPrimeDirectionDemand N h ≤ 2 := by
        intro hLe
        have hStateLt :=
          (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
            (N := N) (h := h) (s := 2)).1 hLe
        have : N < 5 ^ (h + 1) := by
          simpa [rootQuotientStablePrimeBase] using hStateLt
        omega
      have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
        hr (by omega) hBinary
      omega
    have hMu : rootQuotientMinimumCompositeMacroCount r N h = 3 := by omega
    have hSCard : S.ncard = 3 := by rw [hSCardMin, hMu]
    obtain ⟨g₂, g₃, g₅, a, b, c, hSEq,
        haTwo, hbTwo, hcTwo, hg₂Eq, hg₃Eq, hg₅Eq⟩ :=
      minimum_three_macro_family_is_two_three_five_pure_powers
        hr (by omega) hBinary hFiveHard hS hSCard
    have hSepTriple : SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeBasis N ∪ ({g₂, g₃, g₅} : Set ℕ)) := by
      rw [hSEq]
      exact hS.2.2
    by_cases haEq : a = 2
    · have hFourNine : rootQuotientFourNineThreshold h ≤ N :=
        (fourNineThreshold_le_threeMacroStableThreshold_of_six_le (by omega)).trans hThreshold
      exact three_macro_family_with_four_fails_at_fourNineThreshold
        hr (by omega) hBinary hFourNine hbTwo hcTwo hg₃Eq hg₅Eq
        (by simpa [hg₂Eq, haEq] using hSepTriple)
    · have haThree : 3 ≤ a := by omega
      exact three_macro_pure_power_family_fails_at_stableThreshold_of_three_le_twoExponent
        hr (by omega) hBinary hThreshold haThree hbTwo hcTwo
        hg₂Eq hg₃Eq hg₅Eq hSepTriple
  · have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
      hr (by omega) hBinary
    have hDirLeThree : rootQuotientPrimeDirectionDemand N h ≤ 3 :=
      hDirLeMu.trans hMuLe
    have hStateLt :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 3)).1 hDirLeThree
    have : N < 7 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase] using hStateLt
    omega

/-- Explicit stable q=7 upper construction for macro budget three. -/
theorem minimumCompositeMacroCount_le_three_of_stateBound_lt_threeMacroStableThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hBelow : N < rootQuotientThreeMacroStableThreshold h) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ 3 := by
  by_cases hPrimeOnly : N < 2 ^ (h + 1)
  · have hZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
      hr hN hBinary hPrimeOnly
    rw [hZero]
    omega
  · have hPow : 2 ^ (h + 1) ≤ N := by omega
    have h25N : 25 ≤ N := by
      have hEleven : 11 ≤ h + 1 := by omega
      have h2048 : 2 ^ 11 ≤ 2 ^ (h + 1) :=
        Nat.pow_le_pow_right (by omega) hEleven
      norm_num at h2048 ⊢
      omega
    have hSep : SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeEightNineTwentyFiveBasis N) :=
      (primeEightNineTwentyFiveBasis_separates_iff_stateBound_lt_shell
        hr (by omega) (by omega) hBinary).2
        (by simpa [rootQuotientThreeMacroStableThreshold] using hBelow)
    have hEightFree : RPowerFree r 8 :=
      rPowerFree_of_lt_two_pow_rootOrder (by omega)
        ((by omega : 8 ≤ N).trans_lt hBinary)
    have hNineFree : RPowerFree r 9 :=
      rPowerFree_of_lt_two_pow_rootOrder (by omega)
        ((by omega : 9 ≤ N).trans_lt hBinary)
    have hTwentyFiveFree : RPowerFree r 25 :=
      rPowerFree_of_lt_two_pow_rootOrder (by omega)
        (h25N.trans_lt hBinary)
    have hPresentation : RootQuotientCompositeMacroPresentation
        r N h ({8, 9, 25} : Set ℕ) := by
      refine ⟨by simp, ?_, ?_⟩
      · intro g hg
        simp at hg
        rcases hg with rfl | rfl | rfl
        · exact ⟨⟨by omega, by omega, hEightFree⟩, by norm_num⟩
        · exact ⟨⟨by omega, by omega, hNineFree⟩, by norm_num⟩
        · exact ⟨⟨by omega, h25N, hTwentyFiveFree⟩, by norm_num⟩
      · simpa [RootQuotientPrimeEightNineTwentyFiveBasis] using hSep
    have hLe := rootQuotientMinimumCompositeMacroCount_le hPresentation
    norm_num at hLe ⊢
    exact hLe

/-- **Global stable-tail optimality for optional macro budget three.**

For every high-root task at horizon `h>=10`, arbitrary three-macro dictionaries
suffice exactly below the q=7 ladder shell.  Thus the pure-power code
`{8,9,25}` is not merely best inside the pure-power class: it is globally
optimal among all normalized optional composite macro families throughout the
stable tail. -/
theorem minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ 3 ↔
      N < rootQuotientThreeMacroStableThreshold h := by
  constructor
  · intro hMuLe
    by_contra hNot
    have hFour := four_le_minimumCompositeMacroCount_of_threeMacroStableThreshold_le
      hr hTen hBinary (by omega)
    omega
  · intro hBelow
    exact minimumCompositeMacroCount_le_three_of_stateBound_lt_threeMacroStableThreshold
      hr hTen hN hBinary hBelow

end EnterpriseMath.Quotient
