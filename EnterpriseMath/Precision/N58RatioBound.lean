import EnterpriseMath.Precision.GeometricTailBound

namespace EnterpriseMath.PrecisionPi.N58RatioBound

def quarticStepRatio (n : ℕ) : ℚ :=
  ((4 * (n : ℚ) + 1) * (4 * (n : ℚ) + 2) *
      (4 * (n : ℚ) + 3) * (4 * (n : ℚ) + 4)) /
    ((n : ℚ) + 1) ^ 4

def linearStepRatio (n : ℕ) : ℚ :=
  (1103 + 26390 * ((n : ℚ) + 1)) / (1103 + 26390 * (n : ℚ))

def ramanujanStepRatio (n : ℕ) : ℚ :=
  quarticStepRatio n * linearStepRatio n / (396 : ℚ) ^ 4

def q58 : ℚ := 6400 / (396 : ℚ) ^ 4

theorem quarticStepRatio_le_256 (n : ℕ) : quarticStepRatio n ≤ 256 := by
  have hx : 0 ≤ (n : ℚ) := by positivity
  have hden : 0 < ((n : ℚ) + 1) ^ 4 := by positivity
  unfold quarticStepRatio
  apply (div_le_iff₀ hden).2
  have hid :
      256 * ((n : ℚ) + 1) ^ 4 -
          ((4 * (n : ℚ) + 1) * (4 * (n : ℚ) + 2) *
            (4 * (n : ℚ) + 3) * (4 * (n : ℚ) + 4)) =
        8 * (48 * (n : ℚ) ^ 3 + 122 * (n : ℚ) ^ 2 +
          103 * (n : ℚ) + 29) := by
    ring
  have hnonneg :
      0 ≤ 8 * (48 * (n : ℚ) ^ 3 + 122 * (n : ℚ) ^ 2 +
        103 * (n : ℚ) + 29) := by
    positivity
  rw [← hid] at hnonneg
  linarith

theorem linearStepRatio_le_25 (n : ℕ) : linearStepRatio n ≤ 25 := by
  have hx : 0 ≤ (n : ℚ) := by positivity
  have hden : 0 < 1103 + 26390 * (n : ℚ) := by positivity
  unfold linearStepRatio
  apply (div_le_iff₀ hden).2
  have hid :
      25 * (1103 + 26390 * (n : ℚ)) -
          (1103 + 26390 * ((n : ℚ) + 1)) =
        82 + 633360 * (n : ℚ) := by
    ring
  have hnonneg : 0 ≤ 82 + 633360 * (n : ℚ) := by positivity
  rw [← hid] at hnonneg
  linarith

theorem quarticStepRatio_nonneg (n : ℕ) : 0 ≤ quarticStepRatio n := by
  unfold quarticStepRatio
  positivity

theorem linearStepRatio_nonneg (n : ℕ) : 0 ≤ linearStepRatio n := by
  unfold linearStepRatio
  positivity

theorem ramanujanStepRatio_le_q58 (n : ℕ) : ramanujanStepRatio n ≤ q58 := by
  have hden : 0 < (396 : ℚ) ^ 4 := by norm_num
  unfold ramanujanStepRatio q58
  apply (div_le_div_iff_of_pos_right hden).2
  calc
    quarticStepRatio n * linearStepRatio n ≤ 256 * linearStepRatio n :=
      mul_le_mul_of_nonneg_right (quarticStepRatio_le_256 n)
        (linearStepRatio_nonneg n)
    _ ≤ 256 * 25 :=
      mul_le_mul_of_nonneg_left (linearStepRatio_le_25 n) (by norm_num)
    _ = 6400 := by norm_num

theorem q58_nonneg : 0 ≤ q58 := by norm_num [q58]
theorem q58_lt_one : q58 < 1 := by norm_num [q58]

theorem recurrence_implies_q58_bound
    (term : ℕ → ℚ)
    (hterm : ∀ n, 0 ≤ term n)
    (hrec : ∀ n, term (n + 1) = ramanujanStepRatio n * term n) :
    ∀ n, term (n + 1) ≤ q58 * term n := by
  intro n
  rw [hrec n]
  exact mul_le_mul_of_nonneg_right (ramanujanStepRatio_le_q58 n) (hterm n)

end EnterpriseMath.PrecisionPi.N58RatioBound
