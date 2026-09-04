import EnterpriseMath.Relation.WeightedQuotientRelationField
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.WeightedCoefficientCoercivity

open scoped BigOperators

/-- Total weight of a finite action family. -/
def weightedMass {ι : Type*} (S : Finset ι) (u : ι → ℝ) : ℝ :=
  ∑ i ∈ S, u i

/-- Weighted first moment of a finite value channel. -/
def weightedSum {ι : Type*}
    (S : Finset ι) (u x : ι → ℝ) : ℝ :=
  ∑ i ∈ S, u i * x i

/-- Weighted second moment of a finite value channel. -/
def weightedSecond {ι : Type*}
    (S : Finset ι) (u x : ι → ℝ) : ℝ :=
  ∑ i ∈ S, u i * (x i) ^ 2

/-- Complete weighted pair-difference energy. -/
def weightedPairEnergy {ι : Type*}
    (S : Finset ι) (u x : ι → ℝ) : ℝ :=
  ∑ i ∈ S, ∑ j ∈ S,
    u i * u j * (x i - x j) ^ 2

/-- The first square contribution in the pair-energy expansion. -/
theorem sum_sum_left_sq
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ) :
    (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x i) ^ 2) =
      weightedSecond S u x * weightedMass S u := by
  classical
  unfold weightedSecond weightedMass
  calc
    (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x i) ^ 2) =
        ∑ i ∈ S, (u i * (x i) ^ 2) * (∑ j ∈ S, u j) := by
          apply Finset.sum_congr rfl
          intro i hi
          rw [Finset.sum_mul]
          apply Finset.sum_congr rfl
          intro j hj
          ring
    _ = (∑ i ∈ S, u i * (x i) ^ 2) * (∑ j ∈ S, u j) := by
          rw [Finset.sum_mul]

/-- The second square contribution in the pair-energy expansion. -/
theorem sum_sum_right_sq
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ) :
    (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x j) ^ 2) =
      weightedMass S u * weightedSecond S u x := by
  classical
  unfold weightedSecond weightedMass
  calc
    (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x j) ^ 2) =
        ∑ i ∈ S, u i * (∑ j ∈ S, u j * (x j) ^ 2) := by
          apply Finset.sum_congr rfl
          intro i hi
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro j hj
          ring
    _ = (∑ i ∈ S, u i) * (∑ j ∈ S, u j * (x j) ^ 2) := by
          rw [Finset.mul_sum]

/-- The mixed contribution in the pair-energy expansion. -/
theorem sum_sum_cross
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ) :
    (∑ i ∈ S, ∑ j ∈ S, (u i * x i) * (u j * x j)) =
      (weightedSum S u x) ^ 2 := by
  classical
  unfold weightedSum
  calc
    (∑ i ∈ S, ∑ j ∈ S, (u i * x i) * (u j * x j)) =
        ∑ i ∈ S, (u i * x i) * (∑ j ∈ S, u j * x j) := by
          apply Finset.sum_congr rfl
          intro i hi
          rw [Finset.sum_mul]
    _ = (∑ i ∈ S, u i * x i) * (∑ j ∈ S, u j * x j) := by
          rw [Finset.sum_mul]
    _ = (∑ i ∈ S, u i * x i) ^ 2 := by ring

/-- Twice the mixed contribution factors globally. -/
theorem sum_sum_two_cross
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ) :
    (∑ i ∈ S, ∑ j ∈ S, 2 * ((u i * x i) * (u j * x j))) =
      2 * (weightedSum S u x) ^ 2 := by
  classical
  calc
    (∑ i ∈ S, ∑ j ∈ S, 2 * ((u i * x i) * (u j * x j))) =
        2 * (∑ i ∈ S, ∑ j ∈ S, (u i * x i) * (u j * x j)) := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro i hi
          rw [Finset.mul_sum]
    _ = 2 * (weightedSum S u x) ^ 2 := by
          rw [sum_sum_cross]

