import EnterpriseMath.Quotient.RootQuotientPrimeEightNineMetric
import Mathlib.Algebra.Order.Floor.Div
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes plus the transient budget-three pure-power code `4,8,9`.

The two 2-adic macros complete exponent block sizes `1,2,3`, while `9`
completes 3-adic block sizes `1,2`. -/
def RootQuotientPrimeFourEightNineBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({4, 8, 9} : Set ℕ)

/-- Positive-generator property. -/
theorem rootQuotientPrimeFourEightNineBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeFourEightNineBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · simp at hgMacro
    rcases hgMacro with rfl | rfl | rfl <;> omega

/-- Exact 2-direction block cost with available exponent blocks `1,2,3`. -/
def rootQuotientTwoBlockThreeCost (a : ℕ) : ℕ :=
  a ⌈/⌉ 3

/-- Exact 3-direction block cost with exponent blocks `1,2`. -/
def rootQuotientThreeBlockTwoCost (a : ℕ) : ℕ :=
  a ⌈/⌉ 2

/-- Pointwise cost predicted by the separated exponent coin systems. -/
def rootQuotientPrimeFourEightNineCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b - b.factorization 2 - b.factorization 3 +
    rootQuotientTwoBlockThreeCost (b.factorization 2) +
    rootQuotientThreeBlockTwoCost (b.factorization 3)

/-- Prime-token count of a word over primes plus `4,8,9`. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeFourEightNine
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeFourEightNineBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + w.count 4 + 2 * w.count 8 + w.count 9 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeFourEightNineBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeFourEightNineBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeFourEightNineBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeFourEightNineBasis_positive a haBasis
      rw [rootQuotientWordProduct,
        rootQuotientPrimeFactorCount_mul haPos hTailPos, ih hwTail]
      rcases haBasis with haPrime | haMacro
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have h4 : a ≠ 4 := by rintro rfl; norm_num at haPrime
        have h8 : a ≠ 8 := by rintro rfl; norm_num at haPrime
        have h9 : a ≠ 9 := by rintro rfl; norm_num at haPrime
        rw [haCount, List.count_cons, List.count_cons, List.count_cons]
        simp [h4, h8, h9]
        omega
      · simp at haMacro
        rcases haMacro with rfl | rfl | rfl
        · have hCount : rootQuotientPrimeFactorCount 4 = 2 := by
            simpa using rootQuotientPrimeFactorCount_two_pow 2
          rw [hCount, List.count_cons, List.count_cons, List.count_cons]
          simp
          omega
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

