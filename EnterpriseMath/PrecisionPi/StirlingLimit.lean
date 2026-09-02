import Mathlib.Analysis.SpecialFunctions.Stirling

namespace EnterpriseMath.PrecisionPi

open Filter Topology

/-- Stirling-normalized form of the tetrahedral precision sequence.  A later
bridge theorem identifies this expression pointwise with the multinomial
`4 -> 6` precision approximant for positive depth. -/
noncomputable def tetrahedralStirlingPrecision (n : ℕ) : ℝ :=
  Stirling.stirlingSeq (4 * n) * Stirling.stirlingSeq n ^ 2 /
    Stirling.stirlingSeq (6 * n)

/-- The Stirling-normalized tetrahedral precision sequence converges to `π`. -/
theorem tendsto_tetrahedralStirlingPrecision_pi :
    Tendsto tetrahedralStirlingPrecision atTop (𝓝 Real.pi) := by
  change Tendsto
    (fun n : ℕ =>
      Stirling.stirlingSeq (4 * n) * Stirling.stirlingSeq n ^ 2 /
        Stirling.stirlingSeq (6 * n))
    atTop (𝓝 Real.pi)
  have hS := Stirling.tendsto_stirlingSeq_sqrt_pi
  have h4 :
      Tendsto (fun n : ℕ => Stirling.stirlingSeq (4 * n)) atTop
        (𝓝 (Real.sqrt Real.pi)) := by
    exact hS.comp (tendsto_id.const_mul_atTop' (by norm_num : 0 < (4 : ℕ)))
  have h6 :
      Tendsto (fun n : ℕ => Stirling.stirlingSeq (6 * n)) atTop
        (𝓝 (Real.sqrt Real.pi)) := by
    exact hS.comp (tendsto_id.const_mul_atTop' (by norm_num : 0 < (6 : ℕ)))
  have hsqrt : Real.sqrt Real.pi ≠ 0 := by
    positivity
  have hratio :
      Tendsto
        (fun n : ℕ =>
          Stirling.stirlingSeq (4 * n) * Stirling.stirlingSeq n ^ 2 /
            Stirling.stirlingSeq (6 * n))
        atTop
        (𝓝 (Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ 2 /
          Real.sqrt Real.pi)) :=
    (h4.mul (hS.pow 2)).div h6 hsqrt
  have hlim :
      Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ 2 / Real.sqrt Real.pi =
        Real.pi := by
    calc
      Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ 2 / Real.sqrt Real.pi =
          (Real.sqrt Real.pi) ^ 2 := by
            field_simp [hsqrt]
      _ = Real.pi := Real.sq_sqrt (le_of_lt Real.pi_pos)
  simpa [hlim] using hratio

end EnterpriseMath.PrecisionPi
