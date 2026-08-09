import EnterpriseMath.Precision.BinaryRootAtlas
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Every denominator after the high cutoff lies at or below the root horizon.

For
`H = R_(r+1)(r*n-1)` and `D = floor(n/(H+1)^r)`, any positive `d>D` satisfies
`R_r(floor(n/d)) <= H`.  Together with the high-branch theorem this gives the
exact high/low separation at denominator `D`. -/
theorem denominator_after_cutoff_root_at_most_horizon
    {s n d : ℕ}
    (hd : 1 ≤ d) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    D < d → root (s + 1) (n / d) ≤ H := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change D < d → root (s + 1) (n / d) ≤ H
  intro hDd
  have hPowPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hDenGap : n / (H + 1) ^ (s + 1) < d := by
    simpa [D] using hDd
  have hNUpper : n < d * (H + 1) ^ (s + 1) :=
    (Nat.div_lt_iff_lt_mul hPowPos).1 hDenGap
  have hQuotUpper : n / d < (H + 1) ^ (s + 1) := by
    apply (Nat.div_lt_iff_lt_mul (by omega)).2
    simpa [Nat.mul_comm] using hNUpper
  have hRootLower :
      (root (s + 1) (n / d)) ^ (s + 1) ≤ n / d := by
    exact Nat.pow_nthRoot_le (Or.inl (by omega))
  by_contra hnot
  have hHLe : H + 1 ≤ root (s + 1) (n / d) := by omega
  have hPowLe :
      (H + 1) ^ (s + 1) ≤ (root (s + 1) (n / d)) ^ (s + 1) :=
    Nat.pow_le_pow_left hHLe (s + 1)
  omega

/-- Exact binary condition for the final low root `H`.

Assume `H>0`.  The horizon root occurs for some positive denominator iff the
first denominator after the high cutoff already lies below the horizon upper
fiber endpoint:

`(D+1) * H^r <= n`.

Thus every low root below `H` is forced (by `low_root_fiber_nonempty`) and only
`H` contributes one binary atlas bit. -/
theorem horizon_root_fiber_nonempty_iff
    {s n : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      ((∃ d : ℕ, 1 ≤ d ∧ root (s + 1) (n / d) = H) ↔
        (D + 1) * H ^ (s + 1) ≤ n) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 0 < H →
    ((∃ d : ℕ, 1 ≤ d ∧ root (s + 1) (n / d) = H) ↔
      (D + 1) * H ^ (s + 1) ≤ n)
  intro hH
  have hHPow : 0 < H ^ (s + 1) := pow_pos hH (s + 1)
  constructor
  · rintro ⟨d, hd, hRoot⟩
    have hFiber :=
      (quotient_root_fiber_iff
        (r := s + 1) (n := n) (d := d) (t := H)
        (by omega) (by omega) hH).1 hRoot
    have hDlt : D < d := by
      simpa [D] using hFiber.1
    have hD1 : D + 1 ≤ d := by omega
    have hdUpper : d ≤ n / H ^ (s + 1) := hFiber.2
    have hDUpper : D + 1 ≤ n / H ^ (s + 1) := hD1.trans hdUpper
    exact (Nat.le_div_iff_mul_le hHPow).1 hDUpper
  · intro hThreshold
    let d := D + 1
    have hd : 1 ≤ d := by
      dsimp [d]
      omega
    have hLower : n / (H + 1) ^ (s + 1) < d := by
      dsimp [d, D]
      omega
    have hUpper : d ≤ n / H ^ (s + 1) :=
      (Nat.le_div_iff_mul_le hHPow).2 hThreshold
    refine ⟨d, hd, ?_⟩
    apply (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := H)
      (by omega) (by omega) hH).2
    exact ⟨hLower, hUpper⟩

end EnterpriseMath.Precision
