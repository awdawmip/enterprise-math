import EnterpriseMath.Quotient.RootQuotientCapacityOptimality
import EnterpriseMath.Quotient.RootQuotientLeastPhase
import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact state-domain threshold for the bounded prime compiler.

For `r>=2` and `N>=1`, the prime ISA separates within horizon `h` exactly
before the first power-free shell of rank `h+1` enters the bounded domain. -/
theorem rootQuotientPrimeBasis_separates_iff_state_lt_nextShell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) ↔
      N < rootQuotientPrimeShellMinimum r (h + 1) := by
  rw [rootQuotientPrimeBasis_separates_iff_horizon_le (by omega)]
  constructor
  · intro hHorizon
    by_contra hNot
    have hNext : h + 1 ≤ rootQuotientPrimeHorizon r N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := h + 1) hr hN).1 (by omega)
    omega
  · intro hShell
    by_contra hNot
    have hNext : h + 1 ≤ rootQuotientPrimeHorizon r N := by omega
    have hMin : rootQuotientPrimeShellMinimum r (h + 1) ≤ N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := h + 1) hr hN).2 hNext
    omega

/-- Fixed-horizon least-presentation phase in pure shell-threshold form.

For horizons at least two, a least primitive quotient presentation exists
exactly while the bounded state domain remains below the next rank shell. -/
theorem exists_least_separating_rootQuotientAlphabet_iff_state_lt_nextShell
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      N < rootQuotientPrimeShellMinimum r (h + 1) := by
  rw [exists_least_separating_rootQuotientAlphabet_iff_horizon_le hr hh]
  constructor
  · intro hHorizon
    by_contra hNot
    have hNext : h + 1 ≤ rootQuotientPrimeHorizon r N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := h + 1) hr hN).1 (by omega)
    omega
  · intro hShell
    by_contra hNot
    have hNext : h + 1 ≤ rootQuotientPrimeHorizon r N := by omega
    have hMin : rootQuotientPrimeShellMinimum r (h + 1) ≤ N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := h + 1) hr hN).2 hNext
    omega

/-- Complementary no-least phase in shell coordinates. -/
theorem no_least_separating_rootQuotientAlphabet_iff_nextShell_le_state
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 2 ≤ h) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      rootQuotientPrimeShellMinimum r (h + 1) ≤ N := by
  rw [not_congr
    (exists_least_separating_rootQuotientAlphabet_iff_state_lt_nextShell
      hr hN hh)]
  omega

/-- Exact capacity/depth state-domain threshold.

There exists some positive primitive alphabet of factor capacity at most `k`
separating within horizon `h` iff the bounded domain lies strictly below the
first power-free shell whose rank exceeds the total token budget `k*h`. -/
theorem exists_rootQuotientSeparatorWithFactorCapacity_iff_state_lt_nextShell
    {r N k h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    ExistsRootQuotientSeparatorWithFactorCapacity r N h k ↔
      N < rootQuotientPrimeShellMinimum r (k * h + 1) := by
  rw [exists_rootQuotientSeparatorWithFactorCapacity_iff (by omega) hkPos]
  constructor
  · intro hBudget
    by_contra hNot
    have hNext : k * h + 1 ≤ rootQuotientPrimeHorizon r N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := k * h + 1) hr hN).1 (by omega)
    omega
  · intro hShell
    by_contra hNot
    have hNext : k * h + 1 ≤ rootQuotientPrimeHorizon r N := by omega
    have hMin : rootQuotientPrimeShellMinimum r (k * h + 1) ≤ N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := k * h + 1) hr hN).2 hNext
    omega

/-- The canonical Omega-filtered compiler realizes the same exact shell
threshold as the existential capacity feasibility region. -/
theorem rootQuotientOmegaFilteredBasis_separates_iff_state_lt_nextShell
    {r N k h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis r N k) ↔
      N < rootQuotientPrimeShellMinimum r (k * h + 1) := by
  rw [rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
    (by omega) hkPos]
  constructor
  · intro hBudget
    by_contra hNot
    have hNext : k * h + 1 ≤ rootQuotientPrimeHorizon r N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := k * h + 1) hr hN).1 (by omega)
    omega
  · intro hShell
    by_contra hNot
    have hNext : k * h + 1 ≤ rootQuotientPrimeHorizon r N := by omega
    have hMin : rootQuotientPrimeShellMinimum r (k * h + 1) ≤ N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
        (r := r) (N := N) (k := k * h + 1) hr hN).2 hNext
    omega

end EnterpriseMath.Quotient
