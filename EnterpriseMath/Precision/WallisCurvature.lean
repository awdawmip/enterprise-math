import EnterpriseMath.Precision.WallisPrecision

namespace EnterpriseMath.Precision

open scoped BigOperators

/-- The local multiplicative curvature of the integer mode ladder at the `r`-th Wallis cell. -/
def integerModeCurvatureStep (r : ℕ) : ℚ :=
  ((2 * ((r : ℚ) + 1)) ^ 2) /
    ((2 * (r : ℚ) + 1) * (2 * (r : ℚ) + 3))

/-- The integer-mode curvature cell is exactly the corresponding Wallis refinement factor. -/
theorem integerModeCurvatureStep_eq_wallisStep (r : ℕ) :
    integerModeCurvatureStep r = wallisStep r := by
  unfold integerModeCurvatureStep wallisStep
  congr 1
  ring

/-- Product of the first `n` local multiplicative curvatures of the integer mode ladder. -/
def integerParityCurvature (n : ℕ) : ℚ :=
  ∏ r ∈ Finset.range n, integerModeCurvatureStep r

/-- WSR-L28 / WSR-T07: integer-mode parity curvature is exactly the Wallis partial product. -/
theorem integerParityCurvature_eq_wallisPartial (n : ℕ) :
    integerParityCurvature n = wallisPartial n := by
  induction n with
  | zero => simp [integerParityCurvature, wallisPartial]
  | succ n ih =>
      rw [integerParityCurvature, Finset.prod_range_succ, wallisPartial]
      rw [← integerParityCurvature, ih, integerModeCurvatureStep_eq_wallisStep]

end EnterpriseMath.Precision
