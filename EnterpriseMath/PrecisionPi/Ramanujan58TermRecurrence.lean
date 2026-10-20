import EnterpriseMath.PrecisionPi.Ramanujan58AlgebraicApproximants
import EnterpriseMath.PrecisionPi.Ramanujan58RatioBound

namespace EnterpriseMath.PrecisionPi.Ramanujan58AlgebraicApproximants

open QuarticEqualOccupancy
open SignatureBalanceRecurrence

/-- The actual positive `N=58` summands obey the exact ratio encoded by
`Ramanujan58RatioBound.termStep`. -/
theorem term58_succ (n : ℕ) :
    term58 (n + 1) = term58 n *
      Ramanujan58RatioBound.termStep n := by
  have hresp : (1103 + 26390 * (n : ℚ)) ≠ 0 := by positivity
  unfold term58
  rw [equalOccupancyQ_four_succ, pow_succ]
  unfold response58 z58
  unfold Ramanujan58RatioBound.termStep
    Ramanujan58RatioBound.kernelStep
    Ramanujan58RatioBound.linearStep
    Ramanujan58RatioBound.balanceStep
  norm_num [balanceStep, riseStep]
  field_simp [hresp]
  ring

/-- Every actual consecutive summand is bounded by the uniform geometric
factor `25/99⁴`. -/
theorem term58_succ_lt_geometric (n : ℕ) :
    term58 (n + 1) < term58 n * ((25 : ℚ) / 99 ^ 4) := by
  rw [term58_succ]
  exact mul_lt_mul_of_pos_left
    (Ramanujan58RatioBound.termStep_lt_geometric (by positivity))
    (term58_pos n)

/-- Weak form convenient for iteration. -/
theorem term58_succ_le_geometric (n : ℕ) :
    term58 (n + 1) ≤ term58 n * ((25 : ℚ) / 99 ^ 4) :=
  le_of_lt (term58_succ_lt_geometric n)

/-- Iterated geometric domination of every later summand. -/
theorem term58_add_le_geometric (n r : ℕ) :
    term58 (n + r) ≤
      term58 n * (((25 : ℚ) / 99 ^ 4) ^ r) := by
  induction r with
  | zero => simp
  | succ r ih =>
      rw [Nat.add_succ, pow_succ]
      calc
        term58 (n + r + 1) ≤
            term58 (n + r) * ((25 : ℚ) / 99 ^ 4) :=
          term58_succ_le_geometric (n + r)
        _ ≤ (term58 n * (((25 : ℚ) / 99 ^ 4) ^ r)) *
              ((25 : ℚ) / 99 ^ 4) := by
          exact mul_le_mul_of_nonneg_right ih (by positivity)
        _ = term58 n * (((25 : ℚ) / 99 ^ 4) ^ (r + 1)) := by ring

end EnterpriseMath.PrecisionPi.Ramanujan58AlgebraicApproximants
