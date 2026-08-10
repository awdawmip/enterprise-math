import EnterpriseMath.Quotient.RootQuotientCompilerFiltration
import Mathlib.Algebra.Order.Floor.Div
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact relative compiler depth between two `Omega`-filtration presentations.

The lower-level ISA has per-instruction capacity `k`; the higher-level target
presentation exposes semantic rank only up to `min(j,L_r(N))`.  Ceiling
division therefore gives the least number of lower-level instructions needed
in the worst case. -/
def rootQuotientOmegaFiltrationCompilerDepth
    (r N k j : ℕ) : ℕ :=
  rootQuotientOmegaFiltrationExposedRank r N j ⌈/⌉ k

/-- Exact metric characterization: the relative compiler depth is at most `h`
iff `G_k` actually compiles `G_j` within `h` instructions. -/
theorem rootQuotientOmegaFilteredBasis_compilesWithin_iff_compilerDepth_le
    {r N k j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) ↔
      rootQuotientOmegaFiltrationCompilerDepth r N k j ≤ h := by
  rw [rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
    hr hN hkPos]
  rw [rootQuotientOmegaFiltrationCompilerDepth]
  rw [ceilDiv_le_iff_le_mul (by omega)]

/-- The exact relative compiler depth is attained. -/
theorem rootQuotientOmegaFilteredBasis_compiles_at_exact_compilerDepth
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
      (rootQuotientOmegaFiltrationCompilerDepth r N k j)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j) := by
  exact
    (rootQuotientOmegaFilteredBasis_compilesWithin_iff_compilerDepth_le
      (r := r) (N := N) (k := k) (j := j)
      (h := rootQuotientOmegaFiltrationCompilerDepth r N k j)
      hr hN hkPos).2 le_rfl

/-- No smaller depth can implement the target filtration presentation. -/
theorem rootQuotientOmegaFiltrationCompilerDepth_minimal
    {r N k j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hCompile : RootQuotientAlphabetCompilesWithin
      h
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j)) :
    rootQuotientOmegaFiltrationCompilerDepth r N k j ≤ h := by
  exact
    (rootQuotientOmegaFilteredBasis_compilesWithin_iff_compilerDepth_le
      hr hN hkPos).1 hCompile

/-- Exact compiler depth from an `Omega`-capacity-`k` presentation all the way
to the canonical semantic ISA. -/
def rootQuotientSemanticCompilerDepth
    (r N k : ℕ) : ℕ :=
  rootQuotientPrimeHorizon r N ⌈/⌉ k

/-- `G_k` compiles the semantic ISA within `h` iff its exact semantic compiler
depth is at most `h`. -/
theorem rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff_compilerDepth_le
    {r N k h : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientNontrivialPowerFreeBasis r N) ↔
      rootQuotientSemanticCompilerDepth r N k ≤ h := by
  rw [rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff hr hkPos]
  rw [rootQuotientSemanticCompilerDepth]
  rw [ceilDiv_le_iff_le_mul (by omega)]

/-- The semantic compiler depth is attained exactly. -/
theorem rootQuotientOmegaFilteredBasis_compiles_semantic_at_exact_depth
    {r N k : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
      (rootQuotientSemanticCompilerDepth r N k)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
  exact
    (rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff_compilerDepth_le
      (r := r) (N := N) (k := k)
      (h := rootQuotientSemanticCompilerDepth r N k)
      hr hkPos).2 le_rfl

/-- Multiplicative triangle inequality for staged compilation through another
`Omega` presentation.

A staging layer can reorganize storage or implementation structure, but it
cannot beat the exact direct worst-case depth after accounting for expansion at
both compiler stages. -/
theorem rootQuotientSemanticCompilerDepth_le_staged_product
    {r N k j : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hjPos : 1 ≤ j) :
    rootQuotientSemanticCompilerDepth r N k ≤
      rootQuotientOmegaFiltrationCompilerDepth r N k j *
        rootQuotientSemanticCompilerDepth r N j := by
  let a := rootQuotientOmegaFiltrationCompilerDepth r N k j
  let b := rootQuotientSemanticCompilerDepth r N j
  have hKJ : RootQuotientAlphabetCompilesWithin
      a
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientOmegaFilteredBasis r N j) := by
    dsimp [a]
    exact rootQuotientOmegaFilteredBasis_compiles_at_exact_compilerDepth
      hr hN hkPos
  have hJSem : RootQuotientAlphabetCompilesWithin
      b
      (RootQuotientOmegaFilteredBasis r N j)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
    dsimp [b]
    exact rootQuotientOmegaFilteredBasis_compiles_semantic_at_exact_depth
      (by omega) hjPos
  have hKSemBA : RootQuotientAlphabetCompilesWithin
      (b * a)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientNontrivialPowerFreeBasis r N) :=
    rootQuotientAlphabetCompilesWithin_trans hJSem hKJ
  have hKSem : RootQuotientAlphabetCompilesWithin
      (a * b)
      (RootQuotientOmegaFilteredBasis r N k)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
    simpa [Nat.mul_comm] using hKSemBA
  have hMin :=
    (rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff_compilerDepth_le
      (r := r) (N := N) (k := k) (h := a * b)
      (by omega) hkPos).1 hKSem
  simpa [a, b] using hMin

/-- The prime compiler metric is the unit-capacity semantic compiler depth. -/
theorem rootQuotientSemanticCompilerDepth_one
    {r N : ℕ} :
    rootQuotientSemanticCompilerDepth r N 1 =
      rootQuotientPrimeHorizon r N := by
  simp [rootQuotientSemanticCompilerDepth, Nat.ceilDiv_eq_add_pred_div]

end EnterpriseMath.Quotient
