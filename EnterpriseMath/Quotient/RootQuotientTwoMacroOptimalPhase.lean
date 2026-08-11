import EnterpriseMath.Quotient.RootQuotientPrimeEightNineMetric
import EnterpriseMath.Quotient.RootQuotientFirstMixedPhaseDiagram
import EnterpriseMath.Quotient.RootQuotientMixedDirectionWitness
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Transient pure-direction shell supplied by macros `4,9`. -/
def rootQuotientFourNineThreshold (h : ℕ) : ℕ :=
  6 * 4 ^ (h - 1)

/-- Stable next-prime-5 shell supplied by macros `8,9`. -/
def rootQuotientEightNineThreshold (h : ℕ) : ℕ :=
  12 * 5 ^ (h - 2)

/-- Global two-macro candidate threshold from horizon three onward.

The transient code `4,9` wins through horizon five; the stable code `8,9`
wins from horizon six onward. -/
def rootQuotientTwoMacroOptimalThreshold (h : ℕ) : ℕ :=
  if h ≤ 5 then rootQuotientFourNineThreshold h
  else rootQuotientEightNineThreshold h

/-- The `4,9` candidate dominates `8,9` for horizons three through five. -/
theorem eightNineThreshold_le_fourNineThreshold_of_three_le_of_le_five
    {h : ℕ}
    (hThree : 3 ≤ h)
    (hFive : h ≤ 5) :
    rootQuotientEightNineThreshold h ≤ rootQuotientFourNineThreshold h := by
  have hCases : h = 3 ∨ h = 4 ∨ h = 5 := by omega
  rcases hCases with rfl | rfl | rfl <;>
    norm_num [rootQuotientEightNineThreshold, rootQuotientFourNineThreshold]

