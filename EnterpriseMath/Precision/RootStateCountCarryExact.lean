import EnterpriseMath.Precision.RootStateCountCarry
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Exact three-point denominator band for the quotient-root state-count atlas.

For a positive integer state `n` and positive root order `s+1`, define

`H = R_(s+2)((s+1)n - 1)`,
`D = floor(n/(H+1)^(s+1))`,
`q = floor(H/(s+1))`.

Then the high-denominator threshold is forced into the three adjacent values
`q-1`, `q`, `q+1` (with natural subtraction truncating the lower endpoint at
zero):

`q-1 <= D <= q+1`.

This theorem supplies the exact `nthRoot` and Euclidean-division hypotheses to
the API-free arithmetic kernel in `RootStateCountCarry`. -/
theorem root_state_denominator_three_point_band
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    let q := H / (s + 1)
    q - 1 ≤ D ∧ D ≤ q + 1 := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  change q - 1 ≤ D ∧ D ≤ q + 1

  have hOrderPos : 0 < s + 1 := by omega
  have hParentOrder : s + 2 ≠ 0 := by omega
  have hDenPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hProdPos : 0 < (s + 1) * n := Nat.mul_pos hOrderPos hn

  have hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1 := by
    dsimp [H]
    exact Nat.pow_nthRoot_le (Or.inl hParentOrder)

  have hHUpper0 :
      (s + 1) * n - 1 < (H + 1) ^ (s + 2) := by
    dsimp [H]
    exact Nat.lt_pow_nthRoot_add_one hParentOrder ((s + 1) * n - 1)

  have hParentUpper : (s + 1) * n ≤ (H + 1) ^ (s + 2) := by
    omega

  have hDLower : D * (H + 1) ^ (s + 1) ≤ n := by
    dsimp [D]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))

  have hDUpper : n < (D + 1) * (H + 1) ^ (s + 1) := by
    have hDivSucc : n / (H + 1) ^ (s + 1) < n / (H + 1) ^ (s + 1) + 1 :=
      Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hDenPos).1 hDivSucc
    simpa [D, Nat.mul_comm] using hMul

  have hqLower : (s + 1) * q ≤ H := by
    have h := Nat.div_mul_le_self H (s + 1)
    simpa [q, Nat.mul_comm] using h

  have hqUpper : H < (s + 1) * (q + 1) := by
    have hDivSucc : H / (s + 1) < H / (s + 1) + 1 := Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hOrderPos).1 hDivSucc
    simpa [q, Nat.mul_comm] using hMul

  have hBand := root_state_denominator_three_point_band_kernel
    (s := s) (H := H) (n := n) (D := D) (q := q)
    hqUpper hDLower hParentUpper hqLower hHLower hDUpper
  simpa using hBand

/-- The quotient `q=floor(H/(s+1))` already lies strictly inside the horizon
root cell: `q * H^(s+1) < n`.

This is the arithmetic reason the exceptional lower denominator band cannot
also lose the horizon fiber. -/
theorem root_state_horizon_quotient_threshold
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let q := H / (s + 1)
    q * H ^ (s + 1) < n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let q := H / (s + 1)
  change q * H ^ (s + 1) < n

  have hOrderPos : 0 < s + 1 := by omega
  have hParentOrder : s + 2 ≠ 0 := by omega
  have hProdPos : 0 < (s + 1) * n := Nat.mul_pos hOrderPos hn
  have hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1 := by
    dsimp [H]
    exact Nat.pow_nthRoot_le (Or.inl hParentOrder)
  have hqLower : (s + 1) * q ≤ H := by
    have h := Nat.div_mul_le_self H (s + 1)
    simpa [q, Nat.mul_comm] using h
  have hScaled :
      (s + 1) * (q * H ^ (s + 1)) ≤ H ^ (s + 2) := by
    calc
      (s + 1) * (q * H ^ (s + 1))
          = ((s + 1) * q) * H ^ (s + 1) := by ring
      _ ≤ H * H ^ (s + 1) :=
        Nat.mul_le_mul_right (H ^ (s + 1)) hqLower
      _ = H ^ (s + 2) := by
        rw [show s + 2 = (s + 1) + 1 by omega, pow_succ']
  have hScaledLt :
      (s + 1) * (q * H ^ (s + 1)) < (s + 1) * n := by
    calc
      (s + 1) * (q * H ^ (s + 1)) ≤ H ^ (s + 2) := hScaled
      _ ≤ (s + 1) * n - 1 := hHLower
      _ < (s + 1) * n := by omega
  nlinarith

/-- In the lower denominator-band case `D=q-1` with `q>0`, the horizon root is
forced present.  Equivalently, the exact horizon-fiber threshold
`(D+1)H^(s+1) <= n` holds automatically. -/
theorem root_state_lower_band_forces_horizon_threshold
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    let q := H / (s + 1)
    1 ≤ q → D = q - 1 → (D + 1) * H ^ (s + 1) ≤ n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  change 1 ≤ q → D = q - 1 → (D + 1) * H ^ (s + 1) ≤ n
  intro hqPos hD
  have hThreshold := root_state_horizon_quotient_threshold (s := s) (n := n) hn
  change q * H ^ (s + 1) < n at hThreshold
  have hCoeff : D + 1 = q := by omega
  rw [hCoeff]
  exact Nat.le_of_lt hThreshold

end EnterpriseMath.Precision
