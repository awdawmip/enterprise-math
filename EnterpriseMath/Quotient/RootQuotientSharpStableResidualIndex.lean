import EnterpriseMath.Quotient.RootQuotientSharpStableMacroLadder
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The value-indexed sharp residual constant is exactly the executable
index-sum `sum_{i<s} (e_i-1)`, where `e_i=clog_{p_i}(q_s)`.

The value-indexed definition is more convenient for factorization-support
arguments, while the index-sum is more convenient for explicit evaluation and
matches the stable-ladder oracle. -/
theorem rootQuotientSharpStableResidualBudget_eq_indexSum
    (s : ℕ) :
    rootQuotientSharpStableResidualBudget s =
      ∑ i in Finset.range s,
        (rootQuotientStableMacroExponent s i - 1) := by
  classical
  unfold rootQuotientSharpStableResidualBudget
    rootQuotientStablePrimeDirectionFinset
  rw [Finset.sum_image
    (Nat.nth_injective Nat.infinite_setOfPred_prime).injOn]
  apply Finset.sum_congr rfl
  intro i _hi
  simp [rootQuotientStableMacroExponent]

end EnterpriseMath.Quotient
