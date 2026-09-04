import EnterpriseMath.Relation.WeightedCoefficientCoercivity
import Mathlib.Tactic

namespace EnterpriseMath.WeightedRelationMixer

open EnterpriseMath.WeightedQuotientRelationField
open EnterpriseMath.WeightedCoefficientCoercivity

/-- Convexly mix a scalar value channel toward one common mean. -/
def mixValue {ι : Type*}
    (lambda mean : ℝ) (value : ι → ℝ) (i : ι) : ℝ :=
  lambda * value i + (1 - lambda) * mean

/-- Mix capacity-weighted block totals toward a common mean. -/
def mixTotal {ι : Type*}
    (lambda mean : ℝ) (mass total : ι → ℝ) (i : ι) : ℝ :=
  lambda * total i + (1 - lambda) * mass i * mean

/-- Mixing toward a common mean scales every internal relation coordinate. -/
theorem relationField_mixTotal
    {ι : Type*} (lambda mean : ℝ) (mass total : ι → ℝ) (i j : ι) :
    relationField mass (mixTotal lambda mean mass total) i j =
      lambda * relationField mass total i j := by
  unfold relationField mixTotal
  ring

/-- Complete pair energy scales quadratically under common-mean mixing. -/
theorem weightedPairEnergy_mixValue
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ)
    (lambda mean : ℝ) :
    weightedPairEnergy S u (mixValue lambda mean value) =
      lambda ^ 2 * weightedPairEnergy S u value := by
  classical
  unfold weightedPairEnergy mixValue
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  ring

/-- Weighted first moment after common-mean mixing. -/
theorem weightedSum_mixValue
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ)
    (lambda mean : ℝ) :
    weightedSum S u (mixValue lambda mean value) =
      lambda * weightedSum S u value +
        (1 - lambda) * weightedMass S u * mean := by
  classical
  unfold weightedSum weightedMass mixValue
  calc
    (∑ i in S, u i * (lambda * value i + (1 - lambda) * mean)) =
        lambda * (∑ i in S, u i * value i) +
          (1 - lambda) * (∑ i in S, u i) * mean := by
            simp_rw [Finset.sum_add_distrib]
            rw [Finset.mul_sum, Finset.mul_sum, Finset.sum_mul]
            ring
    _ = _ := by rfl

/-- Mixing toward the actual weighted mean preserves the weighted grand total. -/
theorem weightedSum_mixValue_mean
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ)
    (lambda : ℝ) (hU : weightedMass S u ≠ 0) :
    weightedSum S u
        (mixValue lambda
          (weightedSum S u value / weightedMass S u) value) =
      weightedSum S u value := by
  rw [weightedSum_mixValue]
  field_simp [hU]
  ring

/-- The degree-three lift--transposition--project value mixer. -/
def s3ValueMixer {ι : Type*}
    (mean : ℝ) (value : ι → ℝ) (i : ι) : ℝ :=
  (value i + 2 * mean) / 3

/-- The `S_3` value mixer is common-mean mixing with coefficient `1/3`. -/
theorem s3ValueMixer_eq_mixValue
    {ι : Type*} (mean : ℝ) (value : ι → ℝ) :
    s3ValueMixer mean value = mixValue (1 / 3 : ℝ) mean value := by
  funext i
  unfold s3ValueMixer mixValue
  ring

/-- The weighted `S_3` mixer scales every internal relation field by `1/3`. -/
theorem relationField_s3Mix
    {ι : Type*} (mean : ℝ) (mass total : ι → ℝ) (i j : ι) :
    relationField mass (mixTotal (1 / 3 : ℝ) mean mass total) i j =
      (1 / 3 : ℝ) * relationField mass total i j := by
  exact relationField_mixTotal (1 / 3 : ℝ) mean mass total i j

/-- The weighted `S_3` mixer contracts complete pair energy by exactly `1/9`. -/
theorem weightedPairEnergy_s3Mix
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ) (mean : ℝ) :
    weightedPairEnergy S u (s3ValueMixer mean value) =
      (1 / 9 : ℝ) * weightedPairEnergy S u value := by
  rw [s3ValueMixer_eq_mixValue,
    weightedPairEnergy_mixValue S u value (1 / 3 : ℝ) mean]
  ring

/-- The `S_3` mixer preserves the weighted mean when its target is that mean. -/
theorem weightedSum_s3Mix_mean
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ)
    (hU : weightedMass S u ≠ 0) :
    weightedSum S u
        (s3ValueMixer
          (weightedSum S u value / weightedMass S u) value) =
      weightedSum S u value := by
  rw [s3ValueMixer_eq_mixValue]
  exact weightedSum_mixValue_mean S u value (1 / 3 : ℝ) hU

/-- On a centered channel, one `S_3` mixer step multiplies values by `1/3`. -/
theorem s3ValueMixer_centered
    {ι : Type*} (value : ι → ℝ) :
    s3ValueMixer 0 value = fun i => value i / 3 := by
  funext i
  unfold s3ValueMixer
  ring

end EnterpriseMath.WeightedRelationMixer
