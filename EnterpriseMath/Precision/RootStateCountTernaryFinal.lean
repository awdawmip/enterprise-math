import EnterpriseMath.Precision.BinaryRootAtlasCardinality
import EnterpriseMath.Precision.RootStateCountCarryThreshold
import EnterpriseMath.Precision.TernaryBandCarryCount
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Final exact ternary quotient-root state-count formula.

For one positive integer state `n` and positive root order `r=s+1`, define

`H = R_(r+1)(r*n-1)`,
`q = floor(H/r)`,
`A = max(q(H+1)^r,(q+1)H^r)`,
`B = (q+1)(H+1)^r`.

Let `N_r(n)` be the number of distinct positive quotient-root states
`R_r(floor(n/d))` as `1<=d<=n`.  Then

`N_r(n)+1 = H+q+tau`,

where `tau` is exactly `0,1,2` according as `n<A`, `A<=n<B`, or `B<=n`.

This theorem closes the binary atlas and ternary carry chains: no denominator
scan, low-root scan, asymptotic estimate, primality hypothesis, or hidden real
root occurs in the statement or proof. -/
theorem quotientRootStates_ternary_cardinality
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let q := H / (s + 1)
    let X := (H + 1) ^ (s + 1)
    let Y := H ^ (s + 1)
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let tau := if n < A then 0 else if n < B then 1 else 2
    (quotientRootStates s n).card + 1 = H + q + tau := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  let X := (H + 1) ^ (s + 1)
  let Y := H ^ (s + 1)
  change
    (quotientRootStates s n).card + 1 =
      H + q +
        (if n < max (q * X) ((q + 1) * Y) then 0
         else if n < (q + 1) * X then 1 else 2)

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

  have hCount0 := quotientRootStates_binary_cardinality (s := s) (n := n) hn
  have hCount :
      (quotientRootStates s n).card + 1 =
        D + H + (if (D + 1) * Y ≤ n then 1 else 0) := by
    simpa [H, D, Y] using hCount0

  exact ternary_count_from_binary_carry
    hBand.1 hBand.2 hCellLower hCellUpper
    hLowerForced hUpperForced hCount

end EnterpriseMath.Precision
