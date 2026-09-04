import EnterpriseMath.Precision.DirichletDefectSeries
import EnterpriseMath.Precision.DirichletSineSeries
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Analysis.Normed.Group.InfiniteSum
import Mathlib.Order.ConditionallyCompleteLattice.Basic

namespace EnterpriseMath.Precision

open scoped BigOperators Nat

/-- The finite normalized unit-factor product in coefficient `j`. -/
noncomputable def dirichletFiniteUnitProduct (M j : ℕ) : ℝ :=
  ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r)

/-- The exact error majorant assembled from the coefficient-defect main term and factorial tail. -/
noncomputable def dirichletFiniteSineErrorBound (M : ℕ) (R : ℝ) : ℝ :=
  dirichletDefectSeriesValue R / (6 * (M : ℝ) ^ 2) +
    dirichletPositiveTailTerm R M 0 / (1 - dirichletTailRatio R M)

/-- The actual finite determinant written in the internal completion-series coefficients. -/
theorem dirichletFiniteSineDeterminant_eq_series_product
    (M : ℕ) (hM : 1 ≤ M) (x : ℝ) :
    dirichletFiniteSineDeterminant M x =
      ∑ j ∈ Finset.range M,
        dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j := by
  rw [dirichletFiniteSineDeterminant_eq M hM x]
  apply Finset.sum_congr rfl
  intro j hj
  simp [dirichletSineSeriesTerm, dirichletFiniteUnitProduct, dirichletUnitDefect]

/-- Exact absolute value of one internal completion-series coefficient. -/
theorem abs_dirichletSineSeriesTerm (x : ℝ) (j : ℕ) :
    |dirichletSineSeriesTerm x j| =
      |x| ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ) := by
  have hfac : 0 ≤ ((((2 * j + 1) ! : ℕ) : ℝ)) := by positivity
  simp [dirichletSineSeriesTerm, abs_mul, abs_div, abs_pow, abs_of_nonneg hfac]

/-- On `|x|≤R`, the absolute coefficient is bounded by the corresponding positive `R` term. -/
theorem abs_dirichletSineSeriesTerm_le
    (R x : ℝ) (hx : |x| ≤ R) (j : ℕ) :
    |dirichletSineSeriesTerm x j| ≤
      R ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ) := by
  rw [abs_dirichletSineSeriesTerm]
  apply div_le_div_of_nonneg_right
  · exact pow_le_pow_left₀ (abs_nonneg x) hx _
  · positivity

/-- Wrapper for nonnegativity of the finite unit-factor product. -/
theorem dirichletFiniteUnitProduct_nonneg (M j : ℕ) (hj : j < M) :
    0 ≤ dirichletFiniteUnitProduct M j := by
  simpa [dirichletFiniteUnitProduct] using
    dirichletUnitDefectProduct_nonneg M j hj

/-- Wrapper for the upper bound one on the finite unit-factor product. -/
theorem dirichletFiniteUnitProduct_le_one (M j : ℕ) (hj : j < M) :
    dirichletFiniteUnitProduct M j ≤ 1 := by
  simpa [dirichletFiniteUnitProduct] using
    dirichletUnitDefectProduct_le_one M j hj

/-- Wrapper for the finite coefficient-defect upper bound. -/
theorem one_sub_dirichletFiniteUnitProduct_le
    (M j : ℕ) (hj : j < M) :
    1 - dirichletFiniteUnitProduct M j ≤
      (j : ℝ) * ((j : ℝ) + 1) * (2 * (j : ℝ) + 1) /
        (6 * (M : ℝ) ^ 2) := by
  simpa [dirichletFiniteUnitProduct] using
    dirichletUnitDefectProduct_error_le_closed M j hj

/-- One coefficient of the finite determinant differs from the completion coefficient by the stated majorant. -/
theorem dirichletFiniteCoefficient_error_le
    (M j : ℕ) (R x : ℝ) (hj : j < M) (hx : |x| ≤ R) :
    |dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j -
        dirichletSineSeriesTerm x j| ≤
      dirichletDefectWeight R j / (6 * (M : ℝ) ^ 2) := by
  have hUle := dirichletFiniteUnitProduct_le_one M j hj
  have hdef0 : 0 ≤ 1 - dirichletFiniteUnitProduct M j := sub_nonneg.mpr hUle
  have hterm := abs_dirichletSineSeriesTerm_le R x hx j
  have hdef := one_sub_dirichletFiniteUnitProduct_le M j hj
  have hR : 0 ≤ R := (abs_nonneg x).trans hx
  have hbase :
      0 ≤ R ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ) := by positivity
  calc
    |dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j -
        dirichletSineSeriesTerm x j| =
        |dirichletSineSeriesTerm x j| *
          (1 - dirichletFiniteUnitProduct M j) := by
      rw [show dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j -
          dirichletSineSeriesTerm x j =
          dirichletSineSeriesTerm x j * (dirichletFiniteUnitProduct M j - 1) by ring]
      rw [abs_mul, abs_sub_comm,
        abs_of_nonneg (sub_nonneg.mpr hUle)]
    _ ≤ (R ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ)) *
          (1 - dirichletFiniteUnitProduct M j) :=
      mul_le_mul_of_nonneg_right hterm hdef0
    _ ≤ (R ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ)) *
          ((j : ℝ) * ((j : ℝ) + 1) * (2 * (j : ℝ) + 1) /
            (6 * (M : ℝ) ^ 2)) :=
      mul_le_mul_of_nonneg_left hdef hbase
    _ = dirichletDefectWeight R j / (6 * (M : ℝ) ^ 2) := by
      unfold dirichletDefectWeight
      have hfac : ((((2 * j + 1) ! : ℕ) : ℝ)) ≠ 0 := by positivity
      have hM : 0 < M := by omega
      have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hM)
      field_simp [hfac, hM0]
      ring

