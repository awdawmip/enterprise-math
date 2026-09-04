import EnterpriseMath.Precision.DirichletExplicitSpectrum
import EnterpriseMath.Precision.DirichletCurvature
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

namespace EnterpriseMath.Precision

/-- Exact half-angle readout of the positive square root of an interior Dirichlet mode root. -/
theorem sqrt_dirichletModeRoot_eq_two_mul_sin_half
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    Real.sqrt (dirichletModeRoot M k) =
      2 * Real.sin (dirichletModeAngle M k / 2) := by
  have hθ := dirichletModeAngle_mem_Ioo M k hk hkM
  have hθle : dirichletModeAngle M k ≤ 2 * Real.pi := by
    linarith [hθ.2, Real.pi_pos]
  have hs := Real.sin_half_eq_sqrt hθ.1.le hθle
  have hform :
      dirichletModeRoot M k =
        4 * ((1 - Real.cos (dirichletModeAngle M k)) / 2) := by
    unfold dirichletModeRoot
    ring
  calc
    Real.sqrt (dirichletModeRoot M k) =
        Real.sqrt (4 * ((1 - Real.cos (dirichletModeAngle M k)) / 2)) := by
      rw [hform]
    _ = Real.sqrt 4 *
        Real.sqrt ((1 - Real.cos (dirichletModeAngle M k)) / 2) := by
      rw [Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 4)]
    _ = 2 * Real.sqrt ((1 - Real.cos (dirichletModeAngle M k)) / 2) := by
      norm_num
    _ = 2 * Real.sin (dirichletModeAngle M k / 2) := by
      rw [← hs]

/-- Exact classical half-angle readout of the existing coarse radius observable. -/
theorem dirichletModeRadius_eq_two_mul_sin_half
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    dirichletCoarseRadius M (dirichletModeRoot M k) =
      2 * (M : ℝ) * Real.sin (dirichletModeAngle M k / 2) := by
  unfold dirichletCoarseRadius
  rw [sqrt_dirichletModeRoot_eq_two_mul_sin_half M k hk hkM]
  ring

/-- Every interior finite mode radius is strictly larger than its linear lower model `2k`. -/
theorem two_mul_mode_lt_dirichletModeRadius
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    2 * (k : ℝ) < dirichletCoarseRadius M (dirichletModeRoot M k) := by
  have hM : 0 < M := lt_trans hk hkM
  have hθ := dirichletModeAngle_mem_Ioo M k hk hkM
  have hhalf0 : 0 < dirichletModeAngle M k / 2 := by linarith
  have hhalfpi : dirichletModeAngle M k / 2 < Real.pi / 2 := by linarith
  have hs := Real.mul_lt_sin hhalf0 hhalfpi
  have hMreal : 0 < (M : ℝ) := by exact_mod_cast hM
  have hM0 : (M : ℝ) ≠ 0 := ne_of_gt hMreal
  have hpi0 : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hscale : 0 < 2 * (M : ℝ) := by positivity
  have hscaled := mul_lt_mul_of_pos_left hs hscale
  have hleft :
      (2 * (M : ℝ)) *
          (2 / Real.pi * (dirichletModeAngle M k / 2)) =
        2 * (k : ℝ) := by
    unfold dirichletModeAngle
    field_simp [hM0, hpi0]
  calc
    2 * (k : ℝ) =
        (2 * (M : ℝ)) *
          (2 / Real.pi * (dirichletModeAngle M k / 2)) := hleft.symm
    _ < (2 * (M : ℝ)) * Real.sin (dirichletModeAngle M k / 2) := hscaled
    _ = dirichletCoarseRadius M (dirichletModeRoot M k) :=
      (dirichletModeRadius_eq_two_mul_sin_half M k hk hkM).symm

/-- Weak form used by the WSR-T04 finite tail certificate. -/
theorem two_mul_mode_le_dirichletModeRadius
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    2 * (k : ℝ) ≤ dirichletCoarseRadius M (dirichletModeRoot M k) :=
  (two_mul_mode_lt_dirichletModeRadius M k hk hkM).le

end EnterpriseMath.Precision
