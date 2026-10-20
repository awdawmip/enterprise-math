import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralSmithCertificate

/-- Matrix of the zero-sum vertex-to-edge map in paper coordinates. -/
def deltaRestricted : Matrix (Fin 5) (Fin 3) ℤ :=
  ![![0, 1, 0],
    ![1, -1, 1],
    ![1, 0, -1],
    ![0, -1, 0],
    ![-1, 1, -1]]

theorem unit_entry : deltaRestricted 0 1 = 1 := by native_decide

def unitMinor : Matrix (Fin 2) (Fin 2) ℤ :=
  ![![deltaRestricted 0 0, deltaRestricted 0 1],
    ![deltaRestricted 1 0, deltaRestricted 1 1]]

theorem unitMinor_det : Matrix.det unitMinor = -1 := by native_decide

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

def maximalMinorDeterminants : Fin 10 → ℤ :=
  ![2, 0, 0, 0, 2, 0, -2, 0, 0, 2]

theorem maximal_minor_determinants_exact :
    ∀ i : Fin 10, Matrix.det (maximalMinor i) = maximalMinorDeterminants i := by
  native_decide

theorem every_maximal_minor_even :
    ∀ i : Fin 10, Even (Matrix.det (maximalMinor i)) := by
  intro i
  rw [maximal_minor_determinants_exact i]
  fin_cases i <;> norm_num [maximalMinorDeterminants]

theorem maximal_minor_two : Matrix.det (maximalMinor 0) = 2 :=
  maximal_minor_determinants_exact 0

theorem full_column_rank_certificate : Matrix.det (maximalMinor 0) ≠ 0 := by
  rw [maximal_minor_two]
  norm_num

/-- Determinantal-divisor certificate for Smith invariant factors `(1,1,2)`. -/
theorem smith_112_certificate :
    deltaRestricted 0 1 = 1 ∧
      Matrix.det unitMinor = -1 ∧
      (∀ i : Fin 10, Even (Matrix.det (maximalMinor i))) ∧
      Matrix.det (maximalMinor 0) = 2 := by
  exact ⟨unit_entry, unitMinor_det, every_maximal_minor_even, maximal_minor_two⟩

end EnterpriseMath.PrecisionPi.TetrahedralSmithCertificate
