import EnterpriseMath.Quotient.RootQuotientOrthogonalMixedOverheads
import EnterpriseMath.Quotient.RootQuotientPrimeFourNineMetric
import EnterpriseMath.Quotient.RootQuotientFirstMixedPhaseDiagram
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The first mixed hard target has exactly `h+1` prime tokens. -/
theorem primeFactorCount_two_mul_three_pow
    {h : ℕ} :
    rootQuotientPrimeFactorCount (2 * 3 ^ h) = h + 1 := by
  have h2 : rootQuotientPrimeFactorCount 2 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_two]
    simp
  have h3 : rootQuotientPrimeFactorCount 3 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_three]
    simp
  calc
    rootQuotientPrimeFactorCount (2 * 3 ^ h) =
        rootQuotientPrimeFactorCount 2 +
          rootQuotientPrimeFactorCount (3 ^ h) :=
      rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
    _ = 1 + h := by
      rw [h2, rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le, h3]
      omega
    _ = h + 1 := by omega

/-- A single semantic-composite divisor cannot simultaneously hit the hard
pure-2 target and the first mixed target `2*3^h`. -/
theorem no_single_candidate_covers_two_pow_and_two_mul_three_pow
    {r N h g : ℕ}
    (hh : 1 ≤ h)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgTwo : g ∣ 2 ^ (h + 1))
    (hgMixed : g ∣ 2 * 3 ^ h) :
    False := by
  have hServe : RootQuotientMacroServesPrimeDirection g 2 :=
    macroServesPrimeDirection_of_dvd_primePow
      Nat.prime_two hgC.1.1 hgTwo
  obtain ⟨e, hePos, hgeq⟩ := hServe
  have heTwo : 2 ≤ e := by
    by_contra hNot
    have heOne : e = 1 := by omega
    have hgPrime : g ∈ RootQuotientPrimeBasis N := by
      rw [hgeq, heOne]
      exact ⟨Nat.prime_two, by
        have hgN := hgC.1.2.1
        simpa [hgeq, heOne] using hgN⟩
    exact hgC.2 hgPrime
  have htZero : 2 * 3 ^ h ≠ 0 := by positivity
  rw [hgeq] at hgMixed
  have heLeFact : e ≤ (2 * 3 ^ h).factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization htZero).1 hgMixed
  have hFact : (2 * 3 ^ h).factorization 2 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have h3zero : (3 : ℕ).factorization 2 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [Nat.Prime.factorization, h3zero]
  rw [hFact] at heLeFact
  omega

