import EnterpriseMath.Precision.PowerQuotientCoalescence
import Mathlib.Tactic

namespace EnterpriseMath.Precision

/-- Upper half of the quotient-root state-count denominator band.

Write the root order as `s+1`, let `H` be the coalescence horizon, let `D`
be the last high-denominator label, and let `q` be the quotient of `H` by the
root order.  The theorem is deliberately API-free: it consumes only the exact
integer inequalities later supplied by `nthRoot` and floor division.
-/
theorem root_state_denominator_band_upper_kernel
    {s H n D q : ℕ}
    (hqUpper : H < (s + 1) * (q + 1))
    (hDLower : D * (H + 1) ^ (s + 1) ≤ n)
    (hParentUpper : (s + 1) * n ≤ (H + 1) ^ (s + 2)) :
    D ≤ q + 1 := by
  have hPowPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hScaled :
      ((s + 1) * D) * (H + 1) ^ (s + 1) ≤
        (H + 1) * (H + 1) ^ (s + 1) := by
    calc
      ((s + 1) * D) * (H + 1) ^ (s + 1)
          = (s + 1) * (D * (H + 1) ^ (s + 1)) := by ring
      _ ≤ (s + 1) * n := Nat.mul_le_mul_left (s + 1) hDLower
      _ ≤ (H + 1) ^ (s + 2) := hParentUpper
      _ = (H + 1) * (H + 1) ^ (s + 1) := by
        rw [pow_succ']
  have hCoeff : (s + 1) * D ≤ H + 1 := by
    nlinarith [hScaled, hPowPos]
  by_contra hnot
  have hHigh : q + 2 ≤ D := by omega
  nlinarith [hqUpper, hCoeff]

/-- Discrete tangent estimate in the form needed for the lower denominator
band.  If the horizon `H` has reached the root order `s+1`, then removing one
root-order block from `H` and multiplying by the next root-cell width still
stays strictly below `H^(s+2)`.
-/
theorem root_state_horizon_tangent_gap
    {s H : ℕ}
    (hOrder : s + 1 ≤ H) :
    (H - (s + 1)) * (H + 1) ^ (s + 1) < H ^ (s + 2) := by
  have hStep := pow_succ_le_pow_add_tangent H (s + 1)
  have hPrevPos : 0 < (H + 1) ^ s := pow_pos (by omega) s
  have hPrevLt : H * (H + 1) ^ s < (H + 1) ^ (s + 1) := by
    calc
      H * (H + 1) ^ s < (H + 1) * (H + 1) ^ s :=
        Nat.mul_lt_mul_of_pos_right (by omega) hPrevPos
      _ = (H + 1) ^ (s + 1) := by rw [← pow_succ']
  have hHX :
      H * (H + 1) ^ (s + 1) <
        H ^ (s + 2) + (s + 1) * (H + 1) ^ (s + 1) := by
    calc
      H * (H + 1) ^ (s + 1)
          ≤ H * (H ^ (s + 1) + (s + 1) * (H + 1) ^ s) :=
            Nat.mul_le_mul_left H hStep
      _ = H ^ (s + 2) + (s + 1) * (H * (H + 1) ^ s) := by
        rw [show s + 2 = (s + 1) + 1 by omega, pow_succ']
        ring
      _ < H ^ (s + 2) + (s + 1) * (H + 1) ^ (s + 1) := by
        gcongr
  have hDecomp : H = (H - (s + 1)) + (s + 1) := by omega
  have hExpanded :
      (H - (s + 1)) * (H + 1) ^ (s + 1) +
          (s + 1) * (H + 1) ^ (s + 1) <
        H ^ (s + 2) + (s + 1) * (H + 1) ^ (s + 1) := by
    calc
      (H - (s + 1)) * (H + 1) ^ (s + 1) +
          (s + 1) * (H + 1) ^ (s + 1)
          = H * (H + 1) ^ (s + 1) := by rw [hDecomp, Nat.add_mul]
      _ < H ^ (s + 2) + (s + 1) * (H + 1) ^ (s + 1) := hHX
  omega

/-- Lower half of the quotient-root state-count denominator band.

Assume `q>0`, `(s+1)q≤H`, the lower horizon power bound, and the strict upper
endpoint for the floor-division cell of `D`.  Then `D` cannot lie below `q-1`.
-/
theorem root_state_denominator_band_lower_kernel
    {s H n D q : ℕ}
    (hqPos : 1 ≤ q)
    (hqLower : (s + 1) * q ≤ H)
    (hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1)
    (hDUpper : n < (D + 1) * (H + 1) ^ (s + 1)) :
    q - 1 ≤ D := by
  have hOrder : s + 1 ≤ H := by
    nlinarith [hqPos, hqLower]
  have hGap := root_state_horizon_tangent_gap hOrder
  have hQDecomp : q = (q - 1) + 1 := by omega
  have hHDecomp : H = (H - (s + 1)) + (s + 1) := by omega
  have hQSpan : (s + 1) * (q - 1) ≤ H - (s + 1) := by
    nlinarith [hqLower]
  have hPowPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hScaledQ :
      (s + 1) * ((q - 1) * (H + 1) ^ (s + 1)) < (s + 1) * n := by
    calc
      (s + 1) * ((q - 1) * (H + 1) ^ (s + 1))
          = ((s + 1) * (q - 1)) * (H + 1) ^ (s + 1) := by ring
      _ ≤ (H - (s + 1)) * (H + 1) ^ (s + 1) :=
        Nat.mul_le_mul_right ((H + 1) ^ (s + 1)) hQSpan
      _ < H ^ (s + 2) := hGap
      _ ≤ (s + 1) * n - 1 := hHLower
      _ < (s + 1) * n := by
        have hPos : 0 < (s + 1) * n := by
          by_contra hzero
          have : (s + 1) * n = 0 := by omega
          omega
        omega
  have hQCell : (q - 1) * (H + 1) ^ (s + 1) < n := by
    nlinarith [hScaledQ]
  by_contra hnot
  have hDLow : D + 1 ≤ q - 1 := by omega
  have hContr : (D + 1) * (H + 1) ^ (s + 1) ≤
      (q - 1) * (H + 1) ^ (s + 1) :=
    Nat.mul_le_mul_right ((H + 1) ^ (s + 1)) hDLow
  omega

/-- The complete three-point arithmetic band.  The zero-quotient case needs no
lower estimate; otherwise `D` lies between `q-1` and `q+1`.
-/
theorem root_state_denominator_three_point_band_kernel
    {s H n D q : ℕ}
    (hqUpper : H < (s + 1) * (q + 1))
    (hDLower : D * (H + 1) ^ (s + 1) ≤ n)
    (hParentUpper : (s + 1) * n ≤ (H + 1) ^ (s + 2))
    (hqLower : (s + 1) * q ≤ H)
    (hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1)
    (hDUpper : n < (D + 1) * (H + 1) ^ (s + 1)) :
    max 0 (q - 1) ≤ D ∧ D ≤ q + 1 := by
  constructor
  · simp only [Nat.zero_le, max_eq_right]
    by_cases hqZero : q = 0
    · subst q
      simp
    · exact root_state_denominator_band_lower_kernel
        (q := q) (s := s) (H := H) (n := n) (D := D)
        (Nat.pos_of_ne_zero hqZero) hqLower hHLower hDUpper
  · exact root_state_denominator_band_upper_kernel
      (q := q) (s := s) (H := H) (n := n) (D := D)
      hqUpper hDLower hParentUpper

end EnterpriseMath.Precision
