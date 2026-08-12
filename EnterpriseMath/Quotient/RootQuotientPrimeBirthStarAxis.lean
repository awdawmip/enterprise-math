import EnterpriseMath.Quotient.RootQuotientGlobalSemiprimeCover
import EnterpriseMath.Quotient.RootQuotientPrimeBirthCoverPreinvestment
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A semiprime divisor of `p^h*q`, where `p,q` are distinct primes and `q`
occurs only once, is either the pure square `p^2` or the cross term `p*q`.

This is the local arithmetic kernel behind the prime-birth star/axis
dichotomy. -/
theorem semiprime_dvd_primePow_mul_prime_eq_square_or_cross
    {p q h d : ℕ}
    (hp : p.Prime)
    (hq : q.Prime)
    (hpq : p ≠ q)
    (hdTwo : 2 ≤ d)
    (hdCount : rootQuotientPrimeFactorCount d = 2)
    (hdDvd : d ∣ p ^ h * q) :
    d = p ^ 2 ∨ d = p * q := by
  by_cases hqDvd : q ∣ d
  · rcases hqDvd with ⟨k, rfl⟩
    have hkZero : k ≠ 0 := by
      intro hk
      subst k
      simp at hdTwo
    have hkPos : 1 ≤ k := Nat.one_le_iff_ne_zero.mpr hkZero
    have hqCount : rootQuotientPrimeFactorCount q = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hq]
      simp
    have hCountMul := rootQuotientPrimeFactorCount_mul hq.one_le hkPos
    have hkCount : rootQuotientPrimeFactorCount k = 1 := by
      rw [hCountMul, hqCount] at hdCount
      omega
    have hkOne : k ≠ 1 := by
      intro hk
      subst k
      simp [rootQuotientPrimeFactorCount] at hkCount
    have hkTwo : 2 ≤ k := by omega
    have hkPrime : k.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hkTwo).1 hkCount
    have hkDvd : k ∣ p ^ h := by
      apply Nat.dvd_of_mul_dvd_mul_left hq.pos
      simpa [Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using hdDvd
    have hkp : k = p :=
      prime_eq_prime_of_dvd_pow hkPrime hp hkDvd
    right
    rw [hkp]
    exact Nat.mul_comm q p
  · have hdCoprimeQ : d.Coprime q :=
      ((hq.coprime_iff_not_dvd).2 hqDvd).symm
    have hdPow : d ∣ p ^ h :=
      hdCoprimeQ.dvd_of_dvd_mul_right hdDvd
    obtain ⟨k, hkLe, hdEq⟩ := (Nat.dvd_prime_pow hp).1 hdPow
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hp]
      simp
    have hPowCount : rootQuotientPrimeFactorCount (p ^ k) = k := by
      rw [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
      simp
    have hkTwo : k = 2 := by
      rw [hdEq, hPowCount] at hdCount
      omega
    left
    simpa [hdEq, hkTwo]

/-- **No cover preinvestment forces the full future-prime star.**

Let the next state be the hard prime birth `p^(h+1)`.  Before that state is
exposed, if no minimum divisor-cover dictionary has preinvested in the future
`p`-direction, then every minimum semantic-semiprime cover contains `p*q` for
every prime `q<p`.

Indeed, the old hard target `p^h*q` has exactly two possible semantic
semiprime divisors: `p^2` and `p*q`.  Absence of cover preinvestment excludes
the square, forcing the cross edge. -/
theorem no_coverPreinvestment_forces_futurePrimeStar
    {r N h p q : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hp : p.Prime)
    (hq : q.Prime)
    (hqp : q < p)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r)
    (hSFinite : S.Finite)
    (hSemi : RootQuotientRepairSemiprimeCover
      r N (RootQuotientPrimeHardSemanticTargetFinset r N h) S)
    (hSCard : S.ncard = rootQuotientRepairSemiprimeCoverNumber
      r N (RootQuotientPrimeHardSemanticTargetFinset r N h))
    (hNoPre : ¬RootQuotientCoverPrimeDirectionPreinvestment r N h p) :
    p * q ∈ S := by
  have hpSqNot : p ^ 2 ∉ S := by
    intro hpSq
    have hGeneric : RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
      repairSemiprimeCover_is_semanticCompositeDivisorCover hSemi
    have hCoverEq := globalRepairDivisorCoverNumber_eq_semiprimeCoverNumber
      (r := r) (N := N) (h := h) (by omega)
    have hCardGlobal : S.ncard =
        rootQuotientGlobalRepairDivisorCoverNumber r N h := by
      rw [hCoverEq]
      exact hSCard
    apply hNoPre
    exact ⟨S, hSFinite, hGeneric, hCardGlobal,
      ⟨2, by omega, hh, hpSq⟩⟩
  let t := p ^ h * q
  have hPowPos : 0 < p ^ h := Nat.pow_pos hp.pos
  have htLtBirth : t < p ^ (h + 1) := by
    dsimp [t]
    rw [pow_succ]
    exact Nat.mul_lt_mul_left hPowPos hqp
  have htN : t ≤ N := by
    rw [← hBirth] at htLtBirth
    omega
  have htPos : 1 ≤ t := by
    dsimp [t]
    positivity
  have htFree : RPowerFree r t :=
    rPowerFree_of_lt_two_pow_rootOrder htPos
      (htN.trans_lt (by omega))
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hp]
    simp
  have hqCount : rootQuotientPrimeFactorCount q = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hq]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ h) = h := by
    rw [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    simp
  have htCount : rootQuotientPrimeFactorCount t = h + 1 := by
    dsimp [t]
    rw [rootQuotientPrimeFactorCount_mul (by positivity) hq.one_le,
      hPowCount, hqCount]
  have htHard : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    apply (mem_primeHardSemanticTargetFinset_iff).2
    exact ⟨⟨by omega, htN, htFree⟩, by omega⟩
  obtain ⟨d, hdS, hdDvd⟩ := hSemi.2 t htHard
  have hdSemantic := hSemi.1.1 hdS
  have hdCount := hSemi.1.2 d hdS
  have hdCases := semiprime_dvd_primePow_mul_prime_eq_square_or_cross
    hp hq (by omega) hdSemantic.1 hdCount (by simpa [t] using hdDvd)
  rcases hdCases with hdSq | hdCross
  · exact (hpSqNot (hdSq ▸ hdS)).elim
  · simpa [hdCross] using hdS

end EnterpriseMath.Quotient
