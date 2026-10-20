import EnterpriseMath.Quotient.RootQuotientBudgetThreeDecomposition
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Exact budget-three one-spare normal form.**

When directions `2` and `3` are hard, every feasible normalized optional
macro family of cardinality at most three is either exactly the two used pure
prime-power macros, or those two macros plus one singleton spare.

The serving exponents are execution-relevant and lie in the finite interval
`[2,h+1]`. -/
theorem exists_budgetThree_twoThree_pair_or_pair_plus_single_spare
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hTwoHard : 2 ∈ RootQuotientHardPrimeDirections N h)
    (hThreeHard : 3 ∈ RootQuotientHardPrimeDirections N h)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard ≤ 3) :
    ∃ g₂ g₃ a b : ℕ,
      g₂ ∈ S ∧
      g₃ ∈ S ∧
      g₂ ≠ g₃ ∧
      2 ≤ a ∧ a ≤ h + 1 ∧ g₂ = 2 ^ a ∧
      2 ≤ b ∧ b ≤ h + 1 ∧ g₃ = 3 ^ b ∧
      (S = ({g₂, g₃} : Set ℕ) ∨
        ∃ g : ℕ, S = ({g₂, g₃} : Set ℕ) ∪ ({g} : Set ℕ)) := by
  obtain ⟨g₂, g₃, a, b, R,
      hg₂S, hg₃S, hgNe,
      haTwo, haLe, hg₂Eq,
      hbTwo, hbLe, hg₃Eq,
      hREq, hRFinite, hRCard, hSEq⟩ :=
    exists_budgetThree_twoThree_used_powers_and_one_spare
      hr hBinary hTwoHard hThreeHard hS hSCard
  have hRShape : R = ∅ ∨ ∃ g : ℕ, R = {g} :=
    (Set.ncard_le_one_iff_eq hRFinite).1 hRCard
  refine ⟨g₂, g₃, a, b,
    hg₂S, hg₃S, hgNe,
    haTwo, haLe, hg₂Eq,
    hbTwo, hbLe, hg₃Eq, ?_⟩
  rcases hRShape with hEmpty | ⟨g, hSingleton⟩
  · left
    rw [hSEq, hEmpty]
    simp
  · right
    refine ⟨g, ?_⟩
    rw [hSEq, hSingleton]

end EnterpriseMath.Quotient