/-- Finite coefficient deformation contributes exactly the `O(M^-2)` main-term bound. -/
theorem dirichletFiniteSine_main_error_le
    (M : ℕ) (hM : 1 ≤ M) (R x : ℝ) (hx : |x| ≤ R) :
    |dirichletFiniteSineDeterminant M x - dirichletSinePartial M x| ≤
      dirichletDefectSeriesValue R / (6 * (M : ℝ) ^ 2) := by
  rw [dirichletFiniteSineDeterminant_eq_series_product M hM x]
  unfold dirichletSinePartial
  rw [← Finset.sum_sub_distrib]
  calc
    |∑ j ∈ Finset.range M,
        (dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j -
          dirichletSineSeriesTerm x j)| ≤
        ∑ j ∈ Finset.range M,
          |dirichletSineSeriesTerm x j * dirichletFiniteUnitProduct M j -
            dirichletSineSeriesTerm x j| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ j ∈ Finset.range M,
        dirichletDefectWeight R j / (6 * (M : ℝ) ^ 2) := by
      apply Finset.sum_le_sum
      intro j hj
      exact dirichletFiniteCoefficient_error_le M j R x
        (Finset.mem_range.mp hj) hx
    _ = (∑ j ∈ Finset.range M, dirichletDefectWeight R j) /
        (6 * (M : ℝ) ^ 2) := by
      rw [Finset.sum_div]
    _ ≤ dirichletDefectSeriesValue R / (6 * (M : ℝ) ^ 2) := by
      exact div_le_div_of_nonneg_right
        (sum_dirichletDefectWeight_le_value R M) (by positivity)

/-- One shifted alternating completion term is dominated by the positive factorial tail term. -/
theorem norm_dirichletSineSeriesTerm_shift_le
    (M k : ℕ) (R x : ℝ) (hx : |x| ≤ R) :
    ‖dirichletSineSeriesTerm x (k + M)‖ ≤
      dirichletPositiveTailTerm R M k := by
  rw [Real.norm_eq_abs, abs_dirichletSineSeriesTerm]
  unfold dirichletPositiveTailTerm
  rw [Nat.add_comm k M]
  apply div_le_div_of_nonneg_right
  · exact pow_le_pow_left₀ (abs_nonneg x) hx _
  · positivity

/-- The shifted alternating completion tail is bounded by the geometric factorial tail. -/
theorem dirichletSineSeries_tail_error_le
    (M : ℕ) (R x : ℝ) (hx : |x| ≤ R)
    (hq : dirichletTailRatio R M < 1) :
    |∑' k : ℕ, dirichletSineSeriesTerm x (k + M)| ≤
      dirichletPositiveTailTerm R M 0 / (1 - dirichletTailRatio R M) := by
  have hpos := (summable_dirichletPositiveTailTerm R M hq).hasSum
  have hnorm :
      ‖∑' k : ℕ, dirichletSineSeriesTerm x (k + M)‖ ≤
        ∑' k : ℕ, dirichletPositiveTailTerm R M k := by
    exact tsum_of_norm_bounded hpos
      (fun k => norm_dirichletSineSeriesTerm_shift_le M k R x hx)
  rw [← Real.norm_eq_abs]
  exact hnorm.trans (tsum_dirichletPositiveTailTerm_le R M hq)

