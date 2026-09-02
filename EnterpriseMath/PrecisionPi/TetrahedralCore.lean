import EnterpriseMath.PrecisionPi.BalanceRecurrence
import EnterpriseMath.PrecisionPi.TetrahedralRatio

namespace EnterpriseMath.PrecisionPi

/-- The rational part of the tetrahedral precision approximant.  The positive
constant `sqrt(3/8)` is separated off so that strict monotonicity is proved in
exact arithmetic. -/
def tetrahedralCore (n : ℕ) : ℚ :=
  quarticBalance n / ((n : ℚ) * sexticBalance n)

/-- Every equal-occupancy coefficient for a nonempty alphabet is positive. -/
theorem equalOccupancy_pos (k n : ℕ) (hk : 0 < k) :
    0 < equalOccupancy k n := by
  unfold equalOccupancy
  positivity

/-- Every exact refinement step for a nonempty alphabet is positive. -/
theorem equalOccupancyStep_pos (k n : ℕ) (hk : 0 < k) :
    0 < equalOccupancyStep k n := by
  unfold equalOccupancyStep
  positivity

/-- Closed quartic refinement factor. -/
theorem equalOccupancyStep_four (n : ℕ) :
    equalOccupancyStep 4 n =
      let x : ℚ := n
      (2 * x + 1) * (4 * x + 1) * (4 * x + 3) /
        (32 * (x + 1) ^ 3) := by
  have hAsc :
      Nat.ascFactorial (4 * n + 1) 4 =
        (4 * n + 1) * (4 * n + 2) * (4 * n + 3) * (4 * n + 4) := by
    simp [Nat.ascFactorial_succ]
    ring
  dsimp [equalOccupancyStep]
  rw [hAsc]
  push_cast
  field_simp (disch := positivity)
  ring

/-- Closed sextic refinement factor. -/
theorem equalOccupancyStep_six (n : ℕ) :
    equalOccupancyStep 6 n =
      let x : ℚ := n
      (2 * x + 1) * (3 * x + 1) * (3 * x + 2) * (6 * x + 1) * (6 * x + 5) /
        (648 * (x + 1) ^ 5) := by
  have hAsc :
      Nat.ascFactorial (6 * n + 1) 6 =
        (6 * n + 1) * (6 * n + 2) * (6 * n + 3) *
          (6 * n + 4) * (6 * n + 5) * (6 * n + 6) := by
    simp [Nat.ascFactorial_succ]
    ring
  dsimp [equalOccupancyStep]
  rw [hAsc]
  push_cast
  field_simp (disch := positivity)
  ring

/-- The adjacent-depth contraction factor is exactly the quotient of the
quartic and sextic refinement steps, including the extra `n/(n+1)` depth
normalization. -/
theorem tetrahedralRatio_eq_steps (n : ℕ) :
    tetrahedralRatio n =
      equalOccupancyStep 4 n / equalOccupancyStep 6 n *
        ((n : ℚ) / (n + 1 : ℚ)) := by
  rw [equalOccupancyStep_four, equalOccupancyStep_six]
  dsimp [tetrahedralRatio]
  field_simp (disch := positivity)
  ring

/-- The rational tetrahedral precision core is positive at every positive
path depth. -/
theorem tetrahedralCore_pos {n : ℕ} (hn : 0 < n) :
    0 < tetrahedralCore n := by
  unfold tetrahedralCore
  have h4 := equalOccupancy_pos 4 n (by norm_num)
  have h6 := equalOccupancy_pos 6 n (by norm_num)
  positivity

/-- Exact adjacent-depth recurrence of the tetrahedral precision core. -/
theorem tetrahedralCore_succ {n : ℕ} (hn : 0 < n) :
    tetrahedralCore (n + 1) =
      tetrahedralCore n * tetrahedralRatio n := by
  have hnq : (n : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hn)
  have hn1q : ((n + 1 : ℕ) : ℚ) ≠ 0 := by
    positivity
  have h4 : quarticBalance n ≠ 0 :=
    ne_of_gt (equalOccupancy_pos 4 n (by norm_num))
  have h6 : sexticBalance n ≠ 0 :=
    ne_of_gt (equalOccupancy_pos 6 n (by norm_num))
  have hs4 : equalOccupancyStep 4 n ≠ 0 :=
    ne_of_gt (equalOccupancyStep_pos 4 n (by norm_num))
  have hs6 : equalOccupancyStep 6 n ≠ 0 :=
    ne_of_gt (equalOccupancyStep_pos 6 n (by norm_num))
  rw [tetrahedralCore, tetrahedralCore, quarticBalance_succ, sexticBalance_succ,
    tetrahedralRatio_eq_steps]
  field_simp [hnq, hn1q, h4, h6, hs4, hs6]
  push_cast
  ring

/-- Strict finite-resolution improvement: every positive-depth refinement
strictly lowers the tetrahedral precision core. -/
theorem tetrahedralCore_succ_lt {n : ℕ} (hn : 0 < n) :
    tetrahedralCore (n + 1) < tetrahedralCore n := by
  rw [tetrahedralCore_succ hn]
  have hcore := tetrahedralCore_pos hn
  have hratio := tetrahedralRatio_lt_one n
  calc
    tetrahedralCore n * tetrahedralRatio n < tetrahedralCore n * 1 :=
      mul_lt_mul_of_pos_left hratio hcore
    _ = tetrahedralCore n := by ring

end EnterpriseMath.PrecisionPi
