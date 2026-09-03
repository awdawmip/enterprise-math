import Mathlib

namespace EnterpriseMath.PrecisionPi.CodimensionTwoMajorization

open scoped BigOperators

/-- Descending Gamma-shift list `1,(k-1)/k,...,1/k,0`, indexed from zero. -/
def majorA (k i : ℕ) : ℚ :=
  ((k : ℚ) - (i : ℚ)) / (k : ℚ)

/-- Descending comparison list `(k+1)/(k+2),...,1/(k+2)`, indexed from zero. -/
def majorB (k i : ℕ) : ℚ :=
  ((k : ℚ) + 1 - (i : ℚ)) / ((k : ℚ) + 2)

/-- Difference of the first `j` descending partial sums. -/
def topGap (k j : ℕ) : ℚ :=
  ∑ i in Finset.range j, (majorA k i - majorB k i)

/-- Closed form for the majorization gap. -/
def gapFormula (k j : ℕ) : ℚ :=
  (j : ℚ) * ((k : ℚ) - (j : ℚ) + 1) /
    ((k : ℚ) * ((k : ℚ) + 2))

/-- Exact partial-sum gap underlying the codimension-two Gamma majorization. -/
theorem topGap_formula (k j : ℕ) (hk : k ≠ 0) :
    topGap k j = gapFormula k j := by
  induction j with
  | zero =>
      simp [topGap, gapFormula]
  | succ j ih =>
      simp only [topGap, Finset.sum_range_succ] at ih ⊢
      rw [ih]
      have hkq : (k : ℚ) ≠ 0 := by exact_mod_cast hk
      have hk2 : (k : ℚ) + 2 ≠ 0 := by positivity
      simp only [majorA, majorB, gapFormula]
      push_cast
      field_simp [hkq, hk2]
      ring

/-- Every proper nonempty prefix has strictly positive gap. -/
theorem topGap_pos {k j : ℕ} (hk : 1 ≤ k) (hj : 1 ≤ j) (hjk : j ≤ k) :
    0 < topGap k j := by
  rw [topGap_formula k j (by omega)]
  have hjq : 0 < (j : ℚ) := by exact_mod_cast hj
  have hkj : 0 < (k : ℚ) - (j : ℚ) + 1 := by
    have hcast : (j : ℚ) ≤ (k : ℚ) := by exact_mod_cast hjk
    linarith
  have hkq : 0 < (k : ℚ) := by exact_mod_cast hk
  have hk2 : 0 < (k : ℚ) + 2 := by positivity
  exact div_pos (mul_pos hjq hkj) (mul_pos hkq hk2)

/-- The two complete shift lists have the same total sum. -/
theorem topGap_full (k : ℕ) (hk : k ≠ 0) :
    topGap k (k + 1) = 0 := by
  rw [topGap_formula k (k + 1) hk]
  simp [gapFormula]

/-- Paper-I/Paper-II range: for `k>=2`, strict majorization holds at every
proper prefix and equality holds at the full prefix. -/
theorem strict_majorization_certificate {k : ℕ} (hk : 2 ≤ k) :
    (∀ j : ℕ, 1 ≤ j → j ≤ k → 0 < topGap k j) ∧
      topGap k (k + 1) = 0 := by
  constructor
  · intro j hj hjk
    exact topGap_pos (by omega) hj hjk
  · exact topGap_full k (by omega)

end EnterpriseMath.PrecisionPi.CodimensionTwoMajorization
