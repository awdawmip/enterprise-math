import EnterpriseMath.Quotient.RootQuotientPrimeBirthAxisFanout
import EnterpriseMath.Quotient.RootQuotientPrimeBirthHorizonTwoConflict
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A semantic composite divisor of `p^2*q` for distinct primes `p,q` has only
three possible shapes: the shared square axis, the star edge, or the whole
branch target itself. -/
theorem composite_dvd_primeSquare_mul_prime_eq_axis_or_star_or_literal
    {r N p q g : ℕ}
    (hp : p.Prime)
    (hq : q.Prime)
    (_hpq : p ≠ q)
    (hgC : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgDvd : g ∣ p ^ 2 * q) :
    g = p ^ 2 ∨ g = p * q ∨ g = p ^ 2 * q := by
  by_cases hqDvd : q ∣ g
  · rcases hqDvd with ⟨k, rfl⟩
    have hkDvd : k ∣ p ^ 2 := by
      apply Nat.dvd_of_mul_dvd_mul_left hq.pos
      simpa [Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using hgDvd
    obtain ⟨e, heLe, hkEq⟩ := (Nat.dvd_prime_pow hp).1 hkDvd
    have hgSemantic := hgC.1
    have hRank : 2 ≤ rootQuotientPrimeFactorCount (q * k) := by
      have hCountPos : 0 < rootQuotientPrimeFactorCount (q * k) :=
        rootQuotientPrimeFactorCount_pos_of_two_le hgSemantic.1
      by_contra hNot
      have hCountOne : rootQuotientPrimeFactorCount (q * k) = 1 := by omega
      have hgPrime : (q * k).Prime :=
        (rootQuotientPrimeFactorCount_eq_one_iff_prime hgSemantic.1).1 hCountOne
      exact hgC.2 ⟨hgPrime, hgSemantic.2.1⟩
    have hqCount : rootQuotientPrimeFactorCount q = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hq]
      simp
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hp]
      simp
    have hkCount : rootQuotientPrimeFactorCount k = e := by
      rw [hkEq, rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
      simp
    have hCountMul := rootQuotientPrimeFactorCount_mul hq.one_le (by
      by_cases hkZero : k = 0
      · subst k
        simp at hgSemantic
      · exact Nat.one_le_iff_ne_zero.mpr hkZero)
    rw [hqCount, hkCount] at hCountMul
    have hePos : 1 ≤ e := by omega
    have heCases : e = 1 ∨ e = 2 := by omega
    rcases heCases with rfl | rfl
    · right; left
      rw [hkEq, pow_one]
      exact Nat.mul_comm q p
    · right; right
      rw [hkEq]
      ac_rfl
  · have hgCoprimeQ : g.Coprime q :=
      ((hq.coprime_iff_not_dvd).2 hqDvd).symm
    have hgPow : g ∣ p ^ 2 :=
      hgCoprimeQ.dvd_of_dvd_mul_right hgDvd
    obtain ⟨e, heLe, hgEq⟩ := (Nat.dvd_prime_pow hp).1 hgPow
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
    have hPowCount : rootQuotientPrimeFactorCount (p ^ e) = e := by
      rw [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
      simp
    have heTwo : e = 2 := by
      rw [hgEq, hPowCount] at hRank
      omega
    left
    simpa [hgEq, heTwo]

/-- The old cubic branch `p^2*q` is prime-hard at horizon two whenever `q<p`
and the next state is the birth `p^3`. -/
theorem primeSquare_mul_smallerPrime_mem_old_primeHard
    {r N p q : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hq : q.Prime)
    (hqp : q < p)
    (hBirth : N + 1 = p ^ 3)
    (hBinaryNext : N + 1 < 2 ^ r) :
    p ^ 2 * q ∈ RootQuotientPrimeHardSemanticTargetFinset r N 2 := by
  have hPowPos : 0 < p ^ 2 := Nat.pow_pos hp.pos
  have hLtBirth : p ^ 2 * q < p ^ 3 := by
    rw [pow_succ]
    exact (Nat.mul_lt_mul_left hPowPos).2 hqp
  have hN : p ^ 2 * q ≤ N := by
    rw [← hBirth] at hLtBirth
    omega
  have hFree : RPowerFree r (p ^ 2 * q) :=
    rPowerFree_of_lt_two_pow_rootOrder (by positivity)
      (hN.trans_lt (by omega))
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hp]
    simp
  have hqCount : rootQuotientPrimeFactorCount q = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hq]
    simp
  have hSqCount : rootQuotientPrimeFactorCount (p ^ 2) = 2 := by
    rw [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    simp
  have hCount : rootQuotientPrimeFactorCount (p ^ 2 * q) = 3 := by
    rw [rootQuotientPrimeFactorCount_mul (by positivity) hq.one_le,
      hSqCount, hqCount]
  apply (mem_primeHardSemanticTargetFinset_iff).2
  exact ⟨⟨by positivity, hN, hFree⟩, by omega⟩

/-- **Cubic branch choice without the shared square axis.**

At horizon two, if an exact optional-macro presentation does not store `p^2`,
then every old branch target `p^2*q` with prime `q<p` forces a q-specific type:
either the semiprime star edge `p*q` or the one-shot literal `p^2*q` itself. -/
theorem exact_without_square_forces_star_or_branchLiteral
    {r N p q : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hq : q.Prime)
    (hqp : q < p)
    (hBirth : N + 1 = p ^ 3)
    (hBinaryNext : N + 1 < 2 ^ r)
    (hS : RootQuotientCompositeMacroPresentation r N 2 S)
    (hpSqNot : p ^ 2 ∉ S) :
    p * q ∈ S ∨ p ^ 2 * q ∈ S := by
  have htHard := primeSquare_mul_smallerPrime_mem_old_primeHard
    hr hp hq hqp hBirth hBinaryNext
  have hRel : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N) 2
      (RootQuotientPrimeHardSemanticTargetFinset r N 2)
      (RootQuotientSemanticCompositeCandidates r N) S :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1
      ((compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hS)
  have hReach := hRel.2.2 (p ^ 2 * q) htHard
  have hNoPrime : ¬RootQuotientProductReachableWithin 2
      (RootQuotientPrimeBasis N) (p ^ 2 * q) := by
    intro hPrimeReach
    have hCountLe :=
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
        (by positivity) (by
          exact (mem_primeHardSemanticTargetFinset_iff).1 htHard |>.1.2.1)).1
        hPrimeReach
    have hCount : rootQuotientPrimeFactorCount (p ^ 2 * q) = 3 := by
      have hpCount : rootQuotientPrimeFactorCount p = 1 := by
        rw [rootQuotientPrimeFactorCount,
          Nat.primeFactorsList_prime hp]
        simp
      have hqCount : rootQuotientPrimeFactorCount q = 1 := by
        rw [rootQuotientPrimeFactorCount,
          Nat.primeFactorsList_prime hq]
        simp
      rw [rootQuotientPrimeFactorCount_mul (by positivity) hq.one_le,
        rootQuotientPrimeFactorCount_pow hp.one_le, hpCount, hqCount]
      simp
    rw [hCount] at hCountLe
    omega
  obtain ⟨g, hgS, hgDvd⟩ :=
    exists_spare_divisor_of_union_reachable_not_base hReach hNoPrime
  have hgCandidate := hS.2.1 hgS
  have hgCases := composite_dvd_primeSquare_mul_prime_eq_axis_or_star_or_literal
    hp hq (by omega) hgCandidate hgDvd
  rcases hgCases with hgSq | hgStar | hgLiteral
  · exact (hpSqNot (hgSq ▸ hgS)).elim
  · exact Or.inl (by simpa [hgStar] using hgS)
  · exact Or.inr (by simpa [hgLiteral] using hgS)

end EnterpriseMath.Quotient
