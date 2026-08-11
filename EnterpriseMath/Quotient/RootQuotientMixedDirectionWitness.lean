import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import EnterpriseMath.Quotient.RootQuotientHardPrimeDirectionStorage
import EnterpriseMath.Quotient.RootQuotientFactorGeometryAlgebra
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A bounded denominator witnesses genuinely mixed-direction storage pressure
at horizon `h` when it is too expensive prime-only, but it uses every hard pure
prime direction with exponent at most one.

If all available macro slots are already consumed by hard pure directions, each
such macro is a composite pure prime power and therefore cannot divide this
witness. -/
def RootQuotientMixedDirectionWitness
    (N h b : ℕ) : Prop :=
  1 ≤ b ∧
  b ≤ N ∧
  h < rootQuotientPrimeFactorCount b ∧
  ∀ p : ℕ,
    p ∈ RootQuotientHardPrimeDirections N h →
      b.factorization p ≤ 1

/-- If the true optional-macro count equals the pure-direction demand, then a
minimum presentation has no spare macro types: every macro in it serves some
hard prime direction. -/
theorem every_minimumMacro_serves_hardDirection_of_no_mixedOverhead
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = rootQuotientMinimumCompositeMacroCount r N h)
    (hNoMixed : rootQuotientMixedDirectionMacroOverhead r N h = 0) :
    ∀ g : ℕ, g ∈ S →
      ∃ p : ℕ,
        p ∈ RootQuotientHardPrimeDirections N h ∧
        RootQuotientMacroServesPrimeDirection g p := by
  classical
  let H := RootQuotientHardPrimeDirections N h
  have hDirLe := primeDirectionDemand_le_minimumCompositeMacroCount
    hr hh hBinary
  have hMuEqDir : rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientPrimeDirectionDemand N h := by
    dsimp [rootQuotientMixedDirectionMacroOverhead] at hNoMixed
    omega
  have hHardCard : H.ncard = rootQuotientPrimeDirectionDemand N h := by
    dsimp [H, rootQuotientPrimeDirectionDemand]
    exact rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff N h
  have hServe : ∀ p : ℕ, p ∈ H →
      ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
    intro p hp
    exact exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hS.2.1 hS.2.2 hp
  let f : ℕ → ℕ := fun p =>
    if hp : p ∈ H then Classical.choose (hServe p hp) else 1
  have hfSpec : ∀ p : ℕ, (hp : p ∈ H) →
      f p ∈ S ∧ RootQuotientMacroServesPrimeDirection (f p) p := by
    intro p hp
    dsimp [f]
    rw [dif_pos hp]
    exact Classical.choose_spec (hServe p hp)
  have hInj : Set.InjOn f H := by
    intro p hp q hq hEq
    have hpPrime : p.Prime := hp.1
    have hqPrime : q.Prime := hq.1
    have hqServeAsP : RootQuotientMacroServesPrimeDirection (f p) q := by
      rw [hEq]
      exact (hfSpec q hq).2
    exact primeDirection_eq_of_macro_serves_both
      hpPrime hqPrime (hfSpec p hp).2 hqServeAsP
  have hImageSub : f '' H ⊆ S := by
    rintro g ⟨p, hp, rfl⟩
    exact (hfSpec p hp).1
  have hImageCard : (f '' H).ncard = S.ncard := by
    calc
      (f '' H).ncard = H.ncard := hInj.ncard_image
      _ = rootQuotientPrimeDirectionDemand N h := hHardCard
      _ = rootQuotientMinimumCompositeMacroCount r N h := hMuEqDir.symm
      _ = S.ncard := hSCard.symm
  have hImageEq : f '' H = S :=
    Set.eq_of_subset_of_ncard_le hImageSub hImageCard.symm.le hS.1
  intro g hg
  have hgImage : g ∈ f '' H := by
    rw [hImageEq]
    exact hg
  obtain ⟨p, hpH, hfp⟩ := hgImage
  refine ⟨p, hpH, ?_⟩
  rw [← hfp]
  exact (hfSpec p hpH).2