/-- Macro copies consume disjoint prime-power capacity. -/
theorem four_eight_nine_macro_powers_dvd_wordProduct
    (w : List ℕ) :
    4 ^ w.count 4 * 8 ^ w.count 8 * 9 ^ w.count 9 ∣
      rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases h4 : a = 4
      · subst a
        have hMul := Nat.mul_dvd_mul_left 4 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · by_cases h8 : a = 8
        · subst a
          have hMul := Nat.mul_dvd_mul_left 8 ih
          simpa [rootQuotientWordProduct, List.count_cons, h4, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
        · by_cases h9 : a = 9
          · subst a
            have hMul := Nat.mul_dvd_mul_left 9 ih
            simpa [rootQuotientWordProduct, List.count_cons, h4, h8, pow_succ,
              Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
          · have hDvd :
                4 ^ w.count 4 * 8 ^ w.count 8 * 9 ^ w.count 9 ∣
                  a * rootQuotientWordProduct w :=
              dvd_mul_of_dvd_right ih a
            simpa [rootQuotientWordProduct, List.count_cons, h4, h8, h9] using hDvd

/-- Lower bound: the separated block cost cannot beat any literal word. -/
theorem rootQuotientPrimeFourEightNineCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeFourEightNineBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeFourEightNineCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m4 := w.count 4
  let m8 := w.count 8
  let m9 := w.count 9
  have hCount : rootQuotientPrimeFactorCount b =
      w.length + m4 + 2 * m8 + m9 := by
    rw [hProd]
    simpa [m4, m8, m9, Nat.add_assoc] using
      rootQuotientPrimeFactorCount_wordProduct_primeFourEightNine hw
  have hMacroDvd : 4 ^ m4 * 8 ^ m8 * 9 ^ m9 ∣ b := by
    rw [hProd]
    simpa [m4, m8, m9] using four_eight_nine_macro_powers_dvd_wordProduct w
  have hTwoPowDvd : 2 ^ (2 * m4 + 3 * m8) ∣ b := by
    have hDvdMacro : 2 ^ (2 * m4 + 3 * m8) ∣ 4 ^ m4 * 8 ^ m8 * 9 ^ m9 := by
      rw [show (4 : ℕ) = 2 ^ 2 by norm_num,
        show (8 : ℕ) = 2 ^ 3 by norm_num,
        pow_mul, pow_mul, ← pow_add]
      exact dvd_mul_right _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hThreePowDvd : 3 ^ (2 * m9) ∣ b := by
    have hDvdMacro : 3 ^ (2 * m9) ∣ 4 ^ m4 * 8 ^ m8 * 9 ^ m9 := by
      rw [show (9 : ℕ) = 3 ^ 2 by norm_num, pow_mul]
      exact dvd_mul_left _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hTwoCap : 2 * m4 + 3 * m8 ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hThreeCap : 2 * m9 ≤ b.factorization 3 :=
    (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).1 hThreePowDvd
  let a := b.factorization 2
  let c := b.factorization 3
  let s2 := m4 + 2 * m8
  have hCeil2 : rootQuotientTwoBlockThreeCost a ≤ a - s2 := by
    apply (ceilDiv_le_iff_le_mul (by omega : 0 < 3)).2
    dsimp [s2, a]
    omega
  have hCeil3 : rootQuotientThreeBlockTwoCost c ≤ c - m9 := by
    apply (ceilDiv_le_iff_le_mul (by omega : 0 < 2)).2
    dsimp [c]
    omega
  dsimp [rootQuotientPrimeFourEightNineCost]
  dsimp [rootQuotientTwoBlockThreeCost,
    rootQuotientThreeBlockTwoCost] at hCeil2 hCeil3 ⊢
  omega

/-- Canonical word: use as many `8` blocks as possible; encode a two-token
2-adic remainder by one `4`; encode a one-token remainder literally; pair 3s
into `9`; leave all other primes literal. -/
def rootQuotientPrimeFourEightNineCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / 3) 8 ++
    List.replicate ((b.factorization 2 % 3) / 2) 4 ++
      List.replicate ((b.factorization 2 % 3) % 2) 2 ++
        List.replicate (b.factorization 3 / 2) 9 ++
          List.replicate (b.factorization 3 % 2) 3 ++
            b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)

