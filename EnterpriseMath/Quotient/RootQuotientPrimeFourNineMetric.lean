import EnterpriseMath.Quotient.RootQuotientPrimeFourSixMetric
import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with the two pure-direction macros `4=2^2` and
`9=3^2`. -/
def RootQuotientPrimeFourNineBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({4, 9} : Set ℕ)

/-- Exact pointwise cost for the prime-four-nine ISA. -/
def rootQuotientPrimeFourNineCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b -
    b.factorization 2 / 2 - b.factorization 3 / 2

/-- Prime-token count of a prime-four-nine word product. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeFourNine
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + w.count 4 + w.count 9 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeFourNineBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w := by
        apply rootQuotientWordProduct_one_le_of_positiveGenerators
        · intro g hg
          rcases hg with hgPrime | hgMacro
          · exact hgPrime.1.one_le
          · simp at hgMacro
            rcases hgMacro with rfl | rfl <;> omega
        · exact hwTail
      have haPos : 1 ≤ a := by
        rcases haBasis with haPrime | haMacro
        · exact haPrime.1.one_le
        · simp at haMacro
          rcases haMacro with rfl | rfl <;> omega
      rw [rootQuotientWordProduct]
      rw [rootQuotientPrimeFactorCount_mul haPos hTailPos]
      rw [ih hwTail]
      rcases haBasis with haPrime | haMacro
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have haNeFour : a ≠ 4 := by
          intro hEq
          subst a
          norm_num at haPrime
        have haNeNine : a ≠ 9 := by
          intro hEq
          subst a
          norm_num at haPrime
        rw [haCount, List.count_cons, List.count_cons]
        simp [haNeFour, haNeNine]
        omega
      · simp at haMacro
        rcases haMacro with rfl | rfl
        · have hFourCount : rootQuotientPrimeFactorCount 4 = 2 := by
            simpa using rootQuotientPrimeFactorCount_two_pow 2
          rw [hFourCount, List.count_cons, List.count_cons]
          simp
          omega
        · have hNineCount : rootQuotientPrimeFactorCount 9 = 2 := by
            have hThreeCount : rootQuotientPrimeFactorCount 3 = 1 := by
              rw [rootQuotientPrimeFactorCount,
                Nat.primeFactorsList_prime Nat.prime_three]
              simp
            calc
              rootQuotientPrimeFactorCount 9 =
                  rootQuotientPrimeFactorCount (3 ^ 2) := by norm_num
              _ = 2 * rootQuotientPrimeFactorCount 3 :=
                rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le
              _ = 2 := by rw [hThreeCount]
          rw [hNineCount, List.count_cons, List.count_cons]
          simp
          omega

