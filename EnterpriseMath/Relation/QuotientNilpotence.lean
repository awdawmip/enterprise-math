import EnterpriseMath.Relation.PrimePowerQuotientTriangle
import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace EnterpriseMath.QuotientNilpotence

open EnterpriseMath.PrimePowerQuotientTriangle

/-- Execute a finite word of quotient action labels from left to right. -/
def runQuotients : List ℕ → ℕ → ℕ
  | [], n => n
  | a :: w, n => runQuotients w (quotient a n)

/-- A quotient word recoalesces to division by the product of all action labels. -/
theorem runQuotients_eq_div_prod :
    ∀ (w : List ℕ) (n : ℕ), runQuotients w n = n / w.prod := by
  intro w
  induction w with
  | nil =>
      intro n
      simp [runQuotients]
  | cons a w ih =>
      intro n
      simp only [runQuotients, List.prod_cons]
      rw [ih]
      simp [quotient, Nat.div_div_eq_div_mul]

/-- Every nontrivial quotient action strictly lowers every positive state. -/
theorem quotient_lt_self {a n : ℕ} (ha : 2 ≤ a) (hn : 0 < n) :
    quotient a n < n := by
  simpa [quotient] using
    Nat.div_lt_self hn (lt_of_lt_of_le Nat.one_lt_two ha)

/-- A word of labels at least `2` has product at least `2^(word length)`. -/
theorem two_pow_length_le_prod {w : List ℕ}
    (hw : ∀ a ∈ w, 2 ≤ a) :
    2 ^ w.length ≤ w.prod := by
  induction w with
  | nil => simp
  | cons a w ih =>
      have ha : 2 ≤ a := hw a (by simp)
      have hw' : ∀ b ∈ w, 2 ≤ b := by
        intro b hb
        exact hw b (by simp [hb])
      have htail := ih hw'
      simp only [List.length_cons, List.prod_cons]
      rw [Nat.pow_succ']
      exact Nat.mul_le_mul ha htail

/-- Once `2^length` exceeds the starting scale, every such quotient history reaches zero. -/
theorem runQuotients_eq_zero_of_lt_two_pow
    {w : List ℕ} {n : ℕ}
    (hw : ∀ a ∈ w, 2 ≤ a)
    (hn : n < 2 ^ w.length) :
    runQuotients w n = 0 := by
  rw [runQuotients_eq_div_prod]
  apply Nat.div_eq_of_lt
  exact lt_of_lt_of_le hn (two_pow_length_le_prod hw)

/-- The deterministic quotient-by-two word of depth `k`. -/
def q2Word (k : ℕ) : List ℕ := List.replicate k 2

/-- Repeating quotient by two is exactly division by `2^k`. -/
theorem run_q2Word (k n : ℕ) :
    runQuotients (q2Word k) n = n / 2 ^ k := by
  simp [runQuotients_eq_div_prod, q2Word]

/-- A quotient-by-two chain reaches zero exactly beyond its visible binary depth. -/
theorem run_q2Word_eq_zero {k n : ℕ} (hn : n < 2 ^ k) :
    runQuotients (q2Word k) n = 0 := by
  rw [run_q2Word]
  exact Nat.div_eq_of_lt hn

end EnterpriseMath.QuotientNilpotence
