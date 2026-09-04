import EnterpriseMath.Relation.WeightedRelationMixer
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.WeightedTripleBranchMixer

open EnterpriseMath.WeightedCoefficientCoercivity
open EnterpriseMath.WeightedRelationMixer
open scoped BigOperators

/-- One ordered three-history label. -/
structure Triple (α : Type*) where
  first : α
  second : α
  third : α
  deriving DecidableEq

/-- Swap the first two history positions. -/
def swap12 {α : Type*} (t : Triple α) : Triple α :=
  ⟨t.second, t.first, t.third⟩

/-- Swap the first and third history positions. -/
def swap13 {α : Type*} (t : Triple α) : Triple α :=
  ⟨t.third, t.second, t.first⟩

/-- Swap the final two history positions. -/
def swap23 {α : Type*} (t : Triple α) : Triple α :=
  ⟨t.first, t.third, t.second⟩

@[simp] theorem swap12_swap12 {α : Type*} (t : Triple α) :
    swap12 (swap12 t) = t := by
  cases t
  rfl

@[simp] theorem swap13_swap13 {α : Type*} (t : Triple α) :
    swap13 (swap13 t) = t := by
  cases t
  rfl

@[simp] theorem swap23_swap23 {α : Type*} (t : Triple α) :
    swap23 (swap23 t) = t := by
  cases t
  rfl

/-- Product branch mass on ordered triples. -/
def productWeight {α : Type*} (u : α → ℝ) (t : Triple α) : ℝ :=
  u t.first * u t.second * u t.third

/-- Each position transposition preserves the product branch mass. -/
theorem productWeight_swap12 {α : Type*} (u : α → ℝ) (t : Triple α) :
    productWeight u (swap12 t) = productWeight u t := by
  unfold productWeight swap12
  ring

/-- Each position transposition preserves the product branch mass. -/
theorem productWeight_swap13 {α : Type*} (u : α → ℝ) (t : Triple α) :
    productWeight u (swap13 t) = productWeight u t := by
  unfold productWeight swap13
  ring

/-- Each position transposition preserves the product branch mass. -/
theorem productWeight_swap23 {α : Type*} (u : α → ℝ) (t : Triple α) :
    productWeight u (swap23 t) = productWeight u t := by
  unfold productWeight swap23
  ring

/-- Lift a scalar action value to the first history position. -/
def firstReadout {α : Type*} (value : α → ℝ) (t : Triple α) : ℝ :=
  value t.first

/-- Uniform Markov average over the three position transpositions. -/
def transpositionMixer {α : Type*}
    (F : Triple α → ℝ) (t : Triple α) : ℝ :=
  (F (swap12 t) + F (swap13 t) + F (swap23 t)) / 3

/-- The product branch mass is a pointwise stationary density for the mixer. -/
theorem transpositionMixer_productWeight
    {α : Type*} (u : α → ℝ) (t : Triple α) :
    transpositionMixer (productWeight u) t = productWeight u t := by
  unfold transpositionMixer
  rw [productWeight_swap12, productWeight_swap13, productWeight_swap23]
  ring

/-- The positive support of product branch mass is invariant under each swap. -/
theorem productWeight_pos_swap12_iff
    {α : Type*} (u : α → ℝ) (t : Triple α) :
    0 < productWeight u (swap12 t) ↔ 0 < productWeight u t := by
  rw [productWeight_swap12]

/-- The positive support of product branch mass is invariant under each swap. -/
theorem productWeight_pos_swap13_iff
    {α : Type*} (u : α → ℝ) (t : Triple α) :
    0 < productWeight u (swap13 t) ↔ 0 < productWeight u t := by
  rw [productWeight_swap13]

/-- The positive support of product branch mass is invariant under each swap. -/
theorem productWeight_pos_swap23_iff
    {α : Type*} (u : α → ℝ) (t : Triple α) :
    0 < productWeight u (swap23 t) ↔ 0 < productWeight u t := by
  rw [productWeight_swap23]

/-- On a first-coordinate readout, the local mixer is the three-label mean. -/
theorem transpositionMixer_firstReadout
    {α : Type*} (value : α → ℝ) (t : Triple α) :
    transpositionMixer (firstReadout value) t =
      (value t.first + value t.second + value t.third) / 3 := by
  unfold transpositionMixer firstReadout swap12 swap13 swap23
  ring

/-- Nonnegative branch readouts remain nonnegative under transposition averaging. -/
theorem transpositionMixer_nonneg
    {α : Type*} (F : Triple α → ℝ)
    (hF : ∀ t, 0 ≤ F t) (t : Triple α) :
    0 ≤ transpositionMixer F t := by
  unfold transpositionMixer
  positivity

