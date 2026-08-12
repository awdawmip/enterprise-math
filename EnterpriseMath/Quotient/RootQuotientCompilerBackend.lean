import EnterpriseMath.Quotient.RootQuotientCompilerOrder
import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import EnterpriseMath.Quotient.RootQuotientForcedCore
import EnterpriseMath.Quotient.RootQuotientLeastPhase
import EnterpriseMath.Quotient.RootQuotientMinimumStorage
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Compilation is contravariantly monotone in the target alphabet: a compiler
for a larger target ISA automatically compiles every sub-ISA. -/
theorem rootQuotientAlphabetCompilesWithin_mono_target
    {H G T : Set ℕ} {h : ℕ}
    (hGT : G ⊆ T)
    (hCompile : RootQuotientAlphabetCompilesWithin h H T) :
    RootQuotientAlphabetCompilesWithin h H G := by
  intro g hg
  exact hCompile g (hGT hg)

/-- Compilation is covariantly monotone in the implementation alphabet: adding
lower-level primitive instructions cannot hurt compilation depth. -/
theorem rootQuotientAlphabetCompilesWithin_mono_implementation
    {H K G : Set ℕ} {h : ℕ}
    (hHK : H ⊆ K)
    (hCompile : RootQuotientAlphabetCompilesWithin h H G) :
    RootQuotientAlphabetCompilesWithin h K G := by
  intro g hg
  obtain ⟨w, hwLen, hwH, hProd⟩ := hCompile g hg
  refine ⟨w, hwLen, ?_, hProd⟩
  intro a ha
  exact hHK (hwH a ha)

/-- The bounded prime core is a universal backend for every normalized
presentation: at the exact prime compiler horizon it can implement any
subalphabet of the canonical semantic ISA. -/
theorem rootQuotientPrimeBasis_compiles_every_normalizedAlphabet_at_exactHorizon
    {r N : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hGNormalized : G ⊆ RootQuotientNontrivialPowerFreeBasis r N) :
    RootQuotientAlphabetCompilesWithin
      (rootQuotientPrimeHorizon r N)
      (RootQuotientPrimeBasis N) G := by
  apply rootQuotientAlphabetCompilesWithin_mono_target hGNormalized
  exact rootQuotientPrimeBasis_compiles_semanticBasis_at_exact_horizon
    (by omega)

/-- In the intermediate no-least phase, every normalized feasible
presentation contains the same prime forced core, while that core itself
misses the requested latency budget.  Nevertheless the prime core still
implements every normalized presentation at the larger exact compiler depth
`L_r(N)`.

This is the precise "infeasible meet / valid backend" phenomenon behind the
failure of an inclusion-least presentation. -/
theorem intermediate_phase_prime_core_is_infeasible_universal_backend
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    (¬SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeBasis N)) ∧
      (∀ G : Set ℕ,
        RootQuotientFiniteStorageSeparator r N h G →
        RootQuotientPrimeBasis N ⊆ G ∧
        RootQuotientAlphabetCompilesWithin
          (rootQuotientPrimeHorizon r N)
          (RootQuotientPrimeBasis N) G) := by
  constructor
  · intro hPrimeSep
    have hMin := rootQuotientPrimeHorizon_minimal_of_separates
      (r := r) (N := N) (h := h) (by omega) hPrimeSep
    omega
  · intro G hG
    constructor
    · exact rootQuotientPrimeBasis_subset_of_word_separates
        hr hG.2.2.1 hG.2.2.2
    · exact rootQuotientPrimeBasis_compiles_every_normalizedAlphabet_at_exactHorizon
        hr hG.1

/-- The forced core becomes a feasible presentation exactly when the requested
execution budget reaches its compiler depth to the semantic specification. -/
theorem rootQuotientPrimeCore_feasible_iff_backendDepth_le
    {r N h : ℕ}
    (hr : 2 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) ↔
      rootQuotientPrimeHorizon r N ≤ h :=
  rootQuotientPrimeBasis_separates_iff_horizon_le (by omega)

end EnterpriseMath.Quotient
