import EnterpriseMath.Quotient.RootQuotientCoarseStableMacroLadder
import EnterpriseMath.Quotient.RootQuotientStableMacroBudgetLowerBound
import EnterpriseMath.Quotient.RootQuotientMacroPareto
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Coarse stable horizon attached to an optional macro budget `s`.

Its leading term is the next-prime logarithm.  The deliberately loose additive
constant `q_s^2` comes from the first proof-friendly canonical macro ladder; it
is independent of the state bound `N`. -/
def rootQuotientCoarseStableMacroHorizon
    (N s : ℕ) : ℕ :=
  rootQuotientStablePrimeBase s * rootQuotientStablePrimeBase s +
    Nat.log (rootQuotientStablePrimeBase s) N

/-- In the high-root regime, the coarse canonical ladder is a valid finite
optional-composite presentation at its named stable horizon. -/
theorem coarseStableMacroSet_is_compositeMacroPresentation
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    RootQuotientCompositeMacroPresentation
      r N (rootQuotientCoarseStableMacroHorizon N s)
      (RootQuotientCoarseStableMacroSet N s) := by
  refine ⟨
    rootQuotientCoarseStableMacroSet_finite N s,
    coarseStableMacroSet_is_compositeMacroFamily hr hBinary,
    ?_⟩
  simpa [rootQuotientCoarseStableMacroHorizon] using
    coarseStableMacroSet_separates_within_square_add_log
      (r := r) (N := N) (s := s) (by omega)

/-- The true optional-macro requirement at the coarse next-prime horizon fits
inside the requested macro budget. -/
theorem minimumCompositeMacroCount_coarseStableHorizon_le_budget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientCoarseStableMacroHorizon N s) ≤ s := by
  have hPresentation :=
    coarseStableMacroSet_is_compositeMacroPresentation
      (r := r) (N := N) (s := s) hr hBinary
  exact (rootQuotientMinimumCompositeMacroCount_le hPresentation).trans
    (rootQuotientCoarseStableMacroSet_ncard_le N s)

/-- Coarse universal upper bound on optimal execution depth under `s` optional
composite macro types.

Together with the independent next-prime obstruction, this already closes the
stable base: the true optimum is at most `q_s^2 + log_{q_s} N`. -/
theorem minimumHorizonAtCompositeMacroBudget_le_coarseStableHorizon
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
      rootQuotientCoarseStableMacroHorizon N s := by
  let H := rootQuotientCoarseStableMacroHorizon N s
  have hqPrime := rootQuotientStablePrimeBase_prime s
  have hHPos : 1 ≤ H := by
    have hSquarePos :
        1 ≤ rootQuotientStablePrimeBase s * rootQuotientStablePrimeBase s :=
      Nat.one_le_mul hqPrime.one_le hqPrime.one_le
    dsimp [H, rootQuotientCoarseStableMacroHorizon]
    omega
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N H ≤ s := by
    dsimp [H]
    exact minimumCompositeMacroCount_coarseStableHorizon_le_budget
      (r := r) (N := N) (s := s) hr hBinary
  have hStorage :
      rootQuotientMinimumStorageSize r N H ≤
        (RootQuotientPrimeBasis N).ncard + s := by
    rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      hr hHPos]
    exact Nat.add_le_add_left hMuLe _
  have hPrimeBudget :
      (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s :=
    Nat.le_add_right _ _
  have hDepth :
      rootQuotientMinimumHorizonAtStorage r N
          ((RootQuotientPrimeBasis N).ncard + s) ≤ H :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N)
      (s := (RootQuotientPrimeBasis N).ncard + s) (h := H)
      hr hPrimeBudget hHPos).2 hStorage
  simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget, H] using hDepth

/-- **Next-prime stable macro-budget law, coarse finite form.**

For every positive bounded domain in the high-root regime, the optimal
execution horizon under `s` optional composite macro types lies in the fixed
additive window

`log_{q_s} N <= D_macro(s) <= q_s^2 + log_{q_s} N`,

where `q_s` is the `(s+1)`-st prime.  The lower bound holds for every possible
`s`-macro presentation; the upper bound is supplied by the explicit coarse
pure-prime-power ladder.

Hence the optimal stable logarithmic base is exactly the next prime `q_s`.
The additive constant `q_s^2` is intentionally non-optimal and can later be
replaced by the sharp residual-slot constant `T_s`. -/
theorem nextPrime_log_macroBudget_sandwich
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r) :
    Nat.log (rootQuotientStablePrimeBase s) N ≤
        rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ∧
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
        rootQuotientCoarseStableMacroHorizon N s := by
  have hPrimeBudget :
      (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s :=
    Nat.le_add_right _ _
  have hDepthPos :
      1 ≤ rootQuotientMinimumHorizonAtCompositeMacroBudget r N s := by
    have hPos :=
      (rootQuotientMinimumHorizonAtStorage_mem
        (r := r) (N := N)
        (s := (RootQuotientPrimeBasis N).ncard + s)
        hr hPrimeBudget).1
    simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget] using hPos
  constructor
  · simpa [rootQuotientStablePrimeBase] using
      nthPrime_log_le_minimumHorizonAtCompositeMacroBudget
        (r := r) (N := N) (s := s)
        hr hN hBinary hDepthPos
  · exact minimumHorizonAtCompositeMacroBudget_le_coarseStableHorizon
      (r := r) (N := N) (s := s) hr hBinary

end EnterpriseMath.Quotient