/-- **Exact one-type divisor-cover state frontier.** -/
theorem globalRepairDivisorCoverNumber_le_one_iff_stateBound_lt_two_mul_three_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤ 1 ↔
      N < 2 * 3 ^ h := by
  constructor
  · intro hCoverLe
    by_contra hNot
    have hLower : 2 * 3 ^ h ≤ N := by omega
    have hTwoPowLe : 2 ^ (h + 1) ≤ N := by
      have hPow : 2 ^ h ≤ 3 ^ h := Nat.pow_le_pow_left (by omega) h
      rw [pow_succ]
      nlinarith
    have hTwoTarget : 2 ^ (h + 1) ∈
        RootQuotientPrimeHardSemanticTargetFinset r N h := by
      have hpHard : 2 ∈ RootQuotientHardPrimeDirections N h :=
        ⟨Nat.prime_two, hTwoPowLe⟩
      exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
        hr (by omega) hBinary
        (by
          dsimp [RootQuotientHardPrimeTargetFinset]
          exact Finset.mem_image.2 ⟨2,
            (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard, rfl⟩)
    have hMixedTarget : 2 * 3 ^ h ∈
        RootQuotientPrimeHardSemanticTargetFinset r N h := by
      have htPos : 1 ≤ 2 * 3 ^ h := by positivity
      have htFree : RPowerFree r (2 * 3 ^ h) :=
        rPowerFree_of_lt_two_pow_rootOrder htPos (hLower.trans_lt hBinary)
      apply (mem_primeHardSemanticTargetFinset_iff).2
      exact ⟨⟨by positivity, hLower, htFree⟩,
        by rw [primeFactorCount_two_mul_three_pow]; omega⟩
    have hFeasible : ∃ S : Set ℕ,
        S.Finite ∧
        RootQuotientRepairDivisorCover
          (RootQuotientPrimeHardSemanticTargetFinset r N h)
          (RootQuotientSemanticCompositeCandidates r N) S :=
      ⟨RootQuotientSemanticCompositeCandidates r N,
        semanticCompositeCandidates_finite r N,
        semanticCompositeCandidates_cover_primeHardTargets (by omega)⟩
    obtain ⟨S, hSFinite, hScover, hSCard⟩ :=
      exists_minimumRepairDivisorCover hFeasible
    have hSOne : S.ncard ≤ 1 := by
      rw [hSCard]
      exact hCoverLe
    obtain ⟨g₂, hg₂S, hg₂Dvd⟩ := hScover.2 _ hTwoTarget
    obtain ⟨gM, hgMS, hgMDvd⟩ := hScover.2 _ hMixedTarget
    have hEq : g₂ = gM :=
      (Set.ncard_le_one hSFinite).1 hSOne g₂ hg₂S gM hgMS
    have hgC := hScover.1 hg₂S
    exact no_single_candidate_covers_two_pow_and_two_mul_three_pow
      (r := r) (N := N) (h := h) (g := g₂)
      (by omega) hgC hg₂Dvd (by simpa [hEq] using hgMDvd)
  · intro hBound
    have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
      (r := r) (N := N) (h := h) hr (by omega)
    by_cases hPrime : N < 2 ^ (h + 1)
    · have hMuZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
        hr hN hBinary hPrime
      rw [hMuZero] at hCoverLeMu
      omega
    · have hMuOne := minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
        hr hh hBinary (by omega) hBound
      rw [hMuOne] at hCoverLeMu
      exact hCoverLeMu

/-- Prime-factor lower bound when neither `4` nor `9` divides the target.

With at most one literal factor `2` and at most one literal factor `3`, all
remaining prime factors are at least five. -/
theorem six_mul_five_pow_sub_two_le_of_not_four_dvd_not_nine_dvd
    {b : ℕ}
    (hbPos : 1 ≤ b)
    (hCountTwo : 2 ≤ rootQuotientPrimeFactorCount b)
    (hNot4 : ¬4 ∣ b)
    (hNot9 : ¬9 ∣ b) :
    6 * 5 ^ (rootQuotientPrimeFactorCount b - 2) ≤ b := by
  have hbZero : b ≠ 0 := by omega
  let l := b.primeFactorsList
  let u2 := l.count 2
  let u3 := l.count 3
  let rest := l.filter (fun p : ℕ => p != 2 && p != 3)
  let n := rest.length
  have hCount2 : u2 = b.factorization 2 := by
    dsimp [u2, l]
    exact Nat.primeFactorsList_count_eq
  have hCount3 : u3 = b.factorization 3 := by
    dsimp [u3, l]
    exact Nat.primeFactorsList_count_eq
  have hu2 : u2 < 2 := by
    by_contra hNot
    have hPow : 2 ^ 2 ∣ b :=
      (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).2 (by
        rw [← hCount2]
        omega)
    exact hNot4 (by norm_num at hPow ⊢; exact hPow)
  have hu3 : u3 < 2 := by
    by_contra hNot
    have hPow : 3 ^ 2 ∣ b :=
      (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).2 (by
        rw [← hCount3]
        omega)
    exact hNot9 (by norm_num at hPow ⊢; exact hPow)
  have hLenSplit := length_filter_ne_two_three_add_counts l
  have hLen : n + u2 + u3 = rootQuotientPrimeFactorCount b := by
    dsimp [n, rest, u2, u3, l, rootQuotientPrimeFactorCount]
    exact hLenSplit
  have hRest : 5 ^ n ≤ rest.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    have hpMem := (List.mem_filter.1 hp).1
    have hpPred := (List.mem_filter.1 hp).2
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
    simp at hpPred
    omega
  have hProdSplit := pow_count_two_mul_pow_count_three_mul_filter_prod l
  have hProd : 2 ^ u2 * 3 ^ u3 * rest.prod = b := by
    dsimp [u2, u3, rest, l] at hProdSplit ⊢
    rw [Nat.prod_primeFactorsList hbZero] at hProdSplit
    exact hProdSplit
  have hResidual : 6 * 5 ^ (n + u2 + u3 - 2) ≤
      2 ^ u2 * 3 ^ u3 * 5 ^ n := by
    rcases Nat.lt_two_iff.mp hu2 with rfl | rfl <;>
      rcases Nat.lt_two_iff.mp hu3 with rfl | rfl
    · have hn : 2 ≤ n := by omega
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
      simp [pow_add]
      nlinarith [show 0 < 5 ^ t by positivity]
    · have hn : 1 ≤ n := by omega
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
      simp [pow_add]
      nlinarith [show 0 < 5 ^ t by positivity]
    · have hn : 1 ≤ n := by omega
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
      simp [pow_add]
      nlinarith [show 0 < 5 ^ t by positivity]
    · simp
  rw [← hLen]
  exact hResidual.trans (by
    calc
      2 ^ u2 * 3 ^ u3 * 5 ^ n ≤ 2 ^ u2 * 3 ^ u3 * rest.prod :=
        Nat.mul_le_mul_left _ hRest
      _ = b := hProd)

/-- Before `6*5^(h-1)`, every prime-hard semantic target is divisible by `4`
or by `9`. -/
theorem four_dvd_or_nine_dvd_of_primeHard_lt_six_mul_five_pow
    {r N h b : ℕ}
    (hh : 3 ≤ h)
    (hb : b ∈ RootQuotientPrimeHardSemanticTargetFinset r N h)
    (hBound : b < 6 * 5 ^ (h - 1)) :
    4 ∣ b ∨ 9 ∣ b := by
  by_contra hNeither
  push_neg at hNeither
  have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hb
  have hShell := six_mul_five_pow_sub_two_le_of_not_four_dvd_not_nine_dvd
    (by omega) (by omega) hNeither.1 hNeither.2
  have hExp : h - 1 ≤ rootQuotientPrimeFactorCount b - 2 := by omega
  have hPow : 5 ^ (h - 1) ≤
      5 ^ (rootQuotientPrimeFactorCount b - 2) :=
    Nat.pow_le_pow_right (by omega) hExp
  have : 6 * 5 ^ (h - 1) ≤ b :=
    (Nat.mul_le_mul_left 6 hPow).trans hShell
  omega

/-- The pair `{4,9}` is a global divisor cover below its constrained shell. -/
theorem four_nine_is_global_divisor_cover_below_six_mul_five_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ^ (h + 1) ≤ N)
    (hBinary : N < 2 ^ r)
    (hBound : N < 6 * 5 ^ (h - 1)) :
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
      ({4, 9} : Set ℕ) := by
  have hFourN : 4 ≤ N := by
    have : 2 ^ 4 ≤ 2 ^ (h + 1) :=
      Nat.pow_le_pow_right (by omega) (by omega)
    norm_num at this ⊢
    omega
  have hNineN : 9 ≤ N := by
    have h16 : 16 ≤ N := by
      have : 2 ^ 4 ≤ 2 ^ (h + 1) :=
        Nat.pow_le_pow_right (by omega) (by omega)
      norm_num at this ⊢
      omega
    omega
  have hFourFree : RPowerFree r 4 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hFourN.trans_lt hBinary)
  have hNineFree : RPowerFree r 9 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hNineN.trans_lt hBinary)
  constructor
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl
    · exact ⟨⟨by omega, hFourN, hFourFree⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
    · exact ⟨⟨by omega, hNineN, hNineFree⟩,
        by norm_num [RootQuotientPrimeBasis]⟩
  · intro b hb
    rcases four_dvd_or_nine_dvd_of_primeHard_lt_six_mul_five_pow
        hh hb (hb |> (mem_primeHardSemanticTargetFinset_iff).1 |>.1.2.1 |>.trans_lt hBound)
      with h4 | h9
    · exact ⟨4, by simp, h4⟩
    · exact ⟨9, by simp, h9⟩

