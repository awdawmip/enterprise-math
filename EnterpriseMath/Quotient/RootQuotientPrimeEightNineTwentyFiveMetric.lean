import EnterpriseMath.Quotient.RootQuotientPrimeFourEightNineMetric
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Minimal next-prime-seven ladder: bounded primes plus `8=2^3`, `9=3^2`,
and `25=5^2`. -/
def RootQuotientPrimeEightNineTwentyFiveBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({8, 9, 25} : Set ℕ)

/-- Exact sparse-block cost. -/
def rootQuotientPrimeEightNineTwentyFiveCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b -
    2 * (b.factorization 2 / 3) -
    b.factorization 3 / 2 -
    b.factorization 5 / 2

/-- Positive-generator property. -/
theorem rootQuotientPrimeEightNineTwentyFiveBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeEightNineTwentyFiveBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · simp at hgMacro
    rcases hgMacro with rfl | rfl | rfl <;> omega

/-- Prime-token count of a word over the q=7 ladder. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeEightNineTwentyFive
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeEightNineTwentyFiveBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + 2 * w.count 8 + w.count 9 + w.count 25 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeEightNineTwentyFiveBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeEightNineTwentyFiveBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeEightNineTwentyFiveBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeEightNineTwentyFiveBasis_positive a haBasis
      rw [rootQuotientWordProduct,
        rootQuotientPrimeFactorCount_mul haPos hTailPos, ih hwTail]
      rcases haBasis with haPrime | haMacro
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have h8 : a ≠ 8 := by rintro rfl; norm_num at haPrime
        have h9 : a ≠ 9 := by rintro rfl; norm_num at haPrime
        have h25 : a ≠ 25 := by rintro rfl; norm_num at haPrime
        rw [haCount, List.count_cons, List.count_cons, List.count_cons]
        simp [h8, h9, h25]
        omega
      · simp at haMacro
        rcases haMacro with rfl | rfl | rfl
        · have hCount : rootQuotientPrimeFactorCount 8 = 3 := by
            simpa using rootQuotientPrimeFactorCount_two_pow 3
          rw [hCount, List.count_cons, List.count_cons, List.count_cons]
          simp
          omega
        · have hThree : rootQuotientPrimeFactorCount 3 = 1 := by
            rw [rootQuotientPrimeFactorCount,
              Nat.primeFactorsList_prime Nat.prime_three]
            simp
          have hCount : rootQuotientPrimeFactorCount 9 = 2 := by
            calc
              rootQuotientPrimeFactorCount 9 =
                  rootQuotientPrimeFactorCount (3 ^ 2) := by norm_num
              _ = 2 * rootQuotientPrimeFactorCount 3 :=
                rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le
              _ = 2 := by rw [hThree]
          rw [hCount, List.count_cons, List.count_cons, List.count_cons]
          simp
          omega
        · have hFive : rootQuotientPrimeFactorCount 5 = 1 := by
            rw [rootQuotientPrimeFactorCount,
              Nat.primeFactorsList_prime (by norm_num : Nat.Prime 5)]
            simp
          have hCount : rootQuotientPrimeFactorCount 25 = 2 := by
            calc
              rootQuotientPrimeFactorCount 25 =
                  rootQuotientPrimeFactorCount (5 ^ 2) := by norm_num
              _ = 2 * rootQuotientPrimeFactorCount 5 :=
                rootQuotientPrimeFactorCount_pow (by omega)
              _ = 2 := by rw [hFive]
          rw [hCount, List.count_cons, List.count_cons, List.count_cons]
          simp
          omega

