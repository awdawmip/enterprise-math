import EnterpriseMath.Relation.DeepChamberFullIntermediateVariance
import EnterpriseMath.Relation.S3ProvenanceMixer
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberHistoryMean

open EnterpriseMath.DeepChamberFullIntermediateVariance
open EnterpriseMath.S3ProvenanceMixer

noncomputable section

/-- Squared Euclidean distance between two three-branch readout vectors. -/
def intermediateVectorDistance
    (x₁ x₂ x₃ y₁ y₂ y₃ : ℝ) : ℝ :=
  (x₁ - y₁) ^ 2 + (x₂ - y₂) ^ 2 + (x₃ - y₃) ^ 2

/--
Exact trivial/standard decomposition of a difference of two three-history
readout vectors.
-/
theorem intermediateVectorDistance_decomposition
    (x₁ x₂ x₃ y₁ y₂ y₃ : ℝ) :
    intermediateVectorDistance x₁ x₂ x₃ y₁ y₂ y₃ =
      3 * (mean3 x₁ x₂ x₃ - mean3 y₁ y₂ y₃) ^ 2 +
        pairEnergy3 (x₁ - y₁) (x₂ - y₂) (x₃ - y₃) / 3 := by
  unfold intermediateVectorDistance mean3 pairEnergy3
  ring

/-- Mean of the three retained intermediate field readouts. -/
def historyMean
    (f : ℕ → ℝ) (s : FullIntermediateState) : ℝ :=
  mean3
    (f s.firstIntermediate)
    (f s.secondIntermediate)
    (f s.thirdIntermediate)

/-- The forgetful colored endpoint of a complete history state. -/
def coloredEndpointKey (s : FullIntermediateState) : Fin 3 × ℕ :=
  (s.color, s.endpoint)

/-- Arithmetic deepest history `(2,13,13)` at scale `10^3`. -/
def meanWitnessA : FullIntermediateState :=
  ⟨0, 500, 76, 76, 2⟩

/-- Arithmetic deepest history `(3,11,11)` at scale `10^3`. -/
def meanWitnessB : FullIntermediateState :=
  ⟨0, 333, 90, 90, 2⟩

/-- The two histories have the same color and final endpoint. -/
theorem meanWitness_coloredEndpoint_eq :
    coloredEndpointKey meanWitnessA = coloredEndpointKey meanWitnessB := by
  rfl

/-- Exact arithmetic certificate for the two deepest histories. -/
theorem meanWitness_arithmetic_certificate :
    2 ≤ 10 ∧ 10 < 13 ∧
      2 * 13 * 13 ≤ 10 ^ 3 ∧
      10 ^ 3 / (2 * 13 * 13) = 2 ∧
      10 ^ 3 / 2 = 500 ∧
      10 ^ 3 / 13 = 76 ∧
      3 ≤ 10 ∧ 10 < 11 ∧
      3 * 11 * 11 ≤ 10 ^ 3 ∧
      10 ^ 3 / (3 * 11 * 11) = 2 ∧
      10 ^ 3 / 3 = 333 ∧
      10 ^ 3 / 11 = 90 := by
  norm_num

/-- A field that is constant on each witness triple but separates the two triples. -/
def meanWitnessField (n : ℕ) : ℝ :=
  if n = 500 then 1 else if n = 76 then 1 else 0

/-- Each witness separately has zero internal `S_3` standard energy. -/
theorem meanWitness_internalStandardEnergy_zero :
    intermediateStandardEnergy meanWitnessField meanWitnessA = 0 ∧
      intermediateStandardEnergy meanWitnessField meanWitnessB = 0 := by
  norm_num [intermediateStandardEnergy, meanWitnessField,
    meanWitnessA, meanWitnessB]

/-- Their retained history means are nevertheless distinct. -/
theorem meanWitness_historyMean_ne :
    historyMean meanWitnessField meanWitnessA ≠
      historyMean meanWitnessField meanWitnessB := by
  norm_num [historyMean, mean3, meanWitnessField, meanWitnessA, meanWitnessB]

/--
No uniform constant can control the cross-history mean channel using only the
sum of the two internal standard energies.
-/
theorem no_uniform_internalStandardEnergy_controls_historyMean :
    ¬ ∃ C : ℝ, ∀ f : ℕ → ℝ,
      (historyMean f meanWitnessA - historyMean f meanWitnessB) ^ 2 ≤
        C * (intermediateStandardEnergy f meanWitnessA +
          intermediateStandardEnergy f meanWitnessB) := by
  rintro ⟨C, hC⟩
  have h := hC meanWitnessField
  norm_num [historyMean, mean3, intermediateStandardEnergy,
    meanWitnessField, meanWitnessA, meanWitnessB] at h

/--
The complete vector distance has two irreducible channels: history-mean
motion on the trivial line and standard curvature motion transverse to it.
-/
theorem complete_two_channel_identity
    (f : ℕ → ℝ) (s t : FullIntermediateState) :
    intermediateVectorDistance
        (f s.firstIntermediate) (f s.secondIntermediate)
        (f s.thirdIntermediate) (f t.firstIntermediate)
        (f t.secondIntermediate) (f t.thirdIntermediate) =
      3 * (historyMean f s - historyMean f t) ^ 2 +
        pairEnergy3
          (f s.firstIntermediate - f t.firstIntermediate)
          (f s.secondIntermediate - f t.secondIntermediate)
          (f s.thirdIntermediate - f t.thirdIntermediate) / 3 := by
  exact intermediateVectorDistance_decomposition
    (f s.firstIntermediate) (f s.secondIntermediate) (f s.thirdIntermediate)
    (f t.firstIntermediate) (f t.secondIntermediate) (f t.thirdIntermediate)

end

end EnterpriseMath.DeepChamberHistoryMean
