import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Consecutive abstract power-free prime-rank shell minima are strictly
increasing for every root order at least two.

For positive rank `k`, take the minimum boundary on shell `k+1` and remove
prime-factor tokens down to exact rank `k`.  The resulting power-free divisor is
strictly smaller because its prime-factor count changed.  Rank zero is the
separate base case `M_r(0)=1`. -/
theorem rootQuotientPrimeShellMinimum_lt_succ
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r k <
      rootQuotientPrimeShellMinimum r (k + 1) := by
  have hNextMem :=
    rootQuotientPrimeShellMinimum_mem (r := r) (k := k + 1) hr
  by_cases hkZero : k = 0
  · subst k
    rw [rootQuotientPrimeShellMinimum_zero hr]
    have hNextNeOne : rootQuotientPrimeShellMinimum r 1 ≠ 1 := by
      intro hEq
      have hCount := hNextMem.2.2
      rw [hEq] at hCount
      simp [rootQuotientPrimeFactorCount] at hCount
    omega
  · have hkPos : 1 ≤ k := by omega
    have hkLe :
        k ≤ rootQuotientPrimeFactorCount
          (rootQuotientPrimeShellMinimum r (k + 1)) := by
      rw [hNextMem.2.2]
      omega
    obtain ⟨a, haPos, haDvd, haFree, haCount⟩ :=
      exists_rPowerFree_divisor_with_primeFactorCount
        hNextMem.1 hNextMem.2.1 hkPos hkLe
    have haShell : a ∈ RootQuotientPrimeShell r k :=
      ⟨haPos, haFree, haCount⟩
    have hMinLe : rootQuotientPrimeShellMinimum r k ≤ a :=
      rootQuotientPrimeShellMinimum_le haShell
    have haLe : a ≤ rootQuotientPrimeShellMinimum r (k + 1) :=
      Nat.le_of_dvd (by omega) haDvd
    have haNe : a ≠ rootQuotientPrimeShellMinimum r (k + 1) := by
      intro hEq
      have hNextCount := hNextMem.2.2
      rw [hEq] at hNextCount
      rw [haCount] at hNextCount
      omega
    exact hMinLe.trans_lt (lt_of_le_of_ne haLe haNe)

/-- The abstract shell-minimum sequence is strictly monotone in rank. -/
theorem rootQuotientPrimeShellMinimum_strictMono
    {r : ℕ}
    (hr : 2 ≤ r) :
    StrictMono (rootQuotientPrimeShellMinimum r) := by
  exact strictMono_nat_of_lt_succ fun k =>
    rootQuotientPrimeShellMinimum_lt_succ (r := r) (k := k) hr

/-- Shell-threshold intervals are nonempty: the lower endpoint itself realizes
its own rank phase. -/
theorem rootQuotientPrimeHorizon_at_shellMinimum
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeHorizon r (rootQuotientPrimeShellMinimum r k) = k := by
  have hMem := rootQuotientPrimeShellMinimum_mem (r := r) (k := k) hr
  apply (rootQuotientPrimeHorizon_eq_iff_shell_interval hr hMem.1).2
  exact ⟨le_rfl, rootQuotientPrimeShellMinimum_lt_succ hr⟩

/-- The abstract shell minimum is exactly the first state bound at which the
prime-only horizon reaches rank `k`. -/
theorem rootQuotientPrimeShellMinimum_is_first_rank_state
    {r k N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    rootQuotientPrimeShellMinimum r k ≤ N ↔
      k ≤ rootQuotientPrimeHorizon r N :=
  rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon hr hN

end EnterpriseMath.Quotient