/-- Macro copies contribute independent pure-power divisors. -/
theorem eight_nine_twentyFive_macro_powers_dvd_wordProduct
    (w : List ℕ) :
    8 ^ w.count 8 * 9 ^ w.count 9 * 25 ^ w.count 25 ∣
      rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases h8 : a = 8
      · subst a
        have hMul := Nat.mul_dvd_mul_left 8 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · by_cases h9 : a = 9
        · subst a
          have hMul := Nat.mul_dvd_mul_left 9 ih
          simpa [rootQuotientWordProduct, List.count_cons, h8, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
        · by_cases h25 : a = 25
          · subst a
            have hMul := Nat.mul_dvd_mul_left 25 ih
            simpa [rootQuotientWordProduct, List.count_cons, h8, h9, pow_succ,
              Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
          · have hDvd :
                8 ^ w.count 8 * 9 ^ w.count 9 * 25 ^ w.count 25 ∣
                  a * rootQuotientWordProduct w :=
              dvd_mul_of_dvd_right ih a
            simpa [rootQuotientWordProduct, List.count_cons, h8, h9, h25] using hDvd

/-- Universal lower bound on sparse-block word length. -/
theorem rootQuotientPrimeEightNineTwentyFiveCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeEightNineTwentyFiveBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeEightNineTwentyFiveCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m8 := w.count 8
  let m9 := w.count 9
  let m25 := w.count 25
  have hCount : rootQuotientPrimeFactorCount b =
      w.length + 2 * m8 + m9 + m25 := by
    rw [hProd]
    simpa [m8, m9, m25, Nat.add_assoc] using
      rootQuotientPrimeFactorCount_wordProduct_primeEightNineTwentyFive hw
  have hMacroDvd : 8 ^ m8 * 9 ^ m9 * 25 ^ m25 ∣ b := by
    rw [hProd]
    simpa [m8, m9, m25] using eight_nine_twentyFive_macro_powers_dvd_wordProduct w
  have hTwoPowDvd : 2 ^ (3 * m8) ∣ b := by
    have hDvdMacro : 2 ^ (3 * m8) ∣ 8 ^ m8 * 9 ^ m9 * 25 ^ m25 := by
      rw [show (8 : ℕ) = 2 ^ 3 by norm_num, pow_mul]
      exact dvd_mul_right _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hThreePowDvd : 3 ^ (2 * m9) ∣ b := by
    have hDvdMacro : 3 ^ (2 * m9) ∣ 8 ^ m8 * 9 ^ m9 * 25 ^ m25 := by
      rw [show (9 : ℕ) = 3 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_of_dvd_left (dvd_mul_left _ _) _
    exact dvd_trans hDvdMacro hMacroDvd
  have hFivePowDvd : 5 ^ (2 * m25) ∣ b := by
    have hDvdMacro : 5 ^ (2 * m25) ∣ 8 ^ m8 * 9 ^ m9 * 25 ^ m25 := by
      rw [show (25 : ℕ) = 5 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_left _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hTwoCap : 3 * m8 ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hThreeCap : 2 * m9 ≤ b.factorization 3 :=
    (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).1 hThreePowDvd
  have hFiveCap : 2 * m25 ≤ b.factorization 5 :=
    ((by norm_num : Nat.Prime 5).pow_dvd_iff_le_factorization hbZero).1 hFivePowDvd
  have hm8 : m8 ≤ b.factorization 2 / 3 := by omega
  have hm9 : m9 ≤ b.factorization 3 / 2 := by omega
  have hm25 : m25 ≤ b.factorization 5 / 2 := by omega
  dsimp [rootQuotientPrimeEightNineTwentyFiveCost]
  omega

/-- Remove literals `2,3,5` from a prime list. -/
def rootQuotientFilterAboveFive (l : List ℕ) : List ℕ :=
  l.filter (fun p : ℕ => p != 2 && p != 3 && p != 5)

/-- Length partition after removing the first three primes. -/
theorem length_filter_aboveFive_add_counts
    (l : List ℕ) :
    (rootQuotientFilterAboveFive l).length +
        l.count 2 + l.count 3 + l.count 5 = l.length := by
  induction l with
  | nil => simp [rootQuotientFilterAboveFive]
  | cons a l ih =>
      by_cases h2 : a = 2
      · subst a
        simp [rootQuotientFilterAboveFive, List.count_cons, ih]
      · by_cases h3 : a = 3
        · subst a
          simp [rootQuotientFilterAboveFive, List.count_cons, ih]
        · by_cases h5 : a = 5
          · subst a
            simp [rootQuotientFilterAboveFive, List.count_cons, ih]
          · simp [rootQuotientFilterAboveFive, List.count_cons, h2, h3, h5, ih]
            omega

/-- Product partition after removing `2,3,5`. -/
theorem pow_counts_two_three_five_mul_filter_prod
    (l : List ℕ) :
    2 ^ l.count 2 * 3 ^ l.count 3 * 5 ^ l.count 5 *
        (rootQuotientFilterAboveFive l).prod = l.prod := by
  induction l with
  | nil => simp [rootQuotientFilterAboveFive]
  | cons a l ih =>
      by_cases h2 : a = 2
      · subst a
        simp [rootQuotientFilterAboveFive, List.count_cons, ih, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      · by_cases h3 : a = 3
        · subst a
          simp [rootQuotientFilterAboveFive, List.count_cons, ih, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        · by_cases h5 : a = 5
          · subst a
            simp [rootQuotientFilterAboveFive, List.count_cons, ih, pow_succ,
              Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
          · simp [rootQuotientFilterAboveFive, List.count_cons, h2, h3, h5, ih,
              Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Canonical sparse-block word. -/
def rootQuotientPrimeEightNineTwentyFiveCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / 3) 8 ++
    List.replicate (b.factorization 2 % 3) 2 ++
      List.replicate (b.factorization 3 / 2) 9 ++
        List.replicate (b.factorization 3 % 2) 3 ++
          List.replicate (b.factorization 5 / 2) 25 ++
            List.replicate (b.factorization 5 % 2) 5 ++
              rootQuotientFilterAboveFive b.primeFactorsList

/-- Canonical word length is the sparse cost. -/
theorem rootQuotientPrimeEightNineTwentyFiveCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeEightNineTwentyFiveCanonicalWord b).length =
      rootQuotientPrimeEightNineTwentyFiveCost b := by
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hCount5 : b.primeFactorsList.count 5 = b.factorization 5 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_aboveFive_add_counts b.primeFactorsList
  rw [hCount2, hCount3, hCount5] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 3
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  have hDiv5 := Nat.mod_add_div' (b.factorization 5) 2
  dsimp [rootQuotientPrimeEightNineTwentyFiveCanonicalWord,
    rootQuotientPrimeEightNineTwentyFiveCost, rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  omega

/-- Canonical word product is the target integer. -/
theorem rootQuotientPrimeEightNineTwentyFiveCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct
      (rootQuotientPrimeEightNineTwentyFiveCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hCount5 : b.primeFactorsList.count 5 = b.factorization 5 :=
    Nat.primeFactorsList_count_eq
  have hSplit := pow_counts_two_three_five_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, hCount5, Nat.prod_primeFactorsList hbZero] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 3
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  have hDiv5 := Nat.mod_add_div' (b.factorization 5) 2
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeEightNineTwentyFiveCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3 *
          5 ^ b.factorization 5) *
        (rootQuotientFilterAboveFive b.primeFactorsList).prod := hSplit.symm
    _ = ((8 ^ (b.factorization 2 / 3) * 2 ^ (b.factorization 2 % 3)) *
          (9 ^ (b.factorization 3 / 2) * 3 ^ (b.factorization 3 % 2)) *
          (25 ^ (b.factorization 5 / 2) * 5 ^ (b.factorization 5 % 2))) *
        (rootQuotientFilterAboveFive b.primeFactorsList).prod := by
      rw [show (8 : ℕ) = 2 ^ 3 by norm_num,
        show (9 : ℕ) = 3 ^ 2 by norm_num,
        show (25 : ℕ) = 5 ^ 2 by norm_num,
        pow_mul, pow_mul, pow_mul,
        ← pow_add, ← pow_add, ← pow_add]
      congr <;> omega
    _ = 8 ^ (b.factorization 2 / 3) *
        (2 ^ (b.factorization 2 % 3) *
          (9 ^ (b.factorization 3 / 2) *
            (3 ^ (b.factorization 3 % 2) *
              (25 ^ (b.factorization 5 / 2) *
                (5 ^ (b.factorization 5 % 2) *
                  (rootQuotientFilterAboveFive b.primeFactorsList).prod))))) := by
      ac_rfl

/-- Canonical word stays inside the stable basis. -/
theorem rootQuotientPrimeEightNineTwentyFiveCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 5 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeEightNineTwentyFiveBasis N)
      (rootQuotientPrimeEightNineTwentyFiveCanonicalWord b) := by
  intro g hg
  simp only [rootQuotientPrimeEightNineTwentyFiveCanonicalWord,
    List.mem_append, List.mem_replicate] at hg
  rcases hg with h8 | h2 | h9 | h3 | h25 | h5 | ho
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inl ⟨Nat.prime_two, by omega⟩
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inl ⟨Nat.prime_three, by omega⟩
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inl ⟨by norm_num, hN⟩
  · have hgFactors : g ∈ b.primeFactorsList := (List.mem_filter.1 ho).1
    exact Or.inl ⟨Nat.prime_of_mem_primeFactorsList hgFactors,
      (Nat.le_of_mem_primeFactorsList hgFactors).trans hbN⟩

/-- Exact reachability law. -/
theorem rootQuotientPrimeEightNineTwentyFiveBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 5 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin h
        (RootQuotientPrimeEightNineTwentyFiveBasis N) b ↔
      rootQuotientPrimeEightNineTwentyFiveCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeEightNineTwentyFiveCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeEightNineTwentyFiveCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeEightNineTwentyFiveCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeEightNineTwentyFiveCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeEightNineTwentyFiveCanonicalWord_product hbPos

/-- Prime residuals above five are at least seven. -/
theorem seven_le_of_mem_filterAboveFive_primeFactors
    {b p : ℕ}
    (hp : p ∈ rootQuotientFilterAboveFive b.primeFactorsList) :
    7 ≤ p := by
  have hpMem := (List.mem_filter.1 hp).1
  have hpPred := (List.mem_filter.1 hp).2
  have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
  simp at hpPred
  omega

/-- Finite residual inequality for the stable prefix `2,2,3,5`. -/
theorem sixty_mul_seven_pow_residual_le
    {n u2 u3 u5 : ℕ}
    (hu2 : u2 < 3)
    (hu3 : u3 < 2)
    (hu5 : u5 < 2)
    (hk : 4 ≤ n + u2 + u3 + u5) :
    60 * 7 ^ (n + u2 + u3 + u5 - 4) ≤
      2 ^ u2 * 3 ^ u3 * 5 ^ u5 * 7 ^ n := by
  have h2Cases : u2 = 0 ∨ u2 = 1 ∨ u2 = 2 := by omega
  have h3Cases : u3 = 0 ∨ u3 = 1 := by omega
  have h5Cases : u5 = 0 ∨ u5 = 1 := by omega
  rcases h2Cases with rfl | rfl | rfl <;>
    rcases h3Cases with rfl | rfl <;>
      rcases h5Cases with rfl | rfl <;> simp_all
  all_goals
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 1 ≤ n by omega)}
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 2 ≤ n by omega)}
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 3 ≤ n by omega)}
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 4 ≤ n by omega)}
    simp [pow_add] <;> nlinarith [show 0 < 7 ^ t by positivity]

