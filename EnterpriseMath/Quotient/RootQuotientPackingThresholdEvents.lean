import EnterpriseMath.Quotient.RootQuotientFourLayerResourceEvents
import EnterpriseMath.Quotient.RootQuotientThreeLayerPhaseDiagram
import EnterpriseMath.Quotient.RootQuotientThreeMacroStableOptimality
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A semantic composite candidate dividing a pure `p`-power cannot also divide
a target with only one `p`-token. -/
theorem no_candidate_covers_primePow_and_target_of_factorization_eq_one
    {r N g p m t : ℕ}
    (hp : p.Prime)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgPow : g ∣ p ^ m)
    (hgTarget : g ∣ t)
    (htZero : t ≠ 0)
    (hFact : t.factorization p = 1) :
    False := by
  have hServe : RootQuotientMacroServesPrimeDirection g p :=
    macroServesPrimeDirection_of_dvd_primePow hp hgC.1.1 hgPow
  obtain ⟨e, hePos, hgeq⟩ := hServe
  have heTwo : 2 ≤ e := by
    by_contra hNot
    have heOne : e = 1 := by omega
    have hgPrime : g ∈ RootQuotientPrimeBasis N := by
      rw [hgeq, heOne, pow_one]
      exact ⟨hp, hgC.1.2.1⟩
    exact hgC.2 hgPrime
  rw [hgeq] at hgTarget
  have heLe : e ≤ t.factorization p :=
    (hp.pow_dvd_iff_le_factorization htZero).1 hgTarget
  rw [hFact] at heLe
  omega

/-- No semantic composite candidate can divide positive powers of two distinct
primes. -/
theorem no_candidate_covers_two_distinct_primePowers
    {r N g p q a b : ℕ}
    (hp : p.Prime)
    (hq : q.Prime)
    (hpq : p ≠ q)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgP : g ∣ p ^ a)
    (hgQ : g ∣ q ^ b) :
    False := by
  have hServeP : RootQuotientMacroServesPrimeDirection g p :=
    macroServesPrimeDirection_of_dvd_primePow hp hgC.1.1 hgP
  have hServeQ : RootQuotientMacroServesPrimeDirection g q :=
    macroServesPrimeDirection_of_dvd_primePow hq hgC.1.1 hgQ
  exact hpq (primeDirection_eq_of_macro_serves_both hp hq hServeP hServeQ)

/-- Two targets form a divisor-incompatibility packing when no candidate can
hit both. -/
theorem pair_is_repairPacking_of_no_common_candidate
    {C : Set ℕ} {a b : ℕ}
    (hNo : ∀ g : ℕ, g ∈ C → g ∣ a → g ∣ b → False) :
    RootQuotientRepairDivisorPacking C ({a, b} : Finset ℕ) := by
  intro g hgC t ht u hu hgT hgU
  simp at ht hu
  rcases ht with rfl | rfl <;>
    rcases hu with rfl | rfl
  · rfl
  · exact (hNo g hgC hgT hgU).elim
  · exact (hNo g hgC hgU hgT).elim
  · rfl

/-- Three targets form a repair packing when every pair is divisor-incompatible. -/
theorem triple_is_repairPacking_of_pairwise_no_common_candidate
    {C : Set ℕ} {a b c : ℕ}
    (hab : ∀ g : ℕ, g ∈ C → g ∣ a → g ∣ b → False)
    (hac : ∀ g : ℕ, g ∈ C → g ∣ a → g ∣ c → False)
    (hbc : ∀ g : ℕ, g ∈ C → g ∣ b → g ∣ c → False) :
    RootQuotientRepairDivisorPacking C ({a, b, c} : Finset ℕ) := by
  intro g hgC t ht u hu hgT hgU
  simp at ht hu
  rcases ht with rfl | rfl | rfl <;>
    rcases hu with rfl | rfl | rfl
  · rfl
  · exact (hab g hgC hgT hgU).elim
  · exact (hac g hgC hgT hgU).elim
  · exact (hab g hgC hgU hgT).elim
  · rfl
  · exact (hbc g hgC hgT hgU).elim
  · exact (hac g hgC hgU hgT).elim
  · exact (hbc g hgC hgU hgT).elim
  · rfl

