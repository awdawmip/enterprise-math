import EnterpriseMath.Relation.PrimePowerQuotientTriangle
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.OrderedQuotientCurvature

open EnterpriseMath.PrimePowerQuotientTriangle
open scoped BigOperators

/--
The ordered common-suffix curvature compares two signless edges whose total
quotient labels recoalesce to the same product.  The first intermediate vertex
is retained, so the expression remains sensitive to ordered provenance.
-/
def commonSuffixCurvature
    (a b suffix : ℕ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  defect (b * suffix) f (quotient a n) -
    defect (a * suffix) f (quotient b n)

/--
Common-endpoint cancellation: appending the same suffix to both ordered
histories cancels the recoalesced endpoint and leaves exactly the difference
of the two first intermediate values.
-/
theorem commonSuffixCurvature_eq_intermediate_sub
    (a b suffix : ℕ) (f : ℕ → ℝ) (n : ℕ) :
    commonSuffixCurvature a b suffix f n =
      f (quotient a n) - f (quotient b n) := by
  simp only [commonSuffixCurvature, defect, quotient, Nat.div_div_eq_div_mul]
  have hprod : a * (b * suffix) = b * (a * suffix) := by
    ac_rfl
  rw [hprod]
  ring

/-- The lifted curvature is independent of the chosen common suffix. -/
theorem commonSuffixCurvature_invariant
    (a b suffix₁ suffix₂ : ℕ) (f : ℕ → ℝ) (n : ℕ) :
    commonSuffixCurvature a b suffix₁ f n =
      commonSuffixCurvature a b suffix₂ f n := by
  rw [commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub]

/-- Reversing the two ordered histories reverses the curvature orientation. -/
theorem commonSuffixCurvature_swap
    (a b suffix : ℕ) (f : ℕ → ℝ) (n : ℕ) :
    commonSuffixCurvature b a suffix f n =
      -commonSuffixCurvature a b suffix f n := by
  rw [commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub]
  ring

/-- Exact Bianchi/cocycle identity on every action-label triangle. -/
theorem commonSuffixCurvature_cocycle
    (a b c suffix : ℕ) (f : ℕ → ℝ) (n : ℕ) :
    commonSuffixCurvature a b suffix f n +
        commonSuffixCurvature b c suffix f n +
        commonSuffixCurvature c a suffix f n = 0 := by
  rw [commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub,
    commonSuffixCurvature_eq_intermediate_sub]
  ring

/-- Total mass of a finite family of action weights. -/
def totalWeight (S : Finset ℕ) (u : ℕ → ℝ) : ℝ :=
  ∑ a in S, u a

/-- Unnormalized pairwise quotient-cloud variance numerator. -/
def pairCurvatureEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ a in S, ∑ b in S,
    u a * u b * (f (quotient a n) - f (quotient b n)) ^ 2

/--
Ordered degree-three curvature energy.  For each triple `(a,b,c)`, the two
compared signless edges terminate at the common quotient state `q_(abc)(n)`.
-/
def cubicCurvatureEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ a in S, ∑ b in S, ∑ c in S,
    u a * u b * u c * (commonSuffixCurvature a b c f n) ^ 2

/--
Exact degree lift: the cubic ordered-provenance energy is the total action
mass times the pairwise quotient-cloud variance numerator.
-/
theorem cubicCurvatureEnergy_eq_totalWeight_mul_pairCurvatureEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) :
    cubicCurvatureEnergy S u f n =
      totalWeight S u * pairCurvatureEnergy S u f n := by
  classical
  unfold cubicCurvatureEnergy pairCurvatureEnergy totalWeight
  simp_rw [commonSuffixCurvature_eq_intermediate_sub]
  calc
    (∑ a in S, ∑ b in S, ∑ c in S,
        u a * u b * u c *
          (f (quotient a n) - f (quotient b n)) ^ 2) =
        ∑ a in S, ∑ b in S,
          (u a * u b *
              (f (quotient a n) - f (quotient b n)) ^ 2) *
            (∑ c in S, u c) := by
      apply Finset.sum_congr rfl
      intro a ha
      apply Finset.sum_congr rfl
      intro b hb
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro c hc
      ring
    _ = (∑ c in S, u c) *
        (∑ a in S, ∑ b in S,
          u a * u b *
            (f (quotient a n) - f (quotient b n)) ^ 2) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro a ha
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro b hb
      ring

/-- Standard normalized weighted quotient-cloud variance. -/
def quotientCloudVariance
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ) : ℝ :=
  pairCurvatureEnergy S u f n / (2 * totalWeight S u)

/-- Cubic ordered curvature gives exactly the normalized cloud variance. -/
theorem quotientCloudVariance_eq_normalized_cubicCurvatureEnergy
    (S : Finset ℕ) (u : ℕ → ℝ) (f : ℕ → ℝ) (n : ℕ)
    (hU : totalWeight S u ≠ 0) :
    quotientCloudVariance S u f n =
      cubicCurvatureEnergy S u f n / (2 * (totalWeight S u) ^ 2) := by
  unfold quotientCloudVariance
  rw [cubicCurvatureEnergy_eq_totalWeight_mul_pairCurvatureEnergy]
  field_simp [hU] <;> ring

end EnterpriseMath.OrderedQuotientCurvature