/-- Exact q=7 hard-shell lower bound from cost four onward. -/
theorem sixty_mul_seven_pow_sub_four_le_of_primeEightNineTwentyFiveCost
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 4 ≤ k)
    (hCost : rootQuotientPrimeEightNineTwentyFiveCost b = k) :
    60 * 7 ^ (k - 4) ≤ b := by
  let q8 := b.factorization 2 / 3
  let u2 := b.factorization 2 % 3
  let q9 := b.factorization 3 / 2
  let u3 := b.factorization 3 % 2
  let q25 := b.factorization 5 / 2
  let u5 := b.factorization 5 % 2
  let wo := rootQuotientFilterAboveFive b.primeFactorsList
  let o := wo.length
  have hLenRaw := rootQuotientPrimeEightNineTwentyFiveCanonicalWord_length b
  have hLen : q8 + u2 + q9 + u3 + q25 + u5 + o = k := by
    rw [hCost] at hLenRaw
    simpa [rootQuotientPrimeEightNineTwentyFiveCanonicalWord,
      q8, u2, q9, u3, q25, u5, wo, o, Nat.add_assoc] using hLenRaw
  have hu2 : u2 < 3 := by dsimp [u2]; exact Nat.mod_lt _ (by omega)
  have hu3 : u3 < 2 := by dsimp [u3]; exact Nat.mod_lt _ (by omega)
  have hu5 : u5 < 2 := by dsimp [u5]; exact Nat.mod_lt _ (by omega)
  have hWo7 : 7 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    exact seven_le_of_mem_filterAboveFive_primeFactors hp
  have h8 : 7 ^ q8 ≤ 8 ^ q8 := Nat.pow_le_pow_left (by omega) q8
  have h9 : 7 ^ q9 ≤ 9 ^ q9 := Nat.pow_le_pow_left (by omega) q9
  have h25 : 7 ^ q25 ≤ 25 ^ q25 := Nat.pow_le_pow_left (by omega) q25
  have hProduct := rootQuotientPrimeEightNineTwentyFiveCanonicalWord_product hbPos
  have hB : b = 8 ^ q8 * 2 ^ u2 * 9 ^ q9 * 3 ^ u3 *
      25 ^ q25 * 5 ^ u5 * wo.prod := by
    simpa [rootQuotientPrimeEightNineTwentyFiveCanonicalWord,
      q8, u2, q9, u3, q25, u5, wo,
      rootQuotientWordProduct_eq_prod, Nat.mul_assoc] using hProduct
  have hLower : 2 ^ u2 * 3 ^ u3 * 5 ^ u5 * 7 ^ (q8 + q9 + q25 + o) ≤ b := by
    calc
      2 ^ u2 * 3 ^ u3 * 5 ^ u5 * 7 ^ (q8 + q9 + q25 + o) =
          (7 ^ q8 * 2 ^ u2) *
            (7 ^ q9 * 3 ^ u3) *
              (7 ^ q25 * 5 ^ u5) * 7 ^ o := by
        simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      _ ≤ (8 ^ q8 * 2 ^ u2) *
            (9 ^ q9 * 3 ^ u3) *
              (25 ^ q25 * 5 ^ u5) * wo.prod := by
        exact Nat.mul_le_mul
          (Nat.mul_le_mul
            (Nat.mul_le_mul
              (Nat.mul_le_mul_right _ h8)
              (Nat.mul_le_mul_right _ h9))
            (Nat.mul_le_mul_right _ h25)) hWo7
      _ = b := by rw [hB]; ac_rfl
  have hResidual := sixty_mul_seven_pow_residual_le
    (n := q8 + q9 + q25 + o) (u2 := u2) (u3 := u3) (u5 := u5)
    hu2 hu3 hu5 (by omega)
  rw [show k - 4 = (q8 + q9 + q25 + o) + u2 + u3 + u5 - 4 by omega]
  exact hResidual.trans hLower

