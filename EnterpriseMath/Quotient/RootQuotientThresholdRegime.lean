import EnterpriseMath.Quotient.RootQuotientWordBasis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

/-- In the finite regime `N<2^r`, one positive quotient-root observation is
exactly a threshold query on the action denominator.

For `0<=q<=N` and positive `a`,
`root r (q/a)=1` iff `a<=q`. -/
theorem root_quotient_eq_one_iff_action_le_of_lt_two_pow
    {r N q a : ℕ}
    (hr : 1 ≤ r)
    (hN : N < 2 ^ r)
    (hqN : q ≤ N)
    (ha : 1 ≤ a) :
    root r (q / a) = 1 ↔ a ≤ q := by
  have haPos : 0 < a := by omega
  constructor
  · intro hRoot
    have hr0 : r ≠ 0 := by omega
    have hChar :=
      (EnterpriseMath.IntegerRoot.root_eq_iff
        (p := r) (n := q / a) (k := 1) hr0).1 hRoot
    have hOneQuot : 1 ≤ q / a := by simpa using hChar.1
    exact (Nat.le_div_iff_mul_le haPos).1 (by simpa using hOneQuot)
  · intro haq
    have hOneQuot : 1 ≤ q / a :=
      (Nat.le_div_iff_mul_le haPos).2 (by simpa using haq)
    have hQuotLeQ : q / a ≤ q := Nat.div_le_self q a
    have hQuotLeN : q / a ≤ N := hQuotLeQ.trans hqN
    exact root_eq_one_of_pos_le_of_lt_two_pow hr hN hOneQuot hQuotLeN

/-- Consequently, every quotient word in the same finite regime is exactly the
threshold query for its compiled denominator product. -/
theorem root_quotient_word_eq_one_iff_product_le_of_lt_two_pow
    {r N q : ℕ} {G : Set ℕ} {w : List ℕ}
    (hr : 1 ≤ r)
    (hN : N < 2 ^ r)
    (hqN : q ≤ N)
    (hG : PositiveRootQuotientGenerators G)
    (hw : RootQuotientWordOver G w) :
    root r (rootQuotientWordState q w) = 1 ↔
      rootQuotientWordProduct w ≤ q := by
  have hProdPos : 1 ≤ rootQuotientWordProduct w :=
    rootQuotientWordProduct_pos hG hw
  rw [rootQuotientWordState_eq_div_product]
  exact root_quotient_eq_one_iff_action_le_of_lt_two_pow
    hr hN hqN hProdPos

end EnterpriseMath.Quotient
