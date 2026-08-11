import EnterpriseMath.Quotient.RootQuotientExactMixedDirectionPhase
import EnterpriseMath.Quotient.RootQuotientMixedDirectionVanishing
import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Pure-direction demand is exactly one throughout the complete directional
band

`2^(h+1) <= N < 3^(h+1)`.

This is the exact `s=0` / `s=1` slice of the prime-counting / nth-prime Galois
boundary. -/
theorem primeDirectionDemand_eq_one_of_two_pow_le_of_lt_three_pow
    {N h : ℕ}
    (hLower : 2 ^ (h + 1) ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 1 := by
  have hUpperDemand : rootQuotientPrimeDirectionDemand N h ≤ 1 := by
    apply
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 1)).2
    simpa [rootQuotientStablePrimeBase] using hUpper
  have hDemandPos : 1 ≤ rootQuotientPrimeDirectionDemand N h := by
    by_contra hNot
    have hDemandZero : rootQuotientPrimeDirectionDemand N h = 0 := by omega
    have hStateLt :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 0)).1 (by simp [hDemandZero])
    have hStateLtTwo : N < 2 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase] using hStateLt
    omega
  omega

/-- First fixed-horizon phase: below the next prime-only shell, no optional
composite macro is needed. -/
theorem minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hUpper : N < 2 ^ (h + 1)) :
    rootQuotientMinimumCompositeMacroCount r N h = 0 := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
      hr (by omega) hBinary
  have hNZero : N ≠ 0 := by omega
  have hLogLt : Nat.log 2 N < h + 1 :=
    (Nat.log_lt_iff_lt_pow (by omega) hNZero).2 hUpper
  have hLLe : rootQuotientPrimeHorizon r N ≤ h := by
    rw [hLog]
    omega
  exact rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
    hr (by omega) hLLe

/-- Conversely, in a nontrivial high-root domain, zero optional macros imply
that the state bound lies below the next prime-only shell. -/
theorem stateBound_lt_two_pow_succ_of_minimumCompositeMacroCount_eq_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hZero : rootQuotientMinimumCompositeMacroCount r N h = 0) :
    N < 2 ^ (h + 1) := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
      hr (by omega) hBinary
  have hLLe : rootQuotientPrimeHorizon r N ≤ h := by
    by_contra hNot
    have hBelow : h < rootQuotientPrimeHorizon r N := by omega
    have hPos := rootQuotientMinimumCompositeMacroCount_pos_of_belowPrimeHorizon
      hr (by omega) hBelow
    rw [hZero] at hPos
    omega
  have hLogLe : Nat.log 2 N ≤ h := by
    rw [← hLog]
    exact hLLe
  have hNZero : N ≠ 0 := by omega
  exact (Nat.log_lt_iff_lt_pow (by omega) hNZero).1 (by omega)

/-- Exact zero-macro phase boundary. -/
theorem minimumCompositeMacroCount_eq_zero_iff_stateBound_lt_two_pow_succ
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h = 0 ↔
      N < 2 ^ (h + 1) := by
  constructor
  · exact stateBound_lt_two_pow_succ_of_minimumCompositeMacroCount_eq_zero
      hr hN hBinary
  · exact minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
      hr hN hBinary

/-- Second fixed-horizon phase: between the prime-only shell and the one-macro
`4` shell, exactly one optional macro is necessary and sufficient. -/
theorem minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 ^ (h + 1) ≤ N)
    (hUpper : N < 2 * 3 ^ h) :
    rootQuotientMinimumCompositeMacroCount r N h = 1 := by
  have hN : 2 ≤ N := by
    have hTwoPowPos : 2 ≤ 2 ^ (h + 1) := by positivity
    omega
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
      hr (by omega) hBinary
  have hLogGe : h + 1 ≤ Nat.log 2 N :=
    Nat.le_log_of_pow_le (by omega) hLower
  have hLtL : h < rootQuotientPrimeHorizon r N := by
    rw [hLog]
    omega
  have hLThree : 3 ≤ rootQuotientPrimeHorizon r N := by
    rw [hLog]
    omega
  have hSepFour : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeFourBasis N) :=
    (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
      hr hN hBinary).2 hUpper
  have hHLe : rootQuotientPrimeFourHorizon N ≤ h :=
    rootQuotientPrimeFourHorizon_minimal hr hN hBinary hSepFour
  exact rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
    hr hN hBinary hLThree hHLe hLtL

