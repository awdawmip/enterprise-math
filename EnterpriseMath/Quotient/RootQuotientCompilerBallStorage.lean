import EnterpriseMath.Quotient.RootQuotientCompilerExpansionGeometry
import EnterpriseMath.Quotient.RootQuotientMinimumStorage
import EnterpriseMath.Quotient.RootQuotientStorageDepthPareto
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A normalized finite presentation lying in the directed compiler ball of
radius `h` around the canonical semantic specification. -/
def RootQuotientFiniteCompilerBallPresentation
    (r N h : ℕ) (G : Set ℕ) : Prop :=
  G ⊆ RootQuotientNontrivialPowerFreeBasis r N ∧
  G.Finite ∧
  PositiveRootQuotientGenerators G ∧
  rootQuotientCompilerExpansion
      G (RootQuotientNontrivialPowerFreeBasis r N) ≤ (h : ℕ∞)

/-- At positive radius, finite compiler-ball presentations are exactly the
normalized finite separating presentations used by the storage optimizer. -/
theorem finiteCompilerBallPresentation_iff_finiteStorageSeparator
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    RootQuotientFiniteCompilerBallPresentation r N h G ↔
      RootQuotientFiniteStorageSeparator r N h G := by
  constructor
  · intro hG
    refine ⟨hG.1, hG.2.1, hG.2.2.1, ?_⟩
    exact
      (rootQuotientCompilerExpansion_to_semanticBasis_le_iff_separates
        (r := r) (N := N) (h := h) (G := G)
        hr hh hG.2.2.1).1 hG.2.2.2
  · intro hG
    refine ⟨hG.1, hG.2.1, hG.2.2.1, ?_⟩
    exact
      (rootQuotientCompilerExpansion_to_semanticBasis_le_iff_separates
        (r := r) (N := N) (h := h) (G := G)
        hr hh hG.2.2.1).2 hG.2.2.2

/-- Cardinalities realized inside a finite compiler ball. -/
def RootQuotientCompilerBallStorageCardinalities
    (r N h : ℕ) : Set ℕ :=
  {m : ℕ | ∃ G : Set ℕ,
    RootQuotientFiniteCompilerBallPresentation r N h G ∧
    G.ncard = m}

/-- Minimum finite presentation cardinality inside the directed compiler ball. -/
noncomputable def rootQuotientCompilerBallMinimumStorage
    (r N h : ℕ) : ℕ :=
  sInf (RootQuotientCompilerBallStorageCardinalities r N h)

/-- At every positive horizon, the compiler-ball cardinality spectrum is
literally the existing finite-storage cardinality spectrum. -/
theorem compilerBallStorageCardinalities_eq_finiteStorageCardinalities
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    RootQuotientCompilerBallStorageCardinalities r N h =
      RootQuotientFiniteStorageCardinalities r N h := by
  ext m
  constructor
  · rintro ⟨G, hG, hCard⟩
    exact ⟨G,
      (finiteCompilerBallPresentation_iff_finiteStorageSeparator hr hh).1 hG,
      hCard⟩
  · rintro ⟨G, hG, hCard⟩
    exact ⟨G,
      (finiteCompilerBallPresentation_iff_finiteStorageSeparator hr hh).2 hG,
      hCard⟩

/-- Exact geometric interpretation of true minimum storage.

`S_r(N,h)` is the minimum finite dictionary cardinality among normalized
presentations lying inside compiler-expansion radius `h` of the canonical
semantic specification. -/
theorem rootQuotientCompilerBallMinimumStorage_eq_minimumStorageSize
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientCompilerBallMinimumStorage r N h =
      rootQuotientMinimumStorageSize r N h := by
  unfold rootQuotientCompilerBallMinimumStorage
  unfold rootQuotientMinimumStorageSize
  rw [compilerBallStorageCardinalities_eq_finiteStorageCardinalities hr hh]

/-- The compiler-ball minimum is attained. -/
theorem exists_minimumCompilerBallPresentation
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    ∃ G : Set ℕ,
      RootQuotientFiniteCompilerBallPresentation r N h G ∧
      G.ncard = rootQuotientCompilerBallMinimumStorage r N h := by
  obtain ⟨G, hG, hCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) hr hh
  refine ⟨G,
    (finiteCompilerBallPresentation_iff_finiteStorageSeparator hr hh).2 hG,
    ?_⟩
  rw [rootQuotientCompilerBallMinimumStorage_eq_minimumStorageSize hr hh]
  exact hCard

/-- Two-resource feasibility is exactly the existence of a presentation of
cardinality at most `s` inside compiler radius `h`. -/
theorem rootQuotientStorageDepthFeasible_iff_exists_in_compilerBall
    {r N s h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    RootQuotientStorageDepthFeasible r N s h ↔
      ∃ G : Set ℕ,
        RootQuotientFiniteCompilerBallPresentation r N h G ∧
        G.ncard ≤ s := by
  constructor
  · rintro ⟨G, hG, hCard⟩
    exact ⟨G,
      (finiteCompilerBallPresentation_iff_finiteStorageSeparator hr hh).2 hG,
      hCard⟩
  · rintro ⟨G, hG, hCard⟩
    exact ⟨G,
      (finiteCompilerBallPresentation_iff_finiteStorageSeparator hr hh).1 hG,
      hCard⟩

/-- Pareto duality in geometric language: the minimum storage curve is the
minimum cardinality inside nested compiler balls, while the dual depth curve is
the smallest ball radius containing a presentation under the storage budget. -/
theorem rootQuotientCompilerBallPareto_duality
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s)
    (hh : 1 ≤ h) :
    rootQuotientMinimumHorizonAtStorage r N s ≤ h ↔
      rootQuotientCompilerBallMinimumStorage r N h ≤ s := by
  rw [rootQuotientCompilerBallMinimumStorage_eq_minimumStorageSize
    (by omega) hh]
  exact rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
    hr hPrimeBudget hh

end EnterpriseMath.Quotient
