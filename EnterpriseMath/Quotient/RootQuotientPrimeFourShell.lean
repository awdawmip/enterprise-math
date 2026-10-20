import EnterpriseMath.Quotient.RootQuotientBinaryPenultimate
import EnterpriseMath.Quotient.RootQuotientPrimeFourMetric
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every non-two prime factor is at least three. -/
theorem three_le_of_mem_primeFactorsList_filter_ne_two
    {b p : ℕ}
    (hp : p ∈ b.primeFactorsList.filter (fun q : ℕ => q != 2)) :
    3 ≤ p := by
  have hpFactors : p ∈ b.primeFactorsList := (List.mem_filter.1 hp).1
  have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpFactors
  have hpNeTwo : p ≠ 2 := by
    have hBool := (List.mem_filter.1 hp).2
    simpa using hBool
  have hpTwo := hpPrime.two_le
  omega

/-- Exact weighted-shell lower bound.

Any positive integer whose prime-plus-four cost is `k>=1` is at least
`2*3^(k-1)`.  The canonical shortest word makes the economics transparent:
paired twos appear as `4` (cost one, value four), at most one unpaired `2`
(cost one, value two), and every remaining prime instruction is at least `3`.
Hence at most one cost unit can have value below three. -/
theorem two_mul_three_pow_pred_le_of_primeFourCost_eq
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 1 ≤ k)
    (hCost : rootQuotientPrimeFourCost b = k) :
    2 * 3 ^ (k - 1) ≤ b := by
  let e := b.factorization 2
  let q := e / 2
  let s := e % 2
  let odd := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  have hsLt : s < 2 := by
    dsimp [s]
    exact Nat.mod_lt e (by omega)
  have hLen : q + s + odd.length = k := by
    have hCanonical := rootQuotientPrimeFourCanonicalWord_length b
    rw [hCost] at hCanonical
    simpa [rootQuotientPrimeFourCanonicalWord, q, s, odd,
      List.length_append] using hCanonical
  have hProd : b = 4 ^ q * (2 ^ s * odd.prod) := by
    have hCanonical := rootQuotientPrimeFourCanonicalWord_product hbPos
    rw [rootQuotientWordProduct_eq_prod] at hCanonical
    simpa [rootQuotientPrimeFourCanonicalWord, q, s, odd,
      List.prod_append, Nat.mul_assoc] using hCanonical
  have hOddLower : 3 ^ odd.length ≤ odd.prod := by
    apply pow_three_length_le_list_prod
    intro p hp
    exact three_le_of_mem_primeFactorsList_filter_ne_two hp
  have hFourLower : 3 ^ q ≤ 4 ^ q :=
    Nat.pow_le_pow_left (by omega) q
  have hCombined : 3 ^ q * 3 ^ odd.length ≤ 4 ^ q * odd.prod :=
    Nat.mul_le_mul hFourLower hOddLower
  by_cases hsZero : s = 0
  · have hQOdd : q + odd.length = k := by omega
    have hTargetLeThree : 2 * 3 ^ (k - 1) ≤ 3 ^ k := by
      calc
        2 * 3 ^ (k - 1) ≤ 3 * 3 ^ (k - 1) :=
          Nat.mul_le_mul_right (3 ^ (k - 1)) (by omega)
        _ = 3 ^ k := by
          rw [← pow_succ']
          congr 1
          omega
    have hThreeKLe : 3 ^ k ≤ 4 ^ q * odd.prod := by
      calc
        3 ^ k = 3 ^ q * 3 ^ odd.length := by
          rw [← pow_add]
          congr 1
          exact hQOdd.symm
        _ ≤ 4 ^ q * odd.prod := hCombined
    have hProdZero : b = 4 ^ q * odd.prod := by
      simpa [hsZero] using hProd
    rw [hProdZero]
    exact hTargetLeThree.trans hThreeKLe
  · have hsOne : s = 1 := by omega
    have hQOdd : q + odd.length = k - 1 := by omega
    have hTwoCombined :
        2 * (3 ^ q * 3 ^ odd.length) ≤
          2 * (4 ^ q * odd.prod) :=
      Nat.mul_le_mul_left 2 hCombined
    have hProdOne : b = 2 * (4 ^ q * odd.prod) := by
      rw [hProd]
      simp [hsOne, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
    rw [hProdOne]
    calc
      2 * 3 ^ (k - 1) = 2 * (3 ^ q * 3 ^ odd.length) := by
        rw [← pow_add]
        congr 2
        exact hQOdd.symm
      _ ≤ 2 * (4 ^ q * odd.prod) := hTwoCombined

/-- The weighted shell lower bound is attained by `2*3^(k-1)`. -/
theorem primeFourCost_two_mul_three_pow_pred
    {k : ℕ}
    (hk : 1 ≤ k) :
    rootQuotientPrimeFourCost (2 * 3 ^ (k - 1)) = k := by
  have hTwoCount : rootQuotientPrimeFactorCount 2 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_two]
    simp
  have hThreeCount : rootQuotientPrimeFactorCount 3 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_three]
    simp
  have hPowPos : 1 ≤ 3 ^ (k - 1) := by positivity
  have hCount :
      rootQuotientPrimeFactorCount (2 * 3 ^ (k - 1)) = k := by
    calc
      rootQuotientPrimeFactorCount (2 * 3 ^ (k - 1)) =
          rootQuotientPrimeFactorCount 2 +
            rootQuotientPrimeFactorCount (3 ^ (k - 1)) :=
        rootQuotientPrimeFactorCount_mul (by omega) hPowPos
      _ = 1 + (k - 1) * 1 := by
        rw [rootQuotientPrimeFactorCount_pow (by omega)]
        rw [hTwoCount, hThreeCount]
      _ = k := by omega
  have hValuation : (2 * 3 ^ (k - 1)).factorization 2 = 1 := by
    rw [Nat.factorization_mul (by omega) (by positivity)]
    simp [Nat.prime_two, Nat.prime_three]
  dsimp [rootQuotientPrimeFourCost]
  rw [hCount, hValuation]
  omega

