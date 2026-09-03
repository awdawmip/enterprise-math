import Mathlib.Analysis.SpecialFunctions.Stirling

namespace EnterpriseMath.PrecisionPi

open Filter Topology

/-- The Stirling-normalized candidate for the general codimension-`2m`
multinomial precision approximant. -/
noncomputable def stirlingPrecision (k m n : ℕ) : ℝ :=
  Stirling.stirlingSeq (k * n) * Stirling.stirlingSeq n ^ (2 * m) /
    Stirling.stirlingSeq ((k + 2 * m) * n)

/-- For every nonempty base alphabet, adding `2m` balance dimensions produces
`π^m` as the common Stirling completion. -/
theorem tendsto_stirlingPrecision_pi_pow (k m : ℕ) (hk : 0 < k) :
    Tendsto (stirlingPrecision k m) atTop (𝓝 (Real.pi ^ m)) := by
  change Tendsto
    (fun n : ℕ =>
      Stirling.stirlingSeq (k * n) * Stirling.stirlingSeq n ^ (2 * m) /
        Stirling.stirlingSeq ((k + 2 * m) * n))
    atTop (𝓝 (Real.pi ^ m))
  have hkm : 0 < k + 2 * m := by
    omega
  have hS := Stirling.tendsto_stirlingSeq_sqrt_pi
  have hkS :
      Tendsto (fun n : ℕ => Stirling.stirlingSeq (k * n)) atTop
        (𝓝 (Real.sqrt Real.pi)) := by
    exact hS.comp (tendsto_id.const_mul_atTop' hk)
  have hkmS :
      Tendsto (fun n : ℕ => Stirling.stirlingSeq ((k + 2 * m) * n)) atTop
        (𝓝 (Real.sqrt Real.pi)) := by
    exact hS.comp (tendsto_id.const_mul_atTop' hkm)
  have hsqrt : Real.sqrt Real.pi ≠ 0 := by
    positivity
  have hratio :
      Tendsto
        (fun n : ℕ =>
          Stirling.stirlingSeq (k * n) * Stirling.stirlingSeq n ^ (2 * m) /
            Stirling.stirlingSeq ((k + 2 * m) * n))
        atTop
        (𝓝 (Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ (2 * m) /
          Real.sqrt Real.pi)) :=
    (hkS.mul (hS.pow (2 * m))).div hkmS hsqrt
  have hlim :
      Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ (2 * m) /
          Real.sqrt Real.pi = Real.pi ^ m := by
    calc
      Real.sqrt Real.pi * (Real.sqrt Real.pi) ^ (2 * m) /
          Real.sqrt Real.pi = (Real.sqrt Real.pi) ^ (2 * m) := by
            field_simp [hsqrt]
      _ = ((Real.sqrt Real.pi) ^ 2) ^ m := by
            rw [pow_mul]
      _ = Real.pi ^ m := by
            rw [Real.sq_sqrt (le_of_lt Real.pi_pos)]
  simpa [hlim] using hratio

end EnterpriseMath.PrecisionPi
