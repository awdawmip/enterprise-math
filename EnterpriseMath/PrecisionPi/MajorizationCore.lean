import Mathlib

namespace EnterpriseMath.PrecisionPi.MajorizationCore

/-- Prefix sum of the decreasing list
`(K-1)/K, (K-2)/K, ..., 1/K`. -/
def uniformPrefix (K r : ℕ) : ℚ :=
  (r : ℚ) - (r : ℚ) * (r + 1 : ℚ) / (2 * K)

/-- Closed form for the prefix sum of the first `r` descending fractions. -/
theorem uniformPrefix_eq_sum (K r : ℕ) :
    uniformPrefix K r = ∑ j ∈ Finset.Icc 1 r, ((K - j : ℕ) : ℚ) / K := by
  by_cases hK : K = 0
  · subst K
    simp [uniformPrefix]
  · have hKq : (K : ℚ) ≠ 0 := by exact_mod_cast hK
    rw [uniformPrefix]
    rw [Finset.sum_div]
    have hcard : (Finset.Icc 1 r).card = r := by simp
    have hsum : ∑ j ∈ Finset.Icc 1 r, (j : ℚ) = (r : ℚ) * (r + 1) / 2 := by
      rw [show Finset.Icc 1 r = Finset.Icc 0 r \ {0} by ext j; simp]
      simp [Finset.sum_Icc_eq_sum_range]
      ring
    simp_rw [Nat.cast_sub (by omega : ∀ j ∈ Finset.Icc 1 r, j ≤ K)]
    rw [Finset.sum_sub_distrib]
    simp [hcard, hsum]
    field_simp
    ring

/-- Total mass of the majorizing multiset with `m` ones, the `k-1`
fractions `(k-1)/k,...,1/k`, and `m` zeros. -/
def majorizingTotal (k m : ℕ) : ℚ :=
  (m : ℚ) + (k - 1 : ℚ) / 2

/-- Both multisets in the precision-pi Gamma ratio have the same total sum. -/
theorem equal_total (k m : ℕ) (hk : 1 ≤ k) :
    majorizingTotal k m = ((k + 2 * m - 1 : ℕ) : ℚ) / 2 := by
  have hk' : 1 ≤ k + 2 * m := by omega
  simp [majorizingTotal, Nat.cast_sub hk, Nat.cast_sub hk']
  ring

/-- In the initial block of `m` unit entries, the prefix-sum gap is positive. -/
theorem initialPrefixGap_pos {k m r : ℕ}
    (hr : 1 ≤ r) :
    0 < (r : ℚ) - uniformPrefix (k + 2 * m) r := by
  unfold uniformPrefix
  have hden : (0 : ℚ) < 2 * (k + 2 * m) := by positivity
  rw [sub_sub_cancel_left]
  positivity

/-- Exact middle-block prefix gap.  Here `r=m+s`. -/
theorem middlePrefixGap_eq (k m s : ℕ) :
    ((m + s : ℕ) : ℚ) - (s : ℚ) * (s + 1 : ℚ) / (2 * k) -
        uniformPrefix (k + 2 * m) (m + s) =
      (m : ℚ) *
          ((k : ℚ) * ((m : ℚ) + 1 + 2 * s) -
            2 * s * (s + 1)) /
        (2 * k * (k + 2 * m)) := by
  unfold uniformPrefix
  ring

/-- The middle-block prefix gap is strictly positive.  This is the central
finite inequality in the majorization proof for the `π^m` approximants. -/
theorem middlePrefixGap_pos {k m s : ℕ}
    (hk : 1 ≤ k) (hm : 1 ≤ m) (hs : s + 1 ≤ k) :
    0 < ((m + s : ℕ) : ℚ) -
        (s : ℚ) * (s + 1 : ℚ) / (2 * k) -
          uniformPrefix (k + 2 * m) (m + s) := by
  rw [middlePrefixGap_eq]
  have hkq : (0 : ℚ) < k := by exact_mod_cast (show 0 < k by omega)
  have hmq : (0 : ℚ) < m := by exact_mod_cast (show 0 < m by omega)
  have hsq : (s : ℚ) + 1 ≤ k := by exact_mod_cast hs
  have hnonneg :
      0 ≤ 2 * (s : ℚ) * ((k : ℚ) - s - 1) := by positivity
  have hbracket :
      0 < (k : ℚ) * ((m : ℚ) + 1 + 2 * s) - 2 * s * (s + 1) := by
    calc
      (k : ℚ) * ((m : ℚ) + 1 + 2 * s) - 2 * s * (s + 1) =
          (k : ℚ) * ((m : ℚ) + 1) +
            2 * s * ((k : ℚ) - s - 1) := by ring
      _ > 0 := by positivity
  positivity

/-- The final block is controlled by the omitted tail of the uniform list. -/
theorem finalPrefixGap_eq {K r q : ℕ}
    (h : r + q + 1 = K) :
    ((K - 1 : ℕ) : ℚ) / 2 - uniformPrefix K r =
      (q : ℚ) * (q + 1 : ℚ) / (2 * K) := by
  have hK : 1 ≤ K := by omega
  have hq : (K : ℚ) = r + q + 1 := by exact_mod_cast h.symm
  unfold uniformPrefix
  rw [Nat.cast_sub hK, hq]
  ring

/-- Every proper final-block prefix has a strictly positive gap. -/
theorem finalPrefixGap_pos {K r q : ℕ}
    (h : r + q + 1 = K) (hq : 1 ≤ q) :
    0 < ((K - 1 : ℕ) : ℚ) / 2 - uniformPrefix K r := by
  rw [finalPrefixGap_eq h]
  have hK : (0 : ℚ) < K := by exact_mod_cast (show 0 < K by omega)
  have hq' : (0 : ℚ) < q := by exact_mod_cast (show 0 < q by omega)
  positivity

end EnterpriseMath.PrecisionPi.MajorizationCore
