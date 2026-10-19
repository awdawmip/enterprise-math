import Mathlib

namespace EnterpriseMath.PrecisionPi.PositiveAccelerator

/-- Finite transformed inverse-period sum through depth `M`. -/
def partialSum (a : ℕ → ℝ) (M : ℕ) : ℝ :=
  ∑ n in Finset.range (M + 1), a n

/-- The next truncation adds exactly one new transformed term. -/
theorem partialSum_succ (a : ℕ → ℝ) (M : ℕ) :
    partialSum a (M + 1) = partialSum a M + a (M + 1) := by
  simp [partialSum, Finset.sum_range_succ]

/-- Nonnegative terms and a positive initial term make every truncation positive. -/
theorem partialSum_pos
    {a : ℕ → ℝ}
    (h0 : 0 < a 0)
    (ha : ∀ n, 0 ≤ a n)
    (M : ℕ) :
    0 < partialSum a M := by
  induction M with
  | zero => simpa [partialSum] using h0
  | succ M ih =>
      rw [partialSum_succ]
      exact add_pos_of_pos_of_nonneg ih (ha (M + 1))

/-- A positive next term makes the transformed inverse-period sum strictly increase. -/
theorem partialSum_strict_step
    {a : ℕ → ℝ} {M : ℕ}
    (hnext : 0 < a (M + 1)) :
    partialSum a M < partialSum a (M + 1) := by
  rw [partialSum_succ]
  exact lt_add_of_pos_right _ hnext

/-- Reciprocals of positive transformed partial sums strictly decrease. -/
theorem reciprocal_partialSum_strict_step
    {a : ℕ → ℝ} {M : ℕ}
    (hpos : 0 < partialSum a M)
    (hnext : 0 < a (M + 1)) :
    1 / partialSum a (M + 1) < 1 / partialSum a M := by
  apply one_div_lt_one_div_of_lt hpos
  exact partialSum_strict_step hnext

/-- Positive coefficients give a strictly decreasing algebraic precision hierarchy. -/
theorem reciprocal_partialSum_strictAnti
    {a : ℕ → ℝ}
    (ha : ∀ n, 0 < a n) :
    StrictAnti (fun M => 1 / partialSum a M) := by
  apply strictAnti_nat_of_succ_lt
  intro M
  apply reciprocal_partialSum_strict_step
  · exact partialSum_pos (ha 0) (fun n => (ha n).le) M
  · exact ha (M + 1)

/-- If a truncation lies below an exact positive inverse period, its reciprocal lies above
that period. -/
theorem reciprocal_above_period
    {S period : ℝ}
    (hS : 0 < S)
    (hperiod : 0 < period)
    (hbelow : S < 1 / period) :
    period < 1 / S := by
  have hinv : 1 / (1 / period) < 1 / S :=
    one_div_lt_one_div_of_lt hS hbelow
  simpa [hperiod.ne'] using hinv

/-- A positive-tail inverse-period identity yields decreasing upper approximants. -/
theorem finite_precision_step
    {a : ℕ → ℝ} {M : ℕ} {period : ℝ}
    (hperiod : 0 < period)
    (hpos : 0 < partialSum a M)
    (hnext : 0 < a (M + 1))
    (hbelow : partialSum a (M + 1) < 1 / period) :
    period < 1 / partialSum a (M + 1) ∧
      1 / partialSum a (M + 1) < 1 / partialSum a M := by
  have hposNext : 0 < partialSum a (M + 1) :=
    lt_trans hpos (partialSum_strict_step hnext)
  constructor
  · exact reciprocal_above_period hposNext hperiod hbelow
  · exact reciprocal_partialSum_strict_step hpos hnext

end EnterpriseMath.PrecisionPi.PositiveAccelerator