/-- Macro copies contribute disjoint pure-power divisors. -/
theorem four_pow_count_mul_nine_pow_count_dvd_wordProduct
    (w : List ℕ) :
    4 ^ w.count 4 * 9 ^ w.count 9 ∣ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases haFour : a = 4
      · subst a
        have hMul := Nat.mul_dvd_mul_left 4 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · by_cases haNine : a = 9
        · subst a
          have hMul := Nat.mul_dvd_mul_left 9 ih
          simpa [rootQuotientWordProduct, List.count_cons, haFour, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
        · have hDvd : 4 ^ w.count 4 * 9 ^ w.count 9 ∣
              a * rootQuotientWordProduct w :=
            dvd_mul_of_dvd_right ih a
          simpa [rootQuotientWordProduct, List.count_cons, haFour, haNine] using hDvd

/-- Universal lower bound on prime-four-nine word length. -/
theorem rootQuotientPrimeFourNineCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeFourNineBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeFourNineCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m4 := w.count 4
  let m9 := w.count 9
  have hCount : rootQuotientPrimeFactorCount b = w.length + m4 + m9 := by
    rw [hProd]
    simpa [m4, m9, Nat.add_assoc] using
      rootQuotientPrimeFactorCount_wordProduct_primeFourNine hw
  have hMacroDvd : 4 ^ m4 * 9 ^ m9 ∣ b := by
    rw [hProd]
    simpa [m4, m9] using four_pow_count_mul_nine_pow_count_dvd_wordProduct w
  have hTwoPowDvd : 2 ^ (2 * m4) ∣ b := by
    have hDvdMacro : 2 ^ (2 * m4) ∣ 4 ^ m4 * 9 ^ m9 := by
      rw [show (4 : ℕ) = 2 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_right _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hThreePowDvd : 3 ^ (2 * m9) ∣ b := by
    have hDvdMacro : 3 ^ (2 * m9) ∣ 4 ^ m4 * 9 ^ m9 := by
      rw [show (9 : ℕ) = 3 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_left _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hTwoCap : 2 * m4 ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hThreeCap : 2 * m9 ≤ b.factorization 3 :=
    (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).1 hThreePowDvd
  have hm4 : m4 ≤ b.factorization 2 / 2 := by omega
  have hm9 : m9 ≤ b.factorization 3 / 2 := by omega
  dsimp [rootQuotientPrimeFourNineCost]
  omega

/-- Canonical word: pair `2` tokens into `4`, pair `3` tokens into `9`, and
leave all remaining prime factors literal. -/
def rootQuotientPrimeFourNineCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / 2) 4 ++
    List.replicate (b.factorization 2 % 2) 2 ++
      List.replicate (b.factorization 3 / 2) 9 ++
        List.replicate (b.factorization 3 % 2) 3 ++
          b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)

/-- Canonical word has exactly the weighted cost. -/
theorem rootQuotientPrimeFourNineCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeFourNineCanonicalWord b).length =
      rootQuotientPrimeFourNineCost b := by
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_three_add_counts b.primeFactorsList
  rw [hCount2, hCount3] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 2
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  dsimp [rootQuotientPrimeFourNineCanonicalWord,
    rootQuotientPrimeFourNineCost, rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  omega

/-- Canonical word product is the target integer. -/
theorem rootQuotientPrimeFourNineCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeFourNineCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit :=
    pow_count_two_mul_pow_count_three_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, Nat.prod_primeFactorsList hbZero] at hSplit
  have hDiv2 := Nat.mod_add_div' (b.factorization 2) 2
  have hDiv3 := Nat.mod_add_div' (b.factorization 3) 2
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeFourNineCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := hSplit.symm
    _ = ((4 ^ (b.factorization 2 / 2) *
          2 ^ (b.factorization 2 % 2)) *
          (9 ^ (b.factorization 3 / 2) *
          3 ^ (b.factorization 3 % 2))) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := by
      rw [show (4 : ℕ) = 2 ^ 2 by norm_num,
        show (9 : ℕ) = 3 ^ 2 by norm_num,
        pow_mul, pow_mul, ← pow_add, ← pow_add]
      congr <;> omega
    _ = 4 ^ (b.factorization 2 / 2) *
        (2 ^ (b.factorization 2 % 2) *
          (9 ^ (b.factorization 3 / 2) *
            (3 ^ (b.factorization 3 % 2) *
              (b.primeFactorsList.filter
                (fun p : ℕ => p != 2 && p != 3)).prod))) := by ac_rfl

/-- Canonical word stays in bounded primes plus `4,9`. -/
theorem rootQuotientPrimeFourNineCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 3 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeFourNineBasis N)
      (rootQuotientPrimeFourNineCanonicalWord b) := by
  intro g hg
  simp only [rootQuotientPrimeFourNineCanonicalWord, List.mem_append,
    List.mem_replicate] at hg
  rcases hg with h4 | h2 | h9 | h3 | ho
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

/-- Exact pointwise reachability law for bounded primes plus `4,9`. -/
theorem rootQuotientPrimeFourNineBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 3 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin h
        (RootQuotientPrimeFourNineBasis N) b ↔
      rootQuotientPrimeFourNineCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeFourNineCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeFourNineCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeFourNineCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeFourNineCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeFourNineCanonicalWord_product hbPos

