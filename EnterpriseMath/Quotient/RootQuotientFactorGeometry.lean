import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Project prime-factor instruction count is the standard arithmetic-function
`Omega`, equivalently the `l1` sum of the prime-exponent factorization vector. -/
theorem rootQuotientPrimeFactorCount_eq_factorization_sum
    (b : ℕ) :
    rootQuotientPrimeFactorCount b =
      b.factorization.sum (fun _ exponent => exponent) := by
  simpa [rootQuotientPrimeFactorCount,
    ArithmeticFunction.cardFactors_apply] using
    (ArithmeticFunction.cardFactors_eq_sum_factorization (n := b))

/-- For a positive denominator, the project's `r`-power-free predicate is
exactly the coordinate box condition that every prime exponent is strictly
below `r`.

Thus the canonical semantic action set is a bounded down-set in the ordinary
prime-factorization lattice. -/
theorem rPowerFree_iff_prime_factorization_lt
    {r b : ℕ}
    (hbPos : 1 ≤ b) :
    RPowerFree r b ↔
      ∀ p : ℕ, p.Prime → b.factorization p < r := by
  constructor
  · intro hbFree p hp
    by_contra hNot
    have hrLe : r ≤ b.factorization p := by omega
    have hbZero : b ≠ 0 := by omega
    have hPowDvd : p ^ r ∣ b :=
      (hp.pow_dvd_iff_le_factorization hbZero).2 hrLe
    exact hbFree p hp.two_le hPowDvd
  · intro hCap t ht hPowerDvd
    have htOne : t ≠ 1 := by omega
    obtain ⟨p, hpPrime, hpDvdT⟩ := Nat.exists_prime_and_dvd htOne
    obtain ⟨c, htc⟩ := hpDvdT
    have hpPowDvdTPow : p ^ r ∣ t ^ r := by
      refine ⟨c ^ r, ?_⟩
      calc
        t ^ r = (p * c) ^ r := by rw [htc]
        _ = p ^ r * c ^ r := by rw [mul_pow]
    have hpPowDvdB : p ^ r ∣ b :=
      dvd_trans hpPowDvdTPow hPowerDvd
    have hbZero : b ≠ 0 := by omega
    have hrLe : r ≤ b.factorization p :=
      (hpPrime.pow_dvd_iff_le_factorization hbZero).1 hpPowDvdB
    exact (not_lt_of_ge hrLe) (hCap p hpPrime)

end EnterpriseMath.Quotient
