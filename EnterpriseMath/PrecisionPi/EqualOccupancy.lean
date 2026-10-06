import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- Exact equal-occupancy probability for a uniform `k`-state word of length `k*n`.

The value is represented in `ℚ`; no occurrence of `Real.pi` enters this finite layer.
-/
def equalOccupancy (k n : ℕ) : ℚ :=
  (Nat.factorial (k * n) : ℚ) /
    ((Nat.factorial n : ℚ) ^ k * (k : ℚ) ^ (k * n))

/-- The empty word is balanced for every alphabet size. -/
theorem equalOccupancy_zero (k : ℕ) : equalOccupancy k 0 = 1 := by
  simp [equalOccupancy]

/-- The quartic Ramanujan kernel is the four-state equal-occupancy coefficient. -/
abbrev quarticBalance (n : ℕ) : ℚ := equalOccupancy 4 n

/-- The six-state balance coefficient used by the tetrahedral `4 -> 6` precision ratio. -/
abbrev sexticBalance (n : ℕ) : ℚ := equalOccupancy 6 n

/-- First nontrivial quartic coefficient. -/
theorem quarticBalance_one : quarticBalance 1 = 3 / 32 := by
  norm_num [quarticBalance, equalOccupancy, Nat.factorial]

/-- First nontrivial six-state equal-occupancy coefficient. -/
theorem sexticBalance_one : sexticBalance 1 = 5 / 324 := by
  norm_num [sexticBalance, equalOccupancy, Nat.factorial]

/-- The block power in the quartic coefficient can be grouped into powers of `256`. -/
theorem four_pow_four_mul (n : ℕ) : (4 : ℚ) ^ (4 * n) = 256 ^ n := by
  rw [pow_mul]
  norm_num

/-- The block power in the sextic coefficient can be grouped into powers of `46656`. -/
theorem six_pow_six_mul (n : ℕ) : (6 : ℚ) ^ (6 * n) = 46656 ^ n := by
  rw [pow_mul]
  norm_num

end EnterpriseMath.PrecisionPi
