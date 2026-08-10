import EnterpriseMath.Quotient.RootQuotientAlphabetNormalization
import EnterpriseMath.Quotient.RootQuotientCapacity
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Quantitative collective-capacity necessity.

If `c*h` is still below the exact prime-only horizon, every separating
primitive alphabet must contain a genuinely useful semantic instruction whose
prime-factor count exceeds `c`.

The conclusion is deliberately about a generator inside the canonical semantic
down-set, not an irrelevant oversized instruction: semantic normalization
removes such noise before applying the universal capacity lower bound. -/
theorem exists_semantic_generator_above_capacity_threshold
    {r N h c : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hBelow : c * h < rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    ∃ g : ℕ,
      g ∈ G ∧
      g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      c < rootQuotientPrimeFactorCount g := by
  let G' := RootQuotientSemanticNormalization r N G
  have hG'Pos : PositiveRootQuotientGenerators G' :=
    rootQuotientSemanticNormalization_positive hGPos
  have hG'Sep : SeparatesRootQuotientWordsUpTo r N h G' := by
    dsimp [G']
    exact rootQuotient_separator_normalize_to_semanticBasis hr hGPos hSep
  by_contra hNoLarge
  have hCap : RootQuotientFactorCapacity c G' := by
    intro g hgG'
    by_contra hNot
    have hcLt : c < rootQuotientPrimeFactorCount g := by omega
    exact hNoLarge ⟨g, hgG'.1, hgG'.2, hcLt⟩
  have hBound : rootQuotientPrimeHorizon r N ≤ c * h :=
    rootQuotientPrimeHorizon_le_capacity_mul_horizon
      hr hG'Pos hCap hG'Sep
  omega

/-- The intermediate-phase composite-necessity theorem is the capacity-one
instance of the quantitative threshold law. -/
theorem exists_composite_semantic_generator_of_horizon_below_prime
    {r N h : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hBelow : h < rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    ∃ g : ℕ,
      g ∈ G ∧
      g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      ¬g.Prime := by
  obtain ⟨g, hgG, hgSemantic, hgCount⟩ :=
    exists_semantic_generator_above_capacity_threshold
      (r := r) (N := N) (h := h) (c := 1)
      (by omega) (by simpa using hBelow) hGPos hSep
  have hgNotPrime : ¬g.Prime := by
    intro hgPrime
    have hgOne : rootQuotientPrimeFactorCount g = 1 := by
      rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hgPrime]
      simp
    omega
  exact ⟨g, hgG, hgSemantic, hgNotPrime⟩

/-- More generally, any proposed uniform per-instruction capacity `c` below the
resource hyperbola is impossible for a separator. -/
theorem not_factorCapacity_of_capacity_mul_horizon_lt_primeHorizon
    {r N h c : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hBelow : c * h < rootQuotientPrimeHorizon r N)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    ¬RootQuotientFactorCapacity c G := by
  intro hCap
  have hBound := rootQuotientPrimeHorizon_le_capacity_mul_horizon
    hr hGPos hCap hSep
  omega

end EnterpriseMath.Quotient
