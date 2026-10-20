import EnterpriseMath.Quotient.RootQuotientHardPrimeDirectionStorage
import Mathlib.NumberTheory.PrimeCounting
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Integer cutoff for hard pure-prime directions at horizon `h`: the largest
base `p<=N` whose `(h+1)`-st power still lies in the bounded domain. -/
def rootQuotientPrimePowerCutoff
    (N h : ℕ) : ℕ :=
  Nat.findGreatest (fun p => p ^ (h + 1) ≤ N) N

/-- The cutoff itself satisfies the defining power bound. -/
theorem rootQuotientPrimePowerCutoff_pow_succ_le
    (N h : ℕ) :
    (rootQuotientPrimePowerCutoff N h) ^ (h + 1) ≤ N := by
  exact Nat.findGreatest_spec
    (P := fun p => p ^ (h + 1) ≤ N)
    (m := 0) (n := N) (Nat.zero_le _) (by simp)

/-- The cutoff is bounded by the state bound. -/
theorem rootQuotientPrimePowerCutoff_le
    (N h : ℕ) :
    rootQuotientPrimePowerCutoff N h ≤ N := by
  exact Nat.findGreatest_le N

/-- Exact integer-root Galois law for the cutoff. -/
theorem pow_succ_le_stateBound_iff_le_primePowerCutoff
    {N h p : ℕ} :
    p ^ (h + 1) ≤ N ↔
      p ≤ rootQuotientPrimePowerCutoff N h := by
  constructor
  · intro hPow
    have hpN : p ≤ N := by
      by_cases hpZero : p = 0
      · simp [hpZero]
      · have hpPos : 1 ≤ p := Nat.one_le_iff_ne_zero.mpr hpZero
        have hpLePow : p ≤ p ^ (h + 1) := by
          calc
            p = p ^ 1 := by simp
            _ ≤ p ^ (h + 1) :=
              Nat.pow_le_pow_right hpPos (by omega)
        exact hpLePow.trans hPow
    exact Nat.le_findGreatest hpN hPow
  · intro hpCut
    have hCutPow := rootQuotientPrimePowerCutoff_pow_succ_le N h
    have hPowMono :
        p ^ (h + 1) ≤
          (rootQuotientPrimePowerCutoff N h) ^ (h + 1) :=
      Nat.pow_le_pow_left hpCut (h + 1)
    exact hPowMono.trans hCutPow

/-- Hard prime directions are exactly the primes at or below the integer power
cutoff. -/
theorem rootQuotientHardPrimeDirections_eq_primesLE_cutoff
    (N h : ℕ) :
    RootQuotientHardPrimeDirections N h =
      ↑(Nat.primesLE (rootQuotientPrimePowerCutoff N h)) := by
  ext p
  change (p.Prime ∧ p ^ (h + 1) ≤ N) ↔
    p ∈ Nat.primesLE (rootQuotientPrimePowerCutoff N h)
  rw [pow_succ_le_stateBound_iff_le_primePowerCutoff,
    Nat.mem_primesLE]
  tauto

/-- Closed cardinality form: the number of hard directions is the standard
prime-counting function evaluated at the integer power cutoff. -/
theorem rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff
    (N h : ℕ) :
    (RootQuotientHardPrimeDirections N h).ncard =
      Nat.primeCounting (rootQuotientPrimePowerCutoff N h) := by
  rw [rootQuotientHardPrimeDirections_eq_primesLE_cutoff]
  simp

/-- **Prime-counting lower bound on true optional-macro storage.**

At fixed positive horizon `h` in the high-root regime, the minimum number of
optional composite macro types is at least

`pi(rho_{h+1}(N))`,

where `rho_{h+1}(N)` is the largest integer whose `(h+1)`-st power is at most
`N`.

This is the fixed-horizon dual of the next-prime macro-budget obstruction. -/
theorem primeCounting_cutoff_le_minimumCompositeMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    Nat.primeCounting (rootQuotientPrimePowerCutoff N h) ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  rw [← rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff]
  exact hardPrimeDirections_ncard_le_minimumCompositeMacroCount
    hr hh hBinary

/-- Total primitive-storage lower bound in prime-counting form. -/
theorem primeBasis_add_primeCounting_cutoff_le_minimumStorage
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    (RootQuotientPrimeBasis N).ncard +
        Nat.primeCounting (rootQuotientPrimePowerCutoff N h) ≤
      rootQuotientMinimumStorageSize r N h := by
  rw [← rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff]
  exact primeBasis_add_hardPrimeDirections_le_minimumStorage
    hr hh hBinary

end EnterpriseMath.Quotient
