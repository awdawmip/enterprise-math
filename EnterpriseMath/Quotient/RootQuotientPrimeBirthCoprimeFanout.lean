import EnterpriseMath.Quotient.RootQuotientPrimeBirthPrivateFanout
import EnterpriseMath.Quotient.RootQuotientPrimeBirthHorizonTwoConflict
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- All lower cofactors that are already one-step literals after deleting the
future square axis `p^2`, but whose lifted branch `p^2*b` becomes horizon-two
unreachable without that axis. -/
noncomputable def RootQuotientPrivateAxisCofactors
    (N p : ℕ) (S : Set ℕ) : Finset ℕ := by
  classical
  let G := RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})
  exact (Finset.range p).filter fun b =>
    2 ≤ b ∧
      RootQuotientProductReachableWithin 1 G b ∧
      ¬RootQuotientProductReachableWithin 2 G (p ^ 2 * b)

@[simp]
theorem mem_privateAxisCofactors_iff
    {N p b : ℕ} {S : Set ℕ} :
    b ∈ RootQuotientPrivateAxisCofactors N p S ↔
      b < p ∧ 2 ≤ b ∧
      RootQuotientProductReachableWithin 1
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) b ∧
      ¬RootQuotientProductReachableWithin 2
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) (p ^ 2 * b) := by
  classical
  simp [RootQuotientPrivateAxisCofactors, and_assoc]

/-- Branch targets indexed by arbitrary lower cofactors. -/
noncomputable def RootQuotientSquareAxisCofactorTargetFinset
    (p : ℕ) (B : Finset ℕ) : Finset ℕ :=
  B.image (fun b => p ^ 2 * b)

/-- Positive square multiplication preserves the cofactor cardinality. -/
theorem squareAxisCofactorTargetFinset_card_eq
    {p : ℕ} (hp : p.Prime) (B : Finset ℕ) :
    (RootQuotientSquareAxisCofactorTargetFinset p B).card = B.card := by
  classical
  unfold RootQuotientSquareAxisCofactorTargetFinset
  apply Finset.card_image_iff.mpr
  intro b hb c hc hEq
  exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos hp.pos) hEq

/-- If two cofactors are coprime, then any semantic composite dividing both
lifted branches `p^2*b` and `p^2*c` must be the shared square `p^2`. -/
theorem common_composite_divisor_of_coprime_squareAxisBranches_eq_square
    {r N p b c g : ℕ}
    (hp : p.Prime)
    (hbc : b.Coprime c)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgB : g ∣ p ^ 2 * b)
    (hgCof : g ∣ p ^ 2 * c) :
    g = p ^ 2 := by
  have hgGcd : g ∣ Nat.gcd (p ^ 2 * b) (p ^ 2 * c) :=
    Nat.dvd_gcd hgB hgCof
  have hGcd : Nat.gcd (p ^ 2 * b) (p ^ 2 * c) = p ^ 2 := by
    rw [Nat.gcd_mul_left, hbc.gcd_eq_one, Nat.mul_one]
  rw [hGcd] at hgGcd
  obtain ⟨k, _hkLe, hgEq⟩ := (Nat.dvd_prime_pow hp).1 hgGcd
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

/-- Pairwise-coprime private cofactors induce a divisor-incompatibility packing
once the shared square axis is forbidden. -/
theorem coprimeCofactorBranches_are_repairPacking_without_axis
    {r N p : ℕ} {B : Finset ℕ}
    (hp : p.Prime)
    (hPairwise : ∀ b ∈ B, ∀ c ∈ B, b ≠ c → b.Coprime c) :
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
      (RootQuotientSquareAxisCofactorTargetFinset p B) := by
  classical
  intro g hgC t ht u hu hgT hgU
  obtain ⟨b, hbB, rfl⟩ := Finset.mem_image.1 ht
  obtain ⟨c, hcB, rfl⟩ := Finset.mem_image.1 hu
  by_cases hbcEq : b = c
  · subst c
    rfl
  · have hgSq :=
      common_composite_divisor_of_coprime_squareAxisBranches_eq_square
        (r := r) (N := N) (p := p) (b := b) (c := c) (g := g)
        hp (hPairwise b hbB c hcB hbcEq) hgC.1 hgT hgU
    exact (hgC.2 (by simpa [hgSq])).elim

