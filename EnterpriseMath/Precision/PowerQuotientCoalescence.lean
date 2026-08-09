import EnterpriseMath.Precision.QuotientBasin
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Discrete one-step Bernoulli upper bound. -/
theorem pow_succ_le_pow_add_tangent (t r : ℕ) :
    (t + 1) ^ r ≤ t ^ r + r * (t + 1) ^ (r - 1) := by
  induction r with
  | zero => simp
  | succ r ih =>
      calc
        (t + 1) ^ (r + 1) = (t + 1) * (t + 1) ^ r := by rw [pow_succ']
        _ ≤ (t + 1) * (t ^ r + r * (t + 1) ^ (r - 1)) :=
          Nat.mul_le_mul_left (t + 1) ih
        _ = t ^ (r + 1) + t ^ r + r * (t + 1) ^ r := by
          cases r with
          | zero => simp
          | succ r =>
              simp only [Nat.succ_sub_one, pow_succ']
              ring
        _ ≤ t ^ (r + 1) + (t + 1) ^ r + r * (t + 1) ^ r := by
          gcongr
          omega
        _ = t ^ (r + 1) + (r + 1) * (t + 1) ^ r := by ring

/-- Gap-one collision scale bound. -/
theorem divisor_collision_root_scale
    {d t s : ℕ}
    (hcollision : (d + 1) * t ^ (s + 1) < d * (t + 1) ^ (s + 1)) :
    t + 1 < (s + 1) * (d + 1) := by
  by_contra hnot
  have hCoeff' : (s + 1) * (d + 1) ≤ t + 1 := by omega
  have hCoeff : (d + 1) * (s + 1) ≤ t + 1 := by
    simpa [Nat.mul_comm] using hCoeff'
  have hStep := pow_succ_le_pow_add_tangent t (s + 1)
  have hScaled :
      (d + 1) * (t + 1) ^ (s + 1) ≤
        (d + 1) * t ^ (s + 1) +
          (d + 1) * ((s + 1) * (t + 1) ^ s) := by
    calc
      (d + 1) * (t + 1) ^ (s + 1)
          ≤ (d + 1) * (t ^ (s + 1) + (s + 1) * (t + 1) ^ s) :=
            Nat.mul_le_mul_left (d + 1) hStep
      _ = (d + 1) * t ^ (s + 1) +
          (d + 1) * ((s + 1) * (t + 1) ^ s) := by ring
  have hError :
      (d + 1) * ((s + 1) * (t + 1) ^ s) ≤ (t + 1) ^ (s + 1) := by
    calc
      (d + 1) * ((s + 1) * (t + 1) ^ s)
          = ((d + 1) * (s + 1)) * (t + 1) ^ s := by ring
      _ ≤ (t + 1) * (t + 1) ^ s :=
        Nat.mul_le_mul_right ((t + 1) ^ s) hCoeff
      _ = (t + 1) ^ (s + 1) := by rw [← pow_succ']
  have hCombined :
      (d + 1) * (t + 1) ^ (s + 1) ≤
        (d + 1) * t ^ (s + 1) + (t + 1) ^ (s + 1) :=
    le_trans hScaled (Nat.add_le_add_left hError ((d + 1) * t ^ (s + 1)))
  have hCap : d * (t + 1) ^ (s + 1) ≤ (d + 1) * t ^ (s + 1) := by
    have hCancel :
        d * (t + 1) ^ (s + 1) + (t + 1) ^ (s + 1) ≤
          (d + 1) * t ^ (s + 1) + (t + 1) ^ (s + 1) := by
      calc
        d * (t + 1) ^ (s + 1) + (t + 1) ^ (s + 1)
            = (d + 1) * (t + 1) ^ (s + 1) := by ring
        _ ≤ (d + 1) * t ^ (s + 1) + (t + 1) ^ (s + 1) := hCombined
    omega
  omega

/-- All-power cross-divisor quotient-root coalescence law. -/
theorem power_basin_distinct_divisor_root_collision
    {p k n d e s : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (hnUpper : n < (k + 1) ^ p)
    (hroot : root (s + 1) (n / d) = root (s + 1) (n / e)) :
    (root (s + 1) (n / d)) ^ (s + 2) < (s + 1) * (k + 1) ^ p := by
  let t := root (s + 1) (n / d)
  change t ^ (s + 2) < (s + 1) * (k + 1) ^ p
  have hd0 : 0 < d := by omega
  have he0 : 0 < e := by omega
  have hRootE : root (s + 1) (n / e) = t := by
    dsimp [t]
    exact hroot.symm
  have hPowE0 : (root (s + 1) (n / e)) ^ (s + 1) ≤ n / e := by
    exact Nat.pow_nthRoot_le (Or.inl (by omega))
  have hPowE : t ^ (s + 1) ≤ n / e := by simpa [hRootE] using hPowE0
  have hLowerMul : t ^ (s + 1) * e ≤ n :=
    (Nat.le_div_iff_mul_le he0).1 hPowE
  have hLower : e * t ^ (s + 1) ≤ n := by simpa [Nat.mul_comm] using hLowerMul
  have hQuotUpper : n / d < (t + 1) ^ (s + 1) := by
    dsimp [t]
    exact Nat.lt_pow_nthRoot_add_one (by omega) (n / d)
  have hUpperMul : n < (t + 1) ^ (s + 1) * d :=
    (Nat.div_lt_iff_lt_mul hd0).1 hQuotUpper
  have hUpper : n < d * (t + 1) ^ (s + 1) := by simpa [Nat.mul_comm] using hUpperMul
  have hSuccDiv : d + 1 ≤ e := by omega
  have hCollision : (d + 1) * t ^ (s + 1) < d * (t + 1) ^ (s + 1) := by
    calc
      (d + 1) * t ^ (s + 1) ≤ e * t ^ (s + 1) :=
        Nat.mul_le_mul_right (t ^ (s + 1)) hSuccDiv
      _ ≤ n := hLower
      _ < d * (t + 1) ^ (s + 1) := hUpper
  have hScale : t + 1 < (s + 1) * (d + 1) :=
    divisor_collision_root_scale hCollision
  have hLtE : t < (s + 1) * e := by
    have hScaleE : (s + 1) * (d + 1) ≤ (s + 1) * e :=
      Nat.mul_le_mul_left (s + 1) hSuccDiv
    omega
  by_cases htZero : t = 0
  · have hs2 : s + 2 ≠ 0 := by omega
    rw [htZero, zero_pow hs2]
    exact Nat.mul_pos (by omega) (pow_pos (by omega) p)
  · have htPos : 0 < t := Nat.pos_of_ne_zero htZero
    have hMul0 : t * t ^ (s + 1) < ((s + 1) * e) * t ^ (s + 1) :=
      Nat.mul_lt_mul_of_pos_right hLtE (pow_pos htPos (s + 1))
    have hMul : t ^ (s + 2) < (s + 1) * (e * t ^ (s + 1)) := by
      calc
        t ^ (s + 2) = t * t ^ (s + 1) := by
          have hs : s + 2 = (s + 1) + 1 := by omega
          rw [hs, pow_succ']
        _ < ((s + 1) * e) * t ^ (s + 1) := hMul0
        _ = (s + 1) * (e * t ^ (s + 1)) := by ring
    have hWeighted : (s + 1) * (e * t ^ (s + 1)) ≤ (s + 1) * n :=
      Nat.mul_le_mul_left (s + 1) hLower
    have hParent : (s + 1) * n < (s + 1) * (k + 1) ^ p :=
      Nat.mul_lt_mul_of_pos_left hnUpper (by omega)
    exact lt_of_lt_of_le hMul (le_trans hWeighted (Nat.le_of_lt hParent))

/-- Exact integer all-power coalescence horizon. -/
theorem power_basin_distinct_divisor_root_collision_horizon
    {p k n d e s : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (hnUpper : n < (k + 1) ^ p)
    (hroot : root (s + 1) (n / d) = root (s + 1) (n / e)) :
    root (s + 1) (n / d) ≤ root (s + 2) ((s + 1) * (k + 1) ^ p - 1) := by
  have hPower := power_basin_distinct_divisor_root_collision
    (p := p) (k := k) (n := n) (d := d) (e := e) (s := s)
    hd hde hnUpper hroot
  have hLe : (root (s + 1) (n / d)) ^ (s + 2) ≤
      (s + 1) * (k + 1) ^ p - 1 := by omega
  exact (Nat.le_nthRoot_iff (n := s + 2) (by omega)).2 hLe

/-- Exact strict-descent criterion for the all-power horizon. -/
theorem power_basin_collision_strict_descent_of_bound
    {p k n d e s : ℕ}
    (hk : (s + 1) * (k + 1) ^ p ≤ k ^ (s + 2))
    (hd : 2 ≤ d) (hde : d < e)
    (hnUpper : n < (k + 1) ^ p)
    (hroot : root (s + 1) (n / d) = root (s + 1) (n / e)) :
    root (s + 1) (n / d) < k := by
  have hPower := power_basin_distinct_divisor_root_collision
    (p := p) (k := k) (n := n) (d := d) (e := e) (s := s)
    hd hde hnUpper hroot
  by_contra hnot
  have hkRoot : k ≤ root (s + 1) (n / d) := by omega
  have hkPow : k ^ (s + 2) ≤ (root (s + 1) (n / d)) ^ (s + 2) :=
    Nat.pow_le_pow_left hkRoot (s + 2)
  omega

end EnterpriseMath.Precision
