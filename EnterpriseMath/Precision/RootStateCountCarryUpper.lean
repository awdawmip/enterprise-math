import EnterpriseMath.Precision.RootStateCountCarryExact
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Nat specialization of the standard Bernoulli lower tangent bound.

This is prior-art arithmetic already provided by mathlib's
`pow_add_mul_le_add_pow`; the wrapper only fixes `b=1` and Nat notation for the
quotient-root carry layer. -/
theorem pow_add_tangent_le_succ_pow (t r : ℕ) :
    t ^ r + r * t ^ (r - 1) ≤ (t + 1) ^ r := by
  have h :=
    pow_add_mul_le_add_pow (R := ℕ) (a := t) (b := 1)
      (by omega) (by omega) r
  simpa using h

/-- In the upper denominator-band case `D=q+1`, the horizon root is also
forced present.

Thus both extreme denominator bands carry the horizon automatically; only the
middle band `D=q` retains a genuine binary boundary choice. -/
theorem root_state_upper_band_forces_horizon_threshold
    {s n : ℕ}
    (_hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    let q := H / (s + 1)
    D = q + 1 → (D + 1) * H ^ (s + 1) ≤ n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  change D = q + 1 → (D + 1) * H ^ (s + 1) ≤ n
  intro hD

  have hOrderPos : 0 < s + 1 := by omega
  have hqUpper : H < (s + 1) * (q + 1) := by
    have hDivSucc : H / (s + 1) < H / (s + 1) + 1 := Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hOrderPos).1 hDivSucc
    simpa [q, Nat.mul_comm] using hMul

  have hBern := pow_add_tangent_le_succ_pow H (s + 1)
  have hPowerError : H ^ (s + 1) ≤ (q + 1) * (s + 1) * H ^ s := by
    calc
      H ^ (s + 1) = H * H ^ s := by rw [pow_succ']
      _ ≤ ((s + 1) * (q + 1)) * H ^ s :=
        Nat.mul_le_mul_right (H ^ s) (Nat.le_of_lt hqUpper)
      _ = (q + 1) * (s + 1) * H ^ s := by ring

  have hScaledBern :
      (q + 1) * (H ^ (s + 1) + (s + 1) * H ^ s) ≤
        (q + 1) * (H + 1) ^ (s + 1) :=
    Nat.mul_le_mul_left (q + 1) hBern

  have hBridge :
      (q + 2) * H ^ (s + 1) ≤ (q + 1) * (H + 1) ^ (s + 1) := by
    calc
      (q + 2) * H ^ (s + 1)
          = (q + 1) * H ^ (s + 1) + H ^ (s + 1) := by ring
      _ ≤ (q + 1) * H ^ (s + 1) + (q + 1) * (s + 1) * H ^ s :=
        Nat.add_le_add_left hPowerError ((q + 1) * H ^ (s + 1))
      _ = (q + 1) * (H ^ (s + 1) + (s + 1) * H ^ s) := by ring
      _ ≤ (q + 1) * (H + 1) ^ (s + 1) := hScaledBern

  have hDLower : D * (H + 1) ^ (s + 1) ≤ n := by
    dsimp [D]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))

  have hCoeff : D + 1 = q + 2 := by omega
  rw [hCoeff]
  calc
    (q + 2) * H ^ (s + 1) ≤ (q + 1) * (H + 1) ^ (s + 1) := hBridge
    _ = D * (H + 1) ^ (s + 1) := by rw [hD]
    _ ≤ n := hDLower

end EnterpriseMath.Precision
