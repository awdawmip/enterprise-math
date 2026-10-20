import EnterpriseMath.Quotient.RootQuotientPrimeBirthHorizonTwoConflict
import EnterpriseMath.Quotient.RootQuotientRepairPacking
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Prime-branch targets `p^2*q` indexed by a finite set of cofactor primes. -/
noncomputable def RootQuotientPrimeSquareBranchTargetFinset
    (p : ℕ) (Q : Finset ℕ) : Finset ℕ :=
  Q.image (fun q => p ^ 2 * q)

/-- Multiplication by a positive prime square is injective, so the branch-target
family has exactly the cardinality of its cofactor-prime index set. -/
theorem primeSquareBranchTargetFinset_card_eq
    {p : ℕ} (hp : p.Prime) (Q : Finset ℕ) :
    (RootQuotientPrimeSquareBranchTargetFinset p Q).card = Q.card := by
  classical
  unfold RootQuotientPrimeSquareBranchTargetFinset
  apply Finset.card_image_iff.mpr
  intro q hq r hr hEq
  exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos hp.pos) hEq

/-- If a semantic composite candidate divides two distinct prime-square branch
targets, then it must be the common square `p^2` itself. -/
theorem common_composite_divisor_of_distinct_primeSquareBranches_eq_square
    {r N p q₁ q₂ g : ℕ}
    (hp : p.Prime)
    (hq₁ : q₁.Prime)
    (hq₂ : q₂.Prime)
    (hqNe : q₁ ≠ q₂)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hg₁ : g ∣ p ^ 2 * q₁)
    (hg₂ : g ∣ p ^ 2 * q₂) :
    g = p ^ 2 := by
  have hCoprime : q₁.Coprime q₂ :=
    (coprime_primes hq₁ hq₂).2 hqNe
  have hgGcd : g ∣ Nat.gcd (p ^ 2 * q₁) (p ^ 2 * q₂) :=
    Nat.dvd_gcd hg₁ hg₂
  have hGcd : Nat.gcd (p ^ 2 * q₁) (p ^ 2 * q₂) = p ^ 2 := by
    rw [Nat.gcd_mul_left, hCoprime.gcd_eq_one, Nat.mul_one]
  rw [hGcd] at hgGcd
  obtain ⟨k, hkLe, hgEq⟩ := (Nat.dvd_prime_pow hp).1 hgGcd
  have hgSemantic := hgC.1
  have hRank : 2 ≤ rootQuotientPrimeFactorCount g := by
    have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hgSemantic.1
    by_contra hNot
    have hCountOne : rootQuotientPrimeFactorCount g = 1 := by omega
    have hgPrime : g.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hgSemantic.1).1 hCountOne
    exact hgC.2 ⟨hgPrime, hgSemantic.2.1⟩
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hp]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ k) = k := by
    rw [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    simp
  have hkTwo : k = 2 := by
    rw [hgEq, hPowCount] at hRank
    omega
  simpa [hgEq, hkTwo]

/-- **Prime-square branch packing after deleting the axis macro.**

For distinct prime cofactors, no admissible composite macro other than `p^2`
can divide two branch targets `p^2*q`.  Therefore, once `p^2` is excluded from
the candidate set, all such branches form a divisor-incompatibility packing. -/
theorem primeSquareBranches_are_repairPacking_without_axis
    {r N p : ℕ} {Q : Finset ℕ}
    (hp : p.Prime)
    (hQPrime : ∀ q ∈ Q, q.Prime) :
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
      (RootQuotientPrimeSquareBranchTargetFinset p Q) := by
  intro g hgC t ht u hu hgT hgU
  classical
  obtain ⟨q, hqQ, rfl⟩ := Finset.mem_image.1 ht
  obtain ⟨s, hsQ, rfl⟩ := Finset.mem_image.1 hu
  by_cases hqs : q = s
  · subst s
    rfl
  · have hgSq :=
      common_composite_divisor_of_distinct_primeSquareBranches_eq_square
        (r := r) (N := N) (p := p) (q₁ := q) (q₂ := s) (g := g)
        hp (hQPrime q hqQ) (hQPrime s hsQ) hqs hgC.1 hgT hgU
    exact (hgC.2 (by simpa [hgSq])).elim

/-- **Axis fanout lower bound.**

If `m` prime-square branches are to be repaired without storing the common axis
macro `p^2`, then at least `m` distinct replacement composite types are
necessary. -/
theorem primeSquareBranch_card_le_replacement_storage_without_axis
    {r N p : ℕ} {Q : Finset ℕ} {S : Set ℕ}
    (hp : p.Prime)
    (hQPrime : ∀ q ∈ Q, q.Prime)
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover
      (RootQuotientPrimeSquareBranchTargetFinset p Q)
      (RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ)) S) :
    Q.card ≤ S.ncard := by
  have hPack := primeSquareBranches_are_repairPacking_without_axis
    (r := r) (N := N) (p := p) (Q := Q) hp hQPrime
  have hLower := repairDivisorPacking_card_le_cover_ncard
    (T := RootQuotientPrimeSquareBranchTargetFinset p Q)
    (U := RootQuotientPrimeSquareBranchTargetFinset p Q)
    (C := RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
    (S := S) (by simp) hPack hSFinite hCover
  rw [primeSquareBranchTargetFinset_card_eq hp Q] at hLower
  exact hLower

end EnterpriseMath.Quotient
