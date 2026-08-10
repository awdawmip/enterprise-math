import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Discrete one-step upper tangent for adjacent powers.

This is the elementary arithmetic input used by the state-specific quotient-root
coalescence theorem. -/
theorem quotient_root_pow_succ_le_tangent (t r : ℕ) :
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

/-- If one positive root cell can contain denominator labels separated by a gap
`g`, then the root scale is bounded by that label span. -/
theorem quotient_root_divisor_gap_scale
    {d g t s : ℕ}
    (_hg : 1 ≤ g)
    (hcollision : (d + g) * t ^ (s + 1) < d * (t + 1) ^ (s + 1)) :
    g * (t + 1) < (s + 1) * (d + g) := by
  by_contra hnot
  have hCoeff : (d + g) * (s + 1) ≤ g * (t + 1) := by
    nlinarith
  have hStep := quotient_root_pow_succ_le_tangent t (s + 1)
  have hScaled :
      (d + g) * (t + 1) ^ (s + 1) ≤
        (d + g) * t ^ (s + 1) +
          (d + g) * ((s + 1) * (t + 1) ^ s) := by
    simpa [Nat.succ_sub_one, Nat.mul_add, Nat.mul_assoc] using
      Nat.mul_le_mul_left (d + g) hStep
  have hError :
      (d + g) * ((s + 1) * (t + 1) ^ s) ≤
        g * (t + 1) ^ (s + 1) := by
    calc
      (d + g) * ((s + 1) * (t + 1) ^ s)
          = ((d + g) * (s + 1)) * (t + 1) ^ s := by ring
      _ ≤ (g * (t + 1)) * (t + 1) ^ s :=
        Nat.mul_le_mul_right ((t + 1) ^ s) hCoeff
      _ = g * (t + 1) ^ (s + 1) := by
        rw [pow_succ']
        ring
  have hCombined :
      (d + g) * (t + 1) ^ (s + 1) ≤
        (d + g) * t ^ (s + 1) + g * (t + 1) ^ (s + 1) :=
    le_trans hScaled (Nat.add_le_add_left hError ((d + g) * t ^ (s + 1)))
  have hCancel :
      d * (t + 1) ^ (s + 1) + g * (t + 1) ^ (s + 1) ≤
        (d + g) * t ^ (s + 1) + g * (t + 1) ^ (s + 1) := by
    calc
      d * (t + 1) ^ (s + 1) + g * (t + 1) ^ (s + 1)
          = (d + g) * (t + 1) ^ (s + 1) := by ring
      _ ≤ (d + g) * t ^ (s + 1) + g * (t + 1) ^ (s + 1) := hCombined
  have hCap : d * (t + 1) ^ (s + 1) ≤ (d + g) * t ^ (s + 1) := by
    omega
  omega

/-- State-specific graded quotient-root coalescence kernel.

For one positive integer state `n`, if two positive denominators `d<e` give the
same actual `(s+1)`-root after floor division, then

`(e-d) * t^(s+2) < (s+1) * n`.

No source power basin, prime condition, asymptotic estimate, or real root is
present.  Basin-scale horizons are corollaries obtained only after adding their
own upper bound on `n`. -/
theorem quotient_root_state_collision_gap
    {n d e s : ℕ}
    (hn : 0 < n)
    (hd : 0 < d)
    (hde : d < e)
    (hroot : root (s + 1) (n / d) = root (s + 1) (n / e)) :
    (e - d) * (root (s + 1) (n / d)) ^ (s + 2) < (s + 1) * n := by
  let t := root (s + 1) (n / d)
  let g := e - d
  change g * t ^ (s + 2) < (s + 1) * n
  have he0 : 0 < e := by omega
  have hg : 1 ≤ g := by
    dsimp [g]
    omega
  have hdecomp : d + g = e := by
    dsimp [g]
    omega
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
    (Nat.div_lt_iff_lt_mul hd).1 hQuotUpper
  have hUpper : n < d * (t + 1) ^ (s + 1) := by simpa [Nat.mul_comm] using hUpperMul
  have hCollision : (d + g) * t ^ (s + 1) < d * (t + 1) ^ (s + 1) := by
    rw [hdecomp]
    exact lt_of_le_of_lt hLower hUpper
  have hScale : g * (t + 1) < (s + 1) * (d + g) :=
    quotient_root_divisor_gap_scale hg hCollision
  have hScaleE : g * (t + 1) < (s + 1) * e := by
    simpa [hdecomp] using hScale
  have hLt : g * t < (s + 1) * e := by
    nlinarith [hg, hScaleE]
  by_cases htZero : t = 0
  · have hs2 : s + 2 ≠ 0 := by omega
    rw [htZero, zero_pow hs2, Nat.mul_zero]
    exact Nat.mul_pos (by omega) hn
  · have htPos : 0 < t := Nat.pos_of_ne_zero htZero
    have hMul0 :
        (g * t) * t ^ (s + 1) < ((s + 1) * e) * t ^ (s + 1) :=
      Nat.mul_lt_mul_of_pos_right hLt (pow_pos htPos (s + 1))
    have hMul : g * t ^ (s + 2) < (s + 1) * (e * t ^ (s + 1)) := by
      simpa [pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul0
    have hWeighted : (s + 1) * (e * t ^ (s + 1)) ≤ (s + 1) * n :=
      Nat.mul_le_mul_left (s + 1) hLower
    exact lt_of_lt_of_le hMul hWeighted

end EnterpriseMath.Precision
