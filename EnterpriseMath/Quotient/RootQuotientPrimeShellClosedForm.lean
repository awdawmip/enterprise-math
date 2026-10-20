import EnterpriseMath.Quotient.RootQuotientFactorGeometryAlgebra
import EnterpriseMath.Quotient.RootQuotientPrimePrefixGeometry
import EnterpriseMath.Quotient.RootQuotientPrimeShellPigeonhole
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Prefix-product recurrence: adjoining the zero-indexed `q`-th prime extends
the product of the first `q` primes to the first `q+1` primes. -/
theorem rootQuotientPrimePrefixProduct_succ
    (q : ℕ) :
    rootQuotientPrimePrefixProduct (q + 1) =
      rootQuotientPrimePrefixProduct q * Nat.nth Nat.Prime q := by
  simp [rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix,
    List.range_succ, List.map_append, List.prod_append]

/-- Explicit greedy candidate for the rank-`k` `r`-power-free shell.

For `c=r-1`, `q=floor(k/c)`, `s=k mod c`, this is

`(p_0 ... p_(q-1))^c * p_q^s`,

using zero-indexed primes. -/
noncomputable def rootQuotientPrimeShellClosedForm (r k : ℕ) : ℕ :=
  let c := r - 1
  let q := k / c
  let s := k % c
  (rootQuotientPrimePrefixProduct q) ^ c *
    (Nat.nth Nat.Prime q) ^ s

/-- The greedy shell candidate is positive. -/
theorem rootQuotientPrimeShellClosedForm_positive
    {r k : ℕ}
    (hr : 2 ≤ r) :
    1 ≤ rootQuotientPrimeShellClosedForm r k := by
  let c := r - 1
  let q := k / c
  let s := k % c
  have hPrefixPos : 1 ≤ rootQuotientPrimePrefixProduct q :=
    prime_list_product_positive (rootQuotientPrimePrefix_all_prime q)
  have hPrime : (Nat.nth Nat.Prime q).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime q
  dsimp [rootQuotientPrimeShellClosedForm, c, q, s]
  exact Nat.one_le_mul (by positivity) (by positivity)

/-- The greedy shell candidate has exactly rank `k`. -/
theorem rootQuotientPrimeShellClosedForm_factorCount
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeFactorCount (rootQuotientPrimeShellClosedForm r k) = k := by
  let c := r - 1
  let q := k / c
  let s := k % c
  have hcPos : 0 < c := by
    dsimp [c]
    omega
  have hPrefixPos : 1 ≤ rootQuotientPrimePrefixProduct q :=
    prime_list_product_positive (rootQuotientPrimePrefix_all_prime q)
  have hPrime : (Nat.nth Nat.Prime q).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime q
  have hPrimePos : 1 ≤ Nat.nth Nat.Prime q := hPrime.one_le
  have hFullPos : 1 ≤ (rootQuotientPrimePrefixProduct q) ^ c := by positivity
  have hPartPos : 1 ≤ (Nat.nth Nat.Prime q) ^ s := by positivity
  have hPrefixCount := rootQuotientPrimePrefixProduct_factorCount q
  have hPrimeCount :
      rootQuotientPrimeFactorCount (Nat.nth Nat.Prime q) = 1 := by
    rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hPrime]
    simp
  have hDecomp : q * c + s = k := by
    simpa [q, s] using Nat.div_add_mod' k c
  rw [rootQuotientPrimeShellClosedForm]
  dsimp only
  calc
    rootQuotientPrimeFactorCount
        ((rootQuotientPrimePrefixProduct q) ^ c *
          (Nat.nth Nat.Prime q) ^ s) =
        rootQuotientPrimeFactorCount
            ((rootQuotientPrimePrefixProduct q) ^ c) +
          rootQuotientPrimeFactorCount ((Nat.nth Nat.Prime q) ^ s) :=
      rootQuotientPrimeFactorCount_mul hFullPos hPartPos
    _ = c * rootQuotientPrimeFactorCount (rootQuotientPrimePrefixProduct q) +
          s * rootQuotientPrimeFactorCount (Nat.nth Nat.Prime q) := by
      rw [rootQuotientPrimeFactorCount_pow hPrefixPos,
        rootQuotientPrimeFactorCount_pow hPrimePos]
    _ = c * q + s := by rw [hPrefixCount, hPrimeCount]; simp
    _ = q * c + s := by rw [Nat.mul_comm c q]
    _ = k := hDecomp