/-- The second divisor-cover adversarial target has exactly `h+1` prime
factors. -/
theorem primeFactorCount_six_mul_five_pow_sub_one
    {h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientPrimeFactorCount (6 * 5 ^ (h - 1)) = h + 1 := by
  have h6 : rootQuotientPrimeFactorCount 6 = 2 := by
    have h2 : rootQuotientPrimeFactorCount 2 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_two]
      simp
    have h3 : rootQuotientPrimeFactorCount 3 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_three]
      simp
    calc
      rootQuotientPrimeFactorCount 6 =
          rootQuotientPrimeFactorCount (2 * 3) := by norm_num
      _ = rootQuotientPrimeFactorCount 2 + rootQuotientPrimeFactorCount 3 :=
        rootQuotientPrimeFactorCount_mul (by omega) (by omega)
      _ = 2 := by rw [h2, h3]
  have h5 : rootQuotientPrimeFactorCount 5 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime (by norm_num : Nat.Prime 5)]
    simp
  calc
    rootQuotientPrimeFactorCount (6 * 5 ^ (h - 1)) =
        rootQuotientPrimeFactorCount 6 +
          rootQuotientPrimeFactorCount (5 ^ (h - 1)) :=
      rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
    _ = 2 + (h - 1) := by
      rw [h6, rootQuotientPrimeFactorCount_pow (by omega), h5]
    _ = h + 1 := by omega

