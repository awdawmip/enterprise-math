import EnterpriseMath.Relation.BranchRecoalescence
import EnterpriseMath.Relation.DeepChamberIntermediateNoGo
import EnterpriseMath.Relation.OrderedQuotientCurvature
import EnterpriseMath.Relation.WeightedCoefficientCoercivity
import EnterpriseMath.Relation.WeightedTripleBranchMixer
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberFullIntermediateVariance

open EnterpriseMath.BranchRecoalescence
open EnterpriseMath.PrimePowerQuotientTriangle
open EnterpriseMath.OrderedQuotientCurvature
open EnterpriseMath.WeightedCoefficientCoercivity
open EnterpriseMath.WeightedTripleBranchMixer
open scoped BigOperators

noncomputable section

/--
The complete descended state of one deepest three-history packet.  The color
records the unique uncut position; all three one-step intermediate vertices
and the common product endpoint are retained.
-/
structure FullIntermediateState where
  color : Fin 3
  firstIntermediate : ℕ
  secondIntermediate : ℕ
  thirdIntermediate : ℕ
  endpoint : ℕ
  deriving DecidableEq

/-- Complete provenance key of a deepest descended state. -/
def fullIntermediateKey (s : FullIntermediateState) :
    Fin 3 × ℕ × ℕ × ℕ × ℕ :=
  (s.color, s.firstIntermediate, s.secondIntermediate,
    s.thirdIntermediate, s.endpoint)

/-- Every observable explicitly defined on the complete key is recoverable. -/
def keyReadout {R : Type*}
    (F : Fin 3 × ℕ × ℕ × ℕ × ℕ → R)
    (s : FullIntermediateState) : R :=
  F (fullIntermediateKey s)

/-- The full key is sufficient for every readout that factors through it. -/
theorem fullIntermediateKey_recovers_keyReadout
    {R : Type*} (F : Fin 3 × ℕ × ℕ × ℕ × ℕ → R) :
    Recovers fullIntermediateKey (keyReadout F) := by
  exact ⟨F, fun _ => rfl⟩

/-- Realization of the complete state by three quotient actions. -/
def quotientFullIntermediateState
    (color : Fin 3) (n : ℕ) (t : Triple ℕ) : FullIntermediateState where
  color := color
  firstIntermediate := quotient t.first n
  secondIntermediate := quotient t.second n
  thirdIntermediate := quotient t.third n
  endpoint := quotient (t.first * t.second * t.third) n

/-- The stored endpoint is the common endpoint of the ordered three-step history. -/
theorem quotientFullIntermediateState_endpoint_eq
    (color : Fin 3) (n : ℕ) (t : Triple ℕ) :
    (quotientFullIntermediateState color n t).endpoint =
      quotient t.third (quotient t.second (quotient t.first n)) := by
  simp [quotientFullIntermediateState, quotient, Nat.div_div_eq_div_mul,
    Nat.mul_assoc]

/-- Standard pair energy of the three one-step intermediate readouts. -/
def intermediateStandardEnergy
    (f : ℕ → ℝ) (s : FullIntermediateState) : ℝ :=
  (f s.firstIntermediate - f s.secondIntermediate) ^ 2 +
    (f s.secondIntermediate - f s.thirdIntermediate) ^ 2 +
    (f s.thirdIntermediate - f s.firstIntermediate) ^ 2

/--
For an arithmetic three-history state, the complete intermediate standard
energy is exactly the sum of the three cyclic ordered-curvature channels.
-/
theorem quotientFullIntermediateState_standardEnergy_eq_curvature
    (color : Fin 3) (n a b c : ℕ) (f : ℕ → ℝ) :
    intermediateStandardEnergy f
        (quotientFullIntermediateState color n ⟨a, b, c⟩) =
      (commonSuffixCurvature a b c f n) ^ 2 +
        (commonSuffixCurvature b c a f n) ^ 2 +
        (commonSuffixCurvature c a b f n) ^ 2 := by
  unfold intermediateStandardEnergy quotientFullIntermediateState
  rw [commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub]

/-- Read a selected one-step branch from an ordered three-history label. -/
def selectedHistoryValue
    (select : Triple ℕ → ℕ) (f : ℕ → ℝ) (n : ℕ)
    (t : Triple ℕ) : ℝ :=
  f (quotient (select t) n)

