import EnterpriseMath.Precision.PowerQuotientCoalescenceGap
import EnterpriseMath.Precision.QuotientRootFiber
import EnterpriseMath.Precision.RootStateCountCarryUpper
import EnterpriseMath.Precision.TernaryBandCarryCount
import Mathlib.Data.Finset.Interval
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- A quantitative gap between two positive denominator scales forces their
floor quotients to be strictly separated.

This is the exact natural-number form needed for the low-root atlas.  It avoids
passing through real division: if `a<b` and the continuous gap numerator
`n*(b-a)` exceeds `a*b`, then the two integer quotients cannot coincide. -/
theorem strict_floor_quotient_of_gap
    {n a b : ℕ}
    (ha : 0 < a)
    (hab : a < b)
    (hgap : a * b < n * (b - a)) :
    n / b < n / a := by
  let q := n / b
  have hb : 0 < b := lt_trans ha hab
  have hqMul : q * b ≤ n := by
    dsimp [q]
    exact Nat.div_mul_le_self n b
  have hqSuccLe : q + 1 ≤ n / a := by
    apply (Nat.le_div_iff_mul_le ha).2
    by_contra hnot
    have hnLt : n < (q + 1) * a := by omega
    have hqCross : q * b < (q + 1) * a := lt_of_le_of_lt hqMul hnLt
    let g := b - a
    have hg : 0 < g := by
      dsimp [g]
      omega
    have hbDecomp : b = a + g := by
      dsimp [g]
      omega
    have hqGap : q * g < a := by
      rw [hbDecomp] at hqCross
      nlinarith
    have hSuccGap : (q + 1) * g < b := by
      rw [hbDecomp]
      nlinarith
    have hnScaled : n * g < ((q + 1) * a) * g :=
      Nat.mul_lt_mul_of_pos_right hnLt hg
    have hReverse : n * (b - a) < a * b := by
      calc
        n * (b - a) = n * g := by rfl
        _ < ((q + 1) * a) * g := hnScaled
        _ = a * ((q + 1) * g) := by ring
        _ < a * b := Nat.mul_lt_mul_of_pos_left hSuccGap ha
    omega
  dsimp [q] at hqSuccLe
  omega

