import EnterpriseMath.Quotient.RootQuotientPrimeFourSixShell
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

/-- The prime-four-nine ISA is positive. -/
theorem rootQuotientPrimeFourNineBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeFourNineBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · simp at hgMacro
    rcases hgMacro with rfl | rfl <;> omega

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
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeFourNineBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeFourNineBasis_positive a haBasis
      rw [rootQuotientWordProduct,
        rootQuotientPrimeFactorCount_mul haPos hTailPos, ih hwTail]
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
leave every other prime factor literal. -/
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

/-- Finite residual inequality behind the `4,9` shell. -/
theorem six_mul_four_pow_residual_le
    {n u v : ℕ}
    (hu : u < 2)
    (hv : v < 2)
    (hk : 2 ≤ n + u + v) :
    6 * 4 ^ (n + u + v - 2) ≤ 2 ^ u * 3 ^ v * 4 ^ n := by
  rcases Nat.lt_two_iff.mp hu with rfl | rfl <;>
    rcases Nat.lt_two_iff.mp hv with rfl | rfl
  · have hn : 2 ≤ n := by omega
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
    simp [pow_add]
    nlinarith [show 0 < 4 ^ t by positivity]
  · have hn : 1 ≤ n := by omega
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
    simp [pow_add]
    nlinarith [show 0 < 4 ^ t by positivity]
  · have hn : 1 ≤ n := by omega
    obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hn
    simp [pow_add]
    nlinarith [show 0 < 4 ^ t by positivity]
  · simp

/-- Exact `4,9` hard-shell lower bound from cost two onward. -/
theorem six_mul_four_pow_sub_two_le_of_primeFourNineCost
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 2 ≤ k)
    (hCost : rootQuotientPrimeFourNineCost b = k) :
    6 * 4 ^ (k - 2) ≤ b := by
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
  have hWo5 : 5 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    have hpMem := (List.mem_filter.1 hp).1
    have hpPred := (List.mem_filter.1 hp).2
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
    simp at hpPred
    omega
  have hWo4 : 4 ^ o ≤ wo.prod :=
    (Nat.pow_le_pow_left (by omega) o).trans hWo5
  have hm9 : 4 ^ m9 ≤ 9 ^ m9 := Nat.pow_le_pow_left (by omega) m9
  have hProduct := rootQuotientPrimeFourNineCanonicalWord_product hbPos
  have hB : b = 4 ^ m4 * 2 ^ u2 * 9 ^ m9 * 3 ^ u3 * wo.prod := by
    simpa [rootQuotientPrimeFourNineCanonicalWord, m4, u2, m9, u3, wo,
      rootQuotientWordProduct_eq_prod, Nat.mul_assoc] using hProduct
  have hLower : 2 ^ u2 * 3 ^ u3 * 4 ^ (m4 + m9 + o) ≤ b := by
    calc
      2 ^ u2 * 3 ^ u3 * 4 ^ (m4 + m9 + o) =
          (4 ^ m4 * 2 ^ u2) * (4 ^ m9 * 3 ^ u3) * 4 ^ o := by
        simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      _ ≤ (4 ^ m4 * 2 ^ u2) * (9 ^ m9 * 3 ^ u3) * wo.prod := by
        exact Nat.mul_le_mul
          (Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ hm9)) hWo4
      _ = b := by rw [hB]; ac_rfl
  have hResidual := six_mul_four_pow_residual_le
    (n := m4 + m9 + o) (u := u2) (v := u3)
    hu2 hu3 (by omega)
  rw [show k - 2 = (m4 + m9 + o) + u2 + u3 - 2 by omega]
  exact hResidual.trans hLower

