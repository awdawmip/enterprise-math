import EnterpriseMath.Quotient.RootQuotientPrimeShellClosedForm
import EnterpriseMath.Quotient.RootQuotientPrimeShellPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact recurrence of the abstract shell minima. -/
theorem rootQuotientPrimeShellMinimum_succ
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r (k + 1) =
      rootQuotientPrimeShellMinimum r k *
        Nat.nth Nat.Prime (k / (r - 1)) := by
  rw [rootQuotientPrimeShellMinimum_eq_closedForm hr,
    rootQuotientPrimeShellMinimum_eq_closedForm hr,
    rootQuotientPrimeShellClosedForm_succ hr]

/-- Explicit prime-packing interval for the exact prime-only horizon. -/
theorem rootQuotientPrimeHorizon_eq_iff_closedForm_interval
    {r N k : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    rootQuotientPrimeHorizon r N = k ↔
      rootQuotientPrimeShellClosedForm r k ≤ N ∧
      N < rootQuotientPrimeShellClosedForm r (k + 1) := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (rootQuotientPrimeHorizon_eq_iff_shell_interval
      (r := r) (N := N) (k := k) hr hN)

/-- Explicit state-domain threshold for the bounded prime compiler. -/
theorem rootQuotientPrimeBasis_separates_iff_state_lt_closedForm_nextShell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) ↔
      N < rootQuotientPrimeShellClosedForm r (h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (rootQuotientPrimeBasis_separates_iff_state_lt_nextShell
      (r := r) (N := N) (h := h) hr hN)

/-- Explicit fixed-horizon least-presentation threshold for `h>=2`. -/
theorem exists_least_separating_rootQuotientAlphabet_iff_state_lt_closedForm_nextShell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      N < rootQuotientPrimeShellClosedForm r (h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (exists_least_separating_rootQuotientAlphabet_iff_state_lt_nextShell
      (r := r) (N := N) (h := h) hr hN hh)

/-- Explicit complementary no-least threshold. -/
theorem no_least_separating_rootQuotientAlphabet_iff_closedForm_nextShell_le_state
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      rootQuotientPrimeShellClosedForm r (h + 1) ≤ N := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (no_least_separating_rootQuotientAlphabet_iff_nextShell_le_state
      (r := r) (N := N) (h := h) hr hN hh)

/-- Explicit state-domain feasibility threshold for arbitrary factor-capacity
`k` and word horizon `h`. -/
theorem exists_rootQuotientSeparatorWithFactorCapacity_iff_state_lt_closedFormShell
    {r N k h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    ExistsRootQuotientSeparatorWithFactorCapacity r N h k ↔
      N < rootQuotientPrimeShellClosedForm r (k * h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (exists_rootQuotientSeparatorWithFactorCapacity_iff_state_lt_nextShell
      (r := r) (N := N) (k := k) (h := h) hr hN hkPos)

/-- The canonical Omega-filtered compiler realizes the explicit prime-packing
capacity/depth threshold. -/
theorem rootQuotientOmegaFilteredBasis_separates_iff_state_lt_closedFormShell
    {r N k h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis r N k) ↔
      N < rootQuotientPrimeShellClosedForm r (k * h + 1) := by
  simpa [rootQuotientPrimeShellMinimum_eq_closedForm hr] using
    (rootQuotientOmegaFilteredBasis_separates_iff_state_lt_nextShell
      (r := r) (N := N) (k := k) (h := h) hr hN hkPos)

end EnterpriseMath.Quotient