/-- Powers of the prefix product remain coprime to powers of the next prime. -/
theorem rootQuotientPrimePrefixPowers_coprime_nextPrimePower
    {q c s : ℕ}
    (hcPos : 1 ≤ c) :
    Nat.Coprime
      ((rootQuotientPrimePrefixProduct q) ^ c)
      ((Nat.nth Nat.Prime q) ^ s) := by
  have hPrefixPos : 1 ≤ rootQuotientPrimePrefixProduct q :=
    prime_list_product_positive (rootQuotientPrimePrefix_all_prime q)
  have hPrime : (Nat.nth Nat.Prime q).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime q
  have hBaseCoprime := rootQuotientPrimePrefixProduct_coprime_nthPrime q
  by_cases hsZero : s = 0
  · subst s
    simp
  · have hBaseDisjoint :
        Disjoint
          (rootQuotientPrimePrefixProduct q).primeFactors
          (Nat.nth Nat.Prime q).primeFactors :=
      (Nat.disjoint_primeFactors (by omega) hPrime.ne_zero).2 hBaseCoprime
    have hPowerDisjoint :
        Disjoint
          ((rootQuotientPrimePrefixProduct q) ^ c).primeFactors
          ((Nat.nth Nat.Prime q) ^ s).primeFactors := by
      rw [Nat.primeFactors_pow _ (by omega),
        Nat.primeFactors_pow _ hsZero]
      exact hBaseDisjoint
    exact (Nat.disjoint_primeFactors (by positivity) (by positivity)).1
      hPowerDisjoint

/-- The explicit greedy candidate is `r`-power-free. -/
theorem rootQuotientPrimeShellClosedForm_rPowerFree
    {r k : ℕ}
    (hr : 2 ≤ r) :
    RPowerFree r (rootQuotientPrimeShellClosedForm r k) := by
  let c := r - 1
  let q := k / c
  let s := k % c
  have hcPos : 1 ≤ c := by
    dsimp [c]
    omega
  have hcLt : c < r := by
    dsimp [c]
    omega
  have hsLtC : s < c := by
    dsimp [s]
    exact Nat.mod_lt k (by omega)
  have hsLtR : s < r := hsLtC.trans hcLt
  have hPrefixPos : 1 ≤ rootQuotientPrimePrefixProduct q :=
    prime_list_product_positive (rootQuotientPrimePrefix_all_prime q)
  have hPrefixSquarefree := rootQuotientPrimePrefixProduct_squarefree q
  have hPrime : (Nat.nth Nat.Prime q).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime q
  have hFullFree :
      RPowerFree r ((rootQuotientPrimePrefixProduct q) ^ c) :=
    rPowerFree_pow_of_squarefree hPrefixPos hPrefixSquarefree hcLt
  have hPartFree :
      RPowerFree r ((Nat.nth Nat.Prime q) ^ s) :=
    rPowerFree_pow_of_squarefree hPrime.one_le hPrime.squarefree hsLtR
  have hFullPos : 1 ≤ (rootQuotientPrimePrefixProduct q) ^ c := by positivity
  have hPartPos : 1 ≤ (Nat.nth Nat.Prime q) ^ s := by positivity
  have hCoprime :
      Nat.Coprime
        ((rootQuotientPrimePrefixProduct q) ^ c)
        ((Nat.nth Nat.Prime q) ^ s) :=
    rootQuotientPrimePrefixPowers_coprime_nextPrimePower hcPos
  simpa [rootQuotientPrimeShellClosedForm, c, q, s] using
    rPowerFree_mul_of_coprime hFullPos hPartPos hFullFree hPartFree hCoprime

/-- The explicit greedy candidate belongs to the exact rank shell. -/
theorem rootQuotientPrimeShellClosedForm_mem
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellClosedForm r k ∈ RootQuotientPrimeShell r k := by
  exact ⟨rootQuotientPrimeShellClosedForm_positive hr,
    rootQuotientPrimeShellClosedForm_rPowerFree hr,
    rootQuotientPrimeShellClosedForm_factorCount hr⟩