/-- Pairwise fluctuation of one selected intermediate branch across histories. -/
def selectedHistoryPairEnergy
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (select : Triple ℕ → ℕ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  weightedPairEnergy H w (selectedHistoryValue select f n)

/-- The same history fluctuation expressed as an ordered common-suffix curvature. -/
def selectedHistoryCurvatureEnergy
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (select : Triple ℕ → ℕ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ t ∈ H, ∑ s ∈ H,
    w t * w s *
      (commonSuffixCurvature (select t) (select s) 1 f n) ^ 2

/-- Every within-history-bundle branch variance is already an ordered curvature energy. -/
theorem selectedHistoryPairEnergy_eq_curvature
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (select : Triple ℕ → ℕ) (f : ℕ → ℝ) (n : ℕ) :
    selectedHistoryPairEnergy H w select f n =
      selectedHistoryCurvatureEnergy H w select f n := by
  classical
  unfold selectedHistoryPairEnergy selectedHistoryCurvatureEnergy
  unfold weightedPairEnergy selectedHistoryValue
  apply Finset.sum_congr rfl
  intro t ht
  apply Finset.sum_congr rfl
  intro s hs
  rw [commonSuffixCurvature_eq_intermediate_sub]

/-- Sum of the conditional pair energies of all three retained branches. -/
def fullIntermediateHistoryEnergy
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  selectedHistoryPairEnergy H w Triple.first f n +
    selectedHistoryPairEnergy H w Triple.second f n +
    selectedHistoryPairEnergy H w Triple.third f n

/-- Ordered-curvature realization of the complete three-branch fluctuation. -/
def fullIntermediateCurvatureEnergy
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  selectedHistoryCurvatureEnergy H w Triple.first f n +
    selectedHistoryCurvatureEnergy H w Triple.second f n +
    selectedHistoryCurvatureEnergy H w Triple.third f n

/-- The complete conditional fluctuation is exactly the complete curvature packet. -/
theorem fullIntermediateHistoryEnergy_eq_curvature
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ) :
    fullIntermediateHistoryEnergy H w f n =
      fullIntermediateCurvatureEnergy H w f n := by
  unfold fullIntermediateHistoryEnergy fullIntermediateCurvatureEnergy
  rw [selectedHistoryPairEnergy_eq_curvature,
    selectedHistoryPairEnergy_eq_curvature,
    selectedHistoryPairEnergy_eq_curvature]

/-- Complete normalized conditional variance of the retained intermediate bundle. -/
def fullIntermediateConditionalVariance
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  fullIntermediateHistoryEnergy H w f n /
    (2 * weightedMass H w)

/-- The normalized conditional variance has an exact ordered-curvature formula. -/
theorem fullIntermediateConditionalVariance_eq_curvature
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ) :
    fullIntermediateConditionalVariance H w f n =
      fullIntermediateCurvatureEnergy H w f n /
        (2 * weightedMass H w) := by
  unfold fullIntermediateConditionalVariance
  rw [fullIntermediateHistoryEnergy_eq_curvature]

/-- Nonnegative history weights make the complete intermediate energy nonnegative. -/
theorem fullIntermediateHistoryEnergy_nonneg
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ)
    (hw : ∀ t ∈ H, 0 ≤ w t) :
    0 ≤ fullIntermediateHistoryEnergy H w f n := by
  unfold fullIntermediateHistoryEnergy selectedHistoryPairEnergy
  have h₁ := weightedPairEnergy_nonneg H w
    (selectedHistoryValue Triple.first f n) hw
  have h₂ := weightedPairEnergy_nonneg H w
    (selectedHistoryValue Triple.second f n) hw
  have h₃ := weightedPairEnergy_nonneg H w
    (selectedHistoryValue Triple.third f n) hw
  linarith

/-- Positive total mass makes the normalized complete conditional variance nonnegative. -/
theorem fullIntermediateConditionalVariance_nonneg
    (H : Finset (Triple ℕ)) (w : Triple ℕ → ℝ)
    (f : ℕ → ℝ) (n : ℕ)
    (hw : ∀ t ∈ H, 0 ≤ w t)
    (hW : 0 < weightedMass H w) :
    0 ≤ fullIntermediateConditionalVariance H w f n := by
  unfold fullIntermediateConditionalVariance
  exact div_nonneg
    (fullIntermediateHistoryEnergy_nonneg H w f n hw)
    (mul_nonneg (by norm_num) hW.le)

end

end EnterpriseMath.DeepChamberFullIntermediateVariance
