import EnterpriseMath.Precision.DirichletParity
import Mathlib.Algebra.Polynomial.Degree.IsMonicOfDegree

namespace EnterpriseMath.Precision

open Polynomial

/--
The monic characteristic-polynomial normalization of the Dirichlet continuant.
Its real roots are the positive spectral parameters of the finite path matrix.
-/
noncomputable def dirichletSpectralPoly : ℕ → ℝ[X]
  | 0 => 1
  | 1 => X - C 2
  | n + 2 => (X - C 2) * dirichletSpectralPoly (n + 1) - dirichletSpectralPoly n

/-- WSR-L18: `dirichletSpectralPoly n` is monic of exact degree `n`. -/
theorem dirichletSpectralPoly_isMonicOfDegree (n : ℕ) :
    IsMonicOfDegree (dirichletSpectralPoly n) n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [dirichletSpectralPoly]
  | one =>
      exact ⟨natDegree_X_sub_C (2 : ℝ), monic_X_sub_C (2 : ℝ)⟩
  | more n ih0 ih1 =>
      have hlin : IsMonicOfDegree (X - C (2 : ℝ)) 1 :=
        ⟨natDegree_X_sub_C (2 : ℝ), monic_X_sub_C (2 : ℝ)⟩
      have hprod0 := hlin.mul ih1
      have hprod :
          IsMonicOfDegree ((X - C (2 : ℝ)) * dirichletSpectralPoly (n + 1)) (n + 2) := by
        convert hprod0 using 1
        omega
      rw [dirichletSpectralPoly]
      exact hprod.sub (by rw [ih0.natDegree_eq]; omega)

/-- The spectral polynomial has exact natural degree `n`. -/
@[simp] theorem dirichletSpectralPoly_natDegree (n : ℕ) :
    (dirichletSpectralPoly n).natDegree = n :=
  (dirichletSpectralPoly_isMonicOfDegree n).natDegree_eq

/-- The spectral polynomial is monic. -/
theorem dirichletSpectralPoly_monic (n : ℕ) :
    (dirichletSpectralPoly n).Monic :=
  (dirichletSpectralPoly_isMonicOfDegree n).monic

/--
WSR-L19: evaluation of the monic positive-spectrum polynomial is the signed
Dirichlet continuant `(-1)^n D_n(z)`.
-/
theorem dirichletSpectralPoly_eval (n : ℕ) (z : ℝ) :
    (dirichletSpectralPoly n).eval z =
      (-1 : ℝ) ^ n * dirichletContinuant z n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [dirichletSpectralPoly, dirichletContinuant]
  | one =>
      simp [dirichletSpectralPoly, dirichletContinuant]
  | more n ih0 ih1 =>
      have hp1 : (-1 : ℝ) ^ (n + 1) = -((-1 : ℝ) ^ n) := by
        rw [pow_add]
        norm_num
      have hp2 : (-1 : ℝ) ^ (n + 2) = (-1 : ℝ) ^ n := by
        rw [pow_add]
        norm_num
      rw [dirichletSpectralPoly, eval_sub, eval_mul, eval_sub, eval_X, eval_C,
        ih0, ih1, dirichletContinuant, hp1, hp2]
      ring

/-- WSR-L20: exact constant coefficient of the monic spectral polynomial. -/
theorem dirichletSpectralPoly_coeff_zero (n : ℕ) :
    (dirichletSpectralPoly n).coeff 0 =
      (-1 : ℝ) ^ n * ((n + 1 : ℕ) : ℝ) := by
  have h := dirichletSpectralPoly_eval n 0
  rw [dirichletContinuant_zero, ← coeff_zero_eq_eval_zero] at h
  exact h

/-- First midpoint-parity characteristic factor. -/
noncomputable def dirichletParityEvenPoly (n : ℕ) : ℝ[X] :=
  dirichletSpectralPoly (n + 1)

/-- Complementary midpoint-parity characteristic factor. -/
noncomputable def dirichletParityOddPoly (n : ℕ) : ℝ[X] :=
  dirichletSpectralPoly (n + 2) - dirichletSpectralPoly n

/-- The first parity factor is monic of degree `n+1`. -/
theorem dirichletParityEvenPoly_isMonicOfDegree (n : ℕ) :
    IsMonicOfDegree (dirichletParityEvenPoly n) (n + 1) := by
  exact dirichletSpectralPoly_isMonicOfDegree (n + 1)

/-- The complementary parity factor is monic of degree `n+2`. -/
theorem dirichletParityOddPoly_isMonicOfDegree (n : ℕ) :
    IsMonicOfDegree (dirichletParityOddPoly n) (n + 2) := by
  unfold dirichletParityOddPoly
  exact (dirichletSpectralPoly_isMonicOfDegree (n + 2)).sub (by
    rw [dirichletSpectralPoly_natDegree]
    omega)

/-- WSR-L21: the odd fine-chain characteristic polynomial factors into parity sectors. -/
theorem dirichletSpectralPoly_odd_factorization (n : ℕ) :
    dirichletSpectralPoly (2 * n + 3) =
      dirichletParityEvenPoly n * dirichletParityOddPoly n := by
  apply Polynomial.funext
  intro z
  simp only [dirichletParityEvenPoly, dirichletParityOddPoly, eval_mul, eval_sub]
  rw [dirichletSpectralPoly_eval, dirichletSpectralPoly_eval,
    dirichletSpectralPoly_eval, dirichletSpectralPoly_eval]
  rw [dirichletContinuant_odd_factorization]
  have hodd : Odd (2 * n + 3) := ⟨n + 1, by omega⟩
  have hp1 : (-1 : ℝ) ^ (n + 1) = -((-1 : ℝ) ^ n) := by
    rw [pow_add]
    norm_num
  have hp2 : (-1 : ℝ) ^ (n + 2) = (-1 : ℝ) ^ n := by
    rw [pow_add]
    norm_num
  have heven : Even (n * 2) := ⟨n, by ring⟩
  rw [Odd.neg_one_pow hodd, hp1, hp2, Even.neg_one_pow heven]
  ring

/-- Constant coefficient of the first parity factor. -/
theorem dirichletParityEvenPoly_coeff_zero (n : ℕ) :
    (dirichletParityEvenPoly n).coeff 0 =
      (-1 : ℝ) ^ (n + 1) * ((n + 2 : ℕ) : ℝ) := by
  exact dirichletSpectralPoly_coeff_zero (n + 1)

/-- Constant coefficient of the complementary parity factor. -/
theorem dirichletParityOddPoly_coeff_zero (n : ℕ) :
    (dirichletParityOddPoly n).coeff 0 =
      (-1 : ℝ) ^ n * 2 := by
  unfold dirichletParityOddPoly
  rw [coeff_sub, dirichletSpectralPoly_coeff_zero,
    dirichletSpectralPoly_coeff_zero]
  have hp2 : (-1 : ℝ) ^ (n + 2) = (-1 : ℝ) ^ n := by
    rw [pow_add]
    norm_num
  rw [hp2]
  push_cast
  ring

end EnterpriseMath.Precision
