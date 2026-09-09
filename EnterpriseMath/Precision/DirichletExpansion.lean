import EnterpriseMath.Precision.DirichletCoefficients

namespace EnterpriseMath.Precision

open Polynomial
open scoped BigOperators

/-- The square of every `(-1)^n` sign is one. -/
theorem negOnePow_sq (n : ℕ) : (((-1 : ℝ) ^ n) ^ 2) = 1 := by
  rw [← pow_mul]
  exact Even.neg_one_pow ⟨n, by ring⟩

/-- Recover the continuant from the signed monic spectral polynomial evaluation. -/
theorem dirichletContinuant_eq_signed_spectral_eval (n : ℕ) (z : ℝ) :
    dirichletContinuant z n =
      (-1 : ℝ) ^ n * (dirichletSpectralPoly n).eval z := by
  rw [dirichletSpectralPoly_eval]
  have hs := negOnePow_sq n
  calc
    dirichletContinuant z n = 1 * dirichletContinuant z n := by ring
    _ = (((-1 : ℝ) ^ n) ^ 2) * dirichletContinuant z n := by rw [hs]
    _ = (-1 : ℝ) ^ n *
        ((-1 : ℝ) ^ n * dirichletContinuant z n) := by ring

/--
WSR-L30: exact finite choose expansion of the Dirichlet continuant.
No trigonometric function, circle, or primitive `pi` enters this identity.
-/
theorem dirichletContinuant_choose_expansion (n : ℕ) (z : ℝ) :
    dirichletContinuant z n =
      ∑ j ∈ Finset.range (n + 1),
        (-1 : ℝ) ^ j *
          (Nat.choose (n + 1 + j) (2 * j + 1) : ℝ) * z ^ j := by
  rw [dirichletContinuant_eq_signed_spectral_eval]
  rw [Polynomial.eval_eq_sum_range, dirichletSpectralPoly_natDegree]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [dirichletSpectralPoly_coeff_choose]
  rw [pow_add]
  have hs := negOnePow_sq n
  calc
    (-1 : ℝ) ^ n *
        (((-1 : ℝ) ^ n * (-1 : ℝ) ^ j) *
          (Nat.choose (n + 1 + j) (2 * j + 1) : ℝ) * z ^ j)
        = (((-1 : ℝ) ^ n) ^ 2) *
          ((-1 : ℝ) ^ j *
            (Nat.choose (n + 1 + j) (2 * j + 1) : ℝ) * z ^ j) := by ring
    _ = (-1 : ℝ) ^ j *
          (Nat.choose (n + 1 + j) (2 * j + 1) : ℝ) * z ^ j := by
      rw [hs]
      ring

/--
WSR-L31: the `(M-1)`-dimensional Dirichlet determinant expansion in the
natural `M` normalization used by #1159.
-/
theorem dirichletContinuant_pred_choose_expansion (M : ℕ) (hM : 1 ≤ M) (z : ℝ) :
    dirichletContinuant z (M - 1) =
      ∑ j ∈ Finset.range M,
        (-1 : ℝ) ^ j *
          (Nat.choose (M + j) (2 * j + 1) : ℝ) * z ^ j := by
  simpa [Nat.sub_add_cancel hM] using
    dirichletContinuant_choose_expansion (M - 1) z

end EnterpriseMath.Precision
