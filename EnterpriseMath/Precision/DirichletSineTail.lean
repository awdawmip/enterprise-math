import EnterpriseMath.Precision.DirichletCoefficientDefect
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace EnterpriseMath.Precision

open scoped BigOperators Nat

/-- Positive factorial tail term beginning at coefficient index `M`. -/
noncomputable def dirichletPositiveTailTerm (R : ℝ) (M k : ℕ) : ℝ :=
  R ^ (2 * (M + k)) / (((2 * (M + k) + 1) ! : ℕ) : ℝ)

/-- Uniform geometric ratio used to dominate the whole factorial tail. -/
noncomputable def dirichletTailRatio (R : ℝ) (M : ℕ) : ℝ :=
  R ^ 2 / ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3))

/-- Positive tail terms are nonnegative. -/
theorem dirichletPositiveTailTerm_nonneg (R : ℝ) (M k : ℕ) :
    0 ≤ dirichletPositiveTailTerm R M k := by
  have hpow : 0 ≤ R ^ (2 * (M + k)) := by
    rw [show 2 * (M + k) = (M + k) + (M + k) by omega, pow_add]
    exact mul_self_nonneg _
  unfold dirichletPositiveTailTerm
  exact div_nonneg hpow (by positivity)

/-- The uniform tail ratio is nonnegative. -/
theorem dirichletTailRatio_nonneg (R : ℝ) (M : ℕ) :
    0 ≤ dirichletTailRatio R M := by
  unfold dirichletTailRatio
  positivity

/-- Exact one-step factorial ratio for the shifted positive tail. -/
theorem dirichletPositiveTailTerm_succ (R : ℝ) (M k : ℕ) :
    dirichletPositiveTailTerm R M (k + 1) =
      dirichletPositiveTailTerm R M k *
        (R ^ 2 /
          ((2 * (((M + k : ℕ) : ℝ)) + 2) *
            (2 * (((M + k : ℕ) : ℝ)) + 3))) := by
  have hexp : 2 * (M + (k + 1)) = 2 * (M + k) + 2 := by omega
  have hfac :
      (2 * (M + (k + 1)) + 1)! =
        (2 * (M + k) + 3) * (2 * (M + k) + 2) * (2 * (M + k) + 1)! := by
    grind [Nat.factorial_succ]
  unfold dirichletPositiveTailTerm
  rw [hfac, hexp, pow_add]
  push_cast
  have hf : ((((2 * (M + k) + 1)! : ℕ) : ℝ)) ≠ 0 := by positivity
  have h2 : (2 * (((M + k : ℕ) : ℝ)) + 2) ≠ 0 := by positivity
  have h3 : (2 * (((M + k : ℕ) : ℝ)) + 3) ≠ 0 := by positivity
  field_simp [hf, h2, h3]

/-- Every later factorial ratio is bounded by the first tail ratio. -/
theorem dirichletTailStepRatio_le (R : ℝ) (M k : ℕ) :
    R ^ 2 /
        ((2 * (((M + k : ℕ) : ℝ)) + 2) *
          (2 * (((M + k : ℕ) : ℝ)) + 3)) ≤
      dirichletTailRatio R M := by
  have hk0 : 0 ≤ (k : ℝ) := by positivity
  have hM0 : 0 ≤ (M : ℝ) := by positivity
  have hden :
      (2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3) ≤
        (2 * (((M + k : ℕ) : ℝ)) + 2) *
          (2 * (((M + k : ℕ) : ℝ)) + 3) := by
    push_cast
    nlinarith [mul_nonneg hk0 (by positivity : 0 ≤ 4 * (M : ℝ) + 5), sq_nonneg (k : ℝ)]
  unfold dirichletTailRatio
  exact div_le_div_of_nonneg_left (sq_nonneg R) (by positivity) hden

