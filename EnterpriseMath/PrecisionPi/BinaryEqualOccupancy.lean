import EnterpriseMath.PrecisionPi.TernarySexticEqualOccupancy

namespace EnterpriseMath.PrecisionPi.BinaryEqualOccupancy

open SignatureBalanceRecurrence
open QuarticEqualOccupancy
open TernarySexticEqualOccupancy

/-- Two-step factorial expansion. -/
theorem factorial_two_succ (n : ℕ) :
    Nat.factorial (2 * (n + 1)) =
      (2 * n + 2) * (2 * n + 1) * Nat.factorial (2 * n) := by
  calc
    Nat.factorial (2 * (n + 1)) = Nat.factorial (2 * n + 2) := by
      congr 1
      omega
    _ = (2 * n + 2) * Nat.factorial (2 * n + 1) := by
      rw [show 2 * n + 2 = (2 * n + 1) + 1 by omega, Nat.factorial_succ]
    _ = (2 * n + 2) * ((2 * n + 1) * Nat.factorial (2 * n)) := by
      rw [show 2 * n + 1 = (2 * n) + 1 by omega, Nat.factorial_succ]
    _ = (2 * n + 2) * (2 * n + 1) * Nat.factorial (2 * n) := by ring

/-- The exact binary probability obeys the two-state balance step. -/
theorem equalOccupancyQ_two_succ (n : ℕ) :
    equalOccupancyQ 2 (n + 1) =
      equalOccupancyQ 2 n * balanceStep 2 n := by
  have hfn : (Nat.factorial n : ℚ) ≠ 0 := by positivity
  have hf2n : (Nat.factorial (2 * n) : ℚ) ≠ 0 := by positivity
  have hn1 : ((n + 1 : ℕ) : ℚ) ≠ 0 := by positivity
  have hpow : (2 : ℚ) ^ (2 * n) ≠ 0 := by positivity
  unfold equalOccupancyQ
  rw [factorial_two_succ, Nat.factorial_succ]
  rw [show 2 * (n + 1) = 2 * n + 2 by omega, pow_add]
  norm_num [balanceStep, riseStep]
  field_simp [hfn, hf2n, hn1, hpow]
  ring

/-- Binary equal occupancy agrees with the recursive balance kernel. -/
theorem equalOccupancyQ_two_eq_balanceRec (n : ℕ) :
    equalOccupancyQ 2 n = balanceRec 2 n := by
  induction n with
  | zero => simp [equalOccupancyQ, balanceRec]
  | succ n ih => rw [equalOccupancyQ_two_succ, balanceRec, ih]

/-- Signature 2 is exactly the cube of binary equal occupancy. -/
theorem signature2_eq_binary_cubed (n : ℕ) :
    signature2 n = equalOccupancyQ 2 n ^ 3 := by
  rw [signature2_eq_balance_two, ← equalOccupancyQ_two_eq_balanceRec]

/-- Signature 3 is exactly binary times ternary equal occupancy. -/
theorem signature3_eq_binary_mul_ternary (n : ℕ) :
    signature3 n = equalOccupancyQ 2 n * equalOccupancyQ 3 n := by
  rw [signature3_eq_balance_two_mul_three,
    ← equalOccupancyQ_two_eq_balanceRec,
    ← equalOccupancyQ_three_eq_balanceRec]

end EnterpriseMath.PrecisionPi.BinaryEqualOccupancy
