import EnterpriseMath.Precision.DirichletSineTail
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Series
import Mathlib.Topology.Algebra.InfiniteSum.NatInt

namespace EnterpriseMath.Precision

open scoped BigOperators Nat

/-- The target-free even power-series term completing the finite Dirichlet sine carrier. -/
noncomputable def dirichletSineSeriesTerm (x : ℝ) (j : ℕ) : ℝ :=
  (-1 : ℝ) ^ j * x ^ (2 * j) / (((2 * j + 1) ! : ℕ) : ℝ)

/-- Finite truncation of the internally defined completion series. -/
noncomputable def dirichletSinePartial (M : ℕ) (x : ℝ) : ℝ :=
  ∑ j ∈ Finset.range M, dirichletSineSeriesTerm x j

/-- Internal power-series completion target.  This is defined as a `tsum`, not as `sin x / x`. -/
noncomputable def dirichletSineSeries (x : ℝ) : ℝ :=
  ∑' j : ℕ, dirichletSineSeriesTerm x j

/-- At the origin, the internal series is the single nonzero term `1,0,0,...`. -/
theorem dirichletSineSeriesTerm_zero (j : ℕ) :
    dirichletSineSeriesTerm 0 j = if j = 0 then 1 else 0 := by
  cases j with
  | zero => norm_num [dirichletSineSeriesTerm]
  | succ j =>
      simp [dirichletSineSeriesTerm, Nat.succ_ne_zero]

/-- The internal completion series is summable for every real argument. -/
theorem summable_dirichletSineSeriesTerm (x : ℝ) :
    Summable (fun j : ℕ => dirichletSineSeriesTerm x j) := by
  by_cases hx : x = 0
  · subst x
    have hsingle : HasSum (fun j : ℕ => if j = 0 then (1 : ℝ) else 0) 1 :=
      hasSum_ite_eq 0 1
    refine (HasSum.congr_fun hsingle (fun j => ?_)).summable
    exact (dirichletSineSeriesTerm_zero j).symm
  · have hs := (Real.hasSum_sin x).div_const x
    refine (HasSum.congr_fun hs (fun j => ?_)).summable
    unfold dirichletSineSeriesTerm
    have hfac : ((((2 * j + 1) ! : ℕ) : ℝ)) ≠ 0 := by positivity
    rw [show 2 * j + 1 = 2 * j + 1 by rfl, pow_succ]
    field_simp [hx, hfac]
    ring

/-- The `tsum` definition is realized by the proven summable series. -/
theorem hasSum_dirichletSineSeriesTerm (x : ℝ) :
    HasSum (fun j : ℕ => dirichletSineSeriesTerm x j)
      (dirichletSineSeries x) := by
  unfold dirichletSineSeries
  exact (summable_dirichletSineSeriesTerm x).hasSum

/-- Exact decomposition of the internal completion into the first `M` coefficients and its tail. -/
theorem dirichletSineSeries_eq_partial_add_tail (M : ℕ) (x : ℝ) :
    dirichletSineSeries x =
      dirichletSinePartial M x +
        ∑' k : ℕ, dirichletSineSeriesTerm x (k + M) := by
  unfold dirichletSineSeries dirichletSinePartial
  simpa using (summable_dirichletSineSeriesTerm x).sum_add_tsum_nat_add M

/-- Outside the origin, the internal series is compatibly read as `sin x / x`. -/
theorem dirichletSineSeries_eq_sin_div (x : ℝ) (hx : x ≠ 0) :
    dirichletSineSeries x = Real.sin x / x := by
  have hs := (Real.hasSum_sin x).div_const x
  have hinternal := hasSum_dirichletSineSeriesTerm x
  apply HasSum.unique hinternal
  refine HasSum.congr_fun hs (fun j => ?_)
  unfold dirichletSineSeriesTerm
  have hfac : ((((2 * j + 1) ! : ℕ) : ℝ)) ≠ 0 := by positivity
  rw [show 2 * j + 1 = 2 * j + 1 by rfl, pow_succ]
  field_simp [hx, hfac]
  ring

/-- The internal series takes the normalized value one at the origin. -/
theorem dirichletSineSeries_zero : dirichletSineSeries 0 = 1 := by
  have h := hasSum_dirichletSineSeriesTerm 0
  have hsingle : HasSum (fun j : ℕ => if j = 0 then (1 : ℝ) else 0) 1 :=
    hasSum_ite_eq 0 1
  apply HasSum.unique h
  refine HasSum.congr_fun hsingle (fun j => ?_)
  exact (dirichletSineSeriesTerm_zero j).symm

end EnterpriseMath.Precision
