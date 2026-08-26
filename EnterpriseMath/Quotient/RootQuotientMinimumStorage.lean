import EnterpriseMath.Quotient.RootQuotientAlphabetNormalization
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A normalized finite primitive alphabet admissible for storage optimization. -/
def RootQuotientFiniteStorageSeparator
    (r N h : ℕ) (G : Set ℕ) : Prop :=
  G ⊆ RootQuotientNontrivialPowerFreeBasis r N ∧
  G.Finite ∧
  PositiveRootQuotientGenerators G ∧
  SeparatesRootQuotientWordsUpTo r N h G

/-- The canonical nontrivial semantic basis is finite. -/
theorem rootQuotientNontrivialPowerFreeBasis_finite
    {r N : ℕ} :
    (RootQuotientNontrivialPowerFreeBasis r N).Finite := by
  apply Set.finite_Icc.subset
  intro b hb
  exact ⟨hb.1, hb.2.1⟩

/-- At every positive word horizon, the finite-storage feasible family is nonempty. -/
theorem exists_rootQuotientFiniteStorageSeparator
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    ∃ G : Set ℕ, RootQuotientFiniteStorageSeparator r N h G := by
  refine ⟨RootQuotientNontrivialPowerFreeBasis r N,
    Set.Subset.rfl,
    rootQuotientNontrivialPowerFreeBasis_finite,
    rootQuotientNontrivialPowerFreeBasis_positive, ?_⟩
  exact separatesRootQuotientWordsUpTo_mono_horizon hh
    (rootQuotientNontrivialPowerFreeBasis_separates_at_one hr)

/-- Cardinalities attained by normalized finite separating primitive alphabets. -/
def RootQuotientStorageCardinalities
    (r N h : ℕ) : Set ℕ :=
  {m : ℕ | ∃ G : Set ℕ,
    RootQuotientFiniteStorageSeparator r N h G ∧ G.ncard = m}

/-- Minimum primitive-type storage cardinality at fixed horizon. -/
noncomputable def rootQuotientMinimumStorageSize
    (r N h : ℕ) : ℕ :=
  sInf (RootQuotientStorageCardinalities r N h)

/-- The storage-cardinality set is nonempty at every positive horizon. -/
theorem rootQuotientStorageCardinalities_nonempty
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    (RootQuotientStorageCardinalities r N h).Nonempty := by
  obtain ⟨G, hG⟩ := exists_rootQuotientFiniteStorageSeparator hr hh
  exact ⟨G.ncard, G, hG, rfl⟩

/-- The minimum storage cardinality is actually attained by a normalized finite
separator; it is not merely an infimum. -/
theorem exists_rootQuotientMinimumStorageSeparator
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    ∃ G : Set ℕ,
      RootQuotientFiniteStorageSeparator r N h G ∧
      G.ncard = rootQuotientMinimumStorageSize r N h := by
  have hMem :
      rootQuotientMinimumStorageSize r N h ∈
        RootQuotientStorageCardinalities r N h := by
    exact Nat.sInf_mem (rootQuotientStorageCardinalities_nonempty hr hh)
  exact hMem

/-- The minimum storage size is no larger than any attained normalized finite
separator cardinality. -/
theorem rootQuotientMinimumStorageSize_le_normalized
    {r N h : ℕ} {G : Set ℕ}
    (hG : RootQuotientFiniteStorageSeparator r N h G) :
    rootQuotientMinimumStorageSize r N h ≤ G.ncard := by
  apply Nat.sInf_le
  exact ⟨G, hG, rfl⟩

/-- Every finite positive separator can be semantically normalized without
increasing storage cardinality. -/
theorem exists_normalized_storage_separator_le
    {r N h : ℕ} {H : Set ℕ}
    (hr : 1 ≤ r)
    (hHFinite : H.Finite)
    (hHPos : PositiveRootQuotientGenerators H)
    (hHSep : SeparatesRootQuotientWordsUpTo r N h H) :
    ∃ G : Set ℕ,
      RootQuotientFiniteStorageSeparator r N h G ∧
      G.ncard ≤ H.ncard := by
  let G := RootQuotientSemanticNormalization r N H
  have hGSubH : G ⊆ H := by
    dsimp [G]
    exact rootQuotientSemanticNormalization_subset
  have hGFinite : G.Finite := hHFinite.subset hGSubH
  have hGPos : PositiveRootQuotientGenerators G := by
    dsimp [G]
    exact rootQuotientSemanticNormalization_positive hHPos
  have hGSep : SeparatesRootQuotientWordsUpTo r N h G := by
    dsimp [G]
    exact rootQuotient_separator_normalize_to_semanticBasis hr hHPos hHSep
  have hGSemantic : G ⊆ RootQuotientNontrivialPowerFreeBasis r N := by
    intro g hg
    exact hg.2
  have hCard : G.ncard ≤ H.ncard :=
    Set.ncard_le_ncard hGSubH hHFinite
  exact ⟨G, ⟨hGSemantic, hGFinite, hGPos, hGSep⟩, hCard⟩

/-- Global minimum-cardinality theorem.

At every positive horizon, a finite primitive alphabet of minimum cardinality
exists.  This remains true even in the intermediate regime where no
inclusion-least alphabet exists. -/
theorem rootQuotientMinimumStorageSeparator_global_minimum
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    ∃ G : Set ℕ,
      RootQuotientFiniteStorageSeparator r N h G ∧
      G.ncard = rootQuotientMinimumStorageSize r N h ∧
      ∀ {H : Set ℕ},
        H.Finite →
        PositiveRootQuotientGenerators H →
        SeparatesRootQuotientWordsUpTo r N h H →
        G.ncard ≤ H.ncard := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator hr hh
  refine ⟨G, hG, hGCard, ?_⟩
  intro H hHFinite hHPos hHSep
  obtain ⟨H', hH', hH'Card⟩ :=
    exists_normalized_storage_separator_le hr hHFinite hHPos hHSep
  have hMinLe : rootQuotientMinimumStorageSize r N h ≤ H'.ncard :=
    rootQuotientMinimumStorageSize_le_normalized hH'
  rw [hGCard]
  exact hMinLe.trans hH'Card

/-- Minimum-cardinality existence is strictly weaker than inclusion-leastness:
in the intermediate phase a global finite storage optimum still exists even
though no inclusion-least primitive alphabet exists. -/
theorem minimum_storage_exists_without_inclusion_least
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    (∃ G : Set ℕ,
      RootQuotientFiniteStorageSeparator r N h G ∧
      ∀ {H : Set ℕ},
        H.Finite →
        PositiveRootQuotientGenerators H →
        SeparatesRootQuotientWordsUpTo r N h H →
        G.ncard ≤ H.ncard) ∧
    ¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G := by
  constructor
  · obtain ⟨G, hG, _hCard, hGlobal⟩ :=
      rootQuotientMinimumStorageSeparator_global_minimum
        (r := r) (N := N) (h := h) (by omega) (by omega)
    exact ⟨G, hG, hGlobal⟩
  · exact no_least_separating_rootQuotientAlphabet_of_intermediate_horizon
      hr hh hBelow

end EnterpriseMath.Quotient
