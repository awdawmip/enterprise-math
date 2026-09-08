import EnterpriseMath.Relation.BRCFiniteStateLift
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- A finite named family of source/target framed BRC branches.

`BranchId` is deliberately separate from the compressed `FramedArrow`: two
named branch occurrences are allowed to carry identical arrow summaries.  Thus
provenance exists before the matrix observer is applied, while natural
multiplicity is stored explicitly and independently. -/
structure FiniteTransitionSystem
    (BranchId S W G C : Type*)
    [Monoid W] [Monoid G] [AddMonoid C]
    (ρ : CoordinateAction G C) where
  arrow : BranchId → FramedArrow S W G C ρ
  multiplicity : BranchId → ℕ

namespace FiniteTransitionSystem

variable {BranchId S W G C R : Type*}
variable [Monoid W] [Monoid G] [AddMonoid C]
variable {ρ : CoordinateAction G C}

/-- Ordinary finite transition matrix obtained by summing all named branch
occurrences after the exact source/target × frame lift.

This is an explicit observer quotient: distinct branch IDs may recoalesce into
the same matrix entry, but no reverse provenance recovery is assumed. -/
noncomputable def transitionMatrix
    [Semiring R]
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ) :
    Matrix (S × G) (S × G) R :=
  ∑ b : BranchId, T.multiplicity b • (T.arrow b).stateFrameLift E

/-- Entrywise form of the finite transition matrix. -/
@[simp] theorem transitionMatrix_apply
    [Semiring R]
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ)
    (x y : S × G) :
    T.transitionMatrix E x y =
      ∑ b : BranchId,
        T.multiplicity b • ((T.arrow b).stateFrameLift E x y) := by
  classical
  unfold transitionMatrix
  rw [Matrix.sum_apply]
  apply Finset.sum_congr rfl
  intro b _hb
  rfl

/-- If every declared branch multiplicity is zero, the transition observer is
the zero matrix. -/
@[simp] theorem transitionMatrix_eq_zero_of_multiplicity_zero
    [Semiring R]
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ)
    (h : ∀ b, T.multiplicity b = 0) :
    T.transitionMatrix E = 0 := by
  simp [transitionMatrix, h]

/-- Determinant certificate of a finite BRC transition observer.

The determinant lives only after the exact finite state/frame lift has entered a
commutative coefficient ring.  Its alternating signs are algebraic determinant
signs, not signed branch populations. -/
noncomputable def transitionDeterminant
    [CommRing R]
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ) : R :=
  Matrix.det (1 - T.transitionMatrix E)

/-- A system with no positive branch multiplicity has determinant certificate
one. -/
@[simp] theorem transitionDeterminant_eq_one_of_multiplicity_zero
    [CommRing R]
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ)
    (h : ∀ b, T.multiplicity b = 0) :
    T.transitionDeterminant E = 1 := by
  simp [transitionDeterminant, T.transitionMatrix_eq_zero_of_multiplicity_zero E h]

end FiniteTransitionSystem

end EnterpriseMath.BranchRecoalescence
