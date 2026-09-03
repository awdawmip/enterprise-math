import Mathlib

namespace EnterpriseMath.PrecisionPi.MajorizationGap

/-- Total sum of the source multiset in the `k → k+2m` Gamma comparison. -/
def sourceTotal (k m : ℝ) : ℝ :=
  m + (k - 1) / 2

/-- Total sum of the uniform target multiset. -/
def targetTotal (k m : ℝ) : ℝ :=
  (k + 2 * m - 1) / 2

/-- The two Gamma-parameter multisets have equal total sum. -/
theorem sourceTotal_eq_targetTotal (k m : ℝ) :
    sourceTotal k m = targetTotal k m := by
  simp [sourceTotal, targetTotal]
  ring

/-- Middle-range prefix gap for a prefix length `r=m+s`. -/
def middleGap (k m s : ℝ) : ℝ :=
  ((m + s) * (m + s + 1)) / (2 * (k + 2 * m)) -
    (s * (s + 1)) / (2 * k)

/-- Exact factored numerator of the middle-range prefix gap. -/
theorem middleGap_factorization
    {k m s : ℝ} (hk : k ≠ 0) (hK : k + 2 * m ≠ 0) :
    middleGap k m s =
      m * (k * (m + 1 + 2 * s) - 2 * s * (s + 1)) /
        (2 * k * (k + 2 * m)) := by
  field_simp [middleGap, hk, hK]
  ring

/-- The bracket in the factored numerator is strictly positive on the admissible range. -/
theorem middleBracket_pos
    {k m s : ℝ}
    (hk : 0 < k) (hm : 1 ≤ m) (hs : 0 ≤ s) (hsk : s < k) :
    0 < k * (m + 1 + 2 * s) - 2 * s * (s + 1) := by
  have hkm : 0 ≤ k * (m - 1) :=
    mul_nonneg hk.le (sub_nonneg.mpr hm)
  have hs1 : 0 < s + 1 := by linarith
  have hks : 0 < k - s := by linarith
  have hprod : 0 < 2 * (s + 1) * (k - s) := by positivity
  nlinarith

/-- Every middle-range proper prefix has strictly positive majorization gap. -/
theorem middleGap_pos
    {k m s : ℝ}
    (hk : 0 < k) (hm : 1 ≤ m) (hs : 0 ≤ s) (hsk : s < k) :
    0 < middleGap k m s := by
  have hK : 0 < k + 2 * m := by linarith
  rw [middleGap_factorization hk.ne' hK.ne']
  have hm0 : 0 < m := lt_of_lt_of_le zero_lt_one hm
  have hbr := middleBracket_pos hk hm hs hsk
  exact div_pos (mul_pos hm0 hbr) (by positivity)

/-- In the initial range, the source prefix of `r` ones exceeds the target prefix. -/
def initialGap (k m r : ℝ) : ℝ :=
  r * (r + 1) / (2 * (k + 2 * m))

/-- Initial-range proper prefix gaps are positive. -/
theorem initialGap_pos
    {k m r : ℝ}
    (hk : 0 < k) (hm : 0 < m) (hr : 0 < r) :
    0 < initialGap k m r := by
  simp [initialGap]
  positivity

/-- The middle gap at `s=0` agrees with the initial gap at `r=m`. -/
theorem middleGap_zero_eq_initialGap
    {k m : ℝ} (hk : k ≠ 0) (hK : k + 2 * m ≠ 0) :
    middleGap k m 0 = initialGap k m m := by
  field_simp [middleGap, initialGap, hk, hK]
  ring

end EnterpriseMath.PrecisionPi.MajorizationGap
