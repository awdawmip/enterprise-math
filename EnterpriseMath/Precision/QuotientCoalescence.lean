import EnterpriseMath.Precision.QuotientBasin
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Arithmetic kernel for actual cross-divisor quotient-root coalescence.

If two different divisors `d < e` can place the same state `n` in the same
square-root cell `t`, then the shared root is cubically small relative to the
parent square basin:

`e*t^2 <= n < d*(t+1)^2  ->  t^3 < 2*(k+1)^2`.

No primality, parity, or real square root is used. -/
theorem divisor_collision_cubic_kernel
    {k n d e t : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (hnUpper : n < (k + 1) ^ 2)
    (hLower : e * t ^ 2 ≤ n)
    (hUpper : n < d * (t + 1) ^ 2) :
    t ^ 3 < 2 * (k + 1) ^ 2 := by
  have hSucc : d + 1 ≤ e := by omega
  have hStep : (d + 1) * t ^ 2 < d * (t + 1) ^ 2 := by
    calc
      (d + 1) * t ^ 2 ≤ e * t ^ 2 := Nat.mul_le_mul_right (t ^ 2) hSucc
      _ ≤ n := hLower
      _ < d * (t + 1) ^ 2 := hUpper
  have hQuad : t ^ 2 < d * (2 * t + 1) := by
    nlinarith [hStep]
  have htLe : t ≤ 2 * d := by
    by_contra hnot
    have htGe : 2 * d + 1 ≤ t := by omega
    nlinarith [hQuad]
  have htLt : t < 2 * e := by omega
  by_cases htZero : t = 0
  · subst t
    simp
  · have htPos : 0 < t := Nat.pos_of_ne_zero htZero
    have hMul0 : t * t ^ 2 < (2 * e) * t ^ 2 :=
      Nat.mul_lt_mul_of_pos_right htLt (pow_pos htPos 2)
    have hMul : t ^ 3 < 2 * e * t ^ 2 := by
      simpa [pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul0
    nlinarith [hMul, hLower, hnUpper]

/-- P018 discovery theorem: if two distinct natural divisors give the same
actual quotient-root on one complete square basin, the common root lies below
the cubic coalescence scale.

This is stronger than candidate-channel overlap bounds because it uses the exact
root interval on the observed state. -/
theorem square_basin_distinct_divisor_root_collision_cubic
    {k n d e : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (_hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2)
    (hroot : root 2 (n / d) = root 2 (n / e)) :
    (root 2 (n / d)) ^ 3 < 2 * (k + 1) ^ 2 := by
  let t := root 2 (n / d)
  have hd0 : 0 < d := by omega
  have he0 : 0 < e := by omega
  have hRootE : root 2 (n / e) = t := by
    dsimp [t]
    exact hroot.symm
  have hPowE0 : (root 2 (n / e)) ^ 2 ≤ n / e := by
    exact Nat.pow_nthRoot_le (Or.inl (by decide))
  have hPowE : t ^ 2 ≤ n / e := by
    simpa [hRootE] using hPowE0
  have hLowerMul : t ^ 2 * e ≤ n :=
    (Nat.le_div_iff_mul_le he0).1 hPowE
  have hLower : e * t ^ 2 ≤ n := by
    simpa [Nat.mul_comm] using hLowerMul
  have hQuotUpper : n / d < (t + 1) ^ 2 := by
    dsimp [t]
    exact Nat.lt_pow_nthRoot_add_one (by decide) (n / d)
  have hUpperMul : n < (t + 1) ^ 2 * d :=
    (Nat.div_lt_iff_lt_mul hd0).1 hQuotUpper
  have hUpper : n < d * (t + 1) ^ 2 := by
    simpa [Nat.mul_comm] using hUpperMul
  exact divisor_collision_cubic_kernel hd hde hnUpper hLower hUpper

/-- Exact integer cubic horizon corollary.

Any actual collision root is at most
`R_3(2*(k+1)^2 - 1)`. -/
theorem square_basin_distinct_divisor_root_collision_horizon
    {k n d e : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2)
    (hroot : root 2 (n / d) = root 2 (n / e)) :
    root 2 (n / d) ≤ root 3 (2 * (k + 1) ^ 2 - 1) := by
  have hCubic := square_basin_distinct_divisor_root_collision_cubic
    (k := k) (n := n) (d := d) (e := e)
    hd hde hnLower hnUpper hroot
  have hLe : (root 2 (n / d)) ^ 3 ≤ 2 * (k + 1) ^ 2 - 1 := by
    omega
  exact (Nat.le_nthRoot_iff (n := 3) (by decide)).2 hLe

/-- From parent root scale `k >= 4`, the cubic collision horizon itself is
strictly below `k`.

Thus cross-divisor quotient-root coalescence is not merely bounded by a
sublinear asymptotic expression: it is a genuinely reductive scale map on all
nontrivial parent scales beyond the finite base cases. -/
theorem cubic_coalescence_horizon_lt_parent
    {k : ℕ} (hk : 4 ≤ k) :
    root 3 (2 * (k + 1) ^ 2 - 1) < k := by
  have hArgBound : 2 * (k + 1) ^ 2 ≤ k ^ 3 := by
    nlinarith
  have hArgLt : 2 * (k + 1) ^ 2 - 1 < k ^ 3 := by
    omega
  by_contra hnot
  have hkRoot : k ≤ root 3 (2 * (k + 1) ^ 2 - 1) := by
    omega
  have hkPow : k ^ 3 ≤ (root 3 (2 * (k + 1) ^ 2 - 1)) ^ 3 :=
    Nat.pow_le_pow_left hkRoot 3
  have hRootPow : (root 3 (2 * (k + 1) ^ 2 - 1)) ^ 3 ≤
      2 * (k + 1) ^ 2 - 1 := by
    exact Nat.pow_nthRoot_le (Or.inl (by decide))
  have hRootPowLt : (root 3 (2 * (k + 1) ^ 2 - 1)) ^ 3 < k ^ 3 :=
    lt_of_le_of_lt hRootPow hArgLt
  exact (not_lt_of_ge hkPow) hRootPowLt

/-- Every actual distinct-divisor root collision strictly descends the parent
square-root scale once `k >= 4`.

Together with T111 path flatness, this gives a well-founded collision skeleton:
any two factor-extraction paths with different total divisors can merge only
strictly below the current parent root scale. -/
theorem square_basin_distinct_divisor_root_collision_strict_descent
    {k n d e : ℕ}
    (hk : 4 ≤ k)
    (hd : 2 ≤ d) (hde : d < e)
    (hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2)
    (hroot : root 2 (n / d) = root 2 (n / e)) :
    root 2 (n / d) < k := by
  exact lt_of_le_of_lt
    (square_basin_distinct_divisor_root_collision_horizon
      hd hde hnLower hnUpper hroot)
    (cubic_coalescence_horizon_lt_parent hk)

end EnterpriseMath.Precision
