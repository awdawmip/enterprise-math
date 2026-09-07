import EnterpriseMath.Relation.BRCFiniteTransition
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

namespace FiniteTransitionSystem

variable {BranchId S W G C R : Type*}
variable [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
variable {ρ : CoordinateAction G C}

/-- Matrix contribution of an ordered pair of named branches.

Composable endpoints produce the exact typed BRC composite with multiplied
natural multiplicity; a noncomposable pair contributes the zero matrix. -/
noncomputable def twoStepContribution
    [Fintype S] [Fintype G] [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ)
    (a b : BranchId) : Matrix (S × G) (S × G) R :=
  if h : (T.arrow a).target = (T.arrow b).source then
    (T.multiplicity a * T.multiplicity b) •
      ((T.arrow a).compose (T.arrow b) h).stateFrameLift E
  else
    0

/-- The square of the finite transition matrix is exactly the sum of all ordered
two-branch BRC paths.  Endpoint-incompatible pairs disappear algebraically;
compatible pairs recoalesce after exact serial composition. -/
theorem transitionMatrix_sq_eq_twoStep_sum
    [Fintype BranchId] [Fintype S] [Fintype G]
    [DecidableEq S] [DecidableEq G]
    (E : FrameEmission W G C R ρ)
    (T : FiniteTransitionSystem BranchId S W G C ρ) :
    T.transitionMatrix E * T.transitionMatrix E =
      ∑ a : BranchId, ∑ b : BranchId, T.twoStepContribution E a b := by
  classical
  unfold transitionMatrix
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro a _ha
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro b _hb
  by_cases h : (T.arrow a).target = (T.arrow b).source
  · simp [twoStepContribution, h]
  · simp [twoStepContribution, h]

end FiniteTransitionSystem

end EnterpriseMath.BranchRecoalescence
