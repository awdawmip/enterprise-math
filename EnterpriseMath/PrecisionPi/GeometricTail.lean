import Mathlib

namespace EnterpriseMath.PrecisionPi.GeometricTail

/-- A finite tail beginning at index `N` and containing `r` terms. -/
def tailPartial (a : ℕ → ℝ) (N r : ℕ) : ℝ :=
  ∑ j in Finset.range r, a (N + j)

/-- Finite geometric comparison sum. -/
def geometricPartial (q : ℝ) (r : ℕ) : ℝ :=
  ∑ j in Finset.range r, q ^ j

/-- A one-step ratio bound implies a pointwise geometric bound. -/
theorem term_le_geometric
    {a : ℕ → ℝ} {N : ℕ} {q : ℝ}
    (hq : 0 ≤ q)
    (hratio : ∀ n : ℕ, N ≤ n → a (n + 1) ≤ q * a n) :
    ∀ j : ℕ, a (N + j) ≤ q ^ j * a N := by
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
      calc
        a (N + (j + 1)) = a ((N + j) + 1) := by congr 1 <;> omega
        _ ≤ q * a (N + j) := hratio (N + j) (by omega)
        _ ≤ q * (q ^ j * a N) := mul_le_mul_of_nonneg_left ih hq
        _ = q ^ (j + 1) * a N := by rw [pow_succ]; ring

/-- A finite tail is bounded by the corresponding weighted geometric sum. -/
theorem tailPartial_le_weighted_geometric
    {a : ℕ → ℝ} {N r : ℕ} {q : ℝ}
    (hq : 0 ≤ q)
    (hratio : ∀ n : ℕ, N ≤ n → a (n + 1) ≤ q * a n) :
    tailPartial a N r ≤ ∑ j in Finset.range r, q ^ j * a N := by
  apply Finset.sum_le_sum
  intro j hj
  exact term_le_geometric hq hratio j

/-- The weighted comparison sum factors through the finite geometric sum. -/
theorem weighted_geometric_eq
    (q A : ℝ) (r : ℕ) :
    (∑ j in Finset.range r, q ^ j * A) = geometricPartial q r * A := by
  simp [geometricPartial, Finset.sum_mul]

/-- Standard finite geometric tail bound in factored form. -/
theorem tailPartial_le_geometricPartial
    {a : ℕ → ℝ} {N r : ℕ} {q : ℝ}
    (hq : 0 ≤ q)
    (hratio : ∀ n : ℕ, N ≤ n → a (n + 1) ≤ q * a n) :
    tailPartial a N r ≤ geometricPartial q r * a N := by
  calc
    tailPartial a N r ≤ ∑ j in Finset.range r, q ^ j * a N :=
      tailPartial_le_weighted_geometric hq hratio
    _ = geometricPartial q r * a N := weighted_geometric_eq q (a N) r

/-- Add one term to the finite geometric sum. -/
theorem geometricPartial_succ (q : ℝ) (r : ℕ) :
    geometricPartial q (r + 1) = geometricPartial q r + q ^ r := by
  simp [geometricPartial, Finset.sum_range_succ]

/-- Division-free finite geometric-series identity. -/
theorem one_sub_mul_geometricPartial (q : ℝ) (r : ℕ) :
    (1 - q) * geometricPartial q r = 1 - q ^ r := by
  induction r with
  | zero => simp [geometricPartial]
  | succ r ih =>
      rw [geometricPartial_succ, mul_add, ih, pow_succ]
      ring

/-- Reciprocal gaps are exactly normalized inverse-period tails. -/
theorem reciprocal_gap_identity
    {S T : ℝ} (hS : S ≠ 0) (hT : T ≠ 0) :
    1 / S - 1 / T = (T - S) / (S * T) := by
  field_simp [hS, hT]
  ring

/-- A certified inverse-period tail gives a certified reciprocal-period error. -/
theorem reciprocal_gap_le
    {S T R : ℝ}
    (hS : 0 < S) (hT : 0 < T)
    (htail : T - S ≤ R) :
    1 / S - 1 / T ≤ R / (S * T) := by
  rw [reciprocal_gap_identity hS.ne' hT.ne']
  exact div_le_div_of_nonneg_right htail (mul_pos hS hT).le

end EnterpriseMath.PrecisionPi.GeometricTail