/-- Concrete q=7 hard-shell witness. -/
theorem rootQuotientPrimeEightNineTwentyFiveCost_sixty_mul_seven_pow
    {k : ℕ}
    (hk : 4 ≤ k) :
    rootQuotientPrimeEightNineTwentyFiveCost (60 * 7 ^ (k - 4)) = k := by
  let n := k - 4
  have hkEq : k = n + 4 := by dsimp [n]; omega
  have hTwo : (60 * 7 ^ n).factorization 2 = 2 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have h60 : (60 : ℕ).factorization 2 = 2 := by norm_num [Nat.factorization]
    have h7 : (7 : ℕ).factorization 2 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [h60, h7]
  have hThree : (60 * 7 ^ n).factorization 3 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have h60 : (60 : ℕ).factorization 3 = 1 := by norm_num [Nat.factorization]
    have h7 : (7 : ℕ).factorization 3 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [h60, h7]
  have hFive : (60 * 7 ^ n).factorization 5 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have h60 : (60 : ℕ).factorization 5 = 1 := by norm_num [Nat.factorization]
    have h7 : (7 : ℕ).factorization 5 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [h60, h7]
  have h60Omega : rootQuotientPrimeFactorCount 60 = 4 := by norm_num [rootQuotientPrimeFactorCount]
  have h7Omega : rootQuotientPrimeFactorCount 7 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime (by norm_num : Nat.Prime 7)]
    simp
  have hOmega : rootQuotientPrimeFactorCount (60 * 7 ^ n) = n + 4 := by
    calc
      rootQuotientPrimeFactorCount (60 * 7 ^ n) =
          rootQuotientPrimeFactorCount 60 + rootQuotientPrimeFactorCount (7 ^ n) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 4 + n := by
        rw [h60Omega, rootQuotientPrimeFactorCount_pow (by omega), h7Omega]
        omega
      _ = n + 4 := by omega
  rw [hkEq]
  simp [rootQuotientPrimeEightNineTwentyFiveCost,
    hTwo, hThree, hFive, hOmega]

