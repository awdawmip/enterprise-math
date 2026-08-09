import EnterpriseMath.Precision.RootStateCountCarryExact
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Discrete Bernoulli lower tangent bound.

Together with the existing upper tangent estimate, this gives the two-sided
one-step control of integer powers needed by the exact state-count carry. -/
theorem pow_add_tangent_le_succ_pow (t r : ℕ) :
    t ^ r + r * t ^ (r - 1) ≤ (t + 1) ^ r := by
  induction r with
  | zero => simp
  | succ r ih =>
      have hMul := Nat.mul_le_mul_left (t + 1) ih
      have hExpand :
          (t + 1) * (t ^ r + r * t ^ (r - 1)) =
            (t ^ (r + 1) + (r + 1) * t ^ r) + r * t ^ (r - 1) := by
        rw [pow_succ']
        ring
      calc
        t ^ (r + 1) + (r + 1) * t ^ ((r + 1) - 1)
            = t ^ (r + 1) + (r + 1) * t ^ r := by simp
        _ ≤ (t ^ (r + 1) + (r + 1) * t ^ r) + r * t ^ (r - 1) := by omega
        _ = (t + 1) * (t ^ r + r * t ^ (r - 1)) := hExpand.symm
        _ ≤ (t + 1) * (t + 1) ^ r := hMul
        _ = (t + 1) ^ (r + 1) := by rw [pow_succ']

/-- In the upper denominator-band case `D=q+1`, the horizon root is also
forced present.

Thus both extreme denominator bands carry the horizon automatically; only the
middle band `D=q` retains a genuine binary boundary choice. -/
theorem root_state_upper_band_forces_horizon_threshold
    {s n : ℕ}
    (hn : 0 < n) :
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
  have hDenPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
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