/-- Exact characterization of the one-macro phase inside the triadic band. -/
theorem minimumCompositeMacroCount_eq_one_iff_first_mixed_band
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hTriadic : N < 3 ^ (h + 1)) :
    rootQuotientMinimumCompositeMacroCount r N h = 1 ↔
      2 ^ (h + 1) ≤ N ∧ N < 2 * 3 ^ h := by
  constructor
  · intro hMuOne
    have hLower : 2 ^ (h + 1) ≤ N := by
      by_contra hNot
      have hZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
        hr hN hBinary (by omega)
      rw [hMuOne] at hZero
      omega
    have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
      rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
        hr (by omega) hBinary
    have hLogGe : h + 1 ≤ Nat.log 2 N :=
      Nat.le_log_of_pow_le (by omega) hLower
    have hLtL : h < rootQuotientPrimeHorizon r N := by
      rw [hLog]
      omega
    have hLThree : 3 ≤ rootQuotientPrimeHorizon r N := by
      rw [hLog]
      omega
    have hWindow :=
      (rootQuotientMinimumCompositeMacroCount_eq_one_iff_primeFour_window
        (r := r) (N := N) (h := h)
        hr hN hBinary hLThree (by omega)).1 hMuOne
    have hSepFour : SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourBasis N) :=
      (primeFourBasis_separates_iff_horizon_le hr hN hBinary).2 hWindow.1
    have hUpper :=
      (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
        hr hN hBinary).1 hSepFour
    exact ⟨hLower, hUpper⟩
  · rintro ⟨hLower, hUpper⟩
    exact minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
      hr hh hBinary hLower hUpper

/-- Exact characterization of the first two-macro mixed phase, conditional on
remaining below the triadic shell. -/
theorem minimumCompositeMacroCount_eq_two_iff_second_mixed_band
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hTriadic : N < 3 ^ (h + 1)) :
    rootQuotientMinimumCompositeMacroCount r N h = 2 ↔
      2 * 3 ^ h ≤ N := by
  constructor
  · intro hMuTwo
    by_contra hNot
    have hUpperOne : N < 2 * 3 ^ h := by omega
    by_cases hPrimeOnly : N < 2 ^ (h + 1)
    · have hZero := minimumCompositeMacroCount_eq_zero_of_stateBound_lt_two_pow_succ
        hr hN hBinary hPrimeOnly
      rw [hMuTwo] at hZero
      omega
    · have hOne := minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
        hr hh hBinary (by omega) hUpperOne
      rw [hMuTwo] at hOne
      omega
  · intro hLower
    exact minimumCompositeMacroCount_eq_two_of_two_three_wedge
      hr hh hBinary hLower hTriadic

/-- Exact mixed-overhead phase switch inside the directional-demand-one band.

Pure direction demand stays fixed at one throughout
`2^(h+1)<=N<3^(h+1)`, while mixed overhead is zero below `2*3^h` and exactly
one at or above it. -/
theorem mixedDirectionMacroOverhead_eq_zero_or_one_in_first_directional_band
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 ^ (h + 1) ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientMixedDirectionMacroOverhead r N h =
      if N < 2 * 3 ^ h then 0 else 1 := by
  have hDir : rootQuotientPrimeDirectionDemand N h = 1 :=
    primeDirectionDemand_eq_one_of_two_pow_le_of_lt_three_pow hLower hUpper
  by_cases hBelow : N < 2 * 3 ^ h
  · have hMu : rootQuotientMinimumCompositeMacroCount r N h = 1 :=
      minimumCompositeMacroCount_eq_one_of_two_pow_le_of_lt_two_mul_three_pow
        hr hh hBinary hLower hBelow
    simp [rootQuotientMixedDirectionMacroOverhead, hDir, hMu, hBelow]
  · have hMu : rootQuotientMinimumCompositeMacroCount r N h = 2 :=
      minimumCompositeMacroCount_eq_two_of_two_three_wedge
        hr hh hBinary (by omega) hUpper
    simp [rootQuotientMixedDirectionMacroOverhead, hDir, hMu, hBelow]

end EnterpriseMath.Quotient
