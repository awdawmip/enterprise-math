import EnterpriseMath.Quotient.RootQuotientPrimeFourSixHorizon
import EnterpriseMath.Quotient.RootQuotientMixedDirectionMacroPhase
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- In the mixed wedge, the two explicit macros `{4,6}` form a valid optional
composite-macro presentation at horizon `h`. -/
theorem four_six_is_compositeMacroPresentation_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    RootQuotientCompositeMacroPresentation
      r N h ({4, 6} : Set ℕ) := by
  have hPowPos : 1 ≤ 3 ^ h := by positivity
  have hSixN : 6 ≤ N := by omega
  have hFourN : 4 ≤ N := by omega
  have hNThree : 3 ≤ N := by omega
  have hFourFree : RPowerFree r 4 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hFourN.trans_lt hBinary)
  have hSixFree : RPowerFree r 6 :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hSixN.trans_lt hBinary)
  refine ⟨by simp, ?_, ?_⟩
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl
    · refine ⟨⟨by omega, hFourN, hFourFree⟩, ?_⟩
      intro hPrime
      norm_num at hPrime
    · refine ⟨⟨by omega, hSixN, hSixFree⟩, ?_⟩
      intro hPrime
      norm_num at hPrime
  · simpa [RootQuotientPrimeFourSixBasis] using
      (primeFourSixBasis_separates_iff_stateBound_lt_three_pow_succ
        (r := r) (N := N) (h := h)
        hr hNThree hh hBinary).2 hUpper

/-- **Exact two-macro phase in the mixed wedge.**

The one-macro lower bound and the explicit `{4,6}` upper construction meet:
exactly two optional composite macro types are necessary and sufficient. -/
theorem minimumCompositeMacroCount_eq_two_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientMinimumCompositeMacroCount r N h = 2 := by
  have hLowerMu :=
    two_le_minimumCompositeMacroCount_of_two_three_wedge
      hr hh hBinary hLower hUpper
  have hPresentation :=
    four_six_is_compositeMacroPresentation_of_two_three_wedge
      hr hh hBinary hLower hUpper
  have hUpperMu := rootQuotientMinimumCompositeMacroCount_le hPresentation
  have hPairCard : ({4, 6} : Set ℕ).ncard = 2 := by
    norm_num
  rw [hPairCard] at hUpperMu
  omega

/-- In the same exact phase, pure-prime directions account for exactly one of
the two required macro types. -/
theorem directionDemand_eq_one_and_mixedOverhead_eq_one_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 1 ∧
      rootQuotientMixedDirectionMacroOverhead r N h = 1 := by
  have hDir : rootQuotientPrimeDirectionDemand N h = 1 :=
    primeDirectionDemand_eq_one_of_two_three_wedge hh hLower hUpper
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 2 :=
    minimumCompositeMacroCount_eq_two_of_two_three_wedge
      hr hh hBinary hLower hUpper
  constructor
  · exact hDir
  · dsimp [rootQuotientMixedDirectionMacroOverhead]
    rw [hDir, hMu]
    norm_num

/-- Exact total primitive storage in the mixed wedge. -/
theorem minimumStorage_eq_primeBasis_add_two_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard + 2 := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr (by omega)]
  rw [minimumCompositeMacroCount_eq_two_of_two_three_wedge
    hr hh hBinary hLower hUpper]

end EnterpriseMath.Quotient
