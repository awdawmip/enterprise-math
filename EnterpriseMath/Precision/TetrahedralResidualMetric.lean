import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralResidualMetric

abbrev QEdge := Fin 6 → ℚ
abbrev ZEdge := Fin 6 → ℤ

def qdot (x y : QEdge) : ℚ :=
  x 0 * y 0 + x 1 * y 1 + x 2 * y 2 +
    x 3 * y 3 + x 4 * y 4 + x 5 * y 5

def zdot (x y : ZEdge) : ℤ :=
  x 0 * y 0 + x 1 * y 1 + x 2 * y 2 +
    x 3 * y 3 + x 4 * y 4 + x 5 * y 5

def projectedA2Basis : Fin 2 → QEdge :=
  ![![1 / 2, -1 / 2, 0, 1 / 2, -1 / 2, 0],
    ![1 / 2, 0, -1 / 2, 1 / 2, 0, -1 / 2]]

def integralA2Basis : Fin 2 → ZEdge :=
  ![![1, -1, 0, 1, -1, 0],
    ![1, 0, -1, 1, 0, -1]]

theorem projected_basis_zero_sum :
    ∀ i : Fin 2,
      projectedA2Basis i 0 + projectedA2Basis i 1 +
        projectedA2Basis i 2 + projectedA2Basis i 3 +
        projectedA2Basis i 4 + projectedA2Basis i 5 = 0 := by
  native_decide

theorem projected_basis_opposite_pair_constant :
    ∀ i : Fin 2,
      projectedA2Basis i 0 = projectedA2Basis i 3 ∧
      projectedA2Basis i 1 = projectedA2Basis i 4 ∧
      projectedA2Basis i 2 = projectedA2Basis i 5 := by
  native_decide

theorem projected_gram_00 : qdot (projectedA2Basis 0) (projectedA2Basis 0) = 1 := by
  norm_num [qdot, projectedA2Basis]

theorem projected_gram_01 : qdot (projectedA2Basis 0) (projectedA2Basis 1) = 1 / 2 := by
  norm_num [qdot, projectedA2Basis]

theorem projected_gram_10 : qdot (projectedA2Basis 1) (projectedA2Basis 0) = 1 / 2 := by
  norm_num [qdot, projectedA2Basis]

theorem projected_gram_11 : qdot (projectedA2Basis 1) (projectedA2Basis 1) = 1 := by
  norm_num [qdot, projectedA2Basis]

theorem projected_gram_determinant :
    qdot (projectedA2Basis 0) (projectedA2Basis 0) *
        qdot (projectedA2Basis 1) (projectedA2Basis 1) -
      qdot (projectedA2Basis 0) (projectedA2Basis 1) *
        qdot (projectedA2Basis 1) (projectedA2Basis 0) = 3 / 4 := by
  rw [projected_gram_00, projected_gram_01, projected_gram_10, projected_gram_11]
  norm_num

theorem integral_gram_00 : zdot (integralA2Basis 0) (integralA2Basis 0) = 4 := by
  norm_num [zdot, integralA2Basis]

theorem integral_gram_01 : zdot (integralA2Basis 0) (integralA2Basis 1) = 2 := by
  norm_num [zdot, integralA2Basis]

theorem integral_gram_10 : zdot (integralA2Basis 1) (integralA2Basis 0) = 2 := by
  norm_num [zdot, integralA2Basis]

theorem integral_gram_11 : zdot (integralA2Basis 1) (integralA2Basis 1) = 4 := by
  norm_num [zdot, integralA2Basis]

theorem integral_gram_determinant :
    zdot (integralA2Basis 0) (integralA2Basis 0) *
        zdot (integralA2Basis 1) (integralA2Basis 1) -
      zdot (integralA2Basis 0) (integralA2Basis 1) *
        zdot (integralA2Basis 1) (integralA2Basis 0) = 12 := by
  rw [integral_gram_00, integral_gram_01, integral_gram_10, integral_gram_11]
  norm_num

theorem integral_is_twice_projected :
    ∀ i : Fin 2, ∀ e : Fin 6,
      (integralA2Basis i e : ℚ) = 2 * projectedA2Basis i e := by
  native_decide

theorem covolume_square_ratio : (12 : ℚ) = 16 * (3 / 4 : ℚ) := by
  norm_num

end EnterpriseMath.PrecisionPi.TetrahedralResidualMetric
