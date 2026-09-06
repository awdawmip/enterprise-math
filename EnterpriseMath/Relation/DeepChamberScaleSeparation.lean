import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberScaleSeparation

/--
An uncut action `a ≤ Y` sends the cube scale `Y^3` no lower than the square
scale `Y^2`.
-/
theorem cube_quotient_ge_square_of_le
    {Y a : ℕ} (ha : 0 < a) (haY : a ≤ Y) :
    Y ^ 2 ≤ Y ^ 3 / a := by
  rw [Nat.le_div_iff_mul_le ha]
  calc
    Y ^ 2 * a ≤ Y ^ 2 * Y := Nat.mul_le_mul_left _ haY
    _ = Y ^ 3 := by ring

/--
Every overcut action `b > Y` sends the cube scale `Y^3` strictly below the
square scale `Y^2`.
-/
theorem cube_quotient_lt_square_of_lt
    {Y b : ℕ} (hY : 0 < Y) (hYb : Y < b) :
    Y ^ 3 / b < Y ^ 2 := by
  have hb : 0 < b := lt_trans hY hYb
  rw [Nat.div_lt_iff_lt_mul hb]
  calc
    Y ^ 3 = Y ^ 2 * Y := by ring
    _ < Y ^ 2 * b :=
      Nat.mul_lt_mul_of_pos_left hYb (Nat.pow_pos hY)

/--
With two overcut actions and one positive residual action, the common product
endpoint lies strictly below the original cutoff `Y`.
-/
theorem cube_product_quotient_lt_cutoff
    {Y a b c : ℕ}
    (hY : 0 < Y) (ha : 0 < a) (hYb : Y < b) (hYc : Y < c) :
    Y ^ 3 / (a * b * c) < Y := by
  have hb : 0 < b := lt_trans hY hYb
  have hc : 0 < c := lt_trans hY hYc
  have hden : 0 < a * b * c := Nat.mul_pos (Nat.mul_pos ha hb) hc
  rw [Nat.div_lt_iff_lt_mul hden]
  have hbc : Y * Y < b * c :=
    Nat.mul_lt_mul_of_lt_of_lt hYb hYc
  have ha1 : 1 ≤ a := Nat.one_le_iff_ne_zero.mpr (ne_of_gt ha)
  have hbc_le : b * c ≤ a * (b * c) := by
    simpa using Nat.mul_le_mul_right (b * c) ha1
  calc
    Y ^ 3 = Y * (Y * Y) := by ring
    _ < Y * (b * c) := Nat.mul_lt_mul_of_pos_left hbc hY
    _ ≤ Y * (a * (b * c)) := Nat.mul_le_mul_left Y hbc_le
    _ = Y * (a * b * c) := by ring

/-- Exact scale partition for one uncut and two overcut history labels. -/
theorem cube_deep_history_scale_partition
    {Y a b c : ℕ}
    (hY : 0 < Y) (ha : 0 < a) (haY : a ≤ Y)
    (hYb : Y < b) (hYc : Y < c) :
    Y ^ 2 ≤ Y ^ 3 / a ∧
      Y ^ 3 / b < Y ^ 2 ∧
      Y ^ 3 / c < Y ^ 2 ∧
      Y ^ 3 / (a * b * c) < Y := by
  exact ⟨
    cube_quotient_ge_square_of_le ha haY,
    cube_quotient_lt_square_of_lt hY hYb,
    cube_quotient_lt_square_of_lt hY hYc,
    cube_product_quotient_lt_cutoff hY ha hYb hYc
  ⟩

end EnterpriseMath.DeepChamberScaleSeparation
