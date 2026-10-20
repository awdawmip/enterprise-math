import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A witness scheme chooses, for every required nontrivial semantic target,
one multiplicative factor word of length at most `h` using only canonical
semantic instructions and compiling exactly to that target. -/
def RootQuotientSemanticWitnessScheme
    (r N h : ℕ) (F : ℕ → List ℕ) : Prop :=
  ∀ b : ℕ,
    b ∈ RootQuotientNontrivialPowerFreeBasis r N →
      (F b).length ≤ h ∧
      RootQuotientWordOver
        (RootQuotientNontrivialPowerFreeBasis r N) (F b) ∧
      b = rootQuotientWordProduct (F b)

/-- Composite primitive types actually used by a witness scheme, after
removing the mandatory prime core. -/
def RootQuotientWitnessUsedCompositeSet
    (r N : ℕ) (F : ℕ → List ℕ) : Set ℕ :=
  {g : ℕ | ∃ b : ℕ,
    b ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
    g ∈ F b ∧
    g ∉ RootQuotientPrimeBasis N}

/-- The used-composite union of any semantic witness scheme is finite. -/
theorem witnessUsedCompositeSet_finite
    {r N h : ℕ} {F : ℕ → List ℕ}
    (hF : RootQuotientSemanticWitnessScheme r N h F) :
    (RootQuotientWitnessUsedCompositeSet r N F).Finite := by
  apply rootQuotientNontrivialPowerFreeBasis_finite.subset
  intro g hg
  obtain ⟨b, hb, hgWord, _hgNotPrime⟩ := hg
  exact (hF b hb).2.1 g hgWord

/-- The used-composite union of a witness scheme is a valid optional macro
family. -/
theorem witnessUsedCompositeSet_is_macroFamily
    {r N h : ℕ} {F : ℕ → List ℕ}
    (hF : RootQuotientSemanticWitnessScheme r N h F) :
    RootQuotientCompositeMacroFamily
      r N (RootQuotientWitnessUsedCompositeSet r N F) := by
  intro g hg
  obtain ⟨b, hb, hgWord, hgNotPrime⟩ := hg
  exact ⟨(hF b hb).2.1 g hgWord, hgNotPrime⟩

/-- A semantic witness scheme is sufficient: adjoining exactly the composite
factors that occur somewhere in the chosen witness words to the prime core
recompiles every semantic instruction. -/
theorem witnessScheme_gives_compositeMacroPresentation
    {r N h : ℕ} {F : ℕ → List ℕ}
    (hr : 2 ≤ r)
    (hF : RootQuotientSemanticWitnessScheme r N h F) :
    RootQuotientCompositeMacroPresentation
      r N h (RootQuotientWitnessUsedCompositeSet r N F) := by
  let U := RootQuotientWitnessUsedCompositeSet r N F
  have hUFinite : U.Finite := by
    dsimp [U]
    exact witnessUsedCompositeSet_finite hF
  have hUFamily : RootQuotientCompositeMacroFamily r N U := by
    dsimp [U]
    exact witnessUsedCompositeSet_is_macroFamily hF
  have hPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ U) := by
    intro g hg
    rcases hg with hgPrime | hgU
    · exact hgPrime.1.one_le
    · have hgSemantic := (hUFamily hgU).1
      omega
  have hCompile : RootQuotientAlphabetCompilesWithin
      h
      (RootQuotientPrimeBasis N ∪ U)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
    intro b hb
    refine ⟨F b, (hF b hb).1, ?_, (hF b hb).2.2⟩
    intro g hgWord
    have hgSemantic := (hF b hb).2.1 g hgWord
    by_cases hgPrime : g.Prime
    · exact Or.inl ⟨hgPrime, hgSemantic.2.1⟩
    · exact Or.inr ⟨b, hb, hgWord, by
        intro hgPrimeBasis
        exact hgPrime hgPrimeBasis.1⟩
  have hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ U) :=
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ U)
      (by omega) hPos).2 hCompile
  exact ⟨hUFinite, hUFamily, hSep⟩

/-- Conversely, every feasible optional macro family admits semantic witness
words whose total used-composite union is contained in that family. -/
theorem exists_witnessScheme_usedComposite_subset_of_macroPresentation
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S) :
    ∃ F : ℕ → List ℕ,
      RootQuotientSemanticWitnessScheme r N h F ∧
      RootQuotientWitnessUsedCompositeSet r N F ⊆ S := by
  classical
  have hPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hS.2.1 hgS).1
      omega
  have hCompile : RootQuotientAlphabetCompilesWithin
      h
      (RootQuotientPrimeBasis N ∪ S)
      (RootQuotientNontrivialPowerFreeBasis r N) :=
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hPos).1 hS.2.2
  let F : ℕ → List ℕ := fun b =>
    if hb : b ∈ RootQuotientNontrivialPowerFreeBasis r N then
      Classical.choose (hCompile b hb)
    else
      []
  have hFUnion : ∀ b : ℕ,
      b ∈ RootQuotientNontrivialPowerFreeBasis r N →
        (F b).length ≤ h ∧
        RootQuotientWordOver (RootQuotientPrimeBasis N ∪ S) (F b) ∧
        b = rootQuotientWordProduct (F b) := by
    intro b hb
    dsimp [F]
    rw [dif_pos hb]
    exact Classical.choose_spec (hCompile b hb)
  have hFSemantic : RootQuotientSemanticWitnessScheme r N h F := by
    intro b hb
    have hW := hFUnion b hb
    refine ⟨hW.1, ?_, hW.2.2⟩
    intro g hgWord
    have hgUnion := hW.2.1 g hgWord
    rcases hgUnion with hgPrime | hgS
    · exact rootQuotientPrimeBasis_subset_semanticBasis hr hgPrime
    · exact (hS.2.1 hgS).1
  have hUsedSub : RootQuotientWitnessUsedCompositeSet r N F ⊆ S := by
    intro g hg
    obtain ⟨b, hb, hgWord, hgNotPrime⟩ := hg
    have hgUnion := (hFUnion b hb).2.1 g hgWord
    rcases hgUnion with hgPrime | hgS
    · exact (hgNotPrime hgPrime).elim
    · exact hgS
  exact ⟨F, hFSemantic, hUsedSub⟩

