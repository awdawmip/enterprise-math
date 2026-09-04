import EnterpriseMath.Relation.OrderedQuotientCurvature
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.WeightedQuotientRelationField

open EnterpriseMath.PrimePowerQuotientTriangle
open EnterpriseMath.OrderedQuotientCurvature
open scoped BigOperators

/-- Capacity-weighted relation field `Z_ij = m_j c_i - m_i c_j`. -/
def relationField {ι : Type*}
    (mass total : ι → ℝ) (i j : ι) : ℝ :=
  mass j * total i - mass i * total j

@[simp] theorem relationField_self {ι : Type*}
    (mass total : ι → ℝ) (i : ι) :
    relationField mass total i i = 0 := by
  simp [relationField]

/-- The weighted relation field is antisymmetric. -/
theorem relationField_swap {ι : Type*}
    (mass total : ι → ℝ) (i j : ι) :
    relationField mass total j i = -relationField mass total i j := by
  unfold relationField
  ring

/-- Exact weighted three-block closure law from the accepted relation-field carrier. -/
theorem relationField_closure {ι : Type*}
    (mass total : ι → ℝ) (i j k : ι) :
    mass k * relationField mass total i j +
        mass i * relationField mass total j k +
        mass j * relationField mass total k i = 0 := by
  unfold relationField
  ring

/-- Total capacity of a finite block family. -/
def blockMass {ι : Type*} (S : Finset ι) (mass : ι → ℝ) : ℝ :=
  ∑ i in S, mass i

/-- Grand total carried by a finite block family. -/
def blockTotal {ι : Type*} (S : Finset ι) (total : ι → ℝ) : ℝ :=
  ∑ i in S, total i

/-- Row sum of the internal weighted relation field. -/
def relationRowSum {ι : Type*}
    (S : Finset ι) (mass total : ι → ℝ) (i : ι) : ℝ :=
  ∑ j in S, relationField mass total i j

/-- Exact row-sum identity behind weighted block recovery. -/
theorem relationRowSum_eq
    {ι : Type*} (S : Finset ι) (mass total : ι → ℝ) (i : ι) :
    relationRowSum S mass total i =
      blockMass S mass * total i - mass i * blockTotal S total := by
  classical
  unfold relationRowSum relationField blockMass blockTotal
  rw [Finset.sum_sub_distrib, Finset.sum_mul, ← Finset.mul_sum]

/-- Mass, grand total, and relation-row sum recover the weighted block numerator. -/
theorem relationField_recovery_numerator
    {ι : Type*} (S : Finset ι) (mass total : ι → ℝ) (i : ι) :
    blockMass S mass * total i =
      mass i * blockTotal S total + relationRowSum S mass total i := by
  rw [relationRowSum_eq]
  ring

/-- If total capacity is nonzero, every block total is recovered exactly. -/
theorem relationField_recovers_total
    {ι : Type*} (S : Finset ι) (mass total : ι → ℝ) (i : ι)
    (hM : blockMass S mass ≠ 0) :
    total i =
      (mass i * blockTotal S total + relationRowSum S mass total i) /
        blockMass S mass := by
  apply (eq_div_iff hM).2
  simpa [mul_comm] using relationField_recovery_numerator S mass total i

/-- Quotient-cloud block total: capacity times the field value at that endpoint. -/
def quotientCloudTotal
    (u : ℕ → ℝ) (f : ℕ → ℝ) (n a : ℕ) : ℝ :=
  u a * f (quotient a n)

/--
For quotient-cloud totals, the weighted relation field is exactly mass product
times the ordered endpoint difference.
-/
theorem relationField_quotientCloud
    (u : ℕ → ℝ) (f : ℕ → ℝ) (n a b : ℕ) :
    relationField u (quotientCloudTotal u f n) a b =
      u a * u b * (f (quotient a n) - f (quotient b n)) := by
  unfold relationField quotientCloudTotal
  ring

/-- Finite signless return residual over an action family. -/
def signlessReturnResidual
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ c in S, u c * defect c f n

/-- The residual is total mass times the vertex plus the quotient average. -/
theorem signlessReturnResidual_eq
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) :
    signlessReturnResidual S u f n =
      totalWeight S u * f n +
        ∑ c in S, u c * f (quotient c n) := by
  classical
  unfold signlessReturnResidual totalWeight defect
  rw [Finset.sum_add_distrib, Finset.sum_mul]

/--
Pointwise transport identity: one relation field plus its common-suffix
transport is the difference of two signless endpoint residuals.
-/
theorem relationField_signless_transport
    (u : ℕ → ℝ) (f : ℕ → ℝ) (n a b c : ℕ) :
    relationField u (quotientCloudTotal u f n) a b +
        relationField u (quotientCloudTotal u f (quotient c n)) a b =
      u a * u b *
        (defect c f (quotient a n) - defect c f (quotient b n)) := by
  rw [relationField_quotientCloud, relationField_quotientCloud]
  simp [defect, quotient, Nat.div_div_eq_div_mul, Nat.mul_comm,
    Nat.mul_left_comm, Nat.mul_assoc]
  ring

