import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralWallisRatio

/-- Numerator of the exact consecutive ratio for the tetrahedral
`P₄/P₆` precision sequence. -/
def numerator (x : ℚ) : ℚ :=
  81 * x * (x + 1) * (4 * x + 1) * (4 * x + 3)

/-- Denominator of the exact consecutive ratio for the tetrahedral
`P₄/P₆` precision sequence. -/
def denominator (x : ℚ) : ℚ :=
  4 * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5)

/-- Exact rational block appearing in the tetrahedral Wallis product. -/
def ratio (x : ℚ) : ℚ := numerator x / denominator x

/-- The denominator is positive on the nonnegative resolution range. -/
theorem denominator_pos {x : ℚ} (hx : 0 ≤ x) : 0 < denominator x := by
  unfold denominator
  positivity

/-- The numerator is positive at every positive resolution depth. -/
theorem numerator_pos {x : ℚ} (hx : 0 < x) : 0 < numerator x := by
  unfold numerator
  positivity

/-- The denominator-minus-numerator gap collapses to a simple positive
quadratic expression. -/
theorem denominator_sub_numerator (x : ℚ) :
    denominator x - numerator x = 225 * x * (x + 1) + 40 := by
  unfold denominator numerator
  ring

/-- Every positive tetrahedral Wallis ratio is positive. -/
theorem ratio_pos {x : ℚ} (hx : 0 < x) : 0 < ratio x := by
  exact div_pos (numerator_pos hx) (denominator_pos hx.le)

/-- Every nonnegative tetrahedral Wallis block is strictly smaller than one. -/
theorem ratio_lt_one {x : ℚ} (hx : 0 ≤ x) : ratio x < 1 := by
  rw [ratio, div_lt_one (denominator_pos hx)]
  have hgap := denominator_sub_numerator x
  have hnonneg : 0 ≤ 225 * x * (x + 1) := by positivity
  linarith

/-- Hence the block lies in `(0,1)` at every natural depth `n≥1`. -/
theorem ratio_nat_mem_unitInterval {n : ℕ} (hn : 1 ≤ n) :
    0 < ratio n ∧ ratio n < 1 := by
  have hnq : (0 : ℚ) < n := by exact_mod_cast (show 0 < n by omega)
  exact ⟨ratio_pos hnq, ratio_lt_one hnq.le⟩

/-- First tetrahedral Wallis block. -/
theorem ratio_one : ratio 1 = 567 / 616 := by
  norm_num [ratio, numerator, denominator]

end EnterpriseMath.PrecisionPi.TetrahedralWallisRatio
