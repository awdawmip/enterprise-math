import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralResidualMetric

abbrev QEdge := Fin 6 → ℚ
abbrev ZEdge := Fin 6 → ℤ

/-- Dot products in the rational and integral six-edge carriers. -/
def qdot (x y : QEdge) : ℚ :=
  x 0 * y 0 + x 1 * y 1 + x 2 * y 2 +
    x 3 * y 3 + x 4 * y 4 + x 5 * y 5

def zdot (x y : ZEdge) : ℤ :=
  x 0 * y 0 + x 1 * y 1 + x 2 * y 2 +
    x 3 * y 3 + x 4 * y 4 + x 5 * y 5

/--
Half-integral projected basis of the free opposite-pair residual plane.
The three opposite pairs are `(0,3)`, `(1,4)`, `(2,5)`.
-/
def projectedA2Basis : Fin 2 → QEdge :=
  ![![1 / 2, -1 / 2, 0, 1 / 2, -1 / 2, 0],
    ![1 / 2, 0, -1 / 2, 1 / 2, 0, -1 / 2]]

/-- Integral intersection basis of the same real plane. -/
def integralA2Basis : Fin 2 → ZEdge :=
  ![![1, -1, 0, 1, -1, 0],
    ![1, 0, -1, 1, 0, -1]]

/-- The projected basis lies in the zero-sum edge hyperplane. -/
theorem projected_basis_zero_sum :
    ∀ i : Fin 2,
      projectedA2Basis i 0 + projectedA2Basis i 1 +
        projectedA2Basis i 2 + projectedA2Basis i 3 +
        projectedA2Basis i 4 + projectedA2Basis i 5 = 0 := by
  native_decide

/-- Each projected basis vector is constant on each opposite edge pair. -/
theorem projected_basis_opposite_pair_constant :
    ∀ i : Fin 2,
      projectedA2Basis i 0 = projectedA2Basis i 3 ∧
      projectedA2Basis i 1 = projectedA2Basis i 4 ∧
      projectedA2Basis i 2 = projectedA2Basis i 5 := by
  native_decide

/-- Exact projected Gram matrix. -/
theorem projected_gram_00 :
    qdot (projectedA2Basis 0) (projectedA2Basis 0) = 1 := by
  native_decide

theorem projected_gram_01 :
    qdot (projectedA2Basis 0) (projectedA2Basis 1) = 1 / 2 := by
  native_decide

theorem projected_gram_10 :
    qdot (projectedA2Basis 1) (projectedA2Basis 0) = 1 / 2 := by
  native_decide

theorem projected_gram_11 :
    qdot (projectedA2Basis 1) (projectedA2Basis 1) = 1 := by
  native_decide

/-- Squared covolume of the projected basis is `3/4`. -/
theorem projected_gram_determinant :
    qdot (projectedA2Basis 0) (projectedA2Basis 0) *
        qdot (projectedA2Basis 1) (projectedA2Basis 1) -
      qdot (projectedA2Basis 0) (projectedA2Basis 1) *
        qdot (projectedA2Basis 1) (projectedA2Basis 0) = 3 / 4 := by
  rw [projected_gram_00, projected_gram_01,
    projected_gram_10, projected_gram_11]
  norm_num

/-- Exact integral Gram matrix. -/
theorem integral_gram_00 :
    zdot (integralA2Basis 0) (integralA2Basis 0) = 4 := by
  native_decide

theorem integral_gram_01 :
    zdot (integralA2Basis 0) (integralA2Basis 1) = 2 := by
  native_decide

theorem integral_gram_10 :
    zdot (integralA2Basis 1) (integralA2Basis 0) = 2 := by
  native_decide

theorem integral_gram_11 :
    zdot (integralA2Basis 1) (integralA2Basis 1) = 4 := by
  native_decide

/-- Squared covolume of the integral intersection basis is `12`. -/
theorem integral_gram_determinant :
    zdot (integralA2Basis 0) (integralA2Basis 0) *
        zdot (integralA2Basis 1) (integralA2Basis 1) -
      zdot (integralA2Basis 0) (integralA2Basis 1) *
        zdot (integralA2Basis 1) (integralA2Basis 0) = 12 := by
  rw [integral_gram_00, integral_gram_01,
    integral_gram_10, integral_gram_11]
  norm_num

/-- The integral basis is exactly twice the projected basis. -/
theorem integral_is_twice_projected :
    ∀ i : Fin 2, ∀ e : Fin 6,
      (integralA2Basis i e : ℚ) = 2 * projectedA2Basis i e := by
  native_decide

/-- The squared covolume ratio is `16`, hence the lattice index is `4`. -/
theorem covolume_square_ratio :
    (12 : ℚ) = 16 * (3 / 4 : ℚ) := by
  norm_num

end EnterpriseMath.PrecisionPi.TetrahedralResidualMetric
