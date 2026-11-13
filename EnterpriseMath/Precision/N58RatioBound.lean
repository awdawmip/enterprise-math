import EnterpriseMath.Precision.GeometricTailBound

namespace EnterpriseMath.PrecisionPi.N58RatioBound

/-- The factorial part of the N=58 term ratio. -/
def quarticStepRatio (n : ℕ) : ℚ :=
  let x : ℚ := n
  ((4 * x + 1) * (4 * x + 2) * (4 * x + 3) * (4 * x + 4)) /
    (x + 1) ^ 4

/-- The linear-response part of the N=58 term ratio. -/
def linearStepRatio (n : ℕ) : ℚ :=
  let x : ℚ := n
  (1103 + 26390 * (x + 1)) / (1103 + 26390 * x)

/-- Full ratio of successive positive summands before the constant prefactor. -/
def ramanujanStepRatio (n : ℕ) : ℚ :=
  quarticStepRatio n * linearStepRatio n / (396 : ℚ) ^ 4

/-- A simple uniform ratio bound. -/
def q58 : ℚ := 6400 / (396 : ℚ) ^ 4

/-- The factorial ratio is bounded by its limiting value `4⁴ = 256`. -/
theorem quarticStepRatio_le_256 (n : ℕ) : quarticStepRatio n ≤ 256 := by
  let x : ℚ := n
  have hx : 0 ≤ x := by positivity
  have hden : 0 < (x + 1) ^ 4 := by positivity
  unfold quarticStepRatio
  dsimp only
  apply (div_le_iff₀ hden).2
  have hid :
      256 * (x + 1) ^ 4 -
          ((4 * x + 1) * (4 * x + 2) * (4 * x + 3) * (4 * x + 4)) =
        8 * (48 * x ^ 3 + 122 * x ^ 2 + 103 * x + 29) := by
    ring
  have hnonneg :
      0 ≤ 8 * (48 * x ^ 3 + 122 * x ^ 2 + 103 * x + 29) := by
    positivity
  rw [← hid] at hnonneg
  linarith

/-- The linear response ratio is uniformly at most `25`. -/
theorem linearStepRatio_le_25 (n : ℕ) : linearStepRatio n ≤ 25 := by
  let x : ℚ := n
  have hx : 0 ≤ x := by positivity
  have hden : 0 < 1103 + 26390 * x := by positivity
  unfold linearStepRatio
  dsimp only
  apply (div_le_iff₀ hden).2
  have hid :
      25 * (1103 + 26390 * x) - (1103 + 26390 * (x + 1)) =
        82 + 633360 * x := by
    ring
  have hnonneg : 0 ≤ 82 + 633360 * x := by positivity
  rw [← hid] at hnonneg
  linarith

theorem quarticStepRatio_nonneg (n : ℕ) : 0 ≤ quarticStepRatio n := by
  unfold quarticStepRatio
  positivity

theorem linearStepRatio_nonneg (n : ℕ) : 0 ≤ linearStepRatio n := by
  unfold linearStepRatio
  positivity

/-- Every N=58 successive-term ratio is bounded by `q58`. -/
theorem ramanujanStepRatio_le_q58 (n : ℕ) :
    ramanujanStepRatio n ≤ q58 := by
  have hden : 0 < (396 : ℚ) ^ 4 := by norm_num
  unfold ramanujanStepRatio q58
  apply (div_le_div_iff_of_pos_right hden).2
  calc
    quarticStepRatio n * linearStepRatio n ≤
        256 * linearStepRatio n :=
      mul_le_mul_of_nonneg_right (quarticStepRatio_le_256 n)
        (linearStepRatio_nonneg n)
    _ ≤ 256 * 25 :=
      mul_le_mul_of_nonneg_left (linearStepRatio_le_25 n) (by norm_num)
    _ = 6400 := by norm_num

/-- The uniform bound is a genuine contraction. -/
theorem q58_nonneg : 0 ≤ q58 := by
  norm_num [q58]

theorem q58_lt_one : q58 < 1 := by
  norm_num [q58]

/-- Any nonnegative sequence with the N=58 ratio law satisfies the geometric hypothesis. -/
theorem recurrence_implies_q58_bound
    (term : ℕ → ℚ)
    (hterm : ∀ n, 0 ≤ term n)
    (hrec : ∀ n, term (n + 1) = ramanujanStepRatio n * term n) :
    ∀ n, term (n + 1) ≤ q58 * term n := by
  intro n
  rw [hrec n]
  exact mul_le_mul_of_nonneg_right (ramanujanStepRatio_le_q58 n) (hterm n)

end EnterpriseMath.PrecisionPi.N58RatioBound
