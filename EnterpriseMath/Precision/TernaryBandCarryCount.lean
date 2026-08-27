import EnterpriseMath.Precision.TernaryBandCarry
import Mathlib.Tactic

namespace EnterpriseMath.Precision

/-- Once a binary atlas count is known, the generic ternary threshold partition
reduces it to a three-valued carry without any additional geometry.

The binary count is written in subtraction-free form

`N + 1 = D + H + kappa`,

where `kappa` is the indicator of `(D+1)Y <= n`.  The conclusion is

`N + 1 = H + q + tau`,

with `tau=0,1,2` on the three threshold regions defined by
`A=max(qX,(q+1)Y)` and `B=(q+1)X`.

This isolates the final quotient-root state-count proof obligation: once the
binary distinct-root atlas cardinality is formalized, the ternary formula is a
pure arithmetic corollary. -/
theorem ternary_count_from_binary_carry
    {n D q X Y H N : ℕ}
    (hBandLow : q - 1 ≤ D)
    (hBandHigh : D ≤ q + 1)
    (hCellLower : D * X ≤ n)
    (hCellUpper : n < (D + 1) * X)
    (hLowerForced : 1 ≤ q → D = q - 1 → (D + 1) * Y ≤ n)
    (hUpperForced : D = q + 1 → (D + 1) * Y ≤ n)
    (hCount : N + 1 = D + H + (if (D + 1) * Y ≤ n then 1 else 0)) :
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let tau := if n < A then 0 else if n < B then 1 else 2
    N + 1 = H + q + tau := by
  dsimp
  have hPart := ternary_band_carry_partition
    hBandLow hBandHigh hCellLower hCellUpper hLowerForced hUpperForced
  dsimp at hPart
  by_cases hA : n < max (q * X) ((q + 1) * Y)
  · simp [hA]
    have hState := hPart.1.mp hA
    rcases hState with ⟨hDlt, hCarry⟩ | ⟨hDEq, hNoCarry⟩
    · have hDEq : D = q - 1 := by omega
      have hqPos : 1 ≤ q := by omega
      simp [hCarry] at hCount
      omega
    · simp [hNoCarry] at hCount
      omega
  · have hAle : max (q * X) ((q + 1) * Y) ≤ n := by omega
    by_cases hB : n < (q + 1) * X
    · simp [hA, hB]
      have hState := hPart.2.1.mp ⟨hAle, hB⟩
      rcases hState with ⟨hDEq, hCarry⟩
      simp [hCarry] at hCount
      omega
    · have hBle : (q + 1) * X ≤ n := by omega
      simp [hA, hB]
      have hState := hPart.2.2.mp hBle
      rcases hState with ⟨hDEq, hCarry⟩
      simp [hCarry] at hCount
      omega

end EnterpriseMath.Precision
