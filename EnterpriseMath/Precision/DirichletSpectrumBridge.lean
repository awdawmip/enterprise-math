import EnterpriseMath.Precision.DirichletMatrix
import EnterpriseMath.Precision.DirichletPolynomial
import Mathlib.Analysis.Matrix.Spectrum

namespace EnterpriseMath.Precision

open Polynomial

/--
WSR-L36: the recursively declared monic spectral polynomial is exactly the
characteristic polynomial of the finite zero-parameter Dirichlet matrix.
-/
theorem dirichletSpectralPoly_eq_charpoly (n : ℕ) :
    dirichletSpectralPoly n = (dirichletMatrix 0 n).charpoly := by
  apply Polynomial.funext
  intro z
  rw [dirichletSpectralPoly_eval, Matrix.eval_charpoly,
    dirichletMatrix_scalar_sub_zero, Matrix.det_neg,
    Fintype.card_fin, dirichletMatrix_det_eq_continuant]

/-- WSR-L37: every finite Dirichlet spectral polynomial splits over `ℝ`. -/
theorem dirichletSpectralPoly_splits (n : ℕ) :
    (dirichletSpectralPoly n).Splits := by
  rw [dirichletSpectralPoly_eq_charpoly]
  exact (dirichletMatrix_isHermitian 0 n).splits_charpoly

/--
WSR-L38: the two midpoint-parity factors of the odd fine-chain characteristic
polynomial both split over `ℝ`.
-/
theorem dirichletParityFactors_splits (n : ℕ) :
    (dirichletParityEvenPoly n).Splits ∧
      (dirichletParityOddPoly n).Splits := by
  have hfull :
      (dirichletParityEvenPoly n * dirichletParityOddPoly n).Splits := by
    rw [← dirichletSpectralPoly_odd_factorization]
    exact dirichletSpectralPoly_splits (2 * n + 3)
  have hE0 : dirichletParityEvenPoly n ≠ 0 :=
    (dirichletParityEvenPoly_isMonicOfDegree n).monic.ne_zero
  have hO0 : dirichletParityOddPoly n ≠ 0 :=
    (dirichletParityOddPoly_isMonicOfDegree n).monic.ne_zero
  exact (Polynomial.splits_mul hE0 hO0).mp hfull

/--
WSR-L39: the first parity factor has real-root product exactly `n+2`.
With `q=n+2`, this is the finite parity-sector product `q` used in #1159.
-/
theorem dirichletParityEvenPoly_roots_prod (n : ℕ) :
    (dirichletParityEvenPoly n).roots.prod = ((n + 2 : ℕ) : ℝ) := by
  have hs := (dirichletParityFactors_splits n).1.coeff_zero_eq_prod_roots_of_monic
    (dirichletParityEvenPoly_isMonicOfDegree n).monic
  rw [dirichletParityEvenPoly_coeff_zero,
    (dirichletParityEvenPoly_isMonicOfDegree n).natDegree_eq] at hs
  have hsign : ((-1 : ℝ) ^ (n + 1)) ≠ 0 := by positivity
  exact (mul_left_cancel₀ hsign hs).symm

/--
WSR-L40: the complementary parity factor has real-root product exactly `2`.
This is the second finite parity-sector product used in #1159.
-/
theorem dirichletParityOddPoly_roots_prod (n : ℕ) :
    (dirichletParityOddPoly n).roots.prod = (2 : ℝ) := by
  have hs := (dirichletParityFactors_splits n).2.coeff_zero_eq_prod_roots_of_monic
    (dirichletParityOddPoly_isMonicOfDegree n).monic
  rw [dirichletParityOddPoly_coeff_zero,
    (dirichletParityOddPoly_isMonicOfDegree n).natDegree_eq] at hs
  have hp2 : (-1 : ℝ) ^ (n + 2) = (-1 : ℝ) ^ n := by
    rw [pow_add]
    norm_num
  rw [hp2] at hs
  have hsign : ((-1 : ℝ) ^ n) ≠ 0 := by positivity
  exact (mul_left_cancel₀ hsign hs).symm

end EnterpriseMath.Precision
