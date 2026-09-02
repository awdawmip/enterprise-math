import EnterpriseMath.PrecisionPi.N58RotationGeometry

namespace EnterpriseMath.PrecisionPi.N58HalfAngleDefect

/-- Algebraic carrier lengths. -/
def sqrt58 : ℝ := Real.sqrt 58

def sqrt29 : ℝ := Real.sqrt 29

@[simp] theorem sqrt58_sq : sqrt58 ^ 2 = 58 := by
  norm_num [sqrt58]

@[simp] theorem sqrt29_sq : sqrt29 ^ 2 = 29 := by
  norm_num [sqrt29]

/-- Small and large conjugate coordinates of the N=58 near-axis vector. -/
def defect58 : ℝ := 13 * sqrt58 - 99

def conjugate58 : ℝ := 13 * sqrt58 + 99

/-- The negative-Pell equation makes the two conjugates multiply to one. -/
theorem defect58_mul_conjugate58 : defect58 * conjugate58 = 1 := by
  calc
    defect58 * conjugate58 = 169 * sqrt58 ^ 2 - 99 ^ 2 := by
      ring
    _ = 1 := by norm_num

/-- The large conjugate is positive. -/
theorem conjugate58_pos : 0 < conjugate58 := by
  have hs : 0 ≤ sqrt58 := Real.sqrt_nonneg _
  simp [conjugate58]
  positivity

/-- The near-axis defect is positive. -/
theorem defect58_pos : 0 < defect58 := by
  have hp : 0 < defect58 * conjugate58 := by
    rw [defect58_mul_conjugate58]
    norm_num
  rcases (mul_pos_iff.mp hp) with h | h
  · exact h.1
  · exact (not_lt_of_ge conjugate58_pos.le h.2).elim

/-- The small defect is exactly the reciprocal of the large conjugate. -/
theorem defect58_eq_reciprocal : defect58 = 1 / conjugate58 := by
  apply (eq_div_iff conjugate58_pos.ne').2
  exact defect58_mul_conjugate58

/-- Companion near-axis defect for the sqrt(29) direction. -/
def defect29 : ℝ := 13 * sqrt29 - 70

def conjugate29 : ℝ := 13 * sqrt29 + 70

/-- The companion Pell equation also gives a unit conjugate product. -/
theorem defect29_mul_conjugate29 : defect29 * conjugate29 = 1 := by
  calc
    defect29 * conjugate29 = 169 * sqrt29 ^ 2 - 70 ^ 2 := by
      ring
    _ = 1 := by norm_num

/-- Positivity of the large sqrt(29) conjugate. -/
theorem conjugate29_pos : 0 < conjugate29 := by
  have hs : 0 ≤ sqrt29 := Real.sqrt_nonneg _
  simp [conjugate29]
  positivity

/-- Positivity of the companion near-axis defect. -/
theorem defect29_pos : 0 < defect29 := by
  have hp : 0 < defect29 * conjugate29 := by
    rw [defect29_mul_conjugate29]
    norm_num
  rcases (mul_pos_iff.mp hp) with h | h
  · exact h.1
  · exact (not_lt_of_ge conjugate29_pos.le h.2).elim

/-- Exact reciprocal form of the companion defect. -/
theorem defect29_eq_reciprocal : defect29 = 1 / conjugate29 := by
  apply (eq_div_iff conjugate29_pos.ne').2
  exact defect29_mul_conjugate29

/-- Both algebraic defects lie strictly between zero and one. -/
theorem defect_bounds :
    0 < defect58 ∧ defect58 < 1 ∧
    0 < defect29 ∧ defect29 < 1 := by
  have hc58 : 1 < conjugate58 := by
    have hs : 0 ≤ sqrt58 := Real.sqrt_nonneg _
    simp [conjugate58]
    linarith
  have hc29 : 1 < conjugate29 := by
    have hs : 0 ≤ sqrt29 := Real.sqrt_nonneg _
    simp [conjugate29]
    linarith
  refine ⟨defect58_pos, ?_, defect29_pos, ?_⟩
  · rw [defect58_eq_reciprocal]
    exact one_div_lt_one hc58
  · rw [defect29_eq_reciprocal]
    exact one_div_lt_one hc29

end EnterpriseMath.PrecisionPi.N58HalfAngleDefect
