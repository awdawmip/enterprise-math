import EnterpriseMath.Quotient.RootQuotientHardDirectionSaturation
import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- If the previous-prime pure shell already lies in the bounded domain, then
there are at least `s` hard prime directions.

For positive budget `s`, the last direction that can be assigned one of the
`s` available macro slots is the zero-indexed prime `p_{s-1}`. -/
theorem macroBudget_le_hardPrimeDirections_ncard_of_prevPrime_pow_le
    {N h s : ℕ}
    (hs : 1 ≤ s)
    (hPrev : (Nat.nth Nat.Prime (s - 1)) ^ (h + 1) ≤ N) :
    s ≤ (RootQuotientHardPrimeDirections N h).ncard := by
  have hHardEq : (RootQuotientHardPrimeDirections N h).ncard =
      rootQuotientPrimeDirectionDemand N h := by
    rw [rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff]
    rfl
  rw [hHardEq]
  by_contra hNot
  have hDemandLe : rootQuotientPrimeDirectionDemand N h ≤ s - 1 := by
    omega
  have hStateLt :=
    (primeDirectionDemand_le_iff_stateBound_lt_nthPrime_pow_succ
      (N := N) (h := h) (s := s - 1)).1 hDemandLe
  omega

/-- **Macro-budget saturation criterion.**

Once `p_{s-1}^{h+1}` is inside the state domain, any separator with at most
`s` optional composite macro types is exactly saturated: it has exactly `s`
macros, and every macro is a pure power serving one hard prime direction.

This gives the general transition from arbitrary mixed code design to a
pure-power exponent-coin problem. -/
theorem macroBudget_saturation_forces_exact_card_and_pure_powers
    {r N h s : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hs : 1 ≤ s)
    (hBinary : N < 2 ^ r)
    (hPrev : (Nat.nth Nat.Prime (s - 1)) ^ (h + 1) ≤ N)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hSCard : S.ncard ≤ s) :
    S.ncard = s ∧
      ∀ g : ℕ, g ∈ S →
        ∃ p e : ℕ,
          p ∈ RootQuotientHardPrimeDirections N h ∧
          1 ≤ e ∧ g = p ^ e := by
  have hsHard : s ≤ (RootQuotientHardPrimeDirections N h).ncard :=
    macroBudget_le_hardPrimeDirections_ncard_of_prevPrime_pow_le hs hPrev
  have hHardLeS := hardPrimeDirections_ncard_le_macroFamily_of_separator
    hr hBinary hSFinite hSFamily hSep
  have hCardEq : S.ncard = s := by omega
  have hSat : S.ncard ≤ (RootQuotientHardPrimeDirections N h).ncard :=
    hSCard.trans hsHard
  refine ⟨hCardEq, ?_⟩
  exact every_macro_is_pure_power_of_hardPrime_of_saturated_separator
    hr hBinary hSFinite hSFamily hSep hSat

end EnterpriseMath.Quotient