/-- Truncating the internal completion series after the first `M` coefficients has the factorial-tail error. -/
theorem dirichletSinePartial_tail_error_le
    (M : ℕ) (R x : ℝ) (hx : |x| ≤ R)
    (hq : dirichletTailRatio R M < 1) :
    |dirichletSinePartial M x - dirichletSineSeries x| ≤
      dirichletPositiveTailTerm R M 0 / (1 - dirichletTailRatio R M) := by
  have hsplit := dirichletSineSeries_eq_partial_add_tail M x
  have heq :
      dirichletSinePartial M x - dirichletSineSeries x =
        -(∑' k : ℕ, dirichletSineSeriesTerm x (k + M)) := by
    rw [hsplit]
    ring
  rw [heq, abs_neg]
  exact dirichletSineSeries_tail_error_le M R x hx hq

/-- WSR-T02 pointwise error bound in its internally assembled form. -/
theorem dirichletFiniteSine_pointwise_error_le
    (M : ℕ) (hM : 2 ≤ M) (R x : ℝ) (hx : |x| ≤ R)
    (hgap : 0 < 1 - dirichletTailRatio R M) :
    |dirichletFiniteSineDeterminant M x - dirichletSineSeries x| ≤
      dirichletFiniteSineErrorBound M R := by
  have hq : dirichletTailRatio R M < 1 := by linarith
  have hmain := dirichletFiniteSine_main_error_le M (by omega) R x hx
  have htail := dirichletSinePartial_tail_error_le M R x hx hq
  unfold dirichletFiniteSineErrorBound
  calc
    |dirichletFiniteSineDeterminant M x - dirichletSineSeries x| =
        |(dirichletFiniteSineDeterminant M x - dirichletSinePartial M x) +
          (dirichletSinePartial M x - dirichletSineSeries x)| := by
      congr 1
      ring
    _ ≤ |dirichletFiniteSineDeterminant M x - dirichletSinePartial M x| +
        |dirichletSinePartial M x - dirichletSineSeries x| :=
      abs_add_le _ _
    _ ≤ dirichletDefectSeriesValue R / (6 * (M : ℝ) ^ 2) +
        dirichletPositiveTailTerm R M 0 / (1 - dirichletTailRatio R M) :=
      add_le_add hmain htail

/-- The internal WSR-T02 bound is exactly the explicit theorem-packet expression. -/
theorem dirichletFiniteSineErrorBound_eq_packet (M : ℕ) (R : ℝ) :
    dirichletFiniteSineErrorBound M R =
      (R ^ 2 * Real.cosh R + 3 * R * Real.sinh R) /
          (24 * (M : ℝ) ^ 2) +
        (R ^ (2 * M) / (((2 * M + 1) ! : ℕ) : ℝ)) *
          (1 / (1 -
            R ^ 2 / ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3)))) := by
  unfold dirichletFiniteSineErrorBound dirichletTailRatio
  rw [dirichletDefectSeriesValue_eq, dirichletPositiveTailTerm_zero]
  ring

/-- WSR-T02 pointwise certificate in the exact explicit form of the theorem packet. -/
theorem dirichletFiniteSine_pointwise_error_le_packet
    (M : ℕ) (hM : 2 ≤ M) (R x : ℝ) (hx : |x| ≤ R)
    (hgap :
      0 < 1 - R ^ 2 /
        ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3))) :
    |dirichletFiniteSineDeterminant M x - dirichletSineSeries x| ≤
      (R ^ 2 * Real.cosh R + 3 * R * Real.sinh R) /
          (24 * (M : ℝ) ^ 2) +
        (R ^ (2 * M) / (((2 * M + 1) ! : ℕ) : ℝ)) *
          (1 / (1 -
            R ^ 2 / ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3)))) := by
  have hgap' : 0 < 1 - dirichletTailRatio R M := by
    simpa [dirichletTailRatio] using hgap
  rw [← dirichletFiniteSineErrorBound_eq_packet]
  exact dirichletFiniteSine_pointwise_error_le M hM R x hx hgap'

/-- Values of the finite approximation error over the closed radius interval `|x|≤R`. -/
noncomputable def dirichletFiniteSineErrorSet (M : ℕ) (R : ℝ) : Set ℝ :=
  {y | ∃ x : ℝ, |x| ≤ R ∧
    y = |dirichletFiniteSineDeterminant M x - dirichletSineSeries x|}

/-- Compact-sup error observer used for the exact WSR-T02 certificate. -/
noncomputable def dirichletFiniteSineCompactError (M : ℕ) (R : ℝ) : ℝ :=
  sSup (dirichletFiniteSineErrorSet M R)

/-- WSR-T02 compact-sup certificate with the exact explicit theorem-packet constants. -/
theorem dirichletFiniteSine_compact_error_le_packet
    (M : ℕ) (hM : 2 ≤ M) (R : ℝ) (hR : 0 ≤ R)
    (hgap :
      0 < 1 - R ^ 2 /
        ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3))) :
    dirichletFiniteSineCompactError M R ≤
      (R ^ 2 * Real.cosh R + 3 * R * Real.sinh R) /
          (24 * (M : ℝ) ^ 2) +
        (R ^ (2 * M) / (((2 * M + 1) ! : ℕ) : ℝ)) *
          (1 / (1 -
            R ^ 2 / ((2 * (M : ℝ) + 2) * (2 * (M : ℝ) + 3)))) := by
  unfold dirichletFiniteSineCompactError
  apply csSup_le
  · refine ⟨|dirichletFiniteSineDeterminant M 0 - dirichletSineSeries 0|, ?_⟩
    refine ⟨0, ?_, rfl⟩
    simpa using hR
  · intro y hy
    rcases hy with ⟨x, hx, rfl⟩
    exact dirichletFiniteSine_pointwise_error_le_packet M hM R x hx hgap

end EnterpriseMath.Precision
