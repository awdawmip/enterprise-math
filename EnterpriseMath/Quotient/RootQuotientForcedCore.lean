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

end EnterpriseMath.Quotient
