import EnterpriseMath.Precision.PowerQuotientCoalescence
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Generalized collision-scale lemma retaining the full divisor span.

If the endpoint denominator labels are `d` and `d+g`, with `g>0`, and one
`(s+1)`-root cell `t` fits between them, then

`g*(t+1) < (s+1)*(d+g)`.

The gap-one theorem in `PowerQuotientCoalescence` is the specialization `g=1`.
-/
theorem divisor_gap_collision_root_scale
    {d g t s : ℕ}
    (hg : 1 ≤ g)
    (hcollision : (d + g) * t ^ (s + 1) < d * (t + 1) ^ (s + 1)) :
    g * (t + 1) < (s + 1) * (d + g) := by
  by_contra hnot
  have hCoeff : (d + g) * (s + 1) ≤ g * (t + 1) := by
    nlinarith
  have hStep := pow_succ_le_pow_add_tangent t (s + 1)
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
  have hCap : d * (t + 1) ^ (s + 1) ≤ (d + g) * t ^ (s + 1) := by
    have hCancel :
        d * (t + 1) ^ (s + 1) + g * (t + 1) ^ (s + 1) ≤
          (d + g) * t ^ (s + 1) + g * (t + 1) ^ (s + 1) := by
      calc
        d * (t + 1) ^ (s + 1) + g * (t + 1) ^ (s + 1)
            = (d + g) * (t + 1) ^ (s + 1) := by ring
        _ ≤ (d + g) * t ^ (s + 1) + g * (t + 1) ^ (s + 1) := hCombined
    omega
  omega

/-- Sharp graded all-power divisor-span coalescence law.

For source upper bound `n < (k+1)^p`, if `2≤d<e` give the same actual
`(s+1)`-root after floor division, then

`(e-d) * t^(s+2) < (s+1) * (k+1)^p`.

This is the mother inequality behind the graded multiplicity profile. -/
theorem power_basin_distinct_divisor_root_collision_gap
    {p k n d e s : ℕ}
    (hd : 2 ≤ d) (hde : d < e)
    (hnUpper : n < (k + 1) ^ p)
    (hroot : root (s + 1) (n / d) = root (s + 1) (n / e)) :
    (e - d) * (root (s + 1) (n / d)) ^ (s + 2) <
      (s + 1) * (k + 1) ^ p := by
  let t := root (s + 1) (n / d)
  let g := e - d
  change g * t ^ (s + 2) < (s + 1) * (k + 1) ^ p
  have hd0 : 0 < d := by omega
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
  have hPowE : t ^ (s + 1) ≤ n / e := by
    simpa [hRootE] using hPowE0
  have hLowerMul : t ^ (s + 1) * e ≤ n :=
    (Nat.le_div_iff_mul_le he0).1 hPowE
  have hLower : e * t ^ (s + 1) ≤ n := by
    simpa [Nat.mul_comm] using hLowerMul
  have hQuotUpper : n / d < (t + 1) ^ (s + 1) := by
    dsimp [t]
    exact Nat.lt_pow_nthRoot_add_one (by omega) (n / d)
  have hUpperMul : n < (t + 1) ^ (s + 1) * d :=
    (Nat.div_lt_iff_lt_mul hd0).1 hQuotUpper
  have hUpper : n < d * (t + 1) ^ (s + 1) := by
    simpa [Nat.mul_comm] using hUpperMul
  have hCollision : (d + g) * t ^ (s + 1) < d * (t + 1) ^ (s + 1) := by
    rw [hdecomp]
    exact lt_of_le_of_lt hLower hUpper
  have hScale : g * (t + 1) < (s + 1) * (d + g) :=
    divisor_gap_collision_root_scale hg hCollision
  have hScaleE : g * (t + 1) < (s + 1) * e := by
    simpa [hdecomp] using hScale
  have hLt : g * t < (s + 1) * e := by
    nlinarith [hg, hScaleE]
  by_cases htZero : t = 0
  · have hs2 : s + 2 ≠ 0 := by omega
    rw [htZero, zero_pow hs2, Nat.mul_zero]
    exact Nat.mul_pos (by omega) (pow_pos (by omega) p)
  · have htPos : 0 < t := Nat.pos_of_ne_zero htZero
    have hMul0 :
        (g * t) * t ^ (s + 1) < ((s + 1) * e) * t ^ (s + 1) :=
      Nat.mul_lt_mul_of_pos_right hLt (pow_pos htPos (s + 1))
    have hMul : g * t ^ (s + 2) < (s + 1) * (e * t ^ (s + 1)) := by
      simpa [pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul0
    have hWeighted : (s + 1) * (e * t ^ (s + 1)) ≤ (s + 1) * n :=
      Nat.mul_le_mul_left (s + 1) hLower
    have hParent : (s + 1) * n < (s + 1) * (k + 1) ^ p :=
      Nat.mul_lt_mul_of_pos_left hnUpper (by omega)
    exact lt_of_lt_of_le hMul (le_trans hWeighted (Nat.le_of_lt hParent))

end EnterpriseMath.Precision