/-- A macro in a no-mixed-overhead minimum presentation cannot divide a mixed
witness: it is a composite pure power of a hard prime, while the witness uses
that prime with exponent at most one. -/
theorem minimumMacro_not_dvd_mixedWitness_of_no_mixedOverhead
    {r N h b g : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = rootQuotientMinimumCompositeMacroCount r N h)
    (hNoMixed : rootQuotientMixedDirectionMacroOverhead r N h = 0)
    (hb : RootQuotientMixedDirectionWitness N h b)
    (hgS : g ∈ S) :
    ¬g ∣ b := by
  intro hgDvd
  obtain ⟨p, hpH, hgServe⟩ :=
    every_minimumMacro_serves_hardDirection_of_no_mixedOverhead
      hr hh hBinary hS hSCard hNoMixed g hgS
  have hpPrime : p.Prime := hpH.1
  have hpPowLeN : p ^ (h + 1) ≤ N := hpH.2
  have hpLePow : p ≤ p ^ (h + 1) := by
    calc
      p = p ^ 1 := by simp
      _ ≤ p ^ (h + 1) := Nat.pow_le_pow_right hpPrime.one_le (by omega)
  have hpN : p ≤ N := hpLePow.trans hpPowLeN
  obtain ⟨e, hePos, hgeq⟩ := hgServe
  have heTwo : 2 ≤ e := by
    by_contra hNot
    have heOne : e = 1 := by omega
    have hgEqP : g = p := by simp [hgeq, heOne]
    have hgNotPrimeBasis := (hS.2.1 hgS).2
    apply hgNotPrimeBasis
    rw [hgEqP]
    exact ⟨hpPrime, hpN⟩
  have hbZero : b ≠ 0 := by omega
  rw [hgeq] at hgDvd
  have heLeFact : e ≤ b.factorization p :=
    (hpPrime.pow_dvd_iff_le_factorization hbZero).1 hgDvd
  have hFactCap : b.factorization p ≤ 1 := hb.2.2.2 p hpH
  omega

/-- **General mixed-direction witness theorem.**

Any mixed witness forces at least one macro type beyond the pure-direction
prime-counting floor.  Equivalently, the mixed-direction overhead is strictly
positive. -/
theorem one_le_mixedDirectionMacroOverhead_of_witness
    {r N h b : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hb : RootQuotientMixedDirectionWitness N h b) :
    1 ≤ rootQuotientMixedDirectionMacroOverhead r N h := by
  by_contra hNot
  have hNoMixed : rootQuotientMixedDirectionMacroOverhead r N h = 0 := by omega
  obtain ⟨S, hS, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation hr hh
  have hbFree : RPowerFree r b :=
    rPowerFree_of_lt_two_pow_rootOrder hb.1 (hb.2.1.trans_lt hBinary)
  have hUnionPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hS.2.1 hgS).1
      omega
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hUnionPos).1 hS.2.2
      b hb.1 hb.2.1 hbFree
  obtain ⟨w, hwLen, hwUnion, hProd⟩ := hReach
  have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro g hgWord
    have hgUnion := hwUnion g hgWord
    rcases hgUnion with hgPrime | hgS
    · exact hgPrime
    · have hgDvd : g ∣ b :=
        word_member_dvd_compiled_product hgWord hProd
      exact (minimumMacro_not_dvd_mixedWitness_of_no_mixedOverhead
        hr hh hBinary hS hSCard hNoMixed hb hgS hgDvd).elim
  have hExact : w.length = rootQuotientPrimeFactorCount b :=
    prime_word_length_eq_primeFactorCount hwPrime hProd.symm
  omega

/-- Storage form of the mixed-witness theorem. -/
theorem directionDemand_add_one_le_minimumCompositeMacroCount_of_witness
    {r N h b : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hb : RootQuotientMixedDirectionWitness N h b) :
    rootQuotientPrimeDirectionDemand N h + 1 ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  have hMix := one_le_mixedDirectionMacroOverhead_of_witness
    hr hh hBinary hb
  have hDecomp := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    hr hh hBinary
  omega

end EnterpriseMath.Quotient
