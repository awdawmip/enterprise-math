import EnterpriseMath.PrecisionPi.TernarySexticEqualOccupancy
import EnterpriseMath.PrecisionPi.TetrahedralWallisRatio

namespace EnterpriseMath.PrecisionPi.TetrahedralPrecisionMonotone

open SignatureBalanceRecurrence
open QuarticEqualOccupancy
open TernarySexticEqualOccupancy
open TetrahedralWallisRatio

/-- Exact rational part of the tetrahedral precision-pi sequence.  The
constant factor `sqrt(3/8)` is intentionally separated from this finite
algebraic layer. -/
def tetraScaled (n : ℕ) : ℚ :=
  equalOccupancyQ 4 n /
    ((n : ℚ) * equalOccupancyQ 6 n)

/-- Every positive-state equal-occupancy probability is positive. -/
theorem equalOccupancyQ_pos {k : ℕ} (hk : 1 ≤ k) (n : ℕ) :
    0 < equalOccupancyQ k n := by
  have hkq : (0 : ℚ) < k := by exact_mod_cast (show 0 < k by omega)
  unfold equalOccupancyQ
  positivity

/-- The rational tetrahedral precision factor is positive at every positive
depth. -/
theorem tetraScaled_pos {n : ℕ} (hn : 1 ≤ n) : 0 < tetraScaled n := by
  have hnq : (0 : ℚ) < n := by exact_mod_cast (show 0 < n by omega)
  unfold tetraScaled
  exact div_pos (equalOccupancyQ_pos (by norm_num) n)
    (mul_pos hnq (equalOccupancyQ_pos (by norm_num) n))

/-- The exact consecutive ratio of the finite `P₄/P₆` precision sequence is
the tetrahedral Wallis block. -/
theorem tetraScaled_succ (n : ℕ) (hn : 1 ≤ n) :
    tetraScaled (n + 1) = tetraScaled n * ratio n := by
  have hnq : (0 : ℚ) < n := by exact_mod_cast (show 0 < n by omega)
  have hn1q : ((n + 1 : ℕ) : ℚ) ≠ 0 := by positivity
  have hp6 : equalOccupancyQ 6 n ≠ 0 :=
    ne_of_gt (equalOccupancyQ_pos (by norm_num) n)
  simp only [tetraScaled]
  rw [equalOccupancyQ_four_succ, equalOccupancyQ_six_succ]
  unfold ratio numerator denominator
  norm_num [balanceStep, riseStep]
  field_simp [hp6, hn1q, ne_of_gt hnq]
  ring

/-- The rational tetrahedral precision sequence is strictly decreasing. -/
theorem tetraScaled_succ_lt (n : ℕ) (hn : 1 ≤ n) :
    tetraScaled (n + 1) < tetraScaled n := by
  rw [tetraScaled_succ n hn]
  have hpos := tetraScaled_pos hn
  have hratio : ratio (n : ℚ) < 1 := ratio_lt_one (by positivity)
  nlinarith [mul_lt_mul_of_pos_left hratio hpos]

/-- Natural-index antitonicity follows by iterating the strict one-step
contraction. -/
theorem tetraScaled_antitoneOn :
    AntitoneOn tetraScaled (Set.Ici 1) := by
  intro a ha b hb hab
  induction b, hab using Nat.le_induction with
  | base => rfl
  | succ b hab ih =>
      exact le_trans (le_of_lt (tetraScaled_succ_lt b (by omega))) ih

end EnterpriseMath.PrecisionPi.TetrahedralPrecisionMonotone