/-- Canonical word length is exactly the block cost. -/
theorem rootQuotientPrimeFourEightNineCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeFourEightNineCanonicalWord b).length =
      rootQuotientPrimeFourEightNineCost b := by
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_three_add_counts b.primeFactorsList
  rw [hCount2, hCount3] at hSplit
  let r2 := b.factorization 2 % 3
  have hr2 : r2 < 3 := by dsimp [r2]; exact Nat.mod_lt _ (by omega)
  have hRemainder : r2 / 2 + r2 % 2 = if r2 = 0 then 0 else 1 := by
    rcases (show r2 = 0 ∨ r2 = 1 ∨ r2 = 2 by omega) with rfl | rfl | rfl <;> norm_num
  have hCeil2 : b.factorization 2 / 3 + r2 / 2 + r2 % 2 =
      rootQuotientTwoBlockThreeCost (b.factorization 2) := by
    have hDiv := Nat.mod_add_div' (b.factorization 2) 3
    dsimp [rootQuotientTwoBlockThreeCost, r2]
    rw [Nat.ceilDiv_eq_add_pred_div]
    omega
  have hCeil3 : b.factorization 3 / 2 + b.factorization 3 % 2 =
      rootQuotientThreeBlockTwoCost (b.factorization 3) := by
    have hDiv := Nat.mod_add_div' (b.factorization 3) 2
    dsimp [rootQuotientThreeBlockTwoCost]
    rw [Nat.ceilDiv_eq_add_pred_div]
    omega
  dsimp [rootQuotientPrimeFourEightNineCanonicalWord,
    rootQuotientPrimeFourEightNineCost, rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  dsimp [r2] at hCeil2
  omega

/-- Canonical word product is the target integer. -/
theorem rootQuotientPrimeFourEightNineCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeFourEightNineCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit :=
    pow_count_two_mul_pow_count_three_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, Nat.prod_primeFactorsList hbZero] at hSplit
  let q2 := b.factorization 2 / 3
  let r2 := b.factorization 2 % 3
  let q4 := r2 / 2
  let u2 := r2 % 2
  have hR : 2 * q4 + u2 = r2 := by
    dsimp [q4, u2]
    have := Nat.mod_add_div' r2 2
    omega
  have hA : 3 * q2 + 2 * q4 + u2 = b.factorization 2 := by
    have hDiv := Nat.mod_add_div' (b.factorization 2) 3
    dsimp [q2, r2] at hDiv
    omega
  have hC : 2 * (b.factorization 3 / 2) + b.factorization 3 % 2 =
      b.factorization 3 := by
    have hDiv := Nat.mod_add_div' (b.factorization 3) 2
    omega
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeFourEightNineCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := hSplit.symm
    _ = ((8 ^ q2 * 4 ^ q4 * 2 ^ u2) *
          (9 ^ (b.factorization 3 / 2) * 3 ^ (b.factorization 3 % 2))) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := by
      rw [show (8 : ℕ) = 2 ^ 3 by norm_num,
        show (4 : ℕ) = 2 ^ 2 by norm_num,
        show (9 : ℕ) = 3 ^ 2 by norm_num,
        pow_mul, pow_mul, pow_mul,
        ← pow_add, ← pow_add, ← pow_add]
      rw [hA, hC]
    _ = 8 ^ q2 * (4 ^ q4 * (2 ^ u2 *
        (9 ^ (b.factorization 3 / 2) *
          (3 ^ (b.factorization 3 % 2) *
            (b.primeFactorsList.filter
              (fun p : ℕ => p != 2 && p != 3)).prod)))) := by ac_rfl

/-- Canonical word stays inside bounded primes plus `4,8,9`. -/
theorem rootQuotientPrimeFourEightNineCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 3 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeFourEightNineBasis N)
      (rootQuotientPrimeFourEightNineCanonicalWord b) := by
  intro g hg
  simp only [rootQuotientPrimeFourEightNineCanonicalWord, List.mem_append,
    List.mem_replicate] at hg
  rcases hg with h8 | h4 | h2 | h9 | h3 | ho
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inl ⟨Nat.prime_two, by omega⟩
  · subst g; exact Or.inr (by simp)
  · subst g; exact Or.inl ⟨Nat.prime_three, hN⟩
  · have hgFactors : g ∈ b.primeFactorsList := (List.mem_filter.1 ho).1
    exact Or.inl ⟨Nat.prime_of_mem_primeFactorsList hgFactors,
      (Nat.le_of_mem_primeFactorsList hgFactors).trans hbN⟩

/-- Exact reachability law. -/
theorem rootQuotientPrimeFourEightNineBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 3 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin h
        (RootQuotientPrimeFourEightNineBasis N) b ↔
      rootQuotientPrimeFourEightNineCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeFourEightNineCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeFourEightNineCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeFourEightNineCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeFourEightNineCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeFourEightNineCanonicalWord_product hbPos

/-- Finite residual inequality for the marginal prefix `2,3`. -/
theorem six_mul_five_pow_transient_residual_le
    {n q4 u2 u3 : ℕ}
    (hq4 : q4 ≤ 1)
    (hu2 : u2 ≤ 1)
    (hExclusive : q4 + u2 ≤ 1)
    (hu3 : u3 ≤ 1)
    (hk : 2 ≤ n + q4 + u2 + u3) :
    6 * 5 ^ (n + q4 + u2 + u3 - 2) ≤
      4 ^ q4 * 2 ^ u2 * 3 ^ u3 * 5 ^ n := by
  have hqCases : q4 = 0 ∨ q4 = 1 := by omega
  have huCases : u2 = 0 ∨ u2 = 1 := by omega
  have hvCases : u3 = 0 ∨ u3 = 1 := by omega
  rcases hqCases with rfl | rfl <;>
    rcases huCases with rfl | rfl <;>
      rcases hvCases with rfl | rfl <;> simp_all
  all_goals
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 1 ≤ n by omega)}
    try {obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le (show 2 ≤ n by omega)}
    simp [pow_add] <;> nlinarith [show 0 < 5 ^ t by positivity]