/-- The stable `8,9` candidate dominates from horizon six onward. -/
theorem fourNineThreshold_le_eightNineThreshold_of_six_le
    {h : ℕ}
    (hSix : 6 ≤ h) :
    rootQuotientFourNineThreshold h ≤ rootQuotientEightNineThreshold h := by
  obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hSix
  have hPow : 4 ^ n ≤ 5 ^ n := Nat.pow_le_pow_left (by omega) n
  calc
    rootQuotientFourNineThreshold (6 + n) = 6144 * 4 ^ n := by
      simp [rootQuotientFourNineThreshold, pow_add,
        Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num
    _ ≤ 7500 * 5 ^ n := Nat.mul_le_mul (by norm_num) hPow
    _ = rootQuotientEightNineThreshold (6 + n) := by
      simp [rootQuotientEightNineThreshold, pow_add,
        Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      norm_num

/-- Both candidate thresholds lie above the second hard pure-prime shell
`3^(h+1)` from horizon three onward. -/
theorem three_pow_succ_le_twoMacroOptimalThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    3 ^ (h + 1) ≤ rootQuotientTwoMacroOptimalThreshold h := by
  by_cases hFive : h ≤ 5
  · have hCases : h = 3 ∨ h = 4 ∨ h = 5 := by omega
    rcases hCases with rfl | rfl | rfl <;>
      norm_num [rootQuotientTwoMacroOptimalThreshold,
        rootQuotientFourNineThreshold]
  · have hSix : 6 ≤ h := by omega
    obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hSix
    have hPow : 3 ^ n ≤ 5 ^ n := Nat.pow_le_pow_left (by omega) n
    simp [rootQuotientTwoMacroOptimalThreshold,
      rootQuotientEightNineThreshold, pow_add,
      Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    norm_num
    exact Nat.mul_le_mul (by norm_num : 2187 ≤ 7500) hPow

/-- The global candidate threshold still lies strictly below the third hard
prime shell `5^(h+1)`. -/
theorem twoMacroOptimalThreshold_lt_five_pow_succ
    {h : ℕ}
    (hh : 3 ≤ h) :
    rootQuotientTwoMacroOptimalThreshold h < 5 ^ (h + 1) := by
  by_cases hFive : h ≤ 5
  · have hCases : h = 3 ∨ h = 4 ∨ h = 5 := by omega
    rcases hCases with rfl | rfl | rfl <;>
      norm_num [rootQuotientTwoMacroOptimalThreshold,
        rootQuotientFourNineThreshold]
  · have hSix : 6 ≤ h := by omega
    simp [rootQuotientTwoMacroOptimalThreshold, hFive,
      rootQuotientEightNineThreshold]
    rw [show h + 1 = (h - 2) + 3 by omega, pow_add]
    nlinarith [show 0 < 5 ^ (h - 2) by positivity]

/-- The `4,9` hard witness never exceeds the chosen global two-macro threshold. -/
theorem fourNineThreshold_le_twoMacroOptimalThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    rootQuotientFourNineThreshold h ≤ rootQuotientTwoMacroOptimalThreshold h := by
  by_cases hFive : h ≤ 5
  · simp [rootQuotientTwoMacroOptimalThreshold, hFive]
  · have hSix : 6 ≤ h := by omega
    simp [rootQuotientTwoMacroOptimalThreshold, hFive]
    exact fourNineThreshold_le_eightNineThreshold_of_six_le hSix

/-- The `8,9` hard witness never exceeds the chosen global two-macro threshold. -/
theorem eightNineThreshold_le_twoMacroOptimalThreshold
    {h : ℕ}
    (hh : 3 ≤ h) :
    rootQuotientEightNineThreshold h ≤ rootQuotientTwoMacroOptimalThreshold h := by
  by_cases hFive : h ≤ 5
  · simp [rootQuotientTwoMacroOptimalThreshold, hFive]
    exact eightNineThreshold_le_fourNineThreshold_of_three_le_of_le_five hh hFive
  · simp [rootQuotientTwoMacroOptimalThreshold, hFive]

/-- Ground factorization data for the transient adversarial target. -/
theorem factorization_three_fourNineThreshold
    {h : ℕ}
    (hh : 1 ≤ h) :
    (rootQuotientFourNineThreshold h).factorization 3 = 1 := by
  let n := h - 1
  have hSixThree : (6 : ℕ).factorization 3 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    simp [Nat.Prime.factorization]
  have hFourThree : (4 : ℕ).factorization 3 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientFourNineThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [hSixThree, hFourThree]

/-- Ground factorization data for the stable adversarial target. -/
theorem factorization_two_eightNineThreshold
    {h : ℕ}
    (hh : 2 ≤ h) :
    (rootQuotientEightNineThreshold h).factorization 2 = 2 := by
  let n := h - 2
  have hTwelveTwo : (12 : ℕ).factorization 2 = 2 := by
    rw [show (12 : ℕ) = 4 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have hFourTwo : (4 : ℕ).factorization 2 = 2 := by
      simpa [show (4 : ℕ) = 2 ^ 2 by norm_num] using
        (Nat.factorization_pow_self (n := 2) Nat.prime_two)
    simp [hFourTwo, Nat.Prime.factorization]
  have hFiveTwo : (5 : ℕ).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientEightNineThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [hTwelveTwo, hFiveTwo]

/-- Ground factorization data for the stable adversarial target. -/
theorem factorization_three_eightNineThreshold
    {h : ℕ}
    (hh : 2 ≤ h) :
    (rootQuotientEightNineThreshold h).factorization 3 = 1 := by
  let n := h - 2
  have hTwelveThree : (12 : ℕ).factorization 3 = 1 := by
    rw [show (12 : ℕ) = 4 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have hFourThree : (4 : ℕ).factorization 3 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [hFourThree, Nat.Prime.factorization]
  have hFiveThree : (5 : ℕ).factorization 3 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  dsimp [rootQuotientEightNineThreshold, n]
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  simp [hTwelveThree, hFiveThree]

/-- Any two-macro presentation that reaches beyond the second pure-prime shell
but stays below the third must devote its two macro slots to pure powers of `2`
and `3` when it attains the information-theoretic directional floor. -/
theorem minimum_two_macro_family_is_two_three_pure_powers
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hSecond : 3 ^ (h + 1) ≤ N)
    (hThird : N < 5 ^ (h + 1))
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = 2) :
    ∃ g₂ g₃ a b : ℕ,
      S = ({g₂, g₃} : Set ℕ) ∧
      2 ≤ a ∧ 2 ≤ b ∧
      g₂ = 2 ^ a ∧ g₃ = 3 ^ b := by
  have hDirLe : rootQuotientPrimeDirectionDemand N h ≤ 2 :=
    (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
      (N := N) (h := h) (s := 2)).2 (by
        simpa [rootQuotientStablePrimeBase] using hThird)
  have hDirNotOne : ¬rootQuotientPrimeDirectionDemand N h ≤ 1 := by
    intro hLe
    have hState :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 1)).1 hLe
    have : N < 3 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase] using hState
    omega
  have hDir : rootQuotientPrimeDirectionDemand N h = 2 := by omega
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ 2 :=
    (rootQuotientMinimumCompositeMacroCount_le hS).trans_eq hSCard
  have hMuGe := primeDirectionDemand_le_minimumCompositeMacroCount
    hr (by omega) hBinary
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 2 := by
    rw [hDir] at hMuGe
    omega
  have hNoMixed : rootQuotientMixedDirectionMacroOverhead r N h = 0 := by
    simp [rootQuotientMixedDirectionMacroOverhead, hMu, hDir]
  have hTwoHard : 2 ∈ RootQuotientHardPrimeDirections N h := by
    refine ⟨Nat.prime_two, ?_⟩
    have hTwoPow : 2 ^ (h + 1) ≤ 3 ^ (h + 1) :=
      Nat.pow_le_pow_left (by omega) (h + 1)
    exact hTwoPow.trans hSecond
  have hThreeHard : 3 ∈ RootQuotientHardPrimeDirections N h :=
    ⟨Nat.prime_three, hSecond⟩
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
  have hN2 : 2 ≤ N := by
    have : 1 ≤ 3 ^ (h + 1) := by positivity
    omega
  have haTwo : 2 ≤ a := by
    by_contra hNot
    have haOne : a = 1 := by omega
    have hg₂PrimeBasis : g₂ ∈ RootQuotientPrimeBasis N := by
      rw [hg₂Eq, haOne]
      simp [Nat.prime_two, hN2]
    exact (hS.2.1 hg₂S).2 hg₂PrimeBasis
  have hbTwo : 2 ≤ b := by
    by_contra hNot
    have hbOne : b = 1 := by omega
    have hN3 : 3 ≤ N := by omega
    have hg₃PrimeBasis : g₃ ∈ RootQuotientPrimeBasis N := by
      rw [hg₃Eq, hbOne]
      simp [Nat.prime_three, hN3]
    exact (hS.2.1 hg₃S).2 hg₃PrimeBasis
  exact ⟨g₂, g₃, a, b, hPairEq.symm, haTwo, hbTwo, hg₂Eq, hg₃Eq⟩

