import EnterpriseMath.Precision.DirichletNormalizedCoefficients
import EnterpriseMath.Precision.DirichletMatrix

namespace EnterpriseMath.Precision

open scoped BigOperators Nat

/-- The exact finite normalized Dirichlet determinant used as the #1159 sine carrier. -/
noncomputable def dirichletFiniteSineDeterminant (M : ℕ) (x : ℝ) : ℝ :=
  (dirichletMatrix (x ^ 2 / (M : ℝ) ^ 2) (M - 1)).det / (M : ℝ)

/-- Rescale one choose-expansion term into the natural even power of `x`. -/
theorem dirichletFiniteSine_term_rescale (M j : ℕ) (x : ℝ) (hM : 0 < M) :
    ((-1 : ℝ) ^ j * (Nat.choose (M + j) (2 * j + 1) : ℝ) *
        (x ^ 2 / (M : ℝ) ^ 2) ^ j) / (M : ℝ) =
      (-1 : ℝ) ^ j * x ^ (2 * j) *
        ((Nat.choose (M + j) (2 * j + 1) : ℝ) / (M : ℝ) ^ (2 * j + 1)) := by
  have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hM)
  rw [div_pow]
  rw [← pow_mul, ← pow_mul]
  rw [pow_succ]
  field_simp [hM0]

/--
WSR-L33 / WSR-T01: exact finite normalized determinant coefficients.

For the project target range `M >= 2` this is exactly
`F_M(x) = det(L_M^D - x^2/M^2 I)/M`, written in the finite recursive
Dirichlet matrix representation. No circle, trigonometric function, or
primitive `pi` is used.
-/
theorem dirichletFiniteSineDeterminant_eq (M : ℕ) (hM : 1 ≤ M) (x : ℝ) :
    dirichletFiniteSineDeterminant M x =
      ∑ j ∈ Finset.range M,
        ((-1 : ℝ) ^ j * x ^ (2 * j) /
          (((2 * j + 1) ! : ℕ) : ℝ)) *
          ∏ r ∈ Finset.range j,
            (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
  have hMpos : 0 < M := by omega
  unfold dirichletFiniteSineDeterminant
  rw [dirichletMatrix_det_eq_continuant]
  rw [dirichletContinuant_pred_choose_expansion M hM]
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro j hj
  have hjM : j < M := Finset.mem_range.mp hj
  rw [dirichletFiniteSine_term_rescale M j x hMpos]
  rw [normalized_choose_eq_unit_defects M j hjM]
  simp [div_eq_mul_inv]
  ring

end EnterpriseMath.Precision
