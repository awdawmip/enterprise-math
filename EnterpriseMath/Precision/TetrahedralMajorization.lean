import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralMajorization

def numeratorShift : Fin 5 → ℚ :=
  ![1, 3 / 4, 1 / 2, 1 / 4, 0]

def denominatorShift : Fin 5 → ℚ :=
  ![5 / 6, 4 / 6, 3 / 6, 2 / 6, 1 / 6]

def numeratorPrefix : Fin 6 → ℚ :=
  ![0, 1, 7 / 4, 9 / 4, 5 / 2, 5 / 2]

def denominatorPrefix : Fin 6 → ℚ :=
  ![0, 5 / 6, 3 / 2, 2, 7 / 3, 5 / 2]

def prefixDifference : Fin 6 → ℚ :=
  ![0, 1 / 6, 1 / 4, 1 / 4, 1 / 6, 0]

theorem equal_total_sum : numeratorPrefix 5 = denominatorPrefix 5 := by
  norm_num [numeratorPrefix, denominatorPrefix]

theorem prefix_difference_exact (r : Fin 6) :
    numeratorPrefix r - denominatorPrefix r = prefixDifference r := by
  fin_cases r <;>
    norm_num [numeratorPrefix, denominatorPrefix, prefixDifference]

theorem prefix_domination (r : Fin 6) :
    denominatorPrefix r ≤ numeratorPrefix r := by
  have h : 0 ≤ numeratorPrefix r - denominatorPrefix r := by
    rw [prefix_difference_exact]
    fin_cases r <;> norm_num [prefixDifference]
  linarith

theorem strict_prefix_domination
    (r : Fin 6) (hr0 : r ≠ 0) (hr5 : r ≠ 5) :
    denominatorPrefix r < numeratorPrefix r := by
  have h : 0 < numeratorPrefix r - denominatorPrefix r := by
    rw [prefix_difference_exact]
    fin_cases r <;> simp_all [prefixDifference] <;> norm_num
  linarith

theorem numerator_descending :
    numeratorShift 1 ≤ numeratorShift 0 ∧
    numeratorShift 2 ≤ numeratorShift 1 ∧
    numeratorShift 3 ≤ numeratorShift 2 ∧
    numeratorShift 4 ≤ numeratorShift 3 := by
  norm_num [numeratorShift]

theorem denominator_descending :
    denominatorShift 1 ≤ denominatorShift 0 ∧
    denominatorShift 2 ≤ denominatorShift 1 ∧
    denominatorShift 3 ≤ denominatorShift 2 ∧
    denominatorShift 4 ≤ denominatorShift 3 := by
  norm_num [denominatorShift]

end EnterpriseMath.PrecisionPi.TetrahedralMajorization
