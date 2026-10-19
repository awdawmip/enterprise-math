import EnterpriseMath.Relation.DeepChamberColorBalance
import EnterpriseMath.Relation.WeightedCoefficientCoercivity
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberConditionalVariance

open EnterpriseMath.DeepChamberColorBalance
open EnterpriseMath.WeightedCoefficientCoercivity
open scoped BigOperators

/-- Endpoint-weighted total of one color channel. -/
def colorTotal
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ) (j : Fin 3) : ℝ :=
  weightedSum S κ (H j)

/-- Endpoint-weighted second moment over all three color channels. -/
def deepL2Energy
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ) : ℝ :=
  weightedSecond S κ (H 0) +
    weightedSecond S κ (H 1) +
    weightedSecond S κ (H 2)

/-- Squared energy of the three unnormalized color totals. -/
def colorTotalEnergy
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ) : ℝ :=
  (colorTotal S κ H 0) ^ 2 +
    (colorTotal S κ H 1) ^ 2 +
    (colorTotal S κ H 2) ^ 2

/-- Total within-color endpoint pair energy. -/
def withinEndpointPairEnergy
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ) : ℝ :=
  weightedPairEnergy S κ (H 0) +
    weightedPairEnergy S κ (H 1) +
    weightedPairEnergy S κ (H 2)

/-- One-color second moment decomposes into its color total and endpoint variance. -/
theorem weightedSecond_eq_total_sq_add_pair
    (S : Finset ℕ) (κ x : ℕ → ℝ)
    (hK : weightedMass S κ ≠ 0) :
    weightedSecond S κ x =
      (weightedSum S κ x) ^ 2 / weightedMass S κ +
        weightedPairEnergy S κ x / (2 * weightedMass S κ) := by
  rw [weightedPairEnergy_eq_moments]
  field_simp [hK] <;> ring

/--
Exact colored law of total variance: deep energy is color-mean energy plus
within-color endpoint fluctuation.
-/
theorem deepL2Energy_decomposition
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ)
    (hK : weightedMass S κ ≠ 0) :
    deepL2Energy S κ H =
      colorTotalEnergy S κ H / weightedMass S κ +
        withinEndpointPairEnergy S κ H /
          (2 * weightedMass S κ) := by
  unfold deepL2Energy colorTotalEnergy withinEndpointPairEnergy colorTotal
  rw [weightedSecond_eq_total_sq_add_pair S κ (H 0) hK,
    weightedSecond_eq_total_sq_add_pair S κ (H 1) hK,
    weightedSecond_eq_total_sq_add_pair S κ (H 2) hK]
  ring

/-- Pointwise standard color channels have standard color totals. -/
theorem colorTotals_standard
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ)
    (hstd : ∀ m ∈ S, H 0 m + H 1 m + H 2 m = 0) :
    colorTotal S κ H 0 + colorTotal S κ H 1 +
      colorTotal S κ H 2 = 0 := by
  classical
  unfold colorTotal weightedSum
  calc
    (∑ m ∈ S, κ m * H 0 m) +
        (∑ m ∈ S, κ m * H 1 m) +
        (∑ m ∈ S, κ m * H 2 m) =
      ∑ m ∈ S, κ m * (H 0 m + H 1 m + H 2 m) := by
        simp_rw [Finset.sum_add_distrib]
        apply Finset.sum_congr rfl
        intro m hm
        ring
    _ = 0 := by
      apply Finset.sum_eq_zero
      intro m hm
      simp only [hstd m hm, mul_zero]

/-- Color-total energy of a pointwise standard channel is its reduced standard energy. -/
theorem colorTotalEnergy_eq_standardPairEnergy_div_three
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ)
    (hstd : ∀ m ∈ S, H 0 m + H 1 m + H 2 m = 0) :
    colorTotalEnergy S κ H =
      ((colorTotal S κ H 0 - colorTotal S κ H 1) ^ 2 +
        (colorTotal S κ H 1 - colorTotal S κ H 2) ^ 2 +
        (colorTotal S κ H 2 - colorTotal S κ H 0) ^ 2) / 3 := by
  have hsum := colorTotals_standard S κ H hstd
  unfold colorTotalEnergy
  nlinarith [sq_nonneg
    (colorTotal S κ H 0 + colorTotal S κ H 1 + colorTotal S κ H 2)]

/-- The within-endpoint term is nonnegative for nonnegative endpoint masses. -/
theorem withinEndpointPairEnergy_nonneg
    (S : Finset ℕ) (κ : ℕ → ℝ) (H : Fin 3 → ℕ → ℝ)
    (hκ : ∀ m ∈ S, 0 ≤ κ m) :
    0 ≤ withinEndpointPairEnergy S κ H := by
  unfold withinEndpointPairEnergy
  have h0 := weightedPairEnergy_nonneg S κ (H 0) hκ
  have h1 := weightedPairEnergy_nonneg S κ (H 1) hκ
  have h2 := weightedPairEnergy_nonneg S κ (H 2) hκ
  linarith

end EnterpriseMath.DeepChamberConditionalVariance