/--
Exact operator-valued lift of the scalar signless return law to every internal
relation-field coordinate.
-/
theorem relationField_return_lift
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n a b : ℕ) :
    totalWeight S u *
          relationField u (quotientCloudTotal u f n) a b +
        ∑ c in S, u c *
          relationField u (quotientCloudTotal u f (quotient c n)) a b =
      u a * u b *
        (signlessReturnResidual S u f (quotient a n) -
          signlessReturnResidual S u f (quotient b n)) := by
  classical
  unfold totalWeight signlessReturnResidual
  rw [Finset.sum_mul, ← Finset.sum_add_distrib,
    ← Finset.sum_sub_distrib, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro c hc
  have h := relationField_signless_transport u f n a b c
  calc
    u c * relationField u (quotientCloudTotal u f n) a b +
        u c * relationField u (quotientCloudTotal u f (quotient c n)) a b =
      u c *
        (relationField u (quotientCloudTotal u f n) a b +
          relationField u (quotientCloudTotal u f (quotient c n)) a b) := by
            ring
    _ = u c *
        (u a * u b *
          (defect c f (quotient a n) - defect c f (quotient b n))) := by
            rw [h]
    _ = u a * u b *
        (u c * defect c f (quotient a n) -
          u c * defect c f (quotient b n)) := by
            ring

/-- Normalized quotient transport of one internal relation coordinate. -/
def relationTransportAverage
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ)
    (n a b : ℕ) : ℝ :=
  (∑ c in S, u c *
    relationField u (quotientCloudTotal u f (quotient c n)) a b) /
      totalWeight S u

/-- Normalized form of the exact relation-field return equation. -/
theorem relationField_normalized_return_lift
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n a b : ℕ)
    (hU : totalWeight S u ≠ 0) :
    relationField u (quotientCloudTotal u f n) a b +
        relationTransportAverage S u f n a b =
      (u a * u b / totalWeight S u) *
        (signlessReturnResidual S u f (quotient a n) -
          signlessReturnResidual S u f (quotient b n)) := by
  unfold relationTransportAverage
  have h := relationField_return_lift S u f n a b
  calc
    relationField u (quotientCloudTotal u f n) a b +
        (∑ c in S, u c *
          relationField u (quotientCloudTotal u f (quotient c n)) a b) /
            totalWeight S u =
      (totalWeight S u *
          relationField u (quotientCloudTotal u f n) a b +
        ∑ c in S, u c *
          relationField u (quotientCloudTotal u f (quotient c n)) a b) /
            totalWeight S u := by
              field_simp [hU]
              ring
    _ = (u a * u b *
        (signlessReturnResidual S u f (quotient a n) -
          signlessReturnResidual S u f (quotient b n))) /
            totalWeight S u := by
              rw [h]
    _ = (u a * u b / totalWeight S u) *
        (signlessReturnResidual S u f (quotient a n) -
          signlessReturnResidual S u f (quotient b n)) := by
              field_simp [hU]

/-- Positive pairing of the internal relation field with its endpoint difference. -/
def relationFieldEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ a in S, ∑ b in S,
    relationField u (quotientCloudTotal u f n) a b *
      (f (quotient a n) - f (quotient b n))

/-- The relation-field pairing is exactly the pairwise quotient curvature energy. -/
theorem relationFieldEnergy_eq_pairCurvatureEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) :
    relationFieldEnergy S u f n = pairCurvatureEnergy S u f n := by
  classical
  unfold relationFieldEnergy pairCurvatureEnergy
  apply Finset.sum_congr rfl
  intro a ha
  apply Finset.sum_congr rfl
  intro b hb
  rw [relationField_quotientCloud]
  ring

/-- Nonnegative masses make the relation-field energy manifestly nonnegative. -/
theorem relationFieldEnergy_nonneg
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ)
    (hu : ∀ a ∈ S, 0 ≤ u a) :
    0 ≤ relationFieldEnergy S u f n := by
  rw [relationFieldEnergy_eq_pairCurvatureEnergy]
  unfold pairCurvatureEnergy
  apply Finset.sum_nonneg
  intro a ha
  apply Finset.sum_nonneg
  intro b hb
  exact mul_nonneg (mul_nonneg (hu a ha) (hu b hb)) (sq_nonneg _)

/-- The quotient-cloud variance is the normalized internal relation-field energy. -/
theorem quotientCloudVariance_eq_relationFieldEnergy_div
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) :
    quotientCloudVariance S u f n =
      relationFieldEnergy S u f n / (2 * totalWeight S u) := by
  unfold quotientCloudVariance
  rw [relationFieldEnergy_eq_pairCurvatureEnergy]

/--
The ordered cubic curvature is exactly total mass times the internal
capacity-weighted relation-field energy.
-/
theorem cubicCurvatureEnergy_eq_totalWeight_mul_relationFieldEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) :
    cubicCurvatureEnergy S u f n =
      totalWeight S u * relationFieldEnergy S u f n := by
  rw [cubicCurvatureEnergy_eq_totalWeight_mul_pairCurvatureEnergy,
    ← relationFieldEnergy_eq_pairCurvatureEnergy]

/-- A fully averaged block state has zero internal weighted relation field. -/
def uniformTotal {ι : Type*}
    (mass : ι → ℝ) (mean : ℝ) (i : ι) : ℝ :=
  mass i * mean

@[simp] theorem relationField_uniformTotal {ι : Type*}
    (mass : ι → ℝ) (mean : ℝ) (i j : ι) :
    relationField mass (uniformTotal mass mean) i j = 0 := by
  unfold relationField uniformTotal
  ring

/-- With nonzero endpoint masses, vanishing relation is exactly endpoint equality. -/
theorem relationField_quotientCloud_eq_zero_iff
    (u : ℕ → ℝ) (f : ℕ → ℝ) (n a b : ℕ)
    (hua : u a ≠ 0) (hub : u b ≠ 0) :
    relationField u (quotientCloudTotal u f n) a b = 0 ↔
      f (quotient a n) = f (quotient b n) := by
  rw [relationField_quotientCloud]
  constructor
  · intro h
    have hab : u a * u b ≠ 0 := mul_ne_zero hua hub
    have hdiff : f (quotient a n) - f (quotient b n) = 0 := by
      exact (mul_eq_zero.mp h).resolve_left hab
    linarith
  · intro h
    rw [h, sub_self, mul_zero]

end EnterpriseMath.WeightedQuotientRelationField
