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

end EnterpriseMath.Quotient
