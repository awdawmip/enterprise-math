import Mathlib

namespace EnterpriseMath.Precision

/-- The `n`-th multiplicative Wallis refinement factor. -/
def wallisStep (n : ℕ) : ℚ :=
  ((2 * (n : ℚ) + 2) ^ 2) /
    ((2 * (n : ℚ) + 1) * (2 * (n : ℚ) + 3))

/-- Exact rational Wallis partial products, with `W₀ = 1`. -/
def wallisPartial : ℕ → ℚ
  | 0 => 1
  | n + 1 => wallisPartial n * wallisStep n

/-- The elementary rational factor used for the decreasing upper envelope. -/
def wallisUpperFactor (n : ℕ) : ℚ :=
  (4 * (n : ℚ) + 2) / (4 * (n : ℚ) + 1)

/-- Target-free finite upper envelope `Qₙ = Wₙ (4n+2)/(4n+1)`. -/
def wallisUpper (n : ℕ) : ℚ :=
  wallisPartial n * wallisUpperFactor n

/-- Denominator of the exact one-step upper-envelope drop. -/
def wallisDropDen (n : ℕ) : ℚ :=
  (2 * (n : ℚ) + 1) ^ 2 * (4 * (n : ℚ) + 5)

/-- WSR-L09: each Wallis step is `1` plus one explicit positive rational correction. -/
theorem wallisStep_eq_one_add (n : ℕ) :
    wallisStep n =
      1 + 1 / ((2 * (n : ℚ) + 1) * (2 * (n : ℚ) + 3)) := by
  have h1 : (2 * (n : ℚ) + 1) ≠ 0 := by positivity
  have h3 : (2 * (n : ℚ) + 3) ≠ 0 := by positivity
  unfold wallisStep
  field_simp [h1, h3]
  ring

/-- Every finite Wallis refinement factor is strictly larger than one. -/
theorem one_lt_wallisStep (n : ℕ) : 1 < wallisStep n := by
  rw [wallisStep_eq_one_add]
  have h1 : 0 < (2 * (n : ℚ) + 1) := by positivity
  have h3 : 0 < (2 * (n : ℚ) + 3) := by positivity
  have : 0 < 1 / ((2 * (n : ℚ) + 1) * (2 * (n : ℚ) + 3)) := by positivity
  linarith

/-- Every finite Wallis partial product is positive. -/
theorem wallisPartial_pos (n : ℕ) : 0 < wallisPartial n := by
  induction n with
  | zero => norm_num [wallisPartial]
  | succ n ih =>
      rw [wallisPartial]
      exact mul_pos ih (lt_trans (by norm_num) (one_lt_wallisStep n))

/-- WSR-L10: the exact rational Wallis partial products are strictly increasing. -/
theorem wallisPartial_strictMono_step (n : ℕ) :
    wallisPartial n < wallisPartial (n + 1) := by
  rw [wallisPartial]
  have hp := wallisPartial_pos n
  have hs := one_lt_wallisStep n
  nlinarith [mul_pos hp (sub_pos.mpr hs)]

/-- The upper-envelope prefactor is `1 + 1/(4n+1)`. -/
theorem wallisUpperFactor_eq_one_add (n : ℕ) :
    wallisUpperFactor n = 1 + 1 / (4 * (n : ℚ) + 1) := by
  have h : (4 * (n : ℚ) + 1) ≠ 0 := by positivity
  unfold wallisUpperFactor
  field_simp [h]
  ring

/-- The exact finite gap between the upper envelope and the Wallis partial product. -/
theorem wallisUpper_sub_partial (n : ℕ) :
    wallisUpper n - wallisPartial n =
      wallisPartial n / (4 * (n : ℚ) + 1) := by
  unfold wallisUpper
  rw [wallisUpperFactor_eq_one_add]
  ring

/-- Every Wallis partial product lies strictly below its target-free rational upper envelope. -/
theorem wallisPartial_lt_upper (n : ℕ) : wallisPartial n < wallisUpper n := by
  rw [← sub_pos]
  rw [wallisUpper_sub_partial]
  exact div_pos (wallisPartial_pos n) (by positivity)

/-- The denominator governing the upper-envelope drop is strictly larger than one. -/
theorem one_lt_wallisDropDen (n : ℕ) : 1 < wallisDropDen n := by
  unfold wallisDropDen
  have hn : 0 ≤ (n : ℚ) := by positivity
  nlinarith [sq_nonneg (2 * (n : ℚ))]

/-- WSR-L11: exact one-step contraction law for the Wallis upper envelope. -/
theorem wallisUpper_succ (n : ℕ) :
    wallisUpper (n + 1) =
      wallisUpper n * (1 - 1 / wallisDropDen n) := by
  have h1 : (2 * (n : ℚ) + 1) ≠ 0 := by positivity
  have h3 : (2 * (n : ℚ) + 3) ≠ 0 := by positivity
  have h4n1 : (4 * (n : ℚ) + 1) ≠ 0 := by positivity
  have h4n5 : (4 * (n : ℚ) + 5) ≠ 0 := by positivity
  unfold wallisUpper wallisUpperFactor wallisDropDen
  rw [wallisPartial]
  unfold wallisStep
  field_simp [h1, h3, h4n1, h4n5]
  ring

/-- The one-step upper-envelope contraction factor lies strictly between zero and one. -/
theorem wallisDropFactor_pos (n : ℕ) :
    0 < 1 - 1 / wallisDropDen n := by
  have hd := one_lt_wallisDropDen n
  have hd0 : 0 < wallisDropDen n := lt_trans (by norm_num) hd
  have hfrac : 1 / wallisDropDen n < 1 := by
    exact (div_lt_one₀ hd0).2 (by norm_num)
  linarith

/-- The one-step upper-envelope contraction factor is strictly less than one. -/
theorem wallisDropFactor_lt_one (n : ℕ) :
    1 - 1 / wallisDropDen n < 1 := by
  have hd : 0 < wallisDropDen n := lt_trans (by norm_num) (one_lt_wallisDropDen n)
  have hfrac : 0 < 1 / wallisDropDen n := by positivity
  linarith

/-- The target-free Wallis upper envelope is positive. -/
theorem wallisUpper_pos (n : ℕ) : 0 < wallisUpper n := by
  unfold wallisUpper
  exact mul_pos (wallisPartial_pos n) (by
    rw [wallisUpperFactor_eq_one_add]
    positivity)

/-- WSR-L12: the target-free rational Wallis upper envelope is strictly decreasing. -/
theorem wallisUpper_strictAnti_step (n : ℕ) :
    wallisUpper (n + 1) < wallisUpper n := by
  rw [wallisUpper_succ]
  have hq := wallisUpper_pos n
  have hf := wallisDropFactor_lt_one n
  have hfp := wallisDropFactor_pos n
  nlinarith [mul_pos hq hfp, mul_pos hq (sub_pos.mpr hf)]

end EnterpriseMath.Precision
