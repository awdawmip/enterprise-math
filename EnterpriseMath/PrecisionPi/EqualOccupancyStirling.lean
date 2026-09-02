import EnterpriseMath.PrecisionPi.EqualOccupancy
import Mathlib.Analysis.SpecialFunctions.Stirling

namespace EnterpriseMath.PrecisionPi

/-- Real-valued presentation of the finite equal-occupancy probability. -/
noncomputable def equalOccupancyReal (k n : ℕ) : ℝ :=
  (Nat.factorial (k * n) : ℝ) /
    ((Nat.factorial n : ℝ) ^ k * (k : ℝ) ^ (k * n))

/-- The rational and real presentations of equal occupancy agree exactly. -/
theorem equalOccupancyReal_eq_cast (k n : ℕ) :
    equalOccupancyReal k n = (equalOccupancy k n : ℝ) := by
  norm_num [equalOccupancyReal, equalOccupancy]

/-- Exact Stirling factorization of finite equal occupancy.

This is an identity at every positive finite depth, not an asymptotic formula.
All exponential factors cancel before any limit is taken. -/
theorem equalOccupancyReal_eq_stirling
    (k n : ℕ) (hk : 0 < k) (hn : 0 < n) :
    equalOccupancyReal k n =
      Stirling.stirlingSeq (k * n) / Stirling.stirlingSeq n ^ k *
        (Real.sqrt (2 * (k * n : ℕ) : ℝ) /
          Real.sqrt (2 * n : ℝ) ^ k) := by
  have hbase :
      ((k * n : ℕ) : ℝ) / Real.exp 1 =
        (k : ℝ) * ((n : ℝ) / Real.exp 1) := by
    push_cast
    ring
  have hpowN :
      (((n : ℝ) ^ n / Real.exp 1 ^ n) ^ k) =
        (n : ℝ) ^ (k * n) / Real.exp 1 ^ (k * n) := by
    rw [div_pow, ← pow_mul, ← pow_mul, Nat.mul_comm n k]
  unfold equalOccupancyReal Stirling.stirlingSeq
  rw [hbase]
  simp_rw [div_pow, mul_pow]
  rw [hpowN]
  simp_rw [div_pow]
  field_simp (disch := positivity)
  ring

end EnterpriseMath.PrecisionPi
