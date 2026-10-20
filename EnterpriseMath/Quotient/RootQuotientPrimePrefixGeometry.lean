import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The literal first-prime prefix is a prime factorization of its own product. -/
theorem rootQuotientPrimePrefix_perm_primeFactorsList
    (q : ℕ) :
    (rootQuotientPrimePrefix q).Perm
      (rootQuotientPrimePrefixProduct q).primeFactorsList := by
  apply Nat.primeFactorsList_unique
  · rfl
  · exact rootQuotientPrimePrefix_all_prime q

/-- The zero-indexed `q`-th prime does not occur among the first `q` primes. -/
theorem nthPrime_not_mem_rootQuotientPrimePrefix
    (q : ℕ) :
    Nat.nth Nat.Prime q ∉ rootQuotientPrimePrefix q := by
  intro hMem
  rcases List.mem_map.1 hMem with ⟨i, hi, hEq⟩
  have hiLt : i < q := by
    simpa [rootQuotientPrimePrefix] using hi
  have hiEq : i = q :=
    (Nat.nth_strictMono Nat.infinite_setOfPred_prime).injective hEq
  omega

/-- The next prime is absent from the prime support of the prefix product. -/
theorem nthPrime_not_mem_primeFactors_prefixProduct
    (q : ℕ) :
    Nat.nth Nat.Prime q ∉ (rootQuotientPrimePrefixProduct q).primeFactors := by
  intro hFactors
  have hList :
      Nat.nth Nat.Prime q ∈
        (rootQuotientPrimePrefixProduct q).primeFactorsList :=
    (Nat.mem_primeFactors_iff_mem_primeFactorsList).1 hFactors
  have hPrefix :
      Nat.nth Nat.Prime q ∈ rootQuotientPrimePrefix q :=
    (rootQuotientPrimePrefix_perm_primeFactorsList q).mem_iff.mpr hList
  exact nthPrime_not_mem_rootQuotientPrimePrefix q hPrefix

/-- The first-`q`-prime product is coprime to the zero-indexed `q`-th prime. -/
theorem rootQuotientPrimePrefixProduct_coprime_nthPrime
    (q : ℕ) :
    Nat.Coprime
      (rootQuotientPrimePrefixProduct q)
      (Nat.nth Nat.Prime q) := by
  have hPrefixPos : 1 ≤ rootQuotientPrimePrefixProduct q :=
    prime_list_product_positive (rootQuotientPrimePrefix_all_prime q)
  have hNextPrime : (Nat.nth Nat.Prime q).Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime q
  have hDisjoint :
      Disjoint
        (rootQuotientPrimePrefixProduct q).primeFactors
        (Nat.nth Nat.Prime q).primeFactors := by
    rw [hNextPrime.primeFactors]
    simpa using nthPrime_not_mem_primeFactors_prefixProduct q
  exact (Nat.disjoint_primeFactors (by omega) hNextPrime.ne_zero).1 hDisjoint

end EnterpriseMath.Quotient
