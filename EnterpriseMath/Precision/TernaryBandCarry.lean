import Mathlib.Tactic

namespace EnterpriseMath.Precision

/-- Generic ternary carry partition from a three-point coarse band.

Suppose an integer coarse label `D` lies in the three-point band around `q`,
its exact cell is `D*X <= n < (D+1)*X`, and a boundary bit is defined by
`(D+1)*Y <= n`.  If both extreme coarse labels force that bit to be present,
then the two thresholds

`A = max(q*X, (q+1)*Y)`,
`B = (q+1)*X`

partition the only feasible local states exactly:

* `n<A`: either the lower coarse label with forced bit, or the middle label
  with missing bit;
* `A<=n<B`: the middle label with present bit;
* `B<=n`: the upper coarse label with forced bit.

No root, quotient, power, or asymptotic assumption occurs in this theorem. -/
theorem ternary_band_carry_partition
    {n D q X Y : ℕ}
    (hBandLow : q - 1 ≤ D)
    (hBandHigh : D ≤ q + 1)
    (hCellLower : D * X ≤ n)
    (hCellUpper : n < (D + 1) * X)
    (hLowerForced : 1 ≤ q → D = q - 1 → (D + 1) * Y ≤ n)
    (hUpperForced : D = q + 1 → (D + 1) * Y ≤ n) :
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let carry := (D + 1) * Y ≤ n
    (n < A ↔ (D < q ∧ carry) ∨ (D = q ∧ ¬carry)) ∧
    ((A ≤ n ∧ n < B) ↔ D = q ∧ carry) ∧
    (B ≤ n ↔ D = q + 1 ∧ carry) := by
  dsimp
  have hLowMul : ∀ {u v : ℕ}, u ≤ v → u * X ≤ v * X := by
    intro u v huv
    exact Nat.mul_le_mul_right X huv
  have hYMul : ∀ {u v : ℕ}, u ≤ v → u * Y ≤ v * Y := by
    intro u v huv
    exact Nat.mul_le_mul_right Y huv

  constructor
  · constructor
    · intro hA
      rcases (lt_max_iff.mp hA) with hQX | hQY
      · have hDlt : D < q := by
          by_contra hnot
          have hqD : q ≤ D := by omega
          have hqX_DX : q * X ≤ D * X := hLowMul hqD
          omega
        have hqPos : 1 ≤ q := by omega
        have hDEq : D = q - 1 := by omega
        exact Or.inl ⟨hDlt, hLowerForced hqPos hDEq⟩
      · by_cases hDlt : D < q
        · have hqPos : 1 ≤ q := by omega
          have hDEq : D = q - 1 := by omega
          exact Or.inl ⟨hDlt, hLowerForced hqPos hDEq⟩
        · have hqD : q ≤ D := by omega
          have hNotUpper : D ≠ q + 1 := by
            intro hUpper
            have hCarryUpper := hUpperForced hUpper
            have hYOrder : (q + 1) * Y ≤ (D + 1) * Y := by
              apply hYMul
              omega
            omega
          have hDEq : D = q := by omega
          have hNoCarry : ¬(D + 1) * Y ≤ n := by
            intro hCarry
            rw [hDEq] at hCarry
            omega
          exact Or.inr ⟨hDEq, hNoCarry⟩
    · intro hState
      rcases hState with ⟨hDlt, _hCarry⟩ | ⟨hDEq, hNoCarry⟩
      · have hStep : D + 1 ≤ q := by omega
        have hDX_qX : (D + 1) * X ≤ q * X := hLowMul hStep
        have hn_qX : n < q * X := hCellUpper.trans_le hDX_qX
        exact hn_qX.trans_le (le_max_left _ _)
      · have hnY : n < (q + 1) * Y := by
          have hNo : ¬(q + 1) * Y ≤ n := by
            simpa [hDEq] using hNoCarry
          omega
        exact hnY.trans_le (le_max_right _ _)

  constructor
  · constructor
    · rintro ⟨hA, hB⟩
      have hqX : q * X ≤ n := (max_le_iff.mp hA).1
      have hqY : (q + 1) * Y ≤ n := (max_le_iff.mp hA).2
      have hqLeD : q ≤ D := by
        by_contra hnot
        have hStep : D + 1 ≤ q := by omega
        have hDX_qX : (D + 1) * X ≤ q * X := hLowMul hStep
        omega
      have hDltSucc : D < q + 1 := by
        by_contra hnot
        have hSuccD : q + 1 ≤ D := by omega
        have hBX_DX : (q + 1) * X ≤ D * X := hLowMul hSuccD
        omega
      have hDEq : D = q := by omega
      have hCarry : (D + 1) * Y ≤ n := by
        simpa [hDEq] using hqY
      exact ⟨hDEq, hCarry⟩
    · rintro ⟨hDEq, hCarry⟩
      have hqX : q * X ≤ n := by
        simpa [hDEq] using hCellLower
      have hqY : (q + 1) * Y ≤ n := by
        simpa [hDEq] using hCarry
      have hA : max (q * X) ((q + 1) * Y) ≤ n :=
        max_le hqX hqY
      have hB : n < (q + 1) * X := by
        simpa [hDEq] using hCellUpper
      exact ⟨hA, hB⟩

  constructor
  · intro hB
    have hSuccLeD : q + 1 ≤ D := by
      by_contra hnot
      have hDleQ : D ≤ q := by omega
      have hCell_qX : (D + 1) * X ≤ (q + 1) * X := by
        apply hLowMul
        omega
      omega
    have hDEq : D = q + 1 := by omega
    exact ⟨hDEq, hUpperForced hDEq⟩
  · rintro ⟨hDEq, _hCarry⟩
    have hBX_DX : (q + 1) * X ≤ D * X := by
      rw [hDEq]
    exact hBX_DX.trans hCellLower

end EnterpriseMath.Precision
