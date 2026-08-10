import EnterpriseMath.Arithmetic.IntegerRoot
import EnterpriseMath.Precision.QuotientRootFiber
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- A floor quotient cannot push the quotient index beyond the square root of
`k^2 / d`.  This helper is used to compare the Euclidean quotient scale with
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

/-- P018-T110: dividing a complete square-collapse basin by any integer `d ≥ 2`
can move the square-root index to only two adjacent values, and the base quotient
root is strictly below the original basin index.

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

/-- P018-T111: two successive natural-number floor quotients are exactly one
quotient by the product divisor.  This is established Euclidean-division
machinery, recorded here because it makes quotient precision paths flat. -/
theorem quotient_path_flat_two (n a b : ℕ) :
    n / a / b = n / (a * b) := by
  rw [Nat.div_div_eq_div_mul]

/-- P018-T111 consequence: factoring a nontrivial total divisor into two stages
does not create four final square-root branches.  After flattening the quotient
path, T110 applies once to the product divisor, so the final root index is still
one of two adjacent values. -/
theorem square_basin_two_step_div_root_pair
    {k a b n : ℕ} (hk : 0 < k) (ha : 2 ≤ a) (hb : 2 ≤ b)
    (hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2) :
    let d := a * b
    let j := root 2 (k ^ 2 / d)
    (root 2 (n / a / b) = j ∨ root 2 (n / a / b) = j + 1) ∧ j < k := by
  have hbOne : 1 ≤ b := by omega
  have hd : 2 ≤ a * b := by
    calc
      2 ≤ a := ha
      _ = a * 1 := by simp
      _ ≤ a * b := Nat.mul_le_mul_left a hbOne
  simpa [Nat.div_div_eq_div_mul] using
    (square_basin_div_root_pair (k := k) (d := a * b) (n := n)
      hk hd hnLower hnUpper)

/-- P018-T112: from root scale `k ≥ 3`, every nontrivial floor quotient of a
state below `(k+1)^2` lands strictly below the original square boundary `k^2`.
Hence its square-root index is strictly smaller than `k`.
-/
theorem square_basin_div_root_strict
    {k d n : ℕ} (hk : 3 ≤ k) (hd : 2 ≤ d)
    (hnUpper : n < (k + 1) ^ 2) :
    root 2 (n / d) < k := by
  have hd0 : 0 < d := by omega
  have hkTwo : (k + 1) ^ 2 ≤ k ^ 2 * 2 := by
    nlinarith
  have hTwoLeD : k ^ 2 * 2 ≤ k ^ 2 * d :=
    Nat.mul_le_mul_left (k ^ 2) hd
  have hnTarget : n < k ^ 2 * d :=
    lt_of_lt_of_le hnUpper (le_trans hkTwo hTwoLeD)
  have hQuotLt : n / d < k ^ 2 := by
    exact (Nat.div_lt_iff_lt_mul hd0).2 hnTarget
  exact (Nat.nthRoot_lt_iff (n := 2) (by decide)).2 hQuotLt

/-- P018-T113: inside one square basin, the upper T110 root branch has one exact
state threshold. If `j = R₂(floor(k²/d))`, the quotient root is `j+1` exactly
when the original state has reached `d*(j+1)^2`.
-/
theorem square_basin_div_upper_root_iff
    {k d n : ℕ} (hk : 0 < k) (hd : 2 ≤ d)
    (hnLower : k ^ 2 ≤ n) (hnUpper : n < (k + 1) ^ 2) :
    let j := root 2 (k ^ 2 / d)
    root 2 (n / d) = j + 1 ↔ d * (j + 1) ^ 2 ≤ n := by
  let j := root 2 (k ^ 2 / d)
  have hd0 : 0 < d := by omega
  have hpair :
      (root 2 (n / d) = j ∨ root 2 (n / d) = j + 1) ∧ j < k := by
    simpa [j] using
      (square_basin_div_root_pair (k := k) (d := d) (n := n)
        hk hd hnLower hnUpper)
  constructor
  · intro hroot
    have hpow : (j + 1) ^ 2 ≤ n / d := by
      rw [← hroot]
      exact Nat.pow_nthRoot_le (Or.inl (by decide))
    have hmul : (j + 1) ^ 2 * d ≤ n :=
      (Nat.le_div_iff_mul_le hd0).1 hpow
    simpa [Nat.mul_comm] using hmul
  · intro hthreshold
    have hmul : (j + 1) ^ 2 * d ≤ n := by
      simpa [Nat.mul_comm] using hthreshold
    have hpow : (j + 1) ^ 2 ≤ n / d :=
      (Nat.le_div_iff_mul_le hd0).2 hmul
    have hrootLower : j + 1 ≤ root 2 (n / d) :=
      (Nat.le_nthRoot_iff (n := 2) (by decide)).2 hpow
    rcases hpair.1 with hroot | hroot
    · omega
    · exact hroot

end EnterpriseMath.Precision