/-- If the `2`-direction macro is exactly `4`, the transient `4,9` shell is an
unavoidable adversarial target regardless of which composite pure `3`-power is
used in the second slot. -/
theorem two_macro_family_with_four_fails_at_fourNineThreshold
    {r N h g₃ b : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : rootQuotientFourNineThreshold h ≤ N)
    (hbTwo : 2 ≤ b)
    (hg₃Eq : g₃ = 3 ^ b)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ ({4, g₃} : Set ℕ))) :
    False := by
  let t := rootQuotientFourNineThreshold h
  have htPos : 1 ≤ t := by dsimp [t, rootQuotientFourNineThreshold]; positivity
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ ({4, g₃} : Set ℕ))
      (by omega) (by
        intro g hg
        rcases hg with hgPrime | hgMacro
        · exact hgPrime.1.one_le
        · simp at hgMacro
          rcases hgMacro with rfl | rfl
          · omega
          · rw [hg₃Eq]
            positivity)).1 hSep
      t htPos hN (by
        intro q hq hDvd
        have hPowLe := Nat.le_of_dvd (by positivity : 0 < t) hDvd
        have hTwoPow : 2 ^ r ≤ q ^ r := Nat.pow_le_pow_left hq r
        have hTargetLt : t < 2 ^ r := by omega
        omega)
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  have hFact3 : t.factorization 3 = 1 := factorization_three_fourNineThreshold (by omega)
  have hw49 : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w := by
    intro g hgWord
    have hg := hwG g hgWord
    rcases hg with hgPrime | hgMacro
    · exact Or.inl hgPrime
    · simp at hgMacro
      rcases hgMacro with hFour | hG3
      · subst g
        exact Or.inr (by simp)
      · subst g
        have hgDvd : g₃ ∣ t := word_member_dvd_compiled_product hgWord hProd
        rw [hg₃Eq] at hgDvd
        have htZero : t ≠ 0 := by omega
        have hbLeFact : b ≤ t.factorization 3 :=
          (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvd
        omega
  have hCostLe := rootQuotientPrimeFourNineCost_le_word_length
    htPos hw49 hProd
  have hCostEq : rootQuotientPrimeFourNineCost t = h + 1 := by
    dsimp [t, rootQuotientFourNineThreshold]
    simpa [show h + 1 - 2 = h - 1 by omega] using
      (rootQuotientPrimeFourNineCost_six_mul_four_pow (k := h + 1) (by omega))
  rw [hCostEq] at hCostLe
  omega

/-- If the `2`-direction macro exponent is at least three, the stable `8,9`
shell is an unavoidable adversarial target regardless of the exact exponents. -/
theorem two_macro_pure_power_family_fails_at_eightNineThreshold_of_three_le_twoExponent
    {r N h g₂ g₃ a b : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : rootQuotientEightNineThreshold h ≤ N)
    (haThree : 3 ≤ a)
    (hbTwo : 2 ≤ b)
    (hg₂Eq : g₂ = 2 ^ a)
    (hg₃Eq : g₃ = 3 ^ b)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ))) :
    False := by
  let t := rootQuotientEightNineThreshold h
  have htPos : 1 ≤ t := by dsimp [t, rootQuotientEightNineThreshold]; positivity
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ))
      (by omega) (by
        intro g hg
        rcases hg with hgPrime | hgMacro
        · exact hgPrime.1.one_le
        · simp at hgMacro
          rcases hgMacro with rfl | rfl
          · rw [hg₂Eq]; positivity
          · rw [hg₃Eq]; positivity)).1 hSep
      t htPos hN (by
        intro q hq hDvd
        have hPowLe := Nat.le_of_dvd (by positivity : 0 < t) hDvd
        have hTwoPow : 2 ^ r ≤ q ^ r := Nat.pow_le_pow_left hq r
        have hTargetLt : t < 2 ^ r := by omega
        omega)
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  have hFact2 : t.factorization 2 = 2 :=
    factorization_two_eightNineThreshold (by omega)
  have hFact3 : t.factorization 3 = 1 :=
    factorization_three_eightNineThreshold (by omega)
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
  have hCostLe := rootQuotientPrimeEightNineCost_le_word_length
    htPos hw89 hProd
  have hCostEq : rootQuotientPrimeEightNineCost t = h + 1 := by
    dsimp [t, rootQuotientEightNineThreshold]
    simpa [show h + 1 - 3 = h - 2 by omega] using
      (rootQuotientPrimeEightNineCost_twelve_mul_five_pow
        (k := h + 1) (by omega))
  rw [hCostEq] at hCostLe
  omega