/-- Pair-difference energy in first/second-moment form. -/
theorem weightedPairEnergy_eq_moments
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ) :
    weightedPairEnergy S u x =
      2 * weightedMass S u * weightedSecond S u x -
        2 * (weightedSum S u x) ^ 2 := by
  classical
  unfold weightedPairEnergy
  calc
    (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x i - x j) ^ 2) =
        ∑ i ∈ S, ∑ j ∈ S,
          (u i * u j * (x i) ^ 2 +
            u i * u j * (x j) ^ 2 -
            2 * ((u i * x i) * (u j * x j))) := by
              apply Finset.sum_congr rfl
              intro i hi
              apply Finset.sum_congr rfl
              intro j hj
              ring
    _ = (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x i) ^ 2) +
          (∑ i ∈ S, ∑ j ∈ S, u i * u j * (x j) ^ 2) -
          (∑ i ∈ S, ∑ j ∈ S,
            2 * ((u i * x i) * (u j * x j))) := by
              simp_rw [Finset.sum_sub_distrib, Finset.sum_add_distrib]
    _ = weightedSecond S u x * weightedMass S u +
          weightedMass S u * weightedSecond S u x -
          2 * (weightedSum S u x) ^ 2 := by
            rw [sum_sum_left_sq, sum_sum_right_sq, sum_sum_two_cross]
    _ = 2 * weightedMass S u * weightedSecond S u x -
          2 * (weightedSum S u x) ^ 2 := by ring

/-- Weighted variance is nonnegative for nonnegative weights. -/
theorem weightedPairEnergy_nonneg
    {ι : Type*} (S : Finset ι) (u x : ι → ℝ)
    (hu : ∀ i ∈ S, 0 ≤ u i) :
    0 ≤ weightedPairEnergy S u x := by
  unfold weightedPairEnergy
  apply Finset.sum_nonneg
  intro i hi
  apply Finset.sum_nonneg
  intro j hj
  exact mul_nonneg (mul_nonneg (hu i hi) (hu j hj)) (sq_nonneg _)

/-- Tail-coefficient product channel. -/
def coefficientProduct {ι : Type*}
    (V x : ι → ℝ) (i : ι) : ℝ :=
  V i * x i

/-- Current value after adjoining the total mass and tail coefficient. -/
def coefficientLift {ι : Type*}
    (S : Finset ι) (u V x : ι → ℝ) (i : ι) : ℝ :=
  (weightedMass S u + V i) * x i

/-- Exact first moment of the coefficient lift on a centered channel. -/
theorem weightedSum_coefficientLift_of_centered
    {ι : Type*} (S : Finset ι) (u V x : ι → ℝ)
    (hcenter : weightedSum S u x = 0) :
    weightedSum S u (coefficientLift S u V x) =
      weightedSum S u (coefficientProduct V x) := by
  classical
  unfold weightedSum coefficientLift coefficientProduct weightedMass at *
  calc
    (∑ i ∈ S, u i * ((∑ j ∈ S, u j) + V i) * x i) =
        (∑ j ∈ S, u j) * (∑ i ∈ S, u i * x i) +
          ∑ i ∈ S, u i * (V i * x i) := by
            rw [Finset.mul_sum]
            simp_rw [Finset.sum_add_distrib]
            ring
    _ = ∑ i ∈ S, u i * (V i * x i) := by
          rw [hcenter]
          ring

/-- Exact second-moment expansion of the coefficient lift. -/
theorem weightedSecond_coefficientLift
    {ι : Type*} (S : Finset ι) (u V x : ι → ℝ) :
    weightedSecond S u (coefficientLift S u V x) =
      (weightedMass S u) ^ 2 * weightedSecond S u x +
        2 * weightedMass S u *
          (∑ i ∈ S, u i * V i * (x i) ^ 2) +
        weightedSecond S u (coefficientProduct V x) := by
  classical
  unfold weightedSecond coefficientLift coefficientProduct
  calc
    (∑ i ∈ S, u i * ((weightedMass S u + V i) * x i) ^ 2) =
        ∑ i ∈ S,
          ((weightedMass S u) ^ 2 * (u i * (x i) ^ 2) +
            (2 * weightedMass S u) * (u i * V i * (x i) ^ 2) +
            u i * (V i * x i) ^ 2) := by
              apply Finset.sum_congr rfl
              intro i hi
              ring
    _ = (∑ i ∈ S, (weightedMass S u) ^ 2 * (u i * (x i) ^ 2)) +
          (∑ i ∈ S, (2 * weightedMass S u) *
            (u i * V i * (x i) ^ 2)) +
          ∑ i ∈ S, u i * (V i * x i) ^ 2 := by
            rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
    _ = (weightedMass S u) ^ 2 * (∑ i ∈ S, u i * (x i) ^ 2) +
          2 * weightedMass S u *
            (∑ i ∈ S, u i * V i * (x i) ^ 2) +
          ∑ i ∈ S, u i * (V i * x i) ^ 2 := by
            rw [Finset.mul_sum, Finset.mul_sum]

