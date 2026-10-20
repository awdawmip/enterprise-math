import EnterpriseMath.Quotient.RootQuotientFactorGeometry
import Mathlib.Data.Nat.Squarefree
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Prime-factor instruction count grows linearly under positive powers. -/
theorem rootQuotientPrimeFactorCount_pow
    {a m : ℕ}
    (ha : 1 ≤ a) :
    rootQuotientPrimeFactorCount (a ^ m) =
      m * rootQuotientPrimeFactorCount a := by
  induction m with
  | zero => simp [rootQuotientPrimeFactorCount]
  | succ m ih =>
      have hPowPos : 1 ≤ a ^ m := by positivity
      calc
        rootQuotientPrimeFactorCount (a ^ (m + 1)) =
            rootQuotientPrimeFactorCount (a ^ m * a) := by
          rw [pow_succ]
        _ = rootQuotientPrimeFactorCount (a ^ m) +
            rootQuotientPrimeFactorCount a :=
          rootQuotientPrimeFactorCount_mul hPowPos ha
        _ = (m + 1) * rootQuotientPrimeFactorCount a := by
          rw [ih]
          simp [Nat.succ_mul]

/-- A squarefree positive base raised to an exponent below the root order
remains `r`-power-free. -/
theorem rPowerFree_pow_of_squarefree
    {r a m : ℕ}
    (ha : 1 ≤ a)
    (haSquarefree : Squarefree a)
    (hm : m < r) :
    RPowerFree r (a ^ m) := by
  have hPowPos : 1 ≤ a ^ m := by positivity
  apply (rPowerFree_iff_prime_factorization_lt hPowPos).2
  intro p _hp
  have hExpLe : a.factorization p ≤ 1 :=
    haSquarefree.natFactorization_le_one p
  rw [Nat.factorization_pow]
  by_cases hZero : a.factorization p = 0
  · simp [hZero]
  · have hOne : a.factorization p = 1 := by omega
    simpa [hOne] using hm

/-- Coprime positive `r`-power-free factors can be multiplied without violating
the exponent box. -/
theorem rPowerFree_mul_of_coprime
    {r a b : ℕ}
    (ha : 1 ≤ a)
    (hb : 1 ≤ b)
    (haFree : RPowerFree r a)
    (hbFree : RPowerFree r b)
    (hab : Nat.Coprime a b) :
    RPowerFree r (a * b) := by
  have hMulPos : 1 ≤ a * b := Nat.one_le_mul ha hb
  have haZero : a ≠ 0 := by omega
  have hbZero : b ≠ 0 := by omega
  have hDisjointFactors : Disjoint a.primeFactors b.primeFactors :=
    (Nat.disjoint_primeFactors haZero hbZero).2 hab
  have haBox := (rPowerFree_iff_prime_factorization_lt ha).1 haFree
  have hbBox := (rPowerFree_iff_prime_factorization_lt hb).1 hbFree
  apply (rPowerFree_iff_prime_factorization_lt hMulPos).2
  intro p hpPrime
  have hOneZero : a.factorization p = 0 ∨ b.factorization p = 0 := by
    by_contra hNeither
    push_neg at hNeither
    have hpA : p ∈ a.primeFactors := by
      rw [← Nat.support_factorization]
      exact Finsupp.mem_support_iff.mpr hNeither.1
    have hpB : p ∈ b.primeFactors := by
      rw [← Nat.support_factorization]
      exact Finsupp.mem_support_iff.mpr hNeither.2
    exact (Finset.disjoint_left.1 hDisjointFactors hpA hpB)
  rw [Nat.factorization_mul haZero hbZero]
  simp only [Finsupp.add_apply]
  rcases hOneZero with haExpZero | hbExpZero
  · simpa [haExpZero] using hbBox p hpPrime
  · simpa [hbExpZero] using haBox p hpPrime

end EnterpriseMath.Quotient
