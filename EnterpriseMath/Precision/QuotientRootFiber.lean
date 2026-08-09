import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Exact positive-denominator fiber of one positive integer-root observation.

For positive root order `r`, denominator `d`, and target root `t`,

`root r (n / d) = t`

if and only if the denominator label lies in the exact consecutive interval

`n / (t+1)^r < d <= n / t^r`.

This is the state/root-dual of the quotient-basin transport theorem: fixing the
state and observed root produces one exact interval in total-denominator space.
No power-basin, primality, or real-root assumption is used. -/
theorem quotient_root_fiber_iff
    {r n d t : ℕ}
    (hr : 1 ≤ r)
    (hd : 0 < d)
    (ht : 0 < t) :
    root r (n / d) = t ↔
      n / (t + 1) ^ r < d ∧ d ≤ n / t ^ r := by
  have hr0 : r ≠ 0 := by omega
  have htPow : 0 < t ^ r := pow_pos ht r
  have htSuccPow : 0 < (t + 1) ^ r := pow_pos (by omega) r
  rw [EnterpriseMath.IntegerRoot.root_eq_iff (p := r) (n := n / d) (k := t) hr0]
  constructor
  · rintro ⟨hRootLower, hRootUpper⟩
    have hLowerMul : t ^ r * d ≤ n :=
      (Nat.le_div_iff_mul_le hd).1 hRootLower
    have hDenUpper : d ≤ n / t ^ r := by
      apply (Nat.le_div_iff_mul_le htPow).2
      simpa [Nat.mul_comm] using hLowerMul
    have hUpperMul : n < (t + 1) ^ r * d :=
      (Nat.div_lt_iff_lt_mul hd).1 hRootUpper
    have hDenLower : n / (t + 1) ^ r < d := by
      apply (Nat.div_lt_iff_lt_mul htSuccPow).2
      simpa [Nat.mul_comm] using hUpperMul
    exact ⟨hDenLower, hDenUpper⟩
  · rintro ⟨hDenLower, hDenUpper⟩
    have hLowerMul : d * t ^ r ≤ n :=
      (Nat.le_div_iff_mul_le htPow).1 hDenUpper
    have hRootLower : t ^ r ≤ n / d := by
      apply (Nat.le_div_iff_mul_le hd).2
      simpa [Nat.mul_comm] using hLowerMul
    have hUpperMul : n < d * (t + 1) ^ r :=
      (Nat.div_lt_iff_lt_mul htSuccPow).1 hDenLower
    have hRootUpper : n / d < (t + 1) ^ r := by
      apply (Nat.div_lt_iff_lt_mul hd).2
      simpa [Nat.mul_comm] using hUpperMul
    exact ⟨hRootLower, hRootUpper⟩

/-- The exact positive fiber capacity is the difference of the two quotient
endpoints.  This theorem packages only the interval cardinality arithmetic;
`quotient_root_fiber_iff` supplies the semantic identification with root states.
-/
theorem quotient_root_fiber_capacity
    {r n t : ℕ}
    (hr : 1 ≤ r)
    (ht : 0 < t) :
    ((n / t ^ r) + 1) - ((n / (t + 1) ^ r) + 1) =
      n / t ^ r - n / (t + 1) ^ r := by
  omega

end EnterpriseMath.Precision