/-- Exact shell minimum for the prime-plus-four weighted metric. -/
theorem primeFourCost_shell_minimum
    {b k : ℕ}
    (hbPos : 1 ≤ b)
    (hk : 1 ≤ k)
    (hCost : rootQuotientPrimeFourCost b = k) :
    2 * 3 ^ (k - 1) ≤ b ∧
      rootQuotientPrimeFourCost (2 * 3 ^ (k - 1)) = k :=
  ⟨two_mul_three_pow_pred_le_of_primeFourCost_eq hbPos hk hCost,
    primeFourCost_two_mul_three_pow_pred hk⟩

/-- Cost threshold form of the weighted shell minimum. -/
theorem primeFourCost_le_iff_not_next_shell_below
    {b h : ℕ}
    (hbPos : 1 ≤ b) :
    rootQuotientPrimeFourCost b ≤ h ↔
      ¬(2 * 3 ^ h ≤ b ∧ h + 1 ≤ rootQuotientPrimeFourCost b) := by
  constructor
  · intro hCost hBad
    omega
  · intro hNot
    by_contra hCost
    have hNext : h + 1 ≤ rootQuotientPrimeFourCost b := by omega
    have hPositive : 1 ≤ rootQuotientPrimeFourCost b := by omega
    have hLower :=
      two_mul_three_pow_pred_le_of_primeFourCost_eq
        hbPos hPositive rfl
    have hExponent : h ≤ rootQuotientPrimeFourCost b - 1 := by omega
    have hPow : 3 ^ h ≤ 3 ^ (rootQuotientPrimeFourCost b - 1) :=
      Nat.pow_le_pow_right (by omega) hExponent
    have hScaled : 2 * 3 ^ h ≤
        2 * 3 ^ (rootQuotientPrimeFourCost b - 1) :=
      Nat.mul_le_mul_left 2 hPow
    exact hNot ⟨hScaled.trans hLower, hNext⟩

end EnterpriseMath.Quotient
