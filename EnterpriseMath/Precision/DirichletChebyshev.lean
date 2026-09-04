import EnterpriseMath.Precision.SpectralPrecision
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Chebyshev.RootsExtrema

namespace EnterpriseMath.Precision

open Polynomial

/--
Finite effective compatibility bridge for the #1159 Dirichlet carrier.

The native continuant remains recurrence-defined.  This theorem is a downstream
classical readout: its value is the Chebyshev polynomial of the second kind at
`1 - z/2`.  No Chebyshev/trigonometric input is used by the native determinant,
decimation, or compact-error theorems.
-/
theorem dirichletContinuant_eq_chebyshevU (z : ℝ) (n : ℕ) :
    dirichletContinuant z n =
      (Polynomial.Chebyshev.U ℝ (n : ℤ)).eval (1 - z / 2) := by
  induction n using Nat.twoStepInduction with
  | zero =>
      simp [dirichletContinuant]
  | one =>
      simp [dirichletContinuant]
      ring
  | more n ih0 ih1 =>
      rw [dirichletContinuant]
      have h2 : ((n + 2 : ℕ) : ℤ) = (n : ℤ) + 2 := by omega
      have h1 : ((n + 1 : ℕ) : ℤ) = (n : ℤ) + 1 := by omega
      rw [h2, Polynomial.Chebyshev.U_add_two]
      simp only [eval_sub, eval_mul, eval_ofNat, eval_X]
      rw [← h1, ← ih1, ← ih0]
      ring

/-- Classical mode angle used only in the finite Chebyshev compatibility readout. -/
noncomputable def dirichletModeAngle (M k : ℕ) : ℝ :=
  (k : ℝ) * Real.pi / (M : ℝ)

/-- Classical one-indexed Dirichlet mode root used as a downstream finite readout. -/
noncomputable def dirichletModeRoot (M k : ℕ) : ℝ :=
  2 - 2 * Real.cos (dirichletModeAngle M k)

/-- Positive mode indices give positive angles. -/
theorem dirichletModeAngle_pos (M k : ℕ) (hM : 0 < M) (hk : 0 < k) :
    0 < dirichletModeAngle M k := by
  unfold dirichletModeAngle
  positivity

/-- Interior mode indices give angles strictly below `pi`. -/
theorem dirichletModeAngle_lt_pi (M k : ℕ) (hM : 0 < M) (hkM : k < M) :
    dirichletModeAngle M k < Real.pi := by
  unfold dirichletModeAngle
  have hMreal : 0 < (M : ℝ) := by exact_mod_cast hM
  have hkreal : (k : ℝ) < (M : ℝ) := by exact_mod_cast hkM
  apply (div_lt_iff₀ hMreal).2
  simpa [mul_comm] using mul_lt_mul_of_pos_right hkreal Real.pi_pos

/-- The physical mode angle lies in the open half-period. -/
theorem dirichletModeAngle_mem_Ioo (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    dirichletModeAngle M k ∈ Set.Ioo (0 : ℝ) Real.pi := by
  have hM : 0 < M := lt_trans hk hkM
  exact ⟨dirichletModeAngle_pos M k hM hk,
    dirichletModeAngle_lt_pi M k hM hkM⟩

/-- Every classical interior mode root is an exact root of the native finite continuant. -/
theorem dirichletContinuant_modeRoot_zero
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    dirichletContinuant (dirichletModeRoot M k) (M - 1) = 0 := by
  have hM : 0 < M := lt_trans hk hkM
  rw [dirichletContinuant_eq_chebyshevU]
  have harg :
      1 - dirichletModeRoot M k / 2 = Real.cos (dirichletModeAngle M k) := by
    unfold dirichletModeRoot
    ring
  rw [harg]
  have hθ := dirichletModeAngle_mem_Ioo M k hk hkM
  have hsin : Real.sin (dirichletModeAngle M k) ≠ 0 :=
    ne_of_gt (Real.sin_pos_of_mem_Ioo hθ)
  suffices
      (Polynomial.Chebyshev.U ℝ ((M - 1 : ℕ) : ℤ)).eval
          (Real.cos (dirichletModeAngle M k)) *
        Real.sin (dirichletModeAngle M k) = 0 by
    exact (mul_eq_zero_iff_right hsin).mp this
  rw [Polynomial.Chebyshev.U_real_cos]
  have hindex : ((M - 1 : ℕ) : ℤ) + 1 = (M : ℤ) := by omega
  have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hM)
  have hphase :
      ((((M - 1 : ℕ) : ℤ) + 1 : ℤ) : ℝ) * dirichletModeAngle M k =
        (k : ℝ) * Real.pi := by
    rw [hindex]
    push_cast
    unfold dirichletModeAngle
    field_simp [hM0]
  rw [hphase]
  exact Real.sin_nat_mul_pi k

