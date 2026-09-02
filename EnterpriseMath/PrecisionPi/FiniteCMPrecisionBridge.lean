import EnterpriseMath.PrecisionPi.TetrahedralPrecisionMonotone

namespace EnterpriseMath.PrecisionPi.FiniteCMPrecisionBridge

open QuarticEqualOccupancy
open TernarySexticEqualOccupancy
open TetrahedralPrecisionMonotone

/-- The rational precision factor reconstructs the quartic coefficient from
the sextic coefficient at every positive depth. -/
theorem tetraScaled_reconstructs_quartic {n : ℕ} (hn : 1 ≤ n) :
    (n : ℚ) * equalOccupancyQ 6 n * tetraScaled n =
      equalOccupancyQ 4 n := by
  have hnq : (n : ℚ) ≠ 0 := by
    exact_mod_cast (show n ≠ 0 by omega)
  have hp6 : equalOccupancyQ 6 n ≠ 0 :=
    ne_of_gt (equalOccupancyQ_pos (by norm_num) n)
  unfold tetraScaled
  field_simp [hnq, hp6]

/-- Quartic balance polynomial truncated after depth `M`. -/
def quarticPartial (z : ℚ) : ℕ → ℚ
  | 0 => equalOccupancyQ 4 0
  | M + 1 => quarticPartial z M +
      equalOccupancyQ 4 (M + 1) * z ^ (M + 1)

/-- The same truncation reconstructed from the sextic probability and the
slow tetrahedral precision factor. -/
def precisionLiftPartial (z : ℚ) : ℕ → ℚ
  | 0 => 1
  | M + 1 => precisionLiftPartial z M +
      ((M + 1 : ℕ) : ℚ) * equalOccupancyQ 6 (M + 1) *
        tetraScaled (M + 1) * z ^ (M + 1)

/-- Exact finite generating lift: every quartic truncation is already a
weighted transform of the slow precision sequence. -/
theorem quarticPartial_eq_precisionLiftPartial (z : ℚ) (M : ℕ) :
    quarticPartial z M = precisionLiftPartial z M := by
  induction M with
  | zero => simp [quarticPartial, precisionLiftPartial, equalOccupancyQ]
  | succ M ih =>
      simp only [quarticPartial, precisionLiftPartial, ih]
      rw [tetraScaled_reconstructs_quartic (by omega : 1 ≤ M + 1)]

/-- Finite Euler-weighted quartic CM functional. -/
def weightedQuarticPartial (A B z : ℚ) : ℕ → ℚ
  | 0 => A * equalOccupancyQ 4 0
  | M + 1 => weightedQuarticPartial A B z M +
      (A + B * ((M + 1 : ℕ) : ℚ)) *
        equalOccupancyQ 4 (M + 1) * z ^ (M + 1)

/-- The same finite CM functional written directly in precision-sequence
coordinates. -/
def weightedPrecisionPartial (A B z : ℚ) : ℕ → ℚ
  | 0 => A
  | M + 1 => weightedPrecisionPartial A B z M +
      (A + B * ((M + 1 : ℕ) : ℚ)) *
        ((M + 1 : ℕ) : ℚ) * equalOccupancyQ 6 (M + 1) *
          tetraScaled (M + 1) * z ^ (M + 1)

/-- Exact finite boundary-to-CM algebraic bridge before taking any analytic
limit. -/
theorem weightedQuartic_eq_weightedPrecision
    (A B z : ℚ) (M : ℕ) :
    weightedQuarticPartial A B z M =
      weightedPrecisionPartial A B z M := by
  induction M with
  | zero => simp [weightedQuarticPartial, weightedPrecisionPartial,
      equalOccupancyQ]
  | succ M ih =>
      simp only [weightedQuarticPartial, weightedPrecisionPartial, ih]
      rw [tetraScaled_reconstructs_quartic (by omega : 1 ≤ M + 1)]
      ring

end EnterpriseMath.PrecisionPi.FiniteCMPrecisionBridge
