import EnterpriseMath.Quotient.RootQuotientAlphabetNormalization
import EnterpriseMath.Quotient.RootQuotientForcedCore
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Below the exact prime horizon, every separating primitive alphabet must
contain at least one genuinely useful composite semantic instruction.

This statement is stronger than merely saying that primes alone fail: semantic
normalization removes identities and irrelevant generators, so the required
composite can be chosen inside the canonical bounded power-free down-set. -/
theorem exists_composite_semantic_generator_of_intermediate_separator
    {r N h : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    ∃ g : ℕ,
      g ∈ G ∧
      g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      ¬g.Prime := by
  let G' := RootQuotientSemanticNormalization r N G
  have hG'Pos : PositiveRootQuotientGenerators G' :=
    rootQuotientSemanticNormalization_positive hGPos
  have hG'Sep : SeparatesRootQuotientWordsUpTo r N h G' := by
    dsimp [G']
    exact rootQuotient_separator_normalize_to_semanticBasis
      (by omega) hGPos hSep
  by_cases hComposite : ∃ g : ℕ, g ∈ G' ∧ ¬g.Prime
  · obtain ⟨g, hgG', hgNotPrime⟩ := hComposite
    exact ⟨g, hgG'.1, hgG'.2, hgNotPrime⟩
  · have hG'SubPrime : G' ⊆ RootQuotientPrimeBasis N := by
      intro g hgG'
      have hgPrime : g.Prime := by
        by_contra hgNotPrime
        exact hComposite ⟨g, hgG', hgNotPrime⟩
      exact ⟨hgPrime, hgG'.2.2.1⟩
    have hPrimeSubG' : RootQuotientPrimeBasis N ⊆ G' :=
      rootQuotientPrimeBasis_subset_of_word_separates
        hr hG'Pos hG'Sep
    have hEq : G' = RootQuotientPrimeBasis N :=
      Set.Subset.antisymm hG'SubPrime hPrimeSubG'
    rw [hEq] at hG'Sep
    have hNecessary : rootQuotientPrimeHorizon r N ≤ h :=
      rootQuotientPrimeHorizon_minimal_of_separates (by omega) hG'Sep
    omega

/-- No particular composite semantic instruction is pointwise forced once two
composition slots are available: deleting that composite from the full
semantic basis still leaves a separator. -/
theorem exists_separator_omitting_each_composite_semantic_generator
    {r N h g : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgNotPrime : ¬g.Prime) :
    ∃ G : Set ℕ,
      PositiveRootQuotientGenerators G ∧
      SeparatesRootQuotientWordsUpTo r N h G ∧
      g ∉ G := by
  refine ⟨RootQuotientCompositeOmissionBasis r N g,
    rootQuotientCompositeOmissionBasis_positive,
    rootQuotientCompositeOmissionBasis_separates
      (by omega) hgSemantic.1 hgSemantic.2.1 hgNotPrime hh, ?_⟩
  intro hg
  exact hg.2 rfl

/-- Collective-necessity theorem for the intermediate phase.

Additional composite capacity is globally necessary in every separator, while
no named composite semantic generator is individually necessary. -/
theorem composite_capacity_collectively_necessary_but_none_forced
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    (∀ {G : Set ℕ},
      PositiveRootQuotientGenerators G →
      SeparatesRootQuotientWordsUpTo r N h G →
      ∃ g : ℕ,
        g ∈ G ∧
        g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
        ¬g.Prime) ∧
    (∀ g : ℕ,
      g ∈ RootQuotientNontrivialPowerFreeBasis r N →
      ¬g.Prime →
      ∃ G : Set ℕ,
        PositiveRootQuotientGenerators G ∧
        SeparatesRootQuotientWordsUpTo r N h G ∧
        g ∉ G) := by
  constructor
  · intro G hGPos hGSep
    exact exists_composite_semantic_generator_of_intermediate_separator
      hr hh hBelow hGPos hGSep
  · intro g hgSemantic hgNotPrime
    exact exists_separator_omitting_each_composite_semantic_generator
      hr hh hgSemantic hgNotPrime

end EnterpriseMath.Quotient