/-- Successor recurrence of the explicit greedy candidate. -/
theorem rootQuotientPrimeShellClosedForm_succ
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellClosedForm r (k + 1) =
      rootQuotientPrimeShellClosedForm r k *
        Nat.nth Nat.Prime (k / (r - 1)) := by
  let c := r - 1
  let q := k / c
  let s := k % c
  have hcPos : 0 < c := by
    dsimp [c]
    omega
  have hsLt : s < c := by
    dsimp [s]
    exact Nat.mod_lt k hcPos
  have hDecomp : s + q * c = k := by
    simpa [q, s] using Nat.mod_add_div' k c
  by_cases hNoCarry : s + 1 < c
  · have hDivMod : (k + 1) / c = q ∧ (k + 1) % c = s + 1 := by
      apply (Nat.div_mod_unique hcPos).2
      constructor
      · calc
          (s + 1) + c * q = (s + q * c) + 1 := by
            simp [Nat.mul_comm, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]
          _ = k + 1 := by rw [hDecomp]
      · exact hNoCarry
    have hDivR : (k + 1) / (r - 1) = q := by simpa [c] using hDivMod.1
    have hModR : (k + 1) % (r - 1) = s + 1 := by simpa [c] using hDivMod.2
    simp [rootQuotientPrimeShellClosedForm, q, s, hDivR, hModR,
      pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  · have hCarry : s + 1 = c := by omega
    have hDivMod : (k + 1) / c = q + 1 ∧ (k + 1) % c = 0 := by
      apply (Nat.div_mod_unique hcPos).2
      constructor
      · calc
          0 + c * (q + 1) = (s + q * c) + 1 := by
            simp [hCarry, Nat.mul_succ, Nat.mul_comm, Nat.add_assoc,
              Nat.add_comm, Nat.add_left_comm]
          _ = k + 1 := by rw [hDecomp]
      · exact hcPos
    have hDivR : (k + 1) / (r - 1) = q + 1 := by simpa [c] using hDivMod.1
    have hModR : (k + 1) % (r - 1) = 0 := by simpa [c] using hDivMod.2
    rw [rootQuotientPrimeShellClosedForm, rootQuotientPrimeShellClosedForm]
    simp only [hDivR, hModR, pow_zero, Nat.mul_one]
    rw [rootQuotientPrimePrefixProduct_succ]
    rw [mul_pow]
    have hsEq : s + 1 = r - 1 := by simpa [c] using hCarry
    rw [← hsEq, pow_succ]
    simp [q, s, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- The abstract shell minimum is exactly the explicit greedy prime-packing
formula. -/
theorem rootQuotientPrimeShellMinimum_eq_closedForm
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r k =
      rootQuotientPrimeShellClosedForm r k := by
  induction k with
  | zero =>
      rw [rootQuotientPrimeShellMinimum_zero hr]
      simp [rootQuotientPrimeShellClosedForm]
  | succ k ih =>
      apply Nat.le_antisymm
      · exact rootQuotientPrimeShellMinimum_le
          (rootQuotientPrimeShellClosedForm_mem (r := r) (k := k + 1) hr)
      · rw [rootQuotientPrimeShellClosedForm_succ hr]
        rw [← ih]
        exact rootQuotientPrimeShellMinimum_mul_nthPrime_le_succ hr

/-- Closed-form shell threshold in the original quotient/root notation.

For `c=r-1`, `q=k/c`, `s=k mod c`, the least positive `r`-power-free integer
with exactly `k` prime-factor tokens is

`(p_0...p_(q-1))^c * p_q^s`.

All indexing here is zero-based. -/
theorem rootQuotientPrimeShellMinimum_closedForm
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r k =
      (rootQuotientPrimePrefixProduct (k / (r - 1))) ^ (r - 1) *
        (Nat.nth Nat.Prime (k / (r - 1))) ^ (k % (r - 1)) := by
  simpa [rootQuotientPrimeShellClosedForm] using
    rootQuotientPrimeShellMinimum_eq_closedForm (r := r) (k := k) hr

end EnterpriseMath.Quotient
