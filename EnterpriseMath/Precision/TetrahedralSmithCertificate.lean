import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralSmithCertificate

/--
Matrix of the zero-sum vertex-to-edge map in the bases used in the paper.
Rows are the first five edge coordinates and columns are three consecutive
zero-sum vertex differences.
-/
def deltaRestricted : Matrix (Fin 5) (Fin 3) ℤ :=
  ![![0, 1, 0],
    ![1, -1, 1],
    ![1, 0, -1],
    ![0, -1, 0],
    ![-1, 1, -1]]

/-- A unit entry certifies first determinantal divisor `d₁ = 1`. -/
theorem unit_entry : deltaRestricted 0 1 = 1 := by
  native_decide

/-- A unit `2×2` minor certifies `d₁ d₂ = 1`. -/
def unitMinor : Matrix (Fin 2) (Fin 2) ℤ :=
  ![![deltaRestricted 0 0, deltaRestricted 0 1],
    ![deltaRestricted 1 0, deltaRestricted 1 1]]

theorem unitMinor_det : Matrix.det unitMinor = -1 := by
  native_decide

/-- The ten maximal minors, in lexicographic row-triple order. -/
def maximalMinor : Fin 10 → Matrix (Fin 3) (Fin 3) ℤ :=
  ![
    ![deltaRestricted 0, deltaRestricted 1, deltaRestricted 2],
    ![deltaRestricted 0, deltaRestricted 1, deltaRestricted 3],
    ![deltaRestricted 0, deltaRestricted 1, deltaRestricted 4],
    ![deltaRestricted 0, deltaRestricted 2, deltaRestricted 3],
    ![deltaRestricted 0, deltaRestricted 2, deltaRestricted 4],
    ![deltaRestricted 0, deltaRestricted 3, deltaRestricted 4],
    ![deltaRestricted 1, deltaRestricted 2, deltaRestricted 3],
    ![deltaRestricted 1, deltaRestricted 2, deltaRestricted 4],
    ![deltaRestricted 1, deltaRestricted 3, deltaRestricted 4],
    ![deltaRestricted 2, deltaRestricted 3, deltaRestricted 4]
  ]

/-- Exact determinant vector of all maximal minors. -/
def maximalMinorDeterminants : Fin 10 → ℤ :=
  ![2, 0, 0, 0, 2, 0, -2, 0, 0, 2]

theorem maximal_minor_determinants_exact :
    ∀ i : Fin 10, Matrix.det (maximalMinor i) = maximalMinorDeterminants i := by
  native_decide

/-- Every maximal minor is even. -/
theorem every_maximal_minor_even :
    ∀ i : Fin 10, Even (Matrix.det (maximalMinor i)) := by
  intro i
  rw [maximal_minor_determinants_exact i]
  fin_cases i <;> norm_num [maximalMinorDeterminants]

/-- One maximal minor is exactly `2`, so their common divisor cannot exceed `2`. -/
theorem maximal_minor_two : Matrix.det (maximalMinor 0) = 2 := by
  exact maximal_minor_determinants_exact 0

/-- The matrix has full column rank over the rationals. -/
theorem full_column_rank_certificate :
    Matrix.det (maximalMinor 0) ≠ 0 := by
  rw [maximal_minor_two]
  norm_num

/--
Determinantal-divisor certificate for Smith invariant factors `(1,1,2)`:
a unit entry, a unit two-minor, all maximal minors even, and one maximal minor
of absolute value two.
-/
theorem smith_112_certificate :
    deltaRestricted 0 1 = 1 ∧
      Matrix.det unitMinor = -1 ∧
      (∀ i : Fin 10, Even (Matrix.det (maximalMinor i))) ∧
      Matrix.det (maximalMinor 0) = 2 := by
  exact ⟨unit_entry, unitMinor_det, every_maximal_minor_even, maximal_minor_two⟩

end EnterpriseMath.PrecisionPi.TetrahedralSmithCertificate
