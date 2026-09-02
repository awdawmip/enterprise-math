import EnterpriseMath.PrecisionPi.TetrahedralPrecision

namespace EnterpriseMath.PrecisionPi

noncomputable section

/-- The reciprocal square-root normalizations used by the four-state/six-state
precision ratio multiply to one. -/
theorem sqrt_eight_thirds_mul_sqrt_three_eighths :
    Real.sqrt (8 / 3 : ℝ) * Real.sqrt (3 / 8 : ℝ) = 1 := by
  have h83 : (Real.sqrt (8 / 3 : ℝ)) ^ 2 = 8 / 3 := by
    rw [Real.sq_sqrt]
    norm_num
  have h38 : (Real.sqrt (3 / 8 : ℝ)) ^ 2 = 3 / 8 := by
    rw [Real.sq_sqrt]
    norm_num
  have hnonneg :
      0 ≤ Real.sqrt (8 / 3 : ℝ) * Real.sqrt (3 / 8 : ℝ) := by
    positivity
  have hsq :
      (Real.sqrt (8 / 3 : ℝ) * Real.sqrt (3 / 8 : ℝ)) ^ 2 = 1 := by
    rw [mul_pow, h83, h38]
    norm_num
  nlinarith

/-- Multiplying the finite precision ratio by its six-state depth weight
recovers the normalized four-state coefficient exactly. -/
theorem tetrahedralPrecision_weighted {n : ℕ} (hn : 0 < n) :
    ((n : ℝ) * equalOccupancyReal 6 n) * tetrahedralPrecision n =
      Real.sqrt (3 / 8 : ℝ) * equalOccupancyReal 4 n := by
  unfold tetrahedralPrecision
  have hnR : (n : ℝ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hn)
  have h6 : equalOccupancyReal 6 n ≠ 0 := by
    unfold equalOccupancyReal
    positivity
  field_simp [hnR, h6] <;> ring

/-- Coefficient-level generating lift: the quartic Ramanujan kernel is the
six-state balance weight multiplied by the finite tetrahedral precision value.
This is the exact bridge from the slow precision sequence to the quartic
hypergeometric coefficient sequence. -/
theorem equalOccupancyReal_four_eq_precisionCoefficient
    {n : ℕ} (hn : 0 < n) :
    equalOccupancyReal 4 n =
      Real.sqrt (8 / 3 : ℝ) *
        (((n : ℝ) * equalOccupancyReal 6 n) * tetrahedralPrecision n) := by
  have hw := tetrahedralPrecision_weighted hn
  calc
    equalOccupancyReal 4 n =
        (Real.sqrt (8 / 3 : ℝ) * Real.sqrt (3 / 8 : ℝ)) *
          equalOccupancyReal 4 n := by
            rw [sqrt_eight_thirds_mul_sqrt_three_eighths]
            ring
    _ = Real.sqrt (8 / 3 : ℝ) *
        (Real.sqrt (3 / 8 : ℝ) * equalOccupancyReal 4 n) := by ring
    _ = Real.sqrt (8 / 3 : ℝ) *
        (((n : ℝ) * equalOccupancyReal 6 n) * tetrahedralPrecision n) :=
      congrArg (fun t : ℝ => Real.sqrt (8 / 3 : ℝ) * t) hw.symm

/-- Positive-degree quartic generating-function term. -/
noncomputable def quarticPositiveTerm (z : ℝ) (j : ℕ) : ℝ :=
  equalOccupancyReal 4 (j + 1) * z ^ (j + 1)

/-- The same term expressed through the finite tetrahedral precision sequence. -/
noncomputable def precisionLiftTerm (z : ℝ) (j : ℕ) : ℝ :=
  Real.sqrt (8 / 3 : ℝ) *
      ((((j + 1 : ℕ) : ℝ) * equalOccupancyReal 6 (j + 1)) *
        tetrahedralPrecision (j + 1)) *
    z ^ (j + 1)

/-- The quartic coefficient term and its precision-lift expression agree at
every positive degree. -/
theorem quarticPositiveTerm_eq_precisionLiftTerm (z : ℝ) (j : ℕ) :
    quarticPositiveTerm z j = precisionLiftTerm z j := by
  unfold quarticPositiveTerm precisionLiftTerm
  rw [equalOccupancyReal_four_eq_precisionCoefficient (Nat.succ_pos j)]

/-- Finite positive-degree quartic partial sum. -/
noncomputable def quarticPositivePartial (z : ℝ) (M : ℕ) : ℝ :=
  ∑ j ∈ Finset.range M, quarticPositiveTerm z j

/-- Finite positive-degree precision-lift partial sum. -/
noncomputable def precisionLiftPartial (z : ℝ) (M : ℕ) : ℝ :=
  ∑ j ∈ Finset.range M, precisionLiftTerm z j

/-- Every finite truncation of the quartic generating function is exactly the
corresponding weighted truncation of the slow precision sequence. -/
theorem quarticPositivePartial_eq_precisionLiftPartial (z : ℝ) (M : ℕ) :
    quarticPositivePartial z M = precisionLiftPartial z M := by
  unfold quarticPositivePartial precisionLiftPartial
  apply Finset.sum_congr rfl
  intro j hj
  exact quarticPositiveTerm_eq_precisionLiftTerm z j

/-- Including the constant coefficient `1`, the two finite generating lifts
remain exactly equal. -/
theorem quarticGeneratingLift_partial (z : ℝ) (M : ℕ) :
    1 + quarticPositivePartial z M = 1 + precisionLiftPartial z M := by
  rw [quarticPositivePartial_eq_precisionLiftPartial]

end

end EnterpriseMath.PrecisionPi
