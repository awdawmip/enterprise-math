import EnterpriseMath.PrecisionPi.QuarticEqualOccupancy

namespace EnterpriseMath.PrecisionPi.TernarySexticEqualOccupancy

open SignatureBalanceRecurrence
open QuarticEqualOccupancy

/-- Three-step factorial expansion. -/
theorem factorial_three_succ (n : ℕ) :
    Nat.factorial (3 * (n + 1)) =
      (3 * n + 3) * (3 * n + 2) * (3 * n + 1) *
        Nat.factorial (3 * n) := by
  calc
    Nat.factorial (3 * (n + 1)) = Nat.factorial (3 * n + 3) := by
      congr 1
      omega
    _ = (3 * n + 3) * Nat.factorial (3 * n + 2) := by
      rw [show 3 * n + 3 = (3 * n + 2) + 1 by omega, Nat.factorial_succ]
    _ = (3 * n + 3) * ((3 * n + 2) * Nat.factorial (3 * n + 1)) := by
      rw [show 3 * n + 2 = (3 * n + 1) + 1 by omega, Nat.factorial_succ]
    _ = (3 * n + 3) *
        ((3 * n + 2) * ((3 * n + 1) * Nat.factorial (3 * n))) := by
      rw [show 3 * n + 1 = (3 * n) + 1 by omega, Nat.factorial_succ]
    _ = (3 * n + 3) * (3 * n + 2) * (3 * n + 1) *
        Nat.factorial (3 * n) := by ring

/-- Six-step factorial expansion. -/
theorem factorial_six_succ (n : ℕ) :
    Nat.factorial (6 * (n + 1)) =
      (6 * n + 6) * (6 * n + 5) * (6 * n + 4) *
        (6 * n + 3) * (6 * n + 2) * (6 * n + 1) *
          Nat.factorial (6 * n) := by
  calc
    Nat.factorial (6 * (n + 1)) = Nat.factorial (6 * n + 6) := by
      congr 1
      omega
    _ = (6 * n + 6) * Nat.factorial (6 * n + 5) := by
      rw [show 6 * n + 6 = (6 * n + 5) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) * ((6 * n + 5) * Nat.factorial (6 * n + 4)) := by
      rw [show 6 * n + 5 = (6 * n + 4) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) *
        ((6 * n + 5) * ((6 * n + 4) * Nat.factorial (6 * n + 3))) := by
      rw [show 6 * n + 4 = (6 * n + 3) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) *
        ((6 * n + 5) * ((6 * n + 4) *
          ((6 * n + 3) * Nat.factorial (6 * n + 2)))) := by
      rw [show 6 * n + 3 = (6 * n + 2) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) *
        ((6 * n + 5) * ((6 * n + 4) *
          ((6 * n + 3) * ((6 * n + 2) * Nat.factorial (6 * n + 1))))) := by
      rw [show 6 * n + 2 = (6 * n + 1) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) *
        ((6 * n + 5) * ((6 * n + 4) *
          ((6 * n + 3) * ((6 * n + 2) *
            ((6 * n + 1) * Nat.factorial (6 * n)))))) := by
      rw [show 6 * n + 1 = (6 * n) + 1 by omega, Nat.factorial_succ]
    _ = (6 * n + 6) * (6 * n + 5) * (6 * n + 4) *
        (6 * n + 3) * (6 * n + 2) * (6 * n + 1) *
          Nat.factorial (6 * n) := by ring

/-- The exact ternary probability obeys the three-state balance step. -/
theorem equalOccupancyQ_three_succ (n : ℕ) :
    equalOccupancyQ 3 (n + 1) =
      equalOccupancyQ 3 n * balanceStep 3 n := by
  have hfn : (Nat.factorial n : ℚ) ≠ 0 := by positivity
  have hf3n : (Nat.factorial (3 * n) : ℚ) ≠ 0 := by positivity
  have hn1 : ((n + 1 : ℕ) : ℚ) ≠ 0 := by positivity
  have hpow : (3 : ℚ) ^ (3 * n) ≠ 0 := by positivity
  unfold equalOccupancyQ
  rw [factorial_three_succ, Nat.factorial_succ]
  rw [show 3 * (n + 1) = 3 * n + 3 by omega, pow_add]
  norm_num [balanceStep, riseStep]
  field_simp [hfn, hf3n, hn1, hpow]
  ring

/-- The exact sextic probability obeys the six-state balance step. -/
theorem equalOccupancyQ_six_succ (n : ℕ) :
    equalOccupancyQ 6 (n + 1) =
      equalOccupancyQ 6 n * balanceStep 6 n := by
  have hfn : (Nat.factorial n : ℚ) ≠ 0 := by positivity
  have hf6n : (Nat.factorial (6 * n) : ℚ) ≠ 0 := by positivity
  have hn1 : ((n + 1 : ℕ) : ℚ) ≠ 0 := by positivity
  have hpow : (6 : ℚ) ^ (6 * n) ≠ 0 := by positivity
  unfold equalOccupancyQ
  rw [factorial_six_succ, Nat.factorial_succ]
  rw [show 6 * (n + 1) = 6 * n + 6 by omega, pow_add]
  norm_num [balanceStep, riseStep]
  field_simp [hfn, hf6n, hn1, hpow]
  ring

/-- Ternary equal occupancy agrees with the recursive balance kernel. -/
theorem equalOccupancyQ_three_eq_balanceRec (n : ℕ) :
    equalOccupancyQ 3 n = balanceRec 3 n := by
  induction n with
  | zero => simp [equalOccupancyQ, balanceRec]
  | succ n ih => rw [equalOccupancyQ_three_succ, balanceRec, ih]

/-- Sextic equal occupancy agrees with the recursive balance kernel. -/
theorem equalOccupancyQ_six_eq_balanceRec (n : ℕ) :
    equalOccupancyQ 6 n = balanceRec 6 n := by
  induction n with
  | zero => simp [equalOccupancyQ, balanceRec]
  | succ n ih => rw [equalOccupancyQ_six_succ, balanceRec, ih]

/-- Signature 6 times ternary equal occupancy is exactly sextic equal
occupancy. -/
theorem signature6_mul_ternary_eq_sextic (n : ℕ) :
    signature6 n * equalOccupancyQ 3 n = equalOccupancyQ 6 n := by
  rw [equalOccupancyQ_three_eq_balanceRec,
    equalOccupancyQ_six_eq_balanceRec,
    signature6_mul_balance_three_eq_balance_six]

end EnterpriseMath.PrecisionPi.TernarySexticEqualOccupancy
