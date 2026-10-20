import EnterpriseMath.Quotient.RootQuotientPrimeCountingStorageLowerBound
import EnterpriseMath.Quotient.RootQuotientCoarseStableMacroLadder
import Mathlib.NumberTheory.PrimeCounting
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Pure-direction storage demand at state bound `N` and horizon `h`.

This counts exactly the prime directions `p` whose target `p^(h+1)` already lies
inside the bounded domain.  It is the information-theoretic macro floor before
any mixed-direction interaction is considered. -/
def rootQuotientPrimeDirectionDemand
    (N h : ℕ) : ℕ :=
  Nat.primeCounting (rootQuotientPrimePowerCutoff N h)

/-- Prime counting and `Nat.nth Prime` are exact discrete inverses in the form
needed by the resource theory. -/
theorem primeCounting_le_iff_lt_nthPrime
    {x s : ℕ} :
    Nat.primeCounting x ≤ s ↔ x < Nat.nth Nat.Prime s := by
  change Nat.count Nat.Prime (x + 1) ≤ s ↔ x < Nat.nth Nat.Prime s
  rw [Nat.count_le_iff_le_nth Nat.infinite_setOfPred_prime]
  omega

/-- Exact Galois law between pure-direction storage demand and the next-prime
state threshold.

`d_dir(N,h) <= s` iff the `(s+1)`-st prime power `q_s^(h+1)` lies strictly
beyond the bounded domain.  Thus the fixed-horizon prime-counting lower bound
and the fixed-budget next-prime obstruction are literally the same discrete
resource boundary in dual coordinates. -/
theorem primeDirectionDemand_le_iff_stateBound_lt_nthPrime_pow_succ
    {N h s : ℕ} :
    rootQuotientPrimeDirectionDemand N h ≤ s ↔
      N < (Nat.nth Nat.Prime s) ^ (h + 1) := by
  rw [rootQuotientPrimeDirectionDemand,
    primeCounting_le_iff_lt_nthPrime]
  constructor
  · intro hCutLt
    by_contra hNot
    have hPowLe : (Nat.nth Nat.Prime s) ^ (h + 1) ≤ N := by omega
    have hQLeCut :=
      (pow_succ_le_stateBound_iff_le_primePowerCutoff
        (N := N) (h := h) (p := Nat.nth Nat.Prime s)).1 hPowLe
    omega
  · intro hStateLt
    by_contra hNot
    have hQLeCut : Nat.nth Nat.Prime s ≤
        rootQuotientPrimePowerCutoff N h := by omega
    have hPowLe :=
      (pow_succ_le_stateBound_iff_le_primePowerCutoff
        (N := N) (h := h) (p := Nat.nth Nat.Prime s)).2 hQLeCut
    omega

/-- Stable-base notation form of the same exact Galois law. -/
theorem primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
    {N h s : ℕ} :
    rootQuotientPrimeDirectionDemand N h ≤ s ↔
      N < (rootQuotientStablePrimeBase s) ^ (h + 1) := by
  simpa [rootQuotientStablePrimeBase] using
    (primeDirectionDemand_le_iff_stateBound_lt_nthPrime_pow_succ
      (N := N) (h := h) (s := s))

/-- The directional demand is always a lower bound on the true optional-macro
requirement in the high-root regime. -/
theorem primeDirectionDemand_le_minimumCompositeMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  exact primeCounting_cutoff_le_minimumCompositeMacroCount
    hr hh hBinary

/-- Mixed-direction storage overhead: the part of the true minimum optional
macro count not forced by pure-prime directions alone. -/
def rootQuotientMixedDirectionMacroOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientMinimumCompositeMacroCount r N h -
    rootQuotientPrimeDirectionDemand N h

/-- Exact decomposition of the optional-macro frontier into pure-direction
floor plus mixed-direction overhead. -/
theorem minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientPrimeDirectionDemand N h +
        rootQuotientMixedDirectionMacroOverhead r N h := by
  have hDirLe := primeDirectionDemand_le_minimumCompositeMacroCount
    hr hh hBinary
  dsimp [rootQuotientMixedDirectionMacroOverhead]
  omega

/-- Total storage decomposes into the forced prime core, the pure-direction
macro floor, and the residual mixed-direction overhead. -/
theorem minimumStorage_eq_prime_add_directionDemand_add_mixedOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard +
        rootQuotientPrimeDirectionDemand N h +
          rootQuotientMixedDirectionMacroOverhead r N h := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  rw [minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    hr hh hBinary]
  omega

end EnterpriseMath.Quotient