/-- Universal two-macro lower obstruction from horizon three onward. -/
theorem three_le_minimumCompositeMacroCount_of_twoMacroThreshold_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hThreshold : rootQuotientTwoMacroOptimalThreshold h ≤ N) :
    3 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  by_contra hNot
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ 2 := by omega
  have hFivePow : 5 ^ (h + 1) ≤ N ∨ N < 5 ^ (h + 1) := le_total _ _
  rcases hFivePow with hThirdHard | hBelowThird
  · have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
      hr (by omega) hBinary
    have hDirLeTwo : rootQuotientPrimeDirectionDemand N h ≤ 2 :=
      hDirLeMu.trans hMuLe
    have hStateLt :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 2)).1 hDirLeTwo
    have : N < 5 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase] using hStateLt
    omega
  · obtain ⟨S, hS, hSCardMin⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr (by omega)
    have hSecond : 3 ^ (h + 1) ≤ N :=
      (three_pow_succ_le_twoMacroOptimalThreshold hh).trans hThreshold
    have hMuGe : 2 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
      have hNotDirOne : ¬rootQuotientPrimeDirectionDemand N h ≤ 1 := by
        intro hLe
        have hStateLt :=
          (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
            (N := N) (h := h) (s := 1)).1 hLe
        have : N < 3 ^ (h + 1) := by
          simpa [rootQuotientStablePrimeBase] using hStateLt
        omega
      have hDirLeMu := primeDirectionDemand_le_minimumCompositeMacroCount
        hr (by omega) hBinary
      omega
    have hMu : rootQuotientMinimumCompositeMacroCount r N h = 2 := by omega
    have hSCard : S.ncard = 2 := by rw [hSCardMin, hMu]
    obtain ⟨g₂, g₃, a, b, hSEq, haTwo, hbTwo, hg₂Eq, hg₃Eq⟩ :=
      minimum_two_macro_family_is_two_three_pure_powers
        hr hh hBinary hSecond hBelowThird hS hSCard
    have hSepPair : SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeBasis N ∪ ({g₂, g₃} : Set ℕ)) := by
      rw [hSEq]
      exact hS.2.2
    by_cases haEq : a = 2
    · have hA : rootQuotientFourNineThreshold h ≤ N :=
        (fourNineThreshold_le_twoMacroOptimalThreshold hh).trans hThreshold
      exact two_macro_family_with_four_fails_at_fourNineThreshold
        hr hh hA hbTwo hg₃Eq (by simpa [hg₂Eq, haEq] using hSepPair)
    · have haThree : 3 ≤ a := by omega
      have hB : rootQuotientEightNineThreshold h ≤ N :=
        (eightNineThreshold_le_twoMacroOptimalThreshold hh).trans hThreshold
      exact two_macro_pure_power_family_fails_at_eightNineThreshold_of_three_le_twoExponent
        hr hh hB haThree hbTwo hg₂Eq hg₃Eq hSepPair

