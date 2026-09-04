import EnterpriseMath.Precision.HammingShellSpectrum

namespace EnterpriseMath.Precision

open Polynomial

/-- Powers of `-X` carry exactly the scalar sign `(-1)^n`. -/
theorem neg_X_pow (n : ℕ) :
    (-X : ℚ[X]) ^ n = C ((-1 : ℚ) ^ n) * X ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ, ih, pow_succ]
      simp [C_mul, C_neg]

/-- Coefficients under the involution `X ↦ -X`. -/
theorem coeff_comp_neg_X (p : ℚ[X]) (k : ℕ) :
    (p.comp (-X)).coeff k = (-1 : ℚ) ^ k * p.coeff k := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq =>
      simp only [add_comp, coeff_add, hp, hq]
      ring
  | monomial n a =>
      rw [monomial_comp, neg_X_pow]
      rw [← mul_assoc, ← C_mul, coeff_C_mul]
      by_cases h : n = k
      · subst k
        simp [mul_comm]
      · have hk : k ≠ n := by exact fun hkn => h hkn.symm
        simp [h, hk]

/-- Swapping the two shell exponents is exactly the substitution `X ↦ -X`. -/
theorem hammingBasisPoly_swap_comp_neg (a b : ℕ) :
    hammingBasisPoly b a = (hammingBasisPoly a b).comp (-X) := by
  unfold hammingBasisPoly
  simp
  ring

/-- WSR-L48: swapping the two Hamming exponents gives the mode sign `(-1)^k`. -/
theorem hammingModeCoeff_swap (a b k : ℕ) :
    hammingModeCoeff b a k = (-1 : ℚ) ^ k * hammingModeCoeff a b k := by
  unfold hammingModeCoeff
  rw [hammingBasisPoly_swap_comp_neg, coeff_comp_neg_X]

/--
WSR-L49: complement reflection `j ↦ m-j` acts on shell mode `k` by `(-1)^k`.
-/
theorem hammingShellMode_reflection (m k j : ℕ) (hj : j ≤ m) :
    hammingShellMode m k (m - j) =
      (-1 : ℚ) ^ k * hammingShellMode m k j := by
  unfold hammingShellMode
  have hdouble : m - (m - j) = j := by omega
  rw [hdouble]
  exact hammingModeCoeff_swap j (m - j) k

/-- Even-index shell modes are reflection-even. -/
theorem hammingShellMode_reflection_even (m k j : ℕ)
    (hj : j ≤ m) (hk : Even k) :
    hammingShellMode m k (m - j) = hammingShellMode m k j := by
  rw [hammingShellMode_reflection m k j hj, Even.neg_one_pow hk, one_mul]

/-- Odd-index shell modes are reflection-odd. -/
theorem hammingShellMode_reflection_odd (m k j : ℕ)
    (hj : j ≤ m) (hk : Odd k) :
    hammingShellMode m k (m - j) = -hammingShellMode m k j := by
  rw [hammingShellMode_reflection m k j hj, Odd.neg_one_pow hk]
  ring

end EnterpriseMath.Precision