/-- Unnormalized pushback of a triple readout to the first action label. -/
def pushFirstNumerator {α : Type*}
    (S : Finset α) (u : α → ℝ) (F : Triple α → ℝ) (a : α) : ℝ :=
  ∑ b in S, ∑ c in S, u b * u c * F ⟨a, b, c⟩

/-- Product-mass contribution of the first-coordinate term. -/
theorem pushFirst_sum_first
    {α : Type*} (S : Finset α) (u value : α → ℝ) (a : α) :
    (∑ b in S, ∑ c in S, u b * u c * value a) =
      (weightedMass S u) ^ 2 * value a := by
  classical
  unfold weightedMass
  calc
    (∑ b in S, ∑ c in S, u b * u c * value a) =
        ∑ b in S, u b * ((∑ c in S, u c) * value a) := by
          apply Finset.sum_congr rfl
          intro b hb
          rw [Finset.sum_mul]
          apply Finset.sum_congr rfl
          intro c hc
          ring
    _ = (∑ b in S, u b) * ((∑ c in S, u c) * value a) := by
          rw [Finset.sum_mul]
    _ = (∑ b in S, u b) ^ 2 * value a := by ring

/-- Product-mass contribution of the second-coordinate term. -/
theorem pushFirst_sum_second
    {α : Type*} (S : Finset α) (u value : α → ℝ) :
    (∑ b in S, ∑ c in S, u b * u c * value b) =
      weightedMass S u * weightedSum S u value := by
  classical
  unfold weightedMass weightedSum
  calc
    (∑ b in S, ∑ c in S, u b * u c * value b) =
        ∑ b in S, (u b * value b) * (∑ c in S, u c) := by
          apply Finset.sum_congr rfl
          intro b hb
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro c hc
          ring
    _ = (∑ b in S, u b * value b) * (∑ c in S, u c) := by
          rw [Finset.sum_mul]
    _ = (∑ c in S, u c) * (∑ b in S, u b * value b) := by ring

/-- Product-mass contribution of the third-coordinate term. -/
theorem pushFirst_sum_third
    {α : Type*} (S : Finset α) (u value : α → ℝ) :
    (∑ b in S, ∑ c in S, u b * u c * value c) =
      weightedMass S u * weightedSum S u value := by
  classical
  unfold weightedMass weightedSum
  calc
    (∑ b in S, ∑ c in S, u b * u c * value c) =
        ∑ b in S, u b * (∑ c in S, u c * value c) := by
          apply Finset.sum_congr rfl
          intro b hb
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro c hc
          ring
    _ = (∑ b in S, u b) * (∑ c in S, u c * value c) := by
          rw [Finset.sum_mul]

/-- Exact unnormalized lift--transpose--project formula. -/
theorem pushFirstNumerator_transpositionMixer
    {α : Type*} (S : Finset α) (u value : α → ℝ) (a : α) :
    pushFirstNumerator S u
        (transpositionMixer (firstReadout value)) a =
      ((weightedMass S u) ^ 2 * value a +
        2 * weightedMass S u * weightedSum S u value) / 3 := by
  classical
  unfold pushFirstNumerator
  simp_rw [transpositionMixer_firstReadout]
  calc
    (∑ b in S, ∑ c in S,
        u b * u c * ((value a + value b + value c) / 3)) =
      ((∑ b in S, ∑ c in S, u b * u c * value a) +
        (∑ b in S, ∑ c in S, u b * u c * value b) +
        (∑ b in S, ∑ c in S, u b * u c * value c)) / 3 := by
          simp_rw [Finset.sum_add_distrib]
          ring
    _ = ((weightedMass S u) ^ 2 * value a +
        2 * weightedMass S u * weightedSum S u value) / 3 := by
          rw [pushFirst_sum_first, pushFirst_sum_second, pushFirst_sum_third]
          ring

/-- Normalized pushback to the first action coordinate. -/
def pushFirst {α : Type*}
    (S : Finset α) (u : α → ℝ) (F : Triple α → ℝ) (a : α) : ℝ :=
  pushFirstNumerator S u F a / (weightedMass S u) ^ 2

/-- The normalized triple branch mixer is exactly the weighted `S_3` value mixer. -/
theorem pushFirst_transpositionMixer
    {α : Type*} (S : Finset α) (u value : α → ℝ) (a : α)
    (hU : weightedMass S u ≠ 0) :
    pushFirst S u (transpositionMixer (firstReadout value)) a =
      s3ValueMixer
        (weightedSum S u value / weightedMass S u) value a := by
  unfold pushFirst s3ValueMixer
  rw [pushFirstNumerator_transpositionMixer]
  field_simp [hU]
  ring

end EnterpriseMath.WeightedTripleBranchMixer