/-- Hard shell of the `4,9` code from cost two onward. -/
theorem six_mul_four_pow_sub_two_le_of_primeFourNineCost
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 2 ≤ k)
    (hCost : rootQuotientPrimeFourNineCost b = k) :
    6 * 4 ^ (k - 2) ≤ b := by
  have hWordProd := rootQuotientPrimeFourNineCanonicalWord_product hbPos
  let m4 := b.factorization 2 / 2
  let u2 := b.factorization 2 % 2
  let m9 := b.factorization 3 / 2
  let u3 := b.factorization 3 % 2
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)
  let o := wo.length
  have hLenRaw := rootQuotientPrimeFourNineCanonicalWord_length b
  have hLen : m4 + u2 + m9 + u3 + o = k := by
    rw [hCost] at hLenRaw
    simpa [rootQuotientPrimeFourNineCanonicalWord, m4, u2, m9, u3, wo, o,
      Nat.add_assoc] using hLenRaw
  have hu2 : u2 < 2 := by
    dsimp [u2]
    exact Nat.mod_lt _ (by omega)
  have hu3 : u3 < 2 := by
    dsimp [u3]
    exact Nat.mod_lt _ (by omega)
  have hWo : 5 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    have hpMem := (List.mem_filter.1 hp).1
    have hpPred := (List.mem_filter.1 hp).2
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
    simp at hpPred
    omega
  have hB : b = 4 ^ m4 * 2 ^ u2 * 9 ^ m9 * 3 ^ u3 * wo.prod := by
    simpa [rootQuotientPrimeFourNineCanonicalWord, m4, u2, m9, u3, wo,
      rootQuotientWordProduct_eq_prod, Nat.mul_assoc] using hWordProd
  have hRest4 : 4 ^ o ≤ wo.prod :=
    (Nat.pow_le_pow_left (by omega) o).trans hWo
  have hm9 : 4 ^ m9 ≤ 9 ^ m9 := Nat.pow_le_pow_left (by omega) m9
  rcases Nat.lt_two_iff.mp hu2 with hu20 | hu21 <;>
    rcases Nat.lt_two_iff.mp hu3 with hu30 | hu31
  · have hAll : 4 ^ (m4 + m9 + o) ≤ b := by
      calc
        4 ^ (m4 + m9 + o) = 4 ^ m4 * 4 ^ m9 * 4 ^ o := by
          simp [pow_add, Nat.mul_assoc]
        _ ≤ 4 ^ m4 * 9 ^ m9 * wo.prod := by
          exact Nat.mul_le_mul (Nat.mul_le_mul_left _ hm9) hRest4
        _ = b := by rw [hB]; simp [hu20, hu30, Nat.mul_assoc]
    have hK : k = m4 + m9 + o := by omega
    rw [hK]
    have hSixLe : 6 * 4 ^ (m4 + m9 + o - 2) ≤ 4 ^ (m4 + m9 + o) := by
      obtain ⟨n, hn⟩ := Nat.exists_eq_add_of_le hk
      subst k
      norm_num at hK ⊢
      nlinarith [show 0 < 4 ^ n by positivity]
    exact hSixLe.trans hAll
  · have hAll : 3 * 4 ^ (m4 + m9 + o) ≤ b := by
      calc
        3 * 4 ^ (m4 + m9 + o) =
            4 ^ m4 * 4 ^ m9 * 3 * 4 ^ o := by
          simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        _ ≤ 4 ^ m4 * 9 ^ m9 * 3 * wo.prod := by
          exact Nat.mul_le_mul (Nat.mul_le_mul (Nat.mul_le_mul_left _ hm9)
            (le_refl 3)) hRest4
        _ = b := by rw [hB]; simp [hu20, hu31, Nat.mul_assoc]
    have hK : k = m4 + m9 + 1 + o := by omega
    rw [hK]
    have hNum : 6 * 4 ^ (m4 + m9 + 1 + o - 2) ≤
        3 * 4 ^ (m4 + m9 + o) := by
      omega
    exact hNum.trans hAll
  · have hAll : 2 * 4 ^ (m4 + m9 + o) ≤ b := by
      calc
        2 * 4 ^ (m4 + m9 + o) =
            4 ^ m4 * 2 * 4 ^ m9 * 4 ^ o := by
          simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        _ ≤ 4 ^ m4 * 2 * 9 ^ m9 * wo.prod := by
          exact Nat.mul_le_mul (Nat.mul_le_mul (Nat.mul_le_mul_left _ hm9)
            (le_refl 2)) hRest4
        _ = b := by rw [hB]; simp [hu21, hu30, Nat.mul_assoc]
    have hK : k = m4 + 1 + m9 + o := by omega
    rw [hK]
    have hNum : 6 * 4 ^ (m4 + 1 + m9 + o - 2) ≤
        2 * 4 ^ (m4 + m9 + o) := by
      omega
    exact hNum.trans hAll
  · have hAll : 6 * 4 ^ (m4 + m9 + o) ≤ b := by
      calc
        6 * 4 ^ (m4 + m9 + o) =
            4 ^ m4 * 2 * 9 ^ m9 * 3 * 4 ^ o := by
          simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
          nlinarith
        _ ≤ 4 ^ m4 * 2 * 9 ^ m9 * 3 * wo.prod := by
          exact Nat.mul_le_mul_left _ hRest4
        _ = b := by rw [hB]; simp [hu21, hu31, Nat.mul_assoc]
    have hK : k = m4 + 1 + m9 + 1 + o := by omega
    rw [hK]
    simpa [show m4 + 1 + m9 + 1 + o - 2 = m4 + m9 + o by omega] using hAll

