import EnterpriseMath.Quotient.RootQuotientPrimeFourNineMetric
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with the minimal next-prime-5 ladder macros
`8=2^3` and `9=3^2`. -/
def RootQuotientPrimeEightNineBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({8, 9} : Set ℕ)

/-- Exact pointwise cost for the prime-eight-nine ISA. -/
def rootQuotientPrimeEightNineCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b -
    2 * (b.factorization 2 / 3) - b.factorization 3 / 2

/-- The prime-eight-nine ISA is positive. -/
theorem rootQuotientPrimeEightNineBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeEightNineBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · simp at hgMacro
    rcases hgMacro with rfl | rfl <;> omega

/-- Prime-token count of a prime-eight-nine word product. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeEightNine
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeEightNineBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + 2 * w.count 8 + w.count 9 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeEightNineBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeEightNineBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeEightNineBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeEightNineBasis_positive a haBasis
      rw [rootQuotientWordProduct,
        rootQuotientPrimeFactorCount_mul haPos hTailPos, ih hwTail]
      rcases haBasis with haPrime | haMacro
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have haNeEight : a ≠ 8 := by
          intro hEq
          subst a
          norm_num at haPrime
        have haNeNine : a ≠ 9 := by
          intro hEq
          subst a
          norm_num at haPrime
        rw [haCount, List.count_cons, List.count_cons]
        simp [haNeEight, haNeNine]
        omega
      · simp at haMacro
        rcases haMacro with rfl | rfl
        · have hEightCount : rootQuotientPrimeFactorCount 8 = 3 := by
            simpa using rootQuotientPrimeFactorCount_two_pow 3
          rw [hEightCount, List.count_cons, List.count_cons]
          simp
          omega
        · have hNineCount : rootQuotientPrimeFactorCount 9 = 2 := by
            have hThree : rootQuotientPrimeFactorCount 3 = 1 := by
              rw [rootQuotientPrimeFactorCount,
                Nat.primeFactorsList_prime Nat.prime_three]
              simp
            calc
              rootQuotientPrimeFactorCount 9 =
                  rootQuotientPrimeFactorCount (3 ^ 2) := by norm_num
              _ = 2 * rootQuotientPrimeFactorCount 3 :=
                rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le
              _ = 2 := by rw [hThree]
          rw [hNineCount, List.count_cons, List.count_cons]
          simp
          omega

/-- Macro copies contribute their pure-power divisors. -/
theorem eight_pow_count_mul_nine_pow_count_dvd_wordProduct
    (w : List ℕ) :
    8 ^ w.count 8 * 9 ^ w.count 9 ∣ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases haEight : a = 8
      · subst a
        have hMul := Nat.mul_dvd_mul_left 8 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · by_cases haNine : a = 9
        · subst a
          have hMul := Nat.mul_dvd_mul_left 9 ih
          simpa [rootQuotientWordProduct, List.count_cons, haEight, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
        · have hDvd : 8 ^ w.count 8 * 9 ^ w.count 9 ∣
              a * rootQuotientWordProduct w :=
            dvd_mul_of_dvd_right ih a
          simpa [rootQuotientWordProduct, List.count_cons, haEight, haNine] using hDvd

/-- Universal lower bound on prime-eight-nine word length. -/
theorem rootQuotientPrimeEightNineCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeEightNineBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeEightNineCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m8 := w.count 8
  let m9 := w.count 9
  have hCount : rootQuotientPrimeFactorCount b =
      w.length + 2 * m8 + m9 := by
    rw [hProd]
    simpa [m8, m9, Nat.add_assoc] using
      rootQuotientPrimeFactorCount_wordProduct_primeEightNine hw
  have hMacroDvd : 8 ^ m8 * 9 ^ m9 ∣ b := by
    rw [hProd]
    simpa [m8, m9] using eight_pow_count_mul_nine_pow_count_dvd_wordProduct w
  have hTwoPowDvd : 2 ^ (3 * m8) ∣ b := by
    have hDvdMacro : 2 ^ (3 * m8) ∣ 8 ^ m8 * 9 ^ m9 := by
      rw [show (8 : ℕ) = 2 ^ 3 by norm_num, pow_mul]
      exact dvd_mul_right _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hThreePowDvd : 3 ^ (2 * m9) ∣ b := by
    have hDvdMacro : 3 ^ (2 * m9) ∣ 8 ^ m8 * 9 ^ m9 := by
      rw [show (9 : ℕ) = 3 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_left _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hTwoCap : 3 * m8 ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hThreeCap : 2 * m9 ≤ b.factorization 3 :=
    (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).1 hThreePowDvd
  have hm8 : m8 ≤ b.factorization 2 / 3 := by omega
  have hm9 : m9 ≤ b.factorization 3 / 2 := by omega
  dsimp [rootQuotientPrimeEightNineCost]
  omega

/-- Canonical word for the minimal next-prime-5 ladder. -/
def rootQuotientPrimeEightNineCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / 3) 8 ++
    List.replicate (b.factorization 2 % 3) 2 ++
      List.replicate (b.factorization 3 / 2) 9 ++
        List.replicate (b.factorization 3 % 2) 3 ++
          b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)

