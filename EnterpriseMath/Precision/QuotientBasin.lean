import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- A floor quotient cannot push the quotient index beyond the square root of
`k^2 / d`. This helper is used to compare the Euclidean quotient scale with
square-root precision. -/
theorem div_square_le_square_div {k d : ℕ} (hd : 0 < d) :
    (k / d) ^ 2 ≤ k ^ 2 / d := by
  rw [Nat.le_div_iff_mul_le hd]
  calc
    (k / d) ^ 2 * d = (k / d) * ((k / d) * d) := by
      simp [pow_two, Nat.mul_assoc]
    _ ≤ (k / d) * k := Nat.mul_le_mul_left _ (Nat.div_mul_le_self k d)
    _ ≤ k * k := Nat.mul_le_mul_right k (Nat.div_le_self k d)
    _ = k ^ 2 := by simp [pow_two]

/-- P018-T182: dividing a complete square-collapse basin by any integer `d ≥ 2`
can move the square-root index to only two adjacent values, and the base quotient
root is strictly below the original basin index.

This theorem entered `main` concurrently under the provisional identifier
P018-T110. PR #68 already had an earlier validated T110–T181 sequence, so the
integration relabels only this concurrent theorem as T182; the theorem statement
and proof are unchanged.

If `j = R₂(⌊k²/d⌋)` and `k² ≤ n < (k+1)²`, then
`R₂(⌊n/d⌋) ∈ {j,j+1}` and `j < k`.
-/
theorem square_basin_div_root_pair
    {k d n : ℕ} (hk : 0 < k) (hd : 2 ≤ d)
    (hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2) :
    let j := root 2 (k ^ 2 / d)
    (root 2 (n / d) = j ∨ root 2 (n / d) = j + 1) ∧ j < k := by
  let j := root 2 (k ^ 2 / d)
  have hd0 : 0 < d := by omega

  have hjPow : j ^ 2 ≤ k ^ 2 / d := by
    dsimp [j]
    exact Nat.pow_nthRoot_le (Or.inl (by decide))

  have hkDivLe : k ^ 2 / d ≤ n / d := Nat.div_le_div_right hnLower
  have hjPowLe : j ^ 2 ≤ n / d := le_trans hjPow hkDivLe
  have hjLe : j ≤ root 2 (n / d) := by
    exact (Nat.le_nthRoot_iff (n := 2) (by decide)).2 hjPowLe

  have hBaseRootUpper : k ^ 2 / d < (j + 1) ^ 2 := by
    dsimp [j]
    exact Nat.lt_pow_nthRoot_add_one (by decide) (k ^ 2 / d)
  have hkSqLt : k ^ 2 < (j + 1) ^ 2 * d := by
    exact (Nat.div_lt_iff_lt_mul hd0).1 hBaseRootUpper

  have hFloorLeRoot : k / d ≤ j := by
    exact (Nat.le_nthRoot_iff (n := 2) (by decide)).2
      (div_square_le_square_div hd0)

  have hkLtBlock : k < (j + 1) * d := by
    calc
      k < k / d * d + d := @Nat.lt_div_mul_add k d hd0
      _ = (k / d + 1) * d := by ring
      _ ≤ (j + 1) * d :=
        Nat.mul_le_mul_right d (Nat.add_le_add_right hFloorLeRoot 1)

  have hkSqSuccLe : k ^ 2 + 1 ≤ (j + 1) ^ 2 * d := by
    omega
  have hDoubleKLe : 2 * k ≤ 2 * ((j + 1) * d) := by
    exact Nat.mul_le_mul_left 2 (Nat.le_of_lt hkLtBlock)
  have hIndexStep : (j + 1) ^ 2 + 2 * (j + 1) ≤ (j + 2) ^ 2 := by
    nlinarith
  have hkNextSqLe : (k + 1) ^ 2 ≤ (j + 2) ^ 2 * d := by
    calc
      (k + 1) ^ 2 = (k ^ 2 + 1) + 2 * k := by ring
      _ ≤ (j + 1) ^ 2 * d + 2 * ((j + 1) * d) :=
        Nat.add_le_add hkSqSuccLe hDoubleKLe
      _ = ((j + 1) ^ 2 + 2 * (j + 1)) * d := by ring
      _ ≤ (j + 2) ^ 2 * d := Nat.mul_le_mul_right d hIndexStep

  have hnLtTarget : n < (j + 2) ^ 2 * d := lt_of_lt_of_le hnUpper hkNextSqLe
  have hQuotLt : n / d < (j + 2) ^ 2 := by
    exact (Nat.div_lt_iff_lt_mul hd0).2 hnLtTarget
  have hRootLt : root 2 (n / d) < j + 2 := by
    exact (Nat.nthRoot_lt_iff (n := 2) (by decide)).2 hQuotLt

  have hkSqPos : 0 < k ^ 2 := by positivity
  have hkSqLtDouble : k ^ 2 < k ^ 2 + k ^ 2 :=
    Nat.lt_add_of_pos_right hkSqPos
  have hDoubleLeMul : k ^ 2 + k ^ 2 ≤ k ^ 2 * d := by
    calc
      k ^ 2 + k ^ 2 = k ^ 2 * 2 := by simp [Nat.mul_two]
      _ ≤ k ^ 2 * d := Nat.mul_le_mul_left (k ^ 2) hd
  have hkSqLtMul : k ^ 2 < k ^ 2 * d := lt_of_lt_of_le hkSqLtDouble hDoubleLeMul
  have hBaseDivLt : k ^ 2 / d < k ^ 2 := by
    exact (Nat.div_lt_iff_lt_mul hd0).2 hkSqLtMul
  have hjLt : j < k := by
    dsimp [j]
    exact (Nat.nthRoot_lt_iff (n := 2) (by decide)).2 hBaseDivLt

  constructor
  · omega
  · exact hjLt

end EnterpriseMath.Precision
