import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

/-- A positive-order integer root changes across the adjacent boundary
`m-1 | m` exactly when the right endpoint is a positive perfect `r`-th power.

This is the root-side local atom behind the bounded future-action basis: floor
quotient actions can only change by one across an adjacent exact-state boundary,
and the root observes such a one-step change exactly at perfect powers. -/
theorem root_adjacent_jump_iff_power
    {r m : ℕ}
    (hr : 1 ≤ r)
    (hm : 1 ≤ m) :
    root r (m - 1) ≠ root r m ↔
      ∃ t : ℕ, 1 ≤ t ∧ m = t ^ r := by
  have hr0 : r ≠ 0 := by omega
  constructor
  · intro hne
    let t := root r m
    have htPos : 1 ≤ t := by
      exact (Nat.le_nthRoot_iff (n := r) hr0).2 (by simpa [t] using hm)
    have hLower : t ^ r ≤ m := by
      simpa [t] using Nat.pow_nthRoot_le (n := r) (a := m) (.inl hr0)
    have hUpper : m < (t + 1) ^ r := by
      simpa [t] using Nat.lt_pow_nthRoot_add_one hr0 m
    have hPower : m = t ^ r := by
      by_contra hnot
      have hStrict : t ^ r < m :=
        lt_of_le_of_ne hLower (Ne.symm hnot)
      have hPredLower : t ^ r ≤ m - 1 := by omega
      have hPredUpper : m - 1 < (t + 1) ^ r := by omega
      have hPredRoot : root r (m - 1) = t :=
        (root_eq_iff (p := r) (n := m - 1) (k := t) hr0).2
          ⟨hPredLower, hPredUpper⟩
      have hRoot : root r m = t := rfl
      exact hne (hPredRoot.trans hRoot.symm)
    exact ⟨t, htPos, hPower⟩
  · rintro ⟨t, htPos, rfl⟩
    intro hEq
    have hRootPower : root r (t ^ r) = t := root_pow hr0 t
    have hPredRoot : root r (t ^ r - 1) = t := hEq.trans hRootPower
    have hPredChar :=
      (root_eq_iff (p := r) (n := t ^ r - 1) (k := t) hr0).1 hPredRoot
    have hPowPos : 0 < t ^ r := pow_pos (by omega) r
    omega

/-- A positive floor quotient changes across the adjacent exact-state boundary
`q-1 | q` exactly when the action denominator divides the right endpoint.

This is the quotient-side local atom behind the bounded future-action basis. -/
theorem quotient_adjacent_jump_iff_dvd
    {q a : ℕ}
    (hq : 1 ≤ q)
    (ha : 1 ≤ a) :
    (q - 1) / a ≠ q / a ↔ a ∣ q := by
  have haPos : 0 < a := by omega
  constructor
  · intro hne
    by_contra hnotDvd
    have hModNe : q % a ≠ 0 := by
      intro hModZero
      exact hnotDvd (Nat.dvd_of_mod_eq_zero hModZero)
    have hModPos : 1 ≤ q % a := by omega
    have hModLt : q % a < a := Nat.mod_lt q haPos
    have hDecomp : q / a * a + q % a = q := by
      simpa [Nat.mul_comm] using Nat.div_add_mod q a
    have hLower : (q / a) * a ≤ q - 1 := by omega
    have hUpper : q - 1 < (q / a + 1) * a := by omega
    have hPredDiv : (q - 1) / a = q / a :=
      Nat.div_eq_of_lt_le hLower hUpper
    exact hne hPredDiv
  · rintro ⟨k, rfl⟩
    have hProdPos : 0 < a * k := by omega
    have hkPos : 1 ≤ k := by
      by_contra hzero
      have hkZero : k = 0 := by omega
      simp [hkZero] at hProdPos
    have hRight : (a * k) / a = k := by
      simpa using Nat.mul_div_cancel_left k haPos
    have hkDecomp : k = (k - 1) + 1 := by omega
    have hLower : (k - 1) * a ≤ a * k - 1 := by omega
    have hUpper : a * k - 1 < ((k - 1) + 1) * a := by
      rw [← hkDecomp]
      simpa [Nat.mul_comm] using (Nat.pred_lt (Nat.ne_of_gt hProdPos))
    have hLeft : (a * k - 1) / a = k - 1 :=
      Nat.div_eq_of_lt_le hLower hUpper
    rw [hLeft, hRight]
    omega

