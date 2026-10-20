import Mathlib

namespace EnterpriseMath.PrecisionPi.MajorizationCore

/-- Closed form for the prefix sum of the decreasing rational list
`(K-1)/K, (K-2)/K, ..., 1/K`.  The intended range is `r ≤ K`. -/
def uniformPrefix (K r : ℕ) : ℚ :=
  (r : ℚ) - (r : ℚ) * (r + 1 : ℚ) / (2 * K)

/-- The gap between the unit prefix and the uniform prefix is its triangular
correction term.  This identity is purely additive and needs no denominator
cancellation. -/
theorem unitPrefix_sub_uniformPrefix (K r : ℕ) :
    (r : ℚ) - uniformPrefix K r =
      (r : ℚ) * (r + 1 : ℚ) / (2 * K) := by
  unfold uniformPrefix
  ring

/-- Total mass of the majorizing multiset with `m` ones, the `k-1`
fractions `(k-1)/k,...,1/k`, and `m` zeros. -/
def majorizingTotal (k m : ℕ) : ℚ :=
  (m : ℚ) + (k - 1 : ℚ) / 2

/-- Both multisets in the precision-pi Gamma ratio have the same total sum. -/
theorem equal_total (k m : ℕ) (hk : 1 ≤ k) :
    majorizingTotal k m = ((k + 2 * m - 1 : ℕ) : ℚ) / 2 := by
  have hk' : 1 ≤ k + 2 * m := by omega
  simp [majorizingTotal, Nat.cast_sub hk']
  ring

/-- In the initial block of unit entries, every nonempty prefix has a strictly
positive gap over the comparison uniform list. -/
theorem initialPrefixGap_pos {k m r : ℕ}
    (hK : 0 < k + 2 * m) (hr : 0 < r) :
    0 < (r : ℚ) - uniformPrefix (k + 2 * m) r := by
  rw [unitPrefix_sub_uniformPrefix]
  have hKq : (0 : ℚ) < k + 2 * m := by exact_mod_cast hK
  have hrq : (0 : ℚ) < r := by exact_mod_cast hr
  positivity

/-- Exact middle-block prefix gap.  Here the prefix length is `m+s`.
The positive-base hypothesis is exactly what is required to clear the two
rational denominators. -/
theorem middlePrefixGap_eq {k m s : ℕ} (hk : 0 < k) :
    ((m + s : ℕ) : ℚ) - (s : ℚ) * (s + 1 : ℚ) / (2 * k) -
        uniformPrefix (k + 2 * m) (m + s) =
      (m : ℚ) *
          ((k : ℚ) * ((m : ℚ) + 1 + 2 * s) -
            2 * s * (s + 1)) /
        (2 * k * (k + 2 * m)) := by
  have hkq : (k : ℚ) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hk)
  have hkmq : ((k + 2 * m : ℕ) : ℚ) ≠ 0 := by
    exact_mod_cast (show k + 2 * m ≠ 0 by omega)
  unfold uniformPrefix
  push_cast
  field_simp [hkq, hkmq]
  ring

/-- The middle-block prefix gap is strictly positive.  This is the central
finite inequality in the majorization proof for the `π^m` approximants. -/
theorem middlePrefixGap_pos {k m s : ℕ}
    (hk : 1 ≤ k) (hm : 1 ≤ m) (hs : s + 1 ≤ k) :
    0 < ((m + s : ℕ) : ℚ) -
        (s : ℚ) * (s + 1 : ℚ) / (2 * k) -
          uniformPrefix (k + 2 * m) (m + s) := by
  rw [middlePrefixGap_eq (show 0 < k by omega)]
  have hkq : (0 : ℚ) < k := by exact_mod_cast (show 0 < k by omega)
  have hmq : (0 : ℚ) < m := by exact_mod_cast (show 0 < m by omega)
  have hsq : (s : ℚ) + 1 ≤ k := by exact_mod_cast hs
  have htail : 0 ≤ (k : ℚ) - s - 1 := by linarith
  have hnonneg :
      0 ≤ 2 * (s : ℚ) * ((k : ℚ) - s - 1) := by positivity
  have hbracket :
      0 < (k : ℚ) * ((m : ℚ) + 1 + 2 * s) - 2 * s * (s + 1) := by
    calc
      (k : ℚ) * ((m : ℚ) + 1 + 2 * s) - 2 * s * (s + 1) =
          (k : ℚ) * ((m : ℚ) + 1) +
            2 * s * ((k : ℚ) - s - 1) := by ring
      _ > 0 := by positivity
  have hden : (0 : ℚ) < 2 * k * (k + 2 * m) := by positivity
  positivity

/-- The final block is controlled by the omitted tail of the uniform list. -/
theorem finalPrefixGap_eq {K r q : ℕ}
    (h : r + q + 1 = K) :
    ((K - 1 : ℕ) : ℚ) / 2 - uniformPrefix K r =
      (q : ℚ) * (q + 1 : ℚ) / (2 * K) := by
  subst K
  have hsub : r + q + 1 - 1 = r + q := by omega
  rw [hsub]
  unfold uniformPrefix
  push_cast
  have hden : (0 : ℚ) < (r : ℚ) + q + 1 := by positivity
  field_simp [ne_of_gt hden]
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
