import EnterpriseMath.Precision.SpectralPrecision

namespace EnterpriseMath.Precision

/--
WSR-L15: complement symmetry of the finite Dirichlet characteristic continuant.
The parameter involution `z ↦ 4-z` changes the sign of every odd-index continuant.
-/
theorem dirichletContinuant_four_sub (z : ℝ) (n : ℕ) :
    dirichletContinuant (4 - z) n = (-1 : ℝ) ^ n * dirichletContinuant z n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [dirichletContinuant]
  | one => simp [dirichletContinuant]
  | more n ih0 ih1 =>
      have hp1 : (-1 : ℝ) ^ (n + 1) = -((-1 : ℝ) ^ n) := by
        rw [pow_add]
        norm_num
      have hp2 : (-1 : ℝ) ^ (n + 2) = (-1 : ℝ) ^ n := by
        rw [pow_add]
        norm_num
      rw [dirichletContinuant, dirichletContinuant, ih0, ih1, hp1, hp2]
      ring

/--
WSR-L16: eliminating one parity of lattice sites gives a closed second-order
recurrence on every second continuant index.
-/
theorem dirichletContinuant_skip_two (z : ℝ) (k : ℕ) :
    dirichletContinuant z (k + 4) =
      (2 - spectralDecimation z) * dirichletContinuant z (k + 2) -
        dirichletContinuant z k := by
  have hk2 :
      dirichletContinuant z (k + 2) =
        (2 - z) * dirichletContinuant z (k + 1) - dirichletContinuant z k := by
    rw [dirichletContinuant]
  have hk3 :
      dirichletContinuant z (k + 3) =
        (2 - z) * dirichletContinuant z (k + 2) - dirichletContinuant z (k + 1) := by
    change dirichletContinuant z ((k + 1) + 2) = _
    rw [dirichletContinuant]
  have hk4 :
      dirichletContinuant z (k + 4) =
        (2 - z) * dirichletContinuant z (k + 3) - dirichletContinuant z (k + 2) := by
    change dirichletContinuant z ((k + 2) + 2) = _
    rw [dirichletContinuant]
  rw [hk4, hk3]
  unfold spectralDecimation
  linear_combination (norm := ring_nf) hk2

/--
WSR-L17: exact dyadic spectral decimation at the characteristic-polynomial level.
The odd-index fine continuant is the coarse continuant at `z(4-z)`, multiplied by
its first-step factor `2-z`.
-/
theorem dirichletContinuant_decimation (z : ℝ) (n : ℕ) :
    dirichletContinuant z (2 * n + 1) =
      (2 - z) * dirichletContinuant (spectralDecimation z) n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [dirichletContinuant]
  | one =>
      norm_num only [Nat.reduceMul, Nat.reduceAdd]
      simp [dirichletContinuant, spectralDecimation]
      ring
  | more n ih0 ih1 =>
      have hskip := dirichletContinuant_skip_two z (2 * n + 1)
      have hcoarse :
          dirichletContinuant (spectralDecimation z) (n + 2) =
            (2 - spectralDecimation z) *
                dirichletContinuant (spectralDecimation z) (n + 1) -
              dirichletContinuant (spectralDecimation z) n := by
        rw [dirichletContinuant]
      change dirichletContinuant z (2 * (n + 2) + 1) =
        (2 - z) * dirichletContinuant (spectralDecimation z) (n + 2)
      rw [show 2 * (n + 2) + 1 = (2 * n + 1) + 4 by omega]
      rw [hskip]
      rw [show (2 * n + 1) + 2 = 2 * (n + 1) + 1 by omega, ih1, ih0, hcoarse]
      ring

end EnterpriseMath.Precision
