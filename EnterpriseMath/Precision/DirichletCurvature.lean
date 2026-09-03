import EnterpriseMath.Precision.DirichletDecimation

namespace EnterpriseMath.Precision

/-- WSR-L22: every finite Dirichlet continuant root is paired by `z ↦ 4-z`. -/
theorem dirichletContinuant_root_four_sub {z : ℝ} {n : ℕ}
    (hz : dirichletContinuant z n = 0) :
    dirichletContinuant (4 - z) n = 0 := by
  rw [dirichletContinuant_four_sub, hz, mul_zero]

/-- The spectral decimation polynomial is invariant under the endpoint complement involution. -/
theorem spectralDecimation_four_sub (z : ℝ) :
    spectralDecimation (4 - z) = spectralDecimation z := by
  unfold spectralDecimation
  ring

/--
WSR-L23: a non-midpoint root of an odd fine Dirichlet continuant decimates to
an exact root of the coarse continuant.
-/
theorem dirichletContinuant_root_decimation (z : ℝ) (n : ℕ)
    (hz : dirichletContinuant z (2 * n + 1) = 0)
    (hz2 : z ≠ 2) :
    dirichletContinuant (spectralDecimation z) n = 0 := by
  have hdec := dirichletContinuant_decimation z n
  rw [hz] at hdec
  have hmul :
      (2 - z) * dirichletContinuant (spectralDecimation z) n = 0 := hdec.symm
  have hfactor : 2 - z ≠ 0 := by
    intro hzero
    apply hz2
    linarith
  rcases mul_eq_zero.mp hmul with hzero | hroot
  · exact (hfactor hzero).elim
  · exact hroot

/-- The endpoint square-root correction is exactly the square root of the decimated value. -/
theorem sqrt_endpoint_product_eq_sqrt_decimation (z : ℝ)
    (hz0 : 0 ≤ z) :
    Real.sqrt z * Real.sqrt (4 - z) = Real.sqrt (spectralDecimation z) := by
  rw [← Real.sqrt_mul hz0]
  unfold spectralDecimation
  rfl

/-- Coarse normalized mode radius at scale `q`. -/
def dirichletCoarseRadius (q : ℕ) (u : ℝ) : ℝ :=
  (q : ℝ) * Real.sqrt u

/--
The parity-product ratio `q/2`, corrected by the two endpoint square roots.
Once the parity factors are identified with the even/odd spectral products,
this is exactly the #1159 full-spectrum curvature observer.
-/
def dirichletParityEndpointCurvature (q : ℕ) (z : ℝ) : ℝ :=
  ((q : ℝ) / 2) * Real.sqrt z * Real.sqrt (4 - z)

/--
WSR-L24: endpoint complement plus spectral decimation collapses the parity
curvature kernel to one half of the coarse normalized mode radius.
-/
theorem dirichletParityEndpointCurvature_collapse (q : ℕ) (z : ℝ)
    (hz0 : 0 ≤ z) :
    dirichletParityEndpointCurvature q z =
      dirichletCoarseRadius q (spectralDecimation z) / 2 := by
  unfold dirichletParityEndpointCurvature dirichletCoarseRadius
  rw [sqrt_endpoint_product_eq_sqrt_decimation z hz0]
  ring

end EnterpriseMath.Precision
