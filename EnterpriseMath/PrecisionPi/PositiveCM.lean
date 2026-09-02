import EnterpriseMath.PrecisionPi.CMFiniteTransform
import EnterpriseMath.PrecisionPi.PositiveAccelerator

namespace EnterpriseMath.PrecisionPi.PositiveCM

open CMFiniteTransform PositiveAccelerator

/-- One positive-coefficient CM transformed term. -/
def cmTerm (A B z : ℝ) (c : ℕ → ℝ) (n : ℕ) : ℝ :=
  (A + B * (n : ℝ)) * c n * z ^ n

/-- Positivity hypotheses for a CM chart force every transformed term to be positive. -/
theorem cmTerm_pos
    {A B z : ℝ} {c : ℕ → ℝ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n : ℕ, 0 < c n) :
    ∀ n : ℕ, 0 < cmTerm A B z c n := by
  intro n
  have hlinear : 0 < A + B * (n : ℝ) := by positivity
  exact mul_pos (mul_pos hlinear (hc n)) (pow_pos hz n)

/-- The CM partial sum is the generic positive partial sum of its transformed terms. -/
theorem cmPartial_eq_partialSum
    (A B z : ℝ) (c : ℕ → ℝ) (M : ℕ) :
    cmPartial A B c z M = partialSum (cmTerm A B z c) M := by
  rfl

/-- At a positive CM chart, reciprocal truncations strictly decrease. -/
theorem reciprocal_cmPartial_strictAnti
    {A B z : ℝ} {c : ℕ → ℝ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n : ℕ, 0 < c n) :
    StrictAnti (fun M => 1 / cmPartial A B c z M) := by
  rw [funext fun M => cmPartial_eq_partialSum A B z c M]
  exact reciprocal_partialSum_strictAnti (cmTerm_pos hA hB hz hc)

/-- A finite positive CM sum below the exact inverse period gives an upper period approximant. -/
theorem cm_reciprocal_above_period
    {A B z period : ℝ} {c : ℕ → ℝ} {M : ℕ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n : ℕ, 0 < c n)
    (hperiod : 0 < period)
    (hbelow : cmPartial A B c z M < 1 / period) :
    period < 1 / cmPartial A B c z M := by
  apply reciprocal_above_period
  · rw [cmPartial_eq_partialSum]
    exact partialSum_pos
      (cmTerm_pos hA hB hz hc 0)
      (fun n => (cmTerm_pos hA hB hz hc n).le) M
  · exact hperiod
  · exact hbelow

end EnterpriseMath.PrecisionPi.PositiveCM
