import EnterpriseMath.Quotient.RootQuotientLeastPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A primitive denominator is forced at fixed horizon when it belongs to
every positive primitive alphabet separating the bounded exact-state domain. -/
def RootQuotientGeneratorForced
    (r N h g : ℕ) : Prop :=
  ∀ G : Set ℕ,
    PositiveRootQuotientGenerators G →
    SeparatesRootQuotientWordsUpTo r N h G →
    g ∈ G

/-- At every horizon at least two, the exact forced primitive core is the
bounded prime alphabet.

This statement is independent of whether an inclusion-least separating
alphabet exists.  In the intermediate phase the same prime core is forced even
though no least presentation exists. -/
theorem rootQuotientGeneratorForced_iff_primeBasis
    {r N h g : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    RootQuotientGeneratorForced r N h g ↔
      g ∈ RootQuotientPrimeBasis N := by
  constructor
  · intro hForced
    have hBaseSep :
        SeparatesRootQuotientWordsUpTo
          r N h (RootQuotientNontrivialPowerFreeBasis r N) :=
      separatesRootQuotientWordsUpTo_mono_horizon (by omega)
        (rootQuotientNontrivialPowerFreeBasis_separates_at_one (by omega))
    have hgBase : g ∈ RootQuotientNontrivialPowerFreeBasis r N :=
      hForced RootQuotientNontrivialPowerFreeBasis
        rootQuotientNontrivialPowerFreeBasis_positive hBaseSep
    have hgPrime : g.Prime := by
      by_contra hgNotPrime
      have hOmitSep :
          SeparatesRootQuotientWordsUpTo
            r N h (RootQuotientCompositeOmissionBasis r N g) :=
        rootQuotientCompositeOmissionBasis_separates
          (by omega) hgBase.1 hgBase.2.1 hgNotPrime hh
      have hgOmit : g ∈ RootQuotientCompositeOmissionBasis r N g :=
        hForced RootQuotientCompositeOmissionBasis
          rootQuotientCompositeOmissionBasis_positive hOmitSep
      exact hgOmit.2 rfl
    exact ⟨hgPrime, hgBase.2.1⟩
  · intro hgPrime G hGPos hGSep
    exact rootQuotientPrimeBasis_subset_of_word_separates
      hr hGPos hGSep hgPrime

/-- Set-valued form of the fixed-horizon forced-core theorem. -/
theorem rootQuotient_forcedCore_eq_primeBasis
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    {g : ℕ | RootQuotientGeneratorForced r N h g} =
      RootQuotientPrimeBasis N := by
  ext g
  exact rootQuotientGeneratorForced_iff_primeBasis hr hh

/-- For horizons at least two, a least primitive presentation exists exactly
when the forced core itself is realizable as a separating presentation.

This pinpoints the intermediate no-least phase: all valid presentations share
the same prime core, but their intersection is not itself valid. -/
theorem exists_least_separating_iff_forcedCore_separates
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) := by
  constructor
  · rintro ⟨G, hLeast⟩
    rcases hLeast with ⟨hGPos, hGSep, hMinimal⟩
    have hPrimeSub : RootQuotientPrimeBasis N ⊆ G :=
      rootQuotientPrimeBasis_subset_of_word_separates hr hGPos hGSep
    have hGSubPrime : G ⊆ RootQuotientPrimeBasis N := by
      intro g hg
      apply (rootQuotientGeneratorForced_iff_primeBasis hr hh).1
      intro H hHPos hHSep
      exact hMinimal hHPos hHSep hg
    have hEq : G = RootQuotientPrimeBasis N :=
      Set.Subset.antisymm hGSubPrime hPrimeSub
    rw [hEq] at hGSep
    exact hGSep
  · intro hPrimeSep
    refine ⟨RootQuotientPrimeBasis N,
      rootQuotientPrimeBasis_positive, hPrimeSep, ?_⟩
    intro H hHPos hHSep
    exact rootQuotientPrimeBasis_subset_of_word_separates
      hr hHPos hHSep

/-- Equivalent negative form: the no-least phase is exactly failure of the
forced prime core to separate at the available horizon. -/
theorem no_least_separating_iff_forcedCore_not_separating
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      ¬SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) := by
  exact not_congr (exists_least_separating_iff_forcedCore_separates hr hh)

end EnterpriseMath.Quotient