/-- Denominators up through `D=floor(n/(H+1)^r)` always produce roots strictly
above the coalescence horizon `H`. -/
theorem root_state_high_denominator_above_horizon
    {s n d : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    1 ≤ d → d ≤ D → H < root (s + 1) (n / d) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 1 ≤ d → d ≤ D → H < root (s + 1) (n / d)
  intro hdPos hdD
  have hXPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hDMul : D * (H + 1) ^ (s + 1) ≤ n := by
    dsimp [D]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))
  have hdMul : d * (H + 1) ^ (s + 1) ≤ n := by
    exact le_trans
      (Nat.mul_le_mul_right ((H + 1) ^ (s + 1)) hdD)
      hDMul
  have hPow : (H + 1) ^ (s + 1) ≤ n / d := by
    apply (Nat.le_div_iff_mul_le (by omega)).2
    simpa [Nat.mul_comm] using hdMul
  have hRoot : H + 1 ≤ root (s + 1) (n / d) :=
    (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 hPow
  omega

/-- Denominators strictly past the high threshold can only produce roots at or
below the horizon. -/
theorem root_state_low_denominator_at_most_horizon
    {s n d : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    1 ≤ d → D < d → root (s + 1) (n / d) ≤ H := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 1 ≤ d → D < d → root (s + 1) (n / d) ≤ H
  intro hdPos hDd
  have hXPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hDivLt : n / (H + 1) ^ (s + 1) < d := by
    simpa [D] using hDd
  have hnLt : n < (H + 1) ^ (s + 1) * d :=
    (Nat.div_lt_iff_lt_mul hXPos).1 hDivLt
  have hQuotLt : n / d < (H + 1) ^ (s + 1) := by
    apply (Nat.div_lt_iff_lt_mul (by omega)).2
    simpa [Nat.mul_comm] using hnLt
  have hRootLt : root (s + 1) (n / d) < H + 1 :=
    (Nat.nthRoot_lt_iff (n := s + 1) (by omega)).2 hQuotLt
  omega

/-- The high-denominator branch is injective.  Any collision there would, by
the state-specific graded coalescence inequality, have to occur at or below the
same horizon that the branch is already proved to exceed. -/
theorem root_state_high_denominator_injective
    {s n d e : ℕ}
    (hn : 0 < n)
    (hdPos : 1 ≤ d)
    (hde : d < e) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    e ≤ D →
      root (s + 1) (n / d) ≠ root (s + 1) (n / e) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change e ≤ D → root (s + 1) (n / d) ≠ root (s + 1) (n / e)
  intro heD hEq
  have hdD : d ≤ D := le_trans (Nat.le_of_lt hde) heD
  have hHigh0 := root_state_high_denominator_above_horizon
    (s := s) (n := n) (d := d)
  have hHigh : H < root (s + 1) (n / d) := by
    simpa [H, D] using hHigh0 hdPos hdD
  have hCollision := state_distinct_divisor_root_collision_gap
    (n := n) (d := d) (e := e) (s := s)
    hn (by omega) hde hEq
  have hGapPos : 1 ≤ e - d := by omega
  have hPowerWeighted :
      (root (s + 1) (n / d)) ^ (s + 2) ≤
        (e - d) * (root (s + 1) (n / d)) ^ (s + 2) := by
    calc
      (root (s + 1) (n / d)) ^ (s + 2)
          = 1 * (root (s + 1) (n / d)) ^ (s + 2) := by simp
      _ ≤ (e - d) * (root (s + 1) (n / d)) ^ (s + 2) :=
        Nat.mul_le_mul_right _ hGapPos
  have hParentOrder : s + 2 ≠ 0 := by omega
  have hHUpper0 : (s + 1) * n - 1 < (H + 1) ^ (s + 2) := by
    dsimp [H]
    exact Nat.lt_pow_nthRoot_add_one hParentOrder ((s + 1) * n - 1)
  have hParentUpper : (s + 1) * n ≤ (H + 1) ^ (s + 2) := by
    omega
  have hRootPower :
      (H + 1) ^ (s + 2) ≤ (root (s + 1) (n / d)) ^ (s + 2) :=
    Nat.pow_le_pow_left (by omega) (s + 2)
  omega

/-- Every positive root strictly below the horizon is realized by a positive
denominator `d≤n`.

The proof is exact.  Bernoulli gives enough separation between `t^r` and
`(t+1)^r`; the horizon inequality upgrades that separation to a strict floor
quotient gap; the exact quotient-root fiber theorem then supplies a witness. -/
theorem root_state_low_root_realized
    {s n t : ℕ}
    (hn : 0 < n)
    (htPos : 0 < t) :
    let H := root (s + 2) ((s + 1) * n - 1)
    t < H →
      ∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = t := by
  let H := root (s + 2) ((s + 1) * n - 1)
  change t < H → ∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = t
  intro htH
  have hParentOrder : s + 2 ≠ 0 := by omega
  have hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1 := by
    dsimp [H]
    exact Nat.pow_nthRoot_le (Or.inl hParentOrder)
  have hParentLt : H ^ (s + 2) < (s + 1) * n := by
    omega
  have htSuccLe : t + 1 ≤ H := by omega
  have hNextPos : 0 < (t + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hScale : t * (t + 1) ^ (s + 1) < (s + 1) * n := by
    calc
      t * (t + 1) ^ (s + 1) <
          (t + 1) * (t + 1) ^ (s + 1) :=
        Nat.mul_lt_mul_of_pos_right (by omega) hNextPos
      _ = (t + 1) ^ (s + 2) := by
        rw [show s + 2 = (s + 1) + 1 by omega, pow_succ']
      _ ≤ H ^ (s + 2) := Nat.pow_le_pow_left htSuccLe (s + 2)
      _ < (s + 1) * n := hParentLt

  have hBern := pow_add_tangent_le_succ_pow t (s + 1)
  have htSPowPos : 0 < t ^ s := pow_pos htPos s
  have hTangentPos : 0 < (s + 1) * t ^ s := Nat.mul_pos (by omega) htSPowPos
  have hPowLt : t ^ (s + 1) < (t + 1) ^ (s + 1) := by
    omega
  have hDelta :
      (s + 1) * t ^ s ≤ (t + 1) ^ (s + 1) - t ^ (s + 1) := by
    omega
  have hScaled := Nat.mul_lt_mul_of_pos_right hScale htSPowPos
  have hGap :
      t ^ (s + 1) * (t + 1) ^ (s + 1) <
        n * ((t + 1) ^ (s + 1) - t ^ (s + 1)) := by
    calc
      t ^ (s + 1) * (t + 1) ^ (s + 1)
          = (t * (t + 1) ^ (s + 1)) * t ^ s := by
            rw [pow_succ']
            ring
      _ < ((s + 1) * n) * t ^ s := hScaled
      _ = n * ((s + 1) * t ^ s) := by ring
      _ ≤ n * ((t + 1) ^ (s + 1) - t ^ (s + 1)) :=
        Nat.mul_le_mul_left n hDelta

  have hDivGap :
      n / (t + 1) ^ (s + 1) < n / t ^ (s + 1) :=
    strict_floor_quotient_of_gap
      (a := t ^ (s + 1)) (b := (t + 1) ^ (s + 1))
      (pow_pos htPos (s + 1)) hPowLt hGap
  let d := n / (t + 1) ^ (s + 1) + 1
  have hdPos : 1 ≤ d := by
    dsimp [d]
    omega
  have hdUpper : d ≤ n / t ^ (s + 1) := by
    dsimp [d]
    omega
  have hdLeN : d ≤ n := by
    exact le_trans hdUpper (Nat.div_le_self n (t ^ (s + 1)))
  have hRoot : root (s + 1) (n / d) = t := by
    apply (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := t)
      (by omega) (by omega) htPos).2
    constructor
    · dsimp [d]
      omega
    · exact hdUpper
  exact ⟨d, hdPos, hdLeN, hRoot⟩

/-- The horizon root itself is the unique optional low state.  It is realized by
some positive denominator `d≤n` exactly when the horizon is positive and the
single carry threshold `(D+1)H^r≤n` holds. -/
theorem root_state_horizon_realized_iff
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = H) ↔
      0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change
    (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = H) ↔
      0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n
  constructor
  · rintro ⟨d, hdPos, hdN, hRoot⟩
    have hQuotOne : 1 ≤ n / d := by
      apply (Nat.le_div_iff_mul_le (by omega)).2
      simpa using hdN
    have hRootOne : 1 ≤ root (s + 1) (n / d) :=
      (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hQuotOne)
    have hHPos : 0 < H := by
      rw [hRoot] at hRootOne
      omega
    have hFiber := (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := H)
      (by omega) (by omega) hHPos).1 hRoot
    have hLower : D < d := by
      simpa [D] using hFiber.1
    have hUpper : d ≤ n / H ^ (s + 1) := hFiber.2
    have hCarryDiv : D + 1 ≤ n / H ^ (s + 1) := by omega
    have hHPowPos : 0 < H ^ (s + 1) := pow_pos hHPos (s + 1)
    have hCarry : (D + 1) * H ^ (s + 1) ≤ n :=
      (Nat.le_div_iff_mul_le hHPowPos).1 hCarryDiv
    exact ⟨hHPos, hCarry⟩
  · rintro ⟨hHPos, hCarry⟩
    let d := D + 1
    have hHPowPos : 0 < H ^ (s + 1) := pow_pos hHPos (s + 1)
    have hdUpper : d ≤ n / H ^ (s + 1) := by
      apply (Nat.le_div_iff_mul_le hHPowPos).2
      simpa [d] using hCarry
    have hdPos : 1 ≤ d := by
      dsimp [d]
      omega
    have hdLeN : d ≤ n :=
      le_trans hdUpper (Nat.div_le_self n (H ^ (s + 1)))
    have hRoot : root (s + 1) (n / d) = H := by
      apply (quotient_root_fiber_iff
        (r := s + 1) (n := n) (d := d) (t := H)
        (by omega) (by omega) hHPos).2
      constructor
      · dsimp [d, D]
        omega
      · exact hdUpper
    exact ⟨d, hdPos, hdLeN, hRoot⟩

end EnterpriseMath.Precision
