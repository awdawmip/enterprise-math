import Mathlib

namespace EnterpriseMath.PrecisionPi.Ramanujan58RatioBound

/-- Consecutive ratio of the normalized quartic balance kernel. -/
def balanceStep (x : ℚ) : ℚ :=
  ((4 * x + 1) * (4 * x + 2) * (4 * x + 3) * (4 * x + 4)) /
    (256 * (x + 1) ^ 4)

/-- The extra `99⁻⁴` factor at the `N=58` CM point. -/
def kernelStep (x : ℚ) : ℚ := balanceStep x / 99 ^ 4

/-- Consecutive ratio of the linear response factor `1103+26390n`. -/
def linearStep (x : ℚ) : ℚ :=
  (1103 + 26390 * (x + 1)) / (1103 + 26390 * x)

/-- Consecutive ratio of the positive `N=58` Ramanujan summand. -/
def termStep (x : ℚ) : ℚ := kernelStep x * linearStep x

/-- The quartic balance denominator is positive on the physical range. -/
theorem balanceDenominator_pos {x : ℚ} (hx : 0 ≤ x) :
    0 < 256 * (x + 1) ^ 4 := by
  positivity

/-- The quartic balance numerator is positive on the physical range. -/
theorem balanceNumerator_pos {x : ℚ} (hx : 0 ≤ x) :
    0 < (4 * x + 1) * (4 * x + 2) * (4 * x + 3) * (4 * x + 4) := by
  positivity

/-- The normalized quartic balance step is positive. -/
theorem balanceStep_pos {x : ℚ} (hx : 0 ≤ x) : 0 < balanceStep x := by
  exact div_pos (balanceNumerator_pos hx) (balanceDenominator_pos hx)

/-- Exact positive gap proving that the normalized quartic balance step is
strictly below one. -/
theorem balanceGap (x : ℚ) :
    256 * (x + 1) ^ 4 -
        (4 * x + 1) * (4 * x + 2) * (4 * x + 3) * (4 * x + 4) =
      4 * (x + 1) * (96 * x ^ 2 + 148 * x + 58) := by
  ring

/-- The normalized quartic balance step is strictly below one. -/
theorem balanceStep_lt_one {x : ℚ} (hx : 0 ≤ x) : balanceStep x < 1 := by
  rw [balanceStep, div_lt_one (balanceDenominator_pos hx)]
  have hgap := balanceGap x
  have hpos : 0 < 4 * (x + 1) * (96 * x ^ 2 + 148 * x + 58) := by
    positivity
  linarith

/-- The CM-scaled kernel step is positive. -/
theorem kernelStep_pos {x : ℚ} (hx : 0 ≤ x) : 0 < kernelStep x := by
  exact div_pos (balanceStep_pos hx) (by positivity)

/-- The CM-scaled kernel step is strictly smaller than `99⁻⁴`. -/
theorem kernelStep_lt_invPow {x : ℚ} (hx : 0 ≤ x) :
    kernelStep x < 1 / 99 ^ 4 := by
  unfold kernelStep
  exact (div_lt_div_iff_of_pos_right (by positivity : (0 : ℚ) < 99 ^ 4)).2
    (balanceStep_lt_one hx)

/-- The linear response ratio is positive. -/
theorem linearStep_pos {x : ℚ} (hx : 0 ≤ x) : 0 < linearStep x := by
  unfold linearStep
  positivity

/-- Uniform elementary bound for the linear response ratio. -/
theorem linearStep_lt_twentyFive {x : ℚ} (hx : 0 ≤ x) :
    linearStep x < 25 := by
  rw [linearStep, div_lt_iff (by positivity : (0 : ℚ) < 1103 + 26390 * x)]
  linarith

/-- Uniform geometric bound for the positive `N=58` Ramanujan summand ratio. -/
theorem termStep_lt_geometric {x : ℚ} (hx : 0 ≤ x) :
    termStep x < 25 / 99 ^ 4 := by
  unfold termStep
  calc
    kernelStep x * linearStep x <
        (1 / 99 ^ 4) * linearStep x :=
      mul_lt_mul_of_pos_right (kernelStep_lt_invPow hx) (linearStep_pos hx)
    _ < (1 / 99 ^ 4) * 25 :=
      mul_lt_mul_of_pos_left (linearStep_lt_twentyFive hx) (by positivity)
    _ = 25 / 99 ^ 4 := by ring

/-- The uniform ratio bound itself is strictly below one. -/
theorem geometricBound_lt_one : (25 : ℚ) / 99 ^ 4 < 1 := by
  norm_num

/-- Exact quartic compression denominator. -/
theorem ninetyNine_pow_four : (99 : ℚ) ^ 4 = 96059601 := by
  norm_num

end EnterpriseMath.PrecisionPi.Ramanujan58RatioBound
