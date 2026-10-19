import EnterpriseMath.Relation.DeepChamberHistoryMean
import EnterpriseMath.Relation.WeightedCoefficientCoercivity
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberVectorANOVA

open EnterpriseMath.DeepChamberHistoryMean
open EnterpriseMath.S3ProvenanceMixer
open EnterpriseMath.WeightedCoefficientCoercivity
open scoped BigOperators

noncomputable section

/-- Mean channel of three history-coordinate readouts. -/
def meanChannel {ι : Type*}
    (x₀ x₁ x₂ : ι → ℝ) (i : ι) : ℝ :=
  mean3 (x₀ i) (x₁ i) (x₂ i)

/-- Centered coordinate after removing the history mean. -/
def centeredChannel {ι : Type*}
    (x₀ x₁ x₂ : ι → ℝ) (slot : Fin 3) (i : ι) : ℝ :=
  if slot = 0 then x₀ i - meanChannel x₀ x₁ x₂ i
  else if slot = 1 then x₁ i - meanChannel x₀ x₁ x₂ i
  else x₂ i - meanChannel x₀ x₁ x₂ i

/-- Pair energy of the complete three-coordinate history vector. -/
def vectorPairEnergy {ι : Type*}
    (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) : ℝ :=
  ∑ i ∈ H, ∑ j ∈ H, w i * w j *
    ((x₀ i - x₀ j) ^ 2 + (x₁ i - x₁ j) ^ 2 +
      (x₂ i - x₂ j) ^ 2)

/-- Pair-energy contribution carried by motion of the common history mean. -/
def historyMeanPairContribution {ι : Type*}
    (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) : ℝ :=
  ∑ i ∈ H, ∑ j ∈ H, w i * w j *
    (3 * (meanChannel x₀ x₁ x₂ i - meanChannel x₀ x₁ x₂ j) ^ 2)

/-- Pair energy of the centered two-dimensional `S_3` standard vectors. -/
def centeredVectorPairEnergy {ι : Type*}
    (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) : ℝ :=
  ∑ i ∈ H, ∑ j ∈ H, w i * w j *
    ((centeredChannel x₀ x₁ x₂ 0 i -
        centeredChannel x₀ x₁ x₂ 0 j) ^ 2 +
      (centeredChannel x₀ x₁ x₂ 1 i -
        centeredChannel x₀ x₁ x₂ 1 j) ^ 2 +
      (centeredChannel x₀ x₁ x₂ 2 i -
        centeredChannel x₀ x₁ x₂ 2 j) ^ 2)

/-- Pointwise orthogonal decomposition of one cross-history vector difference. -/
theorem pointwise_vectorDifference_decomposition
    {ι : Type*} (x₀ x₁ x₂ : ι → ℝ) (i j : ι) :
    (x₀ i - x₀ j) ^ 2 + (x₁ i - x₁ j) ^ 2 +
        (x₂ i - x₂ j) ^ 2 =
      3 * (meanChannel x₀ x₁ x₂ i - meanChannel x₀ x₁ x₂ j) ^ 2 +
        (centeredChannel x₀ x₁ x₂ 0 i -
          centeredChannel x₀ x₁ x₂ 0 j) ^ 2 +
        (centeredChannel x₀ x₁ x₂ 1 i -
          centeredChannel x₀ x₁ x₂ 1 j) ^ 2 +
        (centeredChannel x₀ x₁ x₂ 2 i -
          centeredChannel x₀ x₁ x₂ 2 j) ^ 2 := by
  simp [centeredChannel, meanChannel, mean3]
  ring

/-- Exact weighted ANOVA on every finite deepest-history bundle. -/
theorem vectorPairEnergy_decomposition
    {ι : Type*} (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) :
    vectorPairEnergy H w x₀ x₁ x₂ =
      historyMeanPairContribution H w x₀ x₁ x₂ +
        centeredVectorPairEnergy H w x₀ x₁ x₂ := by
  classical
  unfold vectorPairEnergy historyMeanPairContribution centeredVectorPairEnergy
  calc
    (∑ i ∈ H, ∑ j ∈ H, w i * w j *
        ((x₀ i - x₀ j) ^ 2 + (x₁ i - x₁ j) ^ 2 +
          (x₂ i - x₂ j) ^ 2)) =
      ∑ i ∈ H, ∑ j ∈ H, w i * w j *
        (3 * (meanChannel x₀ x₁ x₂ i - meanChannel x₀ x₁ x₂ j) ^ 2 +
          (centeredChannel x₀ x₁ x₂ 0 i -
            centeredChannel x₀ x₁ x₂ 0 j) ^ 2 +
          (centeredChannel x₀ x₁ x₂ 1 i -
            centeredChannel x₀ x₁ x₂ 1 j) ^ 2 +
          (centeredChannel x₀ x₁ x₂ 2 i -
            centeredChannel x₀ x₁ x₂ 2 j) ^ 2) := by
        apply Finset.sum_congr rfl
        intro i hi
        apply Finset.sum_congr rfl
        intro j hj
        rw [pointwise_vectorDifference_decomposition]
    _ =
      (∑ i ∈ H, ∑ j ∈ H, w i * w j *
        (3 * (meanChannel x₀ x₁ x₂ i - meanChannel x₀ x₁ x₂ j) ^ 2)) +
      (∑ i ∈ H, ∑ j ∈ H, w i * w j *
        ((centeredChannel x₀ x₁ x₂ 0 i -
            centeredChannel x₀ x₁ x₂ 0 j) ^ 2 +
          (centeredChannel x₀ x₁ x₂ 1 i -
            centeredChannel x₀ x₁ x₂ 1 j) ^ 2 +
          (centeredChannel x₀ x₁ x₂ 2 i -
            centeredChannel x₀ x₁ x₂ 2 j) ^ 2)) := by
        simp_rw [mul_add, Finset.sum_add_distrib]

/-- Normalized complete history-vector variance. -/
def vectorConditionalVariance {ι : Type*}
    (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) : ℝ :=
  vectorPairEnergy H w x₀ x₁ x₂ / (2 * weightedMass H w)

/-- The normalized variance splits exactly into history-mean and standard channels. -/
theorem vectorConditionalVariance_decomposition
    {ι : Type*} (H : Finset ι) (w x₀ x₁ x₂ : ι → ℝ) :
    vectorConditionalVariance H w x₀ x₁ x₂ =
      historyMeanPairContribution H w x₀ x₁ x₂ /
          (2 * weightedMass H w) +
        centeredVectorPairEnergy H w x₀ x₁ x₂ /
          (2 * weightedMass H w) := by
  unfold vectorConditionalVariance
  rw [vectorPairEnergy_decomposition]
  ring

end

end EnterpriseMath.DeepChamberVectorANOVA
