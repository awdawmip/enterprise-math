import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Order.GaloisConnection.Basic

namespace EnterpriseMath.Scale

open EnterpriseMath.IntegerRoot

/-- Integer division by `b` commutes with positive integer `p`-th root after scaling the dividend
by `b^p`. This is the right-adjoint image of the commuting square
`(x * b)^p = x^p * b^p`. -/
theorem root_div_comm {p b : ℕ} (hp : p ≠ 0) (hb : 0 < b) (n : ℕ) :
    root p n / b = root p (n / b ^ p) := by
  have hPow := galoisConnection_pow_root hp
  have hDiv : GaloisConnection (fun x : ℕ => x * b) (fun x : ℕ => x / b) :=
    Nat.galoisConnection_mul_div hb
  have hDivPow : GaloisConnection (fun x : ℕ => x * b ^ p) (fun x : ℕ => x / b ^ p) :=
    Nat.galoisConnection_mul_div (Nat.pow_pos hb)
  exact hPow.u_comm_of_l_comm hPow hDivPow hDiv (fun x => by simp [mul_pow])

/-- Enterprise Math scaled root at base `b` and level `s`. -/
def scaledRoot (p b s n : ℕ) : ℕ :=
  root p (n * b ^ (p * s))

/-- Existing v0.1 scale compatibility, derived from `root_div_comm` rather than from a separate
real-number approximation argument. -/
theorem scaledRoot_succ_div {p b : ℕ} (hp : p ≠ 0) (hb : 0 < b) (s n : ℕ) :
    scaledRoot p b (s + 1) n / b = scaledRoot p b s n := by
  unfold scaledRoot
  rw [root_div_comm hp hb]
  congr 1
  rw [Nat.mul_add, Nat.mul_one, pow_add, ← Nat.mul_assoc]
  rw [Nat.mul_comm (n * b ^ (p * s)) (b ^ p)]
  exact Nat.mul_div_right (n * b ^ (p * s)) (Nat.pow_pos hb)

end EnterpriseMath.Scale
