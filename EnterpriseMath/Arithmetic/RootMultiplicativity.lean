import EnterpriseMath.Arithmetic.IntegerRoot

namespace EnterpriseMath.RootMultiplicativity

open EnterpriseMath.IntegerRoot

/-- P001-T01: positive-exponent integer roots are supermultiplicative. -/
theorem root_supermultiplicative {p a b : ℕ} (hp : p ≠ 0) :
    root p a * root p b ≤ root p (a * b) := by
  apply ((galoisConnection_pow_root hp)
    (root p a * root p b) (a * b)).mp
  rw [mul_pow]
  exact Nat.mul_le_mul
    (Nat.pow_nthRoot_le (n := p) (a := a) (.inl hp))
    (Nat.pow_nthRoot_le (n := p) (a := b) (.inl hp))

end EnterpriseMath.RootMultiplicativity
