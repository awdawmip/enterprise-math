import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A product of `m` integers each at least two is at least `2^m`. -/
theorem pow_two_length_le_list_prod
    {l : List ℕ}
    (hTwo : ∀ a : ℕ, a ∈ l → 2 ≤ a) :
    2 ^ l.length ≤ l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      have haTwo : 2 ≤ a := hTwo a (by simp)
      have hTail : ∀ b : ℕ, b ∈ l → 2 ≤ b := by
        intro b hb
        exact hTwo b (by simp [hb])
      have hInd := ih hTail
      simp only [List.length_cons, List.prod_cons, pow_succ]
      simpa [Nat.mul_comm] using Nat.mul_le_mul hInd haTwo

/-- Universal size lower bound from prime-factor count. -/
theorem pow_two_primeFactorCount_le
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    2 ^ rootQuotientPrimeFactorCount b ≤ b := by
  have hbZero : b ≠ 0 := by omega
  have hTwo : ∀ p : ℕ, p ∈ b.primeFactorsList → 2 ≤ p := by
    intro p hp
    exact (Nat.prime_of_mem_primeFactorsList hp).two_le
  have hProd := pow_two_length_le_list_prod hTwo
  rw [Nat.prod_primeFactorsList hbZero] at hProd
  simpa [rootQuotientPrimeFactorCount] using hProd

/-- Prime-factor count of a power of two is its exponent. -/
theorem rootQuotientPrimeFactorCount_two_pow
    (k : ℕ) :
    rootQuotientPrimeFactorCount (2 ^ k) = k := by
  induction k with
  | zero => simp [rootQuotientPrimeFactorCount]
  | succ k ih =>
      have hPowPos : 1 ≤ 2 ^ k := by positivity
      calc
        rootQuotientPrimeFactorCount (2 ^ (k + 1)) =
            rootQuotientPrimeFactorCount (2 ^ k * 2) := by
          rw [pow_succ]
        _ = rootQuotientPrimeFactorCount (2 ^ k) +
            rootQuotientPrimeFactorCount 2 :=
          rootQuotientPrimeFactorCount_mul hPowPos (by omega)
        _ = k + 1 := by
          rw [ih, rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime Nat.prime_two]
          simp

/-- A power `2^k` is `r`-power-free whenever its exponent is below the root order. -/
theorem two_pow_rPowerFree_of_exponent_lt_rootOrder
    {r k : ℕ}
    (hk : k < r) :
    RPowerFree r (2 ^ k) := by
  intro t ht hDvd
  have hPowPos : 0 < 2 ^ k := by positivity
  have hDvdLe : t ^ r ≤ 2 ^ k :=
    Nat.le_of_dvd hPowPos hDvd
  have hTwoLe : 2 ^ r ≤ t ^ r :=
    Nat.pow_le_pow_left ht r
  have hStrict : 2 ^ k < 2 ^ r := by
    exact pow_lt_pow_right' (by omega : (1 : ℕ) < 2) hk
  omega

/-- Every rank-`k` power-free shell lies above the trivial factor-size bound `2^k`. -/
theorem pow_two_le_rootQuotientPrimeShellMinimum
    {r k : ℕ}
    (hr : 2 ≤ r) :
    2 ^ k ≤ rootQuotientPrimeShellMinimum r k := by
  have hMem := rootQuotientPrimeShellMinimum_mem (r := r) (k := k) hr
  have hLower := pow_two_primeFactorCount_le hMem.1
  simpa [hMem.2.2] using hLower

/-- In the high-root regime `k<r`, the abstract rank-shell minimum is exactly `2^k`. -/
theorem rootQuotientPrimeShellMinimum_eq_two_pow_of_lt_rootOrder
    {r k : ℕ}
    (hr : 2 ≤ r)
    (hk : k < r) :
    rootQuotientPrimeShellMinimum r k = 2 ^ k := by
  apply Nat.le_antisymm
  · apply rootQuotientPrimeShellMinimum_le
    exact ⟨by positivity,
      two_pow_rPowerFree_of_exponent_lt_rootOrder hk,
      rootQuotientPrimeFactorCount_two_pow k⟩
  · exact pow_two_le_rootQuotientPrimeShellMinimum hr

/-- Binary/high-root interval law without invoking logarithms explicitly.

If the state bound lies between consecutive powers of two and the lower rank
`k` is still below the root order, then the exact prime-only horizon is `k`. -/
theorem rootQuotientPrimeHorizon_eq_of_two_pow_interval
    {r N k : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hk : k < r)
    (hLower : 2 ^ k ≤ N)
    (hUpper : N < 2 ^ (k + 1)) :
    rootQuotientPrimeHorizon r N = k := by
  apply (rootQuotientPrimeHorizon_eq_iff_shell_interval hr hN).2
  constructor
  · simpa [rootQuotientPrimeShellMinimum_eq_two_pow_of_lt_rootOrder hr hk]
      using hLower
  · have hShellLower :
        2 ^ (k + 1) ≤ rootQuotientPrimeShellMinimum r (k + 1) :=
      pow_two_le_rootQuotientPrimeShellMinimum hr
    exact hUpper.trans_le hShellLower

/-- Standard binary-regime closed form.

Below the first nontrivial `r`-th power `2^r`, the exact prime-only quotient
compiler horizon is the natural-number floor logarithm in base two.  This is a
corollary of the general shell theorem rather than a separate depth theory. -/
theorem rootQuotientPrimeHorizon_eq_log_two_of_lt_two_pow
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeHorizon r N = Nat.log 2 N := by
  have hNZero : N ≠ 0 := by omega
  have hLogRoot : Nat.log 2 N < r :=
    (Nat.log_lt_iff_lt_pow (by omega) hNZero).2 hBinary
  have hLower : 2 ^ Nat.log 2 N ≤ N :=
    Nat.pow_log_le_self 2 hNZero
  have hUpper : N < 2 ^ (Nat.log 2 N + 1) := by
    simpa [Nat.succ_eq_add_one] using
      Nat.lt_pow_succ_log_self (by omega : 1 < 2) N
  exact rootQuotientPrimeHorizon_eq_of_two_pow_interval
    hr hN hLogRoot hLower hUpper

/-- Shell minima move downward (or stay fixed) as the root order increases,
because the power-free exponent box becomes less restrictive. -/
theorem rootQuotientPrimeShellMinimum_anti_rootOrder
    {r s k : ℕ}
    (hr : 2 ≤ r)
    (hrs : r ≤ s) :
    rootQuotientPrimeShellMinimum s k ≤
      rootQuotientPrimeShellMinimum r k := by
  have hMemR := rootQuotientPrimeShellMinimum_mem (r := r) (k := k) hr
  apply rootQuotientPrimeShellMinimum_le
  exact ⟨hMemR.1,
    rPowerFree_mono_rootOrder hrs hMemR.2.1,
    hMemR.2.2⟩

end EnterpriseMath.Quotient
