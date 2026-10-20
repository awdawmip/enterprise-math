import EnterpriseMath.Quotient.RootQuotientPrimeFourSixMetric
import Mathlib.Data.Nat.Prime.Pow
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A list whose entries are all at least `q` has product at least `q^length`. -/
theorem pow_length_le_list_prod_of_ge
    {q : ℕ} {l : List ℕ}
    (hGe : ∀ a : ℕ, a ∈ l → q ≤ a) :
    q ^ l.length ≤ l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      have ha : q ≤ a := hGe a (by simp)
      have hTail : ∀ b : ℕ, b ∈ l → q ≤ b := by
        intro b hb
        exact hGe b (by simp [hb])
      have hInd := ih hTail
      simp only [List.length_cons, List.prod_cons, pow_succ]
      exact Nat.mul_le_mul hInd ha

/-- For `k>=3`, the possible leftover literal `2` is still too expensive to
beat a pure `3^k` shell: `3^k <= 2*4^(k-1)`. -/
theorem three_pow_le_two_mul_four_pow_sub_one
    {k : ℕ}
    (hk : 3 ≤ k) :
    3 ^ k ≤ 2 * 4 ^ (k - 1) := by
  obtain ⟨n, hkEq⟩ := Nat.exists_eq_add_of_le hk
  subst k
  have hPow : 3 ^ n ≤ 4 ^ n :=
    Nat.pow_le_pow_left (by omega) n
  rw [show 3 + n - 1 = n + 2 by omega]
  rw [show 3 + n = 3 + n by rfl, pow_add, pow_add]
  norm_num
  exact Nat.mul_le_mul (by norm_num : 27 ≤ 32) hPow

/-- The prime-factor-list residual after removing `2` and `3` contains only
instructions at least three. -/
theorem three_le_of_mem_primeFactors_filter_ne_two_three
    {b p : ℕ}
    (hp : p ∈ b.primeFactorsList.filter
      (fun q : ℕ => q != 2 && q != 3)) :
    3 ≤ p := by
  have hpMem := (List.mem_filter.1 hp).1
  have hpPred := (List.mem_filter.1 hp).2
  have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
  have hpNeTwo : p ≠ 2 := by
    simpa using (Bool.and_eq_true.mp hpPred).1
  omega

/-- The same residual entries are in fact at least four, which is useful when
the canonical word also contains the unique leftover literal `2`. -/
theorem four_le_of_mem_primeFactors_filter_ne_two_three
    {b p : ℕ}
    (hp : p ∈ b.primeFactorsList.filter
      (fun q : ℕ => q != 2 && q != 3)) :
    4 ≤ p := by
  have hpMem := (List.mem_filter.1 hp).1
  have hpPred := (List.mem_filter.1 hp).2
  have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpMem
  have hpAnd := Bool.and_eq_true.mp hpPred
  have hpNeTwo : p ≠ 2 := by simpa using hpAnd.1
  have hpNeThree : p ≠ 3 := by simpa using hpAnd.2
  omega

/-- A canonical leftover literal `2` forces the leftover literal `3` count to
be zero: if `2+3` were both still present they would have been paired into a
macro `6`. -/
theorem canonicalThreeRemainder_eq_zero_of_twoRemainder_eq_one
    {b : ℕ}
    (hTwoRem : rootQuotientPrimeFourSixCanonicalTwoRemainder b = 1) :
    rootQuotientPrimeFourSixCanonicalThreeRemainder b = 0 := by
  let a := b.factorization 2
  let c := b.factorization 3
  by_cases hac : a ≤ c
  · have hMin : rootQuotientPrimeFourSixCanonicalSixCount b = a := by
      simp [rootQuotientPrimeFourSixCanonicalSixCount, a, c, min_eq_left hac]
    have hZero : rootQuotientPrimeFourSixCanonicalTwoRemainder b = 0 := by
      simp [rootQuotientPrimeFourSixCanonicalTwoRemainder, hMin, a]
    omega
  · have hca : c ≤ a := by omega
    simp [rootQuotientPrimeFourSixCanonicalThreeRemainder,
      rootQuotientPrimeFourSixCanonicalSixCount, a, c,
      min_eq_right hca]

