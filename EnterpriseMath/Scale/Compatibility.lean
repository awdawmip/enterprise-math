import Mathlib.Order.GaloisConnection.Basic
import EnterpriseMath.Arithmetic.IntegerRoot

namespace EnterpriseMath.Scale

open EnterpriseMath.IntegerRoot

/-- Division by a scale factor commutes with a positive integer root when the input is divided
by the corresponding powered scale factor.

The proof is a direct specialization of mathlib's `GaloisConnection.u_comm_of_l_comm`: the
commuting square on lower adjoints is `(x * b)^p = x^p * b^p`. -/
theorem root_div_scale {p b : ℕ} (hp : p ≠ 0) (hb : 0 < b) (n : ℕ) :
    root p n / b = root p (n / b ^ p) := by
  have hbpow : 0 < b ^ p := Nat.pow_pos hb
  exact (galoisConnection_pow_root hp).u_comm_of_l_comm
    (galoisConnection_pow_root hp)
    (Nat.galoisConnection_mul_div hbpow)
    (Nat.galoisConnection_mul_div hb)
    (fun x => by simp [Nat.mul_pow])

/-- The v0.1 scaled root state, written in the same integer-only form as the specification. -/
def scaledRoot (p b s n : ℕ) : ℕ :=
  root p (n * b ^ (p * s))

/-- Formal version of v0.1 scale compatibility T010. Refining the root state by one base-`b`
scale and projecting back with integer division returns the coarser root state. -/
theorem scaledRoot_succ_div {p b : ℕ} (hp : p ≠ 0) (hb : 0 < b) (s n : ℕ) :
    scaledRoot p b (s + 1) n / b = scaledRoot p b s n := by
  rw [scaledRoot, root_div_scale hp hb, scaledRoot]
  apply congrArg (root p)
  have hbpow : 0 < b ^ p := Nat.pow_pos hb
  rw [Nat.mul_succ, pow_add, ← Nat.mul_assoc, Nat.mul_div_left _ hbpow]

end EnterpriseMath.Scale
