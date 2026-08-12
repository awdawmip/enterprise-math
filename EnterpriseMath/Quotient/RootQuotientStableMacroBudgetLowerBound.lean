import EnterpriseMath.Quotient.RootQuotientMacroPareto
import EnterpriseMath.Quotient.RootQuotientStableMacroObstruction
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- True optional-macro frontier lower bound from the next-prime obstruction.

If the bounded state domain already reaches the `(h+1)`-st power of the
zero-indexed `s`-th prime `q_s`, then `s` optional composite macro types cannot
possibly suffice at horizon `h`; at least `s+1` are required. -/
theorem succ_macroBudget_le_minimumCompositeMacroCount_of_nthPrime_pow_succ_le_stateBound
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hState : (Nat.nth Nat.Prime s) ^ (h + 1) ≤ N) :
    s + 1 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  by_contra hNot
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ s := by
    omega
  obtain ⟨S, hS, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation hr hh
  have hSLe : S.ncard ≤ s := by
    rw [hSCard]
    exact hMuLe
  have hBound :=
    stateBound_lt_nthPrime_pow_succ_of_macroBudget_separator
      (r := r) (N := N) (s := s) (h := h) (S := S)
      hr hBinary hS.1 hS.2.1 hSLe hS.2.2
  omega

/-- Equivalent feasibility form: if `s` optional macro types suffice at
horizon `h`, then the state bound must lie below `q_s^(h+1)`. -/
theorem stateBound_lt_nthPrime_pow_succ_of_minimumCompositeMacroCount_le
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ s) :
    N < (Nat.nth Nat.Prime s) ^ (h + 1) := by
  by_contra hNot
  have hState : (Nat.nth Nat.Prime s) ^ (h + 1) ≤ N := by omega
  have hLower :=
    succ_macroBudget_le_minimumCompositeMacroCount_of_nthPrime_pow_succ_le_stateBound
      hr hh hBinary hState
  omega

/-- A fixed optional macro budget can only attain horizon at most `h` below the
same next-prime state threshold. -/
theorem stateBound_lt_nthPrime_pow_succ_of_macroBudget_minimumHorizon_le
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hDepth :
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤ h) :
    N < (Nat.nth Nat.Prime s) ^ (h + 1) := by
  have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤
      (RootQuotientPrimeBasis N).ncard + s := Nat.le_add_right _ _
  have hStorage : rootQuotientMinimumStorageSize r N h ≤
      (RootQuotientPrimeBasis N).ncard + s :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N)
      (s := (RootQuotientPrimeBasis N).ncard + s) (h := h)
      hr hPrimeBudget hh).1 hDepth
  have hDecomp :=
    rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      (r := r) (N := N) (h := h) hr hh
  rw [hDecomp] at hStorage
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ s := by
    omega
  exact stateBound_lt_nthPrime_pow_succ_of_minimumCompositeMacroCount_le
    hr hh hBinary hMuLe

/-- Logarithmic lower bound on execution depth under an `s`-macro budget.

For positive state domains in the high-root regime, any feasible horizon `h`
with at most `s` optional macros must be at least the floor logarithm of `N` in
the next-prime base. -/
theorem nthPrime_log_le_horizon_of_minimumCompositeMacroCount_le
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ s) :
    Nat.log (Nat.nth Nat.Prime s) N ≤ h := by
  have hState :=
    stateBound_lt_nthPrime_pow_succ_of_minimumCompositeMacroCount_le
      hr hh hBinary hMuLe
  have hQPrime : (Nat.nth Nat.Prime s).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime s
  have hNZero : N ≠ 0 := by omega
  have hLogLt : Nat.log (Nat.nth Nat.Prime s) N < h + 1 :=
    (Nat.log_lt_iff_lt_pow hQPrime.one_lt hNZero).2 hState
  omega

/-- Direct macro-budget depth lower bound in logarithmic form. -/
theorem nthPrime_log_le_minimumHorizonAtCompositeMacroBudget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hDepthPos : 1 ≤ rootQuotientMinimumHorizonAtCompositeMacroBudget r N s) :
    Nat.log (Nat.nth Nat.Prime s) N ≤
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s := by
  let h := rootQuotientMinimumHorizonAtCompositeMacroBudget r N s
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N h ≤ s := by
    have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s := Nat.le_add_right _ _
    have hStorage : rootQuotientMinimumStorageSize r N h ≤
        (RootQuotientPrimeBasis N).ncard + s := by
      apply (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
        (r := r) (N := N)
        (s := (RootQuotientPrimeBasis N).ncard + s) (h := h)
        hr hPrimeBudget hDepthPos).1
      exact le_rfl
    have hDecomp :=
      rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
        (r := r) (N := N) (h := h) hr hDepthPos
    rw [hDecomp] at hStorage
    omega
  exact nthPrime_log_le_horizon_of_minimumCompositeMacroCount_le
    hr hN hDepthPos hBinary hMuLe

end EnterpriseMath.Quotient