/-- Every positive integer of prime-four-six cost at least three lies above the
pure triadic shell `3^cost`.

The canonical shortest word has two cases:

* no leftover literal `2`: every instruction has value at least `3`;
* one leftover literal `2`: no literal `3` remains, and every other instruction
  has value at least `4`, giving `2*4^(k-1) >= 3^k` for `k>=3`. -/
theorem three_pow_primeFourSixCost_le
    {b : ℕ}
    (hbPos : 1 ≤ b)
    (hCost : 3 ≤ rootQuotientPrimeFourSixCost b) :
    3 ^ rootQuotientPrimeFourSixCost b ≤ b := by
  let x := rootQuotientPrimeFourSixCanonicalFourCount b
  let y := rootQuotientPrimeFourSixCanonicalSixCount b
  let u := rootQuotientPrimeFourSixCanonicalTwoRemainder b
  let t := rootQuotientPrimeFourSixCanonicalThreeRemainder b
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2 && p != 3)
  let o := wo.length
  have hLenRaw := rootQuotientPrimeFourSixCanonicalWord_length b
  have hLen : x + y + u + t + o = rootQuotientPrimeFourSixCost b := by
    simpa [rootQuotientPrimeFourSixCanonicalWord,
      x, y, u, t, wo, o, Nat.add_assoc] using hLenRaw
  have hbZero : b ≠ 0 := by omega
  have hCount2 : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hCount3 : b.primeFactorsList.count 3 = b.factorization 3 :=
    Nat.primeFactorsList_count_eq
  have hSplit :=
    pow_count_two_mul_pow_count_three_mul_filter_prod b.primeFactorsList
  rw [hCount2, hCount3, Nat.prod_primeFactorsList hbZero] at hSplit
  have hPrimary := canonical_four_six_two_three_product b
  have hB : b = 4 ^ x * 6 ^ y * 2 ^ u * 3 ^ t * wo.prod := by
    calc
      b = (2 ^ b.factorization 2 * 3 ^ b.factorization 3) * wo.prod := by
        simpa [wo] using hSplit.symm
      _ = (4 ^ x * 6 ^ y * 2 ^ u * 3 ^ t) * wo.prod := by
        rw [← hPrimary]
        rfl
  have hWo3 : 3 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    exact three_le_of_mem_primeFactors_filter_ne_two_three hp
  have hWo4 : 4 ^ o ≤ wo.prod := by
    apply pow_length_le_list_prod_of_ge
    intro p hp
    exact four_le_of_mem_primeFactors_filter_ne_two_three hp
  have huLt : u < 2 := by
    dsimp [u, rootQuotientPrimeFourSixCanonicalTwoRemainder]
    exact Nat.mod_lt _ (by omega)
  rcases Nat.lt_two_iff.mp huLt with huZero | huOne
  · have hx : 3 ^ x ≤ 4 ^ x := Nat.pow_le_pow_left (by omega) x
    have hy : 3 ^ y ≤ 6 ^ y := Nat.pow_le_pow_left (by omega) y
    have hxy : 3 ^ x * 3 ^ y ≤ 4 ^ x * 6 ^ y :=
      Nat.mul_le_mul hx hy
    have hxyt : (3 ^ x * 3 ^ y) * 3 ^ t ≤
        (4 ^ x * 6 ^ y) * 3 ^ t :=
      Nat.mul_le_mul_right (3 ^ t) hxy
    have hAll : ((3 ^ x * 3 ^ y) * 3 ^ t) * 3 ^ o ≤
        ((4 ^ x * 6 ^ y) * 3 ^ t) * wo.prod :=
      Nat.mul_le_mul hxyt hWo3
    have hPow : 3 ^ (x + y + t + o) ≤ b := by
      calc
        3 ^ (x + y + t + o) =
            ((3 ^ x * 3 ^ y) * 3 ^ t) * 3 ^ o := by
          simp [pow_add, Nat.mul_assoc]
        _ ≤ ((4 ^ x * 6 ^ y) * 3 ^ t) * wo.prod := hAll
        _ = b := by
          rw [hB]
          simp [huZero, Nat.mul_assoc]
    have hCostEq : rootQuotientPrimeFourSixCost b = x + y + t + o := by
      omega
    rw [hCostEq]
    exact hPow
  · have hTwoRem : u = 1 := huOne
    have hThreeRem : t = 0 := by
      dsimp [t]
      exact canonicalThreeRemainder_eq_zero_of_twoRemainder_eq_one
        (b := b) (by simpa [u] using hTwoRem)
    have hy : 4 ^ y ≤ 6 ^ y := Nat.pow_le_pow_left (by omega) y
    have hxy : 4 ^ x * 4 ^ y ≤ 4 ^ x * 6 ^ y :=
      Nat.mul_le_mul_left (4 ^ x) hy
    have hxyTwo : (4 ^ x * 4 ^ y) * 2 ≤
        (4 ^ x * 6 ^ y) * 2 :=
      Nat.mul_le_mul_right 2 hxy
    have hAll : ((4 ^ x * 4 ^ y) * 2) * 4 ^ o ≤
        ((4 ^ x * 6 ^ y) * 2) * wo.prod :=
      Nat.mul_le_mul hxyTwo hWo4
    have hLower : 2 * 4 ^ (x + y + o) ≤ b := by
      calc
        2 * 4 ^ (x + y + o) =
            ((4 ^ x * 4 ^ y) * 2) * 4 ^ o := by
          simp [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        _ ≤ ((4 ^ x * 6 ^ y) * 2) * wo.prod := hAll
        _ = b := by
          rw [hB]
          simp [hTwoRem, hThreeRem, Nat.mul_assoc]
    have hCostEq : rootQuotientPrimeFourSixCost b = x + y + 1 + o := by
      omega
    have hNumeric := three_pow_le_two_mul_four_pow_sub_one hCost
    have hPredEq : rootQuotientPrimeFourSixCost b - 1 = x + y + o := by
      omega
    rw [hPredEq] at hNumeric
    exact hNumeric.trans hLower

/-- Pure powers of three have prime-four-six cost exactly their exponent. -/
theorem rootQuotientPrimeFourSixCost_three_pow
    (k : ℕ) :
    rootQuotientPrimeFourSixCost (3 ^ k) = k := by
  have hTwoNotDvd : ¬2 ∣ 3 ^ k := by
    intro hDvd
    have hDvdThree : 2 ∣ 3 := Nat.prime_two.dvd_of_dvd_pow hDvd
    norm_num at hDvdThree
  have hFactTwo : (3 ^ k).factorization 2 = 0 :=
    Nat.factorization_eq_zero_of_not_dvd hTwoNotDvd
  have hFactThree : (3 ^ k).factorization 3 = k :=
    Nat.factorization_pow_self Nat.prime_three
  have hThreeCount : rootQuotientPrimeFactorCount 3 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_three]
    simp
  have hOmega : rootQuotientPrimeFactorCount (3 ^ k) = k := by
    rw [rootQuotientPrimeFactorCount_pow Nat.prime_three.one_le, hThreeCount]
    simp
  simp [rootQuotientPrimeFourSixCost,
    rootQuotientPrimeFourSixSaving, hFactTwo, hFactThree, hOmega]

/-- Exact prime-four-six hard shell from cost three onward. -/
theorem primeFourSixCost_eq_k_iff_three_pow_le_of_three_le
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 3 ≤ k)
    (hCost : rootQuotientPrimeFourSixCost b = k) :
    3 ^ k ≤ b := by
  rw [← hCost]
  exact three_pow_primeFourSixCost_le hbPos (by simpa [hCost] using hk)

end EnterpriseMath.Quotient