/-- Interior finite Dirichlet mode roots are strictly positive. -/
theorem dirichletModeRoot_pos
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    0 < dirichletModeRoot M k := by
  have hθ := dirichletModeAngle_mem_Ioo M k hk hkM
  have h0mem : (0 : ℝ) ∈ Set.Icc 0 Real.pi := ⟨le_rfl, Real.pi_pos.le⟩
  have hθmem : dirichletModeAngle M k ∈ Set.Icc 0 Real.pi :=
    ⟨hθ.1.le, hθ.2.le⟩
  have hc : Real.cos (dirichletModeAngle M k) < Real.cos 0 :=
    Real.strictAntiOn_cos h0mem hθmem hθ.1
  unfold dirichletModeRoot
  simp only [Real.cos_zero] at hc
  linarith

/-- Interior finite Dirichlet mode roots lie strictly below the endpoint value four. -/
theorem dirichletModeRoot_lt_four
    (M k : ℕ) (hk : 0 < k) (hkM : k < M) :
    dirichletModeRoot M k < 4 := by
  have hθ := dirichletModeAngle_mem_Ioo M k hk hkM
  have hθmem : dirichletModeAngle M k ∈ Set.Icc 0 Real.pi :=
    ⟨hθ.1.le, hθ.2.le⟩
  have hpimem : Real.pi ∈ Set.Icc (0 : ℝ) Real.pi :=
    ⟨Real.pi_pos.le, le_rfl⟩
  have hc : Real.cos Real.pi < Real.cos (dirichletModeAngle M k) :=
    Real.strictAntiOn_cos hθmem hpimem hθ.2
  unfold dirichletModeRoot
  rw [Real.cos_pi] at hc
  linarith

/-- The one-indexed finite Dirichlet roots are strictly ordered by their mode index. -/
theorem dirichletModeRoot_strictMono
    (M k l : ℕ) (hk : 0 < k) (hkl : k < l) (hlM : l < M) :
    dirichletModeRoot M k < dirichletModeRoot M l := by
  have hM : 0 < M := lt_trans (lt_trans hk hkl) hlM
  have hkM : k < M := lt_trans hkl hlM
  have hl : 0 < l := lt_trans hk hkl
  have hθk := dirichletModeAngle_mem_Ioo M k hk hkM
  have hθl := dirichletModeAngle_mem_Ioo M l hl hlM
  have hMreal : 0 < (M : ℝ) := by exact_mod_cast hM
  have hklreal : (k : ℝ) < (l : ℝ) := by exact_mod_cast hkl
  have hangle : dirichletModeAngle M k < dirichletModeAngle M l := by
    unfold dirichletModeAngle
    apply (div_lt_div_iff_of_pos_right hMreal).2
    exact mul_lt_mul_of_pos_right hklreal Real.pi_pos
  have hkcc : dirichletModeAngle M k ∈ Set.Icc 0 Real.pi :=
    ⟨hθk.1.le, hθk.2.le⟩
  have hlcc : dirichletModeAngle M l ∈ Set.Icc 0 Real.pi :=
    ⟨hθl.1.le, hθl.2.le⟩
  have hc : Real.cos (dirichletModeAngle M l) <
      Real.cos (dirichletModeAngle M k) :=
    Real.strictAntiOn_cos hkcc hlcc hangle
  unfold dirichletModeRoot
  linarith

end EnterpriseMath.Precision
