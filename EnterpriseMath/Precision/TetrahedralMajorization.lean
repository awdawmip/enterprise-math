import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralMajorization

/-- Descending shifts in the `k = 4` Gamma numerator. -/
def numeratorShift : Fin 5 → ℚ :=
  ![1, 3 / 4, 1 / 2, 1 / 4, 0]

/-- Descending shifts in the `k + 2 = 6` Gamma denominator. -/
def denominatorShift : Fin 5 → ℚ :=
  ![5 / 6, 4 / 6, 3 / 6, 2 / 6, 1 / 6]

/-- Prefix sums of the descending numerator shifts, including the empty prefix. -/
def numeratorPrefix : Fin 6 → ℚ :=
  ![0, 1, 7 / 4, 9 / 4, 5 / 2, 5 / 2]

/-- Prefix sums of the descending denominator shifts, including the empty prefix. -/
def denominatorPrefix : Fin 6 → ℚ :=
  ![0, 5 / 6, 3 / 2, 2, 7 / 3, 5 / 2]

/-- Both shift vectors have the same total sum. -/
theorem equal_total_sum : numeratorPrefix 5 = denominatorPrefix 5 := by
  norm_num [numeratorPrefix, denominatorPrefix]

/-- The exact prefix differences are `0,1/6,1/4,1/4,1/6,0`. -/
def prefixDifference : Fin 6 → ℚ :=
  ![0, 1 / 6, 1 / 4, 1 / 4, 1 / 6, 0]

/-- The stored difference vector is exactly numerator minus denominator. -/
theorem prefix_difference_exact (r : Fin 6) :
    numeratorPrefix r - denominatorPrefix r = prefixDifference r := by
  fin_cases r <;>
    norm_num [numeratorPrefix, denominatorPrefix, prefixDifference]

/-- The numerator shift vector majorizes the denominator shift vector. -/
theorem prefix_domination (r : Fin 6) :
    denominatorPrefix r ≤ numeratorPrefix r := by
  rw [← sub_nonneg]
  rw [prefix_difference_exact]
  fin_cases r <;> norm_num [prefixDifference]

/-- Majorization is strict at every nontrivial proper prefix. -/
theorem strict_prefix_domination
    (r : Fin 6) (hr0 : r ≠ 0) (hr5 : r ≠ 5) :
    denominatorPrefix r < numeratorPrefix r := by
  rw [← sub_pos]
  rw [prefix_difference_exact]
  fin_cases r <;> simp_all [prefixDifference] <;> norm_num

/-- The rational shifts are already written in nonincreasing order. -/
theorem numerator_descending :
    numeratorShift 1 ≤ numeratorShift 0 ∧
    numeratorShift 2 ≤ numeratorShift 1 ∧
    numeratorShift 3 ≤ numeratorShift 2 ∧
    numeratorShift 4 ≤ numeratorShift 3 := by
  norm_num [numeratorShift]

/-- The denominator shifts are likewise nonincreasing. -/
theorem denominator_descending :
    denominatorShift 1 ≤ denominatorShift 0 ∧
    denominatorShift 2 ≤ denominatorShift 1 ∧
    denominatorShift 3 ≤ denominatorShift 2 ∧
    denominatorShift 4 ≤ denominatorShift 3 := by
  norm_num [denominatorShift]

end EnterpriseMath.PrecisionPi.TetrahedralMajorization