/-- Concrete factorization of the `4,9` hard-shell witness. -/
theorem rootQuotientPrimeFourNineCost_six_mul_four_pow
    {k : ℕ}
    (hk : 2 ≤ k) :
    rootQuotientPrimeFourNineCost (6 * 4 ^ (k - 2)) = k := by
  let n := k - 2
  have hkEq : k = n + 2 := by dsimp [n]; omega
  have hSixTwo : (6 : ℕ).factorization 2 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    simp [Nat.Prime.factorization]
  have hSixThree : (6 : ℕ).factorization 3 = 1 := by
    rw [show (6 : ℕ) = 2 * 3 by norm_num,
      Nat.factorization_mul (by norm_num) (by norm_num)]
    simp [Nat.Prime.factorization]
  have hFourTwo : (4 : ℕ).factorization 2 = 2 := by
    simpa [show (4 : ℕ) = 2 ^ 2 by norm_num] using
      (Nat.factorization_pow_self (n := 2) Nat.prime_two)
  have hFourThree : (4 : ℕ).factorization 3 = 0 := by
    exact Nat.factorization_eq_zero_of_not_dvd (by norm_num)
  have hTwoFact : (6 * 4 ^ n).factorization 2 = 2 * n + 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    simp [hSixTwo, hFourTwo]
    omega
  have hThreeFact : (6 * 4 ^ n).factorization 3 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    simp [hSixThree, hFourThree]
  have hSixOmega : rootQuotientPrimeFactorCount 6 = 2 := by
    have hTwo : rootQuotientPrimeFactorCount 2 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_two]
      simp
    have hThree : rootQuotientPrimeFactorCount 3 = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime Nat.prime_three]
      simp
    calc
      rootQuotientPrimeFactorCount 6 =
          rootQuotientPrimeFactorCount (2 * 3) := by norm_num
      _ = rootQuotientPrimeFactorCount 2 + rootQuotientPrimeFactorCount 3 :=
        rootQuotientPrimeFactorCount_mul (by omega) (by omega)
      _ = 2 := by rw [hTwo, hThree]
  have hFourOmega : rootQuotientPrimeFactorCount 4 = 2 := by
    simpa using rootQuotientPrimeFactorCount_two_pow 2
  have hOmega : rootQuotientPrimeFactorCount (6 * 4 ^ n) = 2 * n + 2 := by
    calc
      rootQuotientPrimeFactorCount (6 * 4 ^ n) =
          rootQuotientPrimeFactorCount 6 +
            rootQuotientPrimeFactorCount (4 ^ n) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 2 + n * 2 := by
        rw [hSixOmega, rootQuotientPrimeFactorCount_pow (by omega), hFourOmega]
      _ = 2 * n + 2 := by omega
  rw [hkEq]
  simp [rootQuotientPrimeFourNineCost, hTwoFact, hThreeFact, hOmega]

/-- Exact high-root threshold for the `4,9` ISA. -/
theorem primeFourNineBasis_separates_iff_stateBound_lt_shell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 3 ≤ N)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourNineBasis N) ↔
      N < 6 * 4 ^ (h - 1) := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 6 * 4 ^ (h - 1) ≤ N := by omega
    let b := 6 * 4 ^ (h - 1)
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeFourNineBasis N)
        (by omega) rootQuotientPrimeFourNineBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeFourNineBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeFourNineCost b = h + 1 := by
      dsimp [b]
      simpa [show h + 1 - 2 = h - 1 by omega] using
        (rootQuotientPrimeFourNineCost_six_mul_four_pow (k := h + 1) (by omega))
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeFourNineBasis N)
      (by omega) rootQuotientPrimeFourNineBasis_positive).2
    intro b hbPos hbN _hbFree
    apply (rootQuotientPrimeFourNineBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hCost : h + 1 ≤ rootQuotientPrimeFourNineCost b := by omega
    have hCostTwo : 2 ≤ rootQuotientPrimeFourNineCost b := by omega
    have hShell := six_mul_four_pow_sub_two_le_of_primeFourNineCost
      hbPos hCostTwo rfl
    have hPowMono : 4 ^ (h - 1) ≤
        4 ^ (rootQuotientPrimeFourNineCost b - 2) :=
      Nat.pow_le_pow_right (by omega) (by omega)
    have hContr : 6 * 4 ^ (h - 1) ≤ N :=
      (Nat.mul_le_mul_left 6 hPowMono).trans (hShell.trans hbN)
    omega

end EnterpriseMath.Quotient
