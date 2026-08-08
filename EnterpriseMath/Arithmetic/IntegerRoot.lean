import Mathlib.Analysis.SpecialFunctions.Pow.NthRootLemmas
import EnterpriseMath.Order.Adjoint

namespace EnterpriseMath.IntegerRoot

/-- Enterprise Math notation is implemented by mathlib's existing integer nth-root primitive. -/
abbrev root : ℕ → ℕ → ℕ := Nat.nthRoot

/-- Perfect-power collapse specialized to natural-number nth roots. -/
def collapse (p n : ℕ) : ℕ :=
  root p n ^ p

/-- For positive exponents, powering is left adjoint to `Nat.nthRoot`. -/
theorem galoisConnection_pow_root {p : ℕ} (hp : p ≠ 0) :
    GaloisConnection (fun a : ℕ => a ^ p) (root p) := by
  intro a b
  exact (Nat.le_nthRoot_iff (n := p) (a := a) (b := b) hp).symm

/-- The Enterprise Math collapse is reductive. -/
theorem collapse_le {p : ℕ} (hp : p ≠ 0) (n : ℕ) : collapse p n ≤ n := by
  exact Nat.pow_nthRoot_le (n := p) (a := n) (.inl hp)

/-- Perfect powers are recovered exactly by the integer root. -/
theorem root_pow {p : ℕ} (hp : p ≠ 0) (n : ℕ) : root p (n ^ p) = n := by
  exact Nat.nthRoot_pow hp n

/-- Perfect-power collapse is idempotent. -/
theorem collapse_idempotent {p : ℕ} (hp : p ≠ 0) (n : ℕ) :
    collapse p (collapse p n) = collapse p n := by
  simp [collapse, root, Nat.nthRoot_pow hp]

/-- The fixed points of perfect-power collapse are exactly the perfect `p`-th powers. -/
theorem collapse_eq_self_iff {p : ℕ} (hp : p ≠ 0) (n : ℕ) :
    collapse p n = n ↔ ∃ k : ℕ, k ^ p = n := by
  simpa [collapse, root] using (Nat.exists_pow_eq_iff' (n := p) (a := n) hp).symm

/-- Iterated integer roots compose along multiplication of positive exponents.

This theorem is currently a P008 upstream-candidate audit item: it is derived from mathlib's
existing Galois-connection API, but no theorem with this statement was found in the pinned
mathlib source during the initial audit. -/
theorem root_mul {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0) (n : ℕ) :
    root (p * q) n = root p (root q n) := by
  have hpq : p * q ≠ 0 := Nat.mul_ne_zero hp hq
  have gcPQ := galoisConnection_pow_root hpq
  have gcComp := (galoisConnection_pow_root hp).compose (galoisConnection_pow_root hq)
  exact gcPQ.u_unique gcComp (fun a => by simp [pow_mul])

/-- The two possible orders of iterated positive integer roots agree. -/
theorem root_mul_comm {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0) (n : ℕ) :
    root p (root q n) = root q (root p n) := by
  calc
    root p (root q n) = root (p * q) n := (root_mul hp hq n).symm
    _ = root (q * p) n := by rw [Nat.mul_comm]
    _ = root q (root p n) := root_mul hq hp n

end EnterpriseMath.IntegerRoot