/-- Canonical word has exactly the weighted cost. -/
theorem rootQuotientPrimeEightNineCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeEightNineCanonicalWord b).length =
      rootQuotientPrimeEightNineCost b := by
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_three_add_counts b.primeFactorsList
  rw [hCount2, hCount3] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 3
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  dsimp [rootQuotientPrimeEightNineCanonicalWord,
    rootQuotientPrimeEightNineCost, rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  omega

/-- Canonical word product is the target integer. -/
theorem rootQuotientPrimeEightNineCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeEightNineCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit :=
    pow_count_two_mul_pow_count_three_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, Nat.prod_primeFactorsList hbZero] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 3
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeEightNineCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := hSplit.symm
    _ = ((8 ^ (b.factorization 2 / 3) *
          2 ^ (b.factorization 2 % 3)) *
          (9 ^ (b.factorization 3 / 2) *
          3 ^ (b.factorization 3 % 2))) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := by
      rw [show (8 : ℕ) = 2 ^ 3 by norm_num,
        show (9 : ℕ) = 3 ^ 2 by norm_num,
        pow_mul, pow_mul, ← pow_add, ← pow_add]
      congr <;> omega
    _ = 8 ^ (b.factorization 2 / 3) *
        (2 ^ (b.factorization 2 % 3) *
          (9 ^ (b.factorization 3 / 2) *
            (3 ^ (b.factorization 3 % 2) *
              (b.primeFactorsList.filter
                (fun p : ℕ => p != 2 && p != 3)).prod))) := by ac_rfl

/-- Canonical word stays in bounded primes plus `8,9`. -/
theorem rootQuotientPrimeEightNineCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 3 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeEightNineBasis N)
      (rootQuotientPrimeEightNineCanonicalWord b) := by
  intro g hg
  simp only [rootQuotientPrimeEightNineCanonicalWord, List.mem_append,
    List.mem_replicate] at hg
  rcases hg with h8 | h2 | h9 | h3 | ho
  · subst g
    exact Or.inr (by simp)
  · subst g
    exact Or.inl ⟨Nat.prime_two, by omega⟩
  · subst g
    exact Or.inr (by simp)
  · subst g
    exact Or.inl ⟨Nat.prime_three, hN⟩
  · have hgFactors : g ∈ b.primeFactorsList := (List.mem_filter.1 ho).1
    exact Or.inl ⟨Nat.prime_of_mem_primeFactorsList hgFactors,
      (Nat.le_of_mem_primeFactorsList hgFactors).trans hbN⟩

/-- Exact pointwise reachability law for the next-prime-5 ladder. -/
theorem rootQuotientPrimeEightNineBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 3 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin h
        (RootQuotientPrimeEightNineBasis N) b ↔
      rootQuotientPrimeEightNineCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeEightNineCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeEightNineCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeEightNineCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeEightNineCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeEightNineCanonicalWord_product hbPos

