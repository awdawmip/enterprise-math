import Mathlib

namespace EnterpriseMath.PrecisionPi.PositiveSeriesAcceleration

/-- A finite inverse-period sum with an algebraic constant term. -/
def partialSum (A : ℝ) (term : ℕ → ℝ) (M : ℕ) : ℝ :=
  A + ∑ n in Finset.range (M + 1), term n

/-- Adding one transformed term changes the partial sum by exactly that term. -/
theorem partialSum_succ (A : ℝ) (term : ℕ → ℝ) (M : ℕ) :
    partialSum A term (M + 1) = partialSum A term M + term (M + 1) := by
  simp [partialSum, Finset.sum_range_succ]
  ring

/-- Positive transformed terms make the inverse-period partial sums strictly increase. -/
theorem partialSum_strict_step
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ)
    (hterm : 0 < term (M + 1)) :
    partialSum A term M < partialSum A term (M + 1) := by
  rw [partialSum_succ]
  linarith

/-- A positive constant term and nonnegative transformed terms give positive partial sums. -/
theorem partialSum_pos
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ)
    (hA : 0 < A) (hterm : ∀ n, 0 ≤ term n) :
    0 < partialSum A term M := by
  unfold partialSum
  exact add_pos_of_pos_of_nonneg hA (Finset.sum_nonneg fun i _ => hterm i)

/-- Reciprocal reverses a strict inequality between positive real numbers. -/
theorem one_div_strictAnti {a b : ℝ} (ha : 0 < a) (hab : a < b) :
    1 / b < 1 / a := by
  have hb : 0 < b := lt_trans ha hab
  apply (div_lt_div_iff₀ hb ha).2
  simpa using hab

/-- The finite accelerated approximation is the reciprocal partial inverse period. -/
def reciprocalApproximation (A : ℝ) (term : ℕ → ℝ) (M : ℕ) : ℝ :=
  1 / partialSum A term M

/-- Positive transformed terms make reciprocal approximants strictly decrease. -/
theorem reciprocalApproximation_strict_step
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ)
    (hA : 0 < A)
    (hterm_nonneg : ∀ n, 0 ≤ term n)
    (hterm_pos : 0 < term (M + 1)) :
    reciprocalApproximation A term (M + 1) <
      reciprocalApproximation A term M := by
  unfold reciprocalApproximation
  exact one_div_strictAnti
    (partialSum_pos A term M hA hterm_nonneg)
    (partialSum_strict_step A term M hterm_pos)

/--
If a positive finite inverse-period sum lies below the exact inverse period,
its reciprocal lies strictly above the exact period.
-/
theorem reciprocalApproximation_above_exact
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ) (inversePeriod : ℝ)
    (hA : 0 < A)
    (hterm_nonneg : ∀ n, 0 ≤ term n)
    (hbelow : partialSum A term M < inversePeriod) :
    1 / inversePeriod < reciprocalApproximation A term M := by
  unfold reciprocalApproximation
  exact one_div_strictAnti
    (partialSum_pos A term M hA hterm_nonneg)
    hbelow

/-- Exact reciprocal error identity used by certified tail estimates. -/
theorem reciprocal_error_identity
    {s t : ℝ} (hs : s ≠ 0) (ht : t ≠ 0) :
    1 / s - 1 / t = (t - s) / (s * t) := by
  field_simp
  ring

end EnterpriseMath.PrecisionPi.PositiveSeriesAcceleration
