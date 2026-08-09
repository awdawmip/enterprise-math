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

/-- The same P001 load written directly in fixed basin-root/offset coordinates. -/
def offsetLoad (p r s u v : ℕ) : ℕ :=
  s ^ p * u + r ^ p * v + u * v

/-- The upward carry in root-state units created by multiplying two states. -/
def rootCarry (p a b : ℕ) : ℕ :=
  root p (a * b) - root p a * root p b

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

/-- The product is its base perfect power plus exactly the P001 carry load. -/
theorem product_eq_base_pow_add_carryLoad {p a b : ℕ} (hp : p ≠ 0) :
    a * b = (root p a * root p b) ^ p + carryLoad p a b := by
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
  have hab : a * b = (r * s) ^ p + (s ^ p * u + r ^ p * v + u * v) := by
    rw [ha, hb, mul_pow]
    ring
  simpa [r, s, u, v, carryLoad, rootGap] using hab

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

/-- P001-T03 pointwise form: admissible carry counts are exactly those below the exact root carry. -/
theorem le_rootCarry_iff_threshold_le {p a b c : ℕ} (hp : p ≠ 0) :
    c ≤ rootCarry p a b ↔
      (root p a * root p b + c) ^ p - (root p a * root p b) ^ p
        ≤ carryLoad p a b := by
  have hsuper : root p a * root p b ≤ root p (a * b) :=
    root_supermultiplicative hp
  have hab :
      a * b = (root p a * root p b) ^ p + carryLoad p a b :=
    product_eq_base_pow_add_carryLoad hp
  have hmono :
      (root p a * root p b) ^ p ≤ (root p a * root p b + c) ^ p :=
    Nat.pow_le_pow_left (by omega) p
  constructor
  · intro hc
    have hstate : root p a * root p b + c ≤ root p (a * b) := by
      dsimp [rootCarry] at hc
      omega
    have hpow : (root p a * root p b + c) ^ p ≤ a * b :=
      ((galoisConnection_pow_root hp)
        (root p a * root p b + c) (a * b)).mpr hstate
    rw [hab] at hpow
    omega
  · intro hthreshold
    have hpow : (root p a * root p b + c) ^ p ≤ a * b := by
      rw [hab]
      omega
    have hstate : root p a * root p b + c ≤ root p (a * b) :=
      ((galoisConnection_pow_root hp)
        (root p a * root p b + c) (a * b)).mp hpow
    dsimp [rootCarry]
    omega

/-- P001-T03: `rootCarry` is the greatest admissible integer carry under the exact load. -/
theorem rootCarry_isGreatest {p a b : ℕ} (hp : p ≠ 0) :
    IsGreatest
      {c : ℕ |
        (root p a * root p b + c) ^ p - (root p a * root p b) ^ p
          ≤ carryLoad p a b}
      (rootCarry p a b) := by
  constructor
  · exact (le_rootCarry_iff_threshold_le hp).1 le_rfl
  · intro c hc
    exact (le_rootCarry_iff_threshold_le hp).2 hc

/-- P001-T03 zero-carry corollary: zero exact carry is equivalent to the T02 no-carry inequality. -/
theorem rootCarry_eq_zero_iff {p a b : ℕ} (hp : p ≠ 0) :
    rootCarry p a b = 0 ↔
      carryLoad p a b < basinWidth p (root p a * root p b) := by
  have hsuper : root p a * root p b ≤ root p (a * b) :=
    root_supermultiplicative hp
  constructor
  · intro hzero
    have heq : root p (a * b) = root p a * root p b := by
      dsimp [rootCarry] at hzero
      omega
    exact (root_mul_eq_iff_carryLoad_lt hp).1 heq
  · intro hload
    have heq : root p (a * b) = root p a * root p b :=
      (root_mul_eq_iff_carryLoad_lt hp).2 hload
    simp [rootCarry, heq]

/-- P001-T04 arithmetic core: fixed-basin carry load is monotone in both offsets. -/
theorem offsetLoad_mono {p r s u v u' v' : ℕ}
    (hu : u' ≤ u) (hv : v' ≤ v) :
    offsetLoad p r s u' v' ≤ offsetLoad p r s u v := by
  have h₁ : s ^ p * u' ≤ s ^ p * u :=
    Nat.mul_le_mul (le_rfl) hu
  have h₂ : r ^ p * v' ≤ r ^ p * v :=
    Nat.mul_le_mul (le_rfl) hv
  have h₃ : u' * v' ≤ u * v :=
    Nat.mul_le_mul hu hv
  simp only [offsetLoad]
  omega

/-- P001-T04: every smaller offset pair remains in the no-carry lower set. -/
theorem noCarry_downward {p r s u v u' v' : ℕ}
    (hu : u' ≤ u) (hv : v' ≤ v)
    (hno : offsetLoad p r s u v < basinWidth p (r * s)) :
    offsetLoad p r s u' v' < basinWidth p (r * s) :=
  lt_of_le_of_lt (offsetLoad_mono hu hv) hno

end EnterpriseMath.RootMultiplicativity
