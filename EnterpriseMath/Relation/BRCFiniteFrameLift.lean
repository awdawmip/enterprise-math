import EnterpriseMath.Relation.FramedBranchRecoalescence
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- A commutative-coefficient emission rule for a framed path.  The coefficient
seen from frame `g` is allowed to depend on `g`, but serial composition must obey
the exact twisted law induced by the frame left by the first path.

This is the algebraic contract behind the executable finite-frame lift.  Frame
composition itself is *not* forced into the commutative coefficient ring; it is
retained in the matrix row/column indices. -/
structure FrameEmission (W G C R : Type*)
    [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
    (ρ : CoordinateAction G C) where
  emit : G → FramedPath W G C ρ → R
  emit_one : ∀ g, emit g 1 = 1
  emit_mul : ∀ g a b,
    emit g (a * b) = emit g a * emit (g * a.frame) b

namespace FrameEmission

variable {W G C R : Type*}
variable [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
variable {ρ : CoordinateAction G C}

/-- Finite frame-state matrix of one framed path.  From current frame `g`, the
path has exactly one possible outgoing frame, namely `g * p.frame`; its
commutative coefficient is the declared emission `emit g p`. -/
noncomputable def frameLift [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) (p : FramedPath W G C ρ) : Matrix G G R :=
  fun g h => if h = g * p.frame then E.emit g p else 0

@[simp] theorem frameLift_apply [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) (p : FramedPath W G C ρ) (g h : G) :
    E.frameLift p g h = if h = g * p.frame then E.emit g p else 0 := rfl

/-- The empty framed path lifts to the identity frame matrix. -/
@[simp] theorem frameLift_one [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) :
    E.frameLift (1 : FramedPath W G C ρ) = 1 := by
  ext g h
  simp [frameLift, Matrix.one_apply, E.emit_one, eq_comm]

/-- The finite frame lift converts the semidirect/noncommutative framed product
into ordinary matrix multiplication over the declared coefficient semiring.

The proof has exactly one live intermediate frame, `g * a.frame`; this is the
formal reason the frame must be retained as state rather than erased into a
commutative scalar. -/
@[simp] theorem frameLift_mul [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) (a b : FramedPath W G C ρ) :
    E.frameLift (a * b) = E.frameLift a * E.frameLift b := by
  ext g k
  rw [Matrix.mul_apply]
  rw [Finset.sum_eq_single (g * a.frame)]
  · simp [frameLift, E.emit_mul, mul_assoc]
  · intro h _hh hne
    simp [frameLift, hne]
  · simp

/-- The one-path finite frame lift is a genuine monoid homomorphism. -/
noncomputable def frameLiftMonoidHom [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) :
    FramedPath W G C ρ →* Matrix G G R where
  toFun := E.frameLift
  map_one' := E.frameLift_one
  map_mul' := E.frameLift_mul

/-- Lift the whole positive-multiplicity framed BRC into ordinary finite matrices.
Alternative recoalescence becomes matrix addition and serial convolution becomes
matrix multiplication.  Natural multiplicity remains an outer positive scalar;
there is no signed/amplitude cancellation claim here. -/
noncomputable def frameLiftNBRCAlgHom [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ) :
    FramedNBRC W G C ρ →ₐ[ℕ] Matrix G G R :=
  MonoidAlgebra.lift ℕ (Matrix G G R) (FramedPath W G C ρ)
    E.frameLiftMonoidHom

/-- One atomic BRC branch maps to its finite frame matrix with the same natural
multiplicity. -/
@[simp] theorem frameLiftNBRCAlgHom_single [Fintype G] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (p : FramedPath W G C ρ) (n : ℕ) :
    E.frameLiftNBRCAlgHom (MonoidAlgebra.single p n) = n • E.frameLift p := by
  simp [frameLiftNBRCAlgHom, frameLiftMonoidHom]

end FrameEmission

end EnterpriseMath.BranchRecoalescence