/-- Exact witness for the `4,9` hard shell. -/
theorem rootQuotientPrimeFourNineCost_six_mul_four_pow
    {k : ℕ}
    (hk : 2 ≤ k) :
    rootQuotientPrimeFourNineCost (6 * 4 ^ (k - 2)) = k := by
  let n := k - 2
  have hkEq : k = n + 2 := by dsimp [n]; omega
  rw [hkEq]
  have hTwoFact : (6 * 4 ^ n).factorization 2 = 2 * n + 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      show (4 : ℕ) = 2 ^ 2 by norm_num,
      ← pow_mul]
    have hMul := Nat.factorization_mul (by positivity : 2 * 3 ≠ 0)
      (by positivity : 2 ^ (2 * n) ≠ 0)
    simp [Nat.prime_two.factorization, Nat.prime_three.factorization,
      Nat.Prime.factorization_pow, hMul]
  have hThreeFact : (6 * 4 ^ n).factorization 3 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      show (4 : ℕ) = 2 ^ 2 by norm_num,
      ← pow_mul]
    simp [Nat.factorization_mul, Nat.prime_two.factorization,
      Nat.prime_three.factorization, Nat.Prime.factorization_pow]
  have hOmega : rootQuotientPrimeFactorCount (6 * 4 ^ n) = 2 * n + 2 := by
    calc
      rootQuotientPrimeFactorCount (6 * 4 ^ n) =
          rootQuotientPrimeFactorCount 6 +
            rootQuotientPrimeFactorCount (4 ^ n) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 2 + n * 2 := by
        have hSix : rootQuotientPrimeFactorCount 6 = 2 := by norm_num [rootQuotientPrimeFactorCount]
        rw [hSix, rootQuotientPrimeFactorCount_pow (by omega)]
        have hFour : rootQuotientPrimeFactorCount 4 = 2 := by
          simpa using rootQuotientPrimeFactorCount_two_pow 2
        rw [hFour]
      _ = 2 * n + 2 := by omega
  simp [rootQuotientPrimeFourNineCost, hTwoFact, hThreeFact, hOmega]

end EnterpriseMath.Quotient