/-- Explicit two-macro upper construction below the global threshold. -/
theorem minimumCompositeMacroCount_le_two_of_stateBound_lt_twoMacroThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hBelow : N < rootQuotientTwoMacroOptimalThreshold h) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ 2 := by
  by_cases hPrimeOnly : N < 2 ^ (h + 1)
  · have hZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
      hr hN hBinary hPrimeOnly
    rw [hZero]
    omega
  · have hN16 : 16 ≤ N := by
      have hPow : 2 ^ 4 ≤ 2 ^ (h + 1) :=
        Nat.pow_le_pow_right (by omega) (by omega)
      norm_num at hPow ⊢
      omega
    by_cases hFive : h ≤ 5
    · have hThreshold : rootQuotientTwoMacroOptimalThreshold h =
          rootQuotientFourNineThreshold h := by
        simp [rootQuotientTwoMacroOptimalThreshold, hFive]
      have hSep49 : SeparatesRootQuotientWordsUpTo
          r N h (RootQuotientPrimeFourNineBasis N) :=
        (primeFourNineBasis_separates_iff_stateBound_lt_shell
          hr (by omega) (by omega) hBinary).2 (by simpa [hThreshold] using hBelow)
      have hFourFree : RPowerFree r 4 :=
        rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 4 ≤ N).trans_lt hBinary)
      have hNineFree : RPowerFree r 9 :=
        rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 9 ≤ N).trans_lt hBinary)
      have hPresentation : RootQuotientCompositeMacroPresentation r N h ({4, 9} : Set ℕ) := by
        refine ⟨by simp, ?_, ?_⟩
        · intro g hg
          simp at hg
          rcases hg with rfl | rfl
          · exact ⟨⟨by omega, by omega, hFourFree⟩, by norm_num⟩
          · exact ⟨⟨by omega, by omega, hNineFree⟩, by norm_num⟩
        · simpa [RootQuotientPrimeFourNineBasis] using hSep49
      have hLe := rootQuotientMinimumCompositeMacroCount_le hPresentation
      norm_num at hLe ⊢
      exact hLe
    · have hSix : 6 ≤ h := by omega
      have hThreshold : rootQuotientTwoMacroOptimalThreshold h =
          rootQuotientEightNineThreshold h := by
        simp [rootQuotientTwoMacroOptimalThreshold, hFive]
      have hSep89 : SeparatesRootQuotientWordsUpTo
          r N h (RootQuotientPrimeEightNineBasis N) :=
        (primeEightNineBasis_separates_iff_stateBound_lt_shell
          hr (by omega) (by omega) hBinary).2 (by simpa [hThreshold] using hBelow)
      have hEightFree : RPowerFree r 8 :=
        rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 8 ≤ N).trans_lt hBinary)
      have hNineFree : RPowerFree r 9 :=
        rPowerFree_of_lt_two_pow_rootOrder (by omega) ((by omega : 9 ≤ N).trans_lt hBinary)
      have hPresentation : RootQuotientCompositeMacroPresentation r N h ({8, 9} : Set ℕ) := by
        refine ⟨by simp, ?_, ?_⟩
        · intro g hg
          simp at hg
          rcases hg with rfl | rfl
          · exact ⟨⟨by omega, by omega, hEightFree⟩, by norm_num⟩
          · exact ⟨⟨by omega, by omega, hNineFree⟩, by norm_num⟩
        · simpa [RootQuotientPrimeEightNineBasis] using hSep89
      have hLe := rootQuotientMinimumCompositeMacroCount_le hPresentation
      norm_num at hLe ⊢
      exact hLe

/-- **Global two-macro code-design phase transition.**

From horizon three onward, the exact state capacity of optional macro budget two
is piecewise:

* horizons `3,4,5`: transient optimizer `{4,9}` with first failing state
  `6*4^(h-1)`;
* horizons `h>=6`: stable next-prime optimizer `{8,9}` with first failing state
  `12*5^(h-2)`.

Equivalently, two optional macros suffice exactly below the piecewise threshold. -/
theorem minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroThreshold
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ 2 ↔
      N < rootQuotientTwoMacroOptimalThreshold h := by
  constructor
  · intro hMuLe
    by_contra hNot
    have hThree := three_le_minimumCompositeMacroCount_of_twoMacroThreshold_le
      hr hh hBinary (by omega)
    omega
  · intro hBelow
    exact minimumCompositeMacroCount_le_two_of_stateBound_lt_twoMacroThreshold
      hr hh hN hBinary hBelow

end EnterpriseMath.Quotient
