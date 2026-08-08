import Mathlib.Data.Nat.ModEq

namespace EnterpriseMath.Precision

/-- The coarse-unit carry produced by adding two explicit detail states at modulus `m`. -/
def carry (m u v : ℕ) : ℕ :=
  (u + v) / m

/-- Addition on the explicit residue/detail coordinate. -/
def digitAdd (m u v : ℕ) : ℕ :=
  (u + v) % m

/-- P018-T64: integer carry is exactly the additive defect of quotient projection. -/
theorem div_add_defect {m x y : ℕ} (hm : 0 < m) :
    (x + y) / m = x / m + y / m + carry m (x % m) (y % m) := by
  rw [Nat.add_div hm]
  unfold carry
  rw [Nat.add_div hm]
  simp [Nat.div_eq_of_lt (Nat.mod_lt x hm), Nat.div_eq_of_lt (Nat.mod_lt y hm)]

/-- A detail-state carry is binary when both details are canonical residues. -/
theorem carry_le_one {m u v : ℕ} (hm : 0 < m) (hu : u < m) (hv : v < m) :
    carry m u v ≤ 1 := by
  unfold carry
  rw [Nat.add_div hm]
  simp only [Nat.div_eq_of_lt hu, Nat.div_eq_of_lt hv, zero_add]
  by_cases h : m ≤ u % m + v % m <;> simp [h]

/-- Carry is normalized at zero. -/
@[simp] theorem carry_zero_left {m u : ℕ} (hu : u < m) :
    carry m 0 u = 0 := by
  simp [carry, Nat.div_eq_of_lt hu]

/-- Carry is normalized at zero. -/
@[simp] theorem carry_zero_right {m u : ℕ} (hu : u < m) :
    carry m u 0 = 0 := by
  simp [carry, Nat.div_eq_of_lt hu]

/-- Carry is symmetric. -/
theorem carry_comm (m u v : ℕ) : carry m u v = carry m v u := by
  simp [carry, Nat.add_comm]

/-- P018-T65: canonical carry satisfies the normalized 2-cocycle equation. -/
theorem carry_cocycle {m u v w : ℕ} (hm : 0 < m)
    (hu : u < m) (_hv : v < m) (hw : w < m) :
    carry m u v + carry m (digitAdd m u v) w =
      carry m v w + carry m u (digitAdd m v w) := by
  have hleft := div_add_defect (m := m) (x := u + v) (y := w) hm
  have hright := div_add_defect (m := m) (x := u) (y := v + w) hm
  calc
    carry m u v + carry m (digitAdd m u v) w
        = ((u + v) + w) / m := by
            symm
            simpa [carry, digitAdd, Nat.div_eq_of_lt hw, Nat.mod_eq_of_lt hw] using hleft
    _ = (u + (v + w)) / m := by rw [Nat.add_assoc]
    _ = carry m v w + carry m u (digitAdd m v w) := by
            simpa [carry, digitAdd, Nat.div_eq_of_lt hu, Nat.mod_eq_of_lt hu] using hright

end EnterpriseMath.Precision
