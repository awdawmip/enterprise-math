import EnterpriseMath.Precision.QuotientRootFiber
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- The quotient-root profile in denominator coordinates. -/
def quotientRootProfile (r n d : ℕ) : ℕ :=
  root r (n / d)

/-- The powered floor profile in root-state coordinates. -/
def floorPowerProfile (r n t : ℕ) : ℕ :=
  n / t ^ r

/-- Quotient-root and powered-floor profiles form an exact antitone polarity on
positive coordinates.  Equivalently, both describe the same lattice region
`d * t^r ≤ n` from opposite axes. -/
theorem quotient_root_floor_power_polarity
    {r n d t : ℕ}
    (hr : 1 ≤ r)
    (hd : 0 < d)
    (ht : 0 < t) :
    t ≤ quotientRootProfile r n d ↔ d ≤ floorPowerProfile r n t := by
  have hr0 : r ≠ 0 := by omega
  have htPow : 0 < t ^ r := pow_pos ht r
  dsimp [quotientRootProfile, floorPowerProfile]
  constructor
  · intro hRoot
    have hPow : t ^ r ≤ n / d :=
      (Nat.le_nthRoot_iff (n := r) hr0).1 hRoot
    have hMul : t ^ r * d ≤ n :=
      (Nat.le_div_iff_mul_le hd).1 hPow
    apply (Nat.le_div_iff_mul_le htPow).2
    simpa [Nat.mul_comm] using hMul
  · intro hFloor
    have hMul : d * t ^ r ≤ n :=
      (Nat.le_div_iff_mul_le htPow).1 hFloor
    have hPow : t ^ r ≤ n / d := by
      apply (Nat.le_div_iff_mul_le hd).2
      simpa [Nat.mul_comm] using hMul
    exact (Nat.le_nthRoot_iff (n := r) hr0).2 hPow

/-- A positive quotient-root state occurs exactly at a strict drop of the
powered-floor profile.  No horizon or carry decomposition is needed. -/
theorem quotient_root_state_iff_floor_power_drop
    {r n t : ℕ}
    (hr : 1 ≤ r)
    (ht : 0 < t) :
    (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ quotientRootProfile r n d = t) ↔
      floorPowerProfile r n (t + 1) < floorPowerProfile r n t := by
  constructor
  · rintro ⟨d, hdPos, _hdN, hRoot⟩
    have hFiber :=
      (quotient_root_fiber_iff
        (r := r) (n := n) (d := d) (t := t)
        hr (by omega) ht).1
        (by simpa [quotientRootProfile] using hRoot)
    simpa [floorPowerProfile] using lt_of_lt_of_le hFiber.1 hFiber.2
  · intro hDrop
    let d := floorPowerProfile r n (t + 1) + 1
    have hdPos : 1 ≤ d := by
      dsimp [d]
      omega
    have hdUpper : d ≤ floorPowerProfile r n t := by
      dsimp [d]
      omega
    have hdN : d ≤ n := by
      exact le_trans hdUpper (Nat.div_le_self n (t ^ r))
    have hRoot : quotientRootProfile r n d = t := by
      apply (quotient_root_fiber_iff
        (r := r) (n := n) (d := d) (t := t)
        hr (by omega) ht).2
      constructor
      · simpa [d, floorPowerProfile]
      · simpa [floorPowerProfile] using hdUpper
    exact ⟨d, hdPos, hdN, hRoot⟩

/-- Dually, a positive powered-floor value occurs exactly at a strict drop of
the quotient-root profile.  This is the row/column corner symmetry of the
associated Ferrers diagram. -/
theorem floor_power_value_iff_quotient_root_drop
    {r n d : ℕ}
    (hr : 1 ≤ r)
    (hd : 0 < d) :
    (∃ t : ℕ, 0 < t ∧ floorPowerProfile r n t = d) ↔
      quotientRootProfile r n (d + 1) < quotientRootProfile r n d := by
  constructor
  · rintro ⟨t, ht, hFloor⟩
    have hRight : t ≤ quotientRootProfile r n d := by
      apply (quotient_root_floor_power_polarity
        (r := r) (n := n) (d := d) (t := t) hr hd ht).2
      simpa [hFloor]
    have hNotLeft : ¬ t ≤ quotientRootProfile r n (d + 1) := by
      intro hLeft
      have hSuccLe :=
        (quotient_root_floor_power_polarity
          (r := r) (n := n) (d := d + 1) (t := t)
          hr (by omega) ht).1 hLeft
      rw [hFloor] at hSuccLe
      omega
    omega
  · intro hDrop
    let t := quotientRootProfile r n (d + 1) + 1
    have ht : 0 < t := by
      dsimp [t]
      omega
    have hRight : t ≤ quotientRootProfile r n d := by
      dsimp [t]
      omega
    have hdLe : d ≤ floorPowerProfile r n t :=
      (quotient_root_floor_power_polarity
        (r := r) (n := n) (d := d) (t := t) hr hd ht).1 hRight
    have hNotSucc : ¬ d + 1 ≤ floorPowerProfile r n t := by
      intro hSucc
      have hLeft :=
        (quotient_root_floor_power_polarity
          (r := r) (n := n) (d := d + 1) (t := t)
          hr (by omega) ht).2 hSucc
      dsimp [t] at hLeft
      omega
    have hEq : floorPowerProfile r n t = d := by omega
    exact ⟨t, ht, hEq⟩

end EnterpriseMath.Precision
