import EnterpriseMath.Quotient.RootQuotientPrimeBirthPrivateCofactor
import EnterpriseMath.Quotient.RootQuotientPrimeBirthStarAxis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Strong horizon-two private-cofactor certificate.**

At a cubic prime birth, exact preinvestment in the future direction is
necessarily `p^2`; it owns a private old hard target `t=p^2*b`, where
`2≤b<p`, `b` is already a literal primitive after deleting `p^2`, and `t`
becomes unreachable in two steps once `p^2` is removed. -/
theorem exactPrimeDirectionPreinvestment_horizonTwo_has_private_literal_cofactor
    {r N p : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ 3)
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N 2 p) :
    ∃ S : Set ℕ, ∃ t b : ℕ,
      RootQuotientCompositeMacroPresentation r N 2 S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N 2 ∧
      p ^ 2 ∈ S ∧
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N 2 ∧
      ¬RootQuotientProductReachableWithin 2
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) t ∧
      2 ≤ b ∧ b < p ∧
      b ∈ RootQuotientPrimeBasis N ∪ (S \ {p ^ 2}) ∧
      p ^ 2 * b = t := by
  obtain ⟨S, hS, hSCard, e, heTwo, heLe, heMem⟩ := hPre
  obtain ⟨t, htHard, htReach, htNoReach, _htDvd⟩ :=
    exists_private_primeHard_target_of_mem_minimumCompositeMacroPresentation
      hr (by omega) hS hSCard heMem
  obtain ⟨j, b, hjPos, _hjLe, hbReach, hFactor⟩ :=
    private_target_decomposes_into_macro_power_and_residual
      (N := N) (h := 2) (g := p ^ e) (t := t) (S := S)
      heMem htReach htNoReach
  have htMem := (mem_primeHardSemanticTargetFinset_iff).1 htHard
  have heEq : e = 2 := by omega
  subst e
  have hejLe : 2 * j ≤ 2 := by
    have hPowDvd : p ^ (2 * j) ∣ t := by
      refine ⟨b, ?_⟩
      calc
        p ^ (2 * j) * b = (p ^ 2) ^ j * b := by rw [pow_mul]
        _ = t := hFactor
    have hPowLeT : p ^ (2 * j) ≤ t := Nat.le_of_dvd (by omega) hPowDvd
    by_contra hNot
    have hPowerLe : p ^ 3 ≤ p ^ (2 * j) :=
      pow_le_pow_right' hp.one_le (by omega)
    have : N + 1 ≤ N := by
      rw [hBirth]
      exact hPowerLe.trans (hPowLeT.trans htMem.1.2.1)
    omega
  have hjEq : j = 1 := by omega
  subst j
  have hFactor' : p ^ 2 * b = t := by simpa using hFactor
  have hbPos : 1 ≤ b := by
    by_contra hbZero
    have hbEq : b = 0 := by omega
    rw [hbEq] at hFactor'
    simp at hFactor'
    omega
  have hbNotOne : b ≠ 1 := by
    intro hbOne
    subst b
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hp]
      simp
    have hCount : rootQuotientPrimeFactorCount t = 2 := by
      rw [← hFactor']
      simp [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    omega
  have hbTwo : 2 ≤ b := by omega
  have htLtBirth : t < p ^ 3 := by
    rw [← hBirth]
    omega
  have hPowPos : 0 < p ^ 2 := Nat.pow_pos hp.pos
  have hbLt : b < p := by
    have hMulLt : p ^ 2 * b < p ^ 2 * p := by
      rw [hFactor']
      simpa [pow_succ] using htLtBirth
    exact (Nat.mul_lt_mul_left hPowPos).1 hMulLt
  have hbLiteral : b ∈ RootQuotientPrimeBasis N ∪ (S \ {p ^ 2}) :=
    mem_generators_of_reachableWithin_one_of_two_le hbTwo
      (by simpa using hbReach)
  exact ⟨S, t, b, hS, hSCard, heMem, htHard, htNoReach,
    hbTwo, hbLt, hbLiteral, hFactor'⟩

/-- **A private square-cofactor target forbids its intermediate lift.**

If `p^2*b` is private to the stored square `p^2`, with `b<p`, then the same
exact dictionary cannot also store `p*b`; otherwise `(p*b)*p` would still
compile the target after deleting `p^2`.

This is the factor-lattice `L`-shape forced by horizon-two axis preinvestment:
`p^2` and the lower cofactor are present, while the intermediate lift `p*b` is
absent. -/
theorem prime_cofactor_lift_not_mem_exact_of_private_square
    {N p b t : ℕ} {S : Set ℕ}
    (hp : p.Prime)
    (hbTwo : 2 ≤ b)
    (hbp : b < p)
    (hBirth : N + 1 = p ^ 3)
    (hNoReach : ¬RootQuotientProductReachableWithin 2
      (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) t)
    (hFactor : p ^ 2 * b = t) :
    p * b ∉ S := by
  intro hpbS
  have hpN : p ≤ N := by
    have hpLt : p < p ^ 3 := by
      calc
        p = p ^ 1 := by simp
        _ < p ^ 3 := pow_lt_pow_right' hp.one_lt (by omega)
    rw [← hBirth] at hpLt
    omega
  have hpMem : p ∈ RootQuotientPrimeBasis N := ⟨hp, hpN⟩
  have hpbNeSq : p * b ≠ p ^ 2 := by
    intro hEq
    have hpPos : 0 < p := hp.pos
    have hCancel : b = p := by
      apply Nat.eq_of_mul_eq_mul_left hpPos
      simpa [pow_two, Nat.mul_assoc] using hEq
    omega
  have hpbRest : p * b ∈ S \ {p ^ 2} :=
    ⟨hpbS, by simpa [hpbNeSq]⟩
  let w : List ℕ := [p * b, p]
  apply hNoReach
  refine ⟨w, ?_, ?_, ?_⟩
  · simp [w]
  · intro g hg
    simp [w] at hg
    rcases hg with rfl | rfl
    · exact Or.inr hpbRest
    · exact Or.inl hpMem
  · dsimp [w]
    simp [rootQuotientWordProduct, hFactor,
      pow_two, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Prime-cofactor specialization of the missing-lift theorem. -/
theorem prime_cross_not_mem_exact_of_private_square_prime_cofactor
    {N p q t : ℕ} {S : Set ℕ}
    (hp : p.Prime)
    (_hq : q.Prime)
    (hqp : q < p)
    (hBirth : N + 1 = p ^ 3)
    (_hpSqMem : p ^ 2 ∈ S)
    (hNoReach : ¬RootQuotientProductReachableWithin 2
      (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) t)
    (hFactor : p ^ 2 * q = t) :
    p * q ∉ S :=
  prime_cofactor_lift_not_mem_exact_of_private_square
    hp (by omega) hqp hBirth hNoReach hFactor

/-- **Horizon-two exact-preinvestment dichotomy.**

At a cubic prime birth, a preinvested future square `p^2` has a private
cofactor `b<p`.  Since that cofactor is already a literal after deleting
`p^2`, exactly one of two structural branches occurs:

* `b` is a bounded prime, in which case the exact optimum omits the star edge
  `p*b`;
* `b` is itself an older composite macro in the same exact optimum, strictly
  below the future prime `p`.

In both branches the intermediate lift `p*b` is absent. -/
theorem horizonTwo_exactPreinvestment_starEdge_or_lowerCompositeMacro
    {r N p : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ 3)
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N 2 p) :
    ∃ S : Set ℕ, ∃ t b : ℕ,
      RootQuotientCompositeMacroPresentation r N 2 S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N 2 ∧
      p ^ 2 ∈ S ∧
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N 2 ∧
      2 ≤ b ∧ b < p ∧ p ^ 2 * b = t ∧ p * b ∉ S ∧
      (b.Prime ∨ (b ∈ S \ {p ^ 2} ∧ ¬b.Prime)) := by
  obtain ⟨S, t, b, hS, hSCard, hpSq, htHard, htNoReach,
      hbTwo, hbLt, hbLiteral, hFactor⟩ :=
    exactPrimeDirectionPreinvestment_horizonTwo_has_private_literal_cofactor
      hr hp hBirth hPre
  have hLiftNot : p * b ∉ S :=
    prime_cofactor_lift_not_mem_exact_of_private_square
      hp hbTwo hbLt hBirth htNoReach hFactor
  by_cases hbPrimeBasis : b ∈ RootQuotientPrimeBasis N
  · exact ⟨S, t, b, hS, hSCard, hpSq, htHard,
      hbTwo, hbLt, hFactor, hLiftNot, Or.inl hbPrimeBasis.1⟩
  · have hbRest : b ∈ S \ {p ^ 2} :=
      hbLiteral.resolve_left hbPrimeBasis
    have hbNotPrime : ¬b.Prime := by
      intro hbPrime
      have hbN : b ≤ N := (hS.2.1 hbRest.1).1.2.1
      exact hbPrimeBasis ⟨hbPrime, hbN⟩
    exact ⟨S, t, b, hS, hSCard, hpSq, htHard,
      hbTwo, hbLt, hFactor, hLiftNot, Or.inr ⟨hbRest, hbNotPrime⟩⟩

/-- **Horizon-two dual-catchup prime-branch conflict.**

At a cubic prime birth, if cover has not preinvested in `p^2` but exact storage
has, then every minimum semiprime cover contains the full `p`-star.  Whenever
the exact private cofactor is a prime `q`, the same edge `p*q` is absent from
that exact optimum.

Thus the two layers make opposite storage choices on a concrete star edge. -/
theorem horizonTwo_exactOnlyPreinvestment_primeBranch_starConflict
    {r N p q : ℕ} {C S : Set ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hq : q.Prime)
    (hqp : q < p)
    (hBirth : N + 1 = p ^ 3)
    (hBinaryNext : N + 1 < 2 ^ r)
    (hCFinite : C.Finite)
    (hCover : RootQuotientRepairSemiprimeCover
      r N (RootQuotientPrimeHardSemanticTargetFinset r N 2) C)
    (hCCard : C.ncard = rootQuotientRepairSemiprimeCoverNumber
      r N (RootQuotientPrimeHardSemanticTargetFinset r N 2))
    (hNoCoverPre : ¬RootQuotientCoverPrimeDirectionPreinvestment r N 2 p)
    (_hS : RootQuotientCompositeMacroPresentation r N 2 S)
    (_hSCard : S.ncard = rootQuotientMinimumCompositeMacroCount r N 2)
    (hpSqS : p ^ 2 ∈ S)
    (t : ℕ)
    (hPrivate : ¬RootQuotientProductReachableWithin 2
      (RootQuotientPrimeBasis N ∪ (S \ {p ^ 2})) t)
    (hFactor : p ^ 2 * q = t) :
    p * q ∈ C ∧ p * q ∉ S := by
  constructor
  · exact no_coverPreinvestment_forces_futurePrimeStar
      hr (by omega) hp hq hqp hBirth hBinaryNext
      hCFinite hCover hCCard hNoCoverPre
  · exact prime_cross_not_mem_exact_of_private_square_prime_cofactor
      hp hq hqp hBirth hpSqS hPrivate hFactor

end EnterpriseMath.Quotient
