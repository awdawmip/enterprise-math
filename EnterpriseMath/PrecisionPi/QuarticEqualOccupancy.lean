import EnterpriseMath.PrecisionPi.SignatureBalanceRecurrence

namespace EnterpriseMath.PrecisionPi.QuarticEqualOccupancy

open SignatureBalanceRecurrence

/-- Exact equal-occupancy probability for a uniform finite `k`-state word. -/
def equalOccupancyQ (k n : ℕ) : ℚ :=
  (Nat.factorial (k * n) : ℚ) /
    ((Nat.factorial n : ℚ) ^ k * (k : ℚ) ^ (k * n))

/-- The zero-depth equal-occupancy probability is one. -/
theorem equalOccupancyQ_zero (k : ℕ) : equalOccupancyQ k 0 = 1 := by
  simp [equalOccupancyQ]

/-- Four-step factorial expansion. -/
theorem factorial_four_succ (n : ℕ) :
    Nat.factorial (4 * (n + 1)) =
      (4 * n + 4) * (4 * n + 3) * (4 * n + 2) * (4 * n + 1) *
        Nat.factorial (4 * n) := by
  calc
    Nat.factorial (4 * (n + 1)) = Nat.factorial (4 * n + 4) := by
      congr 1
      omega
    _ = (4 * n + 4) * Nat.factorial (4 * n + 3) := by
      rw [show 4 * n + 4 = (4 * n + 3) + 1 by omega, Nat.factorial_succ]
    _ = (4 * n + 4) * ((4 * n + 3) * Nat.factorial (4 * n + 2)) := by
      rw [show 4 * n + 3 = (4 * n + 2) + 1 by omega, Nat.factorial_succ]
    _ = (4 * n + 4) *
        ((4 * n + 3) * ((4 * n + 2) * Nat.factorial (4 * n + 1))) := by
      rw [show 4 * n + 2 = (4 * n + 1) + 1 by omega, Nat.factorial_succ]
    _ = (4 * n + 4) *
        ((4 * n + 3) * ((4 * n + 2) *
          ((4 * n + 1) * Nat.factorial (4 * n)))) := by
      rw [show 4 * n + 1 = (4 * n) + 1 by omega, Nat.factorial_succ]
    _ = (4 * n + 4) * (4 * n + 3) * (4 * n + 2) * (4 * n + 1) *
        Nat.factorial (4 * n) := by ring

/-- The exact quartic probability obeys the residue-channel balance step. -/
theorem equalOccupancyQ_four_succ (n : ℕ) :
    equalOccupancyQ 4 (n + 1) =
      equalOccupancyQ 4 n * balanceStep 4 n := by
  have hfn : (Nat.factorial n : ℚ) ≠ 0 := by positivity
  have hf4n : (Nat.factorial (4 * n) : ℚ) ≠ 0 := by positivity
  have hn1 : ((n + 1 : ℕ) : ℚ) ≠ 0 := by positivity
  have hpow : (4 : ℚ) ^ (4 * n) ≠ 0 := by positivity
  unfold equalOccupancyQ
  rw [factorial_four_succ, Nat.factorial_succ]
  rw [show 4 * (n + 1) = 4 * n + 4 by omega, pow_add]
  norm_num [balanceStep, riseStep]
  field_simp [hfn, hf4n, hn1, hpow]
  ring

/-- The finite quartic equal-occupancy probability is exactly the recursively
constructed four-state balance kernel. -/
theorem equalOccupancyQ_four_eq_balanceRec (n : ℕ) :
    equalOccupancyQ 4 n = balanceRec 4 n := by
  induction n with
  | zero => simp [equalOccupancyQ_zero, balanceRec]
  | succ n ih =>
      rw [equalOccupancyQ_four_succ, balanceRec, ih]

/-- Hence the classical signature-4 coefficient is exactly the finite
four-state equal-occupancy probability. -/
theorem signature4_eq_equalOccupancyQ_four (n : ℕ) :
    signature4 n = equalOccupancyQ 4 n := by
  rw [signature4_eq_balance_four, ← equalOccupancyQ_four_eq_balanceRec]

end EnterpriseMath.PrecisionPi.QuarticEqualOccupancy
