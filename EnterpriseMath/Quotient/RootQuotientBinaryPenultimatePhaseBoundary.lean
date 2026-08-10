import EnterpriseMath.Quotient.RootQuotientBinaryOneMacroFrontier
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Inside one binary dyadic shell, the exact one-macro horizon equals the
penultimate prime horizon exactly after the secondary threshold
`2*3^(L-2)` is reached. -/
theorem primeFourHorizon_eq_penultimate_iff_secondary_threshold
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientPrimeFourHorizon N =
        rootQuotientPrimeHorizon r N - 1 ↔
      2 * 3 ^ (rootQuotientPrimeHorizon r N - 2) ≤ N := by
  let L := rootQuotientPrimeHorizon r N
  let H := rootQuotientPrimeFourHorizon N
  have hHLe : H ≤ L - 1 := by
    dsimp [H, L]
    exact rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
      hr hN hBinary hLThree
  have hLTwo : 1 ≤ L - 2 := by omega
  constructor
  · intro hEq
    by_contra hNot
    have hStateLt : N < 2 * 3 ^ (L - 2) := by omega
    have hSepEarlier : SeparatesRootQuotientWordsUpTo
        r N (L - 2) (RootQuotientPrimeFourBasis N) :=
      (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
        (r := r) (N := N) (h := L - 2) hr hN hBinary).2 hStateLt
    have hHLeEarlier : H ≤ L - 2 := by
      dsimp [H]
      exact rootQuotientPrimeFourHorizon_minimal
        hr hN hBinary hSepEarlier
    rw [hEq] at hHLeEarlier
    omega
  · intro hThreshold
    apply Nat.le_antisymm hHLe
    by_contra hNot
    have hHLeEarlier : H ≤ L - 2 := by omega
    have hSepEarlier : SeparatesRootQuotientWordsUpTo
        r N (L - 2) (RootQuotientPrimeFourBasis N) := by
      dsimp [H] at hHLeEarlier
      exact (primeFourBasis_separates_iff_horizon_le
        (r := r) (N := N) (h := L - 2) hr hN hBinary).2 hHLeEarlier
    have hStateLt : N < 2 * 3 ^ (L - 2) :=
      (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
        (r := r) (N := N) (h := L - 2) hr hN hBinary).1 hSepEarlier
    omega

/-- Exact binary penultimate Pareto phase boundary.

Within a fixed prime-depth shell `L>=3`, the penultimate execution horizon is
an actual optional-macro Pareto point iff the state bound has crossed
`2*3^(L-2)`.  Below this secondary threshold the single macro `4` already
achieves depth at most `L-2`, so `L-1` is dominated. -/
theorem binary_penultimate_pareto_active_iff_secondary_threshold
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    (∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m =
        rootQuotientPrimeHorizon r N - 1) ↔
      2 * 3 ^ (rootQuotientPrimeHorizon r N - 2) ≤ N := by
  rw [binary_penultimate_pareto_active_iff_primeFourHorizon_eq_penultimate
    hr hN hBinary hLThree]
  exact primeFourHorizon_eq_penultimate_iff_secondary_threshold
    hr hN hBinary hLThree

/-- Complementary dominated region: below the secondary threshold, the
penultimate horizon is not optimal for any optional-macro budget. -/
theorem binary_penultimate_pareto_inactive_iff_below_secondary_threshold
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    (¬∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m =
        rootQuotientPrimeHorizon r N - 1) ↔
      N < 2 * 3 ^ (rootQuotientPrimeHorizon r N - 2) := by
  rw [not_congr
    (binary_penultimate_pareto_active_iff_secondary_threshold
      hr hN hBinary hLThree)]
  omega

end EnterpriseMath.Quotient
