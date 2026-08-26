import EnterpriseMath.Quotient.RootQuotientMixedDirectionMacroPhase
import EnterpriseMath.Quotient.RootQuotientBinaryOneMacroFrontier
import EnterpriseMath.Quotient.RootQuotientPrimeShellBinary
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Below the prime-only horizon in the high-root regime, the pure direction
`2` is still hard, so directional macro demand is positive. -/
theorem one_le_primeDirectionDemand_of_horizon_lt_primeHorizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLtL : h < rootQuotientPrimeHorizon r N) :
    1 ≤ rootQuotientPrimeDirectionDemand N h := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow hr hN hBinary
  have hSuccLeLog : h + 1 ≤ Nat.log 2 N := by
    rw [← hLog]
    omega
  have hNZero : N ≠ 0 := by omega
  have hTwoPowLe : 2 ^ (h + 1) ≤ N :=
    Nat.pow_le_of_le_log hNZero hSuccLeLog
  by_contra hNot
  have hDemandZero : rootQuotientPrimeDirectionDemand N h = 0 := by omega
  have hStateLt :=
    (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
      (N := N) (h := h) (s := 0)).1 (by simp [hDemandZero])
  have hStateLtTwo : N < 2 ^ (h + 1) := by
    simpa [rootQuotientStablePrimeBase] using hStateLt
  omega

/-- Throughout the exact one-macro plateau, directional demand is exactly one.

The true macro minimum is one there, while the pure direction `2` remains hard;
therefore no mixed-direction overhead remains. -/
theorem primeDirectionDemand_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hHLe : rootQuotientPrimeFourHorizon N ≤ h)
    (hLtL : h < rootQuotientPrimeHorizon r N) :
    rootQuotientPrimeDirectionDemand N h = 1 := by
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 1 :=
    rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree hHLe hLtL
  have hHPos := rootQuotientPrimeFourHorizon_pos hr hN hBinary
  have hh : 1 ≤ h := hHPos.trans hHLe
  have hDirLe : rootQuotientPrimeDirectionDemand N h ≤ 1 := by
    have hLe := primeDirectionDemand_le_minimumCompositeMacroCount
      hr hh hBinary
    rw [hMu] at hLe
    exact hLe
  have hDirPos : 1 ≤ rootQuotientPrimeDirectionDemand N h :=
    one_le_primeDirectionDemand_of_horizon_lt_primeHorizon
      hr (by omega) hBinary hLtL
  omega

/-- Mixed-direction overhead vanishes throughout the one-macro plateau. -/
theorem mixedDirectionMacroOverhead_eq_zero_of_primeFourHorizon_le_of_lt_primeHorizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hHLe : rootQuotientPrimeFourHorizon N ≤ h)
    (hLtL : h < rootQuotientPrimeHorizon r N) :
    rootQuotientMixedDirectionMacroOverhead r N h = 0 := by
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 1 :=
    rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree hHLe hLtL
  have hDir : rootQuotientPrimeDirectionDemand N h = 1 :=
    primeDirectionDemand_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree hHLe hLtL
  simp [rootQuotientMixedDirectionMacroOverhead, hMu, hDir]

/-- Once the prime-only horizon is available, both directional demand and true
optional-macro demand are zero. -/
theorem primeDirectionDemand_eq_zero_of_primeHorizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLLe : rootQuotientPrimeHorizon r N ≤ h) :
    rootQuotientPrimeDirectionDemand N h = 0 := by
  have hMuZero : rootQuotientMinimumCompositeMacroCount r N h = 0 :=
    rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
      hr hh hLLe
  have hDirLe := primeDirectionDemand_le_minimumCompositeMacroCount
    hr hh hBinary
  rw [hMuZero] at hDirLe
  omega

/-- Mixed-direction overhead also vanishes after the prime-only horizon. -/
theorem mixedDirectionMacroOverhead_eq_zero_of_primeHorizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLLe : rootQuotientPrimeHorizon r N ≤ h) :
    rootQuotientMixedDirectionMacroOverhead r N h = 0 := by
  have hMuZero : rootQuotientMinimumCompositeMacroCount r N h = 0 :=
    rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
      hr hh hLLe
  have hDirZero : rootQuotientPrimeDirectionDemand N h = 0 :=
    primeDirectionDemand_eq_zero_of_primeHorizon_le
      hr hh hBinary hLLe
  simp [rootQuotientMixedDirectionMacroOverhead, hMuZero, hDirZero]

/-- **Mixed-direction overhead vanishing threshold.**

In the nontrivial high-root regime with prime-only horizon at least three, the
exact one-macro horizon `H4` is a global upper threshold for mixed-direction
storage overhead: at every positive horizon `h>=H4`, the mixed overhead is
zero.

Below `H4` it can be strictly positive, as witnessed by the `2*3^h` / `3^(h+1)`
wedge. -/
theorem mixedDirectionMacroOverhead_eq_zero_of_primeFourHorizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hHLe : rootQuotientPrimeFourHorizon N ≤ h) :
    rootQuotientMixedDirectionMacroOverhead r N h = 0 := by
  by_cases hLtL : h < rootQuotientPrimeHorizon r N
  · exact mixedDirectionMacroOverhead_eq_zero_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree hHLe hLtL
  · have hLLe : rootQuotientPrimeHorizon r N ≤ h := by omega
    have hHPos := rootQuotientPrimeFourHorizon_pos hr hN hBinary
    have hh : 1 ≤ h := hHPos.trans hHLe
    exact mixedDirectionMacroOverhead_eq_zero_of_primeHorizon_le
      hr hh hBinary hLLe

end EnterpriseMath.Quotient
