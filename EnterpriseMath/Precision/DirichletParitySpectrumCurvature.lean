import EnterpriseMath.Precision.DirichletSpectrumBridge
import EnterpriseMath.Precision.DirichletCurvature

namespace EnterpriseMath.Precision

open Polynomial

/--
WSR-L41: the ratio of the two actual finite parity-sector root products is `q/2`,
with `q=n+2`.
-/
theorem dirichletParityRoots_prod_ratio (n : ℕ) :
    (dirichletParityEvenPoly n).roots.prod /
        (dirichletParityOddPoly n).roots.prod =
      ((n + 2 : ℕ) : ℝ) / 2 := by
  rw [dirichletParityEvenPoly_roots_prod, dirichletParityOddPoly_roots_prod]

/--
The endpoint-corrected parity curvature is exactly the true parity-sector root-product
ratio times the two endpoint square roots.
-/
theorem dirichletParityEndpointCurvature_eq_rootProductRatio (n : ℕ) (z : ℝ) :
    dirichletParityEndpointCurvature (n + 2) z =
      ((dirichletParityEvenPoly n).roots.prod /
        (dirichletParityOddPoly n).roots.prod) *
          Real.sqrt z * Real.sqrt (4 - z) := by
  rw [dirichletParityRoots_prod_ratio]
  unfold dirichletParityEndpointCurvature
  push_cast
  ring

/-- An odd-parity spectral root is automatically a root of the full odd fine chain. -/
theorem dirichletParityOddPoly_root_fullContinuant (n : ℕ) (z : ℝ)
    (hz : (dirichletParityOddPoly n).eval z = 0) :
    dirichletContinuant z (2 * n + 3) = 0 := by
  have hfull : (dirichletSpectralPoly (2 * n + 3)).eval z = 0 := by
    rw [dirichletSpectralPoly_odd_factorization, eval_mul, hz, mul_zero]
  rw [dirichletSpectralPoly_eval] at hfull
  have hsign : ((-1 : ℝ) ^ (2 * n + 3)) ≠ 0 := by positivity
  exact (mul_eq_zero.mp hfull).resolve_left hsign

/--
WSR-L42: every non-midpoint odd-parity fine spectral root decimates to a root of the
coarse/even-parity spectral factor.
-/
theorem dirichletParityOddPoly_root_decimates_to_evenPoly (n : ℕ) (z : ℝ)
    (hz : (dirichletParityOddPoly n).eval z = 0)
    (hz2 : z ≠ 2) :
    (dirichletParityEvenPoly n).eval (spectralDecimation z) = 0 := by
  have hfine0 := dirichletParityOddPoly_root_fullContinuant n z hz
  have hfine : dirichletContinuant z (2 * (n + 1) + 1) = 0 := by
    convert hfine0 using 1 <;> omega
  have hcoarse := dirichletContinuant_root_decimation z (n + 1) hfine hz2
  unfold dirichletParityEvenPoly
  rw [dirichletSpectralPoly_eval, hcoarse, mul_zero]

/--
WSR-L43: a non-midpoint odd-parity fine mode has an exact target-free parity-curvature
collapse to one half of the normalized radius of its decimated coarse mode.

No root ordering is required here; choosing the smallest positive odd root later recovers
the fundamental-mode specialization of WSR-T08.
-/
theorem dirichletParityOddMode_curvature_collapse (n : ℕ) (z : ℝ)
    (hz : (dirichletParityOddPoly n).eval z = 0)
    (hz2 : z ≠ 2)
    (hz0 : 0 ≤ z) :
    dirichletParityEndpointCurvature (n + 2) z =
        dirichletCoarseRadius (n + 2) (spectralDecimation z) / 2 ∧
      (dirichletParityEvenPoly n).eval (spectralDecimation z) = 0 := by
  exact ⟨dirichletParityEndpointCurvature_collapse (n + 2) z hz0,
    dirichletParityOddPoly_root_decimates_to_evenPoly n z hz hz2⟩

end EnterpriseMath.Precision
