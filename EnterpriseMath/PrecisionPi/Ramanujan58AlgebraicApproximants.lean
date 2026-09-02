import EnterpriseMath.PrecisionPi.QuarticEqualOccupancy

namespace EnterpriseMath.PrecisionPi.Ramanujan58AlgebraicApproximants

open QuarticEqualOccupancy

/-- Quartic CM coordinate of the `N=58` formula. -/
def z58 : ℚ := 1 / 99 ^ 4

/-- Linear response coefficient in normalized quartic-kernel coordinates. -/
def response58 (n : ℕ) : ℚ := 1103 + 26390 * n

/-- Rational inner summand of the `N=58` Ramanujan formula, before the
positive global factor `2√2/99²`. -/
def term58 (n : ℕ) : ℚ :=
  response58 n * equalOccupancyQ 4 n * z58 ^ n

/-- Every finite `N=58` inner summand is strictly positive. -/
theorem term58_pos (n : ℕ) : 0 < term58 n := by
  have hp4 : 0 < equalOccupancyQ 4 n := by
    unfold equalOccupancyQ
    positivity
  unfold term58 response58 z58
  positivity

/-- Exact first inner summand. -/
theorem term58_zero : term58 0 = 1103 := by
  norm_num [term58, response58, z58, equalOccupancyQ]

/-- Finite inner partial sums, indexed by the largest included depth. -/
def partial58 : ℕ → ℚ
  | 0 => term58 0
  | M + 1 => partial58 M + term58 (M + 1)

/-- Every finite inner partial sum is strictly positive. -/
theorem partial58_pos (M : ℕ) : 0 < partial58 M := by
  induction M with
  | zero => simpa [partial58] using term58_pos 0
  | succ M ih =>
      simp only [partial58]
      exact add_pos ih (term58_pos (M + 1))

/-- Each additional Ramanujan term strictly increases the inverse-period
partial sum. -/
theorem partial58_strict_step (M : ℕ) : partial58 M < partial58 (M + 1) := by
  simp only [partial58]
  exact lt_add_of_pos_right _ (term58_pos (M + 1))

/-- Reciprocal rational component of the finite algebraic precision value. -/
def reciprocalPartial58 (M : ℕ) : ℚ := 1 / partial58 M

/-- The reciprocal partial values are strictly positive. -/
theorem reciprocalPartial58_pos (M : ℕ) : 0 < reciprocalPartial58 M := by
  unfold reciprocalPartial58
  positivity

/-- Positive inverse-period accumulation makes the reciprocal precision
values strictly decrease. -/
theorem reciprocalPartial58_strict_step (M : ℕ) :
    reciprocalPartial58 (M + 1) < reciprocalPartial58 M := by
  unfold reciprocalPartial58
  exact one_div_lt_one_div_of_lt (partial58_pos M) (partial58_strict_step M)

/-- The first reciprocal rational component. -/
theorem reciprocalPartial58_zero : reciprocalPartial58 0 = 1 / 1103 := by
  norm_num [reciprocalPartial58, partial58, term58_zero]

end EnterpriseMath.PrecisionPi.Ramanujan58AlgebraicApproximants
