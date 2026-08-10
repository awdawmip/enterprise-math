import EnterpriseMath.Precision.RootStateCountCarryUpper
import EnterpriseMath.Precision.TernaryBandCarry
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Exact threshold partition for the quotient-root ternary carry.

For positive `n`, put

`H = R_(r+1)(r*n-1)`,
`D = floor(n/(H+1)^r)`,
`q = floor(H/r)`,
`A = max(q(H+1)^r,(q+1)H^r)`,
`B = (q+1)(H+1)^r`.

Let `carry` mean that the horizon root is present, equivalently
`(D+1)H^r <= n`.  Then the three numerical regions are exactly the feasible
local denominator/carry states:

* below `A`: lower band with forced carry, or middle band with missing carry;
* `[A,B)`: middle band with carry;
* from `B` onward: upper band with forced carry.

This is the structural ternary classification behind the executable state-count
formula; no finite-cardinality theorem is asserted here. -/
theorem root_state_ternary_threshold_partition
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    let q := H / (s + 1)
    let X := (H + 1) ^ (s + 1)
    let Y := H ^ (s + 1)
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let carry := (D + 1) * Y ≤ n
    (n < A ↔ (D < q ∧ carry) ∨ (D = q ∧ ¬carry)) ∧
    ((A ≤ n ∧ n < B) ↔ D = q ∧ carry) ∧
    (B ≤ n ↔ D = q + 1 ∧ carry) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  let X := (H + 1) ^ (s + 1)
  let Y := H ^ (s + 1)
  change
    (n < max (q * X) ((q + 1) * Y) ↔
      (D < q ∧ (D + 1) * Y ≤ n) ∨
        (D = q ∧ ¬(D + 1) * Y ≤ n)) ∧
    ((max (q * X) ((q + 1) * Y) ≤ n ∧ n < (q + 1) * X) ↔
      D = q ∧ (D + 1) * Y ≤ n) ∧
    ((q + 1) * X ≤ n ↔ D = q + 1 ∧ (D + 1) * Y ≤ n)

  have hBand0 := root_state_denominator_three_point_band (s := s) (n := n) hn
  have hBand : q - 1 ≤ D ∧ D ≤ q + 1 := by
    simpa [H, D, q] using hBand0

  have hDDef : D = n / X := by
    rfl
  have hXPos : 0 < X := by
    dsimp [X]
    exact pow_pos (by omega) (s + 1)
  have hCellLower : D * X ≤ n := by
    rw [hDDef]
    exact Nat.div_mul_le_self n X
  have hCellUpper : n < (D + 1) * X := by
    have hDivSucc : n / X < n / X + 1 := Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hXPos).1 hDivSucc
    simpa [hDDef, Nat.mul_comm] using hMul

  have hLower0 :=
    root_state_lower_band_forces_horizon_threshold (s := s) (n := n) hn
  have hLowerForced : 1 ≤ q → D = q - 1 → (D + 1) * Y ≤ n := by
    simpa [H, D, q, Y] using hLower0

  have hUpper0 :=
    root_state_upper_band_forces_horizon_threshold (s := s) (n := n) hn
  have hUpperForced : D = q + 1 → (D + 1) * Y ≤ n := by
    simpa [H, D, q, Y] using hUpper0

  exact ternary_band_carry_partition
    hBand.1 hBand.2 hCellLower hCellUpper hLowerForced hUpperForced

end EnterpriseMath.Precision
