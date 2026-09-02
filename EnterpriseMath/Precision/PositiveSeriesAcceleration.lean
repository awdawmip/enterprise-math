import Mathlib

namespace EnterpriseMath.PrecisionPi.PositiveSeriesAcceleration

def partialSum (A : ℝ) (term : ℕ → ℝ) (M : ℕ) : ℝ :=
  A + ∑ n in Finset.range (M + 1), term n

theorem partialSum_succ (A : ℝ) (term : ℕ → ℝ) (M : ℕ) :
    partialSum A term (M + 1) = partialSum A term M + term (M + 1) := by
  simp [partialSum, Finset.sum_range_succ]
  ring

theorem partialSum_strict_step
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ)
    (hterm : 0 < term (M + 1)) :
    partialSum A term M < partialSum A term (M + 1) := by
  rw [partialSum_succ]
  linarith

theorem partialSum_pos
    (A : ℝ) (term : ℕ → ℝ) (M : ℕ)
    (hA : 0 < A) (hterm : ∀ n, 0 ≤ term n) :
    0 < partialSum A term M := by
  unfold partialSum
  exact add_pos_of_pos_of_nonneg hA (Finset.sum_nonneg fun i _ => hterm i)

theorem one_div_strictAnti {a b : ℝ} (ha : 0 < a) (hab : a < b) :
    1 / b < 1 / a := by
  have hb : 0 < b := lt_trans ha hab
  apply (div_lt_div_iff₀ hb ha).2
  simpa using hab

def reciprocalApproximation (A : ℝ) (term : ℕ → ℝ) (M : ℕ) : ℝ :=
  1 / partialSum A term M

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

theorem reciprocal_error_identity
    {s t : ℝ} (hs : s ≠ 0) (ht : t ≠ 0) :
    1 / s - 1 / t = (t - s) / (s * t) := by
  field_simp [hs, ht]
  ring

end EnterpriseMath.PrecisionPi.PositiveSeriesAcceleration
