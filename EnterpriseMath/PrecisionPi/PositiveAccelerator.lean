import Mathlib

namespace EnterpriseMath.PrecisionPi

open Filter Topology

noncomputable section

/-- A general positive-coefficient CM/Ramanujan accelerator term.

The coefficient sequence `a` is kept abstract so the order-theoretic layer is
independent of how the CM identity is constructed. -/
def acceleratorTerm
    (a : ℕ → ℝ) (A B z : ℝ) (n : ℕ) : ℝ :=
  (A + B * (n : ℝ)) * a n * z ^ n

/-- Finite transformed inverse-period sum through depth `M`. -/
def acceleratorPartialSum
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ) : ℝ :=
  ∑ n ∈ Finset.range (M + 1), acceleratorTerm a A B z n

/-- The finite accelerated precision value obtained by reciprocating the
truncated inverse-period sum. -/
def acceleratedPrecision
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ) : ℝ :=
  1 / acceleratorPartialSum a A B z M

/-- Exact adjacent-depth recurrence for transformed partial sums. -/
theorem acceleratorPartialSum_succ
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ) :
    acceleratorPartialSum a A B z (M + 1) =
      acceleratorPartialSum a A B z M +
        acceleratorTerm a A B z (M + 1) := by
  simp [acceleratorPartialSum, Finset.sum_range_succ, Nat.add_assoc]

/-- A positive next transformed term strictly increases the inverse-period
partial sum. -/
theorem acceleratorPartialSum_lt_succ
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ)
    (hterm : 0 < acceleratorTerm a A B z (M + 1)) :
    acceleratorPartialSum a A B z M <
      acceleratorPartialSum a A B z (M + 1) := by
  rw [acceleratorPartialSum_succ]
  linarith

/-- Positive transformed terms make the accelerated precision reciprocals
strictly decrease. -/
theorem acceleratedPrecision_succ_lt
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ)
    (hsum : 0 < acceleratorPartialSum a A B z M)
    (hterm : 0 < acceleratorTerm a A B z (M + 1)) :
    acceleratedPrecision a A B z (M + 1) <
      acceleratedPrecision a A B z M := by
  unfold acceleratedPrecision
  exact one_div_lt_one_div_of_lt hsum
    (acceleratorPartialSum_lt_succ a A B z M hterm)

/-- If every transformed term is positive and every partial sum is positive,
then the complete finite accelerated precision tower is strictly antitone. -/
theorem strictAnti_acceleratedPrecision
    (a : ℕ → ℝ) (A B z : ℝ)
    (hsum : ∀ M, 0 < acceleratorPartialSum a A B z M)
    (hterm : ∀ n, 0 < acceleratorTerm a A B z n) :
    StrictAnti (acceleratedPrecision a A B z) := by
  apply strictAnti_nat_of_succ_lt
  intro M
  exact acceleratedPrecision_succ_lt a A B z M (hsum M) (hterm (M + 1))

/-- Any positive inverse-period truncation lying below `1/π` reciprocates to a
finite precision value strictly above `π`. -/
theorem pi_lt_acceleratedPrecision_of_partial_lt
    (a : ℕ → ℝ) (A B z : ℝ) (M : ℕ)
    (hsum : 0 < acceleratorPartialSum a A B z M)
    (hbelow : acceleratorPartialSum a A B z M < 1 / Real.pi) :
    Real.pi < acceleratedPrecision a A B z M := by
  have hrecip := one_div_lt_one_div_of_lt hsum hbelow
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hcollapse : 1 / (1 / Real.pi) = Real.pi := by
    field_simp [hpi]
  simpa [acceleratedPrecision, hcollapse] using hrecip

/-- Once the transformed partial sums converge to the exact inverse period,
their reciprocals converge to `π`. -/
theorem tendsto_acceleratedPrecision_pi
    (a : ℕ → ℝ) (A B z : ℝ)
    (hseries : Tendsto (acceleratorPartialSum a A B z) atTop
      (𝓝 (1 / Real.pi))) :
    Tendsto (acceleratedPrecision a A B z) atTop (𝓝 Real.pi) := by
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hinv : 1 / Real.pi ≠ 0 := one_div_ne_zero hpi
  have hrecip :
      Tendsto (fun M : ℕ => (1 : ℝ) / acceleratorPartialSum a A B z M)
        atTop (𝓝 ((1 : ℝ) / (1 / Real.pi))) :=
    tendsto_const_nhds.div hseries hinv
  have hcollapse : (1 : ℝ) / (1 / Real.pi) = Real.pi := by
    field_simp [hpi]
  simpa [acceleratedPrecision, hcollapse] using hrecip

end

end EnterpriseMath.PrecisionPi
