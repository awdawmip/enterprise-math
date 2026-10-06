import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- The positive Pell shell used by the `N = 58` Ramanujan coordinate. -/
theorem pellPositive99 : (99 : ℤ) ^ 2 - 2 * 70 ^ 2 = 1 := by
  norm_num

/-- The negative Pell shell used by the `N = 58` Ramanujan coordinate. -/
theorem pellNegative58 : (99 : ℤ) ^ 2 - 58 * 13 ^ 2 = -1 := by
  norm_num

/-- The companion negative Pell relation for the `sqrt 29` coordinate. -/
theorem pellNegative29 : (70 : ℤ) ^ 2 - 29 * 13 ^ 2 = -1 := by
  norm_num

/-- Ramanujan's denominator `396` is four times the longitudinal Pell coordinate. -/
theorem denominator396 : (396 : ℤ) = 4 * 99 := by
  norm_num

/-- The classical denominator square is the square of the Pell coordinate. -/
theorem denominator9801 : (9801 : ℤ) = 99 ^ 2 := by
  norm_num

/-- The linear response coefficient factors through the same integer geometry. -/
theorem response26390 : (26390 : ℤ) = 29 * 70 * 13 := by
  norm_num

/-- An integer form of the geometric identity producing the constant `1103`.

Writing the statement without division keeps the certificate entirely in `ℤ`.
-/
theorem constant1103 :
    (4 : ℤ) * 1103 = 29 * 70 * 13 - 2 * 99 * (99 + 13 - 1) := by
  norm_num

/-- The two Pell shells fuse to the quartic residual factor at the rational level. -/
theorem fusedShell99 :
    (1 - (1 : ℚ) / 99 ^ 2) * (1 + (1 : ℚ) / 99 ^ 2) =
      1 - (1 : ℚ) / 99 ^ 4 := by
  norm_num

end EnterpriseMath.PrecisionPi