/--
Centered tail-potential identity. The lifted pair energy is the baseline
`U^2` energy, plus a positive tail potential, plus the product-channel energy.
-/
theorem weightedPairEnergy_coefficientLift_of_centered
    {ι : Type*} (S : Finset ι) (u V x : ι → ℝ)
    (hcenter : weightedSum S u x = 0) :
    weightedPairEnergy S u (coefficientLift S u V x) =
      (weightedMass S u) ^ 2 * weightedPairEnergy S u x +
        4 * (weightedMass S u) ^ 2 *
          (∑ i ∈ S, u i * V i * (x i) ^ 2) +
        weightedPairEnergy S u (coefficientProduct V x) := by
  rw [weightedPairEnergy_eq_moments,
    weightedPairEnergy_eq_moments,
    weightedPairEnergy_eq_moments,
    weightedSecond_coefficientLift,
    weightedSum_coefficientLift_of_centered S u V x hcenter,
    hcenter]
  ring

/-- Dropping the nonnegative product-channel energy gives the sharp potential bound. -/
theorem weightedPairEnergy_coefficientLift_potential_le
    {ι : Type*} (S : Finset ι) (u V x : ι → ℝ)
    (hcenter : weightedSum S u x = 0)
    (hu : ∀ i ∈ S, 0 ≤ u i) :
    (weightedMass S u) ^ 2 * weightedPairEnergy S u x +
        4 * (weightedMass S u) ^ 2 *
          (∑ i ∈ S, u i * V i * (x i) ^ 2) ≤
      weightedPairEnergy S u (coefficientLift S u V x) := by
  rw [weightedPairEnergy_coefficientLift_of_centered S u V x hcenter]
  exact le_add_of_nonneg_right
    (weightedPairEnergy_nonneg S u (coefficientProduct V x) hu)

/-- If the tail coefficient is nonnegative, the lift dominates the baseline energy. -/
theorem weightedPairEnergy_coefficientLift_baseline_le
    {ι : Type*} (S : Finset ι) (u V x : ι → ℝ)
    (hcenter : weightedSum S u x = 0)
    (hu : ∀ i ∈ S, 0 ≤ u i)
    (hV : ∀ i ∈ S, 0 ≤ V i) :
    (weightedMass S u) ^ 2 * weightedPairEnergy S u x ≤
      weightedPairEnergy S u (coefficientLift S u V x) := by
  rw [weightedPairEnergy_coefficientLift_of_centered S u V x hcenter]
  have hpot : 0 ≤ ∑ i ∈ S, u i * V i * (x i) ^ 2 := by
    apply Finset.sum_nonneg
    intro i hi
    exact mul_nonneg (mul_nonneg (hu i hi) (hV i hi)) (sq_nonneg _)
  have hprod :
      0 ≤ weightedPairEnergy S u (coefficientProduct V x) :=
    weightedPairEnergy_nonneg S u (coefficientProduct V x) hu
  nlinarith [sq_nonneg (weightedMass S u)]

/-- Outside the centered subspace, reciprocal coefficient modes form a kernel. -/
theorem coefficientLift_reciprocal_mode
    {ι : Type*} (S : Finset ι) (u V : ι → ℝ) (C : ℝ)
    (hden : ∀ i ∈ S, weightedMass S u + V i ≠ 0) :
    weightedPairEnergy S u
      (coefficientLift S u V
        (fun i => C / (weightedMass S u + V i))) = 0 := by
  classical
  unfold weightedPairEnergy coefficientLift
  apply Finset.sum_eq_zero
  intro i hi
  apply Finset.sum_eq_zero
  intro j hj
  rw [mul_div_cancel₀ C (hden i hi), mul_div_cancel₀ C (hden j hj), sub_self]
  ring

end EnterpriseMath.WeightedCoefficientCoercivity
