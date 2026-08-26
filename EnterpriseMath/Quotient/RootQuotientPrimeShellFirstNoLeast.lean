import EnterpriseMath.Quotient.RootQuotientPrimeShellClosedFormPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Rank-three shell threshold for squarefree semantics (`r=2`). -/
theorem rootQuotientPrimeShellClosedForm_two_three :
    rootQuotientPrimeShellClosedForm 2 3 = 30 := by
  norm_num [rootQuotientPrimeShellClosedForm,
    rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix]

/-- Rank-three shell threshold for cube-free semantics (`r=3`). -/
theorem rootQuotientPrimeShellClosedForm_three_three :
    rootQuotientPrimeShellClosedForm 3 3 = 12 := by
  norm_num [rootQuotientPrimeShellClosedForm,
    rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix]

/-- From root order four onward, the first rank-three shell is simply `2^3=8`. -/
theorem rootQuotientPrimeShellClosedForm_three_eq_eight_of_four_le
    {r : ℕ}
    (hr : 4 ≤ r) :
    rootQuotientPrimeShellClosedForm r 3 = 8 := by
  by_cases hrFour : r = 4
  · subst r
    norm_num [rootQuotientPrimeShellClosedForm,
      rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix]
  · have hLarge : 3 < r - 1 := by omega
    simp [rootQuotientPrimeShellClosedForm,
      Nat.div_eq_of_lt hLarge, Nat.mod_eq_of_lt hLarge,
      rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix]

/-- At horizon two, squarefree (`r=2`) exact separation has no inclusion-least
primitive alphabet exactly from state bound 30 onward. -/
theorem no_least_at_two_iff_thirty_le_state_squarefree
    {N : ℕ}
    (hN : 1 ≤ N) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet 2 N 2 G) ↔
      30 ≤ N := by
  simpa [rootQuotientPrimeShellClosedForm_two_three] using
    (no_least_separating_rootQuotientAlphabet_iff_closedForm_nextShell_le_state
      (r := 2) (N := N) (h := 2) (by omega) hN (by omega))

/-- At horizon two, cube-free (`r=3`) exact separation has no inclusion-least
primitive alphabet exactly from state bound 12 onward. -/
theorem no_least_at_two_iff_twelve_le_state_cubeFree
    {N : ℕ}
    (hN : 1 ≤ N) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet 3 N 2 G) ↔
      12 ≤ N := by
  simpa [rootQuotientPrimeShellClosedForm_three_three] using
    (no_least_separating_rootQuotientAlphabet_iff_closedForm_nextShell_le_state
      (r := 3) (N := N) (h := 2) (by omega) hN (by omega))

/-- At horizon two, every root order at least four enters the no-least phase
exactly when the state bound reaches eight. -/
theorem no_least_at_two_iff_eight_le_state_of_four_le_root
    {r N : ℕ}
    (hr : 4 ≤ r)
    (hN : 1 ≤ N) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N 2 G) ↔
      8 ≤ N := by
  have hClosed : rootQuotientPrimeShellClosedForm r 3 = 8 :=
    rootQuotientPrimeShellClosedForm_three_eq_eight_of_four_le hr
  simpa [hClosed] using
    (no_least_separating_rootQuotientAlphabet_iff_closedForm_nextShell_le_state
      (r := r) (N := N) (h := 2) (by omega) hN (by omega))

end EnterpriseMath.Quotient
