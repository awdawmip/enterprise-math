import EnterpriseMath.Quotient.RootQuotientPrimeShellBinary
import EnterpriseMath.Quotient.RootQuotientPrimeShellClosedFormPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- For squarefree semantics (`r=2`), the rank-`k` shell minimum is exactly the
product of the first `k` primes.  Thus the shell staircase is the primorial
staircase. -/
theorem rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct
    (k : ℕ) :
    rootQuotientPrimeShellMinimum 2 k = rootQuotientPrimePrefixProduct k := by
  rw [rootQuotientPrimeShellMinimum_closedForm (r := 2) (k := k) (by omega)]
  simp [rootQuotientPrimePrefixProduct]

/-- Squarefree exact prime-horizon intervals are consecutive primorial
intervals. -/
theorem rootQuotientPrimeHorizon_squarefree_eq_iff_primorial_interval
    {N k : ℕ}
    (hN : 1 ≤ N) :
    rootQuotientPrimeHorizon 2 N = k ↔
      rootQuotientPrimePrefixProduct k ≤ N ∧
      N < rootQuotientPrimePrefixProduct (k + 1) := by
  simpa [rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct] using
    (rootQuotientPrimeHorizon_eq_iff_shell_interval
      (r := 2) (N := N) (k := k) (by omega) hN)

/-- In squarefree semantics, the prime ISA separates at horizon `h` exactly
below the next primorial threshold. -/
theorem rootQuotientPrimeBasis_squarefree_separates_iff_state_lt_nextPrimorial
    {N h : ℕ}
    (hN : 1 ≤ N) :
    SeparatesRootQuotientWordsUpTo 2 N h (RootQuotientPrimeBasis N) ↔
      N < rootQuotientPrimePrefixProduct (h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct] using
    (rootQuotientPrimeBasis_separates_iff_state_lt_nextShell
      (r := 2) (N := N) (h := h) (by omega) hN)

/-- In squarefree semantics and horizon at least two, a least primitive
presentation exists exactly below the next primorial threshold. -/
theorem exists_least_squarefree_iff_state_lt_nextPrimorial
    {N h : ℕ}
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet 2 N h G) ↔
      N < rootQuotientPrimePrefixProduct (h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct] using
    (exists_least_separating_rootQuotientAlphabet_iff_state_lt_nextShell
      (r := 2) (N := N) (h := h) (by omega) hN hh)

/-- High-root specialization: below rank `r`, the general capped-prime shell
formula collapses to powers of two. -/
theorem rootQuotientPrimeShellMinimum_highRoot_eq_twoPow
    {r k : ℕ}
    (hr : 2 ≤ r)
    (hk : k < r) :
    rootQuotientPrimeShellMinimum r k = 2 ^ k :=
  rootQuotientPrimeShellMinimum_eq_two_pow_of_lt_rootOrder hr hk

/-- The general shell family interpolates between two classical extremes:
primorial thresholds at root order two, and powers of two while the requested
rank is below the root order. -/
theorem rootQuotientPrimeShell_extreme_specializations
    {r k : ℕ}
    (hr : 2 ≤ r)
    (hk : k < r) :
    rootQuotientPrimeShellMinimum 2 k = rootQuotientPrimePrefixProduct k ∧
    rootQuotientPrimeShellMinimum r k = 2 ^ k := by
  exact ⟨rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct k,
    rootQuotientPrimeShellMinimum_eq_two_pow_of_lt_rootOrder hr hk⟩

end EnterpriseMath.Quotient
