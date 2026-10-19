import EnterpriseMath.Relation.DeepChamberVectorANOVA
import EnterpriseMath.Relation.WeightedCoefficientCoercivity
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberHighLowCoercivity

open EnterpriseMath.DeepChamberVectorANOVA
open EnterpriseMath.S3ProvenanceMixer
open EnterpriseMath.WeightedCoefficientCoercivity
open scoped BigOperators

noncomputable section

/-- Mean of one high intermediate readout and two lower-scale readouts. -/
def highLowMean (high low₁ low₂ : ℝ) : ℝ :=
  mean3 high low₁ low₂

/--
Sharp convenient high/low split: the history-mean pair contribution has a
strict coefficient `1/2` on the high branch; both remaining branches enter as
lower-scale forcing with coefficient `2`.
-/
theorem historyMean_highLow_coercive
    (high high' low₁ low₁' low₂ low₂' : ℝ) :
    3 * (highLowMean high low₁ low₂ -
        highLowMean high' low₁' low₂') ^ 2 ≤
      (1 / 2 : ℝ) * (high - high') ^ 2 +
        2 * ((low₁ - low₁') ^ 2 + (low₂ - low₂') ^ 2) := by
  let dh := high - high'
  let d₁ := low₁ - low₁'
  let d₂ := low₂ - low₂'
  have hcert :
      (1 / 2 : ℝ) * dh ^ 2 + 2 * (d₁ ^ 2 + d₂ ^ 2) -
          3 * ((dh + d₁ + d₂) / 3) ^ 2 =
        ((dh - 2 * (d₁ + d₂)) ^ 2 + 6 * (d₁ - d₂) ^ 2) / 6 := by
    ring
  have hnonneg :
      0 ≤ ((dh - 2 * (d₁ + d₂)) ^ 2 + 6 * (d₁ - d₂) ^ 2) / 6 := by
    positivity
  unfold highLowMean mean3
  change 3 * ((dh + d₁ + d₂) / 3) ^ 2 ≤
    (1 / 2 : ℝ) * dh ^ 2 + 2 * (d₁ ^ 2 + d₂ ^ 2)
  linarith

/-- The coefficient `1/2` is attained only through an explicit square defect. -/
theorem historyMean_highLow_defect_identity
    (high high' low₁ low₁' low₂ low₂' : ℝ) :
    (1 / 2 : ℝ) * (high - high') ^ 2 +
        2 * ((low₁ - low₁') ^ 2 + (low₂ - low₂') ^ 2) -
      3 * (highLowMean high low₁ low₂ -
        highLowMean high' low₁' low₂') ^ 2 =
      (((high - high') -
          2 * ((low₁ - low₁') + (low₂ - low₂'))) ^ 2 +
        6 * ((low₁ - low₁') - (low₂ - low₂')) ^ 2) / 6 := by
  unfold highLowMean mean3
  ring

/-- Weighted high/low majorant on a finite history fiber. -/
def highLowPairMajorant {ι : Type*}
    (H : Finset ι) (w high low₁ low₂ : ι → ℝ) : ℝ :=
  ∑ i ∈ H, ∑ j ∈ H, w i * w j *
    ((1 / 2 : ℝ) * (high i - high j) ^ 2 +
      2 * ((low₁ i - low₁ j) ^ 2 + (low₂ i - low₂ j) ^ 2))

/--
The complete weighted history-mean contribution is strictly high-scale
coercive, with all uncompensated terms carried by the two lower branches.
-/
theorem historyMeanPairContribution_le_highLowPairMajorant
    {ι : Type*} (H : Finset ι) (w high low₁ low₂ : ι → ℝ)
    (hw : ∀ i ∈ H, 0 ≤ w i) :
    historyMeanPairContribution H w high low₁ low₂ ≤
      highLowPairMajorant H w high low₁ low₂ := by
  classical
  unfold historyMeanPairContribution highLowPairMajorant meanChannel
  apply Finset.sum_le_sum
  intro i hi
  apply Finset.sum_le_sum
  intro j hj
  have hpoint := historyMean_highLow_coercive
    (high i) (high j) (low₁ i) (low₁ j) (low₂ i) (low₂ j)
  exact mul_le_mul_of_nonneg_left hpoint
    (mul_nonneg (hw i hi) (hw j hj))

/-- The majorant is the stated weighted combination of three pair energies. -/
theorem highLowPairMajorant_eq_pairEnergies
    {ι : Type*} (H : Finset ι) (w high low₁ low₂ : ι → ℝ) :
    highLowPairMajorant H w high low₁ low₂ =
      (1 / 2 : ℝ) * weightedPairEnergy H w high +
        2 * (weightedPairEnergy H w low₁ +
          weightedPairEnergy H w low₂) := by
  classical
  unfold highLowPairMajorant weightedPairEnergy
  calc
    (∑ i ∈ H, ∑ j ∈ H, w i * w j *
      ((1 / 2 : ℝ) * (high i - high j) ^ 2 +
        2 * ((low₁ i - low₁ j) ^ 2 + (low₂ i - low₂ j) ^ 2))) =
      (∑ i ∈ H, ∑ j ∈ H,
        (1 / 2 : ℝ) * (w i * w j * (high i - high j) ^ 2)) +
      (∑ i ∈ H, ∑ j ∈ H,
        2 * (w i * w j * (low₁ i - low₁ j) ^ 2)) +
      (∑ i ∈ H, ∑ j ∈ H,
        2 * (w i * w j * (low₂ i - low₂ j) ^ 2)) := by
          simp_rw [Finset.sum_add_distrib]
          apply congrArg₂ (· + ·)
          · apply Finset.sum_congr rfl
            intro i hi
            apply Finset.sum_congr rfl
            intro j hj
            ring
          · apply congrArg₂ (· + ·)
            · apply Finset.sum_congr rfl
              intro i hi
              apply Finset.sum_congr rfl
              intro j hj
              ring
            · apply Finset.sum_congr rfl
              intro i hi
              apply Finset.sum_congr rfl
              intro j hj
              ring
    _ = (1 / 2 : ℝ) *
          (∑ i ∈ H, ∑ j ∈ H,
            w i * w j * (high i - high j) ^ 2) +
        2 * (∑ i ∈ H, ∑ j ∈ H,
          w i * w j * (low₁ i - low₁ j) ^ 2) +
        2 * (∑ i ∈ H, ∑ j ∈ H,
          w i * w j * (low₂ i - low₂ j) ^ 2) := by
            rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum]
            apply congrArg₂ (· + ·)
            · apply Finset.sum_congr rfl
              intro i hi
              rw [Finset.mul_sum]
            · apply congrArg₂ (· + ·)
              · apply Finset.sum_congr rfl
                intro i hi
                rw [Finset.mul_sum]
              · apply Finset.sum_congr rfl
                intro i hi
                rw [Finset.mul_sum]

/-- Combined finite strict cascade inequality for the history-mean block. -/
theorem historyMeanPairContribution_le_pairEnergies
    {ι : Type*} (H : Finset ι) (w high low₁ low₂ : ι → ℝ)
    (hw : ∀ i ∈ H, 0 ≤ w i) :
    historyMeanPairContribution H w high low₁ low₂ ≤
      (1 / 2 : ℝ) * weightedPairEnergy H w high +
        2 * (weightedPairEnergy H w low₁ +
          weightedPairEnergy H w low₂) := by
  rw [← highLowPairMajorant_eq_pairEnergies]
  exact historyMeanPairContribution_le_highLowPairMajorant H w high low₁ low₂ hw

end

end EnterpriseMath.DeepChamberHighLowCoercivity
