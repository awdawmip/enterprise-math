import EnterpriseMath.Quotient.RootQuotientPrimeShellFirstNoLeast
import EnterpriseMath.Quotient.RootQuotientPrimeShellSpecializations
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- State-bound onset of the no-least fixed-horizon phase.

At word horizon `h>=2`, the inclusion-least primitive presentation disappears
exactly when `N` reaches this boundary. -/
noncomputable def rootQuotientLeastPhaseBoundary (r h : ℕ) : ℕ :=
  rootQuotientPrimeShellMinimum r (h + 1)

/-- Exact least/no-least threshold in boundary notation. -/
theorem no_least_separating_iff_phaseBoundary_le_state
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      rootQuotientLeastPhaseBoundary r h ≤ N := by
  simpa [rootQuotientLeastPhaseBoundary] using
    (no_least_separating_rootQuotientAlphabet_iff_nextShell_le_state
      (r := r) (N := N) (h := h) hr hN hh)

/-- More execution depth postpones the no-least onset strictly to larger state
bounds. -/
theorem rootQuotientLeastPhaseBoundary_strictMono_horizon
    {r : ℕ}
    (hr : 2 ≤ r) :
    StrictMono (rootQuotientLeastPhaseBoundary r) := by
  intro h j hhj
  dsimp [rootQuotientLeastPhaseBoundary]
  exact (rootQuotientPrimeShellMinimum_strictMono hr)
    (Nat.add_lt_add_right hhj 1)

/-- Increasing root order enlarges the semantic power-free set, so for fixed
execution horizon the no-least onset can only move earlier (or stay fixed). -/
theorem rootQuotientLeastPhaseBoundary_anti_rootOrder
    {r s h : ℕ}
    (hr : 2 ≤ r)
    (hrs : r ≤ s) :
    rootQuotientLeastPhaseBoundary s h ≤
      rootQuotientLeastPhaseBoundary r h := by
  exact rootQuotientPrimeShellMinimum_anti_rootOrder hr hrs

/-- Squarefree (`r=2`) phase boundaries are the next primorials. -/
theorem rootQuotientLeastPhaseBoundary_squarefree_eq_nextPrimorial
    (h : ℕ) :
    rootQuotientLeastPhaseBoundary 2 h =
      rootQuotientPrimePrefixProduct (h + 1) := by
  exact rootQuotientPrimeShellMinimum_squarefree_eq_primePrefixProduct (h + 1)

/-- Once the root order exceeds `h+1`, the fixed-horizon phase boundary has
stabilized to the binary value `2^(h+1)`. -/
theorem rootQuotientLeastPhaseBoundary_eq_twoPow_of_horizon_lt_root
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hh : h + 1 < r) :
    rootQuotientLeastPhaseBoundary r h = 2 ^ (h + 1) := by
  exact rootQuotientPrimeShellMinimum_eq_two_pow_of_lt_rootOrder hr hh

/-- Boundary sandwich: every root order at least two enters the no-least phase
no later than squarefree semantics, while the universal factor-size bound gives
`2^(h+1)` as the earliest possible onset. -/
theorem rootQuotientLeastPhaseBoundary_between_twoPow_and_primorial
    {r h : ℕ}
    (hr : 2 ≤ r) :
    2 ^ (h + 1) ≤ rootQuotientLeastPhaseBoundary r h ∧
    rootQuotientLeastPhaseBoundary r h ≤
      rootQuotientPrimePrefixProduct (h + 1) := by
  constructor
  · exact pow_two_le_rootQuotientPrimeShellMinimum hr
  · calc
      rootQuotientLeastPhaseBoundary r h ≤
          rootQuotientLeastPhaseBoundary 2 h :=
        rootQuotientLeastPhaseBoundary_anti_rootOrder (by omega) hr
      _ = rootQuotientPrimePrefixProduct (h + 1) :=
        rootQuotientLeastPhaseBoundary_squarefree_eq_nextPrimorial h

/-- First no-least boundary at horizon two, in one compact phase statement. -/
theorem rootQuotientLeastPhaseBoundary_two_explicit
    {r : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientLeastPhaseBoundary r 2 =
      if r = 2 then 30 else if r = 3 then 12 else 8 := by
  by_cases hrTwo : r = 2
  · subst r
    simp [rootQuotientLeastPhaseBoundary,
      rootQuotientPrimeShellMinimum_eq_closedForm (r := 2) (k := 3) (by omega),
      rootQuotientPrimeShellClosedForm_two_three]
  · by_cases hrThree : r = 3
    · subst r
      simp [rootQuotientLeastPhaseBoundary,
        rootQuotientPrimeShellMinimum_eq_closedForm (r := 3) (k := 3) (by omega),
        rootQuotientPrimeShellClosedForm_three_three]
    · have hrFour : 4 ≤ r := by omega
      have hEight :=
        rootQuotientPrimeShellClosedForm_three_eq_eight_of_four_le hrFour
      rw [rootQuotientLeastPhaseBoundary,
        rootQuotientPrimeShellMinimum_eq_closedForm hr]
      simp [hrTwo, hrThree, hEight]

end EnterpriseMath.Quotient
