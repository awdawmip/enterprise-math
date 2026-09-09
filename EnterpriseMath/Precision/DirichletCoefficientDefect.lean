import EnterpriseMath.Precision.DirichletFiniteSine
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset

namespace EnterpriseMath.Precision

open scoped BigOperators Nat

/-- The `r`-th normalized quadratic defect appearing in the finite Dirichlet sine carrier. -/
noncomputable def dirichletUnitDefect (M r : ℕ) : ℝ :=
  (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2

/-- Every normalized quadratic defect is nonnegative. -/
theorem dirichletUnitDefect_nonneg (M r : ℕ) :
    0 ≤ dirichletUnitDefect M r := by
  unfold dirichletUnitDefect
  positivity

/-- Inside the physical coefficient range `r < j < M`, every defect is strictly below one. -/
theorem dirichletUnitDefect_lt_one (M j r : ℕ) (hj : j < M) (hr : r < j) :
    dirichletUnitDefect M r < 1 := by
  have hrMnat : r + 1 < M := by omega
  have hrM : (((r + 1 : ℕ) : ℝ)) < (M : ℝ) := by exact_mod_cast hrMnat
  have hMpos : 0 < (M : ℝ) := by
    exact_mod_cast (show 0 < M by omega)
  have hsum : 0 < (M : ℝ) + (((r + 1 : ℕ) : ℝ)) := by positivity
  have hprod :
      0 < ((M : ℝ) - (((r + 1 : ℕ) : ℝ))) *
        ((M : ℝ) + (((r + 1 : ℕ) : ℝ))) :=
    mul_pos (sub_pos.mpr hrM) hsum
  have hsquare :
      (((r + 1 : ℕ) : ℝ) ^ 2) < (M : ℝ) ^ 2 := by
    nlinarith
  have hden : 0 < (M : ℝ) ^ 2 := by positivity
  unfold dirichletUnitDefect
  exact (div_lt_one₀ hden).2 hsquare

/-- The finite unit factor `1-d_r` is nonnegative in the physical coefficient range. -/
theorem dirichletUnitFactor_nonneg (M j r : ℕ) (hj : j < M) (hr : r < j) :
    0 ≤ 1 - dirichletUnitDefect M r := by
  linarith [dirichletUnitDefect_lt_one M j r hj hr]

/-- The finite unit factor `1-d_r` never exceeds one. -/
theorem dirichletUnitFactor_le_one (M r : ℕ) :
    1 - dirichletUnitDefect M r ≤ 1 := by
  linarith [dirichletUnitDefect_nonneg M r]

/-- The physical finite unit-defect product is nonnegative. -/
theorem dirichletUnitDefectProduct_nonneg (M j : ℕ) (hj : j < M) :
    0 ≤ ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) := by
  apply Finset.prod_nonneg
  intro r hr
  exact dirichletUnitFactor_nonneg M j r hj (Finset.mem_range.mp hr)

/-- The physical finite unit-defect product is at most one. -/
theorem dirichletUnitDefectProduct_le_one (M j : ℕ) (hj : j < M) :
    (∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r)) ≤ 1 := by
  apply Finset.prod_le_one
  · intro r hr
    exact dirichletUnitFactor_nonneg M j r hj (Finset.mem_range.mp hr)
  · intro r _hr
    exact dirichletUnitFactor_le_one M r

/-- Hence the coefficient defect `1-Π(1-d_r)` is nonnegative. -/
theorem one_sub_dirichletUnitDefectProduct_nonneg (M j : ℕ) (hj : j < M) :
    0 ≤ 1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) := by
  exact sub_nonneg.mpr (dirichletUnitDefectProduct_le_one M j hj)

/--
Finite union-bound form of the coefficient defect:
`1 - Π(1-d_r) ≤ Σ d_r`.
-/
theorem one_sub_dirichletUnitDefectProduct_le_sum (M j : ℕ) (hj : j < M) :
    1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) ≤
      ∑ r ∈ Finset.range j, dirichletUnitDefect M r := by
  rw [Finset.prod_one_sub_ordered]
  simp only [sub_sub_cancel]
  apply Finset.sum_le_sum
  intro r hr
  have hrj : r < j := Finset.mem_range.mp hr
  have hprefix :
      (∏ s ∈ Finset.range j with s < r,
        (1 - dirichletUnitDefect M s)) ≤ 1 := by
    apply Finset.prod_le_one
    · intro s hs
      have hsrange : s ∈ Finset.range j := (Finset.mem_filter.mp hs).1
      exact dirichletUnitFactor_nonneg M j s hj (Finset.mem_range.mp hsrange)
    · intro s _hs
      exact dirichletUnitFactor_le_one M s
  exact mul_le_of_le_one_right (dirichletUnitDefect_nonneg M r) hprefix

/-- Exact closed form for the sum of the first `j` normalized quadratic defects. -/
theorem sum_dirichletUnitDefect_eq (M j : ℕ) (hM : 0 < M) :
    (∑ r ∈ Finset.range j, dirichletUnitDefect M r) =
      (j : ℝ) * ((j : ℝ) + 1) * (2 * (j : ℝ) + 1) /
        (6 * (M : ℝ) ^ 2) := by
  have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hM)
  induction j with
  | zero => simp [dirichletUnitDefect]
  | succ j ih =>
      rw [Finset.sum_range_succ, ih]
      unfold dirichletUnitDefect
      push_cast
      field_simp [hM0]
      ring

/--
WSR-T02 finite coefficient kernel: the exact normalized product defect is bounded by
`j(j+1)(2j+1)/(6M^2)`.
-/
theorem dirichletUnitDefectProduct_error_le_closed
    (M j : ℕ) (hj : j < M) :
    1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) ≤
      (j : ℝ) * ((j : ℝ) + 1) * (2 * (j : ℝ) + 1) /
        (6 * (M : ℝ) ^ 2) := by
  have hM : 0 < M := by omega
  calc
    1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) ≤
        ∑ r ∈ Finset.range j, dirichletUnitDefect M r :=
      one_sub_dirichletUnitDefectProduct_le_sum M j hj
    _ = _ := sum_dirichletUnitDefect_eq M j hM

/-- Two-sided finite coefficient-defect certificate. -/
theorem dirichletUnitDefectProduct_error_bounds
    (M j : ℕ) (hj : j < M) :
    0 ≤ 1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) ∧
    1 - ∏ r ∈ Finset.range j, (1 - dirichletUnitDefect M r) ≤
      (j : ℝ) * ((j : ℝ) + 1) * (2 * (j : ℝ) + 1) /
        (6 * (M : ℝ) ^ 2) := by
  exact ⟨one_sub_dirichletUnitDefectProduct_nonneg M j hj,
    dirichletUnitDefectProduct_error_le_closed M j hj⟩

end EnterpriseMath.Precision
