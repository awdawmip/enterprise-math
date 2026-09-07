import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

open Matrix

variable {I B R : Type*}
variable [Fintype I] [Fintype B] [DecidableEq I] [DecidableEq B]
variable [CommRing R]

/-- Exact effective boundary transition after eliminating an invertible hidden
resolvent block `1 - A`.  This is the formal algebraic port law

`W = D + Y * (1 - A)⁻¹ * X`.

No numerical stability interpretation is built into this definition. -/
noncomputable def schurPortEffective
    (A : Matrix I I R) (X : Matrix I B R)
    (Y : Matrix B I R) (D : Matrix B B R)
    [Invertible (1 - A)] : Matrix B B R :=
  D + Y * ⅟(1 - A) * X

/-- Subtracting a block transition matrix from the identity acts blockwise with
negative off-diagonal blocks. -/
omit [Fintype I] [Fintype B] in
theorem one_sub_fromBlocks
    (A : Matrix I I R) (X : Matrix I B R)
    (Y : Matrix B I R) (D : Matrix B B R) :
    (1 : Matrix (I ⊕ B) (I ⊕ B) R) - Matrix.fromBlocks A X Y D =
      Matrix.fromBlocks (1 - A) (-X) (-Y) (1 - D) := by
  rw [← Matrix.fromBlocks_one]
  rw [sub_eq_add_neg, Matrix.fromBlocks_neg, Matrix.fromBlocks_add]
  simp [sub_eq_add_neg]

/-- Exact hidden/boundary determinant factorization for BRC port elimination.

If the hidden resolvent block `1 - A` is invertible, then for
`T = [[A,X],[Y,D]]` and `W = D + Y(1-A)⁻¹X`, one has

`det(1 - T) = det(1 - A) * det(1 - W)`.

The signed determinant is an algebraic certificate of the commutative matrix
semantics; it is not interpreted as signed branch mass. -/
theorem det_one_sub_fromBlocks_eq_hidden_mul_effective
    (A : Matrix I I R) (X : Matrix I B R)
    (Y : Matrix B I R) (D : Matrix B B R)
    [Invertible (1 - A)] :
    Matrix.det ((1 : Matrix (I ⊕ B) (I ⊕ B) R) - Matrix.fromBlocks A X Y D) =
      Matrix.det (1 - A) * Matrix.det (1 - schurPortEffective A X Y D) := by
  rw [one_sub_fromBlocks]
  rw [Matrix.det_fromBlocks₁₁]
  apply congrArg₂ (· * ·) rfl
  apply congrArg Matrix.det
  simp only [schurPortEffective, Matrix.neg_mul, Matrix.mul_neg]
  noncomm_ring

end EnterpriseMath.BranchRecoalescence