/-- The first mixed target has exactly one factor two. -/
theorem factorization_two_two_mul_three_pow
    (h : ℕ) :
    (2 * 3 ^ h).factorization 2 = 1 := by
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  have h3 : (3 : ℕ).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  simp [Nat.Prime.factorization, h3]

/-- The second cover adversary has exactly one factor two. -/
theorem factorization_two_six_mul_five_pow_sub_one
    {h : ℕ}
    (hh : 1 ≤ h) :
    (6 * 5 ^ (h - 1)).factorization 2 = 1 := by
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  have h6 : (6 : ℕ).factorization 2 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    simp [Nat.Prime.factorization]
  have h5 : (5 : ℕ).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  simp [h6, h5]

/-- The second cover adversary has exactly one factor three. -/
theorem factorization_three_six_mul_five_pow_sub_one
    {h : ℕ}
    (hh : 1 ≤ h) :
    (6 * 5 ^ (h - 1)).factorization 3 = 1 := by
  rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
  have h6 : (6 : ℕ).factorization 3 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    simp [Nat.Prime.factorization]
  have h5 : (5 : ℕ).factorization 3 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  simp [h6, h5]

/-- At the first mixed threshold the two canonical hard targets already form a
size-two repair packing. -/
theorem two_le_globalRepairPacking_at_firstMixedThreshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : 2 * 3 ^ h < 2 ^ r) :
    2 ≤ rootQuotientGlobalRepairDivisorPackingNumber r (2 * 3 ^ h) h := by
  let N := 2 * 3 ^ h
  let a := 2 ^ (h + 1)
  let b := 2 * 3 ^ h
  have hPow : a ≤ N := by
    dsimp [a, N]
    have h23 : 2 ^ h ≤ 3 ^ h := Nat.pow_le_pow_left (by omega) h
    rw [pow_succ]
    nlinarith
  have haHard : a ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hDir : 2 ∈ RootQuotientHardPrimeDirections N h :=
      ⟨Nat.prime_two, hPow⟩
    exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
      hr (by omega) (by simpa [N] using hBinary)
      (by
        dsimp [RootQuotientHardPrimeTargetFinset, a]
        exact Finset.mem_image.2 ⟨2,
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hDir, rfl⟩)
  have hbHard : b ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (by simpa [b] using hBinary)
    apply (mem_primeHardSemanticTargetFinset_iff).2
    exact ⟨⟨by omega, by simp [b, N], hbFree⟩,
      by rw [primeFactorCount_two_mul_three_pow]; omega⟩
  let U : Finset ℕ := {a, b}
  have hUT : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    intro t ht
    simp [U] at ht
    rcases ht with rfl | rfl
    · exact haHard
    · exact hbHard
  have hab : a ≠ b := by
    dsimp [a, b, N]
    have hStrict := two_pow_succ_lt_two_mul_three_pow (by omega : 1 ≤ h)
    omega
  have hPack : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U := by
    apply pair_is_repairPacking_of_no_common_candidate
    intro g hgC hgA hgB
    exact no_candidate_covers_primePow_and_target_of_factorization_eq_one
      Nat.prime_two hgC hgA hgB (by dsimp [b]; positivity)
      (by simpa [b] using factorization_two_two_mul_three_pow h)
  have hLe := repairDivisorPacking_card_le_number hUT hPack
  have hCard : U.card = 2 := by simp [U, hab]
  rw [hCard] at hLe
  exact hLe