/-- Exact transient hard shell from cost two onward. -/
theorem six_mul_five_pow_sub_two_le_of_primeFourEightNineCost
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 2 ≤ k)
    (hCost : rootQuotientPrimeFourEightNineCost b = k) :
    6 * 5 ^ (k - 2) ≤ b := by
  let q8 := b.factorization 2 / 3
  let r2 := b.factorization 2 % 3
  let q4 := r2 / 2
  let u2 := r2 % 2
  let q9 := b.factorization 3 / 2
  let u3 := b.factorization 3 % 2
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)
  let o := wo.length
  have hLenRaw := rootQuotientPrimeFourEightNineCanonicalWord_length b
  have hLen : q8 + q4 + u2 + q9 + u3 + o = k := by
    rw [hCost] at hLenRaw
    simpa [rootQuotientPrimeFourEightNineCanonicalWord, q8, r2, q4, u2,
      q9, u3, wo, o, Nat.add_assoc] using hLenRaw
  have hr2 : r2 < 3 := by dsimp [r2]; exact Nat.mod_lt _ (by omega)
  have hq4 : q4 ≤ 1 := by dsimp [q4]; omega
  have hu2 : u2 ≤ 1 := by dsimp [u2]; exact Nat.mod_le _ _
  have hExclusive : q4 + u2 ≤ 1 := by
    have hCases : r2 = 0 ∨ r2 = 1 ∨ r2 = 2 := by omega
    rcases hCases with rfl | rfl | rfl <;> norm_num [q4, u2]
  have hu3 : u3 ≤ 1 := by dsimp [u3]; exact Nat.mod_le _ _
  have hWo5 : 5 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    have hpMem := (List.mem_filter.1 hp).1
    have hpPred := (List.mem_filter.1 hp).2
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
    simp at hpPred
    omega
  have h8 : 5 ^ q8 ≤ 8 ^ q8 := Nat.pow_le_pow_left (by omega) q8
  have h9 : 5 ^ q9 ≤ 9 ^ q9 := Nat.pow_le_pow_left (by omega) q9
  have hProduct := rootQuotientPrimeFourEightNineCanonicalWord_product hbPos
  have hB : b = 8 ^ q8 * 4 ^ q4 * 2 ^ u2 * 9 ^ q9 * 3 ^ u3 * wo.prod := by
    simpa [rootQuotientPrimeFourEightNineCanonicalWord, q8, r2, q4, u2,
      q9, u3, wo, rootQuotientWordProduct_eq_prod, Nat.mul_assoc] using hProduct
  have hLower : 4 ^ q4 * 2 ^ u2 * 3 ^ u3 * 5 ^ (q8 + q9 + o) ≤ b := by
    calc
      4 ^ q4 * 2 ^ u2 * 3 ^ u3 * 5 ^ (q8 + q9 + o) =
          (5 ^ q8 * 4 ^ q4 * 2 ^ u2) *
            (5 ^ q9 * 3 ^ u3) * 5 ^ o := by
        simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      _ ≤ (8 ^ q8 * 4 ^ q4 * 2 ^ u2) *
            (9 ^ q9 * 3 ^ u3) * wo.prod := by
        exact Nat.mul_le_mul
          (Nat.mul_le_mul
            (Nat.mul_le_mul_right _ (Nat.mul_le_mul_right _ h8))
            (Nat.mul_le_mul_right _ h9)) hWo5
      _ = b := by rw [hB]; ac_rfl
  have hResidual := six_mul_five_pow_transient_residual_le
    (n := q8 + q9 + o) (q4 := q4) (u2 := u2) (u3 := u3)
    hq4 hu2 hExclusive hu3 (by omega)
  rw [show k - 2 = (q8 + q9 + o) + q4 + u2 + u3 - 2 by omega]
  exact hResidual.trans hLower

