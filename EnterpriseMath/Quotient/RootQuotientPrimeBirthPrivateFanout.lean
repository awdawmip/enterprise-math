import EnterpriseMath.Quotient.RootQuotientPrimeBirthAxisFanout
import EnterpriseMath.Quotient.RootQuotientPrimeBirthBranchChoice
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Prime cofactors whose branch targets `p^2*q` become unreachable when the
shared square axis `p^2` is deleted from a horizon-two exact dictionary. -/
noncomputable def RootQuotientPrivatePrimeBranchCofactors
    (N p : ℕ) (S : Set ℕ) : Finset ℕ := by
  classical
  exact (Finset.range p).filter fun q =>
    q.Prime ∧
      ¬RootQuotientProductReachableWithin 2
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) (p ^ 2 * q)

@[simp]
theorem mem_privatePrimeBranchCofactors_iff
    {N p q : ℕ} {S : Set ℕ} :
    q ∈ RootQuotientPrivatePrimeBranchCofactors N p S ↔
      q < p ∧ q.Prime ∧
      ¬RootQuotientProductReachableWithin 2
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) (p ^ 2 * q) := by
  classical
  simp [RootQuotientPrivatePrimeBranchCofactors, and_left_comm,
    and_assoc]

/-- Every private prime-branch cofactor is literally a smaller prime. -/
theorem privatePrimeBranchCofactors_are_prime
    {N p : ℕ} {S : Set ℕ} :
    ∀ q ∈ RootQuotientPrivatePrimeBranchCofactors N p S, q.Prime := by
  intro q hq
  exact (mem_privatePrimeBranchCofactors_iff.1 hq).2.1

/-- The corresponding target family is horizon-two hard for the dictionary
with the square axis deleted, by construction. -/
theorem privatePrimeBranchTargets_not_reachable_without_axis
    {N p : ℕ} {S : Set ℕ} :
    ∀ t ∈ RootQuotientPrimeSquareBranchTargetFinset p
        (RootQuotientPrivatePrimeBranchCofactors N p S),
      ¬RootQuotientProductReachableWithin 2
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) t := by
  classical
  intro t ht
  obtain ⟨q, hq, rfl⟩ := Finset.mem_image.1 ht
  exact (mem_privatePrimeBranchCofactors_iff.1 hq).2.2

/-- **Private axis-fanout replacement lower bound.**

Let `Q_priv(S,p)` be the prime branches that genuinely depend on a stored
square `p^2`.  Any finite replacement dictionary `R` that avoids `p^2` and
repairs all those branches over the deleted-axis base must contain at least
`|Q_priv(S,p)|` distinct types.

Thus the cardinality of the private prime fanout is a local shadow price for
removing the shared axis macro. -/
theorem privatePrimeBranchFanout_card_le_replacement_storage
    {r N p : ℕ} {S R : Set ℕ}
    (hp : p.Prime)
    (hRFinite : R.Finite)
    (hRCandidate : R ⊆
      RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
    (hRepair : ∀ t ∈ RootQuotientPrimeSquareBranchTargetFinset p
        (RootQuotientPrivatePrimeBranchCofactors N p S),
      RootQuotientProductReachableWithin 2
        ((RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) ∪ R) t) :
    (RootQuotientPrivatePrimeBranchCofactors N p S).card ≤ R.ncard := by
  let Q := RootQuotientPrivatePrimeBranchCofactors N p S
  let G := RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})
  have hNoBase : ∀ t ∈ RootQuotientPrimeSquareBranchTargetFinset p Q,
      ¬RootQuotientProductReachableWithin 2 G t := by
    dsimp [Q, G]
    exact privatePrimeBranchTargets_not_reachable_without_axis
  have hHit : ∀ t ∈ RootQuotientPrimeSquareBranchTargetFinset p Q,
      ∃ g : ℕ, g ∈ R ∧ g ∣ t := by
    apply spare_family_divisor_covers_base_hard_targets
    · intro t ht
      simpa [G, Q, Set.union_assoc] using hRepair t ht
    · exact hNoBase
  have hCover : RootQuotientRepairDivisorCover
      (RootQuotientPrimeSquareBranchTargetFinset p Q)
      (RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ)) R :=
    ⟨hRCandidate, hHit⟩
  have hLower := primeSquareBranch_card_le_replacement_storage_without_axis
    (r := r) (N := N) (p := p) (Q := Q) (S := R)
    hp (by
      intro q hq
      exact privatePrimeBranchCofactors_are_prime q hq)
    hRFinite hCover
  simpa [Q] using hLower

end EnterpriseMath.Quotient
