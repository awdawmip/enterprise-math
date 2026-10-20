import Mathlib

namespace EnterpriseMath.PrecisionPi.MajorizationCore

/-- Prefix sum of the decreasing rational list
`(K-1)/K, (K-2)/K, ..., 1/K`, written in closed form. -/
def uniformPrefix (K r : ℕ) : ℚ :=
  (r : ℚ) - (r : ℚ) * ((r : ℚ) + 1) / (2 * (K : ℚ))

/-- Total mass of the comparison multiset with `m` ones, the `k-1`
fractions `(k-1)/k,...,1/k`, and `m` zeros. -/
def majorizingTotal (k m : ℕ) : ℚ :=
  (m : ℚ) + ((k : ℚ) - 1) / 2

/-- Both comparison multisets have the same total mass. -/
theorem equal_total (k m : ℕ) :
    majorizingTotal k m = ((k : ℚ) + 2 * (m : ℚ) - 1) / 2 := by
  simp [majorizingTotal]
  ring

/-- In the initial unit block, the prefix gap has this exact form. -/
theorem initialPrefixGap_eq (K r : ℕ) :
    (r : ℚ) - uniformPrefix K r =
      (r : ℚ) * ((r : ℚ) + 1) / (2 * (K : ℚ)) := by
  simp [uniformPrefix]

/-- Every nonempty initial-block prefix has strictly positive gap. -/
theorem initialPrefixGap_pos {K r : ℕ}
    (hK : 1 ≤ K) (hr : 1 ≤ r) :
    0 < (r : ℚ) - uniformPrefix K r := by
  rw [initialPrefixGap_eq]
  have hKq : (0 : ℚ) < K := by exact_mod_cast (show 0 < K by omega)
  have hrq : (0 : ℚ) < r := by exact_mod_cast (show 0 < r by omega)
  positivity

/-- Prefix mass in the fractional middle block, where the prefix length is
`m+s`. -/
def middlePrefix (k m s : ℕ) : ℚ :=
  ((m + s : ℕ) : ℚ) -
    (s : ℚ) * ((s : ℚ) + 1) / (2 * (k : ℚ))

/-- Exact middle-block prefix gap. -/
theorem middlePrefixGap_eq {k m s : ℕ} (hk : k ≠ 0) :
    middlePrefix k m s - uniformPrefix (k + 2 * m) (m + s) =
      (m : ℚ) *
          ((k : ℚ) * ((m : ℚ) + 1 + 2 * (s : ℚ)) -
            2 * (s : ℚ) * ((s : ℚ) + 1)) /
        (2 * (k : ℚ) * ((k : ℚ) + 2 * (m : ℚ))) := by
  have hkq : (k : ℚ) ≠ 0 := by exact_mod_cast hk
  have hKq : (k : ℚ) + 2 * (m : ℚ) ≠ 0 := by
    have hkpos : (0 : ℚ) < k := by exact_mod_cast (show 0 < k by omega)
    positivity
  simp only [middlePrefix, uniformPrefix, Nat.cast_add, Nat.cast_mul]
  field_simp
  ring

/-- The middle-block prefix gap is strictly positive.  This is the central
finite inequality in the majorization proof for the `π^m` approximants. -/
theorem middlePrefixGap_pos {k m s : ℕ}
    (hk : 1 ≤ k) (hm : 1 ≤ m) (hs : s + 1 ≤ k) :
    0 < middlePrefix k m s - uniformPrefix (k + 2 * m) (m + s) := by
  rw [middlePrefixGap_eq (by omega : k ≠ 0)]
  have hkq : (0 : ℚ) < k := by exact_mod_cast (show 0 < k by omega)
  have hmq : (0 : ℚ) < m := by exact_mod_cast (show 0 < m by omega)
  have hsq : (s : ℚ) + 1 ≤ k := by exact_mod_cast hs
  have htail : 0 ≤ 2 * (s : ℚ) * ((k : ℚ) - (s : ℚ) - 1) := by
    have hs0 : (0 : ℚ) ≤ s := by positivity
    have hdiff : 0 ≤ (k : ℚ) - (s : ℚ) - 1 := by linarith
    positivity
  have hfirst : 0 < (k : ℚ) * ((m : ℚ) + 1) := by positivity
  have hbracket :
      0 < (k : ℚ) * ((m : ℚ) + 1 + 2 * (s : ℚ)) -
          2 * (s : ℚ) * ((s : ℚ) + 1) := by
    calc
      (k : ℚ) * ((m : ℚ) + 1 + 2 * (s : ℚ)) -
          2 * (s : ℚ) * ((s : ℚ) + 1) =
        (k : ℚ) * ((m : ℚ) + 1) +
          2 * (s : ℚ) * ((k : ℚ) - (s : ℚ) - 1) := by ring
      _ > 0 := add_pos_of_pos_of_nonneg hfirst htail
  have hden : 0 < 2 * (k : ℚ) * ((k : ℚ) + 2 * (m : ℚ)) := by positivity
  exact div_pos (mul_pos hmq hbracket) hden

/-- Total mass of the uniform comparison list. -/
def uniformTotal (K : ℕ) : ℚ := ((K : ℚ) - 1) / 2

/-- In the final zero block, the prefix gap is exactly the omitted tail of
the uniform comparison list. -/
theorem finalPrefixGap_eq {K r q : ℕ} (h : K = r + q + 1) :
    uniformTotal K - uniformPrefix K r =
      (q : ℚ) * ((q : ℚ) + 1) / (2 * (K : ℚ)) := by
  subst K
  simp only [uniformTotal, uniformPrefix, Nat.cast_add, Nat.cast_one]
  field_simp
  ring

/-- Every proper final-block prefix has strictly positive gap. -/
theorem finalPrefixGap_pos {K r q : ℕ}
    (h : K = r + q + 1) (hq : 1 ≤ q) :
    0 < uniformTotal K - uniformPrefix K r := by
  rw [finalPrefixGap_eq h]
  have hKq : (0 : ℚ) < K := by exact_mod_cast (show 0 < K by omega)
  have hqq : (0 : ℚ) < q := by exact_mod_cast (show 0 < q by omega)
  positivity

end EnterpriseMath.PrecisionPi.MajorizationCore