/-- Once the mixed adversary `6*5^(h-1)` enters the domain, no two semantic
composite divisor types can cover all prime-hard targets. -/
theorem three_le_globalRepairDivisorCoverNumber_of_six_mul_five_pow_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 6 * 5 ^ (h - 1) ≤ N) :
    3 ≤ rootQuotientGlobalRepairDivisorCoverNumber r N h := by
  have hThreePow : 3 ^ (h + 1) ≤ 6 * 5 ^ (h - 1) := by
    obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hh
    have hPow : 3 ^ n ≤ 5 ^ n := Nat.pow_le_pow_left (by omega) n
    norm_num [pow_add] at hPow ⊢
    nlinarith
  have hThreeHardBound : 3 ^ (h + 1) ≤ N := hThreePow.trans hLower
  have hTwoHard : 2 ^ (h + 1) ≤ N :=
    (Nat.pow_le_pow_left (by omega) (h + 1)).trans hThreeHardBound
  have hMixedPos : 1 ≤ 6 * 5 ^ (h - 1) := by positivity
  have hMixedFree : RPowerFree r (6 * 5 ^ (h - 1)) :=
    rPowerFree_of_lt_two_pow_rootOrder hMixedPos (hLower.trans_lt hBinary)
  have hMixedTarget : 6 * 5 ^ (h - 1) ∈
      RootQuotientPrimeHardSemanticTargetFinset r N h := by
    apply (mem_primeHardSemanticTargetFinset_iff).2
    exact ⟨⟨by positivity, hLower, hMixedFree⟩,
      by rw [primeFactorCount_six_mul_five_pow_sub_one (by omega)]; omega⟩
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧ RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
    ⟨RootQuotientSemanticCompositeCandidates r N,
      semanticCompositeCandidates_finite r N,
      semanticCompositeCandidates_cover_primeHardTargets (by omega)⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  by_contra hNot
  have hSLe : S.ncard ≤ 2 := by rw [hSCard]; omega
  have hT2 : 2 ^ (h + 1) ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hpHard : 2 ∈ RootQuotientHardPrimeDirections N h :=
      ⟨Nat.prime_two, hTwoHard⟩
    exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
      hr (by omega) hBinary
      (by
        dsimp [RootQuotientHardPrimeTargetFinset]
        exact Finset.mem_image.2 ⟨2,
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard, rfl⟩)
  have hT3 : 3 ^ (h + 1) ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    have hpHard : 3 ∈ RootQuotientHardPrimeDirections N h :=
      ⟨Nat.prime_three, hThreeHardBound⟩
    exact hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset
      hr (by omega) hBinary
      (by
        dsimp [RootQuotientHardPrimeTargetFinset]
        exact Finset.mem_image.2 ⟨3,
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard, rfl⟩)
  obtain ⟨g2, hg2S, hg2Dvd⟩ := hCover.2 _ hT2
  obtain ⟨g3, hg3S, hg3Dvd⟩ := hCover.2 _ hT3
  have hg2C := hCover.1 hg2S
  have hg3C := hCover.1 hg3S
  have hg2Serve := macroServesPrimeDirection_of_dvd_primePow
    Nat.prime_two hg2C.1.1 hg2Dvd
  have hg3Serve := macroServesPrimeDirection_of_dvd_primePow
    Nat.prime_three hg3C.1.1 hg3Dvd
  have hgNe : g2 ≠ g3 := by
    intro hEq
    have := primeDirection_eq_of_macro_serves_both
      Nat.prime_two Nat.prime_three hg2Serve (hEq ▸ hg3Serve)
    omega
  have hPairSub : ({g2, g3} : Set ℕ) ⊆ S := by
    intro g hg
    simp at hg
    rcases hg with rfl | rfl <;> assumption
  have hPairCard : ({g2, g3} : Set ℕ).ncard = 2 := by simp [hgNe]
  have hPairEq : ({g2, g3} : Set ℕ) = S := by
    apply Set.eq_of_subset_of_ncard_le hPairSub
    · rw [hPairCard]
      exact hSLe
    · exact hSFinite
  obtain ⟨g, hgS, hgDvdMixed⟩ := hCover.2 _ hMixedTarget
  have hgPair : g ∈ ({g2, g3} : Set ℕ) := by rw [hPairEq]; exact hgS
  simp at hgPair
  rcases hgPair with hEq2 | hEq3
  · subst g
    obtain ⟨e, hePos, hgeq⟩ := hg2Serve
    have heTwo : 2 ≤ e := by
      by_contra hNotE
      have heOne : e = 1 := by omega
      have hgPrime : g2 ∈ RootQuotientPrimeBasis N := by
        rw [hgeq, heOne]
        exact ⟨Nat.prime_two, by
          have := hg2C.1.2.1
          simpa [hgeq, heOne] using this⟩
      exact hg2C.2 hgPrime
    have htZero : 6 * 5 ^ (h - 1) ≠ 0 := by positivity
    rw [hgeq] at hgDvdMixed
    have heLe : e ≤ (6 * 5 ^ (h - 1)).factorization 2 :=
      (Nat.prime_two.pow_dvd_iff_le_factorization htZero).1 hgDvdMixed
    have hFact : (6 * 5 ^ (h - 1)).factorization 2 = 1 := by
      rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
      have h5zero : (5 : ℕ).factorization 2 = 0 :=
        Nat.factorization_eq_zero_of_not_dvd (by norm_num)
      have h6 : (6 : ℕ).factorization 2 = 1 := by
        rw [show (6 : ℕ) = 2 * 3 by norm_num,
          Nat.factorization_mul (by norm_num) (by norm_num)]
        simp [Nat.Prime.factorization]
      simp [h6, h5zero]
    rw [hFact] at heLe
    omega
  · subst g
    obtain ⟨e, hePos, hgeq⟩ := hg3Serve
    have heTwo : 2 ≤ e := by
      by_contra hNotE
      have heOne : e = 1 := by omega
      have hgPrime : g3 ∈ RootQuotientPrimeBasis N := by
        rw [hgeq, heOne]
        exact ⟨Nat.prime_three, by
          have := hg3C.1.2.1
          simpa [hgeq, heOne] using this⟩
      exact hg3C.2 hgPrime
    have htZero : 6 * 5 ^ (h - 1) ≠ 0 := by positivity
    rw [hgeq] at hgDvdMixed
    have heLe : e ≤ (6 * 5 ^ (h - 1)).factorization 3 :=
      (Nat.prime_three.pow_dvd_iff_le_factorization htZero).1 hgDvdMixed
    have hFact : (6 * 5 ^ (h - 1)).factorization 3 = 1 := by
      rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
      have h5zero : (5 : ℕ).factorization 3 = 0 :=
        Nat.factorization_eq_zero_of_not_dvd (by norm_num)
      have h6 : (6 : ℕ).factorization 3 = 1 := by
        rw [show (6 : ℕ) = 2 * 3 by norm_num,
          Nat.factorization_mul (by norm_num) (by norm_num)]
        simp [Nat.Prime.factorization]
      simp [h6, h5zero]
    rw [hFact] at heLe
    omega

/-- **Exact two-type divisor-cover state frontier.** -/
theorem globalRepairDivisorCoverNumber_le_two_iff_stateBound_lt_six_mul_five_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤ 2 ↔
      N < 6 * 5 ^ (h - 1) := by
  constructor
  · intro hLe
    by_contra hNot
    have hThree := three_le_globalRepairDivisorCoverNumber_of_six_mul_five_pow_le
      hr hh hBinary (by omega)
    omega
  · intro hBound
    by_cases hPrimeEasy : N < 2 ^ (h + 1)
    · have hMuZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
        hr hN hBinary hPrimeEasy
      have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
        (r := r) (N := N) (h := h) hr (by omega)
      rw [hMuZero] at hCoverLeMu
      omega
    · have hCover := four_nine_is_global_divisor_cover_below_six_mul_five_pow
        hr hh (by omega) hBinary hBound
      unfold rootQuotientGlobalRepairDivisorCoverNumber
      have hLe := rootQuotientRepairDivisorCoverNumber_le
        (S := ({4, 9} : Set ℕ)) (by simp) hCover
      norm_num at hLe ⊢
      exact hLe

end EnterpriseMath.Quotient
