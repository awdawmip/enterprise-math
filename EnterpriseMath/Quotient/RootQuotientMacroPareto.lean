import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import EnterpriseMath.Quotient.RootQuotientParetoPhases
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The optional-composite-macro requirement is nonincreasing in execution
horizon.  The forced prime core is constant, so all genuine storage variation
lives in this macro count. -/
theorem rootQuotientMinimumCompositeMacroCount_anti_horizon
    {r N h j : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hhj : h ≤ j) :
    rootQuotientMinimumCompositeMacroCount r N j ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  have hj : 1 ≤ j := hh.trans hhj
  have hStorageMono :=
    rootQuotientMinimumStorageSize_anti_horizon
      (r := r) (N := N) (h := h) (j := j)
      (by omega) hh hhj
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh] at hStorageMono
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hj] at hStorageMono
  omega

/-- Minimum execution horizon as a function of *optional macro budget* rather
than total dictionary size.  The mandatory bounded-prime core is supplied for
free in this coordinate system. -/
def rootQuotientMinimumHorizonAtCompositeMacroBudget
    (r N m : ℕ) : ℕ :=
  rootQuotientMinimumHorizonAtStorage
    r N ((RootQuotientPrimeBasis N).ncard + m)

/-- Exact macro-budget phase interval.

For `h>=2`, the minimum attainable horizon with `m` optional composite macro
types is exactly `h` iff `m` lies between the macro requirements at consecutive
horizons:

`D_macro(m)=h  <->  mu(h)<=m<mu(h-1)`.

This is the forced-core-free form of the true storage/depth Pareto frontier. -/
theorem rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N m = h ↔
      rootQuotientMinimumCompositeMacroCount r N h ≤ m ∧
      m < rootQuotientMinimumCompositeMacroCount r N (h - 1) := by
  let p := (RootQuotientPrimeBasis N).ncard
  have hPrimeBudget : p ≤ p + m := Nat.le_add_right _ _
  have hPareto :=
    rootQuotientMinimumHorizonAtStorage_eq_iff_budget_interval
      (r := r) (N := N) (s := p + m) (h := h)
      hr hPrimeBudget hh
  have hhPos : 1 ≤ h := by omega
  have hPredPos : 1 ≤ h - 1 := by omega
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hhPos] at hPareto
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hPredPos] at hPareto
  dsimp [rootQuotientMinimumHorizonAtCompositeMacroBudget, p]
  simpa only [Nat.add_le_add_iff_left, Nat.add_lt_add_iff_left] using hPareto

/-- A horizon `h>=2` is Pareto-active exactly when the minimum optional macro
count strictly decreases from `h-1` to `h`. -/
theorem exists_macroBudget_with_minimumHorizon_eq_iff_macro_strict_drop
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m = h) ↔
      rootQuotientMinimumCompositeMacroCount r N h <
        rootQuotientMinimumCompositeMacroCount r N (h - 1) := by
  constructor
  · rintro ⟨m, hm⟩
    have hInterval :=
      (rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
        (r := r) (N := N) (m := m) (h := h) hr hh).1 hm
    exact hInterval.1.trans_lt hInterval.2
  · intro hDrop
    let m := rootQuotientMinimumCompositeMacroCount r N h
    refine ⟨m, ?_⟩
    exact
      (rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
        (r := r) (N := N) (m := m) (h := h) hr hh).2
        ⟨le_rfl, hDrop⟩

/-- Macro-count plateaus are exactly Pareto-inactive horizons. -/
theorem no_macroBudget_has_minimumHorizon_of_macro_plateau
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hPlateau :
      rootQuotientMinimumCompositeMacroCount r N h =
        rootQuotientMinimumCompositeMacroCount r N (h - 1)) :
    ¬∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m = h := by
  intro hExists
  have hDrop :=
    (exists_macroBudget_with_minimumHorizon_eq_iff_macro_strict_drop
      (r := r) (N := N) (h := h) hr hh).1 hExists
  rw [hPlateau] at hDrop
  exact (lt_irrefl _ hDrop)

/-- With zero optional macro budget, the minimum positive horizon is the exact
prime-only horizon whenever that horizon is positive. -/
theorem rootQuotientMinimumHorizonAtCompositeMacroBudget_zero_eq_primeHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 0 =
      rootQuotientPrimeHorizon r N := by
  simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget] using
    rootQuotientMinimumHorizonAtStorage_primeBudget_eq_primeHorizon
      (r := r) (N := N) hr hLPos

/-- At the penultimate horizon, the macro requirement is exactly the semantic
semiprime divisor-cover number. -/
theorem rootQuotientMinimumCompositeMacroCount_penultimate_eq_tau
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeHorizon r N - 1) =
      rootQuotientPenultimateSemiprimeCoverNumber r N :=
  rootQuotientMinimumCompositeMacroCount_penultimate_eq_semiprimeCoverNumber
    hr hHorizon

/-- For `L_r(N)>=3`, the penultimate horizon is an actual Pareto phase iff the
semiprime cover number is strictly smaller than the macro requirement one step
further down the execution ladder.

If equality holds, the penultimate set-cover solution is still correct at
`L-1`, but that horizon is Pareto-inactive because the same macro budget already
achieves `L-2`. -/
theorem penultimate_horizon_pareto_active_iff_tau_lt_previous_macro_requirement
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    (∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m =
        rootQuotientPrimeHorizon r N - 1) ↔
      rootQuotientPenultimateSemiprimeCoverNumber r N <
        rootQuotientMinimumCompositeMacroCount
          r N (rootQuotientPrimeHorizon r N - 2) := by
  let L := rootQuotientPrimeHorizon r N
  have hPenTwo : 2 ≤ L - 1 := by omega
  have hActive :=
    exists_macroBudget_with_minimumHorizon_eq_iff_macro_strict_drop
      (r := r) (N := N) (h := L - 1) hr hPenTwo
  have hPenTau :=
    rootQuotientMinimumCompositeMacroCount_penultimate_eq_semiprimeCoverNumber
      (r := r) (N := N) hr (by omega)
  rw [show (L - 1) - 1 = L - 2 by omega] at hActive
  rw [hPenTau] at hActive
  simpa [L] using hActive

end EnterpriseMath.Quotient