/-- Every private cofactor branch is repaired by re-adjoining the single shared
square axis `p^2`. -/
theorem privateAxisCofactorBranches_reachable_with_axis_singleton
    {N p : ℕ} {S : Set ℕ}
    (_hp : p.Prime) :
    ∀ t ∈ RootQuotientSquareAxisCofactorTargetFinset p
        (RootQuotientPrivateAxisCofactors N p S),
      RootQuotientProductReachableWithin 2
        ((RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) ∪ ({p ^ 2} : Set ℕ)) t := by
  classical
  intro t ht
  obtain ⟨b, hb, rfl⟩ := Finset.mem_image.1 ht
  have hbMem := mem_privateAxisCofactors_iff.1 hb
  obtain ⟨w, hwLen, hwG, hProd⟩ := hbMem.2.2.1
  let u : List ℕ := p ^ 2 :: w
  refine ⟨u, ?_, ?_, ?_⟩
  · dsimp [u]
    simp
    omega
  · intro g hg
    dsimp [u] at hg
    simp at hg
    rcases hg with rfl | hgW
    · exact Or.inr (by simp)
    · exact Or.inl (hwG g hgW)
  · dsimp [u]
    simp [rootQuotientWordProduct]
    exact congrArg (fun x => p ^ 2 * x) hProd

/-- **Coprime private-axis fanout lower bound.**

Any pairwise-coprime subfamily `B` of private cofactors behaves like independent
branches once `p^2` is forbidden.  Consequently every finite replacement
dictionary that avoids the shared axis and repairs those branches needs at
least `|B|` distinct types. -/
theorem coprime_privateAxisFanout_card_le_replacement_storage
    {r N p : ℕ} {S R : Set ℕ} {B : Finset ℕ}
    (hp : p.Prime)
    (hBSub : B ⊆ RootQuotientPrivateAxisCofactors N p S)
    (hPairwise : ∀ b ∈ B, ∀ c ∈ B, b ≠ c → b.Coprime c)
    (hRFinite : R.Finite)
    (hRCandidate : R ⊆
      RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
    (hRepair : ∀ t ∈ RootQuotientSquareAxisCofactorTargetFinset p B,
      RootQuotientProductReachableWithin 2
        ((RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) ∪ R) t) :
    B.card ≤ R.ncard := by
  let G := RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})
  have hNoBase : ∀ t ∈ RootQuotientSquareAxisCofactorTargetFinset p B,
      ¬RootQuotientProductReachableWithin 2 G t := by
    classical
    intro t ht
    obtain ⟨b, hbB, rfl⟩ := Finset.mem_image.1 ht
    have hbPriv := mem_privateAxisCofactors_iff.1 (hBSub hbB)
    simpa [G] using hbPriv.2.2.2
  have hHit : ∀ t ∈ RootQuotientSquareAxisCofactorTargetFinset p B,
      ∃ g : ℕ, g ∈ R ∧ g ∣ t := by
    apply spare_family_divisor_covers_base_hard_targets
    · intro t ht
      simpa [G, Set.union_assoc] using hRepair t ht
    · exact hNoBase
  have hCover : RootQuotientRepairDivisorCover
      (RootQuotientSquareAxisCofactorTargetFinset p B)
      (RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ)) R :=
    ⟨hRCandidate, hHit⟩
  have hPack := coprimeCofactorBranches_are_repairPacking_without_axis
    (r := r) (N := N) (p := p) (B := B) hp hPairwise
  have hLower := repairDivisorPacking_card_le_cover_ncard
    (T := RootQuotientSquareAxisCofactorTargetFinset p B)
    (U := RootQuotientSquareAxisCofactorTargetFinset p B)
    (C := RootQuotientSemanticCompositeCandidates r N \ ({p ^ 2} : Set ℕ))
    (S := R) (by simp) hPack hRFinite hCover
  rw [squareAxisCofactorTargetFinset_card_eq hp B] at hLower
  exact hLower

/-- **Exact preinvestment yields a nonempty private-axis cofactor set.**

At a cubic prime birth, if some old minimum exact presentation has preinvested
in `p^2`, then there exists such a minimum presentation whose generalized
private cofactor family is nonempty. -/
theorem exists_minimum_exactPreinvestment_with_nonempty_privateAxisCofactors
    {r N p : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ 3)
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N 2 p) :
    ∃ S : Set ℕ,
      RootQuotientCompositeMacroPresentation r N 2 S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N 2 ∧
      p ^ 2 ∈ S ∧
      (RootQuotientPrivateAxisCofactors N p S).Nonempty := by
  classical
  obtain ⟨S, t, b, hS, hSCard, hpSq, htHard, htNoReach,
      hbTwo, hbLt, hbLiteral, hFactor⟩ :=
    exactPrimeDirectionPreinvestment_horizonTwo_has_private_literal_cofactor
      hr hp hBirth hPre
  have hbReach : RootQuotientProductReachableWithin 1
      (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) b := by
    refine ⟨[b], by simp, ?_, ?_⟩
    · intro g hg
      have hgEq : g = b := by simpa using hg
      subst g
      exact hbLiteral
    · simp [rootQuotientWordProduct]
  have hbPriv : b ∈ RootQuotientPrivateAxisCofactors N p S := by
    apply mem_privateAxisCofactors_iff.2
    exact ⟨hbLt, hbTwo, hbReach, by simpa [hFactor] using htNoReach⟩
  exact ⟨S, hS, hSCard, hpSq, ⟨b, hbPriv⟩⟩

end EnterpriseMath.Quotient