/-- The factorial tail is pointwise dominated by the first term times a geometric progression. -/
theorem dirichletPositiveTailTerm_le_geometric (R : ℝ) (M k : ℕ) :
    dirichletPositiveTailTerm R M k ≤
      dirichletPositiveTailTerm R M 0 * (dirichletTailRatio R M) ^ k := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [dirichletPositiveTailTerm_succ]
      calc
        dirichletPositiveTailTerm R M k *
              (R ^ 2 /
                ((2 * (((M + k : ℕ) : ℝ)) + 2) *
                  (2 * (((M + k : ℕ) : ℝ)) + 3))) ≤
            (dirichletPositiveTailTerm R M 0 *
                (dirichletTailRatio R M) ^ k) *
              (R ^ 2 /
                ((2 * (((M + k : ℕ) : ℝ)) + 2) *
                  (2 * (((M + k : ℕ) : ℝ)) + 3))) := by
          apply mul_le_mul_of_nonneg_right ih
          positivity
        _ ≤ (dirichletPositiveTailTerm R M 0 *
                (dirichletTailRatio R M) ^ k) *
              dirichletTailRatio R M := by
          apply mul_le_mul_of_nonneg_left (dirichletTailStepRatio_le R M k)
          exact mul_nonneg (dirichletPositiveTailTerm_nonneg R M 0)
            (pow_nonneg (dirichletTailRatio_nonneg R M) k)
        _ = dirichletPositiveTailTerm R M 0 *
              (dirichletTailRatio R M) ^ (k + 1) := by
          rw [pow_succ]
          ring

/-- The positive factorial tail is summable whenever the uniform ratio is below one. -/
theorem summable_dirichletPositiveTailTerm
    (R : ℝ) (M : ℕ) (hq : dirichletTailRatio R M < 1) :
    Summable (fun k : ℕ => dirichletPositiveTailTerm R M k) := by
  have hgeo : Summable (fun k : ℕ => (dirichletTailRatio R M) ^ k) :=
    summable_geometric_of_lt_one (dirichletTailRatio_nonneg R M) hq
  refine Summable.of_nonneg_of_le
    (fun k => dirichletPositiveTailTerm_nonneg R M k)
    (fun k => dirichletPositiveTailTerm_le_geometric R M k) ?_
  exact hgeo.mul_left (dirichletPositiveTailTerm R M 0)

/--
Geometric bound for the whole positive factorial tail, in the exact shape used by WSR-T02.
-/
theorem tsum_dirichletPositiveTailTerm_le
    (R : ℝ) (M : ℕ) (hq : dirichletTailRatio R M < 1) :
    (∑' k : ℕ, dirichletPositiveTailTerm R M k) ≤
      dirichletPositiveTailTerm R M 0 /
        (1 - dirichletTailRatio R M) := by
  have hgeo := hasSum_geometric_of_lt_one (dirichletTailRatio_nonneg R M) hq
  have hmaj := hgeo.mul_left (dirichletPositiveTailTerm R M 0)
  have htail := summable_dirichletPositiveTailTerm R M hq
  calc
    (∑' k : ℕ, dirichletPositiveTailTerm R M k) ≤
        ∑' k : ℕ,
          dirichletPositiveTailTerm R M 0 * (dirichletTailRatio R M) ^ k := by
      exact htail.tsum_le_tsum
        (fun k => dirichletPositiveTailTerm_le_geometric R M k)
        hmaj.summable
    _ = dirichletPositiveTailTerm R M 0 *
        (1 - dirichletTailRatio R M)⁻¹ := hmaj.tsum_eq
    _ = dirichletPositiveTailTerm R M 0 /
        (1 - dirichletTailRatio R M) := by rw [div_eq_mul_inv]

/-- Expanded first term of the positive tail. -/
theorem dirichletPositiveTailTerm_zero (R : ℝ) (M : ℕ) :
    dirichletPositiveTailTerm R M 0 =
      R ^ (2 * M) / (((2 * M + 1) ! : ℕ) : ℝ) := by
  simp [dirichletPositiveTailTerm]

end EnterpriseMath.Precision