/-- Exact stable q=7 high-root threshold. -/
theorem primeEightNineTwentyFiveBasis_separates_iff_stateBound_lt_shell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 5 ≤ N)
    (hh : 3 ≤ h)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeEightNineTwentyFiveBasis N) ↔
      N < 60 * 7 ^ (h - 3) := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 60 * 7 ^ (h - 3) ≤ N := by omega
    let b := 60 * 7 ^ (h - 3)
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeEightNineTwentyFiveBasis N)
        (by omega) rootQuotientPrimeEightNineTwentyFiveBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeEightNineTwentyFiveBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeEightNineTwentyFiveCost b = h + 1 := by
      dsimp [b]
      simpa [show h + 1 - 4 = h - 3 by omega] using
        (rootQuotientPrimeEightNineTwentyFiveCost_sixty_mul_seven_pow
          (k := h + 1) (by omega))
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeEightNineTwentyFiveBasis N)
      (by omega) rootQuotientPrimeEightNineTwentyFiveBasis_positive).2
    intro b hbPos hbN _hbFree
    apply (rootQuotientPrimeEightNineTwentyFiveBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hCost : h + 1 ≤ rootQuotientPrimeEightNineTwentyFiveCost b := by omega
    have hCostFour : 4 ≤ rootQuotientPrimeEightNineTwentyFiveCost b := by omega
    have hShell := sixty_mul_seven_pow_sub_four_le_of_primeEightNineTwentyFiveCost
      hbPos hCostFour rfl
    have hPowMono : 7 ^ (h - 3) ≤
        7 ^ (rootQuotientPrimeEightNineTwentyFiveCost b - 4) :=
      Nat.pow_le_pow_right (by omega) (by omega)
    have hContr : 60 * 7 ^ (h - 3) ≤ N :=
      (Nat.mul_le_mul_left 60 hPowMono).trans (hShell.trans hbN)
    omega

end EnterpriseMath.Quotient
