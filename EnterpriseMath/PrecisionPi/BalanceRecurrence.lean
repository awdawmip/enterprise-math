import EnterpriseMath.PrecisionPi.EqualOccupancy
import Mathlib.Data.Nat.Factorial.Basic

namespace EnterpriseMath.PrecisionPi

/-- One exact refinement step of the equal-occupancy coefficient. -/
def equalOccupancyStep (k n : ℕ) : ℚ :=
  (Nat.ascFactorial (k * n + 1) k : ℚ) /
    ((((n + 1 : ℕ) : ℚ) ^ k) * (k : ℚ) ^ k)

/-- The exact equal-occupancy recurrence for every nonempty alphabet.

This is the finite combinatorial recurrence that will later feed the
hypergeometric and gamma-ratio layers; it contains no occurrence of `Real.pi`.
-/
theorem equalOccupancy_succ (k n : ℕ) (hk : k ≠ 0) :
    equalOccupancy k (n + 1) =
      equalOccupancy k n * equalOccupancyStep k n := by
  have hkq : (k : ℚ) ≠ 0 := by
    exact_mod_cast hk
  have hnq : ((n + 1 : ℕ) : ℚ) ≠ 0 := by
    positivity
  have hfacnq : (Nat.factorial n : ℚ) ≠ 0 := by
    positivity
  have hfacNat := Nat.factorial_mul_ascFactorial (k * n) k
  have hfac :
      (Nat.factorial (k * n) : ℚ) *
          (Nat.ascFactorial (k * n + 1) k : ℚ) =
        (Nat.factorial (k * n + k) : ℚ) := by
    exact_mod_cast hfacNat
  have hkn : k * (n + 1) = k * n + k := by
    omega
  rw [equalOccupancy, equalOccupancy, equalOccupancyStep, hkn, ← hfac]
  simp only [Nat.factorial_succ, Nat.cast_mul, Nat.cast_add, Nat.cast_one, pow_add]
  field_simp [hkq, hnq, hfacnq]
  ring

/-- Quartic specialization of the exact recurrence. -/
theorem quarticBalance_succ (n : ℕ) :
    quarticBalance (n + 1) =
      quarticBalance n * equalOccupancyStep 4 n := by
  exact equalOccupancy_succ 4 n (by norm_num)

/-- Sextic specialization of the exact recurrence. -/
theorem sexticBalance_succ (n : ℕ) :
    sexticBalance (n + 1) =
      sexticBalance n * equalOccupancyStep 6 n := by
  exact equalOccupancy_succ 6 n (by norm_num)

end EnterpriseMath.PrecisionPi