/-- If a positive action denominator divides a positive boundary `q`, the two
adjacent floor quotients are exactly `k-1` and `k` for a positive quotient
label `k`, with `q=a*k`. -/
theorem quotient_adjacent_values_of_dvd
    {q a : ℕ}
    (hq : 1 ≤ q)
    (ha : 1 ≤ a)
    (hDvd : a ∣ q) :
    ∃ k : ℕ,
      1 ≤ k ∧ q = a * k ∧ (q - 1) / a = k - 1 ∧ q / a = k := by
  rcases hDvd with ⟨k, rfl⟩
  have haPos : 0 < a := by omega
  have hProdPos : 0 < a * k := by omega
  have hkPos : 1 ≤ k := by
    by_contra hzero
    have hkZero : k = 0 := by omega
    simp [hkZero] at hProdPos
  have hRight : (a * k) / a = k := by
    simpa using Nat.mul_div_cancel_left k haPos
  have hkDecomp : k = (k - 1) + 1 := by omega
  have hLower : (k - 1) * a ≤ a * k - 1 := by omega
  have hUpper : a * k - 1 < ((k - 1) + 1) * a := by
    rw [← hkDecomp]
    simpa [Nat.mul_comm] using (Nat.pred_lt (Nat.ne_of_gt hProdPos))
  have hLeft : (a * k - 1) / a = k - 1 :=
    Nat.div_eq_of_lt_le hLower hUpper
  exact ⟨k, hkPos, rfl, hLeft, hRight⟩

/-- Exact local boundary law for a quotient-root future action.

Action `a` distinguishes exact adjacent states `q-1` and `q` through a positive
`r`-th integer root if and only if the right endpoint has the form

`q = a * t^r`

for a positive integer `t`. -/
theorem root_quotient_adjacent_jump_iff
    {r q a : ℕ}
    (hr : 1 ≤ r)
    (hq : 1 ≤ q)
    (ha : 1 ≤ a) :
    root r ((q - 1) / a) ≠ root r (q / a) ↔
      ∃ t : ℕ, 1 ≤ t ∧ q = a * t ^ r := by
  constructor
  · intro hJump
    have hQuotNe : (q - 1) / a ≠ q / a := by
      intro hEq
      exact hJump (congrArg (root r) hEq)
    have hDvd : a ∣ q :=
      (quotient_adjacent_jump_iff_dvd hq ha).1 hQuotNe
    obtain ⟨k, hkPos, hqEq, hLeft, hRight⟩ :=
      quotient_adjacent_values_of_dvd hq ha hDvd
    have hRootK : root r (k - 1) ≠ root r k := by
      intro hEq
      apply hJump
      simpa [hLeft, hRight] using hEq
    obtain ⟨t, htPos, hkPower⟩ :=
      (root_adjacent_jump_iff_power hr hkPos).1 hRootK
    refine ⟨t, htPos, ?_⟩
    calc
      q = a * k := hqEq
      _ = a * t ^ r := by rw [hkPower]
  · rintro ⟨t, htPos, hqEq⟩
    have hDvd : a ∣ q := ⟨t ^ r, hqEq⟩
    obtain ⟨k, hkPos, hqK, hLeft, hRight⟩ :=
      quotient_adjacent_values_of_dvd hq ha hDvd
    have hMul : a * k = a * t ^ r := hqK.symm.trans hqEq
    have hkPower : k = t ^ r := by
      nlinarith [ha, hMul]
    have hRootK : root r (k - 1) ≠ root r k :=
      (root_adjacent_jump_iff_power hr hkPos).2 ⟨t, htPos, hkPower⟩
    intro hEq
    apply hRootK
    simpa [hLeft, hRight] using hEq

/-- Positive `r`-power-free boundary: no nontrivial positive `r`-th power
factor divides `b`.  This local predicate is intentionally narrower than a
full factorization API; it is exactly what the forced-action theorem needs. -/
def RPowerFree (r b : ℕ) : Prop :=
  ∀ t : ℕ, 2 ≤ t → ¬t ^ r ∣ b

/-- Every `r`-power-free boundary forces its own future quotient action.

If action `a` distinguishes `b-1` from `b` through a positive `r`-th root and
`b` has no nontrivial `r`-th-power divisor, then necessarily `a=b`. -/
theorem rPowerFree_boundary_forces_action
    {r b a : ℕ}
    (hr : 1 ≤ r)
    (hbPos : 1 ≤ b)
    (ha : 1 ≤ a)
    (hbFree : RPowerFree r b)
    (hJump : root r ((b - 1) / a) ≠ root r (b / a)) :
    a = b := by
  obtain ⟨t, htPos, hbEq⟩ :=
    (root_quotient_adjacent_jump_iff hr hbPos ha).1 hJump
  have htOne : t = 1 := by
    by_contra hnotOne
    have htTwo : 2 ≤ t := by omega
    have hDvd : t ^ r ∣ b := by
      refine ⟨a, ?_⟩
      simpa [Nat.mul_comm] using hbEq
    exact hbFree t htTwo hDvd
  subst t
  simpa using hbEq.symm

end EnterpriseMath.Quotient
