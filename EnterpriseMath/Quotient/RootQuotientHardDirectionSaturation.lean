import EnterpriseMath.Quotient.RootQuotientHardPrimeDirectionStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- At hard-direction saturation, the optional-macro cardinality is forced to be
exactly the hard-direction count. -/
theorem hardPrimeDirections_ncard_eq_macroFamily_of_saturated_separator
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hCard : S.ncard ≤ (RootQuotientHardPrimeDirections N h).ncard) :
    S.ncard = (RootQuotientHardPrimeDirections N h).ncard := by
  have hLower := hardPrimeDirections_ncard_le_macroFamily_of_separator
    hr hBinary hSFinite hSFamily hSep
  omega

/-- **Hard-direction slot-saturation theorem.**

Suppose a separator has no more optional macro slots than there are hard pure
prime directions.  The universal hard-direction injection then saturates every
slot: every macro in the family serves one hard prime direction and hence is a
positive pure power of that prime.

This is the general mechanism that removes arbitrary mixed macros from fixed-
storage optimization once enough pure-prime directions become hard. -/
theorem every_macro_serves_hardDirection_of_saturated_separator
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hCard : S.ncard ≤ (RootQuotientHardPrimeDirections N h).ncard) :
    ∀ g : ℕ, g ∈ S →
      ∃ p : ℕ,
        p ∈ RootQuotientHardPrimeDirections N h ∧
        RootQuotientMacroServesPrimeDirection g p := by
  classical
  let H := RootQuotientHardPrimeDirections N h
  have hServe : ∀ p : ℕ, p ∈ H →
      ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
    intro p hp
    exact exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hSFamily hSep hp
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
  have hCardEq : S.ncard = H.ncard := by
    dsimp [H]
    exact hardPrimeDirections_ncard_eq_macroFamily_of_saturated_separator
      hr hBinary hSFinite hSFamily hSep hCard
  have hImageCard : (f '' H).ncard = S.ncard := by
    calc
      (f '' H).ncard = H.ncard := hInj.ncard_image
      _ = S.ncard := hCardEq.symm
  have hImageEq : f '' H = S :=
    Set.eq_of_subset_of_ncard_le hImageSub hImageCard.symm.le hSFinite
  intro g hg
  have hgImage : g ∈ f '' H := by
    rw [hImageEq]
    exact hg
  obtain ⟨p, hpH, hfp⟩ := hgImage
  refine ⟨p, hpH, ?_⟩
  rw [← hfp]
  exact (hfSpec p hpH).2

/-- Saturation corollary with the pure-power structure exposed directly. -/
theorem every_macro_is_pure_power_of_hardPrime_of_saturated_separator
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hCard : S.ncard ≤ (RootQuotientHardPrimeDirections N h).ncard) :
    ∀ g : ℕ, g ∈ S →
      ∃ p e : ℕ,
        p ∈ RootQuotientHardPrimeDirections N h ∧
        1 ≤ e ∧ g = p ^ e := by
  intro g hg
  obtain ⟨p, hpH, e, he, hEq⟩ :=
    every_macro_serves_hardDirection_of_saturated_separator
      hr hBinary hSFinite hSFamily hSep hCard g hg
  exact ⟨p, e, hpH, he, hEq⟩

end EnterpriseMath.Quotient
