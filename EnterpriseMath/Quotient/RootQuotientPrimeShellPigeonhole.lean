import EnterpriseMath.Quotient.RootQuotientPrimeShellOrder
import Mathlib.Data.Nat.Count
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Finite sum bound used by the prime-capacity pigeonhole argument. -/
theorem finset_sum_le_card_mul_bound
    {α : Type*} [DecidableEq α]
    (s : Finset α) (f : α → ℕ) (c : ℕ)
    (hBound : ∀ x ∈ s, f x ≤ c) :
    (∑ x in s, f x) ≤ s.card * c := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
      have haBound : f a ≤ c := hBound a (by simp)
      have hRest : (∑ x in s, f x) ≤ s.card * c := by
        apply ih
        intro x hx
        exact hBound x (by simp [hx])
      simpa [ha, Nat.succ_mul, Nat.add_comm] using
        Nat.add_le_add haBound hRest

/-- Prime-capacity pigeonhole lemma.

If an `r`-power-free positive integer carries more than `q*(r-1)` prime-factor
tokens, one of its prime factors is at least the zero-indexed `q`-th prime.
Otherwise all prime factors would lie among the first `q` primes, each with
multiplicity at most `r-1`, contradicting the total token count. -/
theorem exists_primeFactor_ge_nth_of_factorCount_gt_capacity
    {r b q : ℕ}
    (hr : 2 ≤ r)
    (hbPos : 1 ≤ b)
    (hbFree : RPowerFree r b)
    (hRank : q * (r - 1) < rootQuotientPrimeFactorCount b) :
    ∃ p : ℕ,
      p ∈ b.primeFactors ∧ Nat.nth Nat.Prime q ≤ p := by
  classical
  by_contra hNo
  have hAllSmall :
      ∀ p : ℕ, p ∈ b.primeFactors → p < Nat.nth Nat.Prime q := by
    intro p hp
    by_contra hNotLt
    apply hNo
    exact ⟨p, hp, by omega⟩
  let primeBelow : Finset ℕ :=
    (Finset.range (Nat.nth Nat.Prime q)).filter Nat.Prime
  have hSupportSub : b.factorization.support ⊆ primeBelow := by
    intro p hpSupport
    have hpFactors : p ∈ b.primeFactors := by
      simpa using hpSupport
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactors hpFactors
    have hpLt : p < Nat.nth Nat.Prime q := hAllSmall p hpFactors
    simp [primeBelow, hpLt, hpPrime]
  have hPrimeBelowCard : primeBelow.card = q := by
    calc
      primeBelow.card = Nat.count Nat.Prime (Nat.nth Nat.Prime q) := by
        simpa [primeBelow] using
          (Nat.count_eq_card_filter_range Nat.Prime
            (Nat.nth Nat.Prime q)).symm
      _ = q :=
        Nat.count_nth_of_infinite Nat.infinite_setOfPred_prime q
  have hSupportCard : b.factorization.support.card ≤ q := by
    calc
      b.factorization.support.card ≤ primeBelow.card :=
        Finset.card_le_card hSupportSub
      _ = q := hPrimeBelowCard
  have hCoordinateBound :
      ∀ p ∈ b.factorization.support, b.factorization p ≤ r - 1 := by
    intro p hpSupport
    have hpFactors : p ∈ b.primeFactors := by
      simpa using hpSupport
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactors hpFactors
    have hpLt : b.factorization p < r :=
      (rPowerFree_iff_prime_factorization_lt hbPos).1 hbFree p hpPrime
    omega
  have hOmegaSupport :
      rootQuotientPrimeFactorCount b ≤
        b.factorization.support.card * (r - 1) := by
    rw [rootQuotientPrimeFactorCount_eq_factorization_sum]
    change (∑ p in b.factorization.support, b.factorization p) ≤
      b.factorization.support.card * (r - 1)
    exact finset_sum_le_card_mul_bound
      b.factorization.support (fun p => b.factorization p) (r - 1)
      hCoordinateBound
  have hOmegaCapacity :
      rootQuotientPrimeFactorCount b ≤ q * (r - 1) := by
    exact hOmegaSupport.trans
      (Nat.mul_le_mul_right (r - 1) hSupportCard)
  omega

/-- Recurrence lower bound for abstract shell minima.

Let `c=r-1` and `q=floor(k/c)`.  Any rank-`k+1` power-free boundary contains a
prime factor at least `p_q`; deleting that factor leaves a rank-`k` power-free
divisor, whose value is at least the rank-`k` shell minimum. -/
theorem rootQuotientPrimeShellMinimum_mul_nthPrime_le_succ
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r k *
        Nat.nth Nat.Prime (k / (r - 1)) ≤
      rootQuotientPrimeShellMinimum r (k + 1) := by
  let b := rootQuotientPrimeShellMinimum r (k + 1)
  let q := k / (r - 1)
  have hNextMem : b ∈ RootQuotientPrimeShell r (k + 1) := by
    simpa [b] using
      rootQuotientPrimeShellMinimum_mem (r := r) (k := k + 1) hr
  have hCapacity : q * (r - 1) ≤ k := by
    dsimp [q]
    exact Nat.div_mul_le_self k (r - 1)
  have hRank : q * (r - 1) < rootQuotientPrimeFactorCount b := by
    rw [hNextMem.2.2]
    omega
  obtain ⟨p, hpFactors, hpLarge⟩ :=
    exists_primeFactor_ge_nth_of_factorCount_gt_capacity
      hr hNextMem.1 hNextMem.2.1 hRank
  have hpPrime : p.Prime := Nat.prime_of_mem_primeFactors hpFactors
  have hpDvd : p ∣ b := Nat.dvd_of_mem_primeFactors hpFactors
  rcases hpDvd with ⟨a, hba⟩
  have haPos : 1 ≤ a := by
    by_contra hNot
    have haZero : a = 0 := by omega
    subst a
    simp at hba
    omega
  have haDvd : a ∣ b := by
    refine ⟨p, ?_⟩
    simpa [Nat.mul_comm] using hba
  have haFree : RPowerFree r a :=
    rPowerFree_of_dvd_of_rPowerFree haDvd hNextMem.2.1
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hpPrime]
    simp
  have haCount : rootQuotientPrimeFactorCount a = k := by
    have hMul := rootQuotientPrimeFactorCount_mul hpPrime.one_le haPos
    have hNextCount := hNextMem.2.2
    rw [hba] at hNextCount
    rw [hMul, hpCount] at hNextCount
    omega
  have haShell : a ∈ RootQuotientPrimeShell r k :=
    ⟨haPos, haFree, haCount⟩
  have hMinLeA : rootQuotientPrimeShellMinimum r k ≤ a :=
    rootQuotientPrimeShellMinimum_le haShell
  calc
    rootQuotientPrimeShellMinimum r k * Nat.nth Nat.Prime q ≤ a * p :=
      Nat.mul_le_mul hMinLeA hpLarge
    _ = p * a := by rw [Nat.mul_comm]
    _ = b := hba.symm
    _ = rootQuotientPrimeShellMinimum r (k + 1) := by rfl

end EnterpriseMath.Quotient