/-- Cardinalities attained by used-composite unions of semantic witness
schemes. -/
def RootQuotientWitnessUnionMacroCardinalities
    (r N h : ℕ) : Set ℕ :=
  {m : ℕ | ∃ F : ℕ → List ℕ,
    RootQuotientSemanticWitnessScheme r N h F ∧
    (RootQuotientWitnessUsedCompositeSet r N F).ncard = m}

/-- Minimum cardinality of a used-composite union over all witness schemes. -/
noncomputable def rootQuotientMinimumWitnessUnionMacroCount
    (r N h : ℕ) : ℕ :=
  sInf (RootQuotientWitnessUnionMacroCardinalities r N h)

/-- Witness-union cardinalities are nonempty for every positive horizon: the
literal one-letter semantic witness scheme always works. -/
theorem witnessUnionMacroCardinalities_nonempty
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    (RootQuotientWitnessUnionMacroCardinalities r N h).Nonempty := by
  let F : ℕ → List ℕ := fun b => [b]
  have hF : RootQuotientSemanticWitnessScheme r N h F := by
    intro b hb
    refine ⟨by simp [F, hh], ?_, ?_⟩
    · intro g hg
      simp [F] at hg
      subst g
      exact hb
    · simp [F, rootQuotientWordProduct]
  exact ⟨(RootQuotientWitnessUsedCompositeSet r N F).ncard,
    F, hF, rfl⟩

/-- The minimum witness-union macro count is attained. -/
theorem exists_minimumWitnessUnionScheme
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    ∃ F : ℕ → List ℕ,
      RootQuotientSemanticWitnessScheme r N h F ∧
      (RootQuotientWitnessUsedCompositeSet r N F).ncard =
        rootQuotientMinimumWitnessUnionMacroCount r N h := by
  have hMem : rootQuotientMinimumWitnessUnionMacroCount r N h ∈
      RootQuotientWitnessUnionMacroCardinalities r N h :=
    Nat.sInf_mem (witnessUnionMacroCardinalities_nonempty hh)
  exact hMem

/-- The minimum-union oracle is no larger than any concrete witness scheme. -/
theorem rootQuotientMinimumWitnessUnionMacroCount_le
    {r N h : ℕ} {F : ℕ → List ℕ}
    (hF : RootQuotientSemanticWitnessScheme r N h F) :
    rootQuotientMinimumWitnessUnionMacroCount r N h ≤
      (RootQuotientWitnessUsedCompositeSet r N F).ncard := by
  apply Nat.sInf_le
  exact ⟨F, hF, rfl⟩

/-- Exact general minimum-union theorem.

The minimum number of optional composite macro types at any positive horizon is
exactly the minimum cardinality of the union of composite factors used by one
chosen semantic witness word per required target.  This is the formal general
counterpart of the executable monotone-DNF / witness-hyperedge solver; the
penultimate semiprime set-cover theorem is a special collapse of this model. -/
theorem rootQuotientMinimumCompositeMacroCount_eq_minimumWitnessUnionMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientMinimumWitnessUnionMacroCount r N h := by
  apply Nat.le_antisymm
  · obtain ⟨F, hF, hFCard⟩ := exists_minimumWitnessUnionScheme hh
    have hMacro := witnessScheme_gives_compositeMacroPresentation hr hF
    have hLe := rootQuotientMinimumCompositeMacroCount_le hMacro
    rw [hFCard] at hLe
    exact hLe
  · obtain ⟨S, hS, hSCard⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr hh
    obtain ⟨F, hF, hUsedSub⟩ :=
      exists_witnessScheme_usedComposite_subset_of_macroPresentation hr hS
    have hUnionLe := rootQuotientMinimumWitnessUnionMacroCount_le hF
    have hUsedFinite := witnessUsedCompositeSet_finite hF
    have hUsedCardLe :
        (RootQuotientWitnessUsedCompositeSet r N F).ncard ≤ S.ncard :=
      Set.ncard_le_ncard hUsedSub hS.1
    rw [hSCard] at hUsedCardLe
    exact hUnionLe.trans hUsedCardLe

/-- Full true storage in minimum-union coordinates. -/
theorem rootQuotientMinimumStorageSize_eq_prime_add_minimumWitnessUnionMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard +
        rootQuotientMinimumWitnessUnionMacroCount r N h := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  rw [rootQuotientMinimumCompositeMacroCount_eq_minimumWitnessUnionMacroCount
    hr hh]

end EnterpriseMath.Quotient
