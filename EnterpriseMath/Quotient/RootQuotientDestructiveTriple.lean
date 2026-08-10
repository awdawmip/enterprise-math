import EnterpriseMath.Quotient.RootAdjacentBoundary
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The literal floor-quotient transition is merge-free on the three exact
candidate states `{1,n-1,n}` when their three quotient successors are pairwise
distinct.  This is an execution property, not a counterfactual signature. -/
def QuotientTripleMergeFree (n a : ℕ) : Prop :=
  1 / a ≠ (n - 1) / a ∧
  1 / a ≠ n / a ∧
  (n - 1) / a ≠ n / a

/-- Exact first-step splitter law for the destructive three-state witness.

For `n>=3` and a nonidentity quotient action `a>=2`, the action is merge-free
on `{1,n-1,n}` iff `a` is a nontrivial proper divisor of `n`.

This is the local arithmetic kernel behind the prime/composite execution
boundary: primes have no nonidentity merge-free first splitter, while every
composite has one. -/
theorem quotientTripleMergeFree_iff_proper_dvd
    {n a : ℕ}
    (hn : 3 ≤ n)
    (ha : 2 ≤ a) :
    QuotientTripleMergeFree n a ↔ a < n ∧ a ∣ n := by
  have haPos : 0 < a := by omega
  have hOneLt : 1 < a := by omega
  have hOneDiv : 1 / a = 0 := Nat.div_eq_of_lt hOneLt
  constructor
  · rintro ⟨hOnePred, _hOneTop, hPredTop⟩
    have hPredNonzero : (n - 1) / a ≠ 0 := by
      intro hZero
      apply hOnePred
      simpa [hOneDiv, hZero]
    have haLePred : a ≤ n - 1 := by
      by_contra hnot
      have hPredLtA : n - 1 < a := by omega
      have hPredZero : (n - 1) / a = 0 := Nat.div_eq_of_lt hPredLtA
      exact hPredNonzero hPredZero
    have haLtN : a < n := by omega
    have hDvd : a ∣ n :=
      (quotient_adjacent_jump_iff_dvd (q := n) (a := a) (by omega) (by omega)).1
        hPredTop
    exact ⟨haLtN, hDvd⟩
  · rintro ⟨haLtN, hDvd⟩
    have haLePred : a ≤ n - 1 := by omega
    have hPredPos : 0 < (n - 1) / a := Nat.div_pos haLePred haPos
    have hTopPos : 0 < n / a := Nat.div_pos (by omega) haPos
    have hPredTop : (n - 1) / a ≠ n / a :=
      (quotient_adjacent_jump_iff_dvd (q := n) (a := a) (by omega) (by omega)).2
        hDvd
    constructor
    · omega
    constructor
    · omega
    · exact hPredTop

end EnterpriseMath.Quotient