/-- At the second cover threshold, pure-2, pure-3, and the mixed adversary form
a size-three divisor-incompatibility packing. -/
theorem three_le_globalRepairPacking_at_twoCoverThreshold
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : 6 * 5 ^ (h - 1) < 2 ^ r) :
    3 ≤ rootQuotientGlobalRepairDivisorPackingNumber
      r (6 * 5 ^ (h - 1)) h := by
  let N := 6 * 5 ^ (h - 1)
  let a := 2 ^ (h + 1)
  let b := 3 ^ (h + 1)
  let c := 6 * 5 ^ (h - 1)
  have hThreeLe : b ≤ N := by
    dsimp [b, N]
    obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hh
    have hPow : 3 ^ n ≤ 5 ^ n := Nat.pow_le_pow_left (by omega) n
    norm_num [pow_add] at hPow ⊢
    nlinarith
  have hTwoLe : a ≤ N := by
    dsimp [a]
    exact (Nat.pow_le_pow_left (by omega) (h + 1)).trans hThreeLe
  have haHard : a ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hDir : 2 ∈ RootQuotientHardPrimeDirections N h :=
      ⟨Nat.prime_two, hTwoLe⟩
    exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
      hr (by omega) (by simpa [N] using hBinary)
      (by
        dsimp [RootQuotientHardPrimeTargetFinset, a]
        exact Finset.mem_image.2 ⟨2,
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hDir, rfl⟩)
  have hbHard : b ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hDir : 3 ∈ RootQuotientHardPrimeDirections N h :=
      ⟨Nat.prime_three, hThreeLe⟩
    exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
      hr (by omega) (by simpa [N] using hBinary)
      (by
        dsimp [RootQuotientHardPrimeTargetFinset, b]
        exact Finset.mem_image.2 ⟨3,
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hDir, rfl⟩)
  have hcHard : c ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hcPos : 1 ≤ c := by dsimp [c]; positivity
    have hcFree : RPowerFree r c :=
      rPowerFree_of_lt_two_pow_rootOrder hcPos (by simpa [c] using hBinary)
    apply (mem_primeHardSemanticTargetFinset_iff).2
    exact ⟨⟨by omega, by simp [c, N], hcFree⟩,
      by rw [primeFactorCount_six_mul_five_pow_sub_one (by omega)]; omega⟩
  let U : Finset ℕ := {a, b, c}
  have hUT : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    intro t ht
    simp [U] at ht
    rcases ht with rfl | rfl | rfl
    · exact haHard
    · exact hbHard
    · exact hcHard
  have hab : ∀ g : ℕ, g ∈ RootQuotientSemanticCompositeCandidates r N →
      g ∣ a → g ∣ b → False := by
    intro g hgC hgA hgB
    exact no_candidate_covers_two_distinct_primePowers
      Nat.prime_two Nat.prime_three (by omega) hgC hgA hgB
  have hac : ∀ g : ℕ, g ∈ RootQuotientSemanticCompositeCandidates r N →
      g ∣ a → g ∣ c → False := by
    intro g hgC hgA hgCdiv
    exact no_candidate_covers_primePow_and_target_of_factorization_eq_one
      Nat.prime_two hgC hgA hgCdiv (by dsimp [c]; positivity)
      (by simpa [c] using factorization_two_six_mul_five_pow_sub_one (by omega))
  have hbc : ∀ g : ℕ, g ∈ RootQuotientSemanticCompositeCandidates r N →
      g ∣ b → g ∣ c → False := by
    intro g hgC hgB hgCdiv
    exact no_candidate_covers_primePow_and_target_of_factorization_eq_one
      Nat.prime_three hgC hgB hgCdiv (by dsimp [c]; positivity)
      (by simpa [c] using factorization_three_six_mul_five_pow_sub_one (by omega))
  have hPack : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U :=
    triple_is_repairPacking_of_pairwise_no_common_candidate hab hac hbc
  have hLe := repairDivisorPacking_card_le_number hUT hPack
  have habNe : a ≠ b := by
    dsimp [a, b]
    exact ne_of_lt (pow_lt_pow_left' (by omega : h + 1 ≠ 0) (by omega : (2 : ℕ) < 3))
  have hacNe : a ≠ c := by
    intro hEq
    have hFact := factorization_two_six_mul_five_pow_sub_one (by omega : 1 ≤ h)
    have hAPow : a.factorization 2 = h + 1 := by
      dsimp [a]
      simpa using Nat.factorization_pow_self (n := h + 1) Nat.prime_two
    rw [← hEq, hAPow] at hFact
    omega
  have hbcNe : b ≠ c := by
    intro hEq
    have hFact := factorization_three_six_mul_five_pow_sub_one (by omega : 1 ≤ h)
    have hBPow : b.factorization 3 = h + 1 := by
      dsimp [b]
      simpa using Nat.factorization_pow_self (n := h + 1) Nat.prime_three
    rw [← hEq, hBPow] at hFact
    omega
  have hCard : U.card = 3 := by
    simp [U, habNe, hacNe, hbcNe]
  rw [hCard] at hLe
  exact hLe

end EnterpriseMath.Quotient
