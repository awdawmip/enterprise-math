import EnterpriseMath.Quotient.RootQuotientPrimeFourMetric
import EnterpriseMath.Quotient.RootQuotientFactorGeometryAlgebra
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with macro instructions `4=2^2` and `6=2*3`. -/
def RootQuotientPrimeFourSixBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({4, 6} : Set ℕ)

/-- The prime-four-six ISA is positive. -/
theorem rootQuotientPrimeFourSixBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeFourSixBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · simp at hgMacro
    rcases hgMacro with rfl | rfl <;> omega

/-- Prime-token count of a prime-four-six word product.

Both macros carry two prime tokens, so each macro occurrence contributes one
extra token beyond literal word length. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeFourSix
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + w.count 4 + w.count 6 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeFourSixBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeFourSixBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeFourSixBasis_positive a haBasis
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
        have haNeSix : a ≠ 6 := by
          intro hEq
          subst a
          norm_num at haPrime
        rw [haCount, List.count_cons, List.count_cons]
        simp [haNeFour, haNeSix]
        omega
      · simp at haMacro
        rcases haMacro with haFour | haSix
        · subst a
          have hFourCount : rootQuotientPrimeFactorCount 4 = 2 := by
            simpa using rootQuotientPrimeFactorCount_two_pow 2
          rw [hFourCount, List.count_cons, List.count_cons]
          simp
          omega
        · subst a
          have hTwoCount : rootQuotientPrimeFactorCount 2 = 1 := by
            rw [rootQuotientPrimeFactorCount,
              Nat.primeFactorsList_prime Nat.prime_two]
            simp
          have hThreeCount : rootQuotientPrimeFactorCount 3 = 1 := by
            rw [rootQuotientPrimeFactorCount,
              Nat.primeFactorsList_prime Nat.prime_three]
            simp
          have hSixCount : rootQuotientPrimeFactorCount 6 = 2 := by
            calc
              rootQuotientPrimeFactorCount 6 =
                  rootQuotientPrimeFactorCount (2 * 3) := by norm_num
              _ = rootQuotientPrimeFactorCount 2 +
                  rootQuotientPrimeFactorCount 3 :=
                rootQuotientPrimeFactorCount_mul (by omega) (by omega)
              _ = 2 := by rw [hTwoCount, hThreeCount]
          rw [hSixCount, List.count_cons, List.count_cons]
          simp
          omega

