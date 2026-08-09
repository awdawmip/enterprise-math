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

/-- Pure natural-number floor-gap kernel.

If `A=t*u` and the next scale `B` satisfies the tangent lower bound
`A+r*u <= B`, while the state lies beyond the horizon inequality `t*B < r*n`,
then the two floor quotients are strictly separated:

`floor(n/B) < floor(n/A)`.

This is the arithmetic existence mechanism behind all guaranteed low-root
fibers; no integer-root hypothesis occurs here. -/
theorem floor_quotient_strict_gap_of_tangent
    {n A B t r u : ℕ}
    (ht : 0 < t)
    (hr : 0 < r)
    (hu : 0 < u)
    (hA : A = t * u)
    (hTangent : A + r * u ≤ B)
    (hHorizon : t * B < r * n) :
    n / B < n / A := by
  have hApos : 0 < A := by
    rw [hA]
    exact Nat.mul_pos ht hu
  have hAB : A ≤ B := by omega
  have hMon : n / B ≤ n / A := Nat.div_le_div_left hAB hApos
  by_contra hnot
  have hEq : n / B = n / A := by omega
  let q := n / B
  have hQB : q * B ≤ n := by
    dsimp [q]
    exact Nat.div_mul_le_self n B
  have hDivSucc : n / A < n / A + 1 := Nat.lt_succ_self _
  have hNltA0 : n < (n / A + 1) * A :=
    (Nat.div_lt_iff_lt_mul hApos).1 hDivSucc
  have hNltA : n < (q + 1) * A := by
    dsimp [q]
    rw [hEq]
    exact hNltA0

  have hQBern : q * (A + r * u) ≤ q * B :=
    Nat.mul_le_mul_left q hTangent
  have hQStrict : q * (A + r * u) < (q + 1) * A :=
    hQBern.trans_lt (hQB.trans_lt hNltA)
  have hQRU : q * r * u < A := by
    nlinarith [hQStrict]
  have hQRUFactored : (q * r) * u < t * u := by
    simpa [hA, Nat.mul_assoc] using hQRU
  have hQRLt : q * r < t :=
    (Nat.mul_lt_mul_right hu).mp hQRUFactored

  have hTBern : t * (A + r * u) ≤ t * B :=
    Nat.mul_le_mul_left t hTangent
  have hCoeffLower : (t + r) * A ≤ t * B := by
    calc
      (t + r) * A = t * (A + r * u) := by
        rw [hA]
        ring
      _ ≤ t * B := hTBern
  have hRNUpper : r * n < r * ((q + 1) * A) :=
    Nat.mul_lt_mul_of_pos_left hNltA hr
  have hCoeffMul : (t + r) * A < (r * (q + 1)) * A := by
    calc
      (t + r) * A ≤ t * B := hCoeffLower
      _ < r * n := hHorizon
      _ < r * ((q + 1) * A) := hRNUpper
      _ = (r * (q + 1)) * A := by ring
  have hCoeff : t + r < r * (q + 1) :=
    (Nat.mul_lt_mul_right hApos).mp hCoeffMul
  have hTLtRQ : t < r * q := by
    nlinarith [hCoeff]
  nlinarith [hQRLt, hTLtRQ]

/-- Every positive root strictly below the coalescence horizon has a nonempty
exact denominator fiber.

For `H=R_(r+1)(r*n-1)` and every `1<=t<H`, there exists a positive denominator
`d` with `R_r(floor(n/d))=t`.  The proof factors through the exact denominator
fiber theorem and the pure floor-gap kernel above. -/
theorem low_root_fiber_nonempty
    {s n t : ℕ}
    (hn : 0 < n)
    (ht : 1 ≤ t) :
    let H := root (s + 2) ((s + 1) * n - 1)
    t < H → ∃ d : ℕ, 1 ≤ d ∧ root (s + 1) (n / d) = t := by
  let H := root (s + 2) ((s + 1) * n - 1)
  change t < H → ∃ d : ℕ, 1 ≤ d ∧ root (s + 1) (n / d) = t
  intro htH

  let A := t ^ (s + 1)
  let B := (t + 1) ^ (s + 1)
  let u := t ^ s
  have hu : 0 < u := by
    dsimp [u]
    exact pow_pos (by omega) s
  have hA : A = t * u := by
    dsimp [A, u]
    rw [pow_succ']
  have hBernRaw :=
    pow_add_mul_le_add_pow (R := ℕ) (a := t) (b := 1)
      (by omega) (by omega) (s + 1)
  have hTangent : A + (s + 1) * u ≤ B := by
    simpa [A, B, u] using hBernRaw

  have hHpos : 0 < H := by omega
  have hBLe : B ≤ H ^ (s + 1) := by
    dsimp [B]
    exact Nat.pow_le_pow_left (by omega) (s + 1)
  have hTBltHPow : t * B < H ^ (s + 2) := by
    calc
      t * B ≤ t * H ^ (s + 1) := Nat.mul_le_mul_left t hBLe
      _ < H * H ^ (s + 1) :=
        Nat.mul_lt_mul_of_pos_right htH (pow_pos hHpos (s + 1))
      _ = H ^ (s + 2) := by rw [pow_succ']
  have hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1 := by
    dsimp [H]
    exact Nat.pow_nthRoot_le (Or.inl (by omega))
  have hHorizon : t * B < (s + 1) * n := by
    calc
      t * B < H ^ (s + 2) := hTBltHPow
      _ ≤ (s + 1) * n - 1 := hHLower
      _ < (s + 1) * n := by
        have hProdPos : 0 < (s + 1) * n := Nat.mul_pos (by omega) hn
        omega

  have hDivGap : n / B < n / A :=
    floor_quotient_strict_gap_of_tangent
      (n := n) (A := A) (B := B) (t := t) (r := s + 1) (u := u)
      (by omega) (by omega) hu hA hTangent hHorizon

  let d := n / B + 1
  have hdPos : 1 ≤ d := by
    dsimp [d]
    omega
  have hLower : n / B < d := by
    dsimp [d]
    omega
  have hUpper : d ≤ n / A := by
    dsimp [d]
    omega
  have hFiber : root (s + 1) (n / d) = t := by
    apply (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := t)
      (by omega) (by omega) (by omega)).2
    simpa [A, B] using And.intro hLower hUpper
  exact ⟨d, hdPos, hFiber⟩

end EnterpriseMath.Precision
