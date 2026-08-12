import EnterpriseMath.Quotient.RootQuotientHardDirectionUsedMacro
import EnterpriseMath.Quotient.RootQuotientMultiSpareReachability
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Budget-three hard-direction decomposition.**

If directions `2` and `3` are hard and a feasible normalized presentation uses
at most three optional composite macro types, then two actual used macro slots
can be chosen as `2^a` and `3^b` with `2<=a,b<=h+1`.  They are distinct, and
after removing them at most one spare macro type remains.

This is the structural reduction behind finite budget-three repair
certificates: arbitrary dictionaries reduce to a finite pure-pair exponent grid
plus at most one spare slot. -/
theorem exists_budgetThree_twoThree_used_powers_and_one_spare
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hTwoHard : 2 ∈ RootQuotientHardPrimeDirections N h)
    (hThreeHard : 3 ∈ RootQuotientHardPrimeDirections N h)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard ≤ 3) :
    ∃ g₂ g₃ a b : ℕ, ∃ R : Set ℕ,
      g₂ ∈ S ∧
      g₃ ∈ S ∧
      g₂ ≠ g₃ ∧
      2 ≤ a ∧ a ≤ h + 1 ∧ g₂ = 2 ^ a ∧
      2 ≤ b ∧ b ≤ h + 1 ∧ g₃ = 3 ^ b ∧
      R = S \ ({g₂, g₃} : Set ℕ) ∧
      R.Finite ∧
      R.ncard ≤ 1 ∧
      S = ({g₂, g₃} : Set ℕ) ∪ R := by
  obtain ⟨g₂, a, hg₂S, haTwo, haLe, hg₂Eq, _hg₂Dvd⟩ :=
    exists_used_composite_power_for_hardPrimeDirection
      hr hBinary hS.2.1 hS.2.2 hTwoHard
  obtain ⟨g₃, b, hg₃S, hbTwo, hbLe, hg₃Eq, _hg₃Dvd⟩ :=
    exists_used_composite_power_for_hardPrimeDirection
      hr hBinary hS.2.1 hS.2.2 hThreeHard
  have hgNe : g₂ ≠ g₃ := by
    intro hEq
    have hServeTwo : RootQuotientMacroServesPrimeDirection g₂ 2 :=
      ⟨a, by omega, hg₂Eq⟩
    have hServeThree : RootQuotientMacroServesPrimeDirection g₂ 3 := by
      refine ⟨b, by omega, ?_⟩
      rw [hEq]
      exact hg₃Eq
    have hPrimeEq := primeDirection_eq_of_macro_serves_both
      Nat.prime_two Nat.prime_three hServeTwo hServeThree
    omega
  let P : Set ℕ := ({g₂, g₃} : Set ℕ)
  let R : Set ℕ := S \ P
  have hPSub : P ⊆ S := by
    intro g hg
    dsimp [P] at hg
    simp at hg
    rcases hg with rfl | rfl
    · exact hg₂S
    · exact hg₃S
  have hPCard : P.ncard = 2 := by
    dsimp [P]
    simp [hgNe]
  have hRFinite : R.Finite := by
    dsimp [R]
    exact hS.1.sdiff
  have hDecompCard : R.ncard + P.ncard = S.ncard := by
    dsimp [R]
    exact Set.ncard_sdiff_add_ncard_of_subset hPSub hS.1
  have hRCard : R.ncard ≤ 1 := by
    rw [hPCard] at hDecompCard
    omega
  have hSetEq : S = P ∪ R := by
    ext g
    constructor
    · intro hgS
      by_cases hgP : g ∈ P
      · exact Or.inl hgP
      · exact Or.inr ⟨hgS, hgP⟩
    · intro hg
      rcases hg with hgP | hgR
      · exact hPSub hgP
      · exact hgR.1
  exact ⟨g₂, g₃, a, b, R,
    hg₂S, hg₃S, hgNe,
    haTwo, haLe, hg₂Eq,
    hbTwo, hbLe, hg₃Eq,
    rfl, hRFinite, hRCard,
    by simpa [P] using hSetEq⟩

end EnterpriseMath.Quotient
