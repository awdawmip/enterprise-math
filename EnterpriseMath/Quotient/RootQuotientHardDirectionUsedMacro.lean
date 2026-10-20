import EnterpriseMath.Quotient.RootQuotientHardPrimeDirectionStorage
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Used hard-direction macro witness.**

For a hard prime direction `p`, every high-root separator contains an optional
macro that actually occurs in a successful horizon-`h` word for `p^(h+1)`.
Consequently the macro is `p^e` with `1<=e<=h+1` and divides the hard target.

This strengthens mere dictionary-level existence to an execution-relevant
witness and makes fixed-horizon exponent searches genuinely finite. -/
theorem exists_used_macro_serving_hardPrimeDirection_of_separator
    {r N h p : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hpHard : p ∈ RootQuotientHardPrimeDirections N h) :
    ∃ g e : ℕ,
      g ∈ S ∧
      1 ≤ e ∧
      e ≤ h + 1 ∧
      g = p ^ e ∧
      g ∣ p ^ (h + 1) := by
  classical
  have hpPrime : p.Prime := hpHard.1
  have hpPowLeN : p ^ (h + 1) ≤ N := hpHard.2
  have hpPowPos : 1 ≤ p ^ (h + 1) := by positivity
  have hpPowFree : RPowerFree r (p ^ (h + 1)) :=
    rPowerFree_of_lt_two_pow_rootOrder hpPowPos
      (hpPowLeN.trans_lt hBinary)
  have hUnionPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hSFamily hgS).1
      omega
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hUnionPos).1 hSep
      (p ^ (h + 1)) hpPowPos hpPowLeN hpPowFree
  obtain ⟨w, hwLen, hwUnion, hProd⟩ := hReach
  have hSpareUsed : ∃ g : ℕ, g ∈ w ∧ g ∈ S := by
    by_contra hNo
    push_neg at hNo
    have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
      intro g hgWord
      have hgUnion := hwUnion g hgWord
      rcases hgUnion with hgPrime | hgS
      · exact hgPrime
      · exact (hNo g hgWord hgS).elim
    have hExact : w.length =
        rootQuotientPrimeFactorCount (p ^ (h + 1)) :=
      prime_word_length_eq_primeFactorCount hwPrime hProd.symm
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hpPrime]
      simp
    have hPowCount :
        rootQuotientPrimeFactorCount (p ^ (h + 1)) = h + 1 := by
      rw [rootQuotientPrimeFactorCount_pow hpPrime.one_le, hpCount]
      simp
    rw [hPowCount] at hExact
    omega
  obtain ⟨g, hgWord, hgS⟩ := hSpareUsed
  have hgSemantic := (hSFamily hgS).1
  have hgDvd : g ∣ p ^ (h + 1) :=
    word_member_dvd_compiled_product hgWord hProd
  have hgServe : RootQuotientMacroServesPrimeDirection g p :=
    macroServesPrimeDirection_of_dvd_primePow
      hpPrime hgSemantic.1 hgDvd
  obtain ⟨e, hePos, hgeq⟩ := hgServe
  have hpPowZero : p ^ (h + 1) ≠ 0 := by positivity
  have heLe : e ≤ h + 1 := by
    have hPowDvd : p ^ e ∣ p ^ (h + 1) := by
      rw [← hgeq]
      exact hgDvd
    have hFactLe : e ≤ (p ^ (h + 1)).factorization p :=
      (hpPrime.pow_dvd_iff_le_factorization hpPowZero).1 hPowDvd
    rw [Nat.factorization_pow_self hpPrime] at hFactLe
    exact hFactLe
  exact ⟨g, e, hgS, hePos, heLe, hgeq, hgDvd⟩

/-- Composite-macro normalization upgrades the used exponent lower bound from
one to two: exponent one would make the stored instruction the forced prime
itself. -/
theorem exists_used_composite_power_for_hardPrimeDirection
    {r N h p : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hpHard : p ∈ RootQuotientHardPrimeDirections N h) :
    ∃ g e : ℕ,
      g ∈ S ∧
      2 ≤ e ∧
      e ≤ h + 1 ∧
      g = p ^ e ∧
      g ∣ p ^ (h + 1) := by
  obtain ⟨g, e, hgS, hePos, heLe, hgeq, hgDvd⟩ :=
    exists_used_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hSFamily hSep hpHard
  have heTwo : 2 ≤ e := by
    by_contra hNot
    have heOne : e = 1 := by omega
    have hgPrime : g ∈ RootQuotientPrimeBasis N := by
      rw [hgeq, heOne]
      refine ⟨hpHard.1, ?_⟩
      have hpLePow : p ≤ p ^ (h + 1) := by
        calc
          p = p ^ 1 := by simp
          _ ≤ p ^ (h + 1) :=
            Nat.pow_le_pow_right hpHard.1.one_le (by omega)
      exact hpLePow.trans hpHard.2
    exact (hSFamily hgS).2 hgPrime
  exact ⟨g, e, hgS, heTwo, heLe, hgeq, hgDvd⟩

end EnterpriseMath.Quotient
