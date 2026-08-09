import EnterpriseMath.Precision.QuotientRootFiber
import EnterpriseMath.Precision.PowerQuotientCoalescenceGap
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Every denominator in the high branch `1 <= d <= D` has quotient-root
strictly above the coalescence horizon `H`.

Here
`H = R_(r+1)(r*n-1)` and `D = floor(n/(H+1)^r)`
with shifted Lean notation `r=s+1`. -/
theorem high_denominator_root_above_horizon
    {s n d : ℕ}
    (hd : 1 ≤ d) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    d ≤ D → H < root (s + 1) (n / d) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change d ≤ D → H < root (s + 1) (n / d)
  intro hdD
  have hDLower : D * (H + 1) ^ (s + 1) ≤ n := by
    dsimp [D]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))
  have hdLower : d * (H + 1) ^ (s + 1) ≤ n := by
    exact (Nat.mul_le_mul_right ((H + 1) ^ (s + 1)) hdD).trans hDLower
  have hRootLower : (H + 1) ^ (s + 1) ≤ n / d := by
    apply (Nat.le_div_iff_mul_le (by omega)).2
    simpa [Nat.mul_comm] using hdLower
  have hLeRoot : H + 1 ≤ root (s + 1) (n / d) :=
    (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 hRootLower
  omega

/-- The high denominator branch is collision-free.

For one positive state `n`, denominators in `1,...,D` cannot share the same
`r`-th quotient root.  This combines the state-specific graded coalescence
kernel with the exact horizon definition. -/
theorem high_denominator_root_injective
    {s n d e : ℕ}
    (hn : 0 < n)
    (hd : 1 ≤ d)
    (he : 1 ≤ e) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    d ≤ D → e ≤ D →
      root (s + 1) (n / d) = root (s + 1) (n / e) → d = e := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change d ≤ D → e ≤ D →
    root (s + 1) (n / d) = root (s + 1) (n / e) → d = e
  intro hdD heD hEq

  have hNoCollision :
      ∀ {a b : ℕ},
        1 ≤ a → 1 ≤ b → a ≤ D → b ≤ D → a < b →
        root (s + 1) (n / a) = root (s + 1) (n / b) → False := by
    intro a b ha hb haD hbD hab hRoot
    let t := root (s + 1) (n / a)
    have htH : H < t := by
      dsimp [t]
      exact high_denominator_root_above_horizon ha haD
    have hGap := state_distinct_divisor_root_collision_gap
      (n := n) (d := a) (e := b) (s := s)
      hn (by omega) hab hRoot
    have hGapOne : 1 ≤ b - a := by omega
    have hPowerLt : t ^ (s + 2) < (s + 1) * n := by
      have hOneMul : t ^ (s + 2) ≤ (b - a) * t ^ (s + 2) := by
        simpa using Nat.mul_le_mul_right (t ^ (s + 2)) hGapOne
      exact hOneMul.trans_lt hGap

    have hParentOrder : s + 2 ≠ 0 := by omega
    have hHUpper :
        (s + 1) * n - 1 < (H + 1) ^ (s + 2) := by
      dsimp [H]
      exact Nat.lt_pow_nthRoot_add_one hParentOrder ((s + 1) * n - 1)
    have hParentLe : (s + 1) * n ≤ (H + 1) ^ (s + 2) := by
      have hProdPos : 0 < (s + 1) * n := Nat.mul_pos (by omega) hn
      omega
    have hPowerLe : (H + 1) ^ (s + 2) ≤ t ^ (s + 2) := by
      exact Nat.pow_le_pow_left (by omega) (s + 2)
    omega

  by_contra hne
  by_cases hde : d < e
  · exact hNoCollision hd he hdD heD hde hEq
  · have hed : e < d := by omega
    exact hNoCollision he hd heD hdD hed hEq.symm

end EnterpriseMath.Precision