/-- Concrete hard-shell witness. -/
theorem rootQuotientPrimeFourEightNineCost_six_mul_five_pow
    {k : ℕ}
    (hk : 2 ≤ k) :
    rootQuotientPrimeFourEightNineCost (6 * 5 ^ (k - 2)) = k := by
  let n := k - 2
  have hkEq : k = n + 2 := by dsimp [n]; omega
  have hTwo : (6 * 5 ^ n).factorization 2 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have hSix : (6 : ℕ).factorization 2 = 1 := by
      rw [show (6 : ℕ) = 2 * 3 by norm_num,
        Nat.factorization_mul (by norm_num) (by norm_num)]
      simp [Nat.Prime.factorization]
    have hFive : (5 : ℕ).factorization 2 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [hSix, hFive]
  have hThree : (6 * 5 ^ n).factorization 3 = 1 := by
    rw [Nat.factorization_mul (by norm_num) (by positivity), Nat.factorization_pow]
    have hSix : (6 : ℕ).factorization 3 = 1 := by
      rw [show (6 : ℕ) = 2 * 3 by norm_num,
        Nat.factorization_mul (by norm_num) (by norm_num)]
      simp [Nat.Prime.factorization]
    have hFive : (5 : ℕ).factorization 3 = 0 :=
      Nat.factorization_eq_zero_of_not_dvd (by norm_num)
    simp [hSix, hFive]
  have hSixOmega : rootQuotientPrimeFactorCount 6 = 2 := by
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
  have hFiveOmega : rootQuotientPrimeFactorCount 5 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime (by norm_num : Nat.Prime 5)]
    simp
  have hOmega : rootQuotientPrimeFactorCount (6 * 5 ^ n) = n + 2 := by
    calc
      rootQuotientPrimeFactorCount (6 * 5 ^ n) =
          rootQuotientPrimeFactorCount 6 + rootQuotientPrimeFactorCount (5 ^ n) :=
        rootQuotientPrimeFactorCount_mul (by omega) (by positivity)
      _ = 2 + n := by
        rw [hSixOmega, rootQuotientPrimeFactorCount_pow (by omega), hFiveOmega]
        omega
      _ = n + 2 := by omega
  rw [hkEq]
  simp [rootQuotientPrimeFourEightNineCost,
    rootQuotientTwoBlockThreeCost, rootQuotientThreeBlockTwoCost,
    hTwo, hThree, hOmega]

/-- Exact transient high-root threshold. -/
theorem primeFourEightNineBasis_separates_iff_stateBound_lt_shell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 3 ≤ N)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourEightNineBasis N) ↔
      N < 6 * 5 ^ (h - 1) := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 6 * 5 ^ (h - 1) ≤ N := by omega
    let b := 6 * 5 ^ (h - 1)
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeFourEightNineBasis N)
        (by omega) rootQuotientPrimeFourEightNineBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeFourEightNineBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeFourEightNineCost b = h + 1 := by
      dsimp [b]
      simpa [show h + 1 - 2 = h - 1 by omega] using
        (rootQuotientPrimeFourEightNineCost_six_mul_five_pow
          (k := h + 1) (by omega))
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeFourEightNineBasis N)
      (by omega) rootQuotientPrimeFourEightNineBasis_positive).2
    intro b hbPos hbN _hbFree
    apply (rootQuotientPrimeFourEightNineBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hCost : h + 1 ≤ rootQuotientPrimeFourEightNineCost b := by omega
    have hCostTwo : 2 ≤ rootQuotientPrimeFourEightNineCost b := by omega
    have hShell := six_mul_five_pow_sub_two_le_of_primeFourEightNineCost
      hbPos hCostTwo rfl
    have hPowMono : 5 ^ (h - 1) ≤
        5 ^ (rootQuotientPrimeFourEightNineCost b - 2) :=
      Nat.pow_le_pow_right (by omega) (by omega)
    have hContr : 6 * 5 ^ (h - 1) ≤ N :=
      (Nat.mul_le_mul_left 6 hPowMono).trans (hShell.trans hbN)
    omega

end EnterpriseMath.Quotient