/-- Finite residual inequality behind the stable `8,9` shell. -/
theorem twelve_mul_five_pow_residual_le
    {n u v : ℕ}
    (hu : u < 3)
    (hv : v < 2)
    (hk : 3 ≤ n + u + v) :
    12 * 5 ^ (n + u + v - 3) ≤ 2 ^ u * 3 ^ v * 5 ^ n := by
  have huCases : u = 0 ∨ u = 1 ∨ u = 2 := by omega
  have hvCases : v = 0 ∨ v = 1 := by omega
  rcases huCases with rfl | rfl | rfl <;> rcases hvCases with rfl | rfl
  · have hn : 3 ≤ n := by omega
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
    simp [pow_add]
    nlinarith [show 0 < 5 ^ t by positivity]
  · have hn : 2 ≤ n := by omega
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
    simp [pow_add]
    nlinarith [show 0 < 5 ^ t by positivity]
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

/-- Exact stable hard-shell lower bound from cost three onward. -/
theorem twelve_mul_five_pow_sub_three_le_of_primeEightNineCost
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 3 ≤ k)
    (hCost : rootQuotientPrimeEightNineCost b = k) :
    12 * 5 ^ (k - 3) ≤ b := by
  let m8 := b.factorization 2 / 3
  let u2 := b.factorization 2 % 3
  let m9 := b.factorization 3 / 2
  let u3 := b.factorization 3 % 2
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)
  let o := wo.length
  have hLenRaw := rootQuotientPrimeEightNineCanonicalWord_length b
  have hLen : m8 + u2 + m9 + u3 + o = k := by
    rw [hCost] at hLenRaw
    simpa [rootQuotientPrimeEightNineCanonicalWord, m8, u2, m9, u3, wo, o,
      Nat.add_assoc] using hLenRaw
  have hu2 : u2 < 3 := by
    dsimp [u2]
    exact Nat.mod_lt _ (by omega)
  have hu3 : u3 < 2 := by
    dsimp [u3]
    exact Nat.mod_lt _ (by omega)
  have hWo5 : 5 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    have hpMem := (List.mem_filter.1 hp).1
    have hpPred := (List.mem_filter.1 hp).2
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
    simp at hpPred
    omega
  have hm8 : 5 ^ m8 ≤ 8 ^ m8 := Nat.pow_le_pow_left (by omega) m8
  have hm9 : 5 ^ m9 ≤ 9 ^ m9 := Nat.pow_le_pow_left (by omega) m9
  have hProduct := rootQuotientPrimeEightNineCanonicalWord_product hbPos
  have hB : b = 8 ^ m8 * 2 ^ u2 * 9 ^ m9 * 3 ^ u3 * wo.prod := by
    simpa [rootQuotientPrimeEightNineCanonicalWord, m8, u2, m9, u3, wo,
      rootQuotientWordProduct_eq_prod, Nat.mul_assoc] using hProduct
  have hLower : 2 ^ u2 * 3 ^ u3 * 5 ^ (m8 + m9 + o) ≤ b := by
    calc
      2 ^ u2 * 3 ^ u3 * 5 ^ (m8 + m9 + o) =
          (5 ^ m8 * 2 ^ u2) * (5 ^ m9 * 3 ^ u3) * 5 ^ o := by
        simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      _ ≤ (8 ^ m8 * 2 ^ u2) * (9 ^ m9 * 3 ^ u3) * wo.prod := by
        exact Nat.mul_le_mul
          (Nat.mul_le_mul
            (Nat.mul_le_mul_right _ hm8)
            (Nat.mul_le_mul_right _ hm9)) hWo5
      _ = b := by rw [hB]; ac_rfl
  have hResidual := twelve_mul_five_pow_residual_le
    (n := m8 + m9 + o) (u := u2) (v := u3)
    hu2 hu3 (by omega)
  rw [show k - 3 = (m8 + m9 + o) + u2 + u3 - 3 by omega]
  exact hResidual.trans hLower