/-- All macro occurrences contribute their disjoint word positions to the
compiled product. -/
theorem four_pow_count_mul_six_pow_count_dvd_wordProduct
    (w : List ℕ) :
    4 ^ w.count 4 * 6 ^ w.count 6 ∣ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases haFour : a = 4
      · subst a
        have hMul := Nat.mul_dvd_mul_left 4 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · by_cases haSix : a = 6
        · subst a
          have hMul := Nat.mul_dvd_mul_left 6 ih
          simpa [rootQuotientWordProduct, List.count_cons, haFour, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
        · have hDvd :
              4 ^ w.count 4 * 6 ^ w.count 6 ∣
                a * rootQuotientWordProduct w :=
            dvd_mul_of_dvd_right ih a
          simpa [rootQuotientWordProduct, List.count_cons, haFour, haSix] using hDvd

/-- Maximum one-step saving obtainable from the two semiprime macros `4` and
`6`, expressed only through the `2`- and `3`-adic exponents. -/
def rootQuotientPrimeFourSixSaving (b : ℕ) : ℕ :=
  min (b.factorization 2)
    ((b.factorization 2 + b.factorization 3) / 2)

/-- Exact weighted cost induced by bounded primes plus macros `4` and `6`. -/
def rootQuotientPrimeFourSixCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b - rootQuotientPrimeFourSixSaving b

/-- Algebraic identity for the macro product's prime powers. -/
theorem four_pow_mul_six_pow_eq_two_three_powers
    (a b : ℕ) :
    4 ^ a * 6 ^ b = 2 ^ (2 * a + b) * 3 ^ b := by
  calc
    4 ^ a * 6 ^ b = (2 ^ 2) ^ a * (2 * 3) ^ b := by norm_num
    _ = 2 ^ (2 * a) * (2 ^ b * 3 ^ b) := by
      rw [pow_mul, mul_pow]
    _ = (2 ^ (2 * a) * 2 ^ b) * 3 ^ b := by ac_rfl
    _ = 2 ^ (2 * a + b) * 3 ^ b := by rw [← pow_add]

/-- Universal lower bound: no prime-four-six word can beat the pairing cost. -/
theorem rootQuotientPrimeFourSixCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeFourSixCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m4 := w.count 4
  let m6 := w.count 6
  have hCount : rootQuotientPrimeFactorCount b = w.length + m4 + m6 := by
    rw [hProd]
    simpa [m4, m6, Nat.add_assoc] using
      rootQuotientPrimeFactorCount_wordProduct_primeFourSix hw
  have hMacroDvd : 4 ^ m4 * 6 ^ m6 ∣ b := by
    rw [hProd]
    simpa [m4, m6] using
      four_pow_count_mul_six_pow_count_dvd_wordProduct w
  have hMacroEq : 4 ^ m4 * 6 ^ m6 =
      2 ^ (2 * m4 + m6) * 3 ^ m6 :=
    four_pow_mul_six_pow_eq_two_three_powers m4 m6
  have hTwoPowDvd : 2 ^ (2 * m4 + m6) ∣ b := by
    have hDvdMacro : 2 ^ (2 * m4 + m6) ∣ 4 ^ m4 * 6 ^ m6 := by
      rw [hMacroEq]
      exact dvd_mul_right _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hThreePowDvd : 3 ^ m6 ∣ b := by
    have hDvdMacro : 3 ^ m6 ∣ 4 ^ m4 * 6 ^ m6 := by
      rw [hMacroEq]
      exact dvd_mul_left _ _
    exact dvd_trans hDvdMacro hMacroDvd
  have hTwoCap : 2 * m4 + m6 ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hThreeCap : m6 ≤ b.factorization 3 :=
    (Nat.prime_three.pow_dvd_iff_le_factorization hbZero).1 hThreePowDvd
  have hSaveLeTwo : m4 + m6 ≤ b.factorization 2 := by omega
  have hSaveLePair : m4 + m6 ≤
      (b.factorization 2 + b.factorization 3) / 2 := by
    omega
  have hSaveLe : m4 + m6 ≤ rootQuotientPrimeFourSixSaving b := by
    exact le_min hSaveLeTwo hSaveLePair
  dsimp [rootQuotientPrimeFourSixCost]
  omega

/-- Number of `6` macros in the canonical pairing word. -/
def rootQuotientPrimeFourSixCanonicalSixCount (b : ℕ) : ℕ :=
  min (b.factorization 2) (b.factorization 3)

/-- Number of `4` macros after all possible `2+3` pairs are consumed. -/
def rootQuotientPrimeFourSixCanonicalFourCount (b : ℕ) : ℕ :=
  (b.factorization 2 - rootQuotientPrimeFourSixCanonicalSixCount b) / 2

/-- Remaining literal `2` count after canonical pairing. -/
def rootQuotientPrimeFourSixCanonicalTwoRemainder (b : ℕ) : ℕ :=
  (b.factorization 2 - rootQuotientPrimeFourSixCanonicalSixCount b) % 2

/-- Remaining literal `3` count after canonical `6` pairings. -/
def rootQuotientPrimeFourSixCanonicalThreeRemainder (b : ℕ) : ℕ :=
  b.factorization 3 - rootQuotientPrimeFourSixCanonicalSixCount b

/-- Canonical pairing uses exactly the maximum saving. -/
theorem canonicalFourCount_add_sixCount_eq_saving
    (b : ℕ) :
    rootQuotientPrimeFourSixCanonicalFourCount b +
      rootQuotientPrimeFourSixCanonicalSixCount b =
        rootQuotientPrimeFourSixSaving b := by
  let a := b.factorization 2
  let c := b.factorization 3
  by_cases hac : a ≤ c
  · have hMin : min a c = a := min_eq_left hac
    have hPair : a ≤ (a + c) / 2 := by omega
    simp [rootQuotientPrimeFourSixCanonicalFourCount,
      rootQuotientPrimeFourSixCanonicalSixCount,
      rootQuotientPrimeFourSixSaving, a, c, hMin,
      min_eq_left hPair]
  · have hca : c < a := by omega
    have hMin : min a c = c := min_eq_right hca.le
    have hPairLe : (a + c) / 2 ≤ a := by omega
    simp [rootQuotientPrimeFourSixCanonicalFourCount,
      rootQuotientPrimeFourSixCanonicalSixCount,
      rootQuotientPrimeFourSixSaving, a, c, hMin,
      min_eq_right hPairLe]
    omega

/-- Removing all literal factors `2` and `3` partitions prime-factor-list
length into the residual length plus the two valuations. -/
theorem length_filter_ne_two_three_add_counts
    (l : List ℕ) :
    (l.filter (fun n : ℕ => n != 2 && n != 3)).length +
        l.count 2 + l.count 3 = l.length := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases haTwo : a = 2
      · subst a
        simp [List.count_cons, ih]
      · by_cases haThree : a = 3
        · subst a
          simp [List.count_cons, ih]
        · simp [List.count_cons, haTwo, haThree, ih]
          omega

/-- Multiplicative counterpart of the same two-prime filter partition. -/
theorem pow_count_two_mul_pow_count_three_mul_filter_prod
    (l : List ℕ) :
    2 ^ l.count 2 * 3 ^ l.count 3 *
        (l.filter (fun n : ℕ => n != 2 && n != 3)).prod = l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases haTwo : a = 2
      · subst a
        simp [List.count_cons, ih, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      · by_cases haThree : a = 3
        · subst a
          simp [List.count_cons, ih, pow_succ,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        · simp [List.count_cons, haTwo, haThree, ih,
            Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Canonical pairing reconstructs the complete `2`- and `3`-primary part. -/
theorem canonical_four_six_two_three_product
    (b : ℕ) :
    4 ^ rootQuotientPrimeFourSixCanonicalFourCount b *
        6 ^ rootQuotientPrimeFourSixCanonicalSixCount b *
        2 ^ rootQuotientPrimeFourSixCanonicalTwoRemainder b *
        3 ^ rootQuotientPrimeFourSixCanonicalThreeRemainder b =
      2 ^ b.factorization 2 * 3 ^ b.factorization 3 := by
  let a := b.factorization 2
  let c := b.factorization 3
  let y := min a c
  let d := a - y
  let x := d / 2
  let u := d % 2
  let t := c - y
  have hMod : u + x * 2 = d := by
    dsimp [u, x]
    exact Nat.mod_add_div' d 2
  have hA : 2 * x + y + u = a := by
    have hyA : y ≤ a := min_le_left _ _
    dsimp [d] at hMod
    omega
  have hC : y + t = c := by
    have hyC : y ≤ c := min_le_right _ _
    dsimp [t]
    omega
  have hMacro : 4 ^ x * 6 ^ y =
      2 ^ (2 * x + y) * 3 ^ y :=
    four_pow_mul_six_pow_eq_two_three_powers x y
  change 4 ^ x * 6 ^ y * 2 ^ u * 3 ^ t = 2 ^ a * 3 ^ c
  calc
    4 ^ x * 6 ^ y * 2 ^ u * 3 ^ t =
        (2 ^ (2 * x + y) * 3 ^ y) * 2 ^ u * 3 ^ t := by rw [hMacro]
    _ = (2 ^ (2 * x + y) * 2 ^ u) * (3 ^ y * 3 ^ t) := by ac_rfl
    _ = 2 ^ (2 * x + y + u) * 3 ^ (y + t) := by
      rw [← pow_add, ← pow_add]
    _ = 2 ^ a * 3 ^ c := by rw [hA, hC]

/-- Canonical shortest candidate for the prime-four-six ISA. -/
def rootQuotientPrimeFourSixCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (rootQuotientPrimeFourSixCanonicalFourCount b) 4 ++
    List.replicate (rootQuotientPrimeFourSixCanonicalSixCount b) 6 ++
      List.replicate (rootQuotientPrimeFourSixCanonicalTwoRemainder b) 2 ++
        List.replicate (rootQuotientPrimeFourSixCanonicalThreeRemainder b) 3 ++
          b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)

/-- Exact length of the canonical prime-four-six word. -/
theorem rootQuotientPrimeFourSixCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeFourSixCanonicalWord b).length =
      rootQuotientPrimeFourSixCost b := by
  let a := b.factorization 2
  let c := b.factorization 3
  let y := rootQuotientPrimeFourSixCanonicalSixCount b
  let x := rootQuotientPrimeFourSixCanonicalFourCount b
  let u := rootQuotientPrimeFourSixCanonicalTwoRemainder b
  let t := rootQuotientPrimeFourSixCanonicalThreeRemainder b
  let o := (b.primeFactorsList.filter
    (fun p : ℕ => p != 2 && p != 3)).length
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_three_add_counts b.primeFactorsList
  rw [hCount2, hCount3] at hSplit
  have hMod : u + x * 2 = a - y := by
    dsimp [u, x, rootQuotientPrimeFourSixCanonicalTwoRemainder,
      rootQuotientPrimeFourSixCanonicalFourCount]
    exact Nat.mod_add_div' (b.factorization 2 -
      rootQuotientPrimeFourSixCanonicalSixCount b) 2
  have hA : 2 * x + y + u = a := by
    have hyA : y ≤ a := by
      dsimp [y, rootQuotientPrimeFourSixCanonicalSixCount, a, c]
      exact min_le_left _ _
    omega
  have hC : y + t = c := by
    dsimp [t, rootQuotientPrimeFourSixCanonicalThreeRemainder]
    have hyC : y ≤ c := by
      dsimp [y, rootQuotientPrimeFourSixCanonicalSixCount, a, c]
      exact min_le_right _ _
    omega
  have hSave : x + y = rootQuotientPrimeFourSixSaving b := by
    dsimp [x, y]
    exact canonicalFourCount_add_sixCount_eq_saving b
  dsimp [rootQuotientPrimeFourSixCanonicalWord,
    rootQuotientPrimeFourSixCost, rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  dsimp [o] at hSplit
  omega

/-- Product of the canonical prime-four-six word is the original positive
integer. -/
theorem rootQuotientPrimeFourSixCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeFourSixCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit :=
    pow_count_two_mul_pow_count_three_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, Nat.prod_primeFactorsList hbZero] at hSplit
  have hPrimary := canonical_four_six_two_three_product b
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeFourSixCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := hSplit.symm
    _ = (4 ^ rootQuotientPrimeFourSixCanonicalFourCount b *
          6 ^ rootQuotientPrimeFourSixCanonicalSixCount b *
          2 ^ rootQuotientPrimeFourSixCanonicalTwoRemainder b *
          3 ^ rootQuotientPrimeFourSixCanonicalThreeRemainder b) *
        (b.primeFactorsList.filter
          (fun p : ℕ => p != 2 && p != 3)).prod := by rw [hPrimary]
    _ = 4 ^ rootQuotientPrimeFourSixCanonicalFourCount b *
        (6 ^ rootQuotientPrimeFourSixCanonicalSixCount b *
          (2 ^ rootQuotientPrimeFourSixCanonicalTwoRemainder b *
            (3 ^ rootQuotientPrimeFourSixCanonicalThreeRemainder b *
              (b.primeFactorsList.filter
                (fun p : ℕ => p != 2 && p != 3)).prod))) := by
      ac_rfl

/-- The canonical word stays inside bounded primes plus macros `4,6`. -/
theorem rootQuotientPrimeFourSixCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 3 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeFourSixBasis N)
      (rootQuotientPrimeFourSixCanonicalWord b) := by
  let w4 := List.replicate (rootQuotientPrimeFourSixCanonicalFourCount b) 4
  let w6 := List.replicate (rootQuotientPrimeFourSixCanonicalSixCount b) 6
  let w2 := List.replicate (rootQuotientPrimeFourSixCanonicalTwoRemainder b) 2
  let w3 := List.replicate (rootQuotientPrimeFourSixCanonicalThreeRemainder b) 3
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)
  have hw4 : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w4 := by
    intro g hg
    have hEq : g = 4 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inr (by simp)
  have hw6 : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w6 := by
    intro g hg
    have hEq : g = 6 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inr (by simp)
  have hw2 : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w2 := by
    intro g hg
    have hEq : g = 2 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inl ⟨Nat.prime_two, by omega⟩
  have hw3 : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) w3 := by
    intro g hg
    have hEq : g = 3 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inl ⟨Nat.prime_three, hN⟩
  have hwo : RootQuotientWordOver (RootQuotientPrimeFourSixBasis N) wo := by
    intro p hp
    have hpFactors : p ∈ b.primeFactorsList :=
      (List.mem_filter.1 hp).1
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpFactors
    have hpLeB : p ≤ b := Nat.le_of_mem_primeFactorsList hpFactors
    exact Or.inl ⟨hpPrime, hpLeB.trans hbN⟩
  simpa [rootQuotientPrimeFourSixCanonicalWord, w4, w6, w2, w3, wo] using
    rootQuotientWordOver_append hw4
      (rootQuotientWordOver_append hw6
        (rootQuotientWordOver_append hw2
          (rootQuotientWordOver_append hw3 hwo)))

/-- Exact pointwise reachability law for bounded primes plus macros `4` and `6`. -/
theorem rootQuotientPrimeFourSixBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 3 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin
        h (RootQuotientPrimeFourSixBasis N) b ↔
      rootQuotientPrimeFourSixCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeFourSixCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeFourSixCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeFourSixCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeFourSixCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeFourSixCanonicalWord_product hbPos

end EnterpriseMath.Quotient
