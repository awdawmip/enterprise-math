import Mathlib

open scoped BigOperators

namespace EnterpriseMath.PrecisionPi.GeometricTailBound

/-- A one-step ratio bound propagates to every later term. -/
theorem term_le_geometric
    (term : ℕ → ℝ) (q : ℝ)
    (hq : 0 ≤ q)
    (hratio : ∀ n, term (n + 1) ≤ q * term n)
    (M j : ℕ) :
    term (M + 1 + j) ≤ q ^ j * term (M + 1) := by
  induction j with
  | zero => simp
  | succ j ih =>
      calc
        term (M + 1 + (j + 1)) = term ((M + 1 + j) + 1) := by omega
        _ ≤ q * term (M + 1 + j) := hratio (M + 1 + j)
        _ ≤ q * (q ^ j * term (M + 1)) :=
          mul_le_mul_of_nonneg_left ih hq
        _ = q ^ (j + 1) * term (M + 1) := by
          rw [pow_succ]
          ring

/-- Finite tails inherit the geometric majorant term by term. -/
theorem finite_tail_le_geometric_sum
    (term : ℕ → ℝ) (q : ℝ)
    (hq : 0 ≤ q)
    (hratio : ∀ n, term (n + 1) ≤ q * term n)
    (M N : ℕ) :
    (∑ j in Finset.range N, term (M + 1 + j)) ≤
      (∑ j in Finset.range N, q ^ j) * term (M + 1) := by
  calc
    (∑ j in Finset.range N, term (M + 1 + j)) ≤
        ∑ j in Finset.range N, q ^ j * term (M + 1) := by
      exact Finset.sum_le_sum fun j _ => term_le_geometric term q hq hratio M j
    _ = (∑ j in Finset.range N, q ^ j) * term (M + 1) := by
      rw [Finset.sum_mul]

/-- Exact finite geometric-sum identity in the normalization needed below. -/
theorem geom_sum_mul_one_sub (q : ℝ) (N : ℕ) :
    (∑ j in Finset.range N, q ^ j) * (1 - q) = 1 - q ^ N := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ]
      calc
        ((∑ j in Finset.range N, q ^ j) + q ^ N) * (1 - q) =
            (∑ j in Finset.range N, q ^ j) * (1 - q) + q ^ N * (1 - q) := by
          ring
        _ = (1 - q ^ N) + q ^ N * (1 - q) := by rw [ih]
        _ = 1 - q ^ (N + 1) := by
          rw [pow_succ]
          ring

/-- A nonnegative finite geometric sum is bounded by its infinite majorant. -/
theorem geom_sum_le_one_div
    (q : ℝ) (N : ℕ) (hq0 : 0 ≤ q) (hq1 : q < 1) :
    (∑ j in Finset.range N, q ^ j) ≤ 1 / (1 - q) := by
  apply (le_div_iff₀ (sub_pos.mpr hq1)).2
  rw [geom_sum_mul_one_sub]
  have hpow : 0 ≤ q ^ N := pow_nonneg hq0 N
  linarith

/--
Uniform ratio control gives the standard finite tail certificate
`tail ≤ first omitted term / (1-q)`.
-/
theorem finite_tail_le_first_div_one_sub
    (term : ℕ → ℝ) (q : ℝ)
    (hq0 : 0 ≤ q) (hq1 : q < 1)
    (hterm : ∀ n, 0 ≤ term n)
    (hratio : ∀ n, term (n + 1) ≤ q * term n)
    (M N : ℕ) :
    (∑ j in Finset.range N, term (M + 1 + j)) ≤
      term (M + 1) / (1 - q) := by
  calc
    (∑ j in Finset.range N, term (M + 1 + j)) ≤
        (∑ j in Finset.range N, q ^ j) * term (M + 1) :=
      finite_tail_le_geometric_sum term q hq0 hratio M N
    _ ≤ (1 / (1 - q)) * term (M + 1) := by
      exact mul_le_mul_of_nonneg_right
        (geom_sum_le_one_div q N hq0 hq1) (hterm (M + 1))
    _ = term (M + 1) / (1 - q) := by ring

end EnterpriseMath.PrecisionPi.GeometricTailBound
