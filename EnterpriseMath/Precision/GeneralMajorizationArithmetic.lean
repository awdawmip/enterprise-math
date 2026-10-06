import Mathlib

namespace EnterpriseMath.PrecisionPi.GeneralMajorizationArithmetic

/-- Algebraic decomposition of the middle-prefix majorization numerator. -/
theorem middleNumerator_decomposition
    {K : Type*} [CommRing K] (k m s : K) :
    m * (k * (m + 1 + 2 * s) - 2 * s * (s + 1)) =
      m * (k * (m + 1) + 2 * s * (k - 1 - s)) := by
  ring

/--
The nontrivial middle-prefix numerator in the general `k → k+2m`
majorization argument is strictly positive throughout the allowed range.
-/
theorem middleNumerator_pos
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {k m s : K}
    (hk : 0 < k) (hm : 0 < m)
    (hs0 : 0 ≤ s) (hsk : s ≤ k - 1) :
    0 < m * (k * (m + 1 + 2 * s) - 2 * s * (s + 1)) := by
  rw [middleNumerator_decomposition]
  have hm1 : 0 < m + 1 := by linarith
  have hbase : 0 < k * (m + 1) := mul_pos hk hm1
  have hgap : 0 ≤ k - 1 - s := by linarith
  have hcorr : 0 ≤ 2 * s * (k - 1 - s) := by positivity
  exact mul_pos hm (add_pos_of_pos_of_nonneg hbase hcorr)

/-- The same result in the integer parameter range used by the paper. -/
theorem middleNumerator_nat_pos
    (k m s : ℕ) (hk : 2 ≤ k) (hm : 1 ≤ m) (hs : s ≤ k - 1) :
    0 < (m : ℝ) *
      ((k : ℝ) * ((m : ℝ) + 1 + 2 * (s : ℝ)) -
        2 * (s : ℝ) * ((s : ℝ) + 1)) := by
  apply middleNumerator_pos
  · exact_mod_cast (show 0 < k by omega)
  · exact_mod_cast (show 0 < m by omega)
  · positivity
  · have hnat : s + 1 ≤ k := by omega
    have hreal : (s : ℝ) + 1 ≤ (k : ℝ) := by exact_mod_cast hnat
    linarith

/-- Exact rational middle-prefix difference formula. -/
def middlePrefixDifference (k m s : ℚ) : ℚ :=
  let r := m + s
  r * (r + 1) / (2 * (k + 2 * m)) - s * (s + 1) / (2 * k)

/-- Clearing denominators gives the positive numerator used above. -/
theorem middlePrefixDifference_clear_denominators
    (k m s : ℚ) (hk : k ≠ 0) (hkm : k + 2 * m ≠ 0) :
    middlePrefixDifference k m s * (2 * k * (k + 2 * m)) =
      m * (k * (m + 1 + 2 * s) - 2 * s * (s + 1)) := by
  have hkm' : k + m * 2 ≠ 0 := by
    simpa [mul_comm] using hkm
  unfold middlePrefixDifference
  dsimp only
  field_simp [hk, hkm, hkm']
  ring

/-- Positivity of the rational middle-prefix difference under positive denominators. -/
theorem middlePrefixDifference_pos
    {k m s : ℚ}
    (hk : 0 < k) (hm : 0 < m)
    (hs0 : 0 ≤ s) (hsk : s ≤ k - 1) :
    0 < middlePrefixDifference k m s := by
  have hnum :
      0 < m * (k * (m + 1 + 2 * s) - 2 * s * (s + 1)) :=
    middleNumerator_pos hk hm hs0 hsk
  have hkmPos : 0 < k + 2 * m := by positivity
  have hden : 0 < 2 * k * (k + 2 * m) := by positivity
  have hclear := middlePrefixDifference_clear_denominators
    k m s (ne_of_gt hk) (ne_of_gt hkmPos)
  nlinarith [hnum, hden, hclear]

end EnterpriseMath.PrecisionPi.GeneralMajorizationArithmetic
