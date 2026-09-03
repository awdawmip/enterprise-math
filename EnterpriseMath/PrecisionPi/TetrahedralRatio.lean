import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- Exact adjacent-depth contraction factor for the tetrahedral `4 -> 6`
precision ratio, after cancelling the common square-root normalization. -/
def tetrahedralRatio (n : ℕ) : ℚ :=
  let x : ℚ := n
  81 * x * (x + 1) * (4 * x + 1) * (4 * x + 3) /
    (4 * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5))

/-- The denominator-minus-numerator polynomial has a manifestly positive form. -/
theorem tetrahedralRatio_gap (n : ℕ) :
    let x : ℚ := n
    4 * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5) -
        81 * x * (x + 1) * (4 * x + 1) * (4 * x + 3) =
      5 * (45 * x ^ 2 + 45 * x + 8) := by
  dsimp
  ring

/-- Every finite tetrahedral refinement step is a strict contraction. -/
theorem tetrahedralRatio_lt_one (n : ℕ) : tetrahedralRatio n < 1 := by
  let x : ℚ := n
  have hx : 0 ≤ x := by
    positivity
  have hden :
      0 < 4 * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5) := by
    positivity
  have hgap :
      0 < 5 * (45 * x ^ 2 + 45 * x + 8) := by
    positivity
  have hid :
      4 * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5) -
          81 * x * (x + 1) * (4 * x + 1) * (4 * x + 3) =
        5 * (45 * x ^ 2 + 45 * x + 8) := by
    ring
  apply (div_lt_one hden).2
  linarith

/-- The contraction factor is nonnegative. -/
theorem tetrahedralRatio_nonneg (n : ℕ) : 0 ≤ tetrahedralRatio n := by
  dsimp [tetrahedralRatio]
  positivity

end EnterpriseMath.PrecisionPi
