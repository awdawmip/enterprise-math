import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import EnterpriseMath.Quotient.RootQuotientBinaryOneMacroFrontier
import EnterpriseMath.Quotient.RootQuotientPrimeShellBinary
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- In the wedge

`2 * 3^h <= N < 3^(h+1)`

with `h>=2`, the pure-prime-direction storage demand is exactly one.

The upper threshold says the second prime direction (`3`) is not yet hard,
while the lower threshold already places `2^(h+1)` in the state domain, so the
first prime direction (`2`) is hard. -/
theorem primeDirectionDemand_eq_one_of_two_three_wedge
    {N h : ℕ}
    (hh : 2 ≤ h)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    rootQuotientPrimeDirectionDemand N h = 1 := by
  have hUpperDemand : rootQuotientPrimeDirectionDemand N h ≤ 1 := by
    apply
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 1)).2
    simpa [rootQuotientStablePrimeBase] using hUpper
  have hTwoPowLeThreePow : 2 ^ h ≤ 3 ^ h :=
    Nat.pow_le_pow_left (by omega) h
  have hTwoPowSuccLeN : 2 ^ (h + 1) ≤ N := by
    have hScaled : 2 ^ h * 2 ≤ 3 ^ h * 2 :=
      Nat.mul_le_mul_right 2 hTwoPowLeThreePow
    rw [pow_succ]
    exact hScaled.trans (by simpa [Nat.mul_comm] using hLower)
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

/-- The same wedge lies strictly below the exact one-macro horizon.

Macro `4` separates at horizon `h` exactly below `2*3^h`; therefore the lower
edge of the wedge is already beyond the one-macro feasible state range. -/
theorem horizon_lt_primeFourHorizon_of_two_mul_three_pow_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N) :
    h < rootQuotientPrimeFourHorizon N := by
  by_contra hNot
  have hHLe : rootQuotientPrimeFourHorizon N ≤ h := by omega
  have hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeFourBasis N) :=
    (primeFourBasis_separates_iff_horizon_le hr hN hBinary).2 hHLe
  have hStateLt :=
    (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
      hr hN hBinary).1 hSep
  omega

/-- In the mixed wedge, one optional macro is genuinely insufficient.

Although pure prime directions force only one macro type, the mixed-direction
hard boundary represented by the prime-plus-four shell still forces a second
macro type. -/
theorem two_le_minimumCompositeMacroCount_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (_hUpper : N < 3 ^ (h + 1)) :
    2 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  have hN : 2 ≤ N := by
    have hPowPos : 1 ≤ 3 ^ h := by positivity
    omega
  have hThreePow : 3 ^ 2 ≤ 3 ^ h :=
    Nat.pow_le_pow_right (by omega) hh
  have hEightLe : 2 ^ 3 ≤ N := by
    norm_num at hThreePow ⊢
    omega
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
      hr (by omega) hBinary
  have hLogThree : 3 ≤ Nat.log 2 N :=
    Nat.le_log_of_pow_le (by omega) hEightLe
  have hLThree : 3 ≤ rootQuotientPrimeHorizon r N := by
    rw [hLog]
    exact hLogThree
  have hLtH : h < rootQuotientPrimeFourHorizon N :=
    horizon_lt_primeFourHorizon_of_two_mul_three_pow_le
      hr hN hBinary hLower
  exact two_le_rootQuotientMinimumCompositeMacroCount_of_lt_primeFourHorizon
    hr hN hBinary hLThree (by omega) hLtH

/-- **Strict mixed-direction obstruction phase.**

Inside the wedge

`2*3^h <= N < 3^(h+1)`

for `h>=2`, pure directions demand exactly one optional macro but the true
minimum requires at least two.  Hence the mixed-direction storage overhead is
strictly positive. -/
theorem one_le_mixedDirectionMacroOverhead_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    1 ≤ rootQuotientMixedDirectionMacroOverhead r N h := by
  have hDir : rootQuotientPrimeDirectionDemand N h = 1 :=
    primeDirectionDemand_eq_one_of_two_three_wedge hh hLower hUpper
  have hMu : 2 ≤ rootQuotientMinimumCompositeMacroCount r N h :=
    two_le_minimumCompositeMacroCount_of_two_three_wedge
      hr hh hBinary hLower hUpper
  dsimp [rootQuotientMixedDirectionMacroOverhead]
  rw [hDir]
  omega

/-- The mixed wedge therefore yields a strict total-storage strengthening over
the pure-direction prime-counting floor. -/
theorem prime_add_directionDemand_add_one_le_minimumStorage_of_two_three_wedge
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r)
    (hLower : 2 * 3 ^ h ≤ N)
    (hUpper : N < 3 ^ (h + 1)) :
    (RootQuotientPrimeBasis N).ncard +
        rootQuotientPrimeDirectionDemand N h + 1 ≤
      rootQuotientMinimumStorageSize r N h := by
  have hMix := one_le_mixedDirectionMacroOverhead_of_two_three_wedge
    hr hh hBinary hLower hUpper
  rw [minimumStorage_eq_prime_add_directionDemand_add_mixedOverhead
    hr (by omega) hBinary]
  omega

end EnterpriseMath.Quotient
