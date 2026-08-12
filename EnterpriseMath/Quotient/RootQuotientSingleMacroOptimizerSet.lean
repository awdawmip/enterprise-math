import EnterpriseMath.Quotient.RootQuotientBinaryOneMacroFrontier
import EnterpriseMath.Quotient.RootQuotientSingleMacroClassification
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Complete optimizer-set criterion for one composite semantic macro in the
binary/high-root regime.

Assume the prime-only horizon is at least three, so one macro gives a genuine
strict speedup.  A composite semantic macro `g` attains the globally optimal
one-macro horizon `H4` iff it is a power of two `2^m`, `m>=2`, and the state
bound lies strictly below the generalized `2^m` hard shell at cost `H4+1`.

Thus all ties with macro `4` are explicitly parameterized by the power-of-two
shell geometry. -/
theorem singleCompositeMacro_separates_at_primeFourHorizon_iff_twoPower_shell
    {r N g : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeFourHorizon N)
        (RootQuotientPrimeSingleMacroBasis N g) ↔
      ∃ m : ℕ,
        2 ≤ m ∧
        g = 2 ^ m ∧
        N < rootQuotientPrimeTwoPowerShellMinimumCandidate
          m (rootQuotientPrimeFourHorizon N + 1) := by
  constructor
  · intro hSep
    have hHLePen :=
      rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
        hr hN hBinary hLThree
    have hFast : rootQuotientPrimeFourHorizon N <
        rootQuotientPrimeHorizon r N := by omega
    obtain ⟨m, hm, hgEq⟩ :=
      exists_twoPower_macro_of_singleCompositeMacro_strict_speedup
        hr hN hBinary hgSemantic hgRank hSep hFast
    refine ⟨m, hm, hgEq, ?_⟩
    have hSepM : SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeFourHorizon N)
        (RootQuotientPrimeTwoPowerBasis N m) := by
      simpa [RootQuotientPrimeSingleMacroBasis,
        RootQuotientPrimeTwoPowerBasis, hgEq] using hSep
    exact
      (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
        (r := r) (N := N) (m := m)
        (h := rootQuotientPrimeFourHorizon N)
        hr hm hN hBinary).1 hSepM
  · rintro ⟨m, hm, hgEq, hShell⟩
    have hSepM : SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeFourHorizon N)
        (RootQuotientPrimeTwoPowerBasis N m) :=
      (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
        (r := r) (N := N) (m := m)
        (h := rootQuotientPrimeFourHorizon N)
        hr hm hN hBinary).2 hShell
    simpa [RootQuotientPrimeSingleMacroBasis,
      RootQuotientPrimeTwoPowerBasis, hgEq] using hSepM

/-- Every globally depth-optimal single composite semantic macro is a power of
two. -/
theorem exists_twoPower_of_singleCompositeMacro_depthOptimal
    {r N g : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g)
    (hOptimal : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeFourHorizon N)
      (RootQuotientPrimeSingleMacroBasis N g)) :
    ∃ m : ℕ, 2 ≤ m ∧ g = 2 ^ m := by
  have hCriterion :=
    (singleCompositeMacro_separates_at_primeFourHorizon_iff_twoPower_shell
      hr hN hBinary hLThree hgSemantic hgRank).1 hOptimal
  obtain ⟨m, hm, hgEq, _⟩ := hCriterion
  exact ⟨m, hm, hgEq⟩

/-- Equivalent closed-horizon criterion for a power-of-two macro to tie with
macro `4`. -/
theorem primeTwoPowerMacro_depthOptimal_iff_horizon_eq_primeFour
    {r N m : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeFourHorizon N)
        (RootQuotientPrimeTwoPowerBasis N m) ↔
      rootQuotientPrimeTwoPowerHorizon m N =
        rootQuotientPrimeFourHorizon N := by
  constructor
  · intro hSep
    have hMLe : rootQuotientPrimeTwoPowerHorizon m N ≤
        rootQuotientPrimeFourHorizon N :=
      (primeTwoPowerBasis_separates_iff_closedHorizon_le
        hr hm hN hBinary).1 hSep
    have hFourLe := rootQuotientPrimeFourHorizon_le_primeTwoPowerHorizon
      hr hm hN hBinary
    exact Nat.le_antisymm hMLe hFourLe
  · intro hEq
    exact
      (primeTwoPowerBasis_separates_iff_closedHorizon_le
        hr hm hN hBinary).2 hEq.le

/-- Hard-shell form and closed-horizon form of the optimizer criterion agree. -/
theorem primeTwoPowerMacro_depthOptimal_iff_nextShell_above_stateBound
    {r N m : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeTwoPowerHorizon m N =
        rootQuotientPrimeFourHorizon N ↔
      N < rootQuotientPrimeTwoPowerShellMinimumCandidate
        m (rootQuotientPrimeFourHorizon N + 1) := by
  rw [← primeTwoPowerMacro_depthOptimal_iff_horizon_eq_primeFour
    hr hm hN hBinary]
  exact primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
    hr hm hN hBinary

end EnterpriseMath.Quotient
