import EnterpriseMath.Relation.BRCFiniteFrameLift
import Mathlib.Data.Matrix.Composition
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- A source/target-typed framed BRC arrow.  The path summary retains exact
weight/coordinate/frame/length data, while `source` and `target` retain the
category-algebra endpoint discipline required for contextual composition. -/
structure FramedArrow (S W G C : Type*)
    [Monoid W] [Monoid G] [AddMonoid C]
    (ρ : CoordinateAction G C) where
  source : S
  target : S
  path : FramedPath W G C ρ

namespace FramedArrow

variable {S W G C R : Type*}
variable [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
variable {ρ : CoordinateAction G C}

/-- Compose two typed arrows when the first target equals the second source. -/
def then (a b : FramedArrow S W G C ρ) (h : a.target = b.source) :
    FramedArrow S W G C ρ where
  source := a.source
  target := b.target
  path := a.path * b.path

@[simp] theorem then_source (a b : FramedArrow S W G C ρ)
    (h : a.target = b.source) :
    (a.then b h).source = a.source := rfl

@[simp] theorem then_target (a b : FramedArrow S W G C ρ)
    (h : a.target = b.source) :
    (a.then b h).target = b.target := rfl

@[simp] theorem then_path (a b : FramedArrow S W G C ρ)
    (h : a.target = b.source) :
    (a.then b h).path = a.path * b.path := rfl

/-- Nested state/frame matrix: the only nonzero state-level entry is
`source → target`, and that entry is the exact finite frame-lift matrix. -/
noncomputable def nestedLift [Fintype G] [DecidableEq G] [DecidableEq S]
    (E : FrameEmission W G C R ρ) (a : FramedArrow S W G C ρ) :
    Matrix S S (Matrix G G R) :=
  Matrix.single a.source a.target (E.frameLift a.path)

/-- Flatten the nested state/frame representation to an ordinary matrix indexed
by `(state, frame)`.  This is exactly the finite state enlargement used before
ordinary determinant/Schur algebra is applied. -/
noncomputable def stateFrameLift
    [Fintype S] [Fintype G] [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ) (a : FramedArrow S W G C ρ) :
    Matrix (S × G) (S × G) R :=
  Matrix.compRingEquiv S G R (a.nestedLift E)

/-- If endpoints compose, ordinary matrix multiplication is exactly typed BRC
serial composition. -/
@[simp] theorem stateFrameLift_mul_of_composable
    [Fintype S] [Fintype G] [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (a b : FramedArrow S W G C ρ) (h : a.target = b.source) :
    a.stateFrameLift E * b.stateFrameLift E =
      (a.then b h).stateFrameLift E := by
  unfold stateFrameLift nestedLift
  rw [← (Matrix.compRingEquiv S G R).map_mul]
  congr 1
  subst h
  simp

/-- If endpoints do not compose, their category-algebra product is literally the
zero matrix.  No external error flag or post-processing convention is needed. -/
@[simp] theorem stateFrameLift_mul_of_not_composable
    [Fintype S] [Fintype G] [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (a b : FramedArrow S W G C ρ) (h : a.target ≠ b.source) :
    a.stateFrameLift E * b.stateFrameLift E = 0 := by
  unfold stateFrameLift nestedLift
  rw [← (Matrix.compRingEquiv S G R).map_mul]
  rw [Matrix.single_mul_single_of_ne _ _ _ _ h]
  simp

end FramedArrow

end EnterpriseMath.BranchRecoalescence
