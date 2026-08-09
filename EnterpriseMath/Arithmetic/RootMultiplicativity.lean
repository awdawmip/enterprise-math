import Mathlib.Tactic
import EnterpriseMath.Arithmetic.IntegerRoot

namespace EnterpriseMath.RootMultiplicativity

open EnterpriseMath.IntegerRoot

/-- The offset of a state above the perfect-power floor selected by its integer root. -/
def rootGap (p n : ℕ) : ℕ :=
  n - root p n ^ p

/-- The width from one perfect p-th power to the next. -/
def basinWidth (p k : ℕ) : ℕ :=
  (k + 1) ^ p - k ^ p

/-- The exact product-basin carry load used by P001. -/
def carryLoad (p a b : ℕ) : ℕ :=
  root p b ^ p * rootGap p a
    + root p a ^ p * rootGap p b
    + rootGap p a * rootGap p b

/-- P001-T01: positive-exponent integer roots are supermultiplicative. -/
theorem root_supermultiplicative {p a b : ℕ} (hp : p ≠ 0) :
    root p a * root p b ≤ root p (a * b) := by
  apply ((galoisConnection_pow_root hp)
    (root p a * root p b) (a * b)).mp
  change (root p a * root p b) ^ p ≤ a * b
  rw [mul_pow]
  exact Nat.mul_le_mul
    (Nat.pow_nthRoot_le (n := p) (a := a) (.inl hp))
    (Nat.pow_nthRoot_le (n := p) (a := b) (.inl hp))

/-- Arithmetic core of P001-T02 for two explicitly decomposed collapse basins. -/
theorem root_product_eq_of_basin_decomposition_iff
    {p a b r s u v : ℕ} (hp : p ≠ 0)
    (ha : a = r ^ p + u) (hb : b = s ^ p + v) :
    root p (a * b) = r * s ↔
      s ^ p * u + r ^ p * v + u * v < basinWidth p (r * s) := by
  have hbase : (r * s) ^ p ≤ a * b := by
    rw [ha, hb, mul_pow]
    gcongr <;> omega
  have hab : a * b = (r * s) ^ p + (s ^ p * u + r ^ p * v + u * v) := by
    rw [ha, hb, mul_pow]
    ring
  have hnext : (r * s) ^ p ≤ (r * s + 1) ^ p :=
    Nat.pow_le_pow_left (by omega) p
  constructor
  · intro hroot
    have hupper : a * b < (r * s + 1) ^ p :=
      ((root_eq_iff (p := p) (n := a * b) (k := r * s) hp).1 hroot).2
    rw [hab] at hupper
    simp only [basinWidth]
    omega
  · intro hload
    apply (root_eq_iff (p := p) (n := a * b) (k := r * s) hp).2
    refine ⟨hbase, ?_⟩
    rw [hab]
    simp only [basinWidth] at hload
    omega

/-- P001-T02: exact no-carry criterion for root multiplicativity. -/
theorem root_mul_eq_iff_carryLoad_lt {p a b : ℕ} (hp : p ≠ 0) :
    root p (a * b) = root p a * root p b ↔
      carryLoad p a b < basinWidth p (root p a * root p b) := by
  let r := root p a
  let s := root p b
  let u := a - r ^ p
  let v := b - s ^ p
  have hra : r ^ p ≤ a := by
    dsimp [r]
    exact Nat.pow_nthRoot_le (n := p) (a := a) (.inl hp)
  have hsb : s ^ p ≤ b := by
    dsimp [s]
    exact Nat.pow_nthRoot_le (n := p) (a := b) (.inl hp)
  have ha : a = r ^ p + u := by
    dsimp [u]
    omega
  have hb : b = s ^ p + v := by
    dsimp [v]
    omega
  have h := root_product_eq_of_basin_decomposition_iff
    (p := p) (a := a) (b := b) (r := r) (s := s) (u := u) (v := v) hp ha hb
  simpa [r, s, u, v, carryLoad, rootGap] using h

end EnterpriseMath.RootMultiplicativity