/-- Concrete factorization of the stable hard-shell witness. -/
theorem rootQuotientPrimeEightNineCost_twelve_mul_five_pow
    {k : ℕ}
    (hk : 3 ≤ k) :
    rootQuotientPrimeEightNineCost (12 * 5 ^ (k - 3)) = k := by
  let n := k - 3
  have hkEq : k = n + 3 := by dsimp [n]; omega
  have hTwelveTwo : (12 : ℕ).factorization 2 = 2 := by
    rw [show (12 : ℕ) = 4 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have hFourTwo : (4 : ℕ).factorization 2 = 2 := by
      simpa [show (4 : ℕ) = 2 ^ 2 by norm_num] using
        (Nat.factorization_pow_self (n := 2) Nat.prime_two)
    simp [hFourTwo, Nat.Prime.factorization]
  have hTwelveThree : (12 : ℕ).factorization 3 = 1 := by
    rw [show (12 : ℕ) = 4 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    have hFourThree : (4 : ℕ).factorization 3 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [hFourThree, Nat.Prime.factorization]
  have hFiveTwo : (5 : ℕ).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  have hFiveThree : (5 : ℕ).factorization 3 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  have hTwoFact : (12 * 5 ^ n).factorization 2 = 2 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    simp [hTwelveTwo, hFiveTwo]
  have hThreeFact : (12 * 5 ^ n).factorization 3 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    simp [hTwelveThree, hFiveThree]
  have hTwelveOmega : rootQuotientPrimeFactorCount 12 = 3 := by
    have hFour : rootQuotientPrimeFactorCount 4 = 2 := by
      simpa using rootQuotientPrimeFactorCount_two_pow 2
    have hThree : rootQuotientPrimeFactorCount 3 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_three]
      simp
    calc
      rootQuotientPrimeFactorCount 12 =
          rootQuotientPrimeFactorCount (4 * 3) := by norm_num
      _ = rootQuotientPrimeFactorCount 4 + rootQuotientPrimeFactorCount 3 :=
        rootQuotientPrimeFactorCount_mul (by omega) (by omega)
      _ = 3 := by rw [hFour, hThree]
  have hFiveOmega : rootQuotientPrimeFactorCount 5 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime (by norm_num : Nat.Prime 5)]
    simp
  have hOmega : rootQuotientPrimeFactorCount (12 * 5 ^ n) = n + 3 := by
    calc
      rootQuotientPrimeFactorCount (12 * 5 ^ n) =
          rootQuotientPrimeFactorCount 12 +
            rootQuotientPrimeFactorCount (5 ^ n) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 3 + n * 1 := by
        rw [hTwelveOmega, rootQuotientPrimeFactorCount_pow (by omega), hFiveOmega]
      _ = n + 3 := by omega
  rw [hkEq]
  simp [rootQuotientPrimeEightNineCost, hTwoFact, hThreeFact, hOmega]

/-- Exact high-root threshold for the stable `8,9` ISA. -/
theorem primeEightNineBasis_separates_iff_stateBound_lt_shell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 3 ≤ N)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeEightNineBasis N) ↔
      N < 12 * 5 ^ (h - 2) := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 12 * 5 ^ (h - 2) ≤ N := by omega
    let b := 12 * 5 ^ (h - 2)
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeEightNineBasis N)
        (by omega) rootQuotientPrimeEightNineBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeEightNineBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeEightNineCost b = h + 1 := by
      dsimp [b]
      simpa [show h + 1 - 3 = h - 2 by omega] using
        (rootQuotientPrimeEightNineCost_twelve_mul_five_pow
          (k := h + 1) (by omega))
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeEightNineBasis N)
      (by omega) rootQuotientPrimeEightNineBasis_positive).2
    intro b hbPos hbN _hbFree
    apply (rootQuotientPrimeEightNineBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hCost : h + 1 ≤ rootQuotientPrimeEightNineCost b := by omega
    have hCostThree : 3 ≤ rootQuotientPrimeEightNineCost b := by omega
    have hShell := twelve_mul_five_pow_sub_three_le_of_primeEightNineCost
      hbPos hCostThree rfl
    have hPowMono : 5 ^ (h - 2) ≤
        5 ^ (rootQuotientPrimeEightNineCost b - 3) :=
      Nat.pow_le_pow_right (by omega) (by omega)
    have hContr : 12 * 5 ^ (h - 2) ≤ N :=
      (Nat.mul_le_mul_left 12 hPowMono).trans (hShell.trans hbN)
    omega

end EnterpriseMath.Quotient
