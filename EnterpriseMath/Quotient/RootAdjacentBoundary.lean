import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

/-- A positive-order integer root changes across `m-1 | m` exactly when `m`
is a positive perfect `r`-th power. -/
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
      have hPredLower : t ^ r ≤ m - 1 := by omega
      have hPredUpper : m - 1 < (t + 1) ^ r := by omega
      have hPredRoot : root r (m - 1) = t :=
        (root_eq_iff (p := r) (n := m - 1) (k := t) hr0).2
          ⟨hPredLower, hPredUpper⟩
      exact hne (hPredRoot.trans rfl)
    exact ⟨t, htPos, hPower⟩
  · rintro ⟨t, htPos, rfl⟩
    intro hEq
    have hRootPower : root r (t ^ r) = t := root_pow hr0 t
    have hPredRoot : root r (t ^ r - 1) = t := hEq.trans hRootPower
    have hPredChar :=
      (root_eq_iff (p := r) (n := t ^ r - 1) (k := t) hr0).1 hPredRoot
    have hPowPos : 0 < t ^ r := pow_pos (by omega) r
    omega

/-- A positive floor quotient changes across `q-1 | q` exactly when the action
denominator divides the right endpoint. -/
theorem quotient_adjacent_jump_iff_dvd
    {q a : ℕ}
    (hq : 1 ≤ q)
    (_ha : 1 ≤ a) :
    (q - 1) / a ≠ q / a ↔ a ∣ q := by
  have hqSucc : q - 1 + 1 = q := by omega
  constructor
  · intro hne
    by_contra hnotDvd
    have hnotSucc : ¬a ∣ (q - 1) + 1 := by
      simpa [hqSucc] using hnotDvd
    have hStable := Nat.succ_div_of_not_dvd hnotSucc
    have hEq : q / a = (q - 1) / a := by
      simpa [hqSucc] using hStable
    exact hne hEq.symm
  · intro hDvd
    have hSuccDvd : a ∣ (q - 1) + 1 := by
      simpa [hqSucc] using hDvd
    have hJump := Nat.succ_div_of_dvd hSuccDvd
    have hSucc : q / a = (q - 1) / a + 1 := by
      simpa [hqSucc] using hJump
    intro hEq
    omega

/-- Exact local boundary law for the quotient-root future action `a`. -/
theorem root_quotient_adjacent_jump_iff
    {r q a : ℕ}
    (hr : 1 ≤ r)
    (hq : 1 ≤ q)
    (ha : 1 ≤ a) :
    root r ((q - 1) / a) ≠ root r (q / a) ↔
      ∃ t : ℕ, 1 ≤ t ∧ q = a * t ^ r := by
  have haPos : 0 < a := by omega
  have hqSucc : q - 1 + 1 = q := by omega
  constructor
  · intro hRootJump
    have hQuotJump : (q - 1) / a ≠ q / a := by
      intro hEq
      exact hRootJump (congrArg (root r) hEq)
    have hDvd : a ∣ q := (quotient_adjacent_jump_iff_dvd hq ha).1 hQuotJump
    rcases hDvd with ⟨k, hqEq⟩
    have hkPos : 1 ≤ k := by
      by_contra hk
      have hkZero : k = 0 := by omega
      subst k
      simp at hqEq
      omega
    have hRight : q / a = k := by
      rw [hqEq]
      simpa using Nat.mul_div_cancel_left k haPos
    have hSuccDvd : a ∣ (q - 1) + 1 := by
      simpa [hqSucc] using (show a ∣ q from ⟨k, hqEq⟩)
    have hJump := Nat.succ_div_of_dvd hSuccDvd
    have hSucc : q / a = (q - 1) / a + 1 := by
      simpa [hqSucc] using hJump
    have hLeft : (q - 1) / a = k - 1 := by omega
    have hRootK : root r (k - 1) ≠ root r k := by
      simpa [hLeft, hRight] using hRootJump
    obtain ⟨t, htPos, hkPower⟩ :=
      (root_adjacent_jump_iff_power hr hkPos).1 hRootK
    exact ⟨t, htPos, hqEq.trans (by rw [hkPower])⟩
  · rintro ⟨t, htPos, hqEq⟩
    have htPowPos : 1 ≤ t ^ r := by
      have : 0 < t ^ r := pow_pos (by omega) r
      omega
    have hRight : q / a = t ^ r := by
      rw [hqEq]
      simpa using Nat.mul_div_cancel_left (t ^ r) haPos
    have hDvd : a ∣ q := ⟨t ^ r, hqEq⟩
    have hSuccDvd : a ∣ (q - 1) + 1 := by
      simpa [hqSucc] using hDvd
    have hJump := Nat.succ_div_of_dvd hSuccDvd
    have hSucc : q / a = (q - 1) / a + 1 := by
      simpa [hqSucc] using hJump
    have hLeft : (q - 1) / a = t ^ r - 1 := by omega
    have hRootPowerJump : root r (t ^ r - 1) ≠ root r (t ^ r) :=
      (root_adjacent_jump_iff_power hr htPowPos).2 ⟨t, htPos, rfl⟩
    simpa [hLeft, hRight] using hRootPowerJump

/-- Positive `r`-power-free boundary: no nontrivial positive `r`-th power
divides `b`. -/
def RPowerFree (r b : ℕ) : Prop :=
  ∀ t : ℕ, 2 ≤ t → ¬t ^ r ∣ b

/-- Every `r`-power-free boundary forces its own quotient action. -/
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
